import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock
from ui_components import AppUI
import settings_manager

class TestPhase03PromptTemplateUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        # Mock settings manager to avoid touching real settings file
        self.mock_settings = {
            "mru_md_folder": "",
            "error_icon_path": "",
            "mru_icon_link": "",
            "scan_region": None,
            "alarm_enabled": False,
            "alarm_mp3_path": "",
            "prompt_template": "Initial Prompt Template"
        }
        
        self.patcher_load = patch('settings_manager.load_settings', return_value=self.mock_settings)
        self.patcher_save = patch('settings_manager.save_settings')
        self.patcher_get_config = patch('settings_manager.get_config_file_path', return_value="dummy_path.json")
        
        self.mock_load = self.patcher_load.start()
        self.mock_save = self.patcher_save.start()
        self.mock_get_config = self.patcher_get_config.start()

    def tearDown(self):
        self.root.destroy()
        self.patcher_load.stop()
        self.patcher_save.stop()
        self.patcher_get_config.stop()

    def test_prompt_template_loaded_and_edited(self):
        # 1. Start App UI
        app = AppUI(self.root)
        
        # Test: The template should be loaded into the prompt_text
        current_text = app.prompt_text.get("1.0", tk.END).strip()
        self.assertEqual(current_text, "Initial Prompt Template", "Initial prompt template not loaded correctly")
        
        # 2. Edit the prompt template
        app.prompt_text.delete("1.0", tk.END)
        app.prompt_text.insert(tk.END, "New Edited Prompt Template")
        
        # Trigger modify event or call save explicitly (as we can't easily trigger the exact sequence of events without mainloop)
        app.save_current_settings()
        
        # Test: Ensure save_settings was called with the updated prompt_template
        self.mock_save.assert_called()
        saved_data = self.mock_save.call_args[0][0]
        self.assertEqual(saved_data.get("prompt_template"), "New Edited Prompt Template", "Prompt template not saved correctly")

    @patch('engine.AutomationEngine.start')
    @patch('os.path.exists', return_value=True) # mock path exists so start logic passes
    def test_engine_receives_prompt_template(self, mock_exists, mock_start):
        # 1. Start App UI
        app = AppUI(self.root)
        
        # Set some required values so on_start doesn't return early
        app.folder_path.insert(0, "/dummy/folder")
        app.icon_path.insert(0, "/dummy/icon.png")
        
        # Mock the listbox to have one item selected
        app.file_listbox.insert(tk.END, "file1.md")
        app.file_listbox.select_set(0)
        
        # Edit the template
        app.prompt_text.delete("1.0", tk.END)
        app.prompt_text.insert(tk.END, "Template passed to engine")
        
        # 2. Call on_start
        app.on_start()
        
        # 3. Verify that engine.start was called with the template_prompt
        mock_start.assert_called_once()
        kwargs = mock_start.call_args[1]
        self.assertEqual(kwargs.get('template_prompt'), "Template passed to engine", "Engine did not receive the correct prompt_template")

if __name__ == '__main__':
    unittest.main()
