import threading
import time
import os
from bot_core import BotCore

class AutomationEngine:
    def __init__(self, log_callback, on_finished_callback):
        self.log_callback = log_callback
        self.on_finished_callback = on_finished_callback
        self.bot = BotCore()
        self.is_running = False
        self.thread = None

    def start(self, folder_path, md_files, icon_path, region=None):
        if self.is_running:
            return
        
        self.is_running = True
        self.thread = threading.Thread(
            target=self._run_loop, 
            args=(folder_path, md_files, icon_path, region),
            daemon=True
        )
        self.thread.start()

    def stop(self):
        self.is_running = False
        self.log_callback("Dừng bot theo yêu cầu người dùng.")

    def _run_loop(self, folder_path, md_files, icon_path, region):
        try:
            self.log_callback("Bot sẽ bắt đầu sau 2 giây. Vui lòng chuyển sang cửa sổ đích...")
            time.sleep(2)
            
            for file_name in md_files:
                if not self.is_running:
                    break

                abs_path = os.path.join(folder_path, file_name)
                
                region_info = f" trong vùng {region}" if region else ""
                self.log_callback(f"Đang chờ icon hiển thị{region_info} để xử lý: {file_name}")
                
                # Bước 1: Đợi cho đến khi thấy Icon
                while self.is_running:
                    if self.bot.is_icon_visible(icon_path, region=region):
                        break
                    time.sleep(0.1) # Quét nhanh hơn trong test hoặc thực tế nếu cần, mặc định 0.1s cho mượt
                
                if not self.is_running:
                    break
                
                self.log_callback(f"Icon đã xuất hiện! Thực thi sequence cho {file_name}...")
                
                # Bước 2: Thực thi chuỗi phím tắt
                self.bot.input_vietcode_sequence(abs_path)
                
                # Bước 3: Đợi icon biến mất để tránh trigger nhầm file cũ
                # Hoặc có thể dùng một khoảng nghỉ ngắn tùy thuộc vào tốc độ phản hồi của IDE
                self.log_callback("Đang chờ icon biến mất (hoặc hoàn tất)...")
                time.sleep(2) # Nghỉ tối thiểu 2s để phím tắt được ghi nhận
                
                while self.is_running:
                    if not self.bot.is_icon_visible(icon_path, region=region):
                        break
                    time.sleep(1)
                
                self.log_callback(f"Đã xử lý xong {file_name}, sẵn sàng cho file tiếp theo.")

            if self.is_running:
                self.log_callback("Hoàn thành xử lý tất cả các file.")
            else:
                self.log_callback("Bot đã dừng lại.")
                
        except Exception as e:
            self.log_callback(f"ERROR: Lỗi hệ thống trong engine: {str(e)}")
        finally:
            self.is_running = False
            self.on_finished_callback()
