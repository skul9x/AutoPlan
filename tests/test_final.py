import unittest
from unittest.mock import MagicMock, patch
import os
import sys

# Đảm bảo dùng đúng BotCore thật (không mock module)
from engine import AutomationEngine

class TestFinal(unittest.TestCase):
    def setUp(self):
        self.logs = []
        self.engine = AutomationEngine(lambda m: self.logs.append(m), lambda: None)
        # Mock bot instance để không click thật gây lỗi môi trường không màn hình
        self.engine.bot = MagicMock()

    def test_full_loop(self):
        self.engine.bot.locate_and_click.return_value = True
        
        with patch('time.sleep', return_value=None):
            self.engine._run_loop("/test", ["step1.md", "step2.md"], "icon.png")
        
        # Kiểm tra logic chạy
        self.assertEqual(self.engine.bot.locate_and_click.call_count, 2)
        self.assertEqual(self.engine.bot.type_command.call_count, 2)
        
        print("\n[V] Test logic Engine chạy qua venv: PASSED")
        print(f"[V] Số lượng file xử lý: {len([m for m in self.logs if 'Đang chạy file' in m])}")

if __name__ == '__main__':
    unittest.main()
