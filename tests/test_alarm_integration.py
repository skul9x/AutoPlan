import sys
import os
import time

# Thêm thư mục gốc vào path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from alarm_manager import AlarmManager

def on_stop():
    print("Test: Callback on_stop was called!")

def test_alarm():
    mp3_path = "./venv/lib/python3.12/site-packages/pygame/examples/data/house_lo.mp3"
    
    if not os.path.exists(mp3_path):
        print(f"Error: MP3 file not found at {mp3_path}")
        return

    print("--- Testing AlarmManager ---")
    alarm = AlarmManager(stop_callback=on_stop)
    
    print(f"Starting alarm with file: {mp3_path}")
    print("Please LISTEN for music and PRESS F12 to stop it.")
    
    alarm.start_alarm(mp3_path)
    
    start_time = time.time()
    # Wait for up to 10 seconds or until stopped
    try:
        while alarm.is_playing and (time.time() - start_time < 10):
            time.sleep(0.5)
            
        if alarm.is_playing:
            print("Test timed out after 10 seconds. Stopping alarm manually.")
            alarm.stop_alarm()
        else:
            print("Alarm stopped successfully via F12 or stop_alarm().")
            
    except KeyboardInterrupt:
        print("\nTest interrupted by user (Ctrl+C).")
        alarm.stop_alarm()

if __name__ == "__main__":
    test_alarm()
