import os
import unittest
import tempfile
import shutil
import tkinter as tk
from unittest.mock import MagicMock, patch

import file_manager
import ui_components
import settings_manager

class TestPhase03Verification(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for file_manager tests
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_plan_md_filtering(self):
        """Requirement: Ensure plan.md is never listed."""
        # Create some markdown files including plan.md
        files_to_create = ["step1.md", "step2.md", "plan.md", "PLAN.MD", "other.txt"]
        for f in files_to_create:
            with open(os.path.join(self.test_dir, f), 'w') as temp_f:
                temp_f.write("test")
        
        # Call get_markdown_files
        md_files = file_manager.get_markdown_files(self.test_dir)
        
        # Verify plan.md and PLAN.MD are not in the list
        self.assertIn("step1.md", md_files)
        self.assertIn("step2.md", md_files)
        self.assertNotIn("plan.md", md_files)
        self.assertNotIn("PLAN.MD", md_files)
        self.assertNotIn("other.txt", md_files)
        print("✓ plan.md filtering verified.")

    @patch('settings_manager.save_settings')
    def test_folder_persistence_reset(self, mock_save):
        """Requirement: Ensure folder path is never persisted."""
        # Initialize Tkinter root (withdraw to avoid showing window)
        root = tk.Tk()
        root.withdraw()
        
        # Create AppUI instance
        app = ui_components.AppUI(root)
        
        # Simulate some state
        app.icon_path.delete(0, tk.END)
        app.icon_path.insert(0, "/path/to/icon.png")
        app.folder_path.delete(0, tk.END)
        app.folder_path.insert(0, "/path/to/folder")
        app.scan_region = (0, 0, 100, 100)
        
        # Call save_current_settings
        app.save_current_settings()
        
        # Check if save_settings was called with mru_md_folder as empty string
        mock_save.assert_called_once()
        saved_data = mock_save.call_args[0][0]
        self.assertEqual(saved_data["mru_md_folder"], "")
        self.assertEqual(saved_data["mru_icon_link"], "/path/to/icon.png")
        self.assertEqual(saved_data["scan_region"], (0, 0, 100, 100))
        
        root.destroy()
        print("✓ Folder path persistence reset verified.")

if __name__ == "__main__":
    unittest.main()
