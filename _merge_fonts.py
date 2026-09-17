"""
Build composite Thai fonts for A Date with Death.

Each composite = <original game font> merged with Noto Sans Thai.
Latin/symbols keep the original look; Thai glyphs come from Noto Sans Thai.

Variable fonts (fvar) are instantiated at wght=400 first — pyftmerge can't
merge VarStore, and Ren'Py renders variable fonts at default weight anyway.
"""
import os, sys
from fontTools import ttLib
from fontTools.merge import Merger
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform

sys.stdout.reconfigure(encoding='utf-8')

GAME = os.path.dirname(os.path.abspath(__file__))
GUI = os.path.join(GAME, "game", "gui")
TL = os.path.join(GAME, "game", "tl", "thai")
THAI_REG = os.path.join(TL, "NotoSansThai-Regular.ttf")
THAI_SEMI = os.path.join(TL, "NotoSansThai-SemiBold.ttf")

# (original gui font, output name, thai source)
JOBS = [
    ("ReemKufi-VariableFont_wght.ttf",  "NotoSansThai-Body.ttf",      THAI_REG),
    ("Alata-Regular.ttf",               "NotoSansThai-UI.ttf",        THAI_REG),
    ("8bitOperatorPlusSC-Regular.ttf",  "NotoSansThai-8bit.ttf",      THAI_REG),
    ("MPLUSRounded1c-Light.ttf",        "NotoSansThai-Rounded.ttf",   THAI_REG),
    ("NotoSans-Light.ttf",              "NotoSansThai-SansLight.ttf", THAI_REG),
    ("Kelvinch-Roman.otf",              "NotoSansThai-Kelvinch.ttf",  THAI_REG),
    ("Kembang.ttf",                     "NotoSansThai-Kembang.ttf",   THAI_REG),
    ("JuliaMono-Black.ttf",             "NotoSansThai-JuliaMono.ttf", THAI_REG),
    ("LinLibertine_R.ttf",              "NotoSansThai-Libertine.ttf", THAI_REG),
    ("SawarabiGothic-Regular.ttf",      "NotoSansThai-Sawarabi.ttf",  THAI_REG),
    ("KosugiMaru-Regular.ttf",          "NotoSansThai-Kosugi.ttf",    THAI_REG),
    ("KiwiMaru-Light.ttf",              "NotoSansThai-Kiwi.ttf",      THAI_REG),
    ("NotoSansJP-VariableFont_wght.ttf","NotoSansThai-NotoJP.ttf",    THAI_REG),
    ("NotoSerifKR-Regular.ttf",         "NotoSansThai-NotoSerif.ttf", THAI_REG),
    ("BebasNeue-Regular.ttf",           "NotoSansThai-Bebas.ttf",     THAI_REG),
    ("ApaBedone1112-qZXj5.ttf",         "NotoSansThai-ApaBedone.ttf", THAI_REG),
    ("starthings.ttf",                  "NotoSansThai-Starthings.ttf",THAI_REG),
    ("x12y16pxMaruMonica.ttf",          "NotoSansThai-Monica.ttf",    THAI_REG),
]

def prep(path, tmp_dir, tag):
    """Load font, instantiate variable axes if needed, save to temp, return path."""
    f = ttLib.TTFont(path)
    if "fvar" not in f:
        return path
    instantiateVariableFont(f, {"wght": 400}, inplace=True)
    tmp = os.path.join(tmp_dir, tag + os.path.basename(path))
    f.save(tmp)
    return tmp

def main():
    ok, fail = 0, []
    tmp_dir = os.path.join(GAME, "_tmp_fonts")
    os.makedirs(tmp_dir, exist_ok=True)
    for src, out_name, thai_src in JOBS:
        out_path = os.path.join(TL, out_name)
        try:
            base_p = prep(os.path.join(GUI, src), tmp_dir, "base_")
            thai_p = prep(thai_src, tmp_dir, "thai_")
            try:
                merged = Merger().merge([base_p, thai_p])
                how = "pyftmerge"
            except Exception:
                merged = manual_merge(ttLib.TTFont(base_p), ttLib.TTFont(thai_p))
                how = "manual"
            merged.save(out_path)
            cmap = merged.getBestCmap()
            n_thai = sum(1 for c in cmap if 0x0E00 <= c <= 0x0E7F)
            print(f"OK  {out_name:36s} glyphs={len(cmap):5d} thai={n_thai} [{how}]")
            ok += 1
        except Exception as e:
            print(f"FAIL {src}: {e}")
            fail.append(src)
    print(f"\n{ok}/{len(JOBS)} merged -> {TL}")
    if fail:
        print("Failed:", fail)
        sys.exit(1)

def manual_merge(base, thai):
    """Copy Thai-range glyphs (0x0E00-0x0E7F) from thai font into base font,
    scaling outlines/metrics when unitsPerEm differ. No GSUB/GPOS merge —
    acceptable for decorative fonts used on symbols."""
    factor = base["head"].unitsPerEm / thai["head"].unitsPerEm
    scale_t = Transform(factor, 0, 0, factor, 0, 0)
    bglyf, bhmtx = base["glyf"], base["hmtx"]
    tglyf, thmtx = thai["glyf"], thai["hmtx"]
    bnames = set(base.getGlyphOrder())

    def draw_resolved(gname, pen, transform):
        """Draw glyph into pen, decomposing components (they'd otherwise
        reference glyph names that don't exist in the base font)."""
        g = tglyf[gname]
        if g.isComposite():
            for comp in g.components:
                _, ct = comp.getComponentInfo()
                ct = Transform(*ct)
                draw_resolved(comp.glyphName, pen, transform.transform(ct))
        else:
            g.draw(TransformPen(pen, transform), tglyf)

    for cp, gname in thai.getBestCmap().items():
        if not (0x0E00 <= cp <= 0x0E7F):
            continue
        new_name = f"th.{gname}"
        if new_name in bnames:
            continue
        pen = TTGlyphPen(tglyf)
        draw_resolved(gname, pen, scale_t)
        bglyf[new_name] = pen.glyph()
        adv, lsb = thmtx[gname]
        bhmtx[new_name] = (round(adv * factor), round(lsb * factor))
        bnames.add(new_name)
        for st in base["cmap"].tables:
            if st.isUnicode():
                st.cmap[cp] = new_name

    order = base.getGlyphOrder()
    for n in sorted(bnames):
        if n not in order:
            order.append(n)
    base.setGlyphOrder(order)
    return base

if __name__ == "__main__":
    main()
