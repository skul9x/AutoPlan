# Phase 01: Settings Support
Status: ✅ Completed

## Objective
Cập nhật cơ chế lưu trữ cài đặt để hỗ trợ trường thông tin mới `prompt_template`.

## Implementation Steps
1. [x] Mở file `settings_manager.py`.
2. [x] Thêm khóa `prompt_template` vào biến `DEFAULT_SETTINGS`.
3. [x] Giá trị mặc định của `prompt_template` sẽ là:
   ```
   hãy thực hiện code bám sát theo file {xxx}. chú ý, làm đúng yêu cầu, bảo gì làm đấy, không vẽ việc thêm. yêu cầu bạn phải test thật kĩ khi làm xong, ưu tiên test bằng file (nếu chưa có file test thì bạn phải tạo ra). nếu thấy quá khó thì hãy tra online để tìm cách làm đúng chuẩn nhằm sửa lỗi hoặc tiếp tục phát triển. lưu ý, không được mở trình duyệt rồi lấy dom trực tiếp, dùng search_web / read_url_content khi cần tra cứu
   ```

## Files to Modify
- `settings_manager.py`

## Test Criteria
- [x] Khi load_settings() (với config.json chưa có key), nó phải trả về giá trị mặc định của `prompt_template`.

---
Next Phase: `phase-02-bot-core.md`
