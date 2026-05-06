# Phase 04: Testing
Status: ✅ Completed

## Objective
Kiểm tra tổng thể toàn bộ hệ thống (E2E) đảm bảo flow mới hoạt động đúng.

## Implementation Steps
1. [x] Chạy lệnh `python main.py`.
2. [x] Kiểm tra giá trị default của Prompt Template có xuất hiện đúng trên UI không.
3. [x] Sửa giá trị `{xxx}` thành một đoạn text khác và kiểm tra lưu/load lại.
4. [x] Chạy thử Auto, chọn file ảnh đích và file Markdown.
5. [x] Quan sát bot dán văn bản:
   - Có nhấn Ctrl+Shift+L không?
   - Text được dán ra có đường dẫn đúng thay vì chữ `{xxx}` không?
   - Có chờ 0.5s và nhấn Enter không?

## Test Criteria
- [x] Toàn bộ flow chạy mượt mà, không crash.
- [x] Phù hợp hoàn toàn với yêu cầu của người dùng.
