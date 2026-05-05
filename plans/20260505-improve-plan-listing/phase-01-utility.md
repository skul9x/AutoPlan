# Phase 01: Utility Logic Update
Status: ✅ Completed
Dependencies: None

## Objective
Filter out `plan.md` from the list of markdown files retrieved from a directory.

## Requirements
### Functional
- [ ] Modify `file_manager.get_markdown_files` to exclude `plan.md`.

## Implementation Steps
1. [ ] Edit `file_manager.py`.
2. [ ] Add a condition to the list comprehension to skip filenames matching `plan.md`.

## Files to Create/Modify
- `file_manager.py` - Modify `get_markdown_files` function.

## Test Criteria
- [ ] List a folder containing `plan.md` and other `.md` files.
- [ ] Verify `plan.md` does not appear in the resulting list.

---
Next Phase: [phase-02-ui-logic.md](file:///home/skul9x/Desktop/Test_code/AutoPlan-main/python_app/plans/20260505-improve-plan-listing/phase-02-ui-logic.md)
