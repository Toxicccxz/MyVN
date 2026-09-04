label m1_memorial:
    scene m1_bg_memorial with dissolve
    hide screen m1_reconstruction_badge

    centered "{size=48}MARA ELLIS{/size}"

    "Mara was twenty-nine. She worked at a small photo lab and lived alone in an apartment where the chairs did not match."
    "She kept receipts and notes longer than necessary. She photographed streets after rain, though she insisted that did not make her an artist."
    "She borrowed an umbrella from a coworker and meant to return it. She meant to call her sister. She meant to bring lake photographs to Sunday dinner."

    rachel "The pictures weren't important because they solved anything. They were important because she took them."

    m1_record "The victim is a person first and a case second."
    m1_record "Remember Mara's attention, her routines, her unfinished plans—not only the violence that ended them."

    centered "{size=31}THE RED UMBRELLA is a fictional composite case created for this prototype.{/size}\n{size=27}No real victim, offender, or historical homicide is depicted.{/size}"

    $ m1_case_completed = True

    menu:
        "Return to World Map":
            jump world_map_entry

