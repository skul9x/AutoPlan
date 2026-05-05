from pynput import keyboard
import threading

class HotkeyHandler:
    def __init__(self, stop_callback, key="f9"):
        self.stop_callback = stop_callback
        self.key_name = key.lower()
        self.listener = None

    def start(self):
        if self.listener and self.listener.is_alive():
            return
        
        def on_press(key):
            try:
                # Check if the key matches
                k = None
                if hasattr(key, 'name'):
                    k = key.name
                elif hasattr(key, 'char'):
                    k = key.char
                
                if k == self.key_name:
                    print(f"Panic button ({self.key_name}) pressed!")
                    self.stop_callback()
            except Exception as e:
                print(f"Error in hotkey listener: {e}")

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()
        print(f"Hotkey listener started. Press {self.key_name.upper()} to panic stop.")

    def stop(self):
        if self.listener:
            self.listener.stop()
            print("Hotkey listener stopped.")
