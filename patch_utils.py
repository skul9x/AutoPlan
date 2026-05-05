import pyscreeze
from PIL import Image
import pyautogui

def patch_pyscreeze():
    try:
        import mss
        def mss_screenshot(region=None):
            with mss.mss() as sct:
                if region:
                    # mss uses {"top": y, "left": x, "width": w, "height": h}
                    monitor = {"top": region[1], "left": region[0], "width": region[2], "height": region[3]}
                    sct_img = sct.grab(monitor)
                else:
                    sct_img = sct.grab(sct.monitors[1])
                return Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        
        # Test if screenshot works
        try:
            pyautogui.screenshot()
        except Exception:
            print("Detected Linux screenshotting issue. Patching with mss...")
            pyscreeze.screenshot = mss_screenshot
            # Also patch pyautogui's reference if it exists
            pyautogui.screenshot = mss_screenshot
            
    except ImportError:
        print("mss not installed. Cannot patch screenshot.")

# Run patch immediately when imported
patch_pyscreeze()
