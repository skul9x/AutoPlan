# AutoPlan - Công cụ Tự động hóa Thông minh

AutoPlan là một công cụ tự động hóa mạnh mẽ được viết bằng Python, cho phép thực hiện các quy trình công việc phức tạp dựa trên các kế hoạch được định nghĩa sẵn trong các file Markdown. Dự án tích hợp khả năng nhận diện hình ảnh, tương tác giao diện và hệ thống báo thức thông minh để tối ưu hóa năng suất làm việc.

## 🌟 Tính năng chính

- **Thực thi theo kế hoạch**: Chạy các bước tự động hóa dựa trên file Markdown.
- **Nhận diện hình ảnh**: Sử dụng OpenCV để tìm kiếm và tương tác với các thành phần trên màn hình.
- **Hệ thống báo thức (Stealth Alarm)**: Phát nhạc MP3 lặp lại khi hoàn thành công việc, dừng bằng phím nóng (F12).
- **Quản lý cấu hình**: Tự động lưu và tải các thiết lập người dùng (vùng quét, file báo thức, đường dẫn kế hoạch).
- **Giao diện thân thiện**: Xây dựng trên nền tảng Tkinter, dễ dàng điều chỉnh và theo dõi trạng thái.

## 🛠️ Công nghệ sử dụng

- **Ngôn ngữ chính**: Python 3.x
- **Giao diện (UI)**: `tkinter`
- **Tự động hóa & Tương tác**: `pyautogui`, `pynput`
- **Xử lý hình ảnh**: `opencv-python` (cv2), `mss`, `PIL` (Pillow)
- **Âm thanh**: `pygame`
- **Quản lý dữ liệu**: `json`, `os`, `shutil` (Atomic saving)

## 📂 Cấu trúc dự án

```text
python_app/
├── main.py              # Điểm khởi đầu của ứng dụng
├── engine.py            # Logic cốt lõi thực thi các bước tự động hóa
├── ui_components.py     # Thành phần giao diện người dùng (Dashboard)
├── alarm_manager.py     # Quản lý âm thanh báo thức và phím nóng F12
├── settings_manager.py  # Lưu trữ và tải cấu hình người dùng (config.json)
├── file_manager.py      # Tiện ích quản lý file và thư mục kế hoạch
├── plans/               # Thư mục chứa các file kế hoạch (.md)
├── .brain/              # Lưu trữ kiến thức và bộ nhớ của hệ thống
└── requirements.txt     # Danh sách các thư viện cần thiết
```

## 🚀 Hướng dẫn cài đặt

1. **Clone repository**:
   ```bash
   git clone https://github.com/skul9x/AutoPlan.git
   cd AutoPlan/python_app
   ```

2. **Tạo môi trường ảo và cài đặt thư viện**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   # Hoặc venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **Yêu cầu hệ thống (Linux)**:
   Nếu bạn sử dụng Linux, hãy đảm bảo đã cài đặt các thư viện cần thiết cho Tkinter và X11:
   ```bash
   sudo apt-get install python3-tk scrot
   ```

## 📖 Cách sử dụng

1. Chạy ứng dụng: `python main.py`
2. Chọn thư mục chứa các file kế hoạch Markdown.
3. Cấu hình vùng quét màn hình (Scan Region) và Icon cần tìm kiếm.
4. (Tùy chọn) Bật chế độ Báo thức và chọn file MP3.
5. Nhấn **Start** để bắt đầu quy trình tự động hóa.
6. Khi báo thức kêu, nhấn **F12** để dừng nhạc.

## ⚖️ Bản quyền

Copyright 2026 Nguyễn Duy Trường
