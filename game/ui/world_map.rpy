screen m1_world_map():
    tag menu

    default selected_case = None

    add "m1_bg_map"
    add Solid("#06101877")

    vbox:
        xpos 70
        ypos 55
        spacing 6
        text "CASE ATLAS" size 44 color "#e7e1d7"
        text "Select a location to open its case file" size 22 color "#a9b5bc"

    # The texture is atmosphere only. This node remains the authoritative,
    # keyboard-accessible location marker.
    textbutton "●  TORONTO":
        id "m1_toronto_node"
        xpos 390
        ypos 340
        text_size 27
        text_color "#d76767"
        text_hover_color "#ffffff"
        action SetScreenVariable("selected_case", "toronto")

    frame:
        xpos 1270
        ypos 155
        xsize 580
        ysize 790
        background Solid("#0b141bdd")
        padding (38, 38)

        if selected_case == "toronto":
            vbox:
                spacing 18
                text "TORONTO, CANADA — 1998" size 25 color "#9fb0bc"
                text "THE RED UMBRELLA" size 40 color "#e7e1d7"
                text "FICTIONAL COMPOSITE CASE" size 24 color "#d26262"
                null height 8
                text "Created for prototype development.\nNo real person or historical case is depicted." size 24 color "#c7c7c7" line_spacing 7
                null height 16
                text "Documentary reconstruction • 10–15 minute vertical slice" size 21 color "#8797a2"

                if m1_case_completed:
                    text "CASE COMPLETED" size 24 color "#91b79a"
                else:
                    text "AVAILABLE" size 24 color "#d8c895"

                null height 30
                textbutton "BEGIN CASE":
                    id "m1_begin_case"
                    xsize 330
                    text_size 27
                    action Return("m1_start")
        else:
            vbox:
                spacing 20
                text "SELECT A CASE NODE" size 30 color "#e7e1d7"
                text "Choose the Toronto marker to open the prototype case file." size 24 color "#8797a2"
                null height 20
                text "The marker defines the selectable geography." size 20 color "#71838e"

    text "AI-GENERATED DRAMATIZED RECONSTRUCTION" xpos 70 ypos 925 size 17 color "#d08b78"

    textbutton "MAIN MENU":
        xpos 70
        ypos 975
        text_size 22
        action MainMenu(confirm=True)


screen m1_reconstruction_badge(location_text):
    frame:
        xalign 1.0
        xoffset -35
        yalign 0.0
        yoffset 30
        background Solid("#10161acc")
        padding (18, 10)

        vbox:
            text "AI-GENERATED DRAMATIZED RECONSTRUCTION" size 17 color "#d08b78"
            text location_text size 19 color "#d9d9d9"


screen m1_title_card(heading, subheading=""):
    modal True
    add Solid("#090c0e")

    vbox:
        xalign 0.5
        yalign 0.46
        spacing 20
        text heading xalign 0.5 text_align 0.5 size 52 color "#e7e1d7"
        if subheading:
            text subheading xalign 0.5 text_align 0.5 size 28 color "#91a0aa"

        null height 25
        textbutton "CONTINUE":
            id "m1_title_continue"
            xalign 0.5
            text_size 24
            action Return()
