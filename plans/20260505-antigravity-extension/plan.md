# Plan: Migrate AutoPlan to Antigravity IDE Extension
Created: 2026-05-05
Status: 🟡 In Progress

## Overview
Chuyển đổi công cụ AutoPlan từ Python (Screen Scanning) sang VS Code Extension dành riêng cho Antigravity IDE. Mục tiêu là tự động hóa lệnh `/vietcode` dựa trên sự kiện AI hoàn tất thay vì quét màn hình.

## Tech Stack
- **Language:** TypeScript
- **Environment:** VS Code Extension API (Antigravity Compatible)
- **Tools:** `yo code` (generator), `vsce` (packager)

## Phases

| Phase | Name | Status | Progress |
|-------|------|--------|----------|
| 01 | [Project Setup & Scaffolding](./phase-01-setup.md) | ✅ Completed | 100% |
| 02 | [AI Status Detection](./phase-02-ai-detection.md) | ✅ Completed | 100% |
| 03 | [Command & Terminal Integration](./phase-03-command.md) | ⬜ Pending | 0% |
| 04 | [Webview UI Development](./phase-04-webview.md) | ⬜ Pending | 0% |
| 05 | [Integration & Packaging](./phase-05-packaging.md) | ⬜ Pending | 0% |

## Quick Commands
- Start Phase 1: `/code phase-01`
- Check progress: `/next`
