# search jumpsec to get to sections

##jumpsec######## billcount ################

init -1 python:

    def tspk(what, amt=0, stmt=None, **kwargs):

        t(what, **kwargs)

        global amount
        amount = amt

        global bill

        portion = int(amt/10)

        if amt != 0:

            renpy.hide_screen("moneyadd", layer=None)
            renpy.show_screen("moneyadd", moneyadded=amt)

        if stmt != None:

            renpy.hide_screen("moneystmt", layer=None)
            renpy.show_screen("moneystmt", statement=stmt)

        i = 10

        while i > 0:

            renpy.pause(0.02)

            bill += portion
            amt -= portion

            i -= 1

##jumpsec######## footnotes ################

    def show_footnote(note):

        renpy.show_screen("footnote", fndict[note], _layer="screens", _transient=False)
        renpy.restart_interaction()

define config.hyperlink_handlers = { 'footnote' : show_footnote }

##jumpsec######### styles ####################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

style outlined:
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    color "FFFF00"
    bold True

style friend:
    outlines [ (absolute(2), "#FF00FF", absolute(1), absolute(1)) ]
    color "FFFF00"
    font "courbd.ttf"
    size 72

style choice_button_text:
    color "0000FF"
    font "courbd.ttf"

##jumpsec####### CHARACTERS #################

define narrator = Character(window_background="gui/textbox_narration.png", what_font='courbd.ttf', what_size=22,  color='#000000', what_color='#000000')
define op = Character(window_background="gui/textbox_blank.png", what_font='courbd.ttf', what_size=28,  color='#FFFFFF', what_color='#FFFFFF', what_xalign=0.5, what_text_align=0.5)
define t = Character("TAGORA", color='#FFFFFF', image="tagora", window_background="gui/textbox_teal.png", who_outlines=[ (4, "#008282") ],)
define g = Character("GALEKH", color='#FFFFFF', image="galekh", window_background="gui/textbox_indigo.png", who_outlines=[ (4, "#005682") ],)

##jumpsec######## IMAGES ###################

image tg clasp = Image("images/tagora/Tagora_Clasp.png", ypos=730, xanchor=640, yanchor=720)
image tg doc = Image("images/tagora/Tagora_Document.png", ypos=730, xanchor=640, yanchor=720)
image tg ew = Image("images/tagora/Tagora_Ew.png", ypos=730, xanchor=640, yanchor=720)
image tg help = Image("images/tagora/Tagora_Helpful.png", ypos=730, xanchor=640, yanchor=720)
image tg mad = Image("images/tagora/Tagora_Hollering.png", ypos=730, xanchor=640, yanchor=720)
image tg judge = Image("images/tagora/Tagora_Judging.png", ypos=730, xanchor=640, yanchor=720)
image tg nervous = Image("images/tagora/Tagora_Nervous.png", ypos=730, xanchor=640, yanchor=720)
image tg neutral = Image("images/tagora/Tagora_Neutral.png", ypos=730, xanchor=640, yanchor=720)
image tg neutral2 = Image("images/tagora/Tagora_Neutral2.png", ypos=730, xanchor=640, yanchor=720)

image gx wary = Image("images/galekh/galekh_disappointedpause.png", ypos=730, xanchor=640, yanchor=720)
image gx thumb = Image("images/galekh/galekh_expressions001.png", ypos=730, xanchor=640, yanchor=720)
image gx tie = Image("images/galekh/galekh_frustration.png", ypos=730, xanchor=640, yanchor=720)
image gx angry = Image("images/galekh/galekh_glare.png", ypos=730, xanchor=640, yanchor=720)
image gx hand = Image("images/galekh/galekh_neutral.png", ypos=730, xanchor=640, yanchor=720)
image gx hand_nj = Image("images/galekh/galekh_nojacketneutral.png", ypos=730, xanchor=640, yanchor=720)
image gx smile_nj = Image("images/galekh/galekh_nojacketpleased.png", ypos=730, xanchor=640, yanchor=720)
image gx yelling = Image("images/galekh/galekh_pissed.png", ypos=730, xanchor=640, yanchor=720)
image gx smile = Image("images/galekh/galekh_pleased.png", ypos=730, xanchor=640, yanchor=720)

