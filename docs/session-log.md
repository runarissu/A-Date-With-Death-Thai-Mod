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

## 2026-09-17 — Translation Pass: Day 3 Complete

### Translated files
- `chapters/3_day - strings.rpy` — chat choices
- `chapters/3_day - part 01–08.rpy` — Day 3 chat/call: edgy jokes (เอ็ดจ์), tiny Grim selfie, child diary entries (cute age-appropriate Thai), "Message not sent." → `ส่งข้อความไม่สำเร็จ`
- `chapters/3_roomexplore` strings + parts 01–02

### Fixes
- Missing `<>` wrapper on one choice line; stray `{i}` tag not in source; typo in comment path; duplicated comment line in Day 2 file

### Validation
- 0 residual English; vars/tags/labels preserved across all Day 3 files

## 2026-09-17 — Translation Pass: Day 4 Complete

### Translated files
- `chapters/4_day - strings.rpy` — chat choices (incl. keyboard-mash joke `asdfghjkl.` → Thai-layout equivalent `ฟหกดเ้็ี`, matching JP approach which localized to JP-layout mash)
- `chapters/4_day - part 01–13.rpy` — Day 4 chat/call: shower banter, soul-balance/"broken soul disease", Grim's claim on player's soul, reaper rules, Azrael questions, can't-lie mechanic, pineapple-on-pizza, soul contamination/taint, "Goodnight, Sunshine"
- `chapters/4_roomexplore` strings + parts 01–02 — bed reflection (3 sleep/mood branches), neighbor eavesdrop scene (fate dialogue ×2 variants), all 6 pet naming/grooming branches, plant over-watering gag, `{i}Rovari{/i}` poem → Thai verse โรวารี

### Fixes
- Malformed label/block in part 13 (~line 58); active lines accidentally commented in roomexplore part 01 (`'...'` quote lines) — rewritten; keyboard-mash kept per JP precedent

### Validation
- 0 residual English in active/`new` lines; 0 odd-quote lines; tags/`id` suffixes preserved
- Ren'Py lint: clean for thai files (8,381/8,381 blocks covered); remaining warnings are pre-existing source issues (init priorities, `day6dlc_start` jump, JP TL `{/size}` typo)
- Fixed `{i}flirt{/}` source typo in `5_day - part 02.rpy` new-string
- Deleted all stale `tl/thai/**/*.rpyc` before lint

### Next
- Day 5: `5_day - strings.rpy` + parts + `5_roomexplore`; then Day 6–7, endings, books

## 2026-09-17 — Translation Pass: Day 5 Complete

### Translated files
- `chapters/5_day - strings.rpy` — 825 chat choices (numbering, `{font=…}` glyph letters, `\n` breaks, `{#ofcday5}` jump label preserved)
- `chapters/5_day - part 01–13.rpy` — Day 5 chat/call: family/sibling questions, jealous Grim ("ข้าไม่แบ่งใครหรอก ซันไชน์"), dating history, ninja/crab/papercut banter, in-person window visit (raven glamour), real name reveal → แคสเปอร์, sunflower gift scene
- `chapters/5_roomexplore` strings + parts 01–02 — travel/vacation branches, neighbor door eavesdrop (vulnerable apology ×2 variants), pet history (all 6), plant growth arc, affirmations book

### Fixes
- `day05callcont_d1be3c83` label typo'd as `call1a_day5_` — corrected
- Case-sensitive pet vars kept verbatim: `[pet_Her]`/`[pet_She]` (capital variants) not lowercased to `[pet_her2]`/`[pet_she]` — different vars in engine

### Validation
- 0 residual English in active/`new` lines across all 17 Day 5 files; 0 odd-quote/brace-mismatch lines

### Next
- Day 6: `6_day - strings.rpy` + parts + `6_roomexplore`; then Day 7, endings, books

## 2026-09-17 — Translation Pass: Day 6 → Endings + Books + Contacts + ZWSP

### Translated files
- Day 6: `6_day - strings` (469) + parts 01–09 + `6_roomexplore` — validated; `bucket list` intentionally EN; hiss-tory pun adapted to Thai; `{s}…{/s}` strikethrough in diary preserved
- Day 7: `7_roomexplore` strings + parts 01–03 (Day 7 is roomexplore-only)
- `bad_end` (4 files, incl. badend_roomexplore), `dlc_end` (5), `end_1` (5), `end_2` (5, 203 pairs) — all validated 0 issues
- `script - part 01` (intro narration), `lingo - part 01` (minigame text; word list stays EN), `books - strings` (300 pairs, literary; author attributions kept EN; `Beyond the Bet` DLC title kept EN)

### Contacts (Thai DM lists)
- `replace_screens.rpy` redefines `randomizeDMs()` at `init 10` with a Thai branch: curated pool = DM1–7 (translated via `contacts - strings`) + 5 new Thai contacts (TH_DM1–5, avatars 100–300 exist in archive)
- Gotcha: `default` vars (DM1, DM_list_*) are NOT set at init — all refs deferred to call time; first version crashed lint with `NameError: DM1`
- Fixed pre-existing source bug: load screen permanently overwrites `DM_list_*` with JP lists under Japanese — EN pools now rebuilt from DM objects (`_english_dm_pools()`), not trusted `DM_list_*`
- EN/ไทย overlay toggle now also calls `randomizeDMs()` for parity with game's language buttons

### Thai line breaking
- Game already sets `gui.language = "unicode"` → unicode line breaker honors ZWSP; `thaic90` mode rejected (re-encodes to PUA our fonts lack); PyICU not used
- `_insert_zwsp.py`: pythainlp `newmm` tokenizes maximal Thai runs (`\u0E00–\u0E7F`) in active lines only (skips `#` comments + `old` lines) → joins with `\u200b`; idempotent, vars/tags/paths untouched
- Applied: 130 files / 12,744 lines; lint clean (exit 0), 8,381/8,381 blocks, no thai errors

### Language selection screens
- `language_choose_firstlaunch` redefined: 3 buttons — English / ไทย (new, NotoSansThai-UI font) / 日本語
- `screen preferences()` fully redefined (verbatim copy of screens.rpy:2048-2172) with added ไทย textbutton in Text Language hbox — keep in sync if original changes
- Thai button mirrors Japanese NSFWPatch action (`persistent.NSFWPatch_installed = False`)
- Lint clean; `thai_mod.rpa` rebuilt (157 files / ~47.5 MB)
- `_create_dist.py` → `_dist/thai_mod.zip` (~21 MB, contains `game/thai_mod.rpa`) + `_dist/README.md` bilingual install guide — RPA index verified (157 entries, correct `tl/thai/` paths)
- **RPA fix**: Ren'Py does NOT load `.rpy` from archives (`script.py:707` "Cannot load rpy file from inside an archive") — only `.rpyc`. `_create_rpa.py` now packs `.rpyc`+.ttf; generate via lint/game run first. Verified: with `game/tl/thai/` fully removed, lint still reports 8,381 thai blocks
- Gotcha: moving `tl/thai` within `game/` doesn't disable it (whole `game/` tree is scanned) — move outside `game/` to test; loose .rpy + archive .rpyc coexist fine (same statement names dedupe, but different-path copies collide)

### Next
- In-game QA (menu, toggle, char creation, chat/DM, contacts, books, lingo, endings, save/load, wrapping) → `python _create_rpa.py` → `thai_mod.rpa`
- Low priority: 3D/ActionEditor dev-tool strings; `beyond the bet` DLC scripts have JP TL but no thai tl files generated — scope TBD
