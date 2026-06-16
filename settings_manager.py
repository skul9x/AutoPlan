import os
import json
import pathlib
import platform

APP_NAME = "autoplan"
DEFAULT_SETTINGS = {
    "mru_md_folder": "",
    "error_icon_path": "",
    "mru_icon_link": "",
    "scan_region": None,
    "alarm_enabled": False,
    "alarm_mp3_path": "",
    "prompt_template": "implement the code closely following the file {xxx}. note, follow the requirements exactly. do only what is asked, no extra work. once done, you must thoroughly test what you have just implemented, prioritizing testing with files (if no test file exists, you must create one). after finishing, mark the phase plan file as completed. if it seems too difficult, search online for the correct approach to fix errors or continue development. note, do not open a browser and directly access the dom. use search_web / read_url_content when you need to look something up. no need to explain anything. If you need to run a Python file, run it within a venv. when done, say \"done.\" to save token."
}

def get_config_dir():
    """
    Returns the platform-specific configuration directory.
    - Linux: $XDG_CONFIG_HOME/autoplan or ~/.config/autoplan
    - Windows: %LOCALAPPDATA%/autoplan
    """
    system = platform.system()
    
    if system == "Windows":
        base_dir = os.environ.get("LOCALAPPDATA")
        if not base_dir:
            base_dir = os.path.expanduser("~/AppData/Local")
    else:
        # Fallback for Linux/macOS
        # If run as sudo, HOME might be /root. SUDO_USER gives the original user.
        sudo_user = os.environ.get("SUDO_USER")
        if sudo_user and os.getuid() == 0:
            base_dir = os.path.expanduser(f"~{sudo_user}/.config")
        else:
            base_dir = os.environ.get("XDG_CONFIG_HOME")
            if not base_dir:
                base_dir = os.path.expanduser("~/.config")
            
    config_dir = pathlib.Path(base_dir) / APP_NAME
    return config_dir

def get_config_file_path():
    return get_config_dir() / "config.json"

def save_settings(data):
    """
    Saves settings to config.json using an atomic write operation.
    """
    config_file = get_config_file_path()
    config_dir = config_file.parent
    
    # Ensure directory exists
    config_dir.mkdir(parents=True, exist_ok=True)
    
    tmp_file = config_file.with_suffix(".json.tmp")
    
    try:
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        # Atomic replace
        os.replace(tmp_file, config_file)
    except Exception as e:
        if tmp_file.exists():
            tmp_file.unlink()
        raise e

def load_settings():
    """
    Loads settings from config.json. 
    Returns defaults if file is missing or corrupted.
    """
    config_file = get_config_file_path()
    
    if not config_file.exists():
        return DEFAULT_SETTINGS.copy()
    
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
            # Merge with defaults to ensure all keys are present
            settings = DEFAULT_SETTINGS.copy()
            settings.update(loaded_data)
            
            # Default mru_md_folder to Test_code if empty
            if not settings.get("mru_md_folder"):
                settings["mru_md_folder"] = "/home/skul9x/Desktop/Test_code/"
                
            return settings
    except (json.JSONDecodeError, IOError):
        settings = DEFAULT_SETTINGS.copy()
        settings["mru_md_folder"] = "/home/skul9x/Desktop/Test_code/"
        return settings
