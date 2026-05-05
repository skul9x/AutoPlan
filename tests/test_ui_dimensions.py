import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add the app directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestUIDimensions(unittest.TestCase):
    @patch('ui_components.scrolledtext.ScrolledText')
    @patch('ui_components.tk.BooleanVar')
    @patch('ui_components.ttk.Frame')
    @patch('ui_components.ttk.Label')
    @patch('ui_components.ttk.Entry')
    @patch('ui_components.ttk.Button')
    @patch('ui_components.tk.Listbox')
    @patch('ui_components.ttk.Scrollbar')
    @patch('ui_components.ttk.LabelFrame')
    @patch('ui_components.tk.Checkbutton')
    @patch('ui_components.AutomationEngine')
    @patch('ui_components.HotkeyHandler')
    @patch('ui_components.settings_manager.load_settings')
    @patch('ui_components.settings_manager.get_config_file_path')
    def test_ui_initial_dimensions(self, mock_get_path, mock_load_settings, mock_hotkey, mock_engine, *args):
        import tkinter as tk
        from ui_components import AppUI
        
        # Setup mocks
        root = MagicMock(spec=tk.Tk)
        mock_load_settings.return_value = {}
        mock_get_path.return_value = "config.json"
        
        # Mock screen width/height for center_window
        root.winfo_screenwidth.return_value = 1920
        root.winfo_screenheight.return_value = 1080
        
        # Initialize UI
        app = AppUI(root)
        
        # Check initial geometry call (line 16)
        # Note: center_window also calls geometry, so we check all calls
        geometry_calls = [call.args[0] for call in root.geometry.call_args_list]
        self.assertIn("650x750", geometry_calls)
        
        # Check log_area height (line 137)
        # Re-check patch order: @patch('ui_components.scrolledtext.ScrolledText') is args[9] (first patch, last in args)
        mock_scrolled_text_class = args[9]
        mock_scrolled_text_class.assert_called()
        
        # Check that height=15 was passed to ScrolledText
        args_list = mock_scrolled_text_class.call_args_list
        # Find the call that has height=15
        found_height = False
        for call in args_list:
            if call.kwargs.get('height') == 15:
                found_height = True
                break
        self.assertTrue(found_height, "ScrolledText was not initialized with height=15")

    @patch('ui_components.scrolledtext.ScrolledText')
    @patch('ui_components.tk.BooleanVar')
    @patch('ui_components.ttk.Frame')
    @patch('ui_components.ttk.Label')
    @patch('ui_components.ttk.Entry')
    @patch('ui_components.ttk.Button')
    @patch('ui_components.tk.Listbox')
    @patch('ui_components.ttk.Scrollbar')
    @patch('ui_components.ttk.LabelFrame')
    @patch('ui_components.tk.Checkbutton')
    @patch('ui_components.AutomationEngine')
    @patch('ui_components.HotkeyHandler')
    @patch('ui_components.settings_manager.load_settings')
    @patch('ui_components.settings_manager.get_config_file_path')
    def test_center_window_dimensions(self, mock_get_path, mock_load_settings, mock_hotkey, mock_engine, *args):
        import tkinter as tk
        from ui_components import AppUI
        
        root = MagicMock(spec=tk.Tk)
        mock_load_settings.return_value = {}
        root.winfo_screenwidth.return_value = 1920
        root.winfo_screenheight.return_value = 1080
        
        app = AppUI(root)
        
        # Reset mock to check specific center_window call
        root.geometry.reset_mock()
        app.center_window() # Should use defaults: 650, 750
        
        expected_x = (1920 // 2) - (650 // 2)
        expected_y = (1080 // 2) - (750 // 2)
        expected_geom = f"650x750+{expected_x}+{expected_y}"
        
        root.geometry.assert_called_with(expected_geom)

if __name__ == '__main__':
    unittest.main()
