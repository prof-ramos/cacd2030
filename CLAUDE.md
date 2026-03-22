# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CACD 2030 is a study planning system for the Brazilian Diplomat Career Admission Exam (Concurso de Admissão à Carreira de Diplomata). Goal: approval by 2030.

## Commands

### Track Study Progress

The system uses Excel as the source of truth (recommended over Markdown):

```bash
# From scripts/ directory
python3 progresso_excel.py    # Reads from recursos/CACD2026_checklist.xlsx
python3 progresso.py          # Reads from planejamento/edital-conteudos.md (markdown fallback)
```

To mark progress:
1. Open `recursos/CACD2026_checklist.xlsx`
2. Mark column D ("Estudado") with `x` for studied topics
3. Save and run `python3 scripts/progresso_excel.py`

## Architecture

### Progress Tracking (Dual Source)

**Excel (Primary)**: `recursos/CACD2026_checklist.xlsx`
- Column D contains "Estudado" checkboxes
- Script `progresso_excel.py` reads specific row ranges per discipline
- Disciplinas dict maps: subject name → (start_row, end_row, total_items)

**Markdown (Fallback)**: `planejamento/edital-conteudos.md`
- Uses `- [ ]` and `- [x]` checkboxes under `## MATÉRIA` headers
- Script `progresso.py` parses with regex to find sections and count checkboxes

Both scripts output progress bars and percentages per subject and overall.

### Directory Structure

- `planejamento/`: Study planning docs (edital checklist, cronograma, materias, metas)
- `scripts/`: Progress calculation utilities (Python + bash)
- `recursos/`: Reference materials (Excel checklist, PDFs)
- `notas/`: Study notes per subject (to be created)
- `docs/`: Additional documentation

### Exam Phases

The contest has 6 phases. Current focus: Phases 1 (objective) and 2 (written). Subjects include Portuguese, English, Spanish, French, Brazilian History, World History, International Politics, Geography, Economics, and Law.

## Dependencies

Python scripts require `openpyxl` for Excel reading:
```bash
pip install openpyxl
```

Shell script `progresso.sh` uses `bc` for percentage calculations.

## Subject Priority

Critical: International Politics, Portuguese (1st/2nd phase), English (1st/2nd phase)
High: Law, Brazilian History, Spanish, French
Medium: Geography, Economics
