# Plan: Center Window + Fix Alarm Not Playing
Created: 2026-05-05
Status: 🟡 In Progress

## Overview
Fix 2 bugs trong AutoPlan:

### Bug 1: Window không ở giữa màn hình
- **Hiện tượng:** Mở app → cửa sổ hiện ở góc trên bên trái (hoặc vị trí random)
- **Nguyên nhân:** `root.geometry("650x650")` chỉ set kích thước, KHÔNG set vị trí
- **Fix:** Tính toán tọa độ trung tâm màn hình rồi truyền vào geometry string `"650x650+x+y"`

### Bug 2: Nhạc không phát khi bot hoàn thành ⚠️ CRITICAL
- **Hiện tượng:** Bot chạy xong → không có âm thanh báo → user không biết đã xong
- **Nguyên nhân gốc (Root Cause):** 
  - `ui_components.py` dòng 355: `engine.start()` **KHÔNG truyền** `alarm_enabled` và `alarm_path`
  - `engine.py` dòng 22: method nhận `alarm_enabled=False, alarm_path=""` (default)
  - `engine.py` dòng 90: `if alarm_enabled and alarm_path:` → luôn `False` → KHÔNG BAO GIỜ phát nhạc
- **Fix:** Truyền `alarm_enabled` và `alarm_path` từ UI vào engine

## Root Cause Analysis

```
ui_components.py (on_start):
    self.engine.start(
        folder, selected_files, icon, 
        region=self.scan_region,
        error_icon_path=error_icon  
        # ❌ THIẾU: alarm_enabled=self.alarm_enabled.get()
        # ❌ THIẾU: alarm_path=self.alarm_path_entry.get()
    )

engine.py (start):
    def start(self, ..., alarm_enabled=False, alarm_path=""):
        #                    ↑ luôn False    ↑ luôn rỗng
        
engine.py (_run_loop):
    if alarm_enabled and alarm_path:  # ← Luôn False → skip
        self.alarm.start_alarm(alarm_path)  # ← Không bao giờ chạy
```

## Phases

| Phase | Name | Status | Progress |
|-------|------|--------|----------|
| 01 | Center Window on Screen | ⬜ Pending | 0% |
| 02 | Fix Alarm Parameters | ⬜ Pending | 0% |
| 03 | Testing & Verification | ⬜ Pending | 0% |

**Tổng:** 9 tasks | Ước tính: 1 session

## Quick Commands
- Start Phase 1: `/code phase-01`
- Check progress: `/next`
