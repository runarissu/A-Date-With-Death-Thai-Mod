# Codebase Map — A Date with Death (Thai Mod)

## Game Info
- Engine: Ren'Py 8.2.1 (Steam PC build)
- Launcher: `ADatewithDeath.exe` / `.sh` / `.app` (macOS)
- All game scripts + most assets packed in `game/archive.rpa` (1.09 GB, RPA-3.0)

## Directory Layout

| Path | Contents |
|---|---|
| `game/` | Runtime data — `archive.rpa`, `gui/` (19 loose font files), `images/`, `sgb-words.txt`, `glitch_ren.py`, `tl/None/` |
| `renpy/` | Bundled Ren'Py engine |
| `_extracted_scripts/` | 93 `.rpy` files decompiled from `archive.rpa` (source of truth for TL work) |
| `docs/` | Style guides, task tracking, session log |

## Key Script Files (`_extracted_scripts/`)

| File | Role |
|---|---|
| `script.rpy` | Main entry / story flow |
| `chapters/` | Day 1–7 + roomexplore variants, `bad_end.rpy`, `end_1/2.rpy`, `dlc_end.rpy` |
| `books.rpy` | In-game books (untranslated in JP TL — translate from EN) |
| `call_messages.rpy` | Phone call messages |
| `pronoun selection.rpy` | Pronoun vars via `__()` → `translate thai strings` |
| `screens.rpy`, `gui.rpy`, `options.rpy` | UI text + language screen hook |
| `kinetic_text_tags.rpy` | 9 custom tags: bt, fi, sc, rotat, chaos, swap, move, omega, para |
| `charactercreator.rpy`, `computer.rpy`, `contacts.rpy`, `roomcreation.rpy`, `room_define.rpy` | System/UI screens |
| `lingo.rpy` | Wordle minigame — keep EN (Thai combining marks break grid) |
| `tl/japanese/` | Existing JP translation — structural reference |

## Fonts (`game/gui/`)
- Body: `ReemKufi-VariableFont_wght.ttf`; UI: `Alata-Regular.ttf`
- JP fonts already shipped (NotoSansJP, KiwiMaru, KosugiMaru, PixelMplus12, etc.)
- Plan: composite merge Noto Sans Thai + originals via `config.font_replacement_map` (`replace_font.rpy`)

## Docs
- `docs/en-th-localization-style-guide.md` — EN→TH voice/terminology guide
- `docs/jp-th-localization-style-guide.md` — JP→TH guide (Grim = ข้า/เจ้า archaic)
- `docs/active-task.md`, `docs/session-log.md` — workflow tracking

## Voice Map (summary)
- Grim (Grim Reaper): Title Case EN → Thai ข้า/เจ้า + literary register
- Player (MC): ฉัน/เธอ polite-casual
- Narrator (`center_text`, second-person): คุณ
- Pronoun strings: gender-neutral เขา for all
