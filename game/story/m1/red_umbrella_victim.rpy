label m1_victim_evening:
    scene m1_bg_apartment with dissolve
    show screen m1_reconstruction_badge("MARA'S APARTMENT • OCTOBER 1998")

    centered "{size=43}MARA ELLIS, 29{/size}\nEmployee, Bellweather Photo Lab"

    "Rain follows Mara home in the hems of her trousers and the paper bag tucked beneath her arm."
    "Her apartment is modest: one good lamp, two mismatched chairs, and a kitchen table that collects everything she means to sort later."

    mara "Keys, kettle, dry socks. In that order."

    "She sets the borrowed red umbrella beside the entrance, where it drips into an old baking tray."

    samir "Take it. Bring it back tomorrow, or next June. Whichever comes first."
    "The memory of Samir's joke is still fresh enough to make her smile."

    jump m1_apartment_exploration


label m1_apartment_exploration:
    if m1_red_umbrella_seen and m1_answering_machine_checked and m1_photo_checked and m1_kitchen_note_seen:
        menu:
            "Put the kettle on":
                jump m1_subtle_unease

            "Look around once more":
                pass

    menu:
        "Inspect the red umbrella" if not m1_red_umbrella_seen:
            $ m1_red_umbrella_seen = True
            "The umbrella is too bright for Mara's apartment: red nylon, black handle, one bent spoke."
            "A strip of masking tape around the shaft reads SAMIR in block letters. She leaves it open to dry beside the door."
            mara "Tomorrow. I won't forget."
            jump m1_apartment_exploration

        "Check the answering machine" if not m1_answering_machine_checked:
            $ m1_answering_machine_checked = True
            "The machine clicks. The first message carries Rachel's familiar impatience."
            rachel "Mara, Sunday dinner. You said you'd bring those lake pictures, and I am recording this so you can't claim I never reminded you. Call me when you're in."
            "Mara reaches for the phone, then notices the second message light."
            caleb "Ms. Ellis, Caleb downstairs. I found your note about the sticking latch. I'll come by after I finish the second floor—before eight. Should only take a minute."
            "The tape stops with a soft mechanical clack."
            mara "Tea first. Then Rachel. Then the door."
            jump m1_apartment_exploration

        "Examine the roll of film" if not m1_photo_checked:
            $ m1_photo_checked = True
            "An unfinished roll sits in a yellow lab envelope. Mara has written: RACHEL — LAKE / STREET AFTER RAIN."
            "She holds one negative strip toward the lamp. A blurred streetlight floats in the frame like a pale moon."
            mara "Not art. Just proof I looked up once in a while."
            "She returns the envelope to the table rather than the drawer."
            jump m1_apartment_exploration

        "Read the note on the refrigerator" if not m1_kitchen_note_seen:
            $ m1_kitchen_note_seen = True
            "A grocery receipt is pinned beneath a souvenir magnet. On its back Mara has written: MILK. CALL RACHEL. RETURN LIBRARY BOOK."
            "The library book is already waiting by the door. She crosses out MILK and leaves the other two lines untouched."
            jump m1_apartment_exploration

        "Put the kettle on" if m1_red_umbrella_seen and m1_answering_machine_checked and m1_photo_checked and m1_kitchen_note_seen:
            jump m1_subtle_unease


label m1_subtle_unease:
    "The kettle begins its low pre-boil murmur. In the corridor, a ladder scrapes gently across tile."
    "Three measured knocks follow."

    caleb "Ms. Ellis? Building maintenance. It's Caleb."

    "Mara opens the door on its chain. Caleb stands beneath the unlit corridor fixture with a screwdriver and a folded work sheet."

    caleb "Bulb is done. Your latch was next on my list. Still catching?"
    mara "Only when the weather changes."
    caleb "Everything in this building has opinions about the weather."

    "He tests the latch while Mara holds the door. His manner is practiced and ordinary. When a tenant passes, he steps aside without being asked."
    "For a moment his gaze settles past Mara, toward the red umbrella drying inside. Then he checks the strike plate again."

    caleb "I need a different screw. I'll finish the other floor and come back. Before eight, like I said."
    mara "All right. Knock loudly. The machine is louder than the hallway."

    "He leaves. The corridor light holds steady for several seconds, then flickers once."

    menu:
        "Test the latch":
            "Mara closes the door and tests it twice. It catches on the second pull—annoying, not alarming."

        "Listen to the corridor":
            "The ladder scrapes away. A service door closes somewhere below. Then the building returns to pipes, rain, and distant television."

        "Return to the kettle":
            "Mara decides the tea has already waited long enough."

    "She pours the water, calls Rachel, and gets no answer."
    mara "Your turn to call me back."

    "Outside, evening traffic turns the wet street into ribbons of muted light."
    jump m1_incident_threshold


label m1_incident_threshold:
    scene m1_bg_hallway with dissolve
    show screen m1_reconstruction_badge("INCIDENT THRESHOLD • RECONSTRUCTED")

    "At 7:56 p.m., another knock interrupts the radio. Not loud. Not urgent."
    "Mara sets down her cup."

    menu:
        "Look through the peephole":
            "The corridor light is dark again. She can make out a shoulder, the edge of a work jacket, and something pale held near the door."
            mara "Caleb?"
            caleb "Found the right screw."

        "Ask who is there":
            mara "Who is it?"
            caleb "Caleb. Last thing, then I'll leave you to your evening."
            "The answer is ordinary enough to fit the earlier visit."

        "Check the hallway from the chained door":
            "Mara opens the door as far as the chain permits. The corridor bulb is out; Caleb waits beside his small maintenance case."
            caleb "Bad connection after all. I can still fix your latch."

    "Mara rests one hand on the chain. The answering machine begins to rewind behind her."
    "Something shifts in the dark beyond the door—too close, too quickly."

    hide screen m1_reconstruction_badge
    scene m1_bg_black
    "The radio continues for half a sentence."
    "Then it stops."

    call screen m1_title_card("THE FOLLOWING MORNING", "Behind a commercial block • west Toronto")
    jump m1_discovery


label m1_discovery:
    scene m1_bg_discovery with dissolve
    show screen m1_reconstruction_badge("MUNICIPAL ROUTE • RECONSTRUCTION PLACEHOLDER")

    "A municipal sanitation worker backs a collection truck into the service lane. Rainwater has gathered in shallow dents in the pavement."
    "One dumpster lid is not fully closed. A torn plastic bag is caught along its rim."
    "The worker climbs down, checks the route sheet, and approaches."

    menu:
        "Lift the lid":
            "The lid rises several inches."

    "The worker freezes. Whatever is inside is immediately wrong—not discarded property, not something to move with a gloved hand."
    "The lid falls shut. The worker steps back and calls for emergency services."

    hide screen m1_reconstruction_badge
    scene m1_bg_black
    m1_record "No graphic image is shown. Investigators later confirm that human remains were discovered."
    m1_record "The perspective now shifts from Mara's lived evening to an investigative reconstruction assembled over time."

    jump m1_early_investigation

