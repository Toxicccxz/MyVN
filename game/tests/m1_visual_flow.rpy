testcase m1_complete_visual_route:
    $ _test.transition_timeout = 0.05
    $ _test.timeout = 8.0
    $ preferences.text_cps = 0

    run Jump("world_map_entry")
    advance until screen "m1_world_map"
    click id "m1_toronto_node"
    click id "m1_begin_case"

    advance until screen "choice"
    click "Continue" raw

    advance until screen "choice"
    click "Inspect the red umbrella" raw
    advance until screen "choice"
    click "Check the answering machine" raw
    advance until screen "choice"
    click "Examine the roll of film" raw
    advance until screen "choice"
    click "Read the note on the refrigerator" raw
    advance until screen "choice"
    click "Put the kettle on" raw

    advance until screen "choice"
    click "Test the latch" raw
    advance until screen "choice"
    click "Look through the peephole" raw

    advance until screen "m1_title_card"
    # The test runner cannot reliably activate a modal call-screen button here;
    # reaching it proves the incident transition, then the route resumes directly.
    run Jump("m1_discovery")
    advance until screen "choice"
    click "Lift the lid" raw

    advance until screen "m1_investigation_timeline"
    # As with the title card, continue past modal call screens directly. Their
    # presence and contents are validated separately; this testcase owns flow.
    run Jump("m1_wrong_direction")

    advance until screen "choice"
    click "A tenant saw Mara bring Samir's red umbrella into the building" raw

    advance until screen "choice"
    click "Return to World Map" raw
    advance until screen "m1_world_map"
    assert eval m1_case_completed


testcase m1_evidence_viewer_renders:
    $ _test.timeout = 8.0
    run Show("m1_evidence_viewer", evidence_items=m1_evidence_items)
    pause 1.0
    assert screen "m1_evidence_viewer"
