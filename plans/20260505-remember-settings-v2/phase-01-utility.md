# Phase 01: Settings Manager & Atomic Save
Status: ✅ Completed

## Objective
Create `settings_manager.py` with robust path detection and atomic writing.

## Tasks
- Implement `get_config_path()`:
  - Linux: Check `os.environ.get("XDG_CONFIG_HOME")` then fallback to `~/.config`.
  - Windows: Use `os.environ.get("LOCALAPPDATA")`.
- Implement `save_settings(data)`:
  - Write to `config.json.tmp`.
  - Use `os.replace()` to move it to `config.json` (Atomic operation).
  - Force `utf-8` and `indent=4`.
- Implement `load_settings()`:
  - Handle JSON errors and missing files by returning defaults.

## Test Criteria
- Verify settings are saved in the correct OS-specific folder.
- Verify `config.json` remains valid even if manually edited with junk (should fallback to defaults).
