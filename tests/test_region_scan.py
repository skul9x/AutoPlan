import unittest
from unittest.mock import patch, MagicMock
from engine import AutomationEngine
from bot_core import BotCore
from ui_components import AppUI
import tkinter as tk

class TestRegionScan(unittest.TestCase):
    def setUp(self):
        self.log_mock = MagicMock()
        self.finished_mock = MagicMock()
        self.engine = AutomationEngine(self.log_mock, self.finished_mock)
        self.bot = BotCore()

    @patch('time.sleep')
    @patch('bot_core.BotCore.is_icon_visible')
    @patch('bot_core.BotCore.input_template_sequence')
    def test_scenario_icon_outside_then_inside(self, mock_sequence, mock_visible, mock_sleep):
        """
        Kịch bản: Chọn vùng A -> Để icon ở vùng B (invisible in A) -> Bot đợi -> Icon vào vùng A -> Bot chạy.
        """
        # Giả lập: 
        # Lần 1: Không thấy (icon ở vùng B)
        # Lần 2: Không thấy (icon vẫn ở vùng B)
        # Lần 3: Thấy (icon đã vào vùng A)
        # Lần 4: Không thấy (để thoát vòng lặp chờ icon biến mất)
        mock_visible.side_effect = [False, False, True, False]
        
        region_a = (100, 100, 200, 200)
        md_files = ["test.md"]
        
        self.engine.is_running = True
        # Chạy vòng lặp xử lý 1 file
        self.engine._run_loop("/fake/path", md_files, "icon.png", region_a, None, False, "", "")
        
        # Kiểm tra:
        # 1. is_icon_visible được gọi ít nhất 3 lần để đợi và nhận diện
        self.assertGreaterEqual(mock_visible.call_count, 3)
        
        # 2. Tất cả các lần gọi đều phải truyền đúng region_a
        for call in mock_visible.call_args_list:
            self.assertEqual(call[1].get('region'), region_a)
            
        # 3. input_template_sequence chỉ được gọi KHI icon xuất hiện (sau lần False, False, True)
        mock_sequence.assert_called_once_with("/fake/path/test.md", "")
        
        self.log_mock.assert_any_call("Đang chờ icon hiển thị trong vùng (100, 100, 200, 200) để xử lý: test.md")

    def test_ui_reset_region(self):
        """Kiểm tra tính năng reset vùng về mặc định."""
        root = tk.Tk()
        # Mock dependencies of AppUI
        with patch('hotkey.HotkeyHandler.start'):
            app = AppUI(root)
            
            # Giả lập đã chọn vùng
            app.scan_region = (10, 10, 50, 50)
            app.region_label.config(text="Current Region: (10, 10, 50, 50)")
            
            # Thực hiện reset
            app.on_reset_region()
            
            # Kiểm tra
            self.assertIsNone(app.scan_region)
            self.assertEqual(app.region_label.cget("text"), "Current Region: Full Screen (Default)")
        
        root.destroy()

    @patch('bot_core.pyautogui.locateOnScreen')
    def test_invalid_region_handling(self, mock_locate):
        """Kiểm tra bot_core không crash với vùng chọn không hợp lệ (ví dụ quá nhỏ)."""
        mock_locate.return_value = None # PyAutoGUI thường trả về None nếu không tìm thấy hoặc lỗi vùng
        
        # Trường hợp vùng 0,0,0,0
        result = self.bot.is_icon_visible("icon.png", region=(0, 0, 0, 0))
        self.assertFalse(result)
        
        # Trường hợp None
        result = self.bot.is_icon_visible("icon.png", region=None)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
