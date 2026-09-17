################################################################################
## Thai Font Replacement — A Date with Death
## Replaces all English-only fonts with Thai-capable composites via
## config.font_replacement_map + language callbacks, so every font reference
## is caught — gui.* defines, style fonts, and hardcoded {font=...} text tags.
##
## Composite strategy (built by _merge_fonts.py):
##   Each composite = original game font + Noto Sans Thai merged into one TTF.
##   Latin/symbols keep the original look; Thai glyphs come from Noto Sans Thai.
##   (font_replacement_map only accepts filename strings, not FontGroup objects.)
##
##   NotoSansThai-Body.ttf       = ReemKufi-VariableFont_wght + Noto Sans Thai
##   NotoSansThai-UI.ttf         = Alata-Regular + Noto Sans Thai
##   NotoSansThai-8bit.ttf       = 8bitOperatorPlusSC + Noto Sans Thai
##   NotoSansThai-Rounded.ttf    = MPLUSRounded1c-Light + Noto Sans Thai
##   NotoSansThai-SansLight.ttf  = NotoSans-Light + Noto Sans Thai
##   NotoSansThai-Kelvinch.ttf   = Kelvinch-Roman + Noto Sans Thai
##   NotoSansThai-Kembang.ttf    = Kembang + Noto Sans Thai
##   NotoSansThai-JuliaMono.ttf  = JuliaMono-Black + Noto Sans Thai
##   NotoSansThai-Libertine.ttf  = LinLibertine_R + Noto Sans Thai
##   NotoSansThai-Sawarabi.ttf   = SawarabiGothic + Noto Sans Thai
##   NotoSansThai-Kosugi.ttf     = KosugiMaru + Noto Sans Thai
##   NotoSansThai-Kiwi.ttf       = KiwiMaru-Light + Noto Sans Thai
##   NotoSansThai-NotoJP.ttf     = NotoSansJP + Noto Sans Thai
##   NotoSansThai-NotoSerif.ttf  = NotoSerifKR + Noto Sans Thai
##   NotoSansThai-Bebas.ttf      = BebasNeue + Noto Sans Thai
##   NotoSansThai-ApaBedone.ttf  = ApaBedone + Noto Sans Thai
##   NotoSansThai-Starthings.ttf = starthings + Noto Sans Thai
##   NotoSansThai-Monica.ttf     = x12y16pxMaruMonica + Noto Sans Thai
##   PlainPixel-Regular.ttf      = Plain Pixel (CC-BY 4.0) — Thai+Latin pixel font
##                                 (replaces PixelMplus12 which has no Thai)
################################################################################

