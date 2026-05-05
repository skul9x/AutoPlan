import tkinter as tk
from ui_components import AppUI
import os
import file_manager

def test_ui_initialization():
    root = tk.Tk()
    app = AppUI(root)
    
    # Check if components exist
    assert hasattr(app, 'file_listbox'), "file_listbox should exist"
    assert hasattr(app, 'update_file_list'), "update_file_list should exist"
    assert hasattr(app, 'select_all'), "select_all should exist"
    assert hasattr(app, 'deselect_all'), "deselect_all should exist"
    
    print("UI Components check passed.")
    root.destroy()

def test_file_list_update(tmp_path):
    # Create some dummy .md files
    d = tmp_path / "test_md"
    d.mkdir()
    (d / "file1.md").write_text("content")
    (d / "file2.md").write_text("content")
    (d / "other.txt").write_text("content")
    
    root = tk.Tk()
    app = AppUI(root)
    
    app.update_file_list(str(d))
    
    # Check listbox content
    items = app.file_listbox.get(0, tk.END)
    assert "file1.md" in items
    assert "file2.md" in items
    assert "other.txt" not in items
    assert len(items) == 2
    
    # Check selection (default select all)
    selected = app.file_listbox.curselection()
    assert len(selected) == 2
    
    print("File list update check passed.")
    root.destroy()

if __name__ == "__main__":
    # Since we need a temporary path and pytest-like behavior without pytest
    import tempfile
    import shutil
    from pathlib import Path
    
    test_ui_initialization()
    
    tmpdir = tempfile.mkdtemp()
    try:
        test_file_list_update(Path(tmpdir))
    finally:
        shutil.rmtree(tmpdir)
    
    print("All tests for Phase 01 passed!")
