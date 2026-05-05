# Phase 01: Center Window on Screen
Status: ✅ Completed
Dependencies: None

## Objective
Khi mở app, cửa sổ phải xuất hiện ở **giữa màn hình** thay vì vị trí mặc định (góc trên trái).

## Root Cause
File `ui_components.py` dòng 16:
```python
self.root.geometry("650x650")
```
Chỉ set kích thước `width x height`, KHÔNG có offset `+x+y` → Window Manager tự quyết định vị trí.

## Implementation Steps

### 1. [ ] Tạo helper function `center_window()` trong `ui_components.py`
**Vị trí:** Thêm method mới trong class `AppUI`, ngay sau `__init__`

```python
def center_window(self, width=650, height=650):
    """Center the window on screen."""
    self.root.update_idletasks()  # Đảm bảo geometry đã được tính
    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    self.root.geometry(f"{width}x{height}+{x}+{y}")
```

**Giải thích:**
- `update_idletasks()`: Ép Tkinter tính toán layout trước khi đọc kích thước
- `winfo_screenwidth/height()`: Lấy resolution màn hình
- Công thức: `(screen - window) / 2` = vị trí để window nằm chính giữa

### 2. [ ] Thay thế `self.root.geometry("650x650")` bằng `self.center_window()`
**File:** `ui_components.py` dòng 16
```python
# TRƯỚC:
self.root.geometry("650x650")

# SAU:
self.center_window(650, 650)
```

### 3. [ ] Đảm bảo gọi `center_window()` SAU khi tất cả widget đã được tạo
**Lưu ý:** `center_window()` nên được gọi sau `self.load_and_apply_settings()` (dòng 148) để đảm bảo mọi widget đã render xong, window size đã ổn định.

Cách tiếp cận tốt nhất: Giữ `self.root.geometry("650x650")` ở dòng 16 để set kích thước ban đầu, rồi gọi `center_window()` ở cuối `__init__` để reposition.

## Files to Create/Modify
- `ui_components.py` — Thêm method `center_window()` + gọi nó cuối `__init__`

## Test Criteria
- [ ] Mở app → cửa sổ xuất hiện ở giữa màn hình
- [ ] Resize cửa sổ → đóng → mở lại → vẫn ở giữa (vì luôn center khi khởi động)
- [ ] Test trên multi-monitor nếu có thể

---
Next Phase: [phase-02-fix-alarm.md](./phase-02-fix-alarm.md)
