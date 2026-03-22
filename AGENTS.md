# AGENTS.md

**Timestamp:** 2026-03-22

## Purpose

Projeto CACD 2030 - planejamento de estudos para concurso de diplomata

## Key Files

- `README.md` - Main project documentation and overview
- `CLAUDE.md` - Project guidance and commands for Claude Code
- `.gitignore` - Git ignore rules for the project

## Subdirectories

- `docs/` - Additional documentation files
- `planejamento/` - Study planning documents (edital checklist, cronograma, materias, metas)
- `recursos/` - Reference materials (Excel checklist, PDFs)
- `scripts/` - Progress calculation utilities (Python + bash)

## For AI Agents

### Progress Tracking System

The project uses **Excel as the source of truth** for study progress tracking:

1. **Primary Excel File**: `recursos/CACD2026_checklist.xlsx`
   - Column D contains "Estudado" checkboxes
   - Script `progresso_excel.py` reads specific row ranges per discipline
   - Disciplinas dict maps: subject name → (start_row, end_row, total_items)

2. **Markdown Fallback**: `planejamento/edital-conteudos.md`
   - Uses `- [ ]` and `- [x]` checkboxes under `## MATÉRIA` headers
   - Script `progresso.py` parses with regex to find sections and count checkboxes

### How to Use Progress Scripts

```bash
# From scripts/ directory
python3 progresso_excel.py    # Reads from recursos/CACD2026_checklist.xlsx
python3 progresso.py          # Reads from planejamento/edital-conteudos.md
```

### Marking Progress

1. Open `recursos/CACD2026_checklist.xlsx`
2. Mark column D ("Estudado") with `x` for studied topics
3. Save and run `python3 scripts/progresso_excel.py`

## Dependencies

- `openpyxl` (Python) - Required for Excel reading in Python scripts
- `bc` (shell) - Required for percentage calculations in shell script

## Project Structure Overview

CACD 2030 is a study planning system for the Brazilian Diplomat Career Admission Exam. The system tracks study progress across 6 exam phases, with focus on Phases 1 (objective) and 2 (written). Subjects include Portuguese, English, Spanish, French, Brazilian History, World History, International Politics, Geography, Economics, and Law.