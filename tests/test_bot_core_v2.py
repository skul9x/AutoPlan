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

import pyautogui
import pyperclip
import time
from unittest.mock import call

class TestBotCoreV2(unittest.TestCase):
    def setUp(self):
        self.bot = BotCore(confidence=0.9)
        # Reset mocks before each test
        pyautogui.locateOnScreen.reset_mock()
        pyautogui.locateOnScreen.side_effect = None
        pyautogui.locateOnScreen.return_value = MagicMock()
        
        pyautogui.hotkey.reset_mock()
        pyautogui.press.reset_mock()
        pyperclip.copy.reset_mock()

    def test_is_icon_visible_true(self):
        pyautogui.locateOnScreen.return_value = (100, 100, 50, 50)
        result = self.bot.is_icon_visible("test_icon.png")
        self.assertTrue(result)
        pyautogui.locateOnScreen.assert_called_once_with("test_icon.png", confidence=0.9, region=None)

    def test_is_icon_visible_false(self):
        pyautogui.locateOnScreen.return_value = None
        result = self.bot.is_icon_visible("test_icon.png")
        self.assertFalse(result)

    def test_is_icon_visible_error(self):
        pyautogui.locateOnScreen.side_effect = Exception("OpenCV error")
        result = self.bot.is_icon_visible("test_icon.png")
        self.assertFalse(result)

    @patch('time.sleep')
    def test_input_template_sequence(self, mock_sleep):
        file_path = "/path/to/plan.md"
        template_prompt = "Process file: {xxx}"
        self.bot.input_template_sequence(file_path, template_prompt)
        
        # Check copy
        pyperclip.copy.assert_called_once_with("Process file: /path/to/plan.md")

        # Check hotkeys
        hotkey_calls = [
            call('ctrl', 'shift', 'l'),
            call('ctrl', 'v')
        ]
        pyautogui.hotkey.assert_has_calls(hotkey_calls)
        
        # Check sleeps
        sleep_calls = [
            call(0.68),
            call(0.68),
            call(0.5),
            call(0.5)
        ]
        mock_sleep.assert_has_calls(sleep_calls)
        
        # Check presses
        press_calls = [
            call('enter')
        ]
        pyautogui.press.assert_has_calls(press_calls)

if __name__ == '__main__':
    unittest.main()
