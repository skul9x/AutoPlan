import unittest
from unittest.mock import MagicMock, patch
import os
import sys

# Mock dependencies that might be missing in the environment
mock_modules = [
    'pyautogui', 
    'pyscreeze', 
    'PIL', 
    'PIL.Image', 
    'cv2', 
    'keyboard',
    'patch_utils',
    'pygame',
    'pygame.mixer',
    'pynput',
    'pynput.keyboard',
    'pyperclip',
    'mss'
]
for module_name in mock_modules:
    sys.modules[module_name] = MagicMock()

from engine import AutomationEngine

class TestFirstRunSkip(unittest.TestCase):
    def setUp(self):
        self.log_mock = MagicMock()
        self.finished_mock = MagicMock()
        self.engine = AutomationEngine(self.log_mock, self.finished_mock)
        self.engine.bot = MagicMock()

    @patch('time.sleep')
    def test_first_file_skips_scanning_subsequent_files_scan(self, mock_sleep):
        md_files = ["file1.md", "file2.md"]
        folder_path = "/test/folder"
        icon_path = "icon.png"
        
        # side_effect returns:
        # 1. False for file1.md wait-disappear check.
        # 2. True for file2.md wait-appear check.
        # 3. False for file2.md wait-disappear check.
        self.engine.bot.is_icon_visible.side_effect = [False, True, False]
        self.engine.is_running = True
        
        self.engine._run_loop(folder_path, md_files, icon_path, None, None, False, "", "")
        
        # Verify call count
        # file1.md wait-appear loop: 0 calls (skipped)
        # file1.md wait-disappear loop: 1 call
        # file2.md wait-appear loop: 1 call
        # file2.md wait-disappear loop: 1 call
        # Total = 3 calls
        self.assertEqual(self.engine.bot.is_icon_visible.call_count, 3)
        
        # Verify both sequences were run with correct paths
        self.assertEqual(self.engine.bot.input_template_sequence.call_count, 2)
        self.engine.bot.input_template_sequence.assert_any_call(
            os.path.join(folder_path, "file1.md"), ""
        )
        self.engine.bot.input_template_sequence.assert_any_call(
            os.path.join(folder_path, "file2.md"), ""
        )
        
        # Verify specific logs
        log_messages = [call[0][0] for call in self.log_mock.call_args_list]
        
        self.assertTrue(any("Lần đầu chạy: Bỏ qua quét màn hình, thực thi ngay cho: file1.md" in msg for msg in log_messages))
        self.assertTrue(any("Thực thi sequence cho file1.md..." in msg for msg in log_messages))
        self.assertTrue(any("Đang chờ icon hiển thị để xử lý: file2.md" in msg for msg in log_messages))
        self.assertTrue(any("Thực thi sequence cho file2.md..." in msg for msg in log_messages))
        self.assertTrue(any("Hoàn thành xử lý tất cả các file." in msg for msg in log_messages))

if __name__ == '__main__':
    unittest.main()
