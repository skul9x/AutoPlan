import os
import sys

# Thêm thư mục gốc vào sys.path để import alarm_manager
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from alarm_manager import AlarmManager
import time

def test_missing_alarm_file():
    print("Testing AlarmManager with missing file...")
    manager = AlarmManager()
    
    # Đường dẫn không tồn tại
    bad_path = "non_existent_file.mp3"
    
    print(f"Attempting to start alarm with: {bad_path}")
    try:
        manager.start_alarm(bad_path)
        print("Success: App did not crash when file was missing.")
    except Exception as e:
        print(f"Failure: App crashed with error: {e}")
        sys.exit(1)

def test_invalid_audio_file():
    print("\nTesting AlarmManager with invalid audio file...")
    manager = AlarmManager()
    
    # Tạo một file giả không phải MP3
    dummy_path = "not_an_audio.mp3"
    with open(dummy_path, "w") as f:
        f.write("This is not a real MP3 file content.")
    
    print(f"Attempting to start alarm with: {dummy_path}")
    try:
        manager.start_alarm(dummy_path)
        print("Success: App did not crash when file was invalid.")
    except Exception as e:
        print(f"Failure: App crashed with error: {e}")
        os.remove(dummy_path)
        sys.exit(1)
    finally:
        if os.path.exists(dummy_path):
            os.remove(dummy_path)

if __name__ == "__main__":
    test_missing_alarm_file()
    test_invalid_audio_file()
    print("\nAll robustness tests passed!")
