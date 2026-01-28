import pygame
import os

# Initialize Pygame
pygame.init()

# Define paths and IDs
assets_dir = "assets"
tags = {
    "tag16_05_00015.png": 15,
    "tag16_05_00016.png": 16,
    "tag16_05_00017.png": 17,
    "tag16_05_00018.png": 18,
    "tag16_05_00001.png": 1
}

# Ensure directory exists
if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)

# Create placeholder images
size = 64
font = pygame.font.SysFont('Arial', 40)

for filename, tag_id in tags.items():
    surf = pygame.Surface((size, size))
    surf.fill((255, 255, 255)) # White background
    
    # Black border
    pygame.draw.rect(surf, (0, 0, 0), surf.get_rect(), 8)
    
    # Draw ID
    text = font.render(str(tag_id), True, (0, 0, 0))
    text_rect = text.get_rect(center=(size//2, size//2))
    surf.blit(text, text_rect)
    
    # Save
    pygame.image.save(surf, os.path.join(assets_dir, filename))
    print(f"Generated {filename}")

pygame.quit()
