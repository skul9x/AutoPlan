# Phase 01: Cập nhật UI Components
Status: ✅ Completed
Dependencies: None

## Objective
Tăng chiều cao mặc định của `log_area` trong `ui_components.py` và điều chỉnh kích thước cửa sổ chính để có không gian hiển thị log thoải mái hơn.

## Requirements
### Functional
- [ ] Tăng giá trị `height` của `scrolledtext.ScrolledText` (Log Output).
- [ ] Điều chỉnh kích thước cửa sổ khởi tạo (`650x650` lên `650x750` hoặc tương đương) để bù đắp phần chiều cao log tăng thêm.

## Implementation Steps
1. [ ] Sửa `ui_components.py`: 
   - Tìm dòng khởi tạo `self.log_area` và tăng `height` từ `8` lên `15` (hoặc con số phù hợp).
   - Cập nhật `self.root.geometry("650x750")` và hàm `center_window` để khớp với kích thước mới.
2. [ ] Lưu thay đổi và kiểm tra lỗi cú pháp.

## Files to Create/Modify
- `ui_components.py` - Cập nhật thông số kích thước UI.

## Test Criteria
- [ ] Chạy ứng dụng, cửa sổ hiện lên với chiều cao lớn hơn.
- [ ] Khu vực Log Output hiển thị được nhiều dòng văn bản hơn mà không cần cuộn ngay lập tức.
- [ ] Cửa sổ vẫn được căn giữa màn hình chính xác.
