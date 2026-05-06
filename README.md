# AutoPlan - Công cụ tự động hóa quy trình theo kế hoạch

AutoPlan là một ứng dụng máy tính mạnh mẽ được xây dựng bằng Python, giúp tự động hóa việc thực thi các chuỗi hành động (typing, pasting, command execution) dựa trên việc nhận diện hình ảnh trên màn hình. Dự án này được thiết kế đặc biệt để hỗ trợ các quy trình làm việc lặp đi lặp lại một cách thông minh và an toàn.

## ✨ Tính năng chính

- **Nhận diện hình ảnh thông minh**: Sử dụng OpenCV để quét và tìm kiếm các icon kích hoạt trên màn hình với độ chính xác cao.
- **Tự động hóa phím tắt**: Thực hiện các chuỗi phím tắt phức tạp (`Ctrl + Shift + L`, dán template, `Enter`) hoàn toàn tự động.
- **Quản lý vùng quét (Region Selection)**: Cho phép giới hạn vùng tìm kiếm trên màn hình để tăng tốc độ và tránh nhận diện nhầm.
- **Cơ chế dừng khẩn cấp (Panic Stop)**: Nhấn phím `F9` để dừng ngay lập tức mọi hoạt động của bot.
- **Hỗ trợ Clipboard đa nền tảng**: Tự động chuyển đổi giữa `pyperclip` và `tkinter` để đảm bảo copy/paste hoạt động ổn định trên cả Windows và Linux.
- **Thông báo hoàn tất**: Tích hợp báo thức (MP3) để thông báo cho người dùng khi đã xử lý xong danh sách file.

## 🛠️ Công nghệ sử dụng

- **Ngôn ngữ**: Python 3.12+
- **Giao diện (GUI)**: Tkinter (với giao diện hiện đại, bảng log thời gian thực).
- **Tự động hóa**: PyAutoGUI, pynput (quản lý phím nóng).
- **Xử lý hình ảnh**: OpenCV (`opencv-python`), Pillow, mss (chụp ảnh màn hình tốc độ cao).
- **Âm thanh**: Pygame (quản lý báo thức).
- **Khác**: Pyperclip, JSON settings management.

## 🚀 Hướng dẫn cài đặt

1. **Clone repository**:
   ```bash
   git clone https://github.com/skul9x/AutoPlan.git
   cd AutoPlan
   ```

2. **Tạo và kích hoạt môi trường ảo (venv)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   # hoặc
   venv\Scripts\activate     # Windows
   ```

3. **Cài đặt các thư viện cần thiết**:
   ```bash
   pip install -r requirements.txt
   ```

   *Lưu ý cho người dùng Linux: Nếu gặp lỗi về Clipboard, hãy cài đặt xclip:*
   ```bash
   sudo apt-get install xclip
   ```

## 📖 Cách sử dụng

1. **Khởi chạy ứng dụng**:
   ```bash
   python main.py
   ```
2. **Cấu hình trên giao diện**:
   - Chọn thư mục chứa các file kế hoạch (`.md`).
   - Chọn ảnh icon dùng để kích hoạt (ảnh mẫu mà bot sẽ tìm kiếm trên màn hình).
   - (Tùy chọn) Chọn vùng quét trên màn hình để tối ưu hiệu suất.
   - Thiết lập nội dung Template (nếu dùng tính năng dán template).
3. **Bắt đầu**: Nhấn nút **▶️ START AUTO**. Bot sẽ chờ 2 giây để bạn chuyển sang cửa sổ làm việc.
4. **Dừng**: Nhấn **⏹️ STOP** trên giao diện hoặc phím nóng **F9** để dừng khẩn cấp.

## 📁 Cấu trúc thư mục

- `main.py`: Điểm khởi đầu của ứng dụng.
- `ui_components.py`: Chứa toàn bộ mã nguồn xây dựng giao diện người dùng.
- `engine.py`: Lõi xử lý vòng lặp tự động hóa.
- `bot_core.py`: Xử lý tương tác chuột, bàn phím và nhận diện hình ảnh.
- `hotkey.py`: Quản lý lắng nghe phím nóng dừng khẩn cấp.
- `region_selector.py`: Công cụ GUI để chọn vùng màn hình.
- `settings_manager.py`: Quản lý lưu trữ và tải cấu hình người dùng.
- `plans/`: Thư mục chứa các tài liệu kế hoạch và ghi chú.
- `.brain/`: Thư mục lưu trữ kiến thức và ngữ cảnh làm việc của AI (Eternal Context).

## 📄 Bản quyền

Copyright 2026 Nguyễn Duy Trường
