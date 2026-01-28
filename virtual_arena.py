import pygame
import sys
import math
import numpy as np
import cv2
import time

try:
    import pyvirtualcam
    has_pyvirtualcam = True
except ImportError:
    has_pyvirtualcam = False
    print("Warning: pyvirtualcam not installed. Virtual Camera mode unavailable.")

# 初始化 Pygame
pygame.init()

def monitor_cameras():
    """
    Independent thread to scan and display camera feeds.
    Helps user verify which camera index is receiving the simulation.
    """
    print("\n[Monitor] Starting Camera Monitor...")
    print("[Monitor] Press 'q' in the monitor window to cycle cameras.")
    
    cv2.namedWindow("Camera Monitor", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Camera Monitor", 320, 240)
    
    camera_index = 0
    max_cameras = 5
    cap = None
    
    while True:
        if cap is None:
            cap = cv2.VideoCapture(camera_index)
            if not cap.isOpened():
                camera_index = (camera_index + 1) % max_cameras
                cap = None
                time.sleep(0.1)
                continue
            print(f"[Monitor] Checking Camera #{camera_index}...")
        
        ret, frame = cap.read()
        if ret:
            # Overlay info
            text = f"Cam #{camera_index}"
            cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, "Press SPACE to Lock", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
            cv2.putText(frame, "Press 'n' for Next", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
            
            cv2.imshow("Camera Monitor", frame)
        
        key = cv2.waitKey(50) & 0xFF
        
        # 'n' or 'q' to next camera
        if key == ord('n') or key == ord('q'):
            cap.release()
            cap = None
            camera_index = (camera_index + 1) % max_cameras
        
        # SPACE to keep monitoring this camera (do nothing loop)
        elif key == 32: 
            pass
            
        # Check if main thread died (optional, but good for cleanup)
        if not threading.main_thread().is_alive():
            break

    if cap:
        cap.release()
    cv2.destroyAllWindows()

# 屏幕设置 (放大 2 倍)
SCALE_FACTOR = 2
MARGIN = 40 * SCALE_FACTOR
ARENA_WIDTH = 320 * SCALE_FACTOR
ARENA_HEIGHT = 240 * SCALE_FACTOR
SCREEN_WIDTH = ARENA_WIDTH + 2 * MARGIN
SCREEN_HEIGHT = ARENA_HEIGHT + 2 * MARGIN

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Virtual Arena Simulation (Scaled)")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WALL_COLOR = (50, 50, 50) 
BOX_COLOR = (139, 69, 19) 
TARGET_COLOR = (0, 255, 0)

# 资源路径
TAG_15_PATH = "assets/tag16_05_00015.png"
TAG_16_PATH = "assets/tag16_05_00016.png"
TAG_17_PATH = "assets/tag16_05_00017.png"
TAG_18_PATH = "assets/tag16_05_00018.png"
TAG_CAR_PATH = "assets/tag16_05_00001.png"

# 场地设置 (单位 px, 1px=1cm * SCALE)
BORDER_WIDTH = 5 * SCALE_FACTOR
TAG_SIZE = 20 * SCALE_FACTOR
BOX_SIZE = 20 * SCALE_FACTOR

# 小车设置
CAR_WIDTH = 30 * SCALE_FACTOR
CAR_HEIGHT = 15 * SCALE_FACTOR
CAR_SPEED = 2 * SCALE_FACTOR
ROTATION_SPEED = 3

def load_image(path, size=None):
    try:
        img = pygame.image.load(path)
        if size:
            img = pygame.transform.scale(img, size)
        return img
    except pygame.error:
        # 如果图片不存在，返回一个简单的占位符
        surf = pygame.Surface(size if size else (32, 32))
        surf.fill(BLACK)
        pygame.draw.rect(surf, WHITE, surf.get_rect(), 1)
        # 绘制X
        pygame.draw.line(surf, WHITE, (0, 0), size if size else (32, 32))
        pygame.draw.line(surf, WHITE, (0, size[1] if size else 32), (size[0] if size else 32, 0))
        return surf

# 全局资源字典
assets = {}

class Box:
    def __init__(self, x, y, is_target=False):
        self.x = x
        self.y = y
        self.width = BOX_SIZE
        self.height = BOX_SIZE
        self.is_target = is_target
        self.active = True # 如果是箱子且推到位了，或者目标被触发了，可能消失
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw(self, surface):
        if not self.active:
            return
        
        rect = self.get_rect()
        # 转换坐标 (加上 Margin)
        draw_rect = rect.move(MARGIN, MARGIN)
        
        if self.is_target:
            # 目标点：空心绿色框
            pygame.draw.rect(surface, TARGET_COLOR, draw_rect, 2)
            # 画个叉
            pygame.draw.line(surface, TARGET_COLOR, draw_rect.topleft, draw_rect.bottomright, 2)
            pygame.draw.line(surface, TARGET_COLOR, draw_rect.topright, draw_rect.bottomleft, 2)
        else:
            # 箱子：实心棕色
            pygame.draw.rect(surface, BOX_COLOR, draw_rect)
            pygame.draw.rect(surface, BLACK, draw_rect, 1) # 边框

class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        
    def draw(self, surface):
        draw_rect = self.rect.move(MARGIN, MARGIN)
        pygame.draw.rect(surface, WALL_COLOR, draw_rect)

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0  # 0度朝右, 90度朝下
        self.width = CAR_WIDTH
        self.height = CAR_HEIGHT
        
    def move(self, keys):
        # 预测下一帧位置
        next_x = self.x
        next_y = self.y
        next_angle = self.angle
        
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            next_x += CAR_SPEED * math.cos(math.radians(self.angle))
            next_y += CAR_SPEED * math.sin(math.radians(self.angle))
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            next_x -= CAR_SPEED * math.cos(math.radians(self.angle))
            next_y -= CAR_SPEED * math.sin(math.radians(self.angle))
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            next_angle -= ROTATION_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            next_angle += ROTATION_SPEED
            
        # 边界检查
        if 0 <= next_x <= ARENA_WIDTH and 0 <= next_y <= ARENA_HEIGHT:
            self.x = next_x
            self.y = next_y
        self.angle = next_angle
        
        # 强制约束在场地内
        self.x = max(0, min(self.x, ARENA_WIDTH))
        self.y = max(0, min(self.y, ARENA_HEIGHT))

    def draw(self, surface):
        # 创建一个小车的Surface，支持旋转
        car_surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        part_width = self.width / 3
        
        # 红色矩形
        pygame.draw.rect(car_surf, RED, (0, 0, part_width, self.height))
        
        # 中间Apriltag区域 (白色背景)
        pygame.draw.rect(car_surf, WHITE, (part_width, 0, part_width, self.height))
        
        # 绘制Apriltag (保持正方形，居中)
        tag_img = assets.get('car_tag')
        if tag_img:
            # 中间区域宽度是 part_width (10px)，高度是 self.height (15px)
            # 规则更新：Apriltag为15cm，但中间区域宽度只有10cm (30/3)。
            # 如果Apriltag是15cm，它将超出中间白色区域（10cm宽）。
            # 让我们仔细检查规则：
            # 标识牌 30x15cm。由红、Tag、黄组成。
            # 如果Tag是15cm宽，那么红和黄只剩下 (30-15)/2 = 7.5cm 宽。
            # 或者Tag区就是中间那一块？如果Tag是15cm，那么中间区域也应该是15cm？
            # 规则原文：标志由红色矩形、Apriltag码、黄色矩形组成。没说三等分。
            # 但如果Tag是15cm，且高度也是15cm（它是正方形），那么它就占了 15x15 的空间。
            # 整个板子 30x15。
            # 那么剩下的空间是 30-15 = 15cm。
            # 红和黄各分 7.5cm。
            # 布局应该是：[红7.5cm] [Tag 15cm] [黄7.5cm]
            
            # 更新布局参数
            tag_size = 15.0 # 15cm
            side_width = (self.width - tag_size) / 2.0 # (30-15)/2 = 7.5cm
            
            # 重绘整个背景以适应新比例
            car_surf.fill((0,0,0,0)) # 清空
            
            # 红色矩形 (左侧: 0 到 7.5)
            # 使用 math.ceil 确保覆盖接缝，或者直接用 float
            pygame.draw.rect(car_surf, RED, (0, 0, side_width, self.height))
            
            # 中间白色背景 (Tag区域: 7.5 到 22.5)
            # 注意：Rect 只接受整数，所以需要仔细处理浮点数转换，避免1px的缝隙或重叠
            # 红色：0 ~ 7
            # Tag：8 ~ 22 (15px)
            # 黄色：23 ~ 30
            
            red_w = int(side_width) # 7
            tag_w = int(tag_size)   # 15
            
            # 渲染策略：先画背景，再叠加Tag，避免任何缝隙问题
            
            # 1. 绘制背景 (红-白-黄)
            # 左侧红色 (0 ~ 7.5)
            red_rect = pygame.Rect(0, 0, int(side_width), self.height)
            pygame.draw.rect(car_surf, RED, red_rect)
            
            # 右侧黄色 (22.5 ~ 30)
            # 简化计算：从右边往回算，确保占满右侧
            yellow_width = int(side_width)
            yellow_x = self.width - yellow_width
            yellow_rect = pygame.Rect(yellow_x, 0, yellow_width, self.height)
            pygame.draw.rect(car_surf, YELLOW, yellow_rect)
            
            # 中间白色 (填充剩余空间)
            # 从 red_rect.right 到 yellow_rect.left
            white_x = red_rect.right
            white_width = yellow_rect.left - white_x
            white_rect = pygame.Rect(white_x, 0, white_width, self.height)
            pygame.draw.rect(car_surf, WHITE, white_rect)

            # 2. 叠加 Apriltag
            # 严格居中绘制，不依赖背景色块的边界
            tag_w = int(tag_size)
            tag_h = int(tag_size)
            scaled_tag = pygame.transform.scale(tag_img, (tag_w, tag_h))
            
            # 计算绝对居中位置
            center_x = self.width / 2
            center_y = self.height / 2
            tag_pos_x = center_x - (tag_w / 2)
            tag_pos_y = center_y - (tag_h / 2)
            
            car_surf.blit(scaled_tag, (int(tag_pos_x), int(tag_pos_y)))
            
        else:
             # Fallback: 简单的黑框
            pygame.draw.rect(car_surf, BLACK, (part_width + 2, 2, part_width - 4, self.height - 4))
        
        # 旋转小车
        rotated_car = pygame.transform.rotate(car_surf, -self.angle)
        rect = rotated_car.get_rect(center=(self.x + MARGIN, self.y + MARGIN))
        
        surface.blit(rotated_car, rect.topleft)

def draw_arena_markers(surface):
    # 绘制四个角的 Apriltag 模拟 (15, 16, 17, 18)
    # 规则：四个角的apriltag要位于中心
    # 意味着 Tag 的中心点应该对齐场地的角落 (0,0), (W,0), (W,H), (0,H)
    
    half_tag = TAG_SIZE / 2
    
    # 左上 (15) -> Center at (0, 0)
    # Draw at (0 - half, 0 - half) + MARGIN
    surface.blit(assets['tag15'], (MARGIN - half_tag, MARGIN - half_tag))
    
    # 右上 (16) -> Center at (W, 0)
    surface.blit(assets['tag16'], (MARGIN + ARENA_WIDTH - half_tag, MARGIN - half_tag))
    
    # 右下 (17) -> Center at (W, H)
    surface.blit(assets['tag17'], (MARGIN + ARENA_WIDTH - half_tag, MARGIN + ARENA_HEIGHT - half_tag))
    
    # 左下 (18) -> Center at (0, H)
    surface.blit(assets['tag18'], (MARGIN - half_tag, MARGIN + ARENA_HEIGHT - half_tag))

import threading

def main():
    clock = pygame.time.Clock()
    
    # 启动摄像头监控线程 (自动验证)
    # monitor_thread = threading.Thread(target=monitor_cameras, daemon=True)
    # monitor_thread.start()
    
    # 加载资源
    assets['tag15'] = load_image(TAG_15_PATH, (TAG_SIZE, TAG_SIZE))
    assets['tag16'] = load_image(TAG_16_PATH, (TAG_SIZE, TAG_SIZE))
    assets['tag17'] = load_image(TAG_17_PATH, (TAG_SIZE, TAG_SIZE))
    assets['tag18'] = load_image(TAG_18_PATH, (TAG_SIZE, TAG_SIZE))
    assets['car_tag'] = load_image(TAG_CAR_PATH) # 大小会在绘制时调整
    
    # 字体用于显示调试信息
    font = pygame.font.SysFont('Arial', 14 * SCALE_FACTOR)
 
    car = Car(ARENA_WIDTH // 2, ARENA_HEIGHT // 2)
    
    running = True
    
    # 尝试初始化虚拟摄像头 (保留作为可选项，如果需要)
    # Windows Camera App often requires standard resolutions like 640x480
    # VIRTUAL_CAM_WIDTH = 640
    # VIRTUAL_CAM_HEIGHT = 480
    
    cam = None
    use_virtual_cam = False

    # if has_pyvirtualcam: ... (Virtual Camera Code Removed)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        car.move(keys)
        
        # 绘制背景 (填充灰色)
        screen.fill(GRAY) 
        
        # 绘制黄色边界 (场地内)
        # 场地左上角现在是 (MARGIN, MARGIN)
        arena_rect = pygame.Rect(MARGIN, MARGIN, ARENA_WIDTH, ARENA_HEIGHT)
        
        # 绘制场地背景 (蓝色)
        pygame.draw.rect(screen, BLUE, arena_rect)
        
        # 绘制黄色边界 (覆盖在背景之上)
        pygame.draw.rect(screen, YELLOW, arena_rect, BORDER_WIDTH)
        
        # 绘制四个角的 Apriltag
        draw_arena_markers(screen)
        
        # 绘制小车
        car.draw(screen)
        
        # 显示调试信息 (小车真实坐标)
        debug_text = f"Car: ({int(car.x)}, {int(car.y)}) Angle: {int(car.angle)%360}"
        text_surf = font.render(debug_text, True, RED)
        screen.blit(text_surf, (10, 10))
        
        pygame.display.flip()
        
        # 更新网络推流帧 (已禁用)
        # frame = pygame.surfarray.array3d(screen)
        # ...
        
        clock.tick(60)

    # if use_virtual_cam:
    #     cam.close()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
