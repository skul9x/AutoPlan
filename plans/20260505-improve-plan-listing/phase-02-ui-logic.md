# Phase 02: UI Persistence Update
Status: ✅ Completed
Dependencies: [Phase 01](file:///home/skul9x/Desktop/Test_code/AutoPlan-main/python_app/plans/20260505-improve-plan-listing/phase-01-utility.md)

## Objective
Prevent the MD folder path from being saved to the configuration file.

## Requirements
### Functional
- [x] Modify `AppUI.save_current_settings` to set `mru_md_folder` to an empty string when saving.

## Implementation Steps
1. [x] Edit `ui_components.py`.
2. [x] Locate `save_current_settings` method.
3. [x] Change the value for `mru_md_folder` from `self.folder_path.get()` to `""`.

## Files to Create/Modify
- `ui_components.py` - Modify `save_current_settings` method.

## Test Criteria
- [x] Select a folder in the app.
- [x] Restart the app.
- [x] Verify the "MD Files Folder" entry is empty.

---
Next Phase: [phase-03-verification.md](file:///home/skul9x/Desktop/Test_code/AutoPlan-main/python_app/plans/20260505-improve-plan-listing/phase-03-verification.md)
