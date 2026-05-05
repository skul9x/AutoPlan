import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
import os
import sys

# Add the current directory to sys.path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ui_components
from alarm_manager import AlarmManager

class TestCenterAndAlarm(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the window

    def tearDown(self):
        self.root.destroy()

    @patch('ui_components.AutomationEngine')
    @patch('ui_components.HotkeyHandler')
    @patch('settings_manager.load_settings')
    def test_center_window_called(self, mock_load, mock_hotkey, mock_engine):
        # Mock settings to avoid file I/O
        mock_load.return_value = {}
        
        # Create AppUI
        with patch.object(ui_components.AppUI, 'center_window') as mock_center:
            app = ui_components.AppUI(self.root)
            mock_center.assert_called_once_with(650, 650)

    @patch('ui_components.AutomationEngine')
    @patch('ui_components.HotkeyHandler')
    @patch('settings_manager.load_settings')
    @patch('os.path.exists')
    def test_ui_passes_alarm_settings_to_engine(self, mock_exists, mock_load, mock_hotkey, mock_engine):
        # Setup mocks
        mock_load.return_value = {}
        mock_exists.return_value = True
        engine_instance = mock_engine.return_value
        
        # Create AppUI
        app = ui_components.AppUI(self.root)
        
        # Set UI values
        app.folder_path.insert(0, "/fake/folder")
        app.icon_path.insert(0, "/fake/icon.png")
        app.alarm_enabled.set(True)
        app.alarm_path_entry.insert(0, "/fake/alarm.mp3")
        
        # Mock Listbox selection
        app.file_listbox.insert(0, "file1.md")
        app.file_listbox.select_set(0)
        
        # Trigger on_start
        app.on_start()
        
        # Verify engine.start was called with correct alarm params
        engine_instance.start.assert_called_once()
        args, kwargs = engine_instance.start.call_args
        self.assertEqual(kwargs['alarm_enabled'], True)
        self.assertEqual(kwargs['alarm_path'], "/fake/alarm.mp3")

    @patch('pygame.mixer.music')
    @patch('pygame.mixer.init')
    @patch('pynput.keyboard.Listener')
    @patch('os.path.exists')
    def test_alarm_manager_start_stop(self, mock_exists, mock_listener, mock_init, mock_music):
        mock_exists.return_value = True
        manager = AlarmManager()
        
        # Test start
        manager.start_alarm("/fake/alarm.mp3")
        mock_music.load.assert_called_with("/fake/alarm.mp3")
        mock_music.play.assert_called_with(loops=-1)
        self.assertTrue(manager.is_playing)
        mock_listener.assert_called_once()
        
        # Test stop
        manager.stop_alarm()
        mock_music.stop.assert_called_once()
        self.assertFalse(manager.is_playing)
        mock_listener.return_value.stop.assert_called_once()

if __name__ == '__main__':
    unittest.main()
