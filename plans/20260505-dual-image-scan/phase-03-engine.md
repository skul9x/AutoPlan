# Phase 03: Engine - Logic quét 2 ảnh có điều kiện

**Status:** ✅ Completed  
**Dependencies:** Phase 01 + 02  
**File:** `engine.py`

---

## Mục tiêu

Sửa vòng lặp quét icon trong `engine.py` để hỗ trợ logic:
1. Quét ảnh lỗi trước → nếu thấy → chờ 0.1 giây, **không quét ảnh bình thường**
2. Nếu không thấy ảnh lỗi → quét ảnh bình thường → nếu thấy → bắt đầu flow

## Flowchart logic mới

```
         ┌──────────────────┐
         │  Bắt đầu vòng lặp │
         └────────┬─────────┘
                  ▼
         ┌──────────────────┐
         │ Có error_icon_path│
         │  được cấu hình?  │
         └──┬──────────┬────┘
           Có         Không
            ▼           │
    ┌───────────────┐   │
    │ Quét ảnh lỗi  │   │
    └──┬────────┬───┘   │
     Thấy    Không thấy │
      ▼         ▼       │
  ┌────────┐   ┌────────┤
  │Log lỗi │   │        │
  │Sleep0.1│   ▼        ▼
  │continue│  ┌──────────────┐
  └────────┘  │ Quét ảnh     │
              │ bình thường  │
              └──┬───────┬───┘
               Thấy   Không thấy
                ▼         ▼
           ┌────────┐  ┌──────────┐
           │ BREAK  │  │ Sleep 0.1│
           │→ Flow  │  │ → Lặp lại│
           └────────┘  └──────────┘
```

## Các bước thực hiện

### 1. Sửa signature hàm `start()` - nhận thêm `error_icon_path`

**File:** `engine.py` → dòng 22

**Hiện tại:**
```python
def start(self, folder_path, md_files, icon_path, region=None, alarm_enabled=False, alarm_path=""):
```

**Sửa thành:**
```python
def start(self, folder_path, md_files, icon_path, region=None, error_icon_path=None, alarm_enabled=False, alarm_path=""):
```

### 2. Sửa hàm `start()` - truyền param vào thread

**Hiện tại (dòng 27-29):**
```python
self.thread = threading.Thread(
    target=self._run_loop, 
    args=(folder_path, md_files, icon_path, region, alarm_enabled, alarm_path),
    daemon=True
)
```

**Sửa thành:**
```python
self.thread = threading.Thread(
    target=self._run_loop, 
    args=(folder_path, md_files, icon_path, region, error_icon_path, alarm_enabled, alarm_path),
    daemon=True
)
```

### 3. Sửa signature hàm `_run_loop()` - nhận thêm `error_icon_path`

**Hiện tại (dòng 39):**
```python
def _run_loop(self, folder_path, md_files, icon_path, region, alarm_enabled, alarm_path):
```

**Sửa thành:**
```python
def _run_loop(self, folder_path, md_files, icon_path, region, error_icon_path, alarm_enabled, alarm_path):
```

### 4. ⭐ Sửa vòng lặp chờ icon (PHẦN CHÍNH)

**Hiện tại (dòng 53-57) - Vòng lặp "đợi thấy icon":**
```python
# Bước 1: Đợi cho đến khi thấy Icon
while self.is_running:
    if self.bot.is_icon_visible(icon_path, region=region):
        break
    time.sleep(0.1)
```

**Sửa thành:**
```python
# Bước 1: Đợi icon với logic quét 2 ảnh
while self.is_running:
    # 1a. Nếu có ảnh lỗi → kiểm tra trước
    if error_icon_path and self.bot.is_icon_visible(error_icon_path, region=region):
        self.log_callback("⚠️ Phát hiện ảnh lỗi! Quét lại ngay...")
        time.sleep(0.1)
        continue  # Quay lại đầu vòng lặp, KHÔNG quét ảnh bình thường
    
    # 1b. Không thấy ảnh lỗi (hoặc không có ảnh lỗi) → quét ảnh bình thường
    if self.bot.is_icon_visible(icon_path, region=region):
        break  # Thoát vòng lặp → bắt đầu flow làm việc
    
    time.sleep(0.1)
```

### 5. Thêm log thông tin khi bắt đầu

**Hiện tại (dòng 51):**
```python
self.log_callback(f"Đang chờ icon hiển thị{region_info} để xử lý: {file_name}")
```

**Sửa thành:**
```python
error_info = " (có kiểm tra ảnh lỗi)" if error_icon_path else ""
self.log_callback(f"Đang chờ icon hiển thị{region_info}{error_info} để xử lý: {file_name}")
```

## Logic đảm bảo Backward Compatible

Nếu `error_icon_path` là `None` (user không chọn ảnh lỗi):
```python
if error_icon_path and self.bot.is_icon_visible(error_icon_path, region=region):
#   ↑ False → short-circuit → bỏ qua hoàn toàn
```
→ Bot hoạt động **y hệt** phiên bản cũ. Không ảnh hưởng user hiện tại.

## Kiểm tra

- [ ] **Không có ảnh lỗi:** Bot hoạt động bình thường như trước (chỉ quét 1 ảnh)
- [ ] **Có ảnh lỗi + ảnh lỗi ĐANG hiện:** Bot log "Phát hiện ảnh lỗi!", chờ 0.1s, quét lại
- [ ] **Có ảnh lỗi + ảnh lỗi BIẾN MẤT:** Bot bắt đầu quét ảnh bình thường
- [ ] **Có ảnh lỗi + ảnh bình thường hiện:** Bot bắt đầu flow làm việc
- [ ] **Nhấn STOP giữa chừng:** Bot dừng ngay, không bị treo

## Tình huống đặc biệt (Edge Cases)

| Tình huống | Xử lý |
|------------|--------|
| Cả 2 ảnh cùng xuất hiện | Ảnh lỗi ưu tiên → chờ 0.1s (vì quét ảnh lỗi trước) |
| Ảnh lỗi nhấp nháy liên tục | Bot sẽ log + chờ 0.1s mỗi lần thấy, cho đến khi ảnh lỗi hết |
| File ảnh lỗi bị xóa giữa chừng | `is_icon_visible` sẽ catch exception → return False → bỏ qua |

---
**Hoàn thành plan!** Quay lại → [plan.md](./plan.md)
