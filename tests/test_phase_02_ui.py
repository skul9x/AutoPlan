import unittest
from unittest.mock import MagicMock, patch
import os
import sys

# Add current dir to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Mock tkinter before importing AppUI
tk_mock = MagicMock()
tk_mock.TkVersion = 8.6
sys.modules['tkinter'] = tk_mock
sys.modules['tkinter.ttk'] = MagicMock()
sys.modules['tkinter.filedialog'] = MagicMock()
sys.modules['tkinter.scrolledtext'] = MagicMock()

import ui_components

class TestPhase02UI(unittest.TestCase):
    def setUp(self):
        self.root = MagicMock()
        # Mock BooleanVar to return a mock object
        tk_mock.BooleanVar.return_value = MagicMock()
        
    @patch('settings_manager.load_settings')
    @patch('settings_manager.save_settings')
    def test_ui_elements_presence(self, mock_save, mock_load):
        # Mock load_settings to return empty dict
        mock_load.return_value = {}
        
        # Instantiate AppUI
        ui = ui_components.AppUI(self.root)
        
        # Check if error_icon_path attribute exists
        self.assertTrue(hasattr(ui, 'error_icon_path'))
        
    @patch('settings_manager.save_settings')
    def test_save_settings_includes_error_icon(self, mock_save):
        ui = ui_components.AppUI(self.root)
        
        # Mock entry values
        ui.folder_path = MagicMock()
        ui.folder_path.get.return_value = "/folder"
        ui.error_icon_path = MagicMock()
        ui.error_icon_path.get.return_value = "/error/icon.png"
        ui.icon_path = MagicMock()
        ui.icon_path.get.return_value = "/normal/icon.png"
        ui.alarm_enabled = MagicMock()
        ui.alarm_enabled.get.return_value = False
        ui.alarm_path_entry = MagicMock()
        ui.alarm_path_entry.get.return_value = ""
        
        # Execute
        ui.save_current_settings()
        
        # Verify
        mock_save.assert_called_once()
        saved_data = mock_save.call_args[0][0]
        self.assertEqual(saved_data["error_icon_path"], "/error/icon.png")

    @patch('settings_manager.load_settings')
    def test_load_settings_populates_error_icon(self, mock_load):
        # Mock settings
        mock_load.return_value = {
            "error_icon_path": "/path/to/error.png"
        }
        
        # Mock validate_path to return the path if it exists
        with patch('ui_components.AppUI.validate_path', side_effect=lambda x: x):
            ui = ui_components.AppUI(self.root)
            
            # Since load_and_apply_settings is called in __init__
            # Check if delete/insert were called on error_icon_path
            ui.error_icon_path.delete.assert_called()
            ui.error_icon_path.insert.assert_called_with(0, "/path/to/error.png")

    @patch('os.path.exists')
    def test_on_start_passes_error_icon(self, mock_exists):
        mock_exists.return_value = True
        ui = ui_components.AppUI(self.root)
        
        # Mock engine
        ui.engine = MagicMock()
        
        # Mock UI inputs
        ui.folder_path.get.return_value = "/folder"
        ui.icon_path.get.return_value = "/icon.png"
        ui.error_icon_path.get.return_value = "/error.png"
        ui.file_listbox.curselection.return_value = [0]
        ui.file_listbox.get.return_value = "file1.md"
        
        # Execute
        ui.on_start()
        
        # Verify engine.start call
        ui.engine.start.assert_called_once()
        kwargs = ui.engine.start.call_args[1]
        self.assertEqual(kwargs['error_icon_path'], "/error.png")

if __name__ == "__main__":
    unittest.main()