image gx question = Image("images/galekh/galekh_questioning.png", ypos=730, xanchor=640, yanchor=720)
image gx shock = Image("images/galekh/galekh_surprise.png", ypos=730, xanchor=640, yanchor=720)
image gx tattoo = Image("images/galekh/galekh_tattoocrookedsmile.png", ypos=730, xanchor=640, yanchor=720)
image gx tattoo_flush = Image("images/galekh/galekh_tattooflush.png", ypos=730, xanchor=640, yanchor=720)
image gx tattoo_hm = Image("images/galekh/galekh_tattooneutral.png", ypos=730, xanchor=640, yanchor=720)
image gx tatto_wince = Image("images/galekh/galekh_tattoowince.png", ypos=730, xanchor=640, yanchor=720)

image tbox = Image("gui/textbox_teal.png")

image money = "images/money/cashmoney.png"

image bg alternia = "images/bgs/alternia.png"
image bg tg_bath = "images/bgs/tagorabath.png"
image bg tg_ext = "images/bgs/tagoraexterior.png"
image bg tg_int = "images/bgs/tagorainterior.png"

image gx_good_end = "images/endings/Galekh_Good_End.png"
image tg_good_end = "images/endings/Tagora_win.png"

##jumpsec##### TRANSFORMS ##############

transform bounce:
    ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730

transform nod:
    ypos 730
    easeout 0.12 ypos 742
    linear 0.12 ypos 730

transform twitch:
    ypos 730 xpos 640
    easein 0.06 ypos 736 xpos 644
    linear 0.06 ypos 730 xpos 640

transform shudder:
    xpos 640
    linear 0.04 xpos 637
    linear 0.04 xpos 640
    linear 0.04 xpos 643
    linear 0.04 xpos 640
    repeat 4

transform lowered:
    ypos 730
    linear 0.75 ypos 765

transform bouncing:
    ypos 730
    linear 0.1 ypos 720
    linear 0.1 ypos 730
    repeat

transform shaking:
    ypos 730
    linear 0.07 ypos 732
    linear 0.07 ypos 730
    repeat

transform shuddering:
    xpos 640
    linear 0.04 xpos 637
    linear 0.04 xpos 640
    linear 0.04 xpos 643
    linear 0.04 xpos 640
    repeat

transform speaking:
    easein 0.1 zoom 1.01

transform stopspeaking:
    easein 0.1 zoom 1

transform shoveright:
    linear 0.1 xpos 960

transform shoveleft:
    xpos 640
    linear 0.1 xpos 320

transform shoveoffleft:
    linear 0.1 xpos -320

transform shoveup:
    xpos 640 ypos 1440
    linear 0.1 ypos 730

# transform statementbounce:
#     parallel:
#         alpha 0.0
#         linear 0.1 alpha 1.0
#         pause 1
#         easeout 1 alpha 0.0
#     parallel:
#         xpos 910 ypos 110
#         easein 1 ypos 95
#         pause 1
#         easeout 1 ypos 110
#
# transform moneybounce:
#     parallel:
#         alpha 0.0
#         linear 0.1 alpha 1.0
#         pause 1
#         easeout 1 alpha 0.0
#     parallel:
#         xpos 910 ypos 80
#         easein 1 ypos 65
#         pause 1
#         easeout 1 ypos 80

transform moneybounce:
    parallel:
        alpha 0.0
        linear 0.1 alpha 1.0
        pause 1.8
        easeout 2.0 alpha 0.0
    parallel:
        xpos 910 ypos 80
        easein 1 ypos 65
        pause 1.8
        easeout 1 ypos 80

transform statementbounce:
    parallel:
        alpha 0.0
        linear 0.1 alpha 1.0
        pause 1.8
        easeout 2 alpha 0.0
    parallel:
        xpos 910 ypos 110
        easein 1 ypos 95
        pause 1.8
        easeout 1 ypos 110

########################################################################
##jumpsec################ ACTUAL GAME SCRIPT ###########################
########################################################################

