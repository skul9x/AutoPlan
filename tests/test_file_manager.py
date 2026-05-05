import sys
import os

# Add parent directory to sys.path to allow importing from root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import file_manager

def test_file_manager():
    test_dir = os.path.join(os.path.dirname(__file__), "fixtures", "test_folder")
    print(f"Testing directory: {test_dir}")
    
    files = file_manager.get_markdown_files(test_dir)
    
    expected = ["phase-01.md", "phase-02.md"]
    
    print(f"Found files: {files}")
    
    assert files == expected, f"Expected {expected}, but got {files}"
    print("Test passed!")

if __name__ == "__main__":
    test_file_manager()
