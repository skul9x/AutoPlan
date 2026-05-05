# Phase 03: Persistence Hooks
Status: ✅ Completed
Dependencies: Phase 02

## Objective
Link UI changes to the new secure storage.

## Tasks
- Update `browse_folder`, `browse_file`, and region selection methods to call `settings_manager.save_settings`.
- Ensure we save a dictionary containing all 3 main settings every time one changes.

## Test Criteria
- Settings persist even if the project folder is moved (since config is in the User folder).
