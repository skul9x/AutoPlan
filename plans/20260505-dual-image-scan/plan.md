# Plan: Dual Image Scan (Quét 2 ảnh có điều kiện)

**Created:** 2026-05-05  
**Status:** 🟡 In Progress

---

## Overview

Thêm tính năng **quét 2 ảnh** vào AutoPlan:

- **Ảnh 1 (Ảnh lỗi):** Nếu thấy trên màn hình → bot biết đang có lỗi, **chờ 2 giây** rồi quét lại. Không quét ảnh 2.
- **Ảnh 2 (Ảnh bình thường):** Nếu KHÔNG thấy ảnh lỗi VÀ thấy ảnh này → bắt đầu flow làm việc (giống logic icon hiện tại).

Hai ảnh xuất hiện **cùng vùng** trên màn hình. Path của cả 2 ảnh được **lưu lại** cho lần dùng sau.

## Logic tóm tắt

```
while running:
    if thấy_ảnh_lỗi:
        log("Phát hiện lỗi, chờ 2s...")
        sleep(2)
        continue          ← quay lại đầu vòng lặp

    if thấy_ảnh_bình_thường:
        break             ← bắt đầu flow làm việc

    sleep(0.1)            ← không thấy gì, quét lại
```

## Danh sách file cần sửa

| File | Thay đổi |
|------|----------|
| `settings_manager.py` | Thêm key `error_icon_path` vào DEFAULT_SETTINGS |
| `ui_components.py` | Thêm dòng Browse "Ảnh lỗi" phía trên dòng icon hiện tại, đổi label icon cũ, save/load path mới |
| `engine.py` | Sửa `_run_loop` để quét 2 ảnh theo logic điều kiện, nhận thêm param `error_icon_path` |
| `bot_core.py` | Không cần sửa (đã có `is_icon_visible`) |

## Phases

| Phase | Name | Status | Files |
|-------|------|--------|-------|
| 01 | Settings & Data Layer | ⬜ Pending | `settings_manager.py` |
| 02 | UI - Thêm ô chọn Ảnh lỗi | ⬜ Pending | `ui_components.py` |
| 03 | Engine - Logic quét 2 ảnh | ⬜ Pending | `engine.py` |

**Tổng:** 3 phases nhỏ, ~15 thay đổi code | Độ phức tạp: 🟢 Đơn giản

## Quick Commands

- Bắt đầu Phase 1: `/code phase-01`
- Check progress: `/next`
