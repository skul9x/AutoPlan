import settings_manager
import pathlib
import os

# clear config if it exists so we can test the fallback
config_file = settings_manager.get_config_file_path()

# just test load_settings directly. Since we're adding a new key, if the config.json doesn't have it, it should fallback from DEFAULT_SETTINGS.
# load_settings does `settings = DEFAULT_SETTINGS.copy(); settings.update(loaded_data)`
# so it handles missing keys from an existing config.json as well.
settings = settings_manager.load_settings()

print(f"prompt_template: {settings.get('prompt_template')}")

assert settings.get('prompt_template') == "hãy thực hiện code bám sát theo file {xxx}. chú ý, làm đúng yêu cầu, bảo gì làm đấy, không vẽ việc thêm. yêu cầu bạn phải test thật kĩ khi làm xong, ưu tiên test bằng file (nếu chưa có file test thì bạn phải tạo ra). nếu thấy quá khó thì hãy tra online để tìm cách làm đúng chuẩn nhằm sửa lỗi hoặc tiếp tục phát triển. lưu ý, không được mở trình duyệt rồi lấy dom trực tiếp, dùng search_web / read_url_content khi cần tra cứu"

print("Test passed!")
