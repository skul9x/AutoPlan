import unittest
from unittest.mock import MagicMock, patch
import os
import time
import sys

# Mock dependencies that might be missing in the environment
mock_modules = [
    'pyautogui', 
    'pyscreeze', 
    'PIL', 
    'PIL.Image', 
    'cv2', 
    'keyboard',
    'patch_utils'
]
for module_name in mock_modules:
    sys.modules[module_name] = MagicMock()

from engine import AutomationEngine

class TestEngineLogic(unittest.TestCase):
    def setUp(self):
        self.log_mock = MagicMock()
        self.finished_mock = MagicMock()
        self.engine = AutomationEngine(self.log_mock, self.finished_mock)
        # Mock BotCore instance inside engine
        self.engine.bot = MagicMock()

    @patch('time.sleep')
    def test_run_loop_sequence(self, mock_sleep):
        # Mocking file list and paths
        md_files = ["file1.md"]
        folder_path = "/test/folder"
        icon_path = "icon.png"
        
        # Scenario: 
        # 1. First check: icon not visible
        # 2. Second check: icon visible
        # 3. Third check (after sequence): icon still visible
        # 4. Fourth check: icon disappeared
        self.engine.bot.is_icon_visible.side_effect = [False, True, True, False]
        self.engine.is_running = True
        
        # Execute the loop (normally this runs in a thread, but we call _run_loop directly for testing)
        self.engine._run_loop(folder_path, md_files, icon_path, None, None, False, "", "")
        
        # Verify sequence of calls
        # Wait for icon visible: called twice (False, True)
        # Input sequence: called once
        # Wait for icon disappear: called twice (True, False)
        self.assertEqual(self.engine.bot.is_icon_visible.call_count, 4)
        
        abs_path = os.path.join(folder_path, "file1.md")
        self.engine.bot.input_template_sequence.assert_called_once_with(abs_path, "")
        
        # Verify logs
        self.log_mock.assert_any_call("Đang chờ icon hiển thị để xử lý: file1.md")
        self.log_mock.assert_any_call("Icon đã xuất hiện! Thực thi sequence cho file1.md...")
        self.log_mock.assert_any_call("Đang chờ icon biến mất (hoặc hoàn tất)...")
        self.log_mock.assert_any_call("Hoàn thành xử lý tất cả các file.")

    @patch('time.sleep')
    def test_stop_during_wait_visible(self, mock_sleep):
        md_files = ["file1.md"]
        self.engine.bot.is_icon_visible.return_value = False
        self.engine.is_running = True
        
        # Simulate stopping the engine after 2 checks
        # We use a wrapper function for side_effect to track calls
        self.call_count = 0
        def side_effect(path, **kwargs):
            self.call_count += 1
            if self.call_count >= 2:
                self.engine.is_running = False
            return False
        
        self.engine.bot.is_icon_visible.side_effect = side_effect
        
        self.engine._run_loop("/path", md_files, "icon.png", None, None, False, "", "")
        
        # Should have broken out of the loop
        self.engine.bot.input_template_sequence.assert_not_called()
        self.log_mock.assert_any_call("Bot đã dừng lại.")

if __name__ == '__main__':
    unittest.main()
