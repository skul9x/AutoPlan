# Phase 04: Webview UI Development
Status: ✅ Done

## Objective
Xây dựng giao diện Webview hiện đại bên trong IDE để quản lý danh sách file và theo dõi tiến trình.

## Implementation Steps
1. [ ] Thiết kế giao diện HTML/CSS theo phong cách "Vibe UI" (Dark mode, Glassmorphism).
2. [ ] Hiển thị danh sách các file `.md` trong thư mục project với checkbox để chọn.
3. [ ] Xây dựng cơ chế **Message Passing**:
    - Webview -> Extension: Gửi danh sách file đã chọn khi nhấn "START".
    - Extension -> Webview: Cập nhật trạng thái log (giống Log Console cũ).
4. [ ] Thêm các nút điều khiển: START AUTO, STOP, và nút cấu hình thư mục.

## Files to Create/Modify
- `src/webviewPanel.ts` - Quản lý vòng đời của Webview.
- `media/main.css` - Styling cho giao diện.
- `media/main.js` - Logic tương tác phía Webview.

## Test Criteria
- Mở được Webview trong IDE.
- Click chọn file trên Webview và Extension nhận được danh sách đó.
- Giao diện đáp ứng tốt khi thay đổi kích thước cửa sổ IDE.
