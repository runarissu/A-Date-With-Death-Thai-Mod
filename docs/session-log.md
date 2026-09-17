# Session Log

## 2026-09-16 — Thai Mod Planning + Style Guide

### Decisions
- Engine: Ren'Py 8.2.1; all scripts in `game/archive.rpa` (1.09 GB)
- Extracted 93 `.rpy` files to `_extracted_scripts/` via custom Python RPA-3 index reader (unrpa has no file filter)
- Pronouns use `__()`-wrapped vars (`she/her/her2/girl/woman/wife/pretty/beautiful` + custom) → translate via `translate thai strings`, no Python override needed (same approach as existing `tl/japanese`)
- Grim's Title Case voice → Thai archaic register (ข้า/เจ้า); JP TL used 貴様 as equivalent
- lingo wordle minigame keeps English `sgb-words.txt` (Thai combining marks break letter grid)
- Font plan: composite Noto Sans Thai + original fonts via `config.font_replacement_map` (reuse merge script from 14DaysWithYou reference project)

### Files Created
- `docs/en-th-localization-style-guide.md` — full EN→TH style guide adapted for this game
- `docs/active-task.md` — task scope & todo

### Reference Project
- `X:\14DaysWithYou-5.5-pc\docs\` — completed Thai mod for another Ren'Py game; reuse tooling & patterns

## 2026-09-16 — JP→TH Style Guide

### Findings from `tl/japanese/` analysis
- Grim's JP voice: 我/貴様 + 歴史的仮名遣い (まつたく/だつた) + archaic endings (ぞ/ぬ/えん) → maps to Thai ข้า/เจ้า + literary register
- Player JP voice: わたし/キミ polite-casual → ฉัน/เธอ
- Narration is `center_text` second-person "you" (EN) / あなた (JP) → Thai "คุณ" — fixed en-th guide which wrongly said ฉัน
- JP pronoun strings: they→あの人, she→彼女, he→彼 — Thai uses gender-neutral เขา for all
- JP choices use `１.《…》` fullwidth format — Thai keeps `1. <…>`
- **`books.rpy` is untranslated in JP** (all `new ""`) — Thai must translate books from EN

### Files Created
- `docs/jp-th-localization-style-guide.md`

### Files Updated
- `docs/en-th-localization-style-guide.md` — corrected narrator to second-person คุณ

## 2026-09-16 — Framework Build (14DWY workflow)

### Decisions
- No SDK needed: bundled `ADatewithDeath.exe . translate thai` generates tl framework (arg1 = basedir)
- `_tmp_project/` = game copy minus `archive.rpa`, extracted `.rpy` placed in `game/`
- Fonts: composite merge (original + Noto Sans Thai) via `_merge_fonts.py`; pyftmerge for same-upm fonts, manual glyph-scale+decompose fallback for mismatched upm/variable fonts
- PixelMplus12 → PlainPixel-Regular.ttf (Thai+Latin pixel font, reused from 14DWY)
- Language switch = `config.overlay_screens` EN/ไทย toggle (game's language screens only have EN/JP) + Thai default on first launch
- Split tl files ~100 blocks → 134 part files; originals backed up to `_backup_tl_original/`
- Pronouns need NO python override — `__()` strings handled by `translate thai strings`

### Results
- Lint: clean (only pre-existing source typo `{i}flirt{/}` in 5_day)
- Game boots with mod loaded, zero errors
- Scope: 8,381 dialogue blocks / 61,519 words to translate

### Files Created
- `game/tl/thai/` — 18 composite TTFs + PlainPixel + NotoSansThai-Regular/SemiBold, `replace_font.rpy`, `replace_screens.rpy`, 134 split tl files
- `_merge_fonts.py`, `_split_tl.py`, `_create_rpa.py`, `docs/codebase-map.md`

### Known Issue
- Stale `.rpyc` under `tl/thai/` caused duplicate-translation init errors after splitting — always `find game/tl/thai -name '*.rpyc' -delete` after file renames
- PyICU for Thai line breaking not yet installed (bundled Python is 3.9 — check wheel availability, else ZWSP via pythainlp at merge time)

## 2026-09-17 — Translation Pass: Day 1 Complete

### Translated files
- Pronoun/gender keys: `pronoun selection`, `charactercreator`, `1_roomexplore - strings` — she/he/they/her/him/them→เขา; his/their→ของเขา; girl→ผู้หญิง, guy/boy→ผู้ชาย (kept gendered so pronoun choice stays meaningful); pretty→สวย, cute→น่ารัก, beautiful→งดงาม, handsome→หล่อ, captivating→มีเสน่ห์, divine→งดงามดั่งเทพ
- UI/framework: `common`, `screens`, `computer` (cat fortune uses cute Thai cat register), `extra`, `contacts`, `options`, `script`, `roomcreation`, `for_testing`, `pong`, `runner`, `call_messages`, `3D/image_viewer`, `3D/sound_viewer`
- `chapters/1_day - strings.rpy` — 539 chat choices (kept numbering + `{font=…}` suffixes + vars)
- `chapters/1_day - part 01–08.rpy` — full Day 1 chat/call dialogue
- `chapters/1_roomexplore - part 01–02.rpy` — room exploration narration (pet vars `[pet_She]`/`[pet_her2]` etc. attach directly to Thai words, no spaces)

### Voice notes
- Grim chat (GR): Title Case → ข้า/เจ้า archaic register; post-call lowercase lines kept deflated
- Grim call (GRC): spoken, still ข้า/เจ้า, slightly less stiff
- Player: ฉัน/เธอ, internet-chat teasing; "lol"→"555"; puns adapted (make a killing→ทำกำไรเป็นกอบเป็นกำ, no-bunny→กระต่ายตัวไหน)
- Narrator: second-person คุณ
- `grimmy` nickname → กริมมี่

### Next
- Day 2: `2_day - strings.rpy` + parts 01–12 + `2_roomexplore` 01–02
- Then Day 3–7, bad_end, badend_roomexplore, dlc_end, end_1, end_2, `books - strings.rpy` (from EN; JP skipped it)

## 2026-09-17 — Translation Pass: Day 2 Complete

### Translated files
- `chapters/2_day - strings.rpy` — 747 chat choices (numbering, `<>` wrappers, font suffixes, vars preserved; fixed 2 malformed inner-quote lines)
- `chapters/2_day - part 01–12.rpy` — Day 2 chat (GR) + first phone call (GRC): emoji gag, nickname gauntlet → settled on "Sunshine" (ซันไชน์), plushie named Azrael (อัซราเอล), sexy-scale banter
- `chapters/2_roomexplore - strings.rpy` + `part 01–02` — eavesdrop neighbor date recap, all 6 pet branches, plant watering, "The Raven and the Koi" book text (อีกากับปลาคาร์ป)

### Validation
- 0 residual English lines in translated positions; 0 odd-quote lines; all `[var]`/`{tag}` token sets match source comments (0 mismatches)

### Next
- Day 3: `3_day - strings.rpy` + parts + `3_roomexplore`

## 2026-09-17 — Git Init + .gitignore

- Created whitelist-style `.gitignore`: `/*` ignores all, re-includes only `docs/`, `game/tl/thai/` (minus `*.rpyc`, `thai_mod.rpa`), and `_create_rpa.py`/`_merge_fonts.py`/`_split_tl.py`
- Excluded: `renpy/`, `lib/`, `game/` assets, `_tmp_project/` (273M), `_extracted_scripts/` + `_backup_tl_original/` (game-derived content, regenerable), logs/traceback
- Gotcha: `*` (no slash) matches at ALL depths and re-ignored files inside `thai/` — must use `/*` for root-level ignore
