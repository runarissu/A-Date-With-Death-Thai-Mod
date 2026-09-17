"""
Create a Ren'Py .rpa archive (version 3.0) from a directory.
RPA v3 format:
  - Header: "RPA-3.0 " + hex(offset) + " " + hex(key) + "\n"
  - Index: pickled dict of {filename: [(offset, length, prefix), ...]}
  - File data
All offsets and lengths are XORed with the key.
"""
import os, sys, pickle, zlib

sys.stdout.reconfigure(encoding='utf-8')

def create_rpa(source_dir, output_path, base_dir=None):
    """
    Create an RPA-3.0 archive from source_dir.
    
    base_dir: the directory that paths in the archive should be relative to.
              For a mod in game/tl/thai/, base_dir should be game/ so that
              paths are stored as tl/thai/replace_screens.rpy etc.
              If None, defaults to source_dir (paths relative to source_dir).
    """
    if base_dir is None:
        base_dir = source_dir
    key = 0x12345678  # arbitrary key
    files = []

    # Pack .rpyc + .ttf — Ren'Py does NOT load .rpy sources from inside
    # an archive (script.py: "Cannot load rpy file from inside an archive"),
    # so only compiled .rpyc works. Generate them first by running the game
    # or `ADatewithDeath.exe . lint` once with the loose tl/thai tree present.
    allowed_exts = {".rpyc", ".ttf"}
    for root, dirs, fnames in os.walk(source_dir):
        for fn in sorted(fnames):
            ext = os.path.splitext(fn)[1].lower()
            if ext not in allowed_exts:
                continue
            full = os.path.join(root, fn)
            # Path in archive must be relative to base_dir (game/)
            rel = os.path.relpath(full, base_dir).replace("\\", "/")
            files.append((rel, full))

    # RPA-3.0 header format: "RPA-3.0 " + 16 hex digits + " " + 8 hex digits + "\n"
    # Ren'Py reads l[8:24] (16 chars) for offset, l[25:33] (8 chars) for key
    # Total = 8 + 16 + 1 + 8 + 1 = 34 bytes
    header_len = 34

    with open(output_path, "wb") as out:
        # Write placeholder header of exact size (we'll overwrite it later)
        out.write(b" " * header_len)

        index = {}
        for rel, full in files:
            with open(full, "rb") as f:
                data = f.read()
            offset = out.tell()
            out.write(data)
            length = len(data)
            # XOR offset and length with key
            index[rel] = [(offset ^ key, length ^ key, b"")]

        # Write index (zlib compressed pickle)
        index_offset = out.tell()
        pickled = pickle.dumps(index, protocol=2)
        compressed = zlib.compress(pickled)
        out.write(compressed)

        # Go back and write the real header (must be exactly header_len bytes)
        out.seek(0)
        header = f"RPA-3.0 {index_offset:016x} {key:08x}\n".encode("ascii")
        assert len(header) == header_len, f"Header is {len(header)} bytes, expected {header_len}"
        out.write(header)

    print(f"Created: {output_path}")
    print(f"  Files: {len(files)}")
    print(f"  Size: {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    source = r"D:\Steam\steamapps\common\A Date with Death\game\tl\thai"
    output = r"D:\Steam\steamapps\common\A Date with Death\game\thai_mod.rpa"
    # The game_dir is the parent of tl/thai/ — paths in the .rpa must be
    # relative to game/ so Ren'Py loads them at the correct location.
    game_dir = r"D:\Steam\steamapps\common\A Date with Death\game"
    create_rpa(source, output, base_dir=game_dir)
