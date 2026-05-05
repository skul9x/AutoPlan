import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Mock các thư viện UI
sys.modules['patch_utils'] = MagicMock()
sys.modules['pyautogui'] = MagicMock()
sys.modules['pyscreeze'] = MagicMock()
sys.modules['PIL'] = MagicMock()
sys.modules['cv2'] = MagicMock()
sys.modules['bot_core'] = MagicMock()

from engine import AutomationEngine

class TestEngineLogic(unittest.TestCase):
    def test_run_loop_logic(self):
        logs = []
        finished = [False]
        
        def log_cb(m): logs.append(m)
        def finish_cb(): finished[0] = True
        
        # Patch BotCore trong module engine
        with patch('engine.BotCore') as MockBot:
            mock_instance = MockBot.return_value
            mock_instance.locate_and_click.return_value = True
            
            engine = AutomationEngine(log_cb, finish_cb)
            engine.bot = mock_instance # Gán lại instance đã mock
            
            # Chạy thử loop với 2 file
            with patch('time.sleep', return_value=None): # Bỏ qua sleep để test nhanh
                engine._run_loop("/path", ["f1.md", "f2.md"], "icon.png")
            
            # Kiểm tra xem có gọi click và gõ phím đúng 2 lần không
            self.assertEqual(mock_instance.locate_and_click.call_count, 2)
            self.assertEqual(mock_instance.type_command.call_count, 2)
            
            # Kiểm tra log
            self.assertTrue(any("f1.md" in m for m in logs))
            self.assertTrue(any("f2.md" in m for m in logs))
            self.assertTrue(finished[0])

if __name__ == '__main__':
    unittest.main()
