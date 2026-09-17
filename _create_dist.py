"""Build the distributable Thai mod package into _dist/.

Produces:
  _dist/thai_mod.zip  — contains game/thai_mod.rpa (extract into the game
                        root folder and the .rpa lands in game/)
  _dist/README.md     — bilingual install/uninstall instructions

Run _create_rpa.py first so game/thai_mod.rpa is up to date.
"""
import os, zipfile, sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT = r"D:\Steam\steamapps\common\A Date with Death"
RPA = os.path.join(ROOT, "game", "thai_mod.rpa")
DIST = os.path.join(ROOT, "_dist")
ZIP = os.path.join(DIST, "thai_mod.zip")

os.makedirs(DIST, exist_ok=True)

if not os.path.exists(RPA):
    sys.exit("ERROR: game/thai_mod.rpa not found — run _create_rpa.py first")

with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as zf:
    # Store as game/thai_mod.rpa so extracting into the game root works
    zf.write(RPA, "game/thai_mod.rpa")

size = os.path.getsize(ZIP)
print("Created: {}".format(ZIP))
print("  Size: {} bytes ({:.1f} MB)".format(size, size/1024/1024))
