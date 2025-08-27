# Brain Dump

Personal "brain dump": articles, collections, notes, and topic‑based compilations — primarily written in LaTeX.

This repository is actively evolving.

## Why

- Keep knowledge in one place — from quick notes to fully edited articles or curated watch/read lists.
- Work in a single typesetting tool (LaTeX) to produce consistent, printable PDFs with stable typography and citations.
- Build themed **collections** (reading lists, study plans, mini‑books) by reusing articles and notes.

## Why it might be useful to you

- Browse the **collections** by topic and pick what you need; each collection references concrete, ready‑to‑compile content.
- Reuse the LaTeX layout and structure as a starting point for your own notes, papers, or course handouts.
- Everything is **reproducible**: clone the repo, build locally with LaTeX, and you’ll get the same PDFs.

## Structure

```
articles/     # polished articles/essays (standalone .tex that produce PDFs)
collections/  # themed compilations that include multiple articles/notes
library/      # personal library: .bib files (and shared assets later if needed)
notes/        # quick notes, drafts, working outlines
Makefile      # convenience targets (build/clean), if defined
```
