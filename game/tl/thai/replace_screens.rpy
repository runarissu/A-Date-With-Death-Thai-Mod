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
