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
                action [Language(None), Function(randomizeDMs)]
                style "thai_lang_button"
            textbutton "ไทย":
                action [Language("thai"), Function(randomizeDMs)]
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

################################################################################
## First-launch language screen — A Date with Death
##
## The original screen only offers English / 日本語. Redefine it with a
## third option: ไทย (Thai) — the mod's default language.
################################################################################
screen language_choose_firstlaunch():
    hbox:
        align 0.5, 0.5
        spacing 50
        textbutton "English" action [Language(None), Function(randomizeDMs), SelectedIf(testing_var == "0"), Return()] text_size 50 text_color "#ffff" text_hover_color "#3b36ff"
        textbutton "ไทย" action [Language("thai"), Function(randomizeDMs), SelectedIf(testing_var == "0"), Return()] text_size 50 text_color "#ffff" text_hover_color "#3b36ff" text_font "tl/thai/NotoSansThai-UI.ttf"
        textbutton "{font=gui/MPLUSRounded1c-Light.ttf}日本語{/font}" action [Language("japanese"), Function(randomizeDMs), SelectedIf(testing_var == "0"), Return()] text_size 50 text_color "#ffff" text_hover_color "#3b36ff"

################################################################################
## Preferences screen — adds a ไทย button to the Text Language row.
##
## Verbatim copy of the original screen (screens.rpy:2048) with one added
## textbutton. Must be kept in sync if the original ever changes.
################################################################################
screen preferences():

    tag menu
    showif color_mode == "dark":
        add "gui/custom/title/title_base_dark.png"
        add "gui/custom/settings/settings_dark_base.png" at popup_transformtest
        add "gui/custom/settings/frame_dark_overlay.png" at logo_transform


    # Headers
    text _("Display") xalign 0.0 xpos 577 ypos 213 size 30 at logo_transform
    text _("Stream Safe Music") xalign 0.0 xpos 577 ypos 422 size 30 at logo_transform
    text _("Skipping") xalign 0.0 xpos 577 ypos 625 size 30 at logo_transform

    text _("BGM") xalign 0.0 xpos 977 ypos 217 size 30 at logo_transform
    text _("SFX") xalign 0.0 xpos 977 ypos 350 size 30 at logo_transform
    text _("VA") xalign 0.0 xpos 977 ypos 484 size 30 at logo_transform
    text _("Auto") xalign 0.0 xpos 977 ypos 620 size 30 at logo_transform

    text _("Voice Language") xalign 0.0 xpos 977 ypos 715 size 30 at logo_transform
    text _("Text Language") xalign 0.0 xpos 977 ypos 805 size 30 at logo_transform

    if not voice_acting:
        text _("Coming soon") xalign 0.0 xpos 1306 ypos 715 size 30  at popup_transformtest
    #

    # Pref. choices

    vbox:
        xpos 570 ypos 285
        textbutton _("Windowed") action Preference("display", "window") text_style "preferences_choices" at popup_transformtest
        textbutton _("Fullscreen") action Preference("display", "fullscreen") text_style "preferences_choices" at popup_transformtest

    vbox:
        xpos 570 ypos 490
        textbutton _("On") text_style "preferences_choices" at popup_transformtest:
            if persistent.streamer_friendly == False:
                action [SetVariable("config.main_menu_music", "audio/BGM/comfy night.ogg"), SetVariable("persistent.streamer_friendly", True), renpy.reload_script]
            else:
                action SelectedIf(persistent.streamer_friendly==True)

        textbutton _("Off") text_style "preferences_choices" at popup_transformtest:
            action [SetVariable("config.main_menu_music", "audio/BGM/midnight groove.ogg"), SetVariable("persistent.streamer_friendly", False), renpy.reload_script]

    vbox:
        xpos 570 ypos 700
        textbutton _("Unread Text") action Preference("skip", "toggle") text_style "preferences_choices" at popup_transformtest
        textbutton _("After Choices") action Preference("after choices", "toggle") text_style "preferences_choices" at popup_transformtest

    if voice_acting:
        hbox:
            xpos 1300 ypos 710
            spacing 20

            textbutton _("English") at popup_transformtest:
                text_style "preferences_choices"
                action [ SetVariable("persistent.grimmy_callback", "English"),
                         Function(apply_va_choice),
                         Function(renpy.save_persistent) ]
                selected persistent.grimmy_callback == "English"

            textbutton _("Typing Sounds") at popup_transformtest:
                text_style "preferences_choices"
                action [ SetVariable("persistent.grimmy_callback", "Beeps"),
                         Function(apply_va_choice),
                         Function(renpy.save_persistent) ]
                selected persistent.grimmy_callback == "Beeps"
    hbox:
        xpos 1300 ypos 800
        spacing 20

        textbutton _("English") action [Language(None), Function(randomizeDMs), If(renpy.has_label("nsfwpatch"), SetVariable("persistent.NSFWPatch_installed", True), NullAction())] at popup_transformtest:
            text_insensitive_color "303030"
            text_idle_color "555555"
            text_hover_color "ffff"
            text_selected_idle_color "ffff"
            text_selected_hover_color "3b36ff"
            text_size 28
            xalign 0.0
        textbutton "ไทย" action [Language("thai"), Function(randomizeDMs), SetVariable("persistent.NSFWPatch_installed", False)] at popup_transformtest:
            text_insensitive_color "303030"
            text_idle_color "555555"
            text_hover_color "ffff"
            text_selected_idle_color "ffff"
            text_selected_hover_color "3b36ff"
            text_size 28
            text_font "tl/thai/NotoSansThai-UI.ttf"
            xalign 0.0
        textbutton _("Japanese") action [Language("japanese"), Function(randomizeDMs), SetVariable("persistent.NSFWPatch_installed", False)] at popup_transformtest:
            text_insensitive_color "303030"
            text_idle_color "555555"
            text_hover_color "ffff"
            text_selected_idle_color "ffff"
            text_selected_hover_color "3b36ff"
            text_size 28
            xalign 0.0 #Language("japanese")

    textbutton _("Mute All") action Preference("all mute", "toggle") text_style "preferences_choices" at popup_transformtest xpos 1595 ypos 855

    bar pos (1135, 225) value Preference("music volume") style "pref_slider" at popup_transformtest
    bar pos (1135, 360) value Preference("sfx volume") style "pref_slider" at popup_transformtest
    bar pos (1135, 495) value Preference("voice volume") style "pref_slider" at popup_transformtest
    bar pos (1135, 630) value Preference("auto-forward time") style "pref_slider" at popup_transformtest

    if persistent.BTBDLC_installed:
        add "gui/custom/settings/btb.png" align 0.95, 0.0 at popup_transformtest
        text __("Beyond the Bet") xalign 0.5 xpos 1638 ypos 45 size 30 at logo_transform:
            if _preferences.language == "japanese":
                yoffset 7
        hbox:
            spacing 70
            xalign 0.5 xpos 1638 ypos 90
            textbutton __("On") action SetVariable("persistent.finished_one_route", 1) text_style "preferences_choices" text_size 35 at logo_transform:
                if _preferences.language == "japanese":
                    yoffset 5
            textbutton __("Off") action SetVariable("persistent.finished_one_route", 0) text_style "preferences_choices" text_size 35 at logo_transform:
                if _preferences.language == "japanese":
                    yoffset 5



    use navigation

    $ tooltip = GetTooltip()

