import sys
import os
import unittest
from unittest.mock import MagicMock, patch

# Add parent dir to sys.path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock tkinter and other dependencies before importing ui_components
import tkinter
mock_tk = MagicMock()
mock_tk.TkVersion = 8.6
sys.modules['tkinter'] = mock_tk
sys.modules['tkinter.ttk'] = MagicMock()
sys.modules['tkinter.filedialog'] = MagicMock()
sys.modules['tkinter.scrolledtext'] = MagicMock()

import ui_components
import settings_manager

class TestPhase02Loading(unittest.TestCase):
    def setUp(self):
        self.root = MagicMock()
        # Mocking required UI elements for AppUI init
        with patch('ui_components.HotkeyHandler'), \
             patch('ui_components.AutomationEngine'), \
             patch('ui_components.RegionSelector'):
            # We need to mock create_path_selector to avoid real tkinter calls
            with patch.object(ui_components.AppUI, 'create_path_selector'):
                self.ui = ui_components.AppUI(self.root)
                # Manually add the attributes that create_path_selector would have added
                self.ui.folder_path = MagicMock()
                self.ui.icon_path = MagicMock()
                self.ui.region_label = MagicMock()
                self.ui.file_listbox = MagicMock()

    def test_validate_path_valid(self):
        # Current file is a valid path
        current_file = os.path.abspath(__file__)
        self.assertEqual(self.ui.validate_path(current_file), os.path.normpath(current_file))

    def test_validate_path_invalid(self):
        self.assertEqual(self.ui.validate_path("/non/existent/path/here"), "")
        self.assertEqual(self.ui.validate_path("C:\\NonExistent\\Path"), "")

    def test_load_and_apply_settings(self):
        test_settings = {
            "mru_md_folder": os.path.dirname(os.path.abspath(__file__)),
            "mru_icon_link": os.path.abspath(__file__),
            "scan_region": [10, 20, 100, 200]
        }
        
        with patch('settings_manager.load_settings', return_value=test_settings), \
             patch.object(self.ui, 'update_file_list') as mock_update:
            
            self.ui.load_and_apply_settings()
            
            # Check if UI was populated
            # folder_path.insert(0, path)
            self.ui.folder_path.insert.assert_called_with(0, os.path.normpath(test_settings["mru_md_folder"]))
            self.ui.icon_path.insert.assert_called_with(0, os.path.normpath(test_settings["mru_icon_link"]))
            self.assertEqual(self.ui.scan_region, (10, 20, 100, 200))
            self.ui.region_label.config.assert_called_with(text=f"Current Region: (10, 20, 100, 200)")
            mock_update.assert_called_once()

if __name__ == '__main__':
    unittest.main()
