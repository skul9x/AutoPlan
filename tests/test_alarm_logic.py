import unittest
from unittest.mock import MagicMock, patch
import os
import sys

# Add the current directory to sys.path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine import AutomationEngine

class TestAlarmLogic(unittest.TestCase):
    def setUp(self):
        self.log_callback = MagicMock()
        self.finished_callback = MagicMock()
        # Mock BotCore to avoid actual automation during tests
        with patch('engine.BotCore'):
            self.engine = AutomationEngine(self.log_callback, self.finished_callback)
        self.engine.is_running = True
        
        # Patch time.sleep to speed up tests
        self.sleep_patcher = patch('time.sleep', return_value=None)
        self.mock_sleep = self.sleep_patcher.start()

    def tearDown(self):
        self.sleep_patcher.stop()

    @patch('os.path.exists')
    def test_alarm_enabled_and_path_provided(self, mock_exists):
        # Setup
        mock_exists.return_value = True
        # Mock the existing alarm instance
        self.engine.alarm = MagicMock()
        self.engine.alarm.is_playing = False
        self.engine.is_running = True
        
        # Test parameters
        folder = "/tmp"
        md_files = ["test.md"]
        icon = "icon.png"
        alarm_path = "alarm.mp3"
        
        # Run loop directly
        # Mock is_icon_visible to return True (found icon) then False (icon disappeared)
        with patch.object(self.engine.bot, 'is_icon_visible', side_effect=[True, False]):
            self.engine._run_loop(folder, md_files, icon, None, None, True, alarm_path)
        
        # Verify
        self.engine.alarm.start_alarm.assert_called_once_with(alarm_path)
        self.log_callback.assert_any_call("Đang kích hoạt báo thức... (Nhấn F12 để dừng)")

    def test_alarm_disabled(self):
        # Setup
        self.engine.alarm = MagicMock()
        
        # Test parameters
        folder = "/tmp"
        md_files = ["test.md"]
        icon = "icon.png"
        alarm_path = "alarm.mp3"
        
        # Run loop
        with patch.object(self.engine.bot, 'is_icon_visible', side_effect=[True, False]):
            self.engine._run_loop(folder, md_files, icon, None, None, False, alarm_path)
        
        # Verify
        self.engine.alarm.start_alarm.assert_not_called()

    def test_alarm_enabled_but_no_path(self):
        # Setup
        self.engine.alarm = MagicMock()
        
        # Test parameters
        folder = "/tmp"
        md_files = ["test.md"]
        icon = "icon.png"
        alarm_path = ""
        
        # Run loop
        with patch.object(self.engine.bot, 'is_icon_visible', side_effect=[True, False]):
            self.engine._run_loop(folder, md_files, icon, None, None, True, alarm_path)
        
        # Verify
        self.engine.alarm.start_alarm.assert_not_called()

if __name__ == '__main__':
    unittest.main()
