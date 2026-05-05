import os
import file_manager

def test_file_manager():
    test_dir = os.path.abspath("test_folder")
    print(f"Testing directory: {test_dir}")
    
    files = file_manager.get_markdown_files(test_dir)
    
    expected = ["phase-01.md", "phase-02.md"]
    
    print(f"Found files: {files}")
    
    assert files == expected, f"Expected {expected}, but got {files}"
    print("Test passed!")

if __name__ == "__main__":
    test_file_manager()
