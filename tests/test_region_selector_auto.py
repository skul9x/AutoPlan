import threading
import time
import pyautogui
from region_selector import RegionSelector

def simulate_selection(start_pos, end_pos):
    time.sleep(1) # Wait for UI to load
    pyautogui.moveTo(start_pos[0], start_pos[1])
    pyautogui.dragTo(end_pos[0], end_pos[1], duration=0.5, button='left')
    time.sleep(0.5)

def test_selection_forward():
    print("Testing forward selection (100, 100) -> (300, 300)...")
    selector = RegionSelector()
    
    # Start simulation thread
    t = threading.Thread(target=simulate_selection, args=((100, 100), (300, 300)))
    t.start()
    
    region = selector.get_selection()
    print(f"Result: {region}")
    
    assert region is not None
    assert region[0] == 100
    assert region[1] == 100
    assert region[2] == 200
    assert region[3] == 200
    print("Forward selection test passed!")

def test_selection_backward():
    print("Testing backward selection (300, 300) -> (100, 100)...")
    selector = RegionSelector()
    
    # Start simulation thread
    t = threading.Thread(target=simulate_selection, args=((300, 300), (100, 100)))
    t.start()
    
    region = selector.get_selection()
    print(f"Result: {region}")
    
    assert region is not None
    assert region[0] == 100
    assert region[1] == 100
    assert region[2] == 200
    assert region[3] == 200
    print("Backward selection test passed!")

if __name__ == "__main__":
    # Ensure fail-safe is off for testing if needed, but better to keep it
    pyautogui.FAILSAFE = False 
    try:
        test_selection_forward()
        test_selection_backward()
        print("\nAll tests passed successfully!")
    except Exception as e:
        print(f"\nTest failed: {e}")
        exit(1)
