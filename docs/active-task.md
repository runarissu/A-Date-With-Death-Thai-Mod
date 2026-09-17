# Active Task — A Date with Death Thai Mod

## Current Scope
Thai localization mod for *A Date with Death* (Ren'Py 8.2.1, Steam PC build).
Workflow mirrors the completed 14DaysWithYou mod (`X:\14DaysWithYou-5.5-pc`).

## Status
- [x] Extract `.rpy` scripts from `game/archive.rpa` → `_extracted_scripts/` (93 files)
- [x] Analyze pronoun system, character voices, custom tags, fonts, JP TL structure
- [x] Write `docs/en-th-localization-style-guide.md` + `docs/jp-th-localization-style-guide.md`
- [x] Build `_tmp_project/` (game copy minus `archive.rpa` + loose scripts) — no SDK needed
- [x] `ADatewithDeath.exe . translate thai` → `game/tl/thai/` (8,381 dialogue blocks / 61,519 words)
- [x] `_merge_fonts.py` → 18 composite NotoSansThai fonts + PlainPixel in `game/tl/thai/`
- [x] `replace_font.rpy` — `config.font_replacement_map` + language callbacks
- [x] `replace_screens.rpy` — EN/ไทย overlay toggle + Thai first-launch default
- [x] `_split_tl.py` → 134 part files (~100 blocks each) + `*-strings.rpy`; originals in `_backup_tl_original/`
- [x] `_create_rpa.py` adapted → packs `game/tl/thai/` → `game/thai_mod.rpa`
- [x] Lint clean; game boots with mod, no errors
- [x] **Translate `*-strings.rpy` first** (pronouns, names, UI) — pronoun selection, charactercreator, 1_roomexplore, extra, computer, screens, common, call_messages, contacts, options, script, roomcreation, for_testing, pong, runner, 3D viewers
- [x] Translate `common - strings.rpy` (Ren'Py UI)
- [ ] Translate chapters Day 1→7 → endings → books/call_messages → DLC
  - [x] Day 1: `1_day - strings.rpy` (539 choices) + parts 01–08 + `1_roomexplore` parts 01–02
  - [x] Day 2: `2_day - strings.rpy` (747 choices) + parts 01–12 + `2_roomexplore` strings + parts 01–02 — validated (vars/tags/quotes clean)
  - [ ] Day 3–7, bad_end, dlc_end, end_1, end_2, books
- [ ] Thai DM/contact lists in `replace_screens.rpy` (cf. JP `JP_DM_list_*` pattern in screens.rpy)
- [ ] Thai line breaking: PyICU (py3.9 wheel?) or ZWSP pre-segmentation via pythainlp
- [ ] Fix source typo tag `{i}flirt{/}` → `{/i}` in `5_day - part 02.rpy` new-string
- [ ] In-game QA per checklist → `python _create_rpa.py` → `thai_mod.rpa`

## Key Facts
- All scripts+assets in `game/archive.rpa` (1.09 GB, RPA-3.0, 6,479 files — NO fonts inside)
- Fonts loose in `game/gui/` (19 files); body = `ReemKufi-VariableFont_wght.ttf`, UI = `Alata-Regular.ttf`
- Pronoun vars are `__()`-wrapped → `translate thai strings` only, NO Python override needed
- Grim speaks Title Case → ข้า/เจ้า archaic register; MC = ฉัน/เธอ; narrator = คุณ (second person)
- 9 kinetic custom tags: bt, fi, sc, rotat, chaos, swap, move, omega, para
- ChaosText font_list fonts aren't shipped (dead in EN) — mapped to composites anyway
- JP TL at `tl/japanese/` — structure reference; its `renxel.rpy` shows `translate <lang> python` gui.font pattern
- lingo wordle minigame keeps English `sgb-words.txt` (Thai combining marks break letter grid)
- Commands: `ADatewithDeath.exe . translate thai` / `. lint` (arg1 = basedir)
- Stale `.rpyc` in tl dirs causes duplicate-translation errors — delete before relaunch