init python:

    def _thai_setup_fonts():
        # Map (original_font, bold, italic) -> (composite_font, bold, italic).
        # bold/italic flags pass through so Ren'Py applies synthetic
        # bold/italic transformation on the composite font.
        _F = "tl/thai/"

        def _m(orig, comp):
            return {
                (orig, False, False): (_F + comp, False, False),
                (orig, True,  False): (_F + comp, True,  False),
                (orig, False, True):  (_F + comp, False, True),
                (orig, True,  True):  (_F + comp, True,  True),
            }

        config.font_replacement_map = { }

        for orig, comp in [
            # Body text / names / NVL — ReemKufi -> NotoSansThai-Body
            ("gui/ReemKufi-VariableFont_wght.ttf", "NotoSansThai-Body.ttf"),
            # Interface / buttons — Alata -> NotoSansThai-UI
            ("gui/Alata-Regular.ttf", "NotoSansThai-UI.ttf"),
            # Pixel font (chat/computer/lingo) -> PlainPixel (Thai+Latin)
            ("gui/PixelMplus12-Regular.ttf", "PlainPixel-Regular.ttf"),
            # Decorative fonts used by {font=} tags / UI
            ("gui/8bitOperatorPlusSC-Regular.ttf", "NotoSansThai-8bit.ttf"),
            ("gui/MPLUSRounded1c-Light.ttf", "NotoSansThai-Rounded.ttf"),
            ("gui/NotoSans-Light.ttf", "NotoSansThai-SansLight.ttf"),
            ("gui/Kelvinch-Roman.otf", "NotoSansThai-Kelvinch.ttf"),
            ("gui/Kembang.ttf", "NotoSansThai-Kembang.ttf"),
            ("gui/JuliaMono-Black.ttf", "NotoSansThai-JuliaMono.ttf"),
            ("gui/LinLibertine_R.ttf", "NotoSansThai-Libertine.ttf"),
            ("gui/SawarabiGothic-Regular.ttf", "NotoSansThai-Sawarabi.ttf"),
            ("gui/KosugiMaru-Regular.ttf", "NotoSansThai-Kosugi.ttf"),
            ("gui/KiwiMaru-Light.ttf", "NotoSansThai-Kiwi.ttf"),
            ("gui/NotoSansJP-VariableFont_wght.ttf", "NotoSansThai-NotoJP.ttf"),
            ("gui/NotoSerifKR-Regular.ttf", "NotoSansThai-NotoSerif.ttf"),
            ("gui/BebasNeue-Regular.ttf", "NotoSansThai-Bebas.ttf"),
            ("gui/ApaBedone1112-qZXj5.ttf", "NotoSansThai-ApaBedone.ttf"),
            ("gui/starthings.ttf", "NotoSansThai-Starthings.ttf"),
            ("gui/x12y16pxMaruMonica.ttf", "NotoSansThai-Monica.ttf"),
            # ChaosText font_list (kinetic_text_tags.rpy) — fonts don't ship
            # with the game, so {chaos} already falls back in EN. Mapping them
            # to Thai-capable composites keeps Thai legible under {chaos}.
            ("FOT-PopJoyStd-B.otf", "NotoSansThai-Body.ttf"),
            ("GrenzeGotisch-VariableFont_wght.ttf", "NotoSansThai-8bit.ttf"),
            ("Pacifico-Regular.ttf", "NotoSansThai-SansLight.ttf"),
            ("RobotoSlab-ExtraBold.ttf", "NotoSansThai-Bebas.ttf"),
            ("RobotoSlab-Medium.ttf", "NotoSansThai-UI.ttf"),
            ("SyneTactile-Regular.ttf", "NotoSansThai-Rounded.ttf"),
            ("TurretRoad-Bold.ttf", "NotoSansThai-Kosugi.ttf"),
            ("TurretRoad-ExtraBold.ttf", "NotoSansThai-Kelvinch.ttf"),
            ("TurretRoad-ExtraLight.ttf", "NotoSansThai-Sawarabi.ttf"),
            ("TurretRoad-Light.ttf", "NotoSansThai-Libertine.ttf"),
            ("TurretRoad-Medium.ttf", "NotoSansThai-JuliaMono.ttf"),
            ("TurretRoad-Regular.ttf", "NotoSansThai-Body.ttf"),
        ]:
            config.font_replacement_map.update(_m(orig, comp))

        # Thai combining marks sit above/below the line — a touch more leading
        # prevents clipping between lines.
        style.text.line_leading = 2

    def _thai_reset_fonts():
        config.font_replacement_map = { }
        style.text.line_leading = 0

    # Swap fonts when language changes
    if "thai" not in config.language_callbacks:
        config.language_callbacks["thai"] = [ ]
    config.language_callbacks["thai"].append(_thai_setup_fonts)

    if None not in config.language_callbacks:
        config.language_callbacks[None] = [ ]
    config.language_callbacks[None].append(_thai_reset_fonts)

    # Apply at init too — composites contain the original Latin glyphs, so
    # English still renders identically. Ensures fonts are ready before any
    # screen (incl. language picker / confirm) displays, before callbacks fire.
    _thai_setup_fonts()
