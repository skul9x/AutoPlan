# Plan: Professional Cross-Platform Settings (V3 - Final)
Created: 2026-05-05
Status: 🟡 In Progress

## Overview
Implement a robust settings system ready for packaging (.exe/.deb).
Key focus: Standard paths, High DPI support, and Data Integrity.

## Expert Considerations
- **Data Integrity:** Use Atomic Writes (write to temp, then rename) to prevent config corruption.
- **Linux Standards:** Support `XDG_CONFIG_HOME` for proper Linux integration.
- **Windows High DPI:** Force Process DPI Awareness to fix region selection offsets on scaled displays.
- **Error Handling:** Graceful fallback if settings are corrupted or invalid.

## Phases

| Phase | Name | Status | Progress |
|-------|------|--------|----------|
| 01 | Settings Manager & Atomic Save | ⬜ Pending | 0% |
| 02 | DPI Awareness & Startup Loading | ⬜ Pending | 0% |
| 03 | UI Hooks & Auto-Save | ⬜ Pending | 0% |
| 04 | Final Packaging Validation | ⬜ Pending | 0% |

## Quick Commands
- Start Phase 1: `/code phase-01`
