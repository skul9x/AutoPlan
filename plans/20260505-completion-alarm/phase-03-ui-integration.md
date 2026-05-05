# Phase 03: UI & Settings Integration

## Objective
Cung cấp giao diện cho người dùng cấu hình tính năng báo thức và lưu lại để không phải chọn lại mỗi lần mở app.

## Requirements
- [x] Thêm checkbox "Enable Alarm on Finish" vào UI.
- [x] Thêm nút "Browse MP3" và hiển thị đường dẫn file đã chọn.
- [x] Tích hợp logic MRU cho "MD files folder": Nhớ đường dẫn gần nhất, nếu chưa có thì mặc định là Desktop.
- [x] Lưu `alarm_enabled` và `alarm_mp3_path` vào `settings_manager`.

## Implementation Steps
1. **Cập nhật `ui_components.py`:**
   - Thêm các widget mới vào phần "Settings" hoặc "Control Panel".
   - Dùng `tkinter.filedialog.askopenfilename` để chọn file MP3.
   - Kết nối sự kiện thay đổi UI với việc lưu settings.

2. **Cập nhật `settings_manager.py`:**
   - Đảm bảo các key mới được khởi tạo mặc định.
   - Hàm `load_settings` sẽ trả về Desktop nếu key `mru_md_folder` trống.
   - Hàm `save_settings` phải cập nhật `mru_md_folder` mỗi khi người dùng chọn thư mục mới.

## Files to Create/Modify
- `ui_components.py` - Thêm giao diện cấu hình.
- `settings_manager.py` - Lưu trữ cấu hình mới.

## Test Criteria
- [x] Chọn file MP3 xong, tắt app mở lại vẫn thấy đường dẫn file cũ.
- [x] Có thể bật/tắt tính năng báo thức qua giao diện.

---
Next Phase: [Phase 04: Final Test & Packaging](phase-04-final-test.md)
