# Plan: Thay đổi Automation Sequence - Template Prompt v1.1
Created: 2026-05-06
Status: 🟡 In Progress

## Overview
Thay thế logic gõ lệnh `/vietcod` truyền thống bằng việc dán một đoạn text prompt hoàn chỉnh chứa đường dẫn đầy đủ của file kế hoạch. Điều này giúp tích hợp tốt hơn với các AI tool yêu cầu ngữ cảnh chi tiết ngay từ đầu. Nội dung prompt có thể tùy chỉnh từ giao diện UI.

## Quyết định thiết kế (Design Decisions)
1. **Flow mới:** `Ctrl+Shift+L` -> `Paste Template Prompt (đã thay thế {xxx} bằng absolute_path)` -> Chờ 0.5s -> `Enter`.
2. **File Info:** Dùng đường dẫn đầy đủ (absolute path) như logic cũ.
3. **Tùy biến:** Cấu hình prompt được thêm vào phần giao diện để người dùng có thể thoải mái thay đổi.
4. **Hotkeys:** Giữ nguyên `Ctrl + Shift + L`.

## Tech Stack
- Python (PyAutoGUI, Pyperclip)
- Tkinter (UI)

## Phases

| Phase | Name | Status | Progress |
|-------|------|--------|----------|
| 01 | Settings Support | ⬜ Pending | 0% |
| 02 | Bot Core Logic | ⬜ Pending | 0% |
| 03 | UI Components | ⬜ Pending | 0% |
| 04 | Testing | ⬜ Pending | 0% |

## Quick Commands
- Start Phase 1: `/code phase-01`
- Check progress: `/next`
