import pygame
from pynput import keyboard
import threading
import time
import os

class AlarmManager:
    def __init__(self, stop_callback=None):
        """
        Quản lý việc phát báo thức và lắng nghe phím tắt dừng.
        :param stop_callback: Hàm callback được gọi khi báo thức dừng (vd: cập nhật UI).
        """
        self.stop_callback = stop_callback
        self.is_playing = False
        self.listener = None
        
        # Khởi tạo mixer nếu chưa được khởi tạo
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
        except Exception as e:
            print(f"Failed to initialize pygame mixer: {e}")

    def _on_press(self, key):
        if key == keyboard.Key.f12:
            self.stop_alarm()
            if self.stop_callback:
                self.stop_callback()
            return False  # Dừng listener của pynput

    def start_alarm(self, mp3_path):
        """
        Phát nhạc loop và bắt đầu lắng nghe phím F12.
        """
        if self.is_playing:
            return
        
        if not mp3_path or not os.path.exists(mp3_path):
            print(f"Alarm file not found: {mp3_path}")
            return

        try:
            pygame.mixer.music.load(mp3_path)
            pygame.mixer.music.play(loops=-1)  # Phát lặp vô tận
            self.is_playing = True
            
            # Bắt đầu lắng nghe phím F12 trong một thread riêng (pynput.Listener đã là thread)
            self.listener = keyboard.Listener(on_press=self._on_press)
            self.listener.start()
            
        except Exception as e:
            print(f"Error playing alarm: {e}")

    def stop_alarm(self):
        """
        Dừng nhạc và dừng listener.
        """
        if self.is_playing:
            pygame.mixer.music.stop()
            self.is_playing = False
        
        if self.listener:
            self.listener.stop()
            self.listener = None
