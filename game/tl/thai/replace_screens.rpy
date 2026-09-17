################################################################################
## Thai Language Toggle — A Date with Death
##
## Adds a small EN / ไทย toggle in the top-left corner, always visible via
## config.overlay_screens so the player can switch language at any time —
## works around the fact that the game's built-in language screens
## (language_choose_firstlaunch, preferences) only offer English/Japanese.
## Default language is set to Thai on first launch.
################################################################################

style thai_lang_button is button:
    xsize 60
    ysize 30

style thai_lang_button_text is button_text:
    size 16
    color "#888888"
    hover_color "#ffffff"
    selected_color "#3b36ff"
    selected_hover_color "#3b36ff"

screen thai_language_toggle():
    zorder 200
    frame:
        background None
        pos (10, 10)
        hbox:
            spacing 10
            textbutton "EN":
                action Language(None)
                style "thai_lang_button"
            textbutton "ไทย":
                action Language("thai")
                style "thai_lang_button"
                text_font "tl/thai/NotoSansThai-UI.ttf"

## --- Set default language to Thai on first launch ---
init -100 python:
    if persistent._thai_first_launch is None:
        persistent._thai_first_launch = True
        _preferences.language = "thai"

## --- Register overlay screen so it's always visible ---
init -1 python:
    if "thai_language_toggle" not in config.overlay_screens:
        config.overlay_screens.append("thai_language_toggle")
