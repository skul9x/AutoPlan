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
mkdir -p autoplan-pkg/usr/share/applications
mkdir -p autoplan-pkg/usr/share/icons/hicolor/scalable/apps

# Copy binary vào thư mục bin của hệ thống
cp dist/autoplan autoplan-pkg/usr/bin/
chmod +x autoplan-pkg/usr/bin/autoplan

# Copy icon
if [ -f "icon.png" ]; then
    cp icon.png autoplan-pkg/usr/share/icons/hicolor/scalable/apps/autoplan.png
fi

# Tạo file .desktop để hiện thị trong menu ứng dụng
cat <<EOF > autoplan-pkg/usr/share/applications/autoplan.desktop
[Desktop Entry]
Name=AutoPlan
Comment=AutoPlan Python Automation Tool
Exec=autoplan
Icon=autoplan
Terminal=false
Type=Application
Categories=Utility;Automation;
EOF

# Tạo file control
printf "Package: autoplan\nVersion: 1.0.0\nSection: utils\nPriority: optional\nArchitecture: amd64\nMaintainer: Nguyen Duy Truong <skul9x@gmail.com>\nDescription: AutoPlan Python Automation Tool\n" > autoplan-pkg/DEBIAN/control

# 6. Build file .deb
echo "📦 Đang nén thành file .deb..."
dpkg-deb --build autoplan-pkg

echo "------------------------------------------------"
echo "✅ Đã đóng gói xong: autoplan-pkg.deb"
echo "------------------------------------------------"
echo "🛠️ Đang tự động cài đặt gói .deb..."
echo "1" | sudo -S dpkg -i autoplan-pkg.deb
echo "------------------------------------------------"
echo "🎉 Hoàn tất! Bạn có thể chạy AutoPlan từ menu ứng dụng."
echo "------------------------------------------------"
