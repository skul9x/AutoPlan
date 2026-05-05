import os
import sys
import unittest
import pathlib
import json
import shutil

# Add parent dir to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import settings_manager

class TestPhase04(unittest.TestCase):
    def setUp(self):
        self.test_dir = pathlib.Path("./test_config_temp")
        self.test_dir.mkdir(parents=True, exist_ok=True)
        # Mock settings_manager's config path for testing
        self.original_get_config_dir = settings_manager.get_config_dir
        settings_manager.get_config_dir = lambda: self.test_dir

    def tearDown(self):
        settings_manager.get_config_dir = self.original_get_config_dir
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_config_path_resolution(self):
        path = settings_manager.get_config_file_path()
        self.assertTrue(str(path).endswith("config.json"))
        print(f"DEBUG: Config path is {path}")

    def test_atomic_save_and_cleanup(self):
        data = {"test": "value"}
        settings_manager.save_settings(data)
        
        config_file = settings_manager.get_config_file_path()
        tmp_file = config_file.with_suffix(".json.tmp")
        
        self.assertTrue(config_file.exists(), "Config file should exist after save")
        self.assertFalse(tmp_file.exists(), "Temporary file should be removed after successful save")
        
        with open(config_file, "r") as f:
            loaded = json.load(f)
            self.assertEqual(loaded["test"], "value")

    def test_cleanup_on_failure(self):
        # We can't easily force a failure inside save_settings without mocking 'open'
        # but we can check if it at least handles basic exceptions
        config_file = settings_manager.get_config_file_path()
        tmp_file = config_file.with_suffix(".json.tmp")
        
        # Manually create a tmp file
        tmp_file.touch()
        self.assertTrue(tmp_file.exists())
        
        # Running save_settings should replace it or clean it
        settings_manager.save_settings({"new": "data"})
        self.assertFalse(tmp_file.exists(), "Temporary file should not exist after save_settings")

if __name__ == "__main__":
    unittest.main()
