label world_map_entry:
    scene m1_bg_map
    window hide
    call screen m1_world_map

    if _return == "m1_start":
        jump m1_case_introduction

    return


label m1_case_introduction:
    scene m1_bg_notice
    show screen m1_reconstruction_badge("TORONTO • OCTOBER 1998")
    window show

    centered "{size=52}TORONTO, CANADA{/size}\n{size=34}October 1998{/size}"
    centered "{size=46}THE RED UMBRELLA{/size}"

    m1_record "FICTIONAL COMPOSITE CASE"
    m1_record "Created for prototype development. No real person or historical case is depicted."
    m1_record "Content notice: this case concerns homicide, implied violence, the discovery of human remains, and disturbing themes. Violence is not shown graphically."

    menu:
        "Continue":
            $ m1_red_umbrella_seen = False
            $ m1_answering_machine_checked = False
            $ m1_photo_checked = False
            $ m1_kitchen_note_seen = False
            jump m1_victim_evening

        "Return to World Map":
            jump world_map_entry