################################################################################
## Thai DM contacts — A Date with Death
##
## randomizeDMs() in screens.rpy only rolls contacts for English (None) and
## Japanese, leaving dm_name1..4 blank under Thai. We redefine it at a later
## init priority with a Thai branch.
##
## Contacts DM8+ are plain (non-translatable) English strings, so the Thai
## pool mirrors the Japanese approach: the 7 dev/friend profiles (translated
## via contacts - strings.rpy) plus a few Thai-flavored contacts defined here.
################################################################################
init 10 python:

    ## Extra Thai contacts (handles kept Latin, like real Thai netizens)
    TH_DM1 = Contacts('MooPingMaster', 'หมู​ปิ้ง​ไม้​ละ​สิบ​บาท', 'gui/custom/chat/DM icons/100_avatar.png')
    TH_DM2 = Contacts('SomTamQueen', 'แซ่บ​นัวร์​ทุก​มื้อ', 'gui/custom/chat/DM icons/150_avatar.png')
    TH_DM3 = Contacts('ChaYenAddict', 'ชาเย็น​หวาน​ๆ แก้​เหนื่อย', 'gui/custom/chat/DM icons/200_avatar.png')
    TH_DM4 = Contacts('TuKTukFast', 'เร็ว​กว่า​แสง', 'gui/custom/chat/DM icons/250_avatar.png')
    TH_DM5 = Contacts('MaeKlongFisher', 'ร่ม​หุบ! ร่ม​หุบ!', 'gui/custom/chat/DM icons/300_avatar.png')

    ## `default` store vars (DM1..DM458, DM_list_*) are not set until game
    ## start, so every reference to them is deferred to call time.

    def _thai_dm_pools():
        return (
            [DM1, DM2, TH_DM1],
            [DM3, DM4, TH_DM2],
            [DM5, DM6, TH_DM3],
            [DM7, TH_DM4, TH_DM5],
        )

    ## The load screen overwrites DM_list_* with the JP lists when Japanese
    ## is active and never restores them, so rebuild the original English
    ## pools from the DM objects instead of trusting DM_list_*.
    _orig_dm_pools = None

    def _english_dm_pools():
        global _orig_dm_pools
        if _orig_dm_pools is None:
            g = globals()
            _orig_dm_pools = (
                [g['DM%d' % i] for i in list(range(1, 8)) + [456, 457, 458]],
                [g['DM%d' % i] for i in range(8, 150)],
                [g['DM%d' % i] for i in range(150, 295)],
                [g['DM%d' % i] for i in range(295, 456)],
            )
        return _orig_dm_pools

    def randomizeDMs():
        global randomimage1
        global randomimage2
        global randomimage3
        global randomimage4
        global contact1_random
        global contact2_random
        global contact3_random
        global contact4_random

        if _preferences.language == "thai":
            pools = _thai_dm_pools()
        elif _preferences.language == "japanese":
            pools = (JP_DM_list_1, JP_DM_list_2, JP_DM_list_3, JP_DM_list_4)
        else:
            pools = _english_dm_pools()

        contact1_random = renpy.random.choice(pools[0])
        contact2_random = renpy.random.choice(pools[1])
        contact3_random = renpy.random.choice(pools[2])
        contact4_random = renpy.random.choice(pools[3])

        store.dm_name1 = contact1_random.name
        store.dm_status1 = contact1_random.status
        store.randomimage1 = contact1_random.DMimagenumber

        store.dm_name2 = contact2_random.name
        store.dm_status2 = contact2_random.status
        store.randomimage2 = contact2_random.DMimagenumber

        store.dm_name3 = contact3_random.name
        store.dm_status3 = contact3_random.status
        store.randomimage3 = contact3_random.DMimagenumber

        store.dm_name4 = contact4_random.name
        store.dm_status4 = contact4_random.status
        store.randomimage4 = contact4_random.DMimagenumber
