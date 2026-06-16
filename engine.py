import threading
import time
import os
from bot_core import BotCore
from alarm_manager import AlarmManager


class AutomationEngine:
    def __init__(self, log_callback, on_finished_callback):
        self.log_callback = log_callback
        self.on_finished_callback = on_finished_callback
        self.bot = BotCore()
        self.alarm = AlarmManager(stop_callback=self._on_alarm_stop)
        self.is_running = False
        self.thread = None

    def _on_alarm_stop(self):
        self.log_callback("Báo thức đã dừng (F12).")
        self.is_running = False
        self.on_finished_callback()

    def start(self, folder_path, md_files, icon_path, region=None, error_icon_path=None, alarm_enabled=False, alarm_path="", template_prompt=""):
        if self.is_running:
            return
        
        self.is_running = True
        self.thread = threading.Thread(
            target=self._run_loop, 
            args=(folder_path, md_files, icon_path, region, error_icon_path, alarm_enabled, alarm_path, template_prompt),
            daemon=True
        )
        self.thread.start()

    def stop(self):
        self.is_running = False
        self.alarm.stop_alarm()
        self.log_callback("Dừng bot theo yêu cầu người dùng.")

    def _run_loop(self, folder_path, md_files, icon_path, region, error_icon_path, alarm_enabled, alarm_path, template_prompt):
        try:
            self.log_callback("Bot sẽ bắt đầu sau 2 giây. Vui lòng chuyển sang cửa sổ đích...")
            time.sleep(2)
            
            is_first_file = True
            for file_name in md_files:
                if not self.is_running:
                    break

                abs_path = os.path.join(folder_path, file_name)
                
                region_info = f" trong vùng {region}" if region else ""
                error_info = " (có kiểm tra ảnh lỗi)" if error_icon_path else ""
                
                if is_first_file:
                    self.log_callback(f"Lần đầu chạy: Bỏ qua quét màn hình, thực thi ngay cho: {file_name}")
                else:
                    self.log_callback(f"Đang chờ icon hiển thị{region_info}{error_info} để xử lý: {file_name}")
                    
                    # Bước 1: Đợi icon với logic quét 2 ảnh
                    while self.is_running:
                        # 1a. Nếu có ảnh lỗi → kiểm tra trước
                        if error_icon_path and self.bot.is_icon_visible(error_icon_path, region=region):
                            self.log_callback("⚠️ Phát hiện ảnh lỗi! Quét lại ngay...")
                            time.sleep(0.1)
                            continue  # Quay lại đầu vòng lặp, KHÔNG quét ảnh bình thường
                        
                        # 1b. Không thấy ảnh lỗi (hoặc không có ảnh lỗi) → quét ảnh bình thường
                        if self.bot.is_icon_visible(icon_path, region=region):
                            break  # Thoát vòng lặp → bắt đầu flow làm việc
                        
                        time.sleep(0.1)
                
                if not self.is_running:
                    break
                
                self.log_callback(f"Thực thi sequence cho {file_name}...")
                
                # Bước 2: Thực thi chuỗi phím tắt
                self.bot.input_template_sequence(abs_path, template_prompt)
                
                # Bước 3: Đợi icon biến mất để tránh trigger nhầm file cũ
                # Hoặc có thể dùng một khoảng nghỉ ngắn tùy thuộc vào tốc độ phản hồi của IDE
                self.log_callback("Đang chờ icon biến mất (hoặc hoàn tất)...")
                time.sleep(2) # Nghỉ tối thiểu 2s để phím tắt được ghi nhận
                
                while self.is_running:
                    if not self.bot.is_icon_visible(icon_path, region=region):
                        break
                    time.sleep(1)
                
                self.log_callback(f"Đã xử lý xong {file_name}, sẵn sàng cho file tiếp theo.")
                is_first_file = False

            if self.is_running:
                self.log_callback("Hoàn thành xử lý tất cả các file.")
                if alarm_enabled and alarm_path:
                    self.log_callback("Đang kích hoạt báo thức... (Nhấn F12 để dừng)")
                    self.alarm.start_alarm(alarm_path)
                    # Giữ thread sống cho đến khi báo thức dừng hoặc bot bị dừng
                    while self.is_running and self.alarm.is_playing:
                        time.sleep(0.5)
            else:
                self.log_callback("Bot đã dừng lại.")
                
        except Exception as e:
            self.log_callback(f"ERROR: Lỗi hệ thống trong engine: {str(e)}")
        finally:
            self.is_running = False
            self.on_finished_callback()
