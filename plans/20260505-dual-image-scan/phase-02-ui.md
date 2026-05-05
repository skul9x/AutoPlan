# Phase 02: UI - Thêm ô chọn Ảnh lỗi

**Status:** ✅ Done  
**Dependencies:** Phase 01 (settings có key `error_icon_path`)  
**File:** `ui_components.py`

---

## Mục tiêu

Thêm dòng Browse "Ảnh lỗi" vào giao diện, **phía trên** dòng icon hiện tại. Đổi label cho rõ ràng. Save/Load path mới.

## Layout sau khi sửa

```
┌─────────────────────────────────────────────────┐
│  MD Files Folder:    [____________] [Browse]    │  ← row 0 (giữ nguyên)
│  Ảnh lỗi (⚠️):      [____________] [Browse]    │  ← row 1 (MỚI)
│  Ảnh bình thường (➡️):[___________] [Browse]    │  ← row 2 (cũ, đổi row + label)
│  ┌─ Select Files to Execute: ─────────────────┐ │
│  │  file1.md                                   │ │
│  │  file2.md                       [Select All]│ │  ← row 3,4 (giữ nguyên, chỉ dịch row)
│  └─────────────────────────────────────────────┘ │
│  ... (phần còn lại dịch row xuống 1 bậc)        │
└─────────────────────────────────────────────────┘
```

## Các bước thực hiện

### 1. Thêm ô chọn "Ảnh lỗi" (row 1) vào `__init__`

**File:** `ui_components.py` → sau dòng 42 (kết thúc block folder selection)

**Thêm mới:**
```python
# Error icon selection (Ảnh lỗi - Ảnh điều kiện)
self.create_path_selector(
    "Ảnh lỗi (⚠️):", 
    "error_icon_path", 
    self.browse_error_icon, 
    1
)
```

### 2. Đổi label + row của icon hiện tại (từ row 1 → row 2)

**File:** `ui_components.py` → dòng 45-50

**Hiện tại:**
```python
# Icon selection
self.create_path_selector(
    "Icon Image (➡️):", 
    "icon_path", 
    self.browse_file, 
    1
)
```

**Sửa thành:**
```python
# Normal icon selection (Ảnh bình thường - trigger flow)
self.create_path_selector(
    "Ảnh bình thường (➡️):", 
    "icon_path", 
    self.browse_file, 
    2
)
```

### 3. Dịch tất cả row tiếp theo xuống +1

Vì thêm 1 row mới (row 1), tất cả các widget từ row 2 trở đi cần **dịch xuống 1**:

| Widget | Row cũ | Row mới |
|--------|--------|---------|
| "Select Files to Execute:" label | 2 | 3 |
| File Listbox | 3 | 4 |
| List buttons (Select All, Deselect All) | 3 | 4 |
| Region Selection frame | 4 | 5 |
| Alarm Settings frame | 5 | 6 |
| Control Buttons | 6 | 7 |
| "Log Output:" label | 7 | 8 |
| Log Area (scrolledtext) | 8 | 9 |
| `rowconfigure(8, weight=1)` | 8 | 9 |

**Tổng cộng:** Sửa ~10 chỗ `.grid(row=X)` → `row=X+1`.

### 4. Thêm hàm `browse_error_icon()`

**Thêm mới** vào class AppUI (gần hàm `browse_file`):
```python
def browse_error_icon(self):
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp"), ("All files", "*.*")]
    )
    if file_path:
        self.error_icon_path.delete(0, tk.END)
        self.error_icon_path.insert(0, file_path)
        self.log(f"Selected error icon: {file_path}")
        self.save_current_settings()
```

### 5. Cập nhật `save_current_settings()` - thêm key mới

**Hiện tại (dòng 190-196):**
```python
data = {
    "mru_md_folder": self.folder_path.get(),
    "mru_icon_link": self.icon_path.get(),
    ...
}
```

**Sửa thành:**
```python
data = {
    "mru_md_folder": self.folder_path.get(),
    "error_icon_path": self.error_icon_path.get(),   # ← THÊM MỚI
    "mru_icon_link": self.icon_path.get(),
    ...
}
```

### 6. Cập nhật `load_and_apply_settings()` - load key mới

**Thêm vào** sau block load `md_folder` (sau dòng 154):
```python
# 1.5. Error Icon Path
error_icon = self.validate_path(settings.get("error_icon_path", ""))
if error_icon:
    self.error_icon_path.delete(0, tk.END)
    self.error_icon_path.insert(0, error_icon)
```

### 7. Cập nhật `on_start()` - truyền error_icon_path vào engine

**Hiện tại (dòng 329):**
```python
self.engine.start(folder, selected_files, icon, region=self.scan_region)
```

**Sửa thành:**
```python
error_icon = self.error_icon_path.get()
self.engine.start(
    folder, selected_files, icon, 
    region=self.scan_region,
    error_icon_path=error_icon if error_icon and os.path.exists(error_icon) else None
)
```

**Lưu ý:** `error_icon_path` là **optional**. Nếu user không chọn ảnh lỗi, bot vẫn hoạt động bình thường như cũ (chỉ quét 1 ảnh).

## Kiểm tra

- [ ] Mở app → thấy 3 dòng Browse: MD Folder, Ảnh lỗi, Ảnh bình thường
- [ ] Chọn file ảnh cho "Ảnh lỗi" → hiển thị path trong ô
- [ ] Đóng app → mở lại → path "Ảnh lỗi" vẫn còn (đã save)
- [ ] Không chọn ảnh lỗi → nhấn START vẫn hoạt động bình thường (backward compatible)

---
**Next Phase:** → [Phase 03: Engine Logic](./phase-03-engine.md)
