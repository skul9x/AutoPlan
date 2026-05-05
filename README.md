# 🚀 AutoPlan Runner (Advanced Python Edition)

**AutoPlan Runner** là một công cụ tự động hóa mạnh mẽ, được thiết kế để tối ưu hóa quy trình làm việc với các kế hoạch phát triển phần mềm (Markdown plans). Công cụ này sử dụng công nghệ nhận diện hình ảnh thông minh để tương tác với IDE hoặc bất kỳ ứng dụng nào, giúp thực thi các bước trong kế hoạch một cách tự động và chính xác.

---

## ✨ Tính năng nổi bật

### 🎨 Giao diện Hiện đại & Trực quan
- **Vibe UI**: Giao diện được thiết kế hiện đại, dễ sử dụng với các thông báo trạng thái thời gian thực.
- **Responsive Design**: Các thành phần giao diện linh hoạt, hỗ trợ theo dõi log chi tiết ngay trên ứng dụng.

### 🔍 Nhận diện Hình ảnh Thông minh
- **OpenCV Integration**: Sử dụng thuật toán so khớp mẫu (Template Matching) để tìm kiếm các biểu tượng (nút Run, Debug, v.v.) trên màn hình với độ chính xác cao.
- **Confidence Control**: Cho phép cấu hình độ tin cậy để tránh click nhầm các phần tử tương tự.

### 🎯 Custom Scan Region (Mới)
- **Tiết kiệm tài nguyên**: Thay vì quét toàn bộ màn hình, bạn có thể chọn một vùng cụ thể để Bot tìm kiếm Icon.
- **Tăng tốc độ**: Giảm thời gian xử lý và tăng độ chính xác bằng cách giới hạn phạm vi tìm kiếm.
- **Công cụ chọn vùng**: Tích hợp sẵn công cụ kéo thả để xác định tọa độ `(x, y, w, h)` một cách trực quan.

### 🛡️ An toàn & Kiểm soát
- **Emergency Stop (F9)**: Phím tắt khẩn cấp để dừng ngay lập tức mọi hoạt động của Bot.
- **Fail-safe Corners**: Cơ chế an toàn của PyAutoGUI (di chuyển chuột vào 4 góc màn hình để ngắt kết nối).
- **Retry Mechanism**: Tự động thử lại nếu không tìm thấy Icon, giúp ứng dụng hoạt động ổn định hơn trong môi trường UI không nhất quán.

### 🤖 VietCode Workflow
- **Lệnh tự động**: Tự động nhập lệnh `/vietcode <file_path>` sau khi click vào Icon mục tiêu.
- **Xử lý theo hàng đợi**: Thực thi lần lượt danh sách các tệp Markdown đã chọn trong thư mục.

---

## 🛠️ Công nghệ sử dụng

- **Core**: Python 3.8+
- **Automation**: `pyautogui`, `opencv-python`, `mss` (cho hiệu suất cao trên Linux/Windows)
- **GUI**: `tkinter` với custom components
- **Hotkey**: `pynput`
- **Testing**: `pytest`

---

## 📂 Cấu trúc thư mục chi tiết

```text
python_app/
├── main.py                # Điểm khởi đầu (Entry point) của ứng dụng
├── ui_components.py       # Các thành phần giao diện và logic UI chính
├── engine.py              # Bộ điều phối (Orchestrator) quản lý luồng thực thi
├── bot_core.py            # Lõi xử lý tương tác thấp (Click, Type, Scan)
├── region_selector.py     # Công cụ chọn vùng quét màn hình bằng chuột
├── file_manager.py        # Quản lý lọc và sắp xếp file .md
├── hotkey.py              # Lắng nghe phím tắt toàn cục (Global Hotkeys)
├── patch_utils.py         # Tiện ích sửa lỗi và tối ưu hóa hệ thống
├── icon.png               # Ảnh mẫu (Template) mặc định để tìm kiếm
├── plans/                 # Thư mục chứa các file kế hoạch (.md)
├── tests/                 # Thư mục chứa bộ kiểm thử (Unit & Integration tests)
└── venv/                  # Môi trường ảo (Virtual Environment)
```

---

## ⚙️ Cài đặt & Khởi chạy

### 1. Chuẩn bị môi trường
Yêu cầu Python 3.8 trở lên. Khuyến khích sử dụng môi trường ảo:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
```

### 2. Cài đặt thư viện
```bash
pip install pyautogui opencv-python pynput mss pillow
```

*Lưu ý: Trên Linux (Ubuntu/Debian), bạn có thể cần cài đặt thêm: `sudo apt-get install scrot xclip wl-clipboard`.*

### 3. Khởi chạy
```bash
python main.py
```

---

## 📖 Hướng dẫn sử dụng chi tiết

### Bước 1: Thiết lập thư mục và Icon
- **MD Files Folder**: Nhấn "Browse" để chọn thư mục chứa các file kế hoạch của bạn.
- **Icon Image**: Nhấn "Browse" để chọn ảnh chụp màn hình của nút bạn muốn Bot click vào (ví dụ: nút ▷ Run trong VS Code).

### Bước 2: Xác định vùng quét (Tùy chọn nhưng khuyến khích)
- Nhấn **"Select Scan Area"**.
- Màn hình sẽ mờ đi, hãy kéo thả chuột để chọn vùng chứa Icon mục tiêu.
- Điều này sẽ giúp Bot tìm kiếm nhanh hơn và không bị nhiễu bởi các thành phần khác trên màn hình.

### Bước 3: Bắt đầu Auto
- Nhấn **"START AUTO"**.
- Bot sẽ chờ 2 giây để bạn chuyển sang cửa sổ làm việc.
- Nó sẽ quét Icon trong vùng đã chọn, click vào, và gõ lệnh thực thi cho từng file `.md`.

### Bước 4: Kiểm soát và Dừng
- Bạn có thể theo dõi tiến trình trong bảng **Log Console**.
- Nhấn **F9** hoặc nút **STOP** để dừng bất cứ lúc nào.

---

## 🧪 Kiểm thử (Testing)

Dự án đi kèm với bộ test suite toàn diện để đảm bảo tính ổn định:

```bash
# Chạy tất cả các test
pytest tests/

# Chạy test cho logic nhận diện vùng
pytest tests/test_region_scan.py
```

---

## ⚠️ Lưu ý quan trọng
- **Độ phân giải**: Ảnh Icon phải được chụp trên cùng màn hình và cùng tỷ lệ scale mà bạn đang sử dụng.
- **Quyền truy cập**: Trên Linux/macOS, hãy đảm bảo Terminal có quyền điều khiển chuột và bàn phím (Accessibility features).
- **Hỗ trợ Clipboard**: Nếu gặp lỗi khi dán đường dẫn, hãy cài đặt `xclip` hoặc `wl-clipboard`.

---
*Phát triển bởi Antigravity Team.*
