import unittest
import os
import shutil
import sys

# Thêm đường dẫn gốc vào sys.path để import file_manager
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from file_manager import get_markdown_files

class TestIntegrationPhase03(unittest.TestCase):
    def setUp(self):
        # Create a temporary test folder
        self.test_dir = "test_phase_03_folder"
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)
        
        # Create mixed files
        self.files = [
            "c_file.md",
            "a_file.md",
            "b_file.txt", # Should be ignored
            "d_file.md",
            "01_start.md"
        ]
        for f in self.files:
            with open(os.path.join(self.test_dir, f), "w") as f_out:
                f_out.write("test content")

    def tearDown(self):
        # Cleanup
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_file_filtering_and_sorting(self):
        """Check if only .md files are returned and they are sorted alphabetically."""
        md_files = get_markdown_files(self.test_dir)
        
        # Expected results: sorted md files
        expected = ["01_start.md", "a_file.md", "c_file.md", "d_file.md"]
        
        self.assertEqual(md_files, expected)
        self.assertNotIn("b_file.txt", md_files)

    def test_empty_or_invalid_directory(self):
        """Check behavior with invalid directory."""
        self.assertEqual(get_markdown_files("non_existent_folder"), [])
        self.assertEqual(get_markdown_files(""), [])

if __name__ == "__main__":
    unittest.main()
