# Phase 02: Alarm Manager Logic

## Objective
Xây dựng module `alarm_manager.py` để quản lý việc phát nhạc và lắng nghe phím dừng một cách chuyên nghiệp, không làm treo ứng dụng chính.

## Requirements
- [x] Class `AlarmManager` hỗ trợ các hàm: `start_alarm(mp3_path)`, `stop_alarm()`.
- [x] Chạy việc lắng nghe phím F12 trong một Thread riêng.
- [x] Tích hợp vào `AutomationEngine` để tự động gọi khi xong việc.

## Implementation Steps
1. **Tạo `alarm_manager.py`:**
   - Sử dụng `pygame.mixer` để điều khiển nhạc.
   - Sử dụng `pynput.keyboard.Listener` để bắt phím F12.
   - Đảm bảo nhạc dừng và listener cũng dừng khi `stop_alarm` được gọi.

2. **Chỉnh sửa `engine.py`:**
   - Import `AlarmManager`.
   - Trong `_run_loop`, sau khi hoàn thành tất cả file, kiểm tra xem người dùng có bật báo thức không.
   - Nếu có, gọi `alarm_manager.start_alarm()`.

## Files to Create/Modify
- `alarm_manager.py` (New) - Logic cốt lõi của báo thức.
- `engine.py` - Gọi báo thức khi kết thúc.

## Test Criteria
- [x] Khi bot chạy xong, nhạc tự động nổi lên.
- [x] Đang nghe nhạc, nhấn F12 nhạc tắt và bot kết thúc trạng thái "Running" hoàn toàn.

---
Next Phase: [Phase 03: UI & Settings Integration](phase-03-ui-integration.md)
