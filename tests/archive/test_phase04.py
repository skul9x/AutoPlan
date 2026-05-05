import unittest
from unittest.mock import MagicMock
import sys

# Mock dependencies to allow execution without UI/Libraries
sys.modules['patch_utils'] = MagicMock()
sys.modules['pyautogui'] = MagicMock()
sys.modules['pyscreeze'] = MagicMock()
sys.modules['PIL'] = MagicMock()
sys.modules['cv2'] = MagicMock()
sys.modules['bot_core'] = MagicMock()

from engine import AutomationEngine

class TestPhase04(unittest.TestCase):
    def test_instantiation(self):
        log_cb = MagicMock()
        finish_cb = MagicMock()
        engine = AutomationEngine(log_cb, finish_cb)
        self.assertIsNotNone(engine)
        self.assertFalse(engine.is_running)

if __name__ == '__main__':
    unittest.main()
