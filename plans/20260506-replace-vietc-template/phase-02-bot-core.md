# Phase 02: Bot Core Logic
Status: ✅ Completed

## Objective
Thay đổi logic gõ phím trong `bot_core.py` và cập nhật cách `engine.py` gọi hàm đó để truyền tham số template prompt.

## Implementation Steps
1. [x] Cập nhật hàm `input_vietcode_sequence` trong `bot_core.py` thành `input_template_sequence(self, file_path, template_prompt)`.
2. [x] Sửa logic của hàm mới:
   - Nhấn `Ctrl + Shift + L` và chờ (giống cũ).
   - Format lại `template_prompt`: thay thế chuỗi `{xxx}` bằng `file_path`.
   - Copy nội dung đã format vào clipboard qua `pyperclip.copy()`.
   - Dán (Ctrl+V) nội dung.
   - Chờ 0.5 giây.
   - Nhấn `Enter`.
3. [x] Cập nhật `engine.py` (hàm `start` và `_run_loop`) để nhận thêm tham số `template_prompt` và truyền nó cho `bot.input_template_sequence`.

## Files to Modify
- `bot_core.py`
- `engine.py`

## Test Criteria
- [x] Mã đã format sẽ thay thế `{xxx}` đúng bằng đường dẫn file.
- [x] Gửi lệnh thành công qua clipboard + Ctrl V + Enter.

---
Next Phase: `phase-03-ui.md`
