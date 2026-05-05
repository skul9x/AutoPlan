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

class TestUIPersistence(unittest.TestCase):
    @patch('settings_manager.save_settings')
    def test_save_current_settings_excludes_folder(self, mock_save):
        # Setup
        root = MagicMock()
        ui = ui_components.AppUI(root)
        
        # Mock entry values
        ui.folder_path = MagicMock()
        ui.folder_path.get.return_value = "/some/path"
        ui.icon_path = MagicMock()
        ui.icon_path.get.return_value = "/icon/path"
        ui.scan_region = (10, 10, 100, 100)
        
        # Execute
        ui.save_current_settings()
        
        # Verify
        mock_save.assert_called_once()
        saved_data = mock_save.call_args[0][0]
        
        # This is what we are testing: mru_md_folder should be empty string
        # according to the new requirement.
        # Currently it probably fails if I expect "" before applying the fix.
        self.assertEqual(saved_data["mru_md_folder"], "")
        self.assertEqual(saved_data["mru_icon_link"], "/icon/path")
        self.assertEqual(saved_data["scan_region"], (10, 10, 100, 100))

if __name__ == "__main__":
    unittest.main()
