define m1_evidence_items = [
    (
        "RED UMBRELLA",
        "KNOWN FACT\nSamir Patel lent Mara a red umbrella at the photo lab. A tenant saw Mara carry it into her building. It was not in her apartment when police searched it.\n\nINFERENCE\nMara returned home after work, despite the earliest account suggesting otherwise.\n\nUNCONFIRMED\nWho removed the umbrella, and when."
    ),
    (
        "ANSWERING-MACHINE TAPE",
        "KNOWN FACT\nAt 7:08 p.m., Caleb Ross left a message saying he would check Mara's sticking door latch before eight. The original cassette remained in the machine.\n\nINFERENCE\nHis contact with Mara that evening was planned, not accidental.\n\nUNCONFIRMED\nWhether Mara heard the message before he arrived."
    ),
    (
        "FILM ENVELOPE",
        "KNOWN FACT\nMara brought home an unfinished roll from the photo lab. The envelope bears the lab date stamp and her handwriting.\n\nINFERENCE\nThe roll was among the ordinary objects she intended to sort that evening.\n\nUNCONFIRMED\nWhy the envelope later left the apartment."
    ),
    (
        "WITNESS STATEMENTS",
        "KNOWN FACT\nA tenant saw Mara enter with a red umbrella shortly after seven. Caleb first said he never visited her door and later said he saw her leave carrying the same umbrella after eight.\n\nINFERENCE\nThe two accounts cannot both describe the umbrella's movements accurately.\n\nUNCONFIRMED\nWhich detail the tenant may have remembered imperfectly."
    ),
]

define m1_timeline_items = [
    ("6:35 P.M.", "Mara leaves the photo lab with Samir's red umbrella."),
    ("7:03 P.M.", "A tenant sees Mara enter her apartment building."),
    ("7:08 P.M.", "Caleb's maintenance message is recorded."),
    ("BEFORE 8:00 P.M.", "Caleb is expected to inspect Mara's door latch."),
    ("8:00–9:00 P.M.", "Probable incident window; exact sequence initially unknown."),
    ("NEXT MORNING", "Suspicious remains are discovered behind a commercial block."),
]


label m1_early_investigation:
    scene m1_bg_investigation with dissolve
    show screen m1_reconstruction_badge("INVESTIGATIVE RECONSTRUCTION")

    m1_record "Identification does not come from one dramatic revelation. It comes from several ordinary things agreeing."
    m1_record "Rachel reports Mara missing after her calls go unanswered. She describes a small scar on Mara's hand, the coat she wore to work, and the photographs they planned to look through on Sunday."
    m1_record "Samir confirms Mara's final shift and the umbrella he lent her in the rain. The identification is formally established through additional official procedures."
    m1_record "The first working timeline remains incomplete."

    window hide
    call screen m1_investigation_timeline(m1_timeline_items)
    window show

    m1_record "Four items become important. They can be reviewed in any order."

    window hide
    call screen m1_evidence_viewer(m1_evidence_items)
    window show

    jump m1_wrong_direction


label m1_wrong_direction:
    m1_record "During the first days, the missing coat and Caleb's account suggest that Mara left the building again after eight."
    m1_record "Investigators consider whether she arranged a private meeting and whether someone outside her normal circle accompanied her."
    m1_record "Mara was private. That true description becomes an invitation for speculation: an unknown relationship, an undisclosed plan, a voluntary departure."
    m1_record "It is plausible because the record is incomplete—not because evidence confirms it."

    rachel "Private doesn't mean secret. She told me small things because small things were most of her life. A broken latch. A borrowed umbrella. Pictures she hadn't developed."

    m1_record "Rachel's distinction returns attention to the apartment building and to the order of known events."
    jump m1_contradiction_question


label m1_contradiction_question:
    m1_record "Which detail most strongly conflicts with the claim that Mara never returned home after work?"

    menu:
        "The film roll was unfinished":
            m1_record "Not by itself. An unfinished roll describes Mara's habit, but it does not establish where she went after work."
            m1_record "Look for an observation that places both Mara and an identifiable object."
            jump m1_contradiction_question

        "Rachel expected photographs on Sunday":
            m1_record "That establishes Mara's plans and relationship with Rachel, not her movement that evening."
            m1_record "The stronger contradiction joins a workplace object to a building observation."
            jump m1_contradiction_question

        "A tenant saw Mara bring Samir's red umbrella into the building":
            m1_record "Correct. Samir identifies the borrowed umbrella at work, and an independent tenant places Mara and that same distinctive object inside the building shortly after seven."
            m1_record "Caleb's earliest suggestion that she never came home cannot stand. His later account—that she left again carrying it—now requires scrutiny."
            jump m1_reinterpretation


label m1_reinterpretation:
    scene m1_bg_apartment with dissolve
    show screen m1_reconstruction_badge("EARLIER DETAILS • RECONSIDERED")

    m1_record "The first evening was not a separate prologue. It was evidence before it had that name."

    if m1_red_umbrella_seen:
        "The red umbrella stood open beside Mara's door, Samir's name taped around its shaft. Caleb could see it during his first maintenance visit."

    if m1_answering_machine_checked:
        "The answering-machine cassette preserved Caleb's own voice: he planned to return before eight to inspect the latch. His first statement denied any planned visit."

    if m1_photo_checked:
        "The yellow film envelope was on Mara's table, marked in her handwriting. It was absent when the apartment was searched."

    if m1_kitchen_note_seen:
        "The receipt on the refrigerator still carried two unfinished intentions: call Rachel; return the library book. Ordinary plans interrupted, not evidence of a planned disappearance."

    m1_record "No single object explains the crime. Together, they expose the limits of the first reconstruction."
    jump m1_resolution


label m1_resolution:
    scene m1_bg_investigation with dissolve
    show screen m1_reconstruction_badge("CASE RESOLUTION • FICTIONAL COMPOSITE")

    m1_record "The investigation continues for months, not minutes. Statements are retaken. Maintenance access records are compared with the answering-machine tape and witness times."
    m1_record "Caleb changes his account: first Mara never returned, then she returned but left alone, then his visit happened earlier than the recorded message."
    m1_record "A lawful search of the building's maintenance storage recovers Samir's red umbrella and Mara's marked film envelope among items Caleb controlled."
    m1_record "Those objects do not stand alone. Trace evidence, access records, and independent testimony corroborate the timeline and link Caleb to Mara after his claimed final contact."
    m1_record "Investigators conclude that he used the expected maintenance visit to approach her. The exact physical sequence is not recreated here."
    m1_record "Caleb Ross is arrested. At trial, the recording, recovered property, timeline evidence, and corroborating forensic findings establish accountability. He is convicted."

    m1_record "A conviction resolves legal responsibility. It does not restore the ordinary future recorded on Mara's refrigerator."
    jump m1_memorial
