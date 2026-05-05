# Phase 03: Command & Terminal Integration
Status: ✅ Completed

## Objective
Tự động gửi lệnh `/vietcode` vào Terminal sau khi AI xong.

## Implementation Steps
1. [x] Lấy đường dẫn file từ hàng đợi của Webview.
2. [x] Thực hiện chuỗi lệnh tối ưu:
    - Focus vào ô nhập liệu bằng Command ID tìm được ở Phase 2.
    - Gửi text `/vietcode <path>` trực tiếp thay vì gõ phím + dán (để tránh lỗi clipboard trên Linux như code Python cũ).
3. [x] Xây dựng hàm `delay(ms)` để xử lý các khoảng nghỉ cần thiết (tương tự `time.sleep` trong code cũ nhưng không làm treo IDE).
4. [x] Tạo một `EventEmitter` để quản lý hàng đợi (Queue) các file `.md` cần chạy.

## Files to Create/Modify
- `src/commandExecutor.ts` - Logic gửi lệnh vào terminal.

## Test Criteria
- Sau khi AI xong, Terminal tự động hiện dòng chữ `/vietcode path/to/file.md` và thực thi.
