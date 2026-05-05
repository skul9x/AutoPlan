# AutoPlan - Công cụ Tự động hóa Quy trình theo Kế hoạch

AutoPlan là một ứng dụng Python mạnh mẽ giúp tự động hóa các tác vụ trên máy tính bằng cách đọc các tệp kế hoạch Markdown (.md) và thực hiện các thao tác chuột/bàn phím tương ứng khi phát hiện các biểu tượng mục tiêu trên màn hình.

## 🌟 Tính năng chính

- **Quét kế hoạch thông minh**: Tự động liệt kê các tệp kế hoạch trong thư mục được chọn (loại bỏ tệp cấu hình `plan.md`).
- **Nhận diện hình ảnh**: Sử dụng thị giác máy tính để tìm kiếm icon mục tiêu trên màn hình.
- **Tự động hóa nâng cao**: Thực hiện chuỗi lệnh `/vietcode` phức tạp bao gồm phím tắt, nhập văn bản và dán đường dẫn tệp.
- **Vùng quét tùy chỉnh**: Cho phép người dùng giới hạn khu vực quét màn hình để tăng tốc độ và độ chính xác.
- **Dừng khẩn cấp**: Phím nóng (mặc định F9) cho phép dừng ngay lập tức quá trình tự động hóa nếu có sự cố.
- **Giao diện hiện đại**: GUI được thiết kế bằng Tkinter trực quan, dễ sử dụng.
- **Bảo mật & Riêng tư**: Không lưu lại đường dẫn thư mục làm việc giữa các phiên làm việc để đảm bảo tính riêng tư.

## 🛠️ Công nghệ sử dụng

- **Ngôn ngữ**: Python 3.x
- **Thư viện chính**:
  - `Tkinter`: Xây dựng giao diện đồ họa người dùng.
  - `PyAutoGUI`: Thực hiện các thao tác di chuột, click và nhấn phím.
  - `OpenCV-Python`: Hỗ trợ nhận diện hình ảnh với độ chính xác cao (confidence).
  - `Pynput`: Quản lý và lắng nghe các phím nóng toàn cục.
  - `MSS`: Chụp ảnh màn hình hiệu suất cao, tối ưu cho đa nền tảng.
  - `Pyperclip`: Quản lý clipboard an toàn trên Linux và Windows.

## 📁 Cấu trúc thư mục

```text
python_app/
├── main.py            # Điểm khởi đầu của ứng dụng
├── ui_components.py    # Quản lý giao diện người dùng Tkinter
├── bot_core.py        # Logic lõi điều khiển chuột/bàn phím
├── engine.py          # Bộ điều phối luồng thực thi
├── file_manager.py     # Quản lý quét và lọc tệp .md
├── settings_manager.py # Lưu trữ cấu hình ứng dụng
├── hotkey.py          # Xử lý phím nóng dừng khẩn cấp
├── region_selector.py  # Công cụ chọn vùng quét màn hình
├── patch_utils.py     # Các bản vá tối ưu hệ thống
└── requirements.txt    # Danh sách thư viện phụ thuộc
```

## 🚀 Hướng dẫn cài đặt

1. **Clone repository**:
   ```bash
   git clone https://github.com/skul9x/AutoPlan.git
   cd AutoPlan/python_app
   ```

2. **Tạo môi trường ảo (Khuyến nghị)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # hoặc
   venv\Scripts\activate     # Windows
   ```

3. **Cài đặt các thư viện phụ thuộc**:
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Cách sử dụng

1. **Khởi chạy ứng dụng**:
   ```bash
   python main.py
   ```
2. **Cấu hình**:
   - Nhấn **Browse** tại mục "MD Files Folder" để chọn thư mục chứa các tệp kế hoạch.
   - Nhấn **Browse** tại mục "Icon Image" để chọn ảnh icon mục tiêu (ví dụ: mũi tên ➡️).
   - (Tùy chọn) Nhấn **Select Scan Area** để chọn vùng cụ thể trên màn hình.
3. **Thực thi**:
   - Chọn các tệp kế hoạch bạn muốn chạy trong danh sách.
   - Nhấn **START AUTO**. Ứng dụng sẽ chờ đợi cho đến khi icon mục tiêu xuất hiện để thực thi lệnh.
4. **Dừng lại**:
   - Nhấn **F9** bất kỳ lúc nào để dừng khẩn cấp quá trình tự động.

## ⚠️ Lưu ý bảo mật

- Tuyệt đối không lưu trữ API Key hoặc thông tin nhạy cảm trong các tệp `.md` hoặc mã nguồn.
- Ứng dụng đã được cấu hình để không tự động lưu lại đường dẫn thư mục làm việc để bảo vệ dữ liệu của bạn.

## 📝 Bản quyền

Copyright 2026 Nguyễn Duy Trường
