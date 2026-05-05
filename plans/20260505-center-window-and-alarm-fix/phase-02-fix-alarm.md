# Phase 02: Fix Alarm Not Playing
Status: ✅ Completed
Dependencies: None (có thể làm song song với Phase 01)

## Objective
Fix bug khiến nhạc báo thức KHÔNG BAO GIỜ phát khi bot hoàn thành công việc.

## Root Cause (Chi tiết)

### Luồng lỗi hiện tại:
```
1. User bật checkbox "Enable Alarm" ✅
2. User chọn file MP3 ✅
3. User nhấn START → gọi on_start() 
4. on_start() gọi engine.start(...) ❌ THIẾU alarm_enabled và alarm_path
5. engine.start() nhận alarm_enabled=False (default) 
6. engine._run_loop() kiểm tra: if False and "": → SKIP
7. Kết quả: Không phát nhạc ❌
```

### Code lỗi - `ui_components.py` dòng 354-359:
```python
error_icon = self.error_icon_path.get()
self.engine.start(
    folder, selected_files, icon, 
    region=self.scan_region,
    error_icon_path=error_icon if error_icon and os.path.exists(error_icon) else None
    # ❌ THIẾU: alarm_enabled
    # ❌ THIẾU: alarm_path
)
```

### Code nhận - `engine.py` dòng 22:
```python
def start(self, folder_path, md_files, icon_path, region=None, 
          error_icon_path=None, alarm_enabled=False, alarm_path=""):
    # alarm_enabled luôn = False vì UI không truyền
    # alarm_path luôn = "" vì UI không truyền
```

## Implementation Steps

### 1. [ ] Sửa `on_start()` trong `ui_components.py` — Truyền alarm params
**File:** `ui_components.py`, method `on_start()` (dòng ~354-359)

```python
# TRƯỚC (thiếu params):
error_icon = self.error_icon_path.get()
self.engine.start(
    folder, selected_files, icon, 
    region=self.scan_region,
    error_icon_path=error_icon if error_icon and os.path.exists(error_icon) else None
)

# SAU (đầy đủ params):
error_icon = self.error_icon_path.get()
alarm_mp3 = self.alarm_path_entry.get()
self.engine.start(
    folder, selected_files, icon, 
    region=self.scan_region,
    error_icon_path=error_icon if error_icon and os.path.exists(error_icon) else None,
    alarm_enabled=self.alarm_enabled.get(),
    alarm_path=alarm_mp3 if alarm_mp3 and os.path.exists(alarm_mp3) else ""
)
```

### 2. [ ] Thêm log message khi alarm được bật
**File:** `ui_components.py`, method `on_start()`, sau khi gọi `engine.start()`

```python
if self.alarm_enabled.get():
    alarm_mp3 = self.alarm_path_entry.get()
    if alarm_mp3 and os.path.exists(alarm_mp3):
        self.log(f"🔔 Alarm enabled. File: {os.path.basename(alarm_mp3)}")
    else:
        self.log("⚠️ Alarm bật nhưng chưa chọn file MP3 hợp lệ!")
```

### 3. [ ] Verify `engine.py` _run_loop logic (Chỉ đọc, không sửa)
Kiểm tra lại dòng 88-95 trong `engine.py` — logic này đã đúng sẵn:
```python
if self.is_running:
    self.log_callback("Hoàn thành xử lý tất cả các file.")
    if alarm_enabled and alarm_path:  # ← Sẽ đúng khi nhận được params
        self.log_callback("Đang kích hoạt báo thức... (Nhấn F12 để dừng)")
        self.alarm.start_alarm(alarm_path)
        while self.is_running and self.alarm.is_playing:
            time.sleep(0.5)
```
→ Logic engine đã OK, chỉ cần UI truyền đúng params là hoạt động.

## Files to Create/Modify
- `ui_components.py` — Sửa method `on_start()`: thêm `alarm_enabled` + `alarm_path` vào `engine.start()`

## Test Criteria
- [ ] Bật alarm + chọn MP3 + chạy bot → khi xong → nghe thấy nhạc
- [ ] Bật alarm nhưng KHÔNG chọn MP3 → khi xong → log cảnh báo, không crash
- [ ] TẮT alarm → khi xong → không phát nhạc (behavior bình thường)
- [ ] Nhấn F12 khi đang phát nhạc → nhạc dừng

---
Next Phase: [phase-03-testing.md](./phase-03-testing.md)
