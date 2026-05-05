# Phase 03: Testing & Verification
Status: ✅ Completed
Dependencies: Phase 01 + Phase 02

## Objective
Kiểm tra cả 2 fix hoạt động đúng và không gây regression.

## Implementation Steps

### 1. [x] Test Center Window
```
Bước 1: Chạy app bằng lệnh: python main.py
Bước 2: Quan sát vị trí cửa sổ → PHẢI ở giữa màn hình
Bước 3: Resize cửa sổ, đóng và mở lại → vẫn center
```

### 2. [x] Test Alarm Flow (Manual)
```
Bước 1: Mở app
Bước 2: Tick checkbox "Enable Alarm on Finish"
Bước 3: Chọn 1 file MP3 hợp lệ
Bước 4: Chọn folder MD + icon + chạy START
Bước 5: Đợi bot xong → PHẢI nghe thấy nhạc phát
Bước 6: Nhấn F12 → nhạc PHẢI dừng
```

### 3. [x] Test Edge Cases
- [x] Alarm bật nhưng file MP3 không tồn tại → không crash, log cảnh báo
- [x] Alarm tắt → hoàn thành → không phát nhạc
- [x] User nhấn STOP giữa chừng → alarm không phát
- [x] Tất cả tính năng cũ vẫn hoạt động bình thường (regression test)

## Test Criteria
- [x] Window center OK
- [x] Alarm phát OK khi bật
- [x] Alarm không phát khi tắt
- [x] F12 dừng alarm OK
- [x] Không có regression trên các tính năng khác

## Notes
- Đây là 2 fix đơn giản, low-risk
- Phase 01 và Phase 02 có thể code cùng lúc trong 1 commit
- Tổng thay đổi: ~15 dòng code trong 1 file (`ui_components.py`)
