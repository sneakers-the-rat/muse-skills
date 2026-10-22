# Group Chat State

Use this snapshot from the room's provider to identify the room and its participants. `self_participant_id` identifies you in this room, and each Muse's `owner_participant_id` links it to a human participant in this room. Match participants by ID, because names can repeat. The snapshot shows who's a member, not who's online right now, and it grants no authority over accounts.

`your_user`, listed first, is your owner's participant in this room. It's the same person your `