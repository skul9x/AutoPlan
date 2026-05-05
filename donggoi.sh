#!/bin/bash

# AutoPlan Packaging Script for Ubuntu (.deb)
# Copyright 2026 Nguyễn Duy Trường

set -e # Dừng script nếu có lỗi xảy ra

echo "------------------------------------------------"
echo "🚀 Bắt đầu quá trình đóng gói AutoPlan..."
echo "------------------------------------------------"

# 1. Kiểm tra và kích hoạt môi trường ảo
if [ -d "venv" ]; then
    echo "📦 Kích hoạt môi trường ảo venv..."
    source venv/bin/activate
else
    echo "❌ Lỗi: Không tìm thấy thư mục venv. Vui lòng tạo venv trước."
    exit 1
fi

# 2. Cài đặt dependencies
echo "📥 Cài đặt thư viện cần thiết..."
pip install -r requirements.txt
pip install pyinstaller

# 3. Đóng gói binary bằng PyInstaller
echo "🔨 Đang đóng gói binary (có thể mất một lúc)..."
pyinstaller --noconsole --onefile --name "autoplan" main.py

# 4. Thoát venv
deactivate

# 5. Tạo cấu trúc gói .deb
echo "🏗️ Đang tạo cấu trúc gói Debian..."
rm -rf autoplan-pkg # Xóa bản cũ nếu có
mkdir -p autoplan-pkg/usr/bin
mkdir -p autoplan-pkg/DEBIAN

# Copy binary vào thư mục bin của hệ thống
cp dist/autoplan autoplan-pkg/usr/bin/
chmod +x autoplan-pkg/usr/bin/autoplan

# Tạo file control
printf "Package: autoplan\nVersion: 1.0.0\nSection: utils\nPriority: optional\nArchitecture: amd64\nMaintainer: Nguyen Duy Truong <skul9x@gmail.com>\nDescription: AutoPlan Python Automation Tool\n" > autoplan-pkg/DEBIAN/control

# 6. Build file .deb
echo "📦 Đang nén thành file .deb..."
dpkg-deb --build autoplan-pkg

echo "------------------------------------------------"
echo "✅ Đã đóng gói xong: autoplan-pkg.deb"
echo "------------------------------------------------"
echo "Để cài đặt, hãy chạy lệnh sau:"
echo "sudo dpkg -i autoplan-pkg.deb"
echo "------------------------------------------------"
