import unittest
from unittest.mock import MagicMock, patch
import os
import sys

# Add the project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestFileSelectionLogic(unittest.TestCase):
    def setUp(self):
        # Mocking project modules
        self.root = MagicMock()
        
        # We mock these because they are imported in ui_components.py
        with patch('ui_components.AutomationEngine'), \
             patch('ui_components.HotkeyHandler'), \
             patch('ui_components.file_manager'):
            from ui_components import AppUI
            self.app = AppUI(self.root)
            
        # Mock UI elements
        self.app.folder_path = MagicMock()
        self.app.icon_path = MagicMock()
        self.app.file_listbox = MagicMock()
        self.app.engine = MagicMock()
        self.app.log = MagicMock()
        self.app.start_btn = MagicMock()
        self.app.stop_btn = MagicMock()

    def test_on_start_no_folder(self):
        self.app.folder_path.get.return_value = ""
        self.app.on_start()
        self.app.log.assert_any_call("Lỗi: Vui lòng chọn thư mục chứa file .md")
        self.app.engine.start.assert_not_called()

    @patch('os.path.exists')
    def test_on_start_no_icon(self, mock_exists):
        self.app.folder_path.get.return_value = "/mock/folder"
        self.app.icon_path.get.return_value = ""
        mock_exists.return_value = False
        
        self.app.on_start()
        self.app.log.assert_any_call("Lỗi: Vui lòng chọn file ảnh icon hợp lệ.")
        self.app.engine.start.assert_not_called()

    @patch('os.path.exists')
    def test_on_start_no_files_selected(self, mock_exists):
        self.app.folder_path.get.return_value = "/mock/folder"
        self.app.icon_path.get.return_value = "/mock/icon.png"
        mock_exists.return_value = True
        self.app.file_listbox.curselection.return_value = []
        
        self.app.on_start()
        self.app.log.assert_any_call("Lỗi: Vui lòng chọn ít nhất một file từ danh sách để bắt đầu.")
        self.app.engine.start.assert_not_called()

    @patch('os.path.exists')
    def test_on_start_success(self, mock_exists):
        self.app.folder_path.get.return_value = "/mock/folder"
        self.app.icon_path.get.return_value = "/mock/icon.png"
        mock_exists.return_value = True
        self.app.file_listbox.curselection.return_value = [0, 2]
        self.app.file_listbox.get.side_effect = lambda i: ["file1.md", "file2.md", "file3.md"][i]
        
        self.app.on_start()
        
        self.app.engine.start.assert_called_once_with(
            "/mock/folder", 
            ["file1.md", "file3.md"], 
            "/mock/icon.png"
        )
        self.app.log.assert_any_call("Starting Auto Bot...")

if __name__ == '__main__':
    unittest.main()
