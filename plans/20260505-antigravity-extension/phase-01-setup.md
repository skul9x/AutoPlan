# Phase 01: Project Setup & Scaffolding
Status: ✅ Completed

## Objective
Khởi tạo dự án Extension bằng TypeScript và thiết lập môi trường phát triển cho Antigravity IDE.

## Implementation Steps
1. [x] Cài đặt `yo` và `generator-code` nếu chưa có.
2. [x] Khởi tạo project extension mới (Target: TypeScript).
3. [x] Cấu hình `package.json` với các thông tin của Antigravity IDE.
4. [x] Thiết lập file `.vscode/launch.json` để debug trực tiếp trên Antigravity.

## Files to Create/Modify
- `package.json` - Cấu hình metadata và activation events.
- `src/extension.ts` - Entry point của extension.

## Test Criteria
- Extension có thể được "Launch" và hiển thị trong danh sách Extension của IDE.
- Câu lệnh "Hello World" mặc định chạy thành công.
