import tkinter as tk
from ui_components import AppUI
from unittest.mock import MagicMock, patch
import os

def test_region_integration():
    root = tk.Tk()
    app = AppUI(root)
    
    # 1. Check if scan_region is initialized
    assert app.scan_region is None, "scan_region should be None by default"
    
    # 2. Check UI components
    assert hasattr(app, 'region_label'), "region_label should exist"
    assert "Full Screen" in app.region_label.cget("text")
    
    # 3. Test on_reset_region
    app.scan_region = (10, 20, 100, 200)
    app.on_reset_region()
    assert app.scan_region is None
    assert "Full Screen" in app.region_label.cget("text")
    
    # 4. Test on_select_region (Mocking RegionSelector)
    with patch('ui_components.RegionSelector') as MockSelector:
        mock_instance = MockSelector.return_value
        mock_instance.get_selection.return_value = (50, 60, 300, 400)
        
        app.on_select_region()
        
        assert app.scan_region == (50, 60, 300, 400)
        assert "(50, 60, 300, 400)" in app.region_label.cget("text")
    
    print("UI Region Selection Integration check passed.")
    root.destroy()

def test_engine_start_with_region():
    root = tk.Tk()
    app = AppUI(root)
    
    # Mock engine
    app.engine = MagicMock()
    
    # Mock inputs
    app.folder_path.insert(0, "/test/folder")
    app.icon_path.insert(0, "/test/icon.png")
    
    # Mock file listbox
    app.file_listbox.insert(tk.END, "test1.md")
    app.file_listbox.select_set(0)
    
    # Set a region
    app.scan_region = (1, 2, 3, 4)
    
    # Mock os.path.exists to return True for icon
    with patch('os.path.exists', return_value=True):
        app.on_start()
    
    # Verify engine.start was called with the region
    app.engine.start.assert_called_once()
    args, kwargs = app.engine.start.call_args
    assert kwargs.get('region') == (1, 2, 3, 4)
    
    print("Engine start with region check passed.")
    root.destroy()

if __name__ == "__main__":
    test_region_integration()
    test_engine_start_with_region()
    print("All tests for Phase 03 UI Integration passed!")
