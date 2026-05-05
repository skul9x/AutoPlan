import sys
import os

# Add parent directory to sys.path to allow importing from root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import patch_utils
import pyautogui
import time
from bot_core import BotCore

def create_test_image(path=os.path.join(os.path.dirname(__file__), "fixtures", "test_icon.png")):
    """
    Tạo một file ảnh mẫu bằng cách chụp một vùng nhỏ trên màn hình.
    """
    print("Creating test image from screen...")
    # Chụp một vùng 50x50 tại góc trên bên trái (0,0)
    # Lưu ý: Nếu màn hình đen hoặc không có gì, nó có thể khó tìm lại.
    # Nhưng đây là cách nhanh nhất để có một file ảnh thực tế từ màn hình này.
    screenshot = pyautogui.screenshot(region=(100, 100, 50, 50))
    screenshot.save(path)
    print(f"Test image saved to {path}")

def test_bot():
    bot = BotCore(confidence=0.9)
    test_image = os.path.join(os.path.dirname(__file__), "fixtures", "test_icon.png")
    
    # Đảm bảo file test tồn tại
    if not os.path.exists(test_image):
        create_test_image(test_image)
    
    print("Starting test in 3 seconds... Move your mouse away!")
    time.sleep(3)
    
    # 1. Test locate and click
    success = bot.locate_and_click(test_image)
    if success:
        print("Locate and click test: SUCCESS")
    else:
        print("Locate and click test: FAILED (Image might not be visible or match)")

    # 2. Test type command
    print("\nTesting type_command...")
    bot.type_command("/path/to/test_file.md")
    print("Type command test: DONE (Check if the text appeared somewhere)")

if __name__ == "__main__":
    test_bot()
