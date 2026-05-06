import unittest
from unittest.mock import patch, MagicMock
from engine import AutomationEngine
import time

class TestEngineRegion(unittest.TestCase):
    def setUp(self):
        self.log_mock = MagicMock()
        self.finished_mock = MagicMock()
        self.engine = AutomationEngine(self.log_mock, self.finished_mock)

    @patch('time.sleep')
    @patch('bot_core.BotCore.is_icon_visible')
    @patch('bot_core.BotCore.input_template_sequence')
    def test_engine_passes_region(self, mock_sequence, mock_visible, mock_sleep):
        # Setup: icon found, then not found (to exit wait loop)
        mock_visible.side_effect = [True, False]
        
        region = (50, 50, 100, 100)
        md_files = ["test.md"]
        
        # We need to run _run_loop directly to avoid threading for simple test
        self.engine.is_running = True
        self.engine._run_loop("/fake/path", md_files, "icon.png", region, None, False, "", "")
        
        # Verify visibility checks use region
        # First call: wait for icon
        # Second call: wait for icon to disappear
        self.assertEqual(mock_visible.call_args_list[0][1]['region'], region)
        self.assertEqual(mock_visible.call_args_list[1][1]['region'], region)
        
        # Verify sequence called
        mock_sequence.assert_called_once()

if __name__ == '__main__':
    unittest.main()
