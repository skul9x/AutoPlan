# AutoPlan - Công cụ Tự động hóa Thông minh

AutoPlan là một ứng dụng mạnh mẽ dựa trên Python, được thiết kế để tự động hóa các quy trình công việc phức tạp thông qua việc thực thi các kế hoạch được định nghĩa trong file Markdown. Ứng dụng tích hợp khả năng nhận diện hình ảnh thông minh, tương tác giao diện người dùng và hệ thống cảnh báo âm thanh để tối ưu hóa hiệu suất làm việc.

## 🌟 Tính năng chính

- **Thực thi theo kế hoạch**: Tự động hóa các thao tác chuột và bàn phím dựa trên các bước được mô tả trong file Markdown.
- **Nhận diện hình ảnh (OpenCV)**: Tìm kiếm chính xác các icon hoặc thành phần giao diện trên màn hình với độ tin cậy cao.
- **Tùy chỉnh Prompt Template**: Hỗ trợ thiết lập mẫu câu lệnh động (sử dụng `{xxx}` làm biến đường dẫn), cho phép linh hoạt ra lệnh cho các AI khác nhau (như Cursor, Cline) thay vì hardcode.
- **Hệ thống báo thức Stealth**: Tự động phát nhạc MP3 khi hoàn thành nhiệm vụ và hỗ trợ dừng nhanh bằng phím nóng (**F12**).
- **Dừng khẩn cấp (Panic Stop)**: Sử dụng phím nóng (**F9**) để dừng ngay lập tức mọi hoạt động tự động hóa.
- **Quản lý vùng quét**: Cho phép người dùng giới hạn khu vực tìm kiếm hình ảnh trên màn hình để tăng tốc độ và độ chính xác.
- **Lưu trữ cấu hình**: Tự động ghi nhớ các thiết lập như đường dẫn thư mục, icon, vùng quét, mẫu prompt và cài đặt báo thức.

## 🛠️ Công nghệ sử dụng

- **Ngôn ngữ**: [Python 3.x](https://www.python.org/)
- **Giao diện người dùng**: `tkinter` (Thư viện UI tiêu chuẩn của Python)
- **Tự động hóa**: `pyautogui`, `pynput`
- **Xử lý hình ảnh**: `opencv-python` (cv2), `mss`, `Pillow` (PIL)
- **Âm thanh**: `pygame`
- **Quản lý hệ thống**: `json`, `os`, `shutil`

## 📂 Cấu trúc thư mục

```text
python_app/
├── main.py              # Điểm khởi đầu của ứng dụng
├── engine.py            # Logic điều phối quy trình tự động hóa
├── bot_core.py          # Thư viện tương tác cấp thấp (click, type, find)
├── ui_components.py     # Giao diện điều khiển chính (Dashboard)
├── alarm_manager.py     # Quản lý âm thanh và phím nóng kết thúc
├── hotkey.py            # Xử lý phím nóng dừng khẩn cấp (F9)
├── region_selector.py   # Công cụ chọn vùng quét màn hình
├── settings_manager.py  # Quản lý cấu hình (config.json)
├── file_manager.py      # Tiện ích quản lý danh sách file kế hoạch
├── patch_utils.py       # Sửa lỗi môi trường (ví dụ: chụp ảnh trên Linux)
├── plans/               # Chứa các file kế hoạch (.md)
├── .brain/              # Thư mục lưu trữ kiến thức và lịch sử hệ thống
└── requirements.txt     # Danh sách các thư viện phụ thuộc
```

## 🚀 Hướng dẫn cài đặt

### 1. Tải dự án
```bash
git clone https://github.com/skul9x/AutoPlan.git
cd AutoPlan/python_app
```

### 2. Thiết lập môi trường
Khuyên dùng môi trường ảo để tránh xung đột thư viện:
```bash
python3 -m venv venv
source venv/bin/activate  # Trên Linux/macOS
# Hoặc: venv\Scripts\activate  # Trên Windows
```

### 3. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### 4. Yêu cầu hệ thống bổ sung (Linux)
Nếu bạn đang sử dụng Linux, hãy cài đặt các gói cần thiết sau:
```bash
sudo apt-get update
sudo apt-get install python3-tk scrot
```

## 📖 Cách sử dụng

1. **Khởi động**: Chạy lệnh `python main.py`.
2. **Chọn kế hoạch**: Chỉ định thư mục chứa các file `.md` trong mục "MD Files Folder".
3. **Cài đặt Icon**: Chọn ảnh icon mốc (trigger) và ảnh lỗi (nếu có).
4. **Chọn vùng quét**: Nhấn "Select Scan Area" để giới hạn vùng tìm kiếm nếu cần.
5. **Bắt đầu**: Nhấn **START AUTO**.
6. **Kiểm soát**:
   - Nhấn **F9** để dừng khẩn cấp.
   - Khi báo thức hoàn thành kêu, nhấn **F12** để tắt nhạc.

## ⚖️ Bản quyền

Copyright 2026 Nguyễn Duy Trường
