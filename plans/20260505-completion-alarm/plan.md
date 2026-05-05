# Plan: Completion Stealth Alarm
Created: 2026-05-05
Status: ✅ Completed

## Overview
Tính năng này sẽ phát một file MP3 lặp đi lặp lại khi bot hoàn thành công việc. Nhạc chỉ dừng khi người dùng nhấn phím **F12**. 
Mục đích là thông báo cho người dùng biết việc đã xong nhưng vẫn giữ vẻ ngoài như đang "bận rộn" (stealth mode).

## Tech Stack
- **Audio Library:** `pygame.mixer` (ổn định nhất cho việc loop MP3 cross-platform).
- **Hotkey Library:** `pynput` (đã có sẵn trong project, dùng để bắt phím F12 toàn cục).
- **Settings:** `SettingsManager` (để lưu đường dẫn file MP3 và trạng thái bật/tắt báo thức).

## Phases

| Phase | Name | Status | Progress |
|-------|------|--------|----------|
| 01 | Setup & Proof of Concept | ✅ Done | 100% |
| 02 | Alarm Manager Logic | ✅ Done | 100% |
| 03 | UI & Settings Integration | ✅ Done | 100% |
| 04 | Testing & Packaging | ✅ Done | 100% |

## Quick Commands
- Chạy test audio: `python scratch/test_audio.py`
- Kiểm tra Hotkey: `python scratch/test_hotkey.py`
- Bắt đầu Phase 1: `/code phase-01`
