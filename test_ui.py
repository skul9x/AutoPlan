import tkinter as tk
from ui_components import AppUI
import unittest

class TestUI(unittest.TestCase):
    def test_ui_initialization(self):
        """Kiểm tra khởi tạo UI không có lỗi"""
        root = tk.Tk()
        app = AppUI(root)
        self.assertEqual(root.title(), "AutoPlan Runner - Python Edition")
        
        # Test logging
        app.log("Test log message")
        log_content = app.log_area.get("1.0", tk.END)
        self.assertIn("Test log message", log_content)
        
        # Clean up
        root.destroy()

if __name__ == "__main__":
    unittest.main()
