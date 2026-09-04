screen m1_evidence_viewer(evidence_items):
    modal True
    default selected_evidence = 0

    add Solid("#0b1116")

    vbox:
        xpos 65
        ypos 50
        spacing 5
        text "EVIDENCE REVIEW" size 43 color "#e7e1d7"
        text "Select an item. Categories separate fact from interpretation." size 22 color "#8496a1"

    frame:
        xpos 65
        ypos 150
        xsize 520
        ysize 790
        background Solid("#111c23")
        padding (30, 30)

        vbox:
            spacing 18
            for index, item in enumerate(evidence_items):
                textbutton item[0]:
                    xsize 450
                    text_size 24
                    selected (selected_evidence == index)
                    action SetScreenVariable("selected_evidence", index)

    frame:
        xpos 625
        ypos 150
        xsize 1230
        ysize 790
        background Solid("#151b20")
        padding (48, 42)

        vbox:
            spacing 24
            text evidence_items[selected_evidence][0] size 37 color "#d9d0c2"
            hbox:
                spacing 34
                frame:
                    xsize 620
                    ysize 390
                    background Solid("#080d10")
                    padding (10, 10)
                    add evidence_items[selected_evidence][1] xysize (600, 338) xalign 0.5 yalign 0.5
                text evidence_items[selected_evidence][2] xsize 470 size 23 color "#c4cbd0" line_spacing 7

    textbutton "RETURN TO INVESTIGATION":
        id "m1_evidence_return"
        xpos 65
        ypos 975
        text_size 22
        action Return()


screen m1_investigation_timeline(timeline_items):
    modal True
    add Solid("#0a1015")

    vbox:
        xalign 0.5
        ypos 70
        spacing 16

        text "WORKING TIMELINE" xalign 0.5 size 42 color "#e7e1d7"
        text "October 1998 • Toronto" xalign 0.5 size 23 color "#8ea0ac"

        null height 20

        for time_text, event_text in timeline_items:
            frame:
                xsize 1180
                background Solid("#15212a")
                padding (26, 16)
                hbox:
                    spacing 35
                    text time_text xsize 230 size 23 color "#c3a879"
                    text event_text xsize 850 size 23 color "#d0d4d6"

        null height 15
        textbutton "CONTINUE":
            id "m1_timeline_continue"
            xalign 0.5
            text_size 23
            action Return()
