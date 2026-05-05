# Phase 02: AI Status Detection
Status: ✅ Completed

## Objective
Thay thế việc "quét màn hình" bằng việc lắng nghe sự kiện AI hoàn tất câu trả lời.

## Implementation Steps
1. [ ] **Command Discovery:** Quét danh sách lệnh của Antigravity (`vscode.commands.getCommands`) để tìm ID chính xác của chat agent hoặc lệnh `/vietcode`.
2. [ ] Theo dõi `vscode.chat.onDidReceiveChatResponse` hoặc monitor Terminal Output để nhận diện trạng thái AI đã hoàn thành.
3. [ ] Tạo một `EventEmitter` để báo hiệu cho các module khác khi AI đã "dứt lời".

## Files to Create/Modify
- `src/agentObserver.ts` - Logic theo dõi trạng thái AI.

## Test Criteria
- Extension log được dòng chữ "AI FINISHED" ngay khi Agent ngừng stream dữ liệu mà không cần nhìn màn hình.
