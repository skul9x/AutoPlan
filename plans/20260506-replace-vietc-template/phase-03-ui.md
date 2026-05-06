# Phase 03: UI Components
Status: ✅ Done

## Objective
Thêm một giao diện nhập liệu để chỉnh sửa nội dung của `prompt_template` trong màn hình chính.

## Implementation Steps
1. [x] Mở `ui_components.py`.
2. [x] Trong hàm `__init__`, thêm một widget `Text` hoặc `ScrolledText` (kèm Label) với tiêu đề "Prompt Template:" dưới phần Alarm Settings hoặc ở vị trí thích hợp, chiều cao khoảng 4-5 dòng.
3. [x] Cập nhật hàm `load_and_apply_settings` để đọc `prompt_template` từ settings và đưa vào widget này.
4. [x] Cập nhật hàm `save_current_settings` để lấy nội dung từ widget và lưu vào settings.
5. [x] Cập nhật lời gọi `self.engine.start(...)` trong `on_start` để truyền giá trị `prompt_template` vào engine.
6. [x] Cân nhắc mở rộng chiều cao cửa sổ chính nếu cần (hiện tại là `650x750`, có thể lên `650x850`).

## Files to Modify
- `ui_components.py`

## Test Criteria
- [x] Có thể chỉnh sửa nội dung template trên giao diện và lưu lại.
- [x] Khi tắt app mở lại, nội dung template vẫn giữ nguyên.
- [x] Engine nhận được đúng nội dung mới nhất khi nhấn START.

---
Next Phase: `phase-04-testing.md`
