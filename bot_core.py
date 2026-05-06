import patch_utils
import pyautogui
import time
import os
import tkinter as tk

class BotCore:
    def __init__(self, confidence=0.9):
        self.confidence = confidence
        # Disable pyautogui fail-safe if needed, but keeping it ON is safer
        pyautogui.FAILSAFE = True

    def locate_and_click(self, image_path, region=None):
        """
        Tìm kiếm hình ảnh trên màn hình và click vào tâm của nó.
        Sử dụng confidence để tăng độ chính xác (yêu cầu opencv-python).
        """
        print(f"Searching for image: {image_path} in region: {region}...")
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=self.confidence, region=region)
            if location:
                print(f"Found image at: {location}. Clicking...")
                pyautogui.click(location)
                return True
            else:
                print("Image not found on screen.")
                return False
        except Exception as e:
            print(f"Error locating image: {e}")
            return False

    def is_icon_visible(self, image_path, region=None):
        """
        Kiểm tra xem icon có xuất hiện trên màn hình hay không.
        Trả về True nếu thấy, False nếu không.
        """
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=self.confidence, region=region)
            return location is not None
        except Exception as e:
            print(f"Error checking visibility: {e}")
            return False

    def input_template_sequence(self, file_path, template_prompt):
        """
        Thực hiện chuỗi phím tắt và dán nội dung template.
        Sử dụng clipboard để dán chuỗi đã format nhằm tăng tốc độ và tránh treo.
        """
        print(f"Executing template sequence for: {file_path}")
        # Nhấn Ctrl + Shift + L
        time.sleep(0.68)
        pyautogui.hotkey('ctrl', 'shift', 'l')
        
        # Nghỉ 1.0 giây (giống trước để UI phản hồi)
        time.sleep(0.68)
        
        # Format lại template prompt: thay thế chuỗi {xxx} bằng file_path
        formatted_prompt = template_prompt.replace("{xxx}", file_path)
        
        # Sử dụng pyperclip để copy vào clipboard (ổn định hơn trên Linux)
        import pyperclip
        pyperclip.copy(formatted_prompt)
        
        # Nghỉ một chút trước khi dán để tránh xung đột trên Linux
        time.sleep(0.5)
        
        # Nhấn Ctrl + V để dán
        pyautogui.hotkey('ctrl', 'v')
        
        # Nghỉ 0.5 giây để IDE xử lý lệnh dán
        time.sleep(0.5) 
        
        # Nhấn Enter
        pyautogui.press('enter')

    def type_command(self, file_path):
        """
        Gõ lệnh /code <file_path> và nhấn Enter.
        """
        command = f"/code {file_path}"
        print(f"Typing command: {command}")
        pyautogui.write(command, interval=0.01)
        pyautogui.press('enter')
        time.sleep(0.5) # Chờ một chút sau khi nhấn Enter
