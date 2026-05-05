import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add parent directory to sys.path to allow importing from root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bot_core import BotCore

class TestBotCoreRegion(unittest.TestCase):
    def setUp(self):
        self.bot = BotCore()

    @patch('pyautogui.locateCenterOnScreen')
    def test_locate_and_click_with_region(self, mock_locate):
        # Setup mock
        mock_locate.return_value = (100, 100)
        region = (0, 0, 500, 500)
        
        with patch('pyautogui.click') as mock_click:
            result = self.bot.locate_and_click("test.png", region=region)
            
            # Verify
            mock_locate.assert_called_once_with("test.png", confidence=0.9, region=region)
            mock_click.assert_called_once_with((100, 100))
            self.assertTrue(result)

    @patch('pyautogui.locateOnScreen')
    def test_is_icon_visible_with_region(self, mock_locate):
        # Setup mock
        mock_locate.return_value = (10, 10, 50, 50)
        region = (100, 100, 200, 200)
        
        result = self.bot.is_icon_visible("test.png", region=region)
        
        # Verify
        mock_locate.assert_called_once_with("test.png", confidence=0.9, region=region)
        self.assertTrue(result)

    @patch('pyautogui.locateOnScreen')
    def test_is_icon_visible_outside_region(self, mock_locate):
        # Setup mock to return None (not found in region)
        mock_locate.return_value = None
        region = (100, 100, 10, 10)
        
        result = self.bot.is_icon_visible("test.png", region=region)
        
        # Verify
        mock_locate.assert_called_once_with("test.png", confidence=0.9, region=region)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
