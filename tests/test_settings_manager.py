import unittest
import os
import json
import shutil
import tempfile
from pathlib import Path
from unittest.mock import patch
import settings_manager

class TestSettingsManager(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        # Mock get_config_dir to use our temp directory
        self.patcher = patch('settings_manager.get_config_dir', return_value=Path(self.test_dir))
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        shutil.rmtree(self.test_dir)

    def test_save_and_load(self):
        data = {"mru_icon_link": "http://example.com/icon.png", "scan_region": [10, 20, 100, 200]}
        settings_manager.save_settings(data)
        
        loaded = settings_manager.load_settings()
        self.assertEqual(loaded["mru_icon_link"], data["mru_icon_link"])
        self.assertEqual(loaded["scan_region"], data["scan_region"])

    def test_load_defaults_if_missing(self):
        loaded = settings_manager.load_settings()
        self.assertEqual(loaded, settings_manager.DEFAULT_SETTINGS)

    def test_load_defaults_if_corrupted(self):
        config_file = settings_manager.get_config_file_path()
        config_file.parent.mkdir(parents=True, exist_ok=True)
        with open(config_file, "w") as f:
            f.write("INVALID JSON {")
            
        loaded = settings_manager.load_settings()
        self.assertEqual(loaded, settings_manager.DEFAULT_SETTINGS)

    def test_atomic_save(self):
        # Verify that config.json only exists after replace
        # This is hard to test perfectly without internal hooks, 
        # but we can check if it works normally.
        data = {"test": "value"}
        settings_manager.save_settings(data)
        config_file = settings_manager.get_config_file_path()
        self.assertTrue(config_file.exists())
        
        with open(config_file, "r") as f:
            content = json.load(f)
        self.assertEqual(content["test"], "value")

    def test_path_detection_linux(self):
        with patch('platform.system', return_value='Linux'):
            with patch.dict(os.environ, {"XDG_CONFIG_HOME": "/tmp/xdg_config"}):
                # Un-patch the get_config_dir for this specific test
                self.patcher.stop()
                path = settings_manager.get_config_dir()
                self.assertEqual(str(path), "/tmp/xdg_config/autoplan")
                self.patcher.start()

            with patch.dict(os.environ, {}, clear=True):
                self.patcher.stop()
                path = settings_manager.get_config_dir()
                # Should fallback to ~/.config/autoplan
                expected = Path.home() / ".config" / "autoplan"
                self.assertEqual(path, expected)
                self.patcher.start()

if __name__ == '__main__':
    unittest.main()
