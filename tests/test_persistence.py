import sys
import os
import unittest
from unittest.mock import MagicMock, patch

# Add the app directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import settings_manager
import ui_components

class TestPersistence(unittest.TestCase):
    def setUp(self):
        # Backup existing config if any
        self.config_file = settings_manager.get_config_file_path()
        self.backup_file = self.config_file.with_suffix(".json.bak")
        if self.config_file.exists():
            os.rename(self.config_file, self.backup_file)

    def tearDown(self):
        # Restore backup
        if self.backup_file.exists():
            if self.config_file.exists():
                os.remove(self.config_file)
            os.rename(self.backup_file, self.config_file)
        elif self.config_file.exists():
            os.remove(self.config_file)

    @patch('tkinter.Tk')
    @patch('tkinter.ttk.Frame')
    @patch('tkinter.ttk.Label')
    @patch('tkinter.ttk.Entry')
    @patch('tkinter.ttk.Button')
    @patch('tkinter.ttk.Scrollbar')
    @patch('tkinter.Listbox')
    @patch('tkinter.scrolledtext.ScrolledText')
    def test_save_current_settings(self, mock_st, mock_lb, mock_sb, mock_btn, mock_entry, mock_label, mock_frame, mock_tk):
        # Setup mocks
        root = mock_tk()
        
        # Create instances of Entry for folder_path and icon_path
        folder_entry = MagicMock()
        folder_entry.get.return_value = "/mock/folder"
        
        icon_entry = MagicMock()
        icon_entry.get.return_value = "/mock/icon.png"
        
        # We need to control what setattr does or just mock the AppUI instance partially
        with patch('ui_components.AppUI.create_path_selector'):
            app = ui_components.AppUI(root)
            
            # Manually set the entries since we mocked create_path_selector
            app.folder_path = folder_entry
            app.icon_path = icon_entry
            app.scan_region = (10, 20, 100, 200)
            
            # Call the method we want to test
            app.save_current_settings()
            
            # Check if settings were saved
            saved_settings = settings_manager.load_settings()
            self.assertEqual(saved_settings["mru_md_folder"], "/mock/folder")
            self.assertEqual(saved_settings["mru_icon_link"], "/mock/icon.png")
            self.assertEqual(saved_settings["scan_region"], [10, 20, 100, 200]) # JSON turns tuple to list

    @patch('tkinter.filedialog.askdirectory')
    @patch('ui_components.AppUI.save_current_settings')
    @patch('ui_components.AppUI.update_file_list')
    def test_browse_folder_triggers_save(self, mock_update, mock_save, mock_ask):
        mock_ask.return_value = "/new/folder"
        
        # Mock AppUI and its dependencies
        root = MagicMock()
        with patch('ui_components.AppUI.__init__', return_value=None):
            app = ui_components.AppUI(root)
            app.folder_path = MagicMock()
            app.log = MagicMock()
            app.save_current_settings = mock_save
            app.update_file_list = mock_update
            
            # Call browse_folder
            ui_components.AppUI.browse_folder(app)
            
            # Verify save_current_settings was called
            mock_save.assert_called_once()

if __name__ == '__main__':
    unittest.main()
