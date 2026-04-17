label sh_ch43:
    label .s1:

        $ set_window_tint(TINT_LILLY)

        scene bg kasshoku_englishcafe
        show crowd
        show hiroyuki serious_close at center:
            xpos 0.45
        with Dissolve(2.0)

        play music music_pearly fadein 4.0

        play ambient sfx_crowd_indoors fadein 1.0

        play sound sfx_phonedial # TODO maybe replace with phone ringing sfx

        pause 3.0

        li "Hmmm. No response this time either."

        show hiroyuki thinking_close
        with chchange

        hyf "Perhaps she is taking a restroom break right now."
        li "Perhaps. But since it's nearly four o' clock already, I'd be surprised if they're not already at our meeting point. The building they went to was rather close to the entrance if I recall correctly."

        show hiroyuki eyebrow_close
        with chchange

        hyf "Maybe we should head back to the entrance ourselves after all."

        show hiroyuki serious_close
        with chchange

        li "It would be rude to show up late without letting the others know."

        play sound sfx_phonedial

        "I absentmindedly pick my phone back up and dial Hisao's number this time. Maybe I'll have more luck with him."
        li "..."

        play sound sfx_phonepickup

        show hisao basic_smile_swt_phone at phonebox
        with charaenter

        hi "Hey, Lilly."
        li "Hisao, good to hear from you. How was your day?"

        show hisao basic_grin_swt_phone
        with chchange

        hi "Tiring, but very interesting. They gave some pretty interesting workshops over here."
        hi "I've just left the faculty building, so if I keep a steady pace I can be at our meeting spot in ten minutes. I hope you can forgive the slight tardiness."
        li "Ah... About that... The last lecture at the English faculty took longer than expected and we landed in the middle of rush hour here. I suggested to Father to take a little break in the building's cafeteria. Today was a rather busy day."

        show hisao basic_neutral_swt_phone
        with chchange

        hi "Is your father alright?"
        "He's not exactly in peak condition yet, and he seemed a bit tired earlier, which is why I offered to take a break here rather than immediately take the rather long walk back to the entrance. I'd like him to save his strength."
        "Of course, I can't tell Hisao that or Father will overhear and might feel that I'm being a busybody."
        li "Yes, he's fine. Hisao, would it be a problem for you to come over to the English faculty building and join us here?"

        show hisao basic_sweet_swt_phone
        with chchange

        hi "Well, it's probably not that much further from here than the entrance, so I don't mind."
        "I smile."
        li "Much obliged. Father and I will be sure to treat you for your trouble."

        show hisao basic_smile_swt_phone
        with chchange

        hi "Okay, I'll be there in about ten minutes."

        hide hisao
        with charaexit

        "I hang up and turn to Father."
        li "Hisao will be here shortly."

        show hiroyuki eyebrow_close
        with chchange

        hyf "We'll still need to get in touch with Miss Ikezawa and Miss Inoue."
        li "Hmmm... Maybe I should wait a bit. It's strange that Hanako has her cell phone turned on and yet isn't responding to my calls."

        show hiroyuki awkward_close
        with chchange

        hyf "But we cannot simply keep them waiting at the front gate. It will still take them some time to get here. I assume you do not have Miss Inoue's number?"
        li "I'm afraid I don't. Hanako got to know her through the newspaper club. I've never really interacted with her much."

        show hiroyuki eyebrow_close
        with chchange

        hyf "Despite the fact that she's friends with Miss Ikezawa and she seems to admire your mother?"

        show hiroyuki serious_close
        with chchange

        play sound sfx_phonedial

        "I nod while absentmindedly dialing Hanako's number once more."
        li "I don't have the passion for writing and journalism that the three of them seem to share, or I'd probably have befriended her as well."
        li "It's not that I dislike her. She seems to be a kind-hearted person who's always cheerful and in high spirits, and Hanako seems to enjoy hanging out with her."
        li "It's just that I already have plenty of friends at school and one can only maintain so many friendships at the same time."

        play sound sfx_phonepickup

        "I smile as I hear the sound of Hanako's phone being picked up..."
        li "Hanako?"

        play music music_rain

        show naomi basic_angry_phone at phonebox
        with Dissolve(0.2)

        na "Where the HELL ARE YOU?{fast}"
        "...only to nearly drop my phone in surprise as an angry voice on the other end of the line snarls at me."

        show hiroyuki eyebrow_close
        with chchange

        li "H-Hanako?"

        show naomi basic_annoyed_phone
        with chchange

        na "It's not Hanako, it's me."
        "It's Naomi. But what's gotten into her?"
        li "Ah... What is the meaning of this?"

        show naomi basic_angry_phone
        with chchange

        na "I'm at the entrance and you guys aren't. So again... Where... ARE... you?"
        "What's going on? Why is Naomi answering Hanako's phone? And what is she so angry about?"
        li "W-we're at the English faculty's cafeteria. I wanted to ask if you'd be willing to come over here and let us treat you to something to eat."

        show naomi basic_concern_phone
        with chchange

        "I hear what sounds like a desperate sigh on the other end."
        na "You called... just... for... that?"
        li "Y-yes... What's going on?"

        show naomi basic_serious_phone
        with chchange

        na "Stay put. I'm on my way over to where you are."
        li "Why are you answering Hanako's phone? Where is she?"

        show naomi basic_concern_phone
        with chchange

        na "...No idea."
        "An ominous feeling worms its way into the pit of my stomach at Naomi's words."
        li "No idea? What happened? Did you lose sight of her?"

        show naomi basic_serious_phone
        with chchange

        na "Something like that. Stay where you are. I'm on my way."
        li "We could head towards the entrance ourselves and meet up half-way."

        show naomi basic_annoyed_phone
        with chchange

        na "Not needed. You've already done enough for one day."

        hide naomi
        with charaexit

        "What's that supposed to mean?"
        li "Naomi... Naomi?"
        "No more response. She must have hung up the phone."
        "What happened? Naomi's tone was really hostile... venomous even. I can make neither heads nor tails of it."
        hyf "Is something wrong? You look very upset."
        li "I just called Hanako's number, yet Naomi was the one who picked up the phone. She said she has lost sight of Hanako and is heading this way."

        show hiroyuki serious_close
        with chchange

        li "She sounded really... angry about something. I don't really understand what's going on."

        show hiroyuki thinking_close
        with chchange

        hyf "Hmmm... If Miss Ikezawa has gone missing yet she has left her phone with Miss Inoue, finding her here will be quite difficult."
        "I don't even want to think about that right now. I hope Hisao and Naomi are here soon."

        scene bg kasshoku_englishcafe
        show crowd
        show hiroyuki eyebrow_close at center:
            xpos 0.45 ypos 1.03
        with shorttimeskip

        hyf "Hmmm... I think I see Mister Nakai near the entrance over there. Perhaps you should get up for a second, Lilly. You are almost certain to draw his attention that way."
        li "How are we supposed to tell Hisao that his girlfriend has gone missing?"

        show hiroyuki serious_close
        with chchange

        hyf "Until we know the details, it may be best not to mention the matter at all. Undue worrying will only cause stress."
        li "Ah..."
        "I'm not sure if I'm completely comfortable with that, but since I don't really know what's going on either, all we'd be doing until Naomi gets here would be throwing speculations back and forth."

        show hisao basic_smile_swt at left:
            ypos 1.03
        with charaenter

        show hiroyuki smile_close
        with chchange
        show hisao basic_smile_swt_close
        with chchange

        hi "Hey, Lilly. Hello, sir."
        li "Hello, Hisao."

        show hiroyuki smileclosed_close
        with chchange

        hyf "Good afternoon, Mister Nakai. Have you had a good time today?"

        show hisao cross_grin_swt_close
        with chchange

        hi "Yeah, it was pretty interesting. They had a whole group of first-years who had a wide range of basic scientific experiments going that you could take part in like building a primitive electromagnet or creating different colors of fire."
        hi "It's kind of a cheap way to reel people in, but it's pretty effective nevertheless."
        hi "I've built up a pretty impressive list of experiments that are easy to do at the science club. It might help the guys attract more new members at the start of the next school year."
        li "It sounds like you had fun."

        show hiroyuki thinking_close
        show hisao cross_neutral_swt_close
        with chchange

        "Hisao pauses."

        show hisao cross_speak_swt_close
        with chchange

        hi "No nerd-related comeback this time?"
        "I smile awkwardly. Hanako and I often joke about how Hisao has gotten slightly nerdier since he founded the science club, and what he just said was indeed practically begging for a playful little jab, but after the talk I just had with Naomi I'm not in a teasing mood anymore."

        show hisao basic_neutral_swt_close
        with chchange

        li "Maybe some other time."
        hi "You didn't have fun today?"
        li "I did."

        show hiroyuki speak_close
        with chchange

        hyf "One of the things Lilly and I attended today was a student panel reciting various excerpts from English poetry and literature. I believe the students participating were first-years as well. Perhaps the two of you will be in their place next year."

        show hisao basic_speak_swt_close
        show hiroyuki serious_close
        with chchange

        hi "I think I'd like that..."
        "I notice Hisao's voice trailing off as he finishes his sentence."
        li "Hisao, is something the matter?"
        hi "I thought I just saw Naomi among those people near the entrance. Her hair's pretty easy to spot."
        "I guess this is it."

        show hisao cross_speak_swt_close
        with chchange

        hi "Yeah, it's her alright. She looks pretty winded. Did she run all the way over here?"
        hi "Hey, where's Hanako?"

        show hisao basic_neutral_swt_close
        show naomi basic_shock at right:
            ypos 1.03
        with charaenter

        "I hear someone running up to us followed by the sound of heavy breathing."

        show hisao cross_speak_swt_close
        with chchange

        hi "Naomi, what on earth is going on? Where's Hanako?"
        hi "Don't tell me you two got separated."
        na "I... That's..."

        show hisao basic_frown_swt_close
        with chchange

        hi "Damnit, you know she doesn't handle crowded places well."
        "Hisao sounds agitated. He's probably as worried as I am right now."

        show naomi basic_annoyed
        with chchange

        "Naomi lets out a joyless laugh in response while trying to catch her breath."
        na "H-hahaha... R-really? You... learn s-something... new every day."

        show hisao cross_speak_swt_close
        with chchange

        hi "What on earth is that supposed to mean? What happened?"

        show hisao cross_neutral_swt_close
        show hiroyuki speak_close
        with chchange

        hyf "Hmmm, you had better get seated and take a few moments to catch your breath, Miss Inoue. Then you can tell us what has happened."

        show hiroyuki serious_close
        show naomi basic_concern_close
        with chchange

        "I hear Naomi sit down next to me, and we anxiously wait until her ragged breathing slows down."
        "She finally lets out a loud sigh as she puts something on the table that's probably a backpack."

        show hisao basic_worry_swt_close
        with chchange

        na "If you guys have any suggestions on how to find her, I'm all ears, because I'm fresh out of ideas."

        show hiroyuki thinking_close
        show naomi basic_neutral_close
        with chchange

        hyf "Miss Inoue, it would probably be better to start at the beginning. You and Miss Ikezawa lost sight of one another. Yet you are carrying her backpack. You did not just get separated in the middle of a crowd, did you?"
        na "...No."
        "Another silence."

        show hiroyuki serious_close
        with chchange

        na "She... uh... We were still attending a lecture when her phone went off. She... probably forgot to turn it off. She kept it in her backpack, so she couldn't immediately take it out and turn it off either..."
        "Oh no! I didn't even think of the possibility of Hanako not having her phone turned off or Hanako's and Naomi's program taking longer than mine. How could I have been so stupid?"
        "I hear Hisao let out a pained groan."
        hi "Are you saying that she became the center of attention, panicked, and then ran off?"
        na "Something like that. I... uh... didn't even know it was her phone at first. Nobody's ever called her in my presence before, so I didn't know what her ringtone sounded like."
        na "When that second phone call came and I realized it was probably Hanako whose phone was ringing, I tried to make my way over to her, but she got up and ran away just before I got to her."

        show hisao cross_speak_swt_close
        with chchange

        hi "Make your way over to her? Was that classroom so crowded you had to push your way past several people just to get to her?"
        "For a moment Naomi doesn't answer."
        "When she finally speaks, her voice is little more than a whisper."

        show naomi basic_concern_close
        with chchange

        na "It... wasn't a classroom. It... it was a lecture hall. And most seats were occupied too. Like... perhaps... around 150 people. Maybe 200."
        na "And... {i}*sigh*{/i} I bet a lot of those were looking in Hanako's direction by the time she finally lost it."

        show hisao basic_worry_swt_close
        with chchange

        "{i}200 PEOPLE?{/i} It feels like my blood suddenly freezes in my veins, and for a few seconds my reaction is to deny it in my mind."
        "Surely she's exaggerating. This couldn't have happened. Because if it's true... If it's really true then... then I..."
        "...Then I did something truly unforgivable to my best friend."

        show hiroyuki thinking_close
        show hisao basic_frown_swt_close
        with chchange

        hi "Shit."
        "But the sound of Hisao softly cursing under his breath hammers home the point that this is all too real."
        "The thought of Hanako's terrified expression in the middle of a crowd that's becoming more and more aware of her presence with every passing second is enough to make my blood curdle, and for a moment I feel like I'm going to pass out."
        li "Oh my God..."
        "For several long seconds nobody knows what to say. Then Hisao speaks up with a baffled tone in his voice."

        show hiroyuki serious_close
        show hisao basic_annoy_swt_close
        with chchange

        hi "You and Hanako attend a lecture in a large and crowded HALL, and you thought it was a good idea to take a seat... I don't know how far... AWAY FROM HER? What on earth were you thinking?"

        show naomi basic_angry_close
        with chchange

        na "Hey, don't give me that! I thought I'd give her a seat near the edge of the room, and there weren't too many of those left! Besides, it wasn't me who called her... TWICE!"
        li "THAT'S NOT FAIR! I DIDN'T KNOW YOUR PROGRAM ENDED LATER! IF YOU KNEW THIS IN ADVANCE THEN WHY DIDN'T YOU LET US KNOW BEFOREHAND?"
        na "WE WOULD HAVE MADE IT TO THE ORIGINAL MEETING POINT IN TIME IF IT HADN'T BEEN FOR THIS SUDDEN CHANGE OF PLANS OF YOURS! WHAT THE HELL WAS UP WITH THAT ANYWAY? WAS IT REALLY TOO MUCH TO WALK FOR A FEW MORE MINUTES?"
        li "I WAS JUST TRYING TO...!"

        $ renpy.music.set_pause(True)
        play sound sfx_impact2

        show hiroyuki scold_close
        show hisao basic_neutral_swt_close
        show naomi basic_confused_close
        with vpunch

        hyf "{cps=200}Lillian!{w=0.5} Inoue!{w=0.5} Nakai!"
        "We all fall silent as the stern and authoritive tone in Father's voice cuts our argument short."

        show hiroyuki stern_close
        show naomi basic_concern_close
        with chchange

        hyf "We are all worried here, but pointing fingers and making a public spectacle will not help us find Ikezawa. And people are looking at us right now."
        li "Sorry Father."
        hi "Sorry..."
        na "Yeah, sorry."
        "I realize with some embarrassment that we've just been hysterically shouting at each other. People around here must have wondered what's going on."

        show hiroyuki stern_close
        show hisao cross_worry_swt_close
        show naomi basic_neutral_close
        with chchange

        hyf "Let us first return to the entrance. It was our original meeting point. If she is, by any chance, searching for us at the moment then that place is where she will be looking for us."
        "I personally doubt that Hanako is currently actively looking for us, but Father does have a point. Sitting around here won't do much good."

        show hiroyuki serious_close
        show hisao basic_worry_swt_close
        with chchange

        hi "Okay then."

        scene bg kasshoku_grounds_ss
        show crowd_ss
        show hisao basic_neutral_swt_ss at twoleft:
            xpos 0.25
        show naomi basic_neutral_ss at center
        show hiroyuki serious_close_ss at right
        with locationchange

        play music music_moonlight fadein 4.0

        "We get up and head out, going for the quickest pace I can manage. I find it a bit hard to keep up and hold tight to Father's arm, praying I won't end up bumping into people."
        "Apparently though, we're still not going fast enough for everyone as Naomi speaks up after merely a few minutes."

        show naomi basic_serious_ss
        with chchange

        na "Say, would you guys mind if I went on ahead?"
        "Father lets out a soft “hmmm”."

        show hiroyuki speak_close_ss
        with chchange

        hyf "Miss Inoue, do you remember where I parked the car this morning?"
        na "Uh, yeah. I think so."
        hyf "When you get to the entrance and Miss Ikezawa is not there, please stop by the car and look for her there as well. We should rule out as many possible locations as we can."
        hyf "We will keep Miss Ikezawa's phone here with us. If you find her, please call us on that number and let us know. If you cannot find her in the parking lot either, please return to the gate, and wait for us there."
        na "Sure. See you guys soon."

        show hiroyuki serious_close_ss
        with chchange

        show naomi basic_neutral_ss at offscreenright
        with charamovefastest

        hide naomi
        with None

        "I can hear Naomi's footsteps accelerating and then moving away from us at a rapid pace."
        "Hisao sighs."

        show hisao basic_speak_swt_ss
        with chchange

        hi "I'd be surprised if she's at the gate or in the parking lot. Those areas are probably the most crowded places at the moment. If anything, she'll avoid them."

        show hiroyuki speak_close_ss
        show hisao basic_neutral_swt_ss
        with chchange

        hyf "As her boyfriend, it is probably fair to assume that you know Miss Ikezawa better than anyone else. Perhaps there are some insights into her way of thinking in a situation such as this that you can share with us. They may prove useful."

        show hiroyuki serious_close_ss
        show hisao cross_worry_swt_ss
        with chchange

        hi "If what happened is anywhere near as bad as Naomi said it was, I doubt she's thinking at all. At least not rationally."
        hyf "Certainly she does not act in a completely unpredictable manner whenever she feels seriously distressed?"
        hi "There was a time in class where she just completely froze up. In other cases where she got distressed, she'd usually run off."

        show hiroyuki thinking_close_ss
        with chchange

        hyf "And where would she run off to?"

        show hisao cross_speak_swt_ss
        with chchange

        hi "Preferably her own bedroom because she can lock the door. Otherwise, the room where we usually have lunch or her favorite corner in the library would probably be where she'd go."

        show hiroyuki speak_close_ss
        show hisao basic_neutral_swt_ss
        with chchange

        hyf "In other words, places with a sense of familiarity that are devoid of other people?"

        show hiroyuki serious_close_ss
        show hisao basic_speak_swt_ss
        with chchange

        hi "Yeah, although the familiarity-part probably doesn't apply here."

        show hiroyuki serious_close_ss
        with chchange

        hyf "That leaves us with places where she does not expect other people to find her."

        show hisao basic_worry_swt_ss
        with chchange

        hi "On an unfamiliar campus this big, that could be anywhere..."

        show hiroyuki thinking_close_ss
        with chchange

        hyf "What about restrooms? They would be suitable for hiding."

        show hisao basic_speak_swt_ss
        with chchange

        hi "She doesn't really have the habit of hiding in stalls when she's distressed. Maybe because she's afraid of imposing on others by occupying a stall that others could be using. Or maybe she's afraid of being teased as ‘Hanako the toilet girl’."

        show hiroyuki smileclosed_close_ss
        show hisao basic_neutral_swt_ss
        with chchange

        hyf "Like the bathroom-haunting ghost of the same name from the urban legend?"

        show hiroyuki serious_close_ss
        show hisao basic_neutral_swt_ss
        with chchange

        hi "Yeah... Though maybe the restrooms are worth checking anyway just to be sure. Just to rule them out."

        show hiroyuki thinking_close_ss
        with chchange

        hyf "It would be improper for either of us to do that checking, so Miss Inoue and Lilly will have to take that upon themselves."
        "I nod."
        li "We will if it comes to that."

        show hiroyuki stern_close_ss
        show hisao basic_worry_swt_ss
        with chchange

        hyf "It might. We are nearing the gate, and Miss Inoue is waiting for us over there. Miss Ikezawa is nowhere to be seen."
        "So we'll be searching the campus for Hanako after all. God, I hope she's alright."

        scene bg kasshoku_entrance_ss
        show crowd_ss
        show hiroyuki stern_close_ss at center
        show hisao cross_worry_swt_close_ss at left
        with locationchange

        show naomi basic_neutral_close_ss at right
        with charaenter

        "As we finally reach the campus' entrance gate, Hisao steps forward."
        hi "No sign of her in the parking lot?"

        show naomi basic_concern_close_ss
        with chchange

        "I hear Naomi letting out a depressed sigh."
        na "No. Haven't seen her near here, either."
        na "So... Now what? Search every square meter of the entire campus with just the four of us?"

        show hiroyuki thinking_close_ss
        show hisao basic_neutral_swt_close_ss
        show naomi basic_neutral_close_ss
        with chchange

        hyf "I would like to suggest a more refined approach. Can I ask you a question, Miss Inoue?"
        na "Uhuh?"

        show hiroyuki speak_close_ss
        show hisao cross_neutral_swt_close_ss
        with chchange

        hyf "Did you chase after Miss Ikezawa immediately after she fled from the lecture hall? Did you see in which direction she ran off to?"

        show hiroyuki serious_close_ss
        show naomi basic_serious_close_ss
        with chchange

        na "Sorry. She left all her things at her seat when she bolted from the room, and it took me precious seconds to gather them. Didn't want to leave them in that hall. When I made it out of there, she was already gone."

        show hiroyuki speak_close_ss
        show naomi basic_neutral_close_ss
        show hisao basic_neutral_swt_close_ss
        with chchange

        hyf "I would like you and Lilly to check all restrooms at the journalism faculty. If she is still in the building, it is likely she will be hiding in one of them."
        hyf "If you find her, please notify us at once and do whatever you can to put her at ease. If you cannot find her in the faculty building, please return to the gate and wait there."

        show hiroyuki serious_close_ss
        show naomi basic_confused_close_ss
        with chchange

        na "Well... Okay."
        hyf "Mister Nakai, you would not happen to have a photo of Miss Ikezawa in your wallet, would you?"

        show naomi basic_neutral_close_ss
        show hisao cross_frown_swt_close_ss
        with chchange

        hi "I do, but... We're not going to walk around showing random people her picture, are we? Hanako would hate that. She's extremely sensitive about her appearance."

        show hiroyuki thinkraised_close_ss
        show hisao basic_neutral_swt_close_ss
        with chchange

        hyf "Not random people. A campus this large usually has some security staff on duty, especially during an event such as this one. We will ask at the journalism faculty where their office is located and ask them to assist us in a search of the campus."
        hyf "Maybe a description of her will suffice, and they will not even ask us for a photo."

        show hiroyuki thinking_close_ss
        show hisao basic_worry_swt_close_ss
        with chchange

        hi "Asking security guards to go and look for her...?"
        "Hisao doesn't sound completely convinced yet."
        hyf "Yes. They know this place much better than we do and can conduct a search with a much greater degree of efficiency."

        show hiroyuki serious_close_ss
        show hisao basic_speak_swt_close_ss
        with chchange

        hi "If a stranger approaches her, she'll certainly just run off again. And then what?"

        show hiroyuki thinking_close_ss
        show hisao basic_neutral_swt_close_ss
        with chchange

        hyf "Then we will ask them to keep their distance and merely notify us of her location without approaching her."
        "Naomi grumbles softly."

        show naomi basic_concern_close_ss
        show hisao basic_worry_swt_close_ss
        with chchange

        na "This is kinda starting to sound like a manhunt."

        show hiroyuki stern_close_ss
        with chchange

        hyf "We have less than two hours before it will be completely dark outside. I believe it is important that we find her quickly."
        "I give a determined nod."
        li "I agree with Father. If this helps us find Hanako before it gets dark, we should consider it."

        show hiroyuki serious_close_ss
        show hisao cross_speak_swt_close_ss
        show naomi basic_neutral_close_ss
        with chchange

        hi "So... Will the two of us be heading to wherever the security staff is located?"

        show hiroyuki thinkraised_close_ss
        show hisao cross_worry_swt_close_ss
        with chchange

        hyf "Yes. If Miss Ikezawa is found and still in a state of distress, you will probably be the person most suitable to calm her down."
        hi "I just hope they'll take us seriously when I tell them we need help in finding a lost 18-year old girl."

        show hiroyuki speak_close_ss
        show hisao basic_neutral_swt_close_ss
        with chchange

        hyf "I will be happy to take the task of explaining the situation off your hands. I assure you they will not turn us down."
        hyf "Shall we go?"

        show hiroyuki serious_close_ss
        show hisao cross_speak_swt_close_ss
        with chchange

        hi "...Alright."

        stop music fadeout 2.0
        stop ambient fadeout 2.0

        if _in_replay:
            return

    label .s2:

        $ set_window_tint(TINT_LILLY)

        scene bg kasshoku_journalhall
        show naomi basic_neutral at right
        with shorttimeskipsilent

        queue music music_rain fadein 4.0

        na "I just checked, and it looks like one stall's occupied."

        show naomi basic_neutral_close at center
        with characlose

        "I nod and gently grab Naomi's sleeve so she can lead me into the restroom. This'll be the third restroom on the ground floor we'll be searching."

        scene bg kasshoku_restroom
        show naomi basic_neutral_close at right
        with locationchange

        "We enter, and Naomi carefully positions me near the door of the locked stall."
        "I manage to concentrate enough to pick up the faint sound of breathing on the other side of the door. I take a deep breath and softly call out Hanako's name."
        li "Hanako... Are you there?"
        "No reply."
        li "Hanako?"
        "I listen closely once again, but I fail to notice any changes in the breathing on the other side of the door. If Hanako had been here, I'm pretty sure I would have picked up a gasp or an acceleration in the breathing pattern."

        show naomi basic_concern_close
        with chchange

        "Sensing that Naomi's eyeing me, I shake my head and extend my hand. I feel how she puts my hand on her arm, and we slowly walk back out."

        scene bg kasshoku_journalhall:
            align (0.5, 0.5) zoom 1.03
        show naomi basic_concern_close
        with locationchange

        na "Nothing, huh?"
        li "If it had been her, I'm sure I would have picked up a reaction of some sort."
        na "There's one more restroom on this level. I'm not sure..."

        play ambient sfx_phonering

        show naomi basic_shock
        with Dissolve(0.2)

        na "Whoa!"
        "Naomi gives a cry of surprise and I can feel her flinch as my cell phone suddenly springs to life."
        "I hurriedly take it out of my backpack. I hear Naomi grumble softly."

        show naomi basic_annoyed
        with chchange

        na "I think I've heard enough cell phones for one day."

        stop ambient

        play sound sfx_phonepickup

        show naomi basic_neutral
        with chchange

        li "G-good afternoon. Lilly Satou speaking."

        show hiroyuki speak_phone at phonebox
        with charaenter

        hyf "Lilly."
        li "Yes, Father?"

        show hiroyuki serious_phone
        with chchange

        hyf "We have found a few people who are willing to help us look. I assume you have not run into Miss Ikezawa yet?"
        li "That's a relief. We haven't found any sign of her at the faculty."

        show hiroyuki thinking_phone
        with chchange

        hyf "If I were Miss Ikezawa, I would try to get out of the building if there were no obvious safe places in the direct vicinity. It is unlikely for her to have tried and hide on one of the higher floors."
        "That's probably what Naomi was about to say too."
        li "I think so too. She'd try to make it outside, but the entrance gate might have been too crowded for her to approach."

        show hiroyuki awkward_phone
        with chchange

        hyf "Could you put Miss Inoue on the phone for just a second?"
        li "Of course."

        show naomi basic_neutral_close:
            ypos 1.03
        with characlose

        "I hand my phone over to Naomi and lean in close so I can still hear Father's voice."
        na "Yes?"

        show hiroyuki speak_phone
        with chchange

        hyf "Miss Inoue, our search will have the journalism faculty as its starting point and spread out from there. Did you and Miss Ikezawa head straight from the gate to the faculty building this morning or did you go anywhere else?"

        show hiroyuki serious_phone
        with chchange

        na "No. We figured we'd have time to explore the campus for a bit afterwards. We didn't want to be late."

        show hiroyuki thinking_phone
        with chchange

        hyf "How about during lunch? The cafeteria at the English faculty was rather crowded, and perhaps the same was true here. Did you and Miss Ikezawa..."

        play sound sfx_impact2

        show naomi basic_shock_close
        show hiroyuki scold_phone
        with vpunch

        na "THE SPORTS FIELD!{fast}"

        pause 0.3

        show hiroyuki speak_phone
        with chchange

        "My ears ring as Naomi unexpectedly shouts into my phone."

        show naomi basic_serious_close
        with chchange

        na "Hanako wanted to avoid the crowds at the cafeteria, so we went out and had lunch in quiet spot near the running track some distance away from the faculty building! We ate at a bench in sight of the bleachers!"

        show hiroyuki smile_phone
        with chchange

        hyf "Good call, Miss Inoue. Are there any other places outside of the faculty that you have visited today?"
        na "No, but I have a hunch that she is where we had our lunch break. Maybe we should go over there too."

        show hiroyuki thinking_phone
        with chchange

        hyf "The security staff will likely be there before you, so it is probably better for the two of you to finish your search in your current location and then head back to the gate as we agreed."

        show naomi basic_neutral_close
        with chchange

        na "...Okay then."

        show hiroyuki smileclosed_phone
        with chchange

        hyf "Good. We will hopefully see you soon."

        hide hiroyuki
        with charaexit

        "I hear a short beep as Father hangs up the phone. Naomi puts the phone back into my hand."

        show naomi basic_concern_close
        with chchange

        na "I've been an idiot for not thinking of that place sooner. Let's hope she's there. She has to be there."
        li "I hope so too."

        show naomi basic_neutral_close
        with chchange

        na "Wanna go back to the gate?"
        li "Let's stop by the remaining restroom and then go back."
        na "Right."

        stop music fadeout 2.0

        scene bg kasshoku_entrance_ss
        show naomi basic_neutral_close_ss at center
        with shorttimeskipsilent

        queue music music_night fadein 4.0

        "Our search of the journalism faculty having returned no results, Naomi and I return to the gate and sit down on one of the benches."
        "The walking across the campus has left me tired, but my mind feels even more exausted than my body. The temperature today wasn't that bad for a day in November, but now that the afternoon is coming to an end, it's rapidly getting colder, and I shiver despite my fairly thick coat."
        na "It's getting kinda chilly, isn't it?"
        "I nod at Naomi but don't reply."

        show naomi basic_serious_close_ss
        with chchange

        na "I really hope she's at the sports field. The sun is already starting to set..."
        "What if she isn't there? What if we can't find her, and it gets dark? Is she going to seek shelter eventually? What if she stays out here all night and gets hypothermia?"
        "What if... No, don't think like this. Don't even start thinking like this."
        "She'll be fine. Please let her be fine."

        show naomi basic_concern_close_ss
        with chchange

        na "Erm..."
        "I sigh and rub my temples. This wasn't so bad while we were busy walking around the faculty building, but now that we're just sitting and waiting, I have nothing to do except be worried sick about Hanako."
        na "Hey, you alright?"
        li "I'm okay."
        na "I... uh... just wanted to say... uh..."
        "I hear her shuffle on the bench a bit."
        na "Sorry about shouting before. You were right. I wasn't being fair. I was taking my stress out on you. We could have phoned you during lunch break that our program ended at four. We just didn't think of it. We thought we'd be able to make it in time."
        "I never really held Naomi's angry outburst against her. She's probably as worried about Hanako as I am. Still, I appreciate her gesture."
        li "No, you were right to be angry. I... really did... mess up. I... put Hanako through something horrible and I... I'll take full responsibility for that."

        show naomi basic_serious_close_ss
        with chchange

        na "I messed up too. I should have tried staying closer to her. I should have reacted sooner when that phone started ringing. Hanako never even really wanted to attend that last lecture to begin with. She simply did it to accommodate me, I think."
        na "I should have done as she said and skipped the damn thing."

        show naomi basic_annoyed_close_ss
        with chchange

        na "I should have taken the hint when we entered that hall, and I saw that look on her face instead of listening to a reassurance that wasn't even remotely convincing. And I couldn't even follow her quickly enough to find out where the hell she went."

        show naomi basic_angry_close_ss
        with chchange

        na "Urg... And I could hear some assholes softly laughing at the whole thing. If I had known running after Hanako was useless, I would have stayed and given them a few pokes with my injection pen. I have a really funny anticonvulsant in there. Give 'em something to laugh about."
        li "I occasionally laugh when I'm nervous or uncomfortable. Perhaps the same was true for them."

        show naomi basic_concern_close_ss
        with chchange

        na "Whatever. The gist of it is that I screwed up just as badly, if not more. Hanako's probably sorry she asked me to come along."
        "That's news to me. I was under the assumption that Hanako simply spoke to Naomi about today during their outing last Friday and that Naomi invited herself along."
        li "She asked you to come along?"

        show naomi basic_serious_close_ss
        with chchange

        na "Yeah, I don't think I would have attended today's events otherwise. I don't like travelling on my own."
        na "I guess... she was hoping things would be less stressful for her with someone else around. So much for that assumption."
        li "I... am still happy you came along. I didn't want to offend Hanako by worrying about her. She has made some truly remarkable progress over the last few months, after all."
        li "But still, someone else coming along so she wouldn't attend today's events all on her own was a relief, and I think Hanako really appreciated it."

        show naomi basic_neutral_close_ss
        with chchange

        na "I guess so... At least, before I screwed up."
        li "I don't think you did anything wrong by wanting to attend the full program. That's what we came here for, after all."

        show naomi basic_sheepish_close_ss
        with chchange

        na "Yeah... So erm... No hard feelings?"
        li "No hard feelings."
        "At least on my part. I'm not sure how Hanako will look back on this."
        "Will she resent us for the part we played in this?{w} No, that's very unlikely. But..."

        show naomi bend_wink_close_ss
        with chchange

        na "You know, ever since I met your really awesome mom, I've been wondering what kind of person she'd be married to."
        na "When I met your dad this morning, I was... I dunno... Maybe a little underwhelmed. I expected him to be more like her."

        show naomi bend_smile_close_ss
        with chchange

        na "But seeing how quickly he jumped in to get this mess under control, maybe there's more to him than meets the eye."

        nvl clear
        nvl show dissolve

        n "Despite the current situation, I manage to let out a proud little smile. I too have been relieved and pleasantly surprised by Father helping us out like this."
        n "{vspace=30}He's been struggling—emotionally more than physically—ever since he lost his status as CEO and position as head of the Satou clan. Even though he's still officially a board member, Akira mentioned to me that in practice, that didn't really mean much since the other three members were many years his senior, and because of that, each of them had much more clout than he did."
        n "He is happy to be back in his homeland, but at the same time, Mother says that he feels being watched whenever he goes outside for a walk during the weekdays. As a result, he spends most of his time indoors, sleeping in bed or reading in his study. Whenever he goes outside, he drives his car to a part of town where people don't know him and takes a walk there or visits a library."
        n "Mother assured him that she didn't think less of him now, and neither did she care what others might think of him. But I'm not sure if her reassurance has made a large difference. Ironically enough, today was supposed to be an inspirational event for him as well. This day may actually have been a success for him from that point of view."

        nvl hide dissolve

        li "I'm certainly glad that he's here right now and that it's not just the three of us."

        show naomi basic_smile_close_ss
        with chchange

        na "Heh, speak of the devil... I think I see him coming back. At least I think it's him."
        li "What about Hisao? And Hanako?"

        show naomi basic_ponder_close_ss
        with chchange

        na "No, it's just him. I hope he hasn't lost sight of Nakai."
        li "No, I don't think that's what happened."
        "I'm pretty sure he would have called me if they got separated for some reason."

        show naomi basic_serious_close_ss
        with chchange

        na "Gee, he looks a little winded. I guess we'd better give him some room to take a load off."

        show naomi basic_neutral_close
        with chchange

        show naomi at right
        with charamove

        show hiroyuki serious_close_ss at twoleft
        with charaenter

        "We both move to the outside of the bench a bit so Father will have room to sit down in between us."
        hyf "Lilly... Miss Inoue."
        li "Father, are you alright?"

        show hiroyuki thinking_close_ss
        with chchange

        hyf "Quite well, thank you."
        "I notice that his breathing is slightly quicker and more uneven than usual, but probably not to a degree that justifies worrying about him."
        li "Father... Hanako, did you...?"

        $ _sh_music_pos = renpy.music.get_pos()

        stop music fadeout 1.0

        show hiroyuki speak_close_ss
        with chchange

        hyf "We have managed to... locate Miss Ikezawa."

        show naomi basic_sheepish_close_ss
        with chchange

        "I breathe a sigh of relief and hear Naomi do the same."
        li "Thank God."
        na "Was she there? Where I said she'd be?"

        play music f"<from {_sh_music_pos}>{music_night}" fadein 4.0

        hyf "Yes and no. She was not at the bench you mentioned to us, but they did an extensive search of that particular area and found her hiding behind the small building near the bleachers that houses the distribution substation powering the floodlights."
        hyf "Mister Nakai is currently keeping her company."

        show hiroyuki serious_close_ss
        show naomi basic_neutral_close_ss
        with chchange

        na "So... Now what?"

        show hiroyuki thinking_close_ss
        with chchange

        hyf "Now we wait until she is ready to leave. We may have to wait until it is dark and there are no more people walking around the campus."
        na "Okay..."

        show hiroyuki serious_close_ss
        with chchange

        hyf "You can wait in the car if you like, Lilly. There is a bit of a chilly wind blowing here."
        li "I don't mind waiting here."

        show hiroyuki eyebrow_close_ss
        with chchange

        hyf "Are you not cold?"
        li "..."
        "It is chilly out here, but I'm not going to take shelter in the car as long as Hanako is still out there in the cold."

        show hiroyuki thinking_close_ss
        with chchange

        "Father lets out an exasperated sigh at my lack of reaction."
        hyf "Perhaps the two of you are willing to do me a favor?"
        li "A favor?"

        show hiroyuki speak_close_ss
        with chchange

        hyf "The original plan was to stop by a restaurant somewhere on our way back and treat the four of you to dinner. With things as they currently are, I believe it to be best if we head straight back to Yamaku when Miss Ikezawa returns."
        li "I believe so too."

        show hiroyuki smileclosed_close_ss
        with chchange

        hyf "Good. Since it might be rather late before we are back, it would be a good idea to purchase some food in one of the cafeterias here to eat during the trip back. It does not have to be a 4-star meal, but it should get us back to Yamaku without going hungry."
        "I turn to Naomi."
        li "Would you please come along and get some food with me?"

        show naomi bend_smile_close_ss
        with chchange

        na "Sure."

        show naomi basic_smile_close_ss at right
        show hiroyuki thinking_close_ss
        with chchange

        hyf "Hold out your hand, please."

        show hiroyuki speak_close_ss
        with chchange

        "I do so and feel several banknotes being pressed into my hand."
        hyf "Please be sure to buy something that can be eaten on the road with a minimum of fuss and preferably something that does not need to be warm to taste good."
        li "Of course, Father."

        stop music fadeout 2.0

        if _in_replay:
            return

    label .s3:

        $ set_window_tint(TINT_LILLY)

        scene bg kasshoku_grounds2_ni
        show naomi basic_sheepish_close_ni at tworight
        with shorttimeskip

        play music music_night fadein 4.0

        na "You think we have enough riceballs?"
        li "Yes. Between them and the sandwiches, we should be well stocked for the trip back to Yamaku."

        nvl clear
        nvl show dissolve

        n "Fortunately for us, the cafeteria in the nearest faculty building was still open, so Naomi and I took the opportunity to buy a bag full of snacks. Now we're simply hanging around near the building's entrance."
        n "Father said that he'd call me if he received word from Hisao that he and Hanako are on their way, so there's little for us to do right now."
        n "{vspace=60}I wish there were other ways to keep busy right now, because I could really, really use the distraction, but I just know I won't be able to put my mind to studying right now, so there's no point in taking out one of my study books."

        nvl hide dissolve

        show naomi basic_neutral_close_ni
        with chchange

        na "Hey Lilly... I mean, Satou?"
        li "Lilly is fine."
        na "Ah... Can I ask you something?"
        "I turn towards Naomi who's sitting next to me. She's been unusually quiet over the last ten minutes or so."
        li "What would you like to know?"
        na "If you had been in my place... What would you have done?"
        li "I don't understand."

        show naomi basic_concern_close_ni
        with chchange

        na "Imagine you'd ask any of my classmates what would be most likely to end in disaster: sending me into a nightclub full of strobe lights, or sending Hanako into a lecture hall full of people. Everybody would agree on the latter without question."
        na "I mean... She used to break down and run out when one or two people were eyeing her for too long in class. I kinda feel like I really should have known better."
        li "I don't think you necessarily did anything wrong."

        show naomi basic_serious_close_ni
        with chchange

        na "You don't think I necessarily did anything wrong?"
        li "Hanako may have been reluctant to follow you into that hall, but she still did so of her own free will. Maybe you overestimated her this time, but it's probably still better than if you had done the opposite."
        li "Hanako often worries that others look down on her, and being overprotective of her merely confirms her anxieties about that."
        "I found that out the hard way myself. From the way Naomi seems to interact with Hanako, she doesn't run much risk of Hanako jumping to those particular conclusions about her."

        show naomi basic_ponder_close_ni
        with chchange

        na "I never really thought about that much..."
        li "I think your friendship has helped Hanako grow a lot over the last four months. I never imagined she'd do things like join a club, hold writing sessions in her room with others, interview teachers, or go out with clubmates. You're probably the first friend she's had who challenges her like that."

        show naomi bend_grinclosed_close_ni
        with chchange

        na "Heh, says the person who convinced Hanako to accompany her to the other side of the world?"
        li "Aside from that, I think my friendship mostly consisted of offering her comfort and company."

        show naomi bend_smile_close_ni
        with chchange

        na "She didn't really have any of that at the time you two met, so I think those are still really important to her. I think she was more willing to move beyond her comfort zone later on exactly because she knew she'd always have you to fall back on."
        li "...Maybe."

        show naomi basic_ponder_close_ni
        with chchange

        na "I've always wondered a little bit why they didn't put Hanako in your class to begin with. The two of you might have met sooner, and maybe she'd have made some more friends sooner too."

        show naomi basic_neutral_close_ni
        with chchange

        li "If the school had done that, it might have backfired. Hanako might have interpreted it as a sign that they wanted to spare the rest of the student body the sight of her scars."
        li "Besides, not all of the students in my class are completely blind, and even those who completely lack eyesight know what most of their classmates look like. Hanako's scars wouldn't have remained hidden for very long."

        show naomi basic_serious_close_ni
        with chchange

        na "Oh... okay."
        li "I also think that the school believed it to be best for her self esteem if she made some friends in class who could see her scars and still wanted to spend time with her. People who were willing to give her a chance to make a new start."

        show naomi basic_annoyed_close_ni
        with chchange

        "I hear Naomi snorting softly."
        na "You sure make it sound easy. Do you really think people didn't try?"
        li "I didn't mean to imply that."
        na "Because people tried. A lot of people tried. I tried. Natsume tried. Hakamichi and Mikado tried. Even Kawana, Suzuki, and Kapur tried. It just didn't work."
        "I've never had that much contact with the students of Shizune's class, so some of the names Naomi brings up barely ring a bell."
        "I don't really know much about Hanako's time in class before the two of us met. By the time I befriended Hanako, my relationship with Shizune was already turning sour so I couldn't ask her."
        "I wonder about Naomi's perspective on all of this..."
        li "How did the class see Hanako?"

        show naomi basic_serious_close_ni
        with chchange

        na "Most of us got to know the rest through the introduction activities the first week, but Hanako skipped all of those. When she first appeared in class, people were curious about her."
        na "But when we approached her, she just panicked, ran off, and didn't return for the rest of the day. We never really learned much about her, but some things started falling into place eventually."
        li "Falling into place?"

        show naomi basic_concern_close_ni
        with chchange

        na "She had this habit of arriving late or leaving early. Sometimes even skipping class altogether or randomly walking out. The teachers ignored it every single time. Hakamichi asked about it once and was told that every student has special needs."
        na "So we figured that there was some kind of arrangement with the school in place, meaning that the real reason she was attending here probably had more to do with her behavior than with her scars needing constant medical attention. Eventually words like ‘trauma case’ started being dropped."
        "Trauma case. I cringe visibly at the harsh ring of that description of Hanako."
        li "Hanako's had a very difficult life prior to her arrival at Yamaku."

        show naomi basic_serious_close_ni
        with chchange

        na "Yeah, that was kind of obvious from the start. There are many people in school who can attest that being maimed in an accident can really do a number on you."
        na "And I know all too well that others aren't always accommodating or even understanding of your circumstances. Heck, there were several people at my middle school who thought I was a freak. So most people in class tried not to hold her behavior against her."
        na "But... other than not rocking the boat, there wasn't really much else we could do."
        li "Not rocking the boat?"

        show naomi basic_concern_close_ni
        with chchange

        na "If you tried holding an actual conversation with her, she'd often clam up or sometimes even run off. So best thing to do was only have some limited interaction with her if absolutely necessary and otherwise pretend she wasn't there."
        na "I really didn't like it either, but as long as people didn't interact with her, she at least came to class on a regular basis. Nobody wanted to be responsible for her getting low grades. I mean, you could tell she had enough problems as things were."
        li "How depressing..."

        show naomi basic_sheepish_close_ni
        with chchange

        na "I don't think people cared that much about what she looked like. We're all in the same boat after all."
        na "Heck, in my opinion she's easier on the eyes than many of the boys attending our school. And if you spend some time really interacting with her, you kind of stop paying attention to the burns."

        show naomi basic_neutral_close_ni
        with chchange

        na "But she wasn't exactly generous with the opportunities for interaction, even after she met and befriended you."
        "I suppose my friendship didn't really do much to take away Hanako's conviction that people saw her as inferior because of her scars. I wonder if perhaps I should have done more to encourage Hanako to have contact with others as well."
        li "Everybody has their own pace."

        show naomi basic_smileclosed_close_ni
        with chchange

        "This causes Naomi to chuckle briefly."
        na "It sure is an uneven pace though. For over two years, she's like a ghost who's present but doesn't interact with the rest in any way."
        na "Then some random new guy transfers in and BOOM... everything changes."
        na "Heh, not that I'm complaining. I got a new friend out of it, after all."
        li "You two are certainly an interesting combination."

        show naomi basic_grin_close_ni
        with chchange

        na "I hear that all the time, but we actually work together very well. I'm good at talking, and she's good at listening. That's actually often a pretty good combination."
        na "At the writing club, I'm usually the one to throw the ideas around, and she usually writes them down, develops them, and fills in the blanks."

        show naomi basic_laugh_close_ni
        with chchange

        na "We recently followed your mom's advice and did a joint interview with one of the teachers for that club column with me asking the questions and keeping the teacher talking and Hanako observing and taking notes."
        na "As long as the attention isn't squarely focused on her, she's really good at that. She has a knack for reading between the lines and filling in the blanks."
        "That is certainly true, although the same tendency can be a double-edged sword as it has caused Hanako to jump to the wrong conclusions about people in the past due to her low self esteem coloring her vision."
        li "It's good to hear that the two of you work together so well. She seems to enjoy spending time with you, so I assume that there's a personal click as well."

        show naomi basic_sheepish_close_ni
        with chchange

        na "In a way. She's still not exactly open with me, and when we interact, it's mostly me talking and her listening. We usually keep to the safe subjects like the clubs, and I like to share new gossip with her since she's not very likely to repeat it to other people."

        show naomi bend_grin_close_ni
        with chchange

        na "Jun and I are still trying to convince her that being in a relationship doesn’t mean she can’t participate in our discussions about boys. Still, I'm happy we finally got to know each other a bit."

        show naomi bend_smile_close_ni
        with chchange

        na "I've been noticing things about her since she joined our club. Like her approaching Mutou and doing an interview so her boyfriend's club can get some new members."
        na "Or taking your mom to our club to give a motivational speech. Or letting me sleep in her room whenever I have an episode. Or her and Jun keeping me company the day after while I'm bedridden."
        na "The girl obviously has a big heart underneath that shy exterior of hers, and it's only fair I make an effort to be a friend to her because I honestly believe she deserves more of them."
        "Despite the gravity of the current situation, Naomi's words make me smile."
        li "I couldn't agree more on that."

        show naomi basic_smile_close_ni
        with chchange

        "A silence..."
        "Seems like we're running out of things to say. Maybe we should return to the campus entrance. Father must be wondering what's taking us so long."
        li "Shall we go back to the gate? I don't want Father to get worried."

        show naomi basic_neutral_close_ni
        with chchange

        na "Fine with me. It's already getting pretty dark, so hopefully we won't have to wait too long for Hanako to make her way back to us."

        scene black
        with locationchange

        "We get up and walk back to where we left Father with me once again holding onto Naomi's sleeve for navigation."
        "Just when we get close to where I think the bench where we were sitting before is located, Naomi suddenly stops."
        li "Is something wrong? Is Father still sitting there?"
        na "He's standing at the entrance gate, and he's beckoning us. I wonder if he's heard something already."

        scene bg kasshoku_entrance_ni
        show hiroyuki speak_ni at twoleft
        with locationchange

        show naomi basic_neutral_close_ni at right
        with charaenter

        "We quickly make our way over to where Father is waiting for us."
        hyf "Lilly. Miss Inoue. Well timed. I was about to drop the two of you a call."
        li "Father. Have you heard from Hisao already?"

        show hiroyuki thinking_close_ni
        with characlose

        hyf "I have. He and Miss Ikezawa are on their way over here."

        show naomi basic_smile_close_ni
        with chchange

        hyf "I am heading for the car in order to park it as close to the entrance as I can. I believe it to be best if the two of you join me."
        li "We will."

        # TODO replace with bg of campus parking lot

        scene black
        with locationchange

        "I feel a sense of relief as we follow Father to the car. With luck, Hanako and Hisao will soon be with us."
        "I'm not sure what I could possibly say to Hanako to properly apologize to her. It's probably best to first find out how she feels before I start trying to make this up to her."
        li "Father... Did Hisao say how Hanako is doing?"
        hyf "I am afraid he did not. Let us worry about that later."

        scene bg misc_hiroyukicar_ni at center
        show carseats
        show naomi basic_neutral_close at right
        with locationchange

        "We get into the car, and Father drives it up to the entrance gate. I get the impression that the parking lot is almost completely empty already, for Father is able to return us to the school gate while barely having to make any turns."

        show naomi basic_shock_close
        with chchange

        stop music fadeout 1.0

        "A few minutes of silence later, I hear Naomi let out a soft cry."

        show naomi basic_concern_close
        with chchange

        na "There they are. Over there. In the distance."
        hyf "Yes, they have finally made it here."
        li "Can you see how Hanako is doing?"

        play music music_moonlight fadein 4.0

        "No immediate reply. But then I hear a barely audible “geez...” from Naomi that makes my heart immediately skip a beat."
        li "Naomi? What's wrong? What do you see?"

        show naomi basic_serious_close
        with chchange

        na "Erm..."
        "Naomi starts mumbling something but is then interrupted by a short cough coming from my right."
        hyf "Inoue, could you please assist Mister Nakai?"
        na "Uh... Sure."

        # TODO play car door open sfx

        show bg:
            ease 1.0 top
        show naomi at sh_fadebottomexit
        show carseats at sh_fadebottomexit

        pause 1.0

        hide naomi
        hide carseats

        show hiroyuki serious_close at right
        with charaenter

        "I hear the car door opening, and I'm gripped by a sudden sense of frustration as I realize I'm being left out."
        "What was it that Naomi was about to say? Does Father really think he's doing me a favor this way?"
        na "Hey... Are you okay, Hanako? You're not... hurting, are you? That looks..."
        ha "..."
        "But my irritation quickly vanishes as I hear the worried tone in Naomi's voice."
        hi "Naomi, could you take my backpack from me?"
        na "Y-yeah sure."
        "I hear shuffling on the rear seats and eventually I hear the car door slam shut."
        "As it does, seat belts start clicking shut and Father starts the engine."

        show hiroyuki thinking_close
        with chchange

        hyf "Now that we are all here, it is time to return to Yamaku."
        na "Hey, the two of us just did a little shopping, and we got stuff to eat on our way back. Hope you guys don't mind sandwiches and riceballs."

        show hiroyuki serious_close
        with chchange

        hi "That sounds good. I'm kinda hungry. Wanna have one as well, Hanako?"
        ha "..."
        "When Naomi first spotted Hanako and Hisao, I was relieved. But that relief is quickly starting to turn into concern as Hanako barely seems to be responding to us."

        hide hiroyuki
        with charaexit

        "As Father steers the car off the parking lot, I gather all my courage, turn around, and whisper to my best friend."
        li "Hanako?"

        stop music fadeout 1.0

        "There is no response."

        stop music fadeout 2.0

        if _in_replay:
            return

    label .s4:

        $ set_window_tint(TINT_LILLY)

        scene bg suburb_shanghaiint
        show hiroyuki thinking_close at centersit:
            xpos 0.45
        show hisao basic_worry_swt_close at leftsit
        show naomi basic_concern_close at rightsit
        with Fade(1.0, 1.0, 1.0)

        play music music_moonlight fadein 4.0

        "The food at the Shanghai was good as usual, but the atmosphere has been gloomy."
        "We went here to get a quick meal after dropping Hanako off at the dorm, and now I can hear Hisao and Naomi getting up."

        show naomi basic_concern at right
        show hisao basic_sweet_swt at left
        with charadistant

        hi "Mister Satou, thank you for the meal. I hope you don't mind if I leave already."

        show naomi basic_sheepish
        with chchange

        na "I think I'm going too. Thanks for everything. And say hello to your wife for me."

        show hiroyuki eyebrow_close
        with chchange

        hyf "Are you sure you do not want me to drive you back to school? It is still quite the walk uphill from here."
        hi "That's okay. We walk that road all the time during the week and usually with shopping bags to boot. Besides, some fresh night air will probably feel good right now."
        hi "You and Lilly surely like to have a little bit of time for yourself, too."

        show hiroyuki smileclosed_close
        with chchange

        hyf "In that case, I wish the two of you a safe return and a good night."
        "I turn my head towards Hisao and do my best to give him my most reassuring smile."
        li "Try not to worry too much about Hanako, okay? I'm sure she'll be fine once she has recovered a bit."
        "A short pause."
        hi "...The same goes for you Lilly."
        li "I will try to keep that in mind."

        hide hisao
        hide naomi
        with charaexit

        "Hisao and Naomi say their goodbyes, and I hear them leave the room."
        "After the sound of their footsteps has faded away, Father softly clears his throat."

        show hiroyuki awkward
        with chchange

        hyf "Perhaps some fresh air will do us good as well. Unless you are still hungry."
        "I softly nod my head."

        show hiroyuki at center:
            xpos 0.45
        with { "master": charamove }

        "Father walks up to the counter, pays our bill, and we walk out."

        scene bg suburb_shanghaiext_ni
        show hiroyuki awkward_ni
        with locationchange

        hyf "I am afraid that I am not very familiar with this town."
        li "I know of a place that's probably nice and quiet right now. It's not very far from here."

        show hiroyuki smileclosed_ni
        with chchange

        hyf "Lead the way then."

        scene bg suburb_park_ni
        show hiroyuki thinking_ni at tworight
        with locationchange

        li "Here it is. It sounds quiet enough right now, and I think this area of the park smells nice."

        show hiroyuki thinking_close_ni
        with chchange

        "I sit down on the nearby park bench and hear Father taking a seat next to me."
        hyf "The odor is a bit hard for me to judge, but I can attest that it is quiet around here. There is not another person in sight."
        hyf "It is a nice place, although I would probably be able to appreciate the area more during the daytime."

        stop music fadeout 2.0

        li "This is a bit of a special place. This is the place where... H-Hanako and Hisao... c-confessed to one another."

        play music music_sadness fadein 4.0

        "My voice starts breaking as Hanako's name leaves my lips."
        "I thought I'd be relieved when Hisao and Hanako made it back to us. I was hoping Hanako'd be okay after Hisao calmed her down."
        "But when Hanako finally returned, it became obvious almost immediately that she was far from okay."

        show bg misc_hiroyukicar_ni at sepia
        hide hiroyuki
        with { "master": locationchange }

        "She must have been hungry as well, but despite several offers, she hasn't taken a single bite. Nor has she spoken a single word during the whole journey back."

        show bg school_girlsdormhall at sepia
        with { "master": locationchange }

        "Only when we arrived back at Yamaku and she was about to enter her room, she turned to us and said four barely audible words."

        show hanako dulleyed at center, sepia
        with charaenter

        show hanako at tworight
        with charamove

        pause 0.5

        show hanako at right
        with charamove

        ha "{size=*0.7}I will be fine.{/size}"

        pause 0.5

        show hanako at offscreenright
        with charamove

        hide hanako
        with charaexit

        "Nobody believed it."

        show bg suburb_shanghaiint at sepia
        with { "master": locationchange }

        "The atmosphere at the Shanghai was quite heavy because of it with even Naomi barely saying anything."
        "And throughout it all, I've been struggling to maintain a reassuring and composed smile in front of the others."
        "Eventually, my jaw started hurting and my head started pounding, so I was relieved to finally get out of there."

        scene bg suburb_park_ni
        show hiroyuki awkward_close_ni at tworight
        with locationchange

        "And now, with nobody but Father nearby, I hold my head in my hands and let my shoulders slump, trying to keep my tears in check."
        li "What have I done?"

        show hiroyuki thinking_close_ni
        with chchange

        hyf "You have merely made a small mistake with large consequences, just like the others."
        li "The others?"

        show hiroyuki thinkraised_close_ni
        with chchange

        hyf "Miss Inoue made the mistake of having Miss Ikezawa accompany her to that lecture and not staying close to her."
        hyf "Miss Ikezawa herself made the mistake of not turning off her phone."
        hyf "And you made the mistake of phoning her without considering the possibility of them still attending a session."
        hyf "If any of you three had acted differently, what happened today would not have happened."
        li "Even so..."

        show hiroyuki serious_close_ni
        with chchange

        hyf "Try not to take all responsibility for today on your own shoulders. Put some of it on mine if you like."
        li "Yours?"

        show hiroyuki stern_close_ni
        with chchange

        hyf "You seemed rather insistent on taking a break at the English faculty this afternoon rather than heading straight back to the campus entrance. You did not appear to be very tired yourself, so I am curious for whose benefit that was."
        li "I was..."
        "I start to speak, but then think better of it. I don't have any energy left to put on a convincing act, and I suspect that Father has already found me out anyway."
        li "I'm sorry, Father."

        show hiroyuki thinking_close_ni
        with chchange

        hyf "There is nothing wrong with being protective of others, Lilly. But it is not always a positive trait."
        li "Father..."
        "I suppose he's right. I know that my tendency of being overprotective isn't exactly a virtue. But he hardly set the good example today. I wonder if I should bring it up."
        "I don't feel like it's my place to scold or lecture him. He is my father after all."
        "On the other hand, he probably didn't realize how much he offended me. Maybe I should speak up."
        li "When Hisao and Hanako approached the car a few hours ago, Naomi seemed shocked by something, but she didn't say what it was."

        show hiroyuki serious_close_ni
        with chchange

        li "I had the impression that you... discouraged her... from sharing her impression with me."
        li "I would have... really appreciated... being let in on the fact that Hanako injured herself."

        show hiroyuki eyebrow_close_ni
        with chchange

        hyf "How did you find that out?"
        li "I picked up the faint smell of antiseptic in the car while we were driving back. I also paid close attention to the sound of her footsteps, and it sounded like she was limping slightly."

        show hiroyuki thinking_close_ni
        with chchange

        hyf "Impressive."
        li "I probably would have found out eventually. I don't understand what's wrong about having Naomi tell me this immediately."

        show hiroyuki stern_close_ni
        with chchange

        hyf "It is one thing to beat oneself over the head over what happened today, but it is another to ask others to provide you with a cudgel."
        "So he feels that I was burdening Naomi by putting her into the role of bearer of bad news."

        show hiroyuki serious_close_ni
        with chchange

        li "It is more a matter of principle. If I was able to see, I would have been able to see Hanako's situation for myself. But since I lack eyesight, I often rely on others to describe a situation for me, whether it's a good or a bad one."
        li "If others are denied the opportunity to act as my eyes, it feels as if my blindness is being taken advantage of. And that feels... bad to me."

        show hiroyuki thinking_close_ni
        with chchange

        "That's probably as polite as I can phrase it. For nearly a minute, Father doesn't respond."

        show hiroyuki awkwardspeak_close_ni
        with chchange

        "Then he lets out a soft sigh."
        hyf "When Miss Ikezawa was found, she was sitting against the side of the building in what seemed to be a fetal position. We immediately noticed a small hole in her pants near one of the knees and a wound underneath as well as some grazes on her hands."
        hyf "I think it is safe to assume that she tripped during her flight from the building and took a rather nasty fall."
        li "Oh no..."
        hyf "I had the guard who found her go and fetch us a few supplies so Mister Nakai could clean the wounds and put a gauze on her knee. "
        "He sighs softly."

        show hiroyuki awkward_close_ni
        with chchange

        hyf "When we reached the spot where she was hiding, Mister Nakai approached her, sat down next to her, and embraced her. But she just kept staring straight ahead as if he was not even there."
        hyf "I remained with Mister Nakai until the guard came back with the medical supplies. During that whole time, I do not recall her moving even once."
        hyf "It was a very... unsettling sight."
        "I notice that for just a moment his voice trembles slightly."
        "How bad could it have been if even Father was rattled by it? How did this day, that was supposed to be so inspirational, become such a nightmare?"
        "The idea of Hanako sitting there, nearly catatonic and covered in grazes, breaks the last bit of restraint I have left, and tears of grief and guilt start flowing down my cheeks."
        li "Oh, H-Hanako. I'm s-so s-sorry..."
        "I can't recall the last time I've felt this miserable. My mind is swirling with all kinds of emotions—all of them bad."

        show hiroyuki thinking_close_ni
        with chchange

        nvl clear
        nvl show dissolve

        n "I feel anger at myself and at the situation. Hanako's already been through so much. She's already endured enough misery for a lifetime and didn't deserve being put through this."
        n "{vspace=30}I also feel a maddening sense of helplessness and desperation. I'll apologize to her tomorrow, but I know in advance that that's not going to change much. I want to do more, but I can't think of anything."
        n "{vspace=30}And more than anything else, I'm really worried. Hanako was doing so well lately. She still wasn't extremely outgoing, but she was slowly but steadily rediscovering how to enjoy life again after nearly a decade of focusing completely on survival."
        n "{vspace=30}Her grades were steadily climbing, too, and my impression was that she'd easily be able to handle her entrance exams as long as she kept studying hard for it."

        nvl clear

        n "But how much motivation will she have left now?"
        n "Will she have recovered from today's events in time for the mock exams later this week?"
        n "What if she fails them and is forced to take all those extra classes—because of me? What would that do to her?"
        n "What if this has an impact on her performance in the actual exams?"
        n "The national tests are less than two months away. What if she fails her exams?"
        n "What will she do then? Where will she go?"
        n "{vspace=60}No... Don't think like that. Don't even start thinking like that."
        n "Just... keep it together. Stop... worrying... already."

        nvl hide dissolve

        show hiroyuki awkwardspeak_close_ni
        with chchange

        hyf "Lilly?"
        li "I've f-failed her so b-badly. How will I even f-face her after t-today?"
        "I feel embarrassed about Father having to see me like this, but it took all my strength to stay composed in front of Hisao and Naomi, and if I keep this bottled up inside for any longer, I'll probably end up breaking down in the dorms."
        "At least right now there's nobody around but him and me... I think. The only sounds I hear right now are the whistling of the wind through the nearby trees and the sound of my own crying."

        stop music fadeout 2.0

        queue music music_comfort fadein 4.0

        show handkerchief at displayitemshow

        pause 1.0

        show hankerchief at displayitem

        "Just when I start worrying about how extremely uncomfortable this is probably making Father, I feel him take my hand and push something against my palm."
        "As I take it from him, I can feel that it's something light and soft."

        show handkerchief at displayitemhide

        pause 1.0

        hide hankerchief

        show hiroyuki awkward_close_ni
        with chchange

        hyf "It is... ah... a handkerchief to... ah..."
        "Despite my depressed mood, I can't resist a giggle at Father's awkwardness."
        li "I could tell."

        show hiroyuki serious_close_ni
        with chchange

        "Even my gloomy mood cannot prevent a smile from crossing my face for a moment, both at the unexpected sweetness and the endearing awkwardness of his gesture."
        "I use his handkerchief to dry my tears, keeping it with me afterwards in case I tear up again later."
        "As the stream of tears dries up, I let out a loud and tired sigh."
        li "Thank you."

        show hiroyuki thinking_close_ni
        with chchange

        hyf "Think nothing of it."
        li "I'm sorry for you having to see me like this."
        hyf "Not at all. Best to let it out now, so you can be strong and supportive in front of Miss Ikezawa later."
        li "I... would like to do whatever I can to help Hanako, but I'm not really sure what I can do."

        show hiroyuki smileclosed_close_ni
        with chchange

        hyf "I was under the impression that supporting people who are going through a difficult time is like a second nature to you, and that you do not need to go in with a specific plan in mind. All you would need to do would simply be yourself."
        li "Hanako has an appointment with her therapist tomorrow. Knowing her, she might end up skipping it. If she does, maybe I should go. Just to let the school know what happened. Maybe I can ask them to extend Hanako some leniency with the mock exams this week."

        show hiroyuki smile_close_ni
        with chchange

        hyf "That sounds like a good start."
        "I absentmindedly nod my head as Father continues."
        hyf "Perhaps we can buy her a new set of pants to replace the ones that were damaged. I am sure your mother would be happy to obtain some that resemble the ones she was wearing today."

        show hiroyuki smileclosed_close_ni
        with chchange

        li "I would like to pay for them myself if that's okay. I know what size Hanako wears. I will contact Mother about it tomorrow."
        hyf "Very well."

        show hiroyuki thinking_close_ni
        with chchange

        li "But... I fear that it will take more than a new pair of pants to resolve this."
        hyf "Perhaps it would be best not to expect a magic fix to exist and to simply do whatever little things you can for her—as you did for me a few months earlier."
        li "...Yes."
        "Having calmed down a bit, I neatly fold Father's handkerchief and put it away."
        li "Father... Thank you so much. I'd like you to know that I really appreciate this."

        show hiroyuki smileclosed_close_ni
        with chchange

        "He merely chuckles modestly."
        hyf "That is an unusual amount of gratitude for a mere handkerchief."
        "I shake my head with a sad smile."
        li "Not just the handkerchief, but everything else today as well. I'm really happy you came along with us today."

        show hiroyuki serious_close_ni
        with chchange

        hyf "Do not worry about it."

        nvl clear
        nvl show dissolve

        n "He dismisses my compliment as usual, but my gratitude is completely sincere. I'm not even sure if we would have found Hanako in time if it hadn't been for Father keeping a level head, and now he's here keeping me company too."
        n "{vspace=60}He's been in a somber and apathic mood since Grandfather adopted Mister Kojima as his heir, and me asking him to come along today was mostly an effort on my part to get him out of the house."
        n "Yet when Hisao, Naomi, and I were at a loss on what to do, he took charge and quickly put forth a plan of action. His voice even sounded more alive than before too. Perhaps an event like this was necessary to shake him out of the rut he was in. If that is so, then at least something positive happened today."

        nvl hide dissolve

        li "I meant what I just said. I am very proud of you. I was surprised how well you handled the effort to find Hanako."

        show hiroyuki awkwardspeak_close_ni
        with chchange

        "Father merely mumbles something under his breath that even I would have missed if it hadn't been for the fact that I taught myself over the last few months to pay close attention to him whenever he lowers his voice. I turn to him and give him an inquisitive smile."
        li "...Practice makes perfect?"

        show hiroyuki awkward_close_ni
        with chchange

        hyf "Never mind."
        li "I don't remember getting lost myself very often. Mother, Grandmother, or Akira would usually keep an eye on me at all times."

        show hiroyuki thinking_close_ni
        with chchange

        hyf "That they did."
        li "Hmmm... Akira then?"
        "Father pauses for a moment and then sighs."

        show hiroyuki stern_close_ni
        with chchange

        hyf "This was mostly before you were born, but your sister had the unfortunate tendency to run off on her own whenever we went into town or on a trip, and it was often up to me to track her down."
        hyf "Before long, we would start making mental notes of toy stores, pet stores, and video game stores we came across because those were often the places we suspected she would walk off to if we put ourselves in her shoes."
        "So Father applied the same mindset today while we were trying to track down Hanako. I grin at the thought of Akira sneaking off while our parents weren't looking, but Father didn't sound particularly amused just now."
        li "That must have been troublesome at times."

        show hiroyuki thinking_close_ni
        with chchange

        "He lets out a dejected sigh."
        hyf "Your sister was always a bit of a rebel. We used to tell her that she was being a burden on others by acting the way she did, but I do not think our words ever truly stuck."
        li "Was it really that much of a problem?"

        show hiroyuki awkward_close_ni
        with chchange

        hyf "There were other things too. Akira was a bit of a tomboy even when she was young and played with boys more often than with girls. Things got rough sometimes, and there were times when we heard about her giving some boy a black eye."
        hyf "She would insist things merely got out of hand a bit, but we as parents would be the ones who would get the blame, particularly your mother."
        hyf "We would spend a week or so apologizing to that boy's parents, and things would quiet down, only for something similar to happen again a month or two later."
        "I personally wonder if those occurrances were really just children playing and accidentally going a bit too far or if Akira was perhaps being picked on and stood up for herself."
        li "Akira can be a handful, but she has a softer side as well, Father. Even though there was a rather large age gap between us, she has always been very kind and attentive towards me, and she'd always play with me if I was bored or lonely, even if she had homework to finish."
        li "I don't think I could have wished for a more loving sister at the time, and I believe she will be a wonderful mother herself someday. She may not be the most refined person in the world, but she's responsible when it counts."

        show hiroyuki awkwardspeak_close_ni
        with chchange

        hyf "...Perhaps."
        li "Definitely."

        show hiroyuki smileclosed_close_ni
        with chchange

        hyf "The bond between you two and the good influence you had on Akira when the two of you were together did not escape our attention. We tried to encourage contact between the two of you as much as possible."
        "I'm suddenly reminded of how Akira used to complain about how quick our parents were in letting her look after me instead of doing it themselves. With a surprised expression, I turn in Father's direction."
        li "Are you saying that letting Akira look after me was for her benefit instead of mine or yours?"

        show hiroyuki thinking_close_ni
        with chchange

        hyf "Scolding Akira had little effect, but you never failed to bring out her gentler side. We had been hoping that some of that would eventually rub off on her permanently, but perhaps that was not a realistic expectation after all."
        "I don't think so either. Akira's kind, up-beat and a wonderful person to be around. Those traits are just as much part of her as her laid-back and informal attitude. They simply make her who she is."
        li "Father, how do you... feel about Akira?"

        show hiroyuki eyebrow_close_ni
        with chchange

        hyf "Hmmm?"
        li "I mean... You two may not be on the best of terms, but... she..."

        show hiroyuki thinking_close_ni
        with chchange

        hyf "Hmmm."
        "She's still your daughter."
        "A long silence. Does he lack an opinion or is he simply reluctant to share it with me?"

        show hiroyuki speak_close_ni
        with chchange

        hyf "I think... it is good that Akira stayed behind in Scotland."
        "I cringe at those unexpectedly blunt words. Is he happy to be rid of Akira?"
        li "But Father..."

        show hiroyuki serious_close_ni
        with chchange

        "He softly scrapes his throat as an indication that there's more he'd like to say."
        hyf "Your mother once told me that she believed that Akira was really a Scot at heart."
        hyf "Despite our efforts to give her a traditional upbringing and education, there were some traits of hers—traits like a strong sense of individualism, a strong yearning for independence, and a sense of straightforwardness—that are not good or bad qualities in and of themselves, but become good or bad depending on one's surroundings."
        hyf "I think that in her current environment, those traits probably serve her well, while they used to be a cause of severe worry for us when she was still living here. Perhaps... this was how things were meant to play out all along."
        li "Is this how you and Mother feel about it?"

        show hiroyuki thinking_close_ni
        with chchange

        hyf "Yes. We have felt this way even before it became clear that your attempts at convincing her to also return to Japan were not going to be succesful. Perhaps she will be happier there than she would be here. It would make sense to give her the opportunity to find out for herself."
        "I remember having spent a lot of effort trying to talk Akira into moving back to Japan as well after it became clear that our parents would be moving. Maybe more effort than I should have made. I remember being frustrated when Mother and Father failed to support my efforts."
        "It appears that I might have been so fixated on reuniting our family again once and for all that I completely lost sight of how Akira must have felt, essentially causing me to follow in our parents' footsteps."
        "I make a mental note to apologize to my sister the next time I speak to her even though I doubt she was ever upset with me about this."
        li "I think... you're right. To be honest, when you said it was good that Akira stayed behind, I was worried for a moment that you admitted to hating her."

        show hiroyuki scold_close_ni
        with chchange

        hyf "That girl has made us worry about her on many occasions and could probably use a healthy dose of parental respect, but... hating her would be... very difficult for me to do."
        li "What do you mean?"

        show hiroyuki thinking_close_ni
        with chchange

        hyf "I am afraid that it is not something rational, so I cannot truly explain it. But..."
        "Another long silence."

        show hiroyuki awkwardspeak_close_ni
        with chchange

        hyf "Akira is probably more like your mother than any other person I know. Could you truly hate someone who is similar in so many ways to the person you ended up marrying?"
        "It takes me a second to grasp the significance of Father's words. Over the last several months, I've slowly grown accustomed to Mother's energetic and up-beat behavior."
        "Even though she's living in Japan again now, her way of acting hasn't changed—although she usually adopts a much more reserved and formal posture when we go for a walk around the neighborhood."
        "There have been several times when I considered the possibility that the mother I remembered from my childhood never really existed to begin with, but this is the first time one of my parents actually comes out and confirms it."
        li "Father... Was Mother ever... ashamed of who she was?"

        show hiroyuki smileclosed_close_ni
        with chchange

        "Father lets out a soft chuckle at that. I guess we can rule out that possibility."
        hyf "Your mother realized it was important to set the good example, Lilly."
        li "The good example?"
        "Is it right to put up such a radical facade just to set the good example?"
        "I get the importance of always showing your best side in front of other people, but someone should be able to be herself in front of her family and closest friends, shouldn't she? I mean, I sometimes have trouble showing others the real me, but this is just..."

        show hiroyuki speak_close_ni
        with chchange

        hyf "Lilly, do you get along with your mother?"

        show hiroyuki serious_close_ni
        with chchange

        "It took me some time to completely get used to Mother's casual attitude, but thinking back on it, I think she grew on me faster than I expected. And after hearing what Father just said, I also realize why."
        "Mother and Akira really do act similar in many ways, and since Akira has been somewhat like a mother figure to me for several years, hearing my actual mother act this informal towards me doesn't feel quite as jarring as I would have thought at first. In fact, there's something strangely familiar and comfortable about it."
        "Mother may not be acting as proper and refined now as I remember her, but she's still kind and loving in her own way. That aspect of her hasn't changed."
        li "I do, Father."

        show hiroyuki thinkraised_close_ni
        with chchange

        hyf "Then perhaps it is best not to worry about the matter and focus on the more pressing issues."
        li "...Hanako."

        show hiroyuki serious_close_ni
        with chchange

        "He coughs curtly."
        hyf "And your own exams. Try not to forget about those."
        li "That too."

        show hiroyuki smileclosed_ni
        with chchange

        hyf "Since you have mock exams this week and it is already ten o' clock, it may be a good idea to return to the car."
        li "That late already?"
        hyf "Yes, today has been a long day. And your mother will probably not let me sleep until I have told her all that has happened."

        scene misc_hiroyukicar_ni
        with locationchange

        "We walk back to the car, and Father drives us back to school. He's probably eager to get home himself, so I say my farewells at the school gate."

        scene bg school_gate_ni
        show hiroyuki serious_ni
        with locationchange

        hyf "Very well then. Try your best, and study as hard as you can these last few days. Your mother and I will probably call you before the mock exams start."
        li "Yes. I'm eager to hear how Mother's last few days in Scotland have been."
        hyf "Do not forget to keep your chin up, Lilly. Remember that a proper lady does not mope in public."

        show hiroyuki scold_ni
        with chchange

        hyf "{size=*0.7}Nor does she scream at others in the middle of a crowded place. Do not embarrass me like that again.{/size}"
        "I feel a bit flustered by his scolding, even though he doesn't sound extremely upset with me."

        show hiroyuki thinking_ni
        with chchange

        li "I'll... ah... remember that, Father. I'm sorry."
        hyf "Please hold out your hand."

        show hiroyuki thinkraised_close_ni
        with chchange

        "I do so, slightly puzzled. Moments later, I feel something light being dropped into it."

        show hiroyuki smileclosed_ni
        with chchange

        hyf "For good luck this week."
        "Curiously, I examine what I just got with my finger."
        li "Oh."

        show hiroyuki awkwardspeak_ni
        with chchange

        hyf "It is... ah... a restaurant bill."

        show hiroyuki awkward_ni
        with chchange

        "I chuckle."
        li "Thank you, Father."

        show hiroyuki thinking_ni
        with chchange

        hyf "Good night. And give Miss Ikezawa my regards."
        li "I will."

        hide hiroyuki
        with charaexit

        "And with that, we part ways."
        "It's probably best if I try and get some sleep as soon as I can, so I can get up early tomorrow."

        scene bg school_dormext_full_ni
        with locationchange

        show billorigami_hand at displayitemshow

        pause 1.0

        show billorigami_hand at displayitem

        "Promising myself to check on Hanako first thing in the morning, I drop Father's little paper crane into my bag, take out my cane, and walk back to the dorms."

        show billorigami_hand at displayitemhide

        pause 1.0

        hide billorigami_hand

        li "Please be okay, Hanako."

        stop music fadeout 2.0

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return


    return