label start:

    $ pick = "{color=#000000}>{/color}"

    $ quick_menu = True

    $ volume1 = True

    jump start2

label start2:

    stop music fadeout 1.5

    show image "gui/main_menu.png"

    window hide

    scene black with Dissolve(1.5)

    $ main_menu = True

    call screen vol_select()

    stop music fadeout 1.5

label volumeone:

    $ renpy.block_rollback()

    $ main_menu = False

    show image "gui/game_menu.png"

    window hide

    scene black with Dissolve(1.5)

    op "First few lines of text from op"

    op "Now going to volume select screen"

    call screen troll_select1

    with Pause(0.25)

    return

##jumpsec################ TAGORA ROUTE ###########################

label tagora_route:

    $ renpy.block_rollback()

    scene black with Dissolve(1.0)

    scene bg alternia with dissolve

    $ quick_menu = True

    # TAGORA BILLS
    $ bill = 0

    $ tdone = "\n\n*__________"

    # GALEKH FOOTNOTES
    $ fndict = dict(
    a1="1 I live right around the corner.\n2 This is not a threat; rather it is a genuine expression of the critical nature of my request.{a=footnote:b1}{b}¹{/b}{/a}",
    b1="1 If it were a threat, you would know.",
    a2="1 It is possible your palate is not experienced enough to tell the difference, but I can walk you through the simpler points.",
    a3="1 Specifically, you misunderstanding me.\n2 I have spent considerable time in the interim researching you, of course, which is why I was able to track you down so easily.\n3 Rainbowfucker extraordinaire.{a=footnote:b3}{b}¹{/b}{/a}",
    b3="1 He wishes.",
    a4="1 Technically, not only specifically about that topic, but that is the pertinent piece of information in this conversational context.",
    # etc etc
    )

    # End initial route setup

    "Yes, someone is approaching! A strange, grey-skinned alien, with some other modifier that I don't really want to come up with right now. Who could it be????????"

    window hide

    play music "music/tagora_theme.mp3" loop

    show tg neutral with moveinbottom

    show screen billcount

    show tbox

    tspk "Some sample text [tdone]" (amt=100, stmt="First line of text")

    show tg neutral2 at twitch

    tspk "More sample text. [tdone]" (amt=10, stmt="Initial constructs")

    show tg judge at nod

    tspk "Eurgh." (amt=10, stmt="Initial constructs")

    show tg help at shoveoffleft

    hide tbox

    tspk "Bye." (amt=-110)

    hide screen billcount

    $ renpy.pause(0.5)

    $ quick_menu = False

    play music "music/victory_jingle.mp3" fadeout 1.0 noloop

    scene tg_good_end with Dissolve(1.0)

    $ renpy.pause()

    stop music fadeout 1.0

    scene black with Dissolve(1.0)

    return

##jumpsec################ GALEKH ROUTE ###########################

label galekh_route:

    $ renpy.block_rollback()

    scene black with Dissolve(1.0)

    scene bg alternia with dissolve

    $ quick_menu = True

    # TAGORA BILLS
    $ bill = 0

    $ tdone = "\n\n*__________"

    # GALEKH FOOTNOTES
    $ fndict = dict(
    a1="1 I live right around the corner.\n2 This is not a threat; rather it is a genuine expression of the critical nature of my request.{a=footnote:b1}{b}¹{/b}{/a}",
    b1="1 If it were a threat, you would know.",
    a2="1 It is possible your palate is not experienced enough to tell the difference, but I can walk you through the simpler points.",
    a3="1 Specifically, you misunderstanding me.\n2 I have spent considerable time in the interim researching you, of course, which is why I was able to track you down so easily.\n3 Rainbowfucker extraordinaire.{a=footnote:b3}{b}¹{/b}{/a}",
    b3="1 He wishes.",
    a4="1 Technically, not only specifically about that topic, but that is the pertinent piece of information in this conversational context.",
    # etc etc
    )

    # End initial route setup

    show gx smile with moveinbottom

    g "Placeholder text."

    $ renpy.pause()

    stop music fadeout 1.0

    scene black with Dissolve(1.0)

return
