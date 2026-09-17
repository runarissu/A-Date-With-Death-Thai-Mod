# Insert zero-width spaces (ZWSP, U+200B) at Thai word boundaries in all
# translated strings under game/tl/thai/. Ren'Py's unicode line breaker
# (gui.language = "unicode") honors ZWSP, giving Thai proper word-level
# line wrapping without any runtime dependency.
#
# Only maximal runs of Thai-block characters are tokenized, so [variables],
# {tags}, \n escapes, image paths, and identifiers are never touched.
# Comment lines (original source) and `old` lines are skipped.
# Idempotent: ZWSP is outside the Thai block, so re-runs are stable.

import glob
import re
import sys

from pythainlp import word_tokenize

ROOT = "game/tl/thai"
ZWSP = "​"
THAI_RUN = re.compile(r"[ก-๿]+")

def segment(match):
    run = match.group(0)
    tokens = [t for t in word_tokenize(run, engine="newmm") if t]
    if "".join(tokens) != run:
        return run  # tokenizer altered the text — leave it alone
    return ZWSP.join(tokens)

total_files = 0
total_lines = 0

for path in glob.glob(ROOT + "/**/*.rpy", recursive=True):
    out = []
    changed = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            s = line.lstrip()
            if s.startswith("#") or s.startswith("old ") or s.startswith("old\t"):
                out.append(line)
                continue
            new_line = THAI_RUN.sub(segment, line)
            if new_line != line:
                changed += 1
            out.append(new_line)
    if changed:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write("".join(out))
        total_files += 1
        total_lines += changed
        print("{}: {} line(s)".format(path, changed))

print("DONE: {} files, {} lines modified".format(total_files, total_lines))
sys.exit(0)
