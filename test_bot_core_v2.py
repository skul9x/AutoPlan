import unittest
from unittest.mock import patch, MagicMock
import time
import sys

# Mock dependencies that might be missing in the environment
mock_modules = [
    'pyautogui', 
    'pyscreeze', 
    'PIL', 
    'PIL.Image', 
    'cv2', 
    'keyboard',
    'patch_utils',
    'pyperclip'
]
for module_name in mock_modules:
    sys.modules[module_name] = MagicMock()

from bot_core import BotCore

class TestBotCoreV2(unittest.TestCase):
    def setUp(self):
        self.bot = BotCore(confidence=0.9)

    @patch('pyautogui.locateOnScreen')
    def test_is_icon_visible_true(self, mock_locate):
        mock_locate.return_value = (100, 100, 50, 50)
        result = self.bot.is_icon_visible("test_icon.png")
        self.assertTrue(result)
        mock_locate.assert_called_once_with("test_icon.png", confidence=0.9)

    @patch('pyautogui.locateOnScreen')
    def test_is_icon_visible_false(self, mock_locate):
        mock_locate.return_value = None
        result = self.bot.is_icon_visible("test_icon.png")
        self.assertFalse(result)

    @patch('pyautogui.locateOnScreen')
    def test_is_icon_visible_error(self, mock_locate):
        mock_locate.side_effect = Exception("OpenCV error")
        result = self.bot.is_icon_visible("test_icon.png")
        self.assertFalse(result)

    @patch('pyautogui.hotkey')
    @patch('pyautogui.write')
    @patch('pyautogui.press')
    @patch('time.sleep')
    def test_input_vietcode_sequence(self, mock_sleep, mock_press, mock_write, mock_hotkey):
        file_path = "/path/to/plan.md"
        self.bot.input_vietcode_sequence(file_path)
        
        # Check writes
        mock_write.assert_called_once_with('/vietcod', interval=0.01)

        # Check hotkeys
        hotkey_calls = [
            unittest.mock.call('ctrl', 'shift', 'l'),
            unittest.mock.call('ctrl', 'v')
        ]
        mock_hotkey.assert_has_calls(hotkey_calls)
        
        # Check sleeps
        sleep_calls = [
            unittest.mock.call(1.0),
            unittest.mock.call(0.5),
            unittest.mock.call(0.5)
        ]
        mock_sleep.assert_has_calls(sleep_calls)
        
        # Check presses
        press_calls = [
            unittest.mock.call('enter'),
            unittest.mock.call('enter')
        ]
        mock_press.assert_has_calls(press_calls)

if __name__ == '__main__':
    unittest.main()
