import cv2
import pyvirtualcam
from pyvirtualcam import PixelFormat

def list_cameras(max_check=10):
    print("Checking for available cameras...")
    available_cameras = []
    for i in range(max_check):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            # Try to read a frame
            ret, _ = cap.read()
            if ret:
                print(f"Camera index {i}: Available")
                available_cameras.append(i)
            else:
                print(f"Camera index {i}: Failed to read frame")
            cap.release()
        else:
            # print(f"Camera index {i}: Not available")
            pass
            
    return available_cameras

if __name__ == "__main__":
    print("--- Camera Discovery Tool ---")
    cams = list_cameras()
    
    print("\n--- Virtual Camera Info ---")
    try:
        # Check pyvirtualcam backends
        print("Checking pyvirtualcam backends...")
        # Note: pyvirtualcam doesn't have a direct 'list devices' method exposed easily,
        # but we can try to init and see what happens or catch the error which usually lists backends.
        
        # Try OBS specifically
        print("Attempting to connect to OBS Virtual Camera output...")
        try:
            with pyvirtualcam.Camera(width=640, height=480, fps=20) as cam:
                print(f"Success! Virtual Camera Device: {cam.device}")
                print(f"Backend: {cam.backend}")
        except Exception as e:
            print(f"Failed to initialize default virtual camera: {e}")
            
    except Exception as e:
        print(f"Error checking virtual camera: {e}")

    print("\n--- Instructions ---")
    print("1. If you see 'Camera index X: Available', that is a camera input (physical or virtual).")
    print("   You can use that index in your OpenCV code: cv2.VideoCapture(X)")
    print("2. If pyvirtualcam failed, ensure OBS Studio is installed and 'Start Virtual Camera' is clicked (if using OBS).")
    print("   Or ensure OBS-VirtualCam driver is registered.")
