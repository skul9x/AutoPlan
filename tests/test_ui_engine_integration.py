import unittest
from unittest.mock import MagicMock, patch
import os
import sys

# Thêm đường dẫn gốc vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui_components import AppUI

class TestUIEngineIntegration(unittest.TestCase):
    def setUp(self):
        self.root = MagicMock()
        # Mocking common tkinter elements used in AppUI.__init__
        with patch('tkinter.ttk.Frame'), \
             patch('tkinter.ttk.Label'), \
             patch('tkinter.ttk.Entry'), \
             patch('tkinter.ttk.Button'), \
             patch('tkinter.Listbox'), \
             patch('tkinter.ttk.Scrollbar'), \
             patch('tkinter.scrolledtext.ScrolledText'), \
             patch('hotkey.HotkeyHandler'):
            self.ui = AppUI(self.root)
            
        # Manually set some attributes that were mocked
        self.ui.folder_path = MagicMock()
        self.ui.icon_path = MagicMock()
        self.ui.file_listbox = MagicMock()
        self.ui.start_btn = MagicMock()
        self.ui.stop_btn = MagicMock()
        self.ui.log_area = MagicMock()
        self.ui.engine = MagicMock()

    def test_start_with_no_selection(self):
        """Verify that starting without selecting files shows an error."""
        self.ui.folder_path.get.return_value = "/some/path"
        self.ui.icon_path.get.return_value = "/some/icon.png"
        
        # Patching os.path.exists specifically for this test
        with patch('os.path.exists', return_value=True):
            self.ui.file_listbox.curselection.return_value = []
            
            with patch.object(self.ui, 'log') as mock_log:
                self.ui.on_start()
                mock_log.assert_called_with("Lỗi: Vui lòng chọn ít nhất một file từ danh sách để bắt đầu.")
                self.ui.engine.start.assert_not_called()

    def test_start_with_selection(self):
        """Verify that starting with selected files calls the engine correctly."""
        folder = "/test/folder"
        icon = "/test/icon.png"
        self.ui.folder_path.get.return_value = folder
        self.ui.icon_path.get.return_value = icon
        
        with patch('os.path.exists', return_value=True):
            self.ui.file_listbox.curselection.return_value = [0, 2]
            self.ui.file_listbox.get.side_effect = lambda i: ["file1.md", "file2.md", "file3.md"][i]
            
            self.ui.on_start()
            
            expected_files = ["file1.md", "file3.md"]
            self.ui.engine.start.assert_called_with(folder, expected_files, icon)
            self.ui.start_btn.config.assert_any_call(state='disabled')
            self.ui.stop_btn.config.assert_any_call(state='normal')

    def test_stop_behavior(self):
        """Verify that stopping the UI calls engine.stop."""
        self.ui.on_stop()
        self.ui.engine.stop.assert_called_once()

if __name__ == "__main__":
    unittest.main()
