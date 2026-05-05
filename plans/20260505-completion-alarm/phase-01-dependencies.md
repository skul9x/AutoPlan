# Phase 01: Setup & Proof of Concept

## Objective
Đảm bảo môi trường phát triển có đủ thư viện và kiểm tra khả năng phát nhạc MP3 + bắt phím F12 trên hệ điều hành hiện tại.

## Requirements
- [x] Cài đặt `pygame` vào `requirements.txt` và môi trường ảo.
- [x] Tạo script test nhỏ để phát nhạc MP3 lặp lại.
- [x] Tạo script test nhỏ để lắng nghe phím F12 ở chế độ nền (background).

## Implementation Steps
1. **Update Requirements:**
   - Thêm `pygame` vào `requirements.txt`.
   - Chạy `pip install pygame`.

2. **Audio Test Script (`scratch/test_audio.py`):**
   - Import `pygame`.
   - Load một file MP3 bất kỳ.
   - Play với tham số `-1` để lặp vô hạn.

3. **Hotkey Test Script (`scratch/test_hotkey.py`):**
   - Dùng `pynput.keyboard.Listener`.
   - In ra log khi nhấn phím F12.

## Files to Create/Modify
- `requirements.txt` - Thêm `pygame`.
- `scratch/test_audio.py` - Script test âm thanh.
- `scratch/test_hotkey.py` - Script test phím tắt.

## Test Criteria
- [ ] Nhạc MP3 phát được và tự động lặp lại khi hết bài.
- [ ] Nhấn F12 trong khi đang ở cửa sổ khác vẫn nhận được sự kiện (Global Hotkey).

---
Next Phase: [Phase 02: Alarm Manager Logic](phase-02-alarm-manager.md)
