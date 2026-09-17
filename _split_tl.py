"""
Split generated tl/thai/*.rpy translation files into ~100-block part files,
following the 14DaysWithYou workflow (completed small files survive
interruptions better than one huge file).

- `translate thai <id>:` blocks  -> <name> - part NN.rpy (~100 blocks each)
- `translate thai strings:`      -> <name> - strings.rpy (kept whole)
- `translate thai python/style`  -> stay with the strings file
- Originals are backed up to _backup_tl_original/

Output naming mirrors source layout:
    tl/thai/chapters/1_day.rpy -> tl/thai/chapters/1_day - part 01.rpy, etc.
"""
import os, re, shutil, sys

sys.stdout.reconfigure(encoding='utf-8')

TL = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                  "game", "tl", "thai")
BACKUP = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "_backup_tl_original")
BLOCKS_PER_FILE = 100

BLOCK_RE = re.compile(r"^translate thai (\S+):", re.M)


def split_file(path):
    text = open(path, encoding="utf-8-sig").read()

    # Collect positions of every translate block header.
    marks = [m for m in BLOCK_RE.finditer(text)]
    if not marks:
        return None  # nothing to split

    header = text[:marks[0].start()]

    # Group consecutive blocks: each "translate thai <id>:" starts a block
    # that runs until the next translate line (or EOF).
    blocks = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        blocks.append((m.group(1), text[m.start():end]))

    dialogue = [b for k, b in blocks if k not in ("strings", "python", "style")]
    strings = [b for k, b in blocks if k in ("strings", "python", "style")]

    base = os.path.splitext(os.path.basename(path))[0]
    outdir = os.path.dirname(path)
    written = []

    if strings:
        sp = os.path.join(outdir, f"{base} - strings.rpy")
        with open(sp, "w", encoding="utf-8") as f:
            f.write(header + "".join(strings))
        written.append(sp)

    if not dialogue and not strings:
        return None

    n = max(1, (len(dialogue) + BLOCKS_PER_FILE - 1) // BLOCKS_PER_FILE)
    for i in range(n):
        chunk = dialogue[i * BLOCKS_PER_FILE:(i + 1) * BLOCKS_PER_FILE]
        if not chunk:
            break
        pp = os.path.join(outdir, f"{base} - part {i + 1:02d}.rpy")
        with open(pp, "w", encoding="utf-8") as f:
            f.write(header + "".join(chunk))
        written.append(pp)

    return written


def main():
    os.makedirs(BACKUP, exist_ok=True)
    total_parts = 0
    for root, _dirs, files in os.walk(TL):
        for fn in sorted(files):
            if not fn.endswith(".rpy"):
                continue
            if " - part " in fn or " - strings" in fn:
                continue  # already split
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, TL)
            written = split_file(path)
            if written is None:
                continue
            # Back up original, then remove it.
            bpath = os.path.join(BACKUP, rel)
            os.makedirs(os.path.dirname(bpath), exist_ok=True)
            shutil.copy2(path, bpath)
            os.remove(path)
            total_parts += len(written)
            print(f"{rel}: -> {len(written)} file(s)")
    print(f"\nDone. {total_parts} split files written. Originals in {BACKUP}")


if __name__ == "__main__":
    main()
