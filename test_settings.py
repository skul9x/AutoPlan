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

assert settings.get('prompt_template') == "implement the code closely following the file {xxx}. note, follow the requirements exactly. do only what is asked, no extra work. once done, you must thoroughly test what you have just implemented, prioritizing testing with files (if no test file exists, you must create one). after finishing, mark the phase plan file as completed. if it seems too difficult, search online for the correct approach to fix errors or continue development. note, do not open a browser and directly access the dom. use search_web / read_url_content when you need to look something up. no need to explain anything. If you need to run a Python file, run it within a venv. when done, say \"done.\" to save token."

print("Test passed!")
