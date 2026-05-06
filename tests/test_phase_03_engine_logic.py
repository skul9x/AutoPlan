import unittest
import time
import threading
from unittest.mock import MagicMock, patch
from engine import AutomationEngine

class TestEngineDualScan(unittest.TestCase):
    def setUp(self):
        self.log_mock = MagicMock()
        self.finished_mock = MagicMock()
        self.engine = AutomationEngine(self.log_mock, self.finished_mock)
        # Mock the bot's input sequence to avoid actual keyboard actions
        self.engine.bot.input_template_sequence = MagicMock()

    def test_start_signature_and_thread_init(self):
        """Test if start() accepts error_icon_path and passes it to the thread."""
        with patch('threading.Thread') as mock_thread:
            self.engine.start(
                folder_path="/tmp",
                md_files=["test.md"],
                icon_path="icon.png",
                error_icon_path="error.png",
                region=(0,0,10,10)
            )
            
            # Check if Thread was initialized with correct args
            args = mock_thread.call_args[1]['args']
            # Expected args order in engine.py:
            # (folder_path, md_files, icon_path, region, error_icon_path, alarm_enabled, alarm_path)
            self.assertEqual(args[4], "error.png")

    def test_dual_scan_logic_error_found(self):
        """Test that if error icon is found, it sleeps and continues without breaking."""
        # Setup mocks
        self.engine.bot.is_icon_visible = MagicMock()
        
        # Scenario: 
        # 1. First call: error_icon is visible.
        # 2. Second call: error_icon is NOT visible, but normal_icon IS.
        self.engine.bot.is_icon_visible.side_effect = [
            True,  # is_icon_visible(error_icon_path) -> Found!
            False, # is_icon_visible(error_icon_path) -> Not found
            True   # is_icon_visible(icon_path) -> Found!
        ]

        # We need to run _run_loop in a way we can control or observe.
        # Since it's a loop, we'll run it and then stop the engine.
        
        # To avoid long sleeps in tests, we can mock time.sleep
        with patch('time.sleep') as mock_sleep:
            # Run the loop for one file
            self.engine.is_running = True
            # Mocking os.path.exists or just letting it fail silently if not used before sequence
            with patch('os.path.join', return_value="fake_path"):
                # We only need to test the logic inside the loop
                # Calling _run_loop directly for testing
                # Signature: _run_loop(self, folder_path, md_files, icon_path, region, error_icon_path, alarm_enabled, alarm_path)
                
                # We stop the engine right after it finds the normal icon to avoid infinite loop
                def stop_engine(*args, **kwargs):
                    if self.engine.bot.is_icon_visible.call_count >= 3:
                        self.engine.is_running = False
                
                mock_sleep.side_effect = stop_engine

                self.engine._run_loop("/tmp", ["file1.md"], "normal.png", None, "error.png", False, "", "")

        # Verify calls
        # Call 1: error.png (Found)
        # Call 2: error.png (Not found)
        # Call 3: normal.png (Found)
        
        # Total calls should be at least 3
        self.assertGreaterEqual(self.engine.bot.is_icon_visible.call_count, 3)
        
        # Check if log reported error icon
        error_logs = [call for call in self.log_mock.call_args_list if "Phát hiện ảnh lỗi" in str(call)]
        self.assertTrue(len(error_logs) > 0)
        
        # Check if input sequence was called (meaning it broke the loop correctly after normal icon)
        self.engine.bot.input_template_sequence.assert_called_once()

    def test_backward_compatibility_no_error_path(self):
        """Test that if error_icon_path is None, it works as before."""
        self.engine.bot.is_icon_visible = MagicMock(return_value=True)
        
        with patch('time.sleep'):
            with patch('os.path.join', return_value="fake_path"):
                # Set is_running to False after one iteration to stop the loop if it doesn't break
                # But here it should break naturally on normal icon
                self.engine.is_running = True
                
                # Mock input_template_sequence to stop the loop
                def stop_loop(*args):
                    self.engine.is_running = False
                self.engine.bot.input_template_sequence.side_effect = stop_loop
                
                self.engine._run_loop("/tmp", ["file1.md"], "normal.png", None, None, False, "", "")

        # is_icon_visible should be called with normal.png
        self.engine.bot.is_icon_visible.assert_any_call("normal.png", region=None)
        
        # Log should NOT contain "ảnh lỗi" info in wait message if None
        wait_logs = [call for call in self.log_mock.call_args_list if "Đang chờ icon hiển thị" in str(call)]
        self.assertFalse("ảnh lỗi" in str(wait_logs[0]))

if __name__ == "__main__":
    unittest.main()
