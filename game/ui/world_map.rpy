screen m1_world_map():
    tag menu

    default selected_case = None

    add Solid("#08131b")

    vbox:
        xpos 70
        ypos 55
        spacing 6

        text "CASE ATLAS" size 44 color "#e7e1d7"
        text "Prototype world map — temporary Ren'Py-native presentation" size 22 color "#8394a0"

    frame:
        xpos 70
        ypos 155
        xsize 1160
        ysize 790
        background Solid("#0e202b")
        padding (35, 35)

        fixed:
            text "NORTH AMERICA" xpos 115 ypos 160 size 28 color "#405968"
            text "SOUTH AMERICA" xpos 315 ypos 500 size 25 color "#405968"
            text "EUROPE" xpos 710 ypos 180 size 25 color "#405968"
            text "AFRICA" xpos 720 ypos 390 size 25 color "#405968"
            text "ASIA / OCEANIA" xpos 890 ypos 255 size 23 color "#405968"

            add Solid("#183746", xsize=300, ysize=190) xpos 120 ypos 225
            add Solid("#16323f", xsize=170, ysize=245) xpos 330 ypos 430
            add Solid("#183746", xsize=210, ysize=120) xpos 665 ypos 245
            add Solid("#16323f", xsize=210, ysize=225) xpos 675 ypos 380
            add Solid("#183746", xsize=270, ysize=180) xpos 875 ypos 285

            textbutton "●  TORONTO":
                id "m1_toronto_node"
                xpos 310
                ypos 270
                text_size 27
                text_color "#c44747"
                text_hover_color "#ffffff"
                action SetScreenVariable("selected_case", "toronto")

            text "LOCKED CASE CAPACITY" xpos 860 ypos 610 size 18 color "#536570"
            text "Future cases are intentionally undefined." xpos 800 ypos 645 size 18 color "#536570"

    frame:
        xpos 1270
        ypos 155
        xsize 580
        ysize 790
        background Solid("#121a20")
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
            text "RECONSTRUCTION PLACEHOLDER" size 17 color "#d08b78"
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

