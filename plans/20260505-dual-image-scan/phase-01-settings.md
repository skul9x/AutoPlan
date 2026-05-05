# Phase 01: Settings & Data Layer

**Status:** ✅ Completed  
**Dependencies:** Không  
**File:** `settings_manager.py`

---

## Mục tiêu

Thêm key `error_icon_path` vào hệ thống settings để lưu đường dẫn ảnh lỗi giữa các lần chạy.

## Các bước thực hiện

### 1. Thêm key mới vào `DEFAULT_SETTINGS`

**File:** `settings_manager.py` → dòng 7-13

**Hiện tại:**
```python
DEFAULT_SETTINGS = {
    "mru_md_folder": "",
    "mru_icon_link": "",
    "scan_region": None,
    "alarm_enabled": False,
    "alarm_mp3_path": ""
}
```

**Sửa thành:**
```python
DEFAULT_SETTINGS = {
    "mru_md_folder": "",
    "error_icon_path": "",       # ← THÊM MỚI: path ảnh lỗi (ảnh điều kiện)
    "mru_icon_link": "",         # path ảnh bình thường (ảnh trigger flow)
    "scan_region": None,
    "alarm_enabled": False,
    "alarm_mp3_path": ""
}
```

### 2. Không cần sửa gì thêm

Vì `settings_manager.py` dùng cơ chế `DEFAULT_SETTINGS.copy() + update(loaded_data)` (dòng 80-82), key mới sẽ **tự động** được merge khi load config cũ. Không cần migration script.

## Kiểm tra

- [ ] `load_settings()` trả về dict có key `error_icon_path` (dù config.json cũ chưa có key này)
- [ ] `save_settings()` lưu được `error_icon_path` vào config.json
- [ ] Mở lại app → giá trị `error_icon_path` vẫn còn

## Ghi chú

- Đặt `error_icon_path` **trước** `mru_icon_link` trong dict để sau này đọc code dễ hiểu thứ tự: ảnh lỗi trước, ảnh bình thường sau (khớp với thứ tự trên UI).

---
**Next Phase:** → [Phase 02: UI](./phase-02-ui.md)
