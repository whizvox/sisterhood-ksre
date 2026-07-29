label sh_ch48:

    label .s1:

        $ set_window_tint(TINT_HISAO)

        call sisterhood_timeskip_broken
        scene black

        hi "H-Hanako..."
        "As beads of sweat start appearing on my forehead, and my breathing gets more frantic by the second, I whisper the name of my girlfriend in desperation. I moan as the sensation I'm feeling right now grows even more intense."

        $ i = 0
        while i < 3:
            call sh_heartpulsefast

            $ i += 1
        
        "Not now."

        play music music_tragic
        scene bg school_dormhisao_blurred_ni
        with locationskip

        $ i = 0
        while i < 3:
            call sh_heartpulsefast

            $ i += 1

        "Keep it together."

        $ i = 0
        while i < 3:
            call sh_heartpulsefast

            $ i += 1

        pause 0.05

        "Deep breaths. Breathe in, breathe out, breathe in, breathe out."

        $ i = 0
        while i < 3:
            call sh_heartpulsefast

            $ i += 1

        "I struggle to regain control of myself. If I wasn't sitting behind my desk right now, I probably would have collapsed in a heap already."

        $ i = 0
        while i < 2:
            call sh_heartpulsefast

            $ i += 1

        "Breathe in, breathe out, breathe in, breathe out."

        $ i = 0
        while i < 2:
            call sh_heartpulsefast

            $ i += 1

        "My heart's still pounding like a jackhammer, but its pace doesn't seem to be increasing beyond its already frantic rate."

        $ i = 0
        while i < 2:
            call sh_heartpulsefast

            $ i += 1

        "Breathe in, breathe out..."

        $ i = 0
        while i < 2:
            call sh_heartpulsefast

            $ i += 1

        "I might be able to get up. If this is still going to get worse, I might as well have my episode in the hallway and hope somebody notices and gets help."

        $ i = 0
        while i < 2:
            call sh_heartpulsefast

            $ i += 1

        "At least I'll know the face of my sudden assailant."

        $ i = 0
        while i < 3:
            call sh_heartpulseslow

            $ i += 1

        "I struggle to get on my feet and shuffle towards the door. Just when I reach the doorknob, I feel my heart slowly calming down."

        $ i = 0
        while i < 2:
            call sh_heartpulseslow

            $ i += 1

        "I lean against the door with both hands and try to avoid panicking, concentrating on keeping my breathing steady and emptying my head of any thoughts that might cause distress."

        call sh_heartpulseslow

        show bg school_dormhisao_ni as bg2:
            alpha 0.0
            ease 0.5 alpha 0.2
            1.7
            ease 0.5 alpha 0.4
            1.7
            ease 0.5 alpha 0.6
            1.7
            ease 0.5 alpha 0.8
            1.7
            ease 0.5 alpha 1.0
        with None

        $ renpy.music.set_volume(0.8, delay=1.0)

        pause 1.0

        play sound sfx_heartslow

        $ renpy.music.set_volume(0.6, delay=1.0)

        pause 1.7

        play sound sfx_heartslow

        $ renpy.music.set_volume(0.4, delay=1.0)

        pause 1.7

        play sound sfx_heartslow

        $ renpy.music.set_volume(0.2, delay=1.0)

        pause 1.7

        play sound sfx_heartslow

        $ renpy.music.set_volume(0.0, delay=1.0)

        pause 1.7

        stop music

        $ renpy.music.set_volume(1.0)

        nvl clear
        nvl show dissolve

        n "As my heart slowly returns to its ‘normal’ rhythm, I turn my head around and look at my alarm clock."
        n "It's 00:30 on January the 19th right now and under normal circumstances, I would have been asleep at this time of night already."
        n "{vspace=30}But tomorrow (technically today) will be the first day of the National Center Test for University Admissions, and just about all the subjects I'm not extremely confident about, such as English and history, are on the books this day. That's why I decided to involve myself in a last-minute late-night cramming session."
        n "{vspace=30}I've been doing very little else than studying over the course of the last few weeks with the occasional nap thrown in for good measure. I know that it's not a healthy schedule, but until recently I was convinced that I'd be able to hang in there without any serious issues popping up."
        n "{vspace=30}But then this night came along. I wasn't feeling well, but I've been reminding myself that I'll be able to take it slightly easier after this weekend. All I had to do was hang in there for a little while longer."

        nvl clear
        nvl hide dissolve

        play sound sfx_doorknock
        play ambient ["<silence 0.5>", sfx_heartfast, sfx_heartfast] noloop

        "I was studying when there was suddenly an unusually loud knock on the door that startled the hell out of me and caused my heart to skip a beat, then another beat."

        play ambient ["<silence 0.1>", sfx_heartfast]

        "Just when I realized that this could spell big trouble, my heartbeat returned, only for it to accelerate... and accelerate... and accelerate."
        "While fighting the urge to pass out from the strain, there was interestingly only one thought on my mind."
        "What will happen to Hanako if I die here tonight?"

        stop ambient fadeout 10.0

        "Thankfully, after what felt like an hour but was probably closer to 20 seconds, my heart started slowing its dysfunctional rhythm, and I slowly started regaining my senses."
        "That was close."
        "And now I'm at the door of my room. Whoever nearly scared me to death better have a good reason."

        play sound sfx_dooropen

        scene bg school_dormhallway
        show kenji tsun_gym
        with locationchange

        ke "I was starting to think you dozed off. This is no hour to keep a bro waiting, man."

        play music music_moonlight fadein 2.0

        "I let out a frustrated sigh."
        hi "Damnit, Kenji..."
        "Of course, who else? I consider shouting at him what an idiot he's just been, but then realize I probably don't even have the strength to keep that up and would achieve little anyway aside from getting into trouble with the dorm keeper."

        scene bg school_dormbathroom
        with locationchange

        "So instead, I walk past him and into the bathroom where I soak one of the washing cloths and use it to wipe the sweat off my forehead."
        "As the cool cloth soothes my throbbing head, the adrenaline rush from the experience back in my room makes way for an overwhelming tiredness, so I sit down on the nearby shower seat and wait for my body to get its bearings back."

        show kenji tsun_gym
        with charaenter

        ke "Man, you're not looking so great."
        "Looks like he's still completely oblivious to what just occurred. Of course, obliviousness has always been one of Kenji's strong suits. Even the stress of the upcoming test hasn't changed that."
        "I briefly consider how this could have turned out. The last sight of my life being Kenji looking down at me. What a depressing way to go that would be."
        hi "I think I just got uncomfortably close to keeling over and dying."

        show kenji worried_gym
        with chchange

        ke "You mean like... that thing with your heart happened again?"
        "Wow, I didn't expect him to actually grasp that. Maybe my first impression was wrong."
        hi "Y-yeah, that thing with my heart happened again. I'm kind of impressed you still remember that. The only time I mentioned that to you was nearly half a year ago."
        "That was after my hospitalisation, while I was trying to keep him away from Hanako and Lilly working things out in my room."
        "Man... that feels like such a long time ago. A lot sure has changed since then."

        show kenji neutral_gym
        with chchange

        ke "Of course I remember that. They operated on you and placed that tracking device inside you, right?"
        "And other things haven't changed in the slightest. I guess there's a reason people like to rely on their first impressions after all."
        hi "Forget about the tracking device. Why did you have to knock so loudly? You nearly killed me just there."

        show kenji tsun_gym
        with chchange

        ke "Killed you? That's not a cool thing to say, man. Not cool at all. If I really wanted to kill someone, I wouldn't start making noises to try to scare 'em to death. I'd do something like... drop him off a roof or something... make it look like an accident."
        hi "Look, you startled me with that loud knock. That caused my heart to act up."

        show kenji neutral_gym
        with chchange

        ke "It's gotta be something more. Maybe someone spiked your food. Do you remember it tasting funny?"
        hi "It wasn't the food, Kenji, it was the knocking. Besides, who'd want to poison my food anyway?"

        show kenji tsun_gym
        with chchange

        ke "The feminist conspiracy—or someone working for them. They're trying to keep you from graduating and getting into a university."
        hi "Why would they want to do that?"

        show kenji neutral_gym
        with chchange

        ke "Universities in Japan are still largely dominated by men. They're among the last remaining bulwarks against the feminist influence."

        show kenji tsun_gym
        with chchange

        ke "So now the bitches are conspiring to keep as many men out of there as possible and eliminate contenders before they have the chance to make it in. One at a time. You're lucky you're still alive."
        hi "Is that why you're studying so hard to get admitted to a university yourself?"

        show kenji happy_gym
        with chchange

        ke "Am I ever! And it looks like I got their attention. Damn, now that I think about it, they may have been after me all along. Got the meals mixed up."
        hi "I doubt it. The person who's been making us meals over the last few days is a member of the science club. You said you personally vetted all of them. Shouldn't that clear him?"

        show kenji neutral_gym
        with chchange

        ke "Oh, right. So I guess it wasn't the food. Did you pass any girls carrying umbrellas lately?"
        hi "Why?"
        ke "There's the old trick with the poison-tipped umbrella. You pass a chick carrying such a thing, you feel a little prick in your ankle and by the time you're keeling over, the perp is already on the other side of the country."
        hi "It was the knocking, Kenji."
        ke "Did you receive any letters containing some strange powder lately?"
        hi "It was the knocking, Kenji. Why is that so hard to accept?"

        show kenji tsun_gym
        with chchange

        ke "Because I knock like that all the time whenever I need a favor, man. And you've always handled it just fine."
        "That's kind of difficult to deny."
        hi "You know, maybe you're right. Maybe I'm just way more out of shape than I thought."

        show kenji worried_gym
        with chchange

        ke "You don't really look in good shape, dude. Maybe... you know... you should get some sleep. You look like you need it."
        "I'm already kind of used to Lilly and Hanako mothering me, but if even Kenji starts telling me I need to take it easy, I must be a really sordid sight."
        hi "...maybe I should. Tomorrow's gonna be one hell of a day. I doubt I'll get much more cramming done anyway."

        scene bg school_dormhallway
        with locationchange

        "I get up from the shower seat and carefully make my way back to the door to my room. Before going in, I turn to Kenji, having just remembered something."
        hi "By the way, why did you want to see me at this hour to begin with? Was it really that important that it couldn't wait until morning?"

        show kenji happy_gym
        with charaenter

        ke "Oh yeah, that's right... it was. It was about... uh..."
        "A new feminist plot? Breakfast money? Or something even more..."

        stop music fadeout 5.0

        ke "...your science notes. I need your notes on the aerodynamics stuff. You're the science club president. You took notes on that, right?"
        "...mundane? Gee."
        hi "Yeah, I'll go and get them."

        play sound sfx_dooropen

        scene black
        with locationchange

        "Still feeling tired, but no longer as anxious, I enter my room, get the notes he asked for and walk back out."

        scene bg school_dormhallway
        show kenji happy_gym
        with locationchange

        hi "Here's what I have on the subject."
        ke "You're a real pal. If I can't make it into university, I might as well keep the honor to myself and eat the feminists' fuckin' poisoned food right here and now."

        show kenji worried_gym
        with chchange

        ke "And uh... Sorry about the knocking, man. Didn't expect you to take it that badly."
        hi "Thanks. I didn't expect it either, so maybe it was a wakeup call."

        show kenji neutral_gym
        with chchange

        ke "I'll return them when I'm done with them."
        hi "It's okay. I think I know what's in them anyway. You might not be able to use them though. I wrote in rather tiny letters when I took those notes. You might have trouble reading them."

        show kenji tsun_gym
        with chchange

        ke "Hey, don't knock the eyes, man. They've seen things. Terrible things that you can't imagine..."
        "He's back in his own world again."
        hi "Good night, Kenji."

        play sound sfx_doorclose

        scene black
        with locationchange

        ke "Like when I made a ship in a bottle and my mom sat on it..."

        stop music fadeout 2.0

        scene black

        pause 2.0

        if _in_replay:
            return

    label .s2:

        $ set_window_tint(TINT_HISAO)

        play ambient sfx_phonering

        pause 2.0

        scene bg school_dormhisao_ss
        with openeye

        queue music music_serene fadein 4.0

        "I'm woken up from my slumber by the sudden sound of my cell phone ringing."
        "Still groggy, I stumble out of bed and manage to snap it open just before my voicemail would have kicked in."

        stop ambient

        hi "Hisao Nakai..."
        "Voice" "Good morning, Hicchan!"
        hi "Wha... Misha is that you?"
        "Mom" "Misha? Don't you recognize the voice of your own mother anymore?"
        hi "Sorry, Mom. I just got out of bed."
        "I'm now awake enough to remember that Misha and Shizune weren't even the first people to use that nickname on a regular basis. I guess I shouldn't be surprised that Mom's calling me today."
        "I was just taken off guard by how early she called. She probably wanted to make certain I wouldn't oversleep."
        "Mom" "I hope you weren't too nervous to sleep."
        "To be honest, that little episode last night did manage to rattle me, and I started wondering whether it was even a smart idea to set my alarm clock before ultimately deciding that without it I was almost guaranteed to oversleep."
        "Now it turns out that I was never in danger of that to begin with."
        hi "No, not really."
        "I turn off my alarm clock and start opening my pill bottles with my free hand. I might as well get that out of the way not that I'm awake."
        "Mom" "This is the day you're most nervous about, isn't it?"
        hi "Yeah. History and languages are on the menu today. The most important subjects for me aren't up until tomorrow, but I'll still need to do fairly well on today's exams in order to keep my average up."
        hi "I have some leeway due to science and math being weighed way more heavily by the faculty I'm applying for than today's subjects, but they could still drag me down if I'm not careful."
        "Mom" "You've been studying so hard over the last few months, I know you're going to do well."
        hi "I really hope so."
        "Mom" "When do you expect to know the results?"
        hi "We're not going to get any official results, but the school's making copies of our answer sheets for us and the National Center for University Entrance Examinations is publishing the answers this evening, so that's when I'll know how I did. Same thing tomorrow."
        hi "Tomorrow evening I'll be able to tell whether I have a chance to take the entrance exams for university or whether... I'll have to look for other options."
        "I'm really hoping it won't come to that. There are smaller universities in the area that don't look at the results of the Center Test for student admittance, but after Mutou's countless lectures about aiming high, I would be very reluctant to to apply there."
        "Assuming I won't feel too guilty to approach him, Mutou would be a good person to discuss alternative options with in case I flunk the tests this weekend."
        "Mom" "Let's not think about that yet. You'll let us know once the results are in, won't you?"
        hi "Of course."
        "Mom" "I'll soon be heading over to the shrine a few blocks away to get some good luck charms for you and pray for good luck. The rest is up to you, Hicchan."
        hi "Thanks Mom."
        "Mom" "Well, good luck today."
        hi "Ah, Mom?"
        "Mom" "Yes?"
        hi "Could you... Get some good luck charms for Hanako too? And pray for her good fortune? She's going to need it just as badly as I do."
        "Mom" "I will. How has she been doing?"
        hi "Alright... I think."
        "Mom" "Good luck to both of you today."
        hi "Thanks, Mom."

        scene black
        with locationchange

        "Having finished my morning diet of medication, I take a quick shower and go down to the kitchen to have breakfast, taking one of my study books with me to do some last-minute cramming while I'm eating."
        "There's been an initiative from the junior students over the last few weeks to prepare meals for the seniors so that we had more time to study. It's one more example of the close community that this school is, and I for one am really thankful for it."

        scene bg school_dormext_full
        with locationchange

        "After finishing breakfast, I pack up my things and head for the girls' dorm."

        play ambient sfx_crowd_indoors fadein 2.0

        scene bg school_dormcommon
        show crowd
        with locationchange

        "The girls' dorm's common room is really crowded right now. I see several 3rd years sitting at the tables, eating breakfast with one hand while leafing through a book with the other."

        show naomi basic_neutral at right
        show natsume basic_neutral at tworight
        with charaenter

        "I recognize Natsume and Naomi at one table, both studying intensely and catch Naomi letting out a pronounced yawn. She sure looks like she's seen better days, though she'd probably say the same about me if she heard me say this."

        hide naomi
        hide natsume
        show shizu basic_normal2 at left:
            xzoom -1.0
        with charaenter

        "I also see Misaki from my class swapping notes with another girl whose name I can't remember. In one of the corners of the room sits Shizune, her back partially turned to the rest, calmly flipping through the pages of one of her books."

        hide shizu
        with charaexit

        "Two girls whom I remember being in Lilly's class head towards the exit, and I quickly step aside to let them pass."
        "The common room's probably way too crowded for Hanako to be here, so I head for her room, hoping she hasn't already left."

        stop ambient fadeout 1.0

        scene bg school_girlsdormhall
        show lilly cane_listen at twoleft
        show miyagi neutral at tworight
        with locationchange

        "As I enter the hallway leading to Hanako's and Lilly's room, I notice Lilly standing there talking to one of the teachers. I approach them and give the teacher a polite bow."
        hi "Good morning, Lilly. Good morning, Miss Miyagi."

        show lilly cane_smile
        with chchange

        li "Oh, hello Hisao. How are you? Are you feeling up for today?"
        hi "Yeah, I'm fine, Lilly. I'll be happy when this day is over, but I haven't counted myself out yet."
        "Our English teacher raises an eyebrow at my description of my own condition, but thankfully doesn't say anything."
        "I've already decided that I'm not going to let Lilly (or Hanako) in on what happened in my room last night. The last thing I want is for one of them to have a flashback to what happened with Mister Satou."
        "It's funny, but I think I'm starting to understand how he must have felt: slowly feeling your limits approaching, but also realizing that the stakes are currently too high to quit or slow down. You don't hold back and save your strength in sight of the finish line. You go all out."

        show lilly cane_smileclosed
        with chchange

        "Lilly smiles."
        li "Miss Miyagi has been going around this morning giving pep talks to the girls who are about to participate in the test. Maybe she can give you one as well."

        show miyagi smile
        with chchange

        "Lilly's homeroom teacher gives me a look-over."
        my "You're Mutou's star pupil. You'd better make it through this weekend, or you're going to break his heart."

        show lilly cane_planned
        with chchange

        hi "That's not the most uplifting pep talk I've ever had."

        show miyagi neutral
        show lilly cane_smileclosed
        with chchange

        my "What tests are you taking today?"
        hi "Ethics, Japanese History, Japanese Literature, and English. History's going to be a bit rough, but it's the last one I'm most worried about."
        my "Just focus on one subject at a time without worrying about the rest and try not to spend too much time on one question."
        my "Since all your most important subjects won't be tested until tomorrow, just try to do the best you can and save your strength for the subjects that give you the most points—namely literature and English."
        my "There'll be an English listening test at the very end, but the written test is the one you should try to do as best as you can in since it carries a lot more weight."
        hi "I'll do my best. How about your star pupil?"

        show miyagi smile
        with chchange

        "Miss Miyagi gives Lilly a confident nod."
        my "I think I can safely stake my job on her acing the English test today."
        my "Many students have been dreading the listening part of the test ever since it was introduced two years ago, but someone who was both raised bilingually and is used to paying close attention to audio cues should have no problem achieving a perfect or near-perfect score there."

        show lilly cane_weaksmile
        with chchange

        "Lilly smiles humbly."
        li "I'll do my best to live up to your expectations. English will be the easy part today. I'll still have Contempory Social Studies, World History, and Japanese Literature to deal with first. And there's... tomorrow."
        my "You've been studying pretty hard over the course of the last two months. It should be sufficient. Just concentrate on doing well on the subjects that carry the largest amount of weight for your university application."

        show lilly cane_smileclosed
        with chchange

        li "I'll do my best."

        show miyagi neutral
        with chchange

        hi "Why are there teachers in the dorms, by the way? I noticed Mister Hoshino walking around the guys' dorm this morning as well."
        my "We're essentially doing a head count. Making sure there are no students who are set to take the tests today who accidentally oversleep."

        show lilly cane_smile
        with chchange

        hi "The school really seems to be going out of its way to help its students make it through examination hell."
        my "In the end the actual studying is still in your hands, but yes, we do try to accommodate you as much as we can. That's also why you're allowed to take the tests here on the school grounds instead of having to travel to the nearest university to take part in the examinations."
        my "Normally, only the larger high schools would be granted this privilege. You can thank us for our efforts on your behalf by doing well on your test this weekend."
        hi "Have you already seen Hanako this morning? I came here looking for her."
        my "Not yet. I was about to go and check on her."

        show lilly cane_displeased
        with chchange

        "Lilly takes this moment to speak up."
        li "I believe I have heard her early this morning. She probably went to get some breakfast, though she's been eating in her room—as usual lately."
        "I must admit I'm still a bit worried about her. From what Lilly has told me, Hanako only leaves her room these days to attend the supplementary lessons the school made her take. She eats and studies in her room with the door locked. At least I hope she's been able to study."

        scene bg school_dormhanako
        show hanako emb_timidmessy_close:
            center
            xpos 0.39
        show expression Solid("#00000022")
        show hanako_door_base at right
        show hanako_door_door at left
        with locationskip

        play sound sfx_doorknock2

        "Lilly's homeroom teacher walks up to the door leading to Hanako's room and gives a few gentle raps on it."
        my "Ikezawa? This is Miyagi."

        pause 0.5

        show hanako_door_door:
            xpos -0.06
        with charamove

        "There's no immediate response, but just as the teacher raises her hand to knock again, the door opens just a bit, and I can see Hanako peering at us from inside the room."
        my "Ikezawa, it's about time for everyone to head for the gymnasium. Are you ready to go?"

        show hanako_door_door:
            xpos -0.19
        with charamove

        pause 0.5

        scene bg school_girlsdormhall
        show lilly cane_listen at left
        show miyagi neutral at twoleft
        with locationchange

        show hanako emb_downtimidmessy at right
        with charaenter

        show hanako emb_downtimidmessy at tworight
        with charamove

        "Hanako opens the door further and gives a nervous nod. She takes her bag and then walks out, closing the door behind her."
        hi "Hey, Hanako."

        show lilly cane_weaksmile
        with chchange

        li "Good morning, Hanako. Let's both do our best today."
        ha "H-hey."
        my "Good morning, Ikezawa. What subjects will you be taking today?"

        show hanako emb_timidmessy
        with chchange

        ha "Umm...P-Politics and Economy, J-Japanese History, Japanese Literature, and ah... English."
        my "And you have studied hard for them, haven't you?"
        "A silent nod."
        my "All the teachers here know that your mock exam results weren't an accurate representation of what you're really capable of, so please do your best to prove us right today."
        ha "I'll t-try."
        my "What study are you aiming for?"

        show hanako emb_downtimidmessy
        with chchange

        ha "J-Journalism and Media."
        my "Then those first two tests will probably be critical. Do your best."

        show hanako emb_timidmessy
        with chchange

        ha "Y-yes."
        my "The three of you should go now. My colleagues have probably unlocked the gym already. Also..."

        stop music fadeout 1.0

        show hanako defarms_worrymessy
        show lilly cane_surprised
        with { "master": Dissolve(0.2) }

        "Voice" "TEACHER!"
        "We turn around, and I notice one of the girls from our class running up to us."
        my "We're not supposed to be running in the hallways, Komaki."
        "Ikuno" "Sorry, but... in the common room... Inoue."

        play music music_sadness fadein 4.0

        show hanako defarms_strainmessy
        show lilly cane_reminisce
        show miyagi stern
        with chchange

        show miyagi stern at offscreenright
        with charamovefastest

        show hanako defarms_strainmessy at offscreenright
        with charamovefastest

        "We hear our teacher softly curse under her breath, causing Lilly to cringe, before she takes off and runs down the hallway with Hanako following close behind her."
        hi "This doesn't sound good."

        play ambient sfx_crowd_indoors fadein 1.0

        scene bg school_dormcommon
        show crowd
        with locationchange

        "We make our way down the stairs to the common room as fast as Lilly's navigation skill allows us, but by the time we arrive, it's already so crowded in there that I can see neither Hanako nor the teacher. Even though I can't see Miss Miyagi in the crowd, I can certain hear her."
        my "Damnit, can you give us some room already?"
        my "Suzuki, hand me that pillow over there please!"
        my "Miura, go and get a nurse to help out. Wait, get two of them! Tell them to bring a stretcher too!"
        my "Get the chairs away from here. Put them in the hallway!"
        my "Look, this isn't working. No more spectators! Everyone who's taking the test, go to the gymnasium at once. Everybody else, go to your room! Come on! Today, please!"

        stop ambient fadeout 3.0

        hide crowd
        with charaexit

        "At this point, the crowd starts to disperse, and as the common room starts emptying I finally start taking in the scene before me."

        scene ev seizure_commonroomfit
        with locationchange

        "Naomi's lying on the floor of the common room, her limbs thrashing about as if she's being electrocuted. One of the tables and several chairs are scattered about."
        "Miss Miyagi is kneeling by Naomi's side, holding a pillow under her head and trying to prevent her from hurting herself."
        "I've seen Naomi have fits before, but the sight of them still never fails to make me feel freaked out."

        scene bg school_dormcommon
        show natsume basic_sad at tworight
        show hanako emb_downsadcrymessy at right
        show lilly cane_concerned at left
        with locationchange

        "Now that the bystanders are all gone, the only people in the room besides Naomi and Miyagi are Lilly, Hanako, Natsume, and myself. Neither Hanako nor Natsume are saying anything, but the look in their eyes is all too telling."
        "They both look crushed. I think they both realize the implication of this event. We all do."

        hide lilly
        show miyagi resigned at twoleft
        with charaenter

        my "I really don't think the four of you should still be hanging around here. The nursing staff will probably be here any second now, and they'll take over from me. There's nothing you can do for Inoue right now."
        "Natsume nods sullenly, and when she speaks up her voice sounds like it's about to break."
        nt "M-maybe not right now, but... I think that... someone should stay by her side. When she wakes up and she... she realizes what happened..."

        show miyagi neutral
        with chchange

        my "I hope you're not talking about yourself. I could give Takawa a call. She can probably handle it."
        "Voice" "Natsume?"

        hide miyagi
        show jun basic_sad at twoleft
        with charaenter

        "We turn around and see a frail-looking girl standing in the doorway whom I recognize as Hanako's and Naomi's friend from the writing club."
        nt "Jun!"

        show jun basic_sadclosed
        with chchange

        jun "I... ah... probably won't do as good a job at this as you would, but I'll stay with Naomi. You and Hanako should get going and pass your tests."

        show natsume basic_neutral
        show hanako defarms_worrymessy
        with chchange

        "Natsume and Hanako exchange a short glance and then simultanously nod their head."

        show jun basic_sheepish
        with chchange

        nt "Thank you Jun. That's really kind of you. We'll leave Naomi in your care then."

        scene black
        with locationchange

        "With that issue taken care of, we quickly leave the dorm building and head towards the gymnasium."

        scene bg school_courtyard
        show lilly cane_sad:
            xalign 0.15
        show hanako emb_downsadmessy:
            xalign 0.4
        show natsume basic_sad at tworight
        with locationchange

        "As we pass the main school building, Natsume lets out a depressed sigh."
        nt "She was so looking forward to graduation, too. I really wonder how she's going to take this. Even though she's been a little careless lately, she didn't deserve having the rug pulled out from under her in a way like this."

        show lilly cane_reminisce
        show hanako emb_timidmessy
        with chchange

        "Lilly's ears perk up."
        li "I'm sorry, but... did you say she was careless? This didn't come completely by surprise?"
        "Natsume thinks for a moment and then shrugs as if to say ‘why not?’"

        show lilly cane_displeased
        show natsume basic_neutral
        with chchange

        nt "Naomi can't really do much to prevent her episodes completely, but whether they occur occasionally or all the time depends a little bit on her lifestyle, which hasn't been very healthy lately."

        show lilly cane_sad
        show hanako emb_downsadmessy
        with chchange

        li "Are you saying that she overstepped her own boundaries?"
        nt "Stress and sleep deprivation are things that make her more vulnerable to seizures. Her episodes have been increasing in frequency lately, and over the last week she was down to one every 48 hours or so."
        nt "I was really afraid that she was going to damage her brain if she kept going like this. She was caught up in this downward spiral that only seemed to get worse."

        show lilly cane_reminisce
        show hanako emb_timidmessy
        show natsume basic_sad
        with chchange

        li "What do you mean?"
        nt "The more seizures she went through, the more stressed she became, and the more time she spent cramming in an attempt to make up for all the time all those fits were costing her."

        show lilly cane_concerned
        show hanako emb_downsadmessy
        with chchange

        li "What a horrible situation to be in."
        nt "I was really hoping she'd be able to hold out until the end of the weekend. She kept telling me that she'd take it easier for a bit after tomorrow."
        "Ugh."

        show lilly cane_sad
        with chchange

        li "Please give her my regards when you speak to her."

        show natsume basic_neutral
        with chchange

        nt "Thanks, Satou."

        show hanako emb_sadmessy
        show lilly cane_displeased
        with chchange

        ha "H-Hisao, are you... alright? You look a bit pale."
        hi "I'm okay, Hanako. Just a little upset about what just happened and more than a little nervous about the tests today. I'll be fine. As long as I can struggle my way through history and English, that is."

        scene bg school_gymext
        show crowd
        show shizu behind_blank at right
        show misha perky_sad at tworight
        show yuuko worried_up at left
        with Fade(1.0, 0.0, 1.0)

        play ambient sfx_crowd_outdoors fadein 1.0 volume 0.5

        "When we reach the entrance to the gym, we can see that a lot of people have already gathered there. I even see Yuuko hanging around near the entrance. Is she taking the Center Test too?"

        hide shizu
        hide misha
        hide yuuko
        with charaexit

        "Several groups of students, especially the girls, are speaking to each other in hushed tones. It's not difficult to guess the subject of their current conversation."

        show natsume basic_sad at right
        with charaenter

        "Rather than join one of the groups, Natsume secludes herself some distance away from the rest. She's probably not fond of the idea of people approaching her about Naomi right now."
        "Before we can decide on whether to join her or not, I see Hanako pointing something out, and a moment later I see Lilly's homeroom teacher approaching."

        hide natsume
        show miyagi neutral
        with charaenter

        play sound sfx_clap

        pause 0.2

        play sound sfx_clap

        pause 0.2

        $ renpy.music.set_volume(0.5, delay=1.0, channel="ambient")

        "As she reaches the place where we're gathered and several female students walk up to her, Miss Miyagi loudly claps her hands a few times in order to get everyone's attention."
        my "Alright, listen up everyone! We're all a little shaken by what happened to Inoue this morning, but the situation is under control, the nurses are looking after her, and we'll be talking to the National Center of University Entrance Examinations to work out a solution to this later today!"
        my "So put this issue to rest and focus on your exams! I'll be acting as one of the proctors throughout the day, and if you're in my class and need my assistance with anything sight-related, but not question related, just silently raise your hand and I'll be right with you."
        my "There's a representative of the National Center keeping an eye on things as well today, so there's not a lot of room for leniency. Good luck everyone and go and give this your all!"

        show miyagi neutralsmoke
        with chchange

        "Almost as an indicator that she's finished, Miyagi pulls out a cigarette and lights it."

        show lilly cane_concerned at twoleft
        with charaenter

        show miyagi resignedsmoke
        with chchange

        "The first students start pouring into the gym and Lilly, having smelt the smoke, approaches her mentor with a slightly uncomfortable expression and gets a sigh and semi-guilty look in return."
        my "Borrowed these from the dormkeeper's office just before I left. I really felt I needed one. And to think I was going to give up smoking for real this year."

        show lilly cane_displeased
        with chchange

        show lilly at left
        with charamove

        show natsume basic_neutral at tworight
        show hanako emb_sadmessy at right
        with charaenter

        stop ambient fadeout 2.0

        hide crowd
        with charaexit

        "Natsume approaches Miyagi with a wary expression."

        show miyagi neutralsmoke
        with chchange

        nt "Teacher, what solution could possibly be worked out? Regulations on tardiness and absence are extremely strict for this test and there's no chance for retakes. Are there loopholes we don't know about?"

        show miyagi resigned
        with chchange

        "Miyagi gives a tired sigh while dropping her cigarette on the floor and putting it out with her heel."
        my "What else was I supposed to say? I don't want this lingering in the back of everybody's head all day long."

        show lilly cane_reminisce
        show natsume basic_sad
        show hanako emb_downsadcrymessy at right
        with chchange

        stop music fadeout 5.0

        "Both Natsume's and Hanako's face drops upon hearing this news. Miyagi looks a little bit uncertain, but then puts one hand on each of the girls shoulders and gives them both a tiny squeeze."

        play music music_drama fadein 4.0

        show lilly cane_surprised
        show miyagi angry
        with chchange

        my "You two need to shape up! It's more important than ever that the two of you do well today. Seeing that you are both good friends of hers, how do you think Inoue will feel if this little incident ends up costing both of you your chance to make it into your university of choice?"

        show lilly cane_displeased
        show natsume basic_neutral
        show hanako emb_sadmessy
        with chchange

        "That strategy has an extremely familiar ring to it. It's the same approach Miss Takawa used on Lilly and me. I wonder if this kind of guilt-tripping is the standard approach among school staff."
        "Nevertheless, I can tell that Miyagi's words get through to Natsume and Hanako."
        my "Inoue is going to feel really bad about this, but if I know her a little bit, I don't think it's going to keep her down for long. She'll be set on throwing you two a celebration party in the upcoming spring, so make sure not to deny her that opportunity."

        hide miyagi
        with charaexit

        show lilly cane_listen
        show natsume basic_serious
        show hanako emb_downdeterminedmessy
        with chchange

        "With that, Miss Miyagi enters the gym. Natsume and Hanako exchange a confused look, but then I see something dawn on their faces."
        "Suddenly, Natsume sticks out her hand at Hanako."
        nt "I think Miss Miyagi's right. Naomi will probably be cheering on us, so let's not let her down. Let's do this, Hanako!"
        "Hanako gives the most determined nod I've seen for months and puts her right hand on top of Natsume's as if to reinforce this pact."
        ha "Let's k-keep this burden off Naomi's shoulders, Natsume. Let's make her p-proud of us."

        show natsume basic_annoy
        show hanako emb_determinedmessy
        with chchange

        $ show_doublespeak(nt, _("Right!"), ha, _("Right."))

        hide natsume
        hide hanako
        with charaexit

        show lilly cane_smileclosed
        with chchange

        "The two give a defiant nod and then follow the rest of the students into the gymnasium."
        "I turn to Lilly who now has an admiring smile on her face."
        hi "When I first saw her this morning, Hanako looked a little worse for wear, but she was looking really determined just now. It pains me to say this, but maybe this was just what she needed."
        "I've seen this kind of look on Hanako's face before. It's that look of intense concentration she sometimes puts on during a game she's determined to win. And she often wins when that happens. I really believe she's going to give it everything she has today."

        show lilly cane_smile
        with chchange

        li "We can't do any less, Hisao. Let's do our best today as well."

        scene bg school_gymint_exam
        show crowd
        with locationchange

        "And with that, we walk into the gym ourselves and take our place in our designated spots. When the proctor gives the signal to begin, the only thing on my mind is getting a good score today."
        "But nevertheless, during the break between the Japanese History exam and Japanese Literature test, my thoughts briefly return to the sight of Naomi convulsing on the floor of the common room."

        show ev seizure_commonroomfit at sepia
        with { "master": Dissolve(1.0) }

        "I didn't tell Hanako and Lilly, but what happened to Naomi hit really close to home for me this morning."
        "It could have been me."
        "Naomi's situation sounded eerily similar to my own. It probably was."
        "It could have been me."
        "I could have had an episode less than 12 hours later, and I would have lost an entire year. In just a single moment, all the studying I've done over the last few months would have been rendered meaningless."
        "I make a sincere vow not to let this happen to me."

        show black
        with { "master": Dissolve(1.0) }

        "Tomorrow is primarily science and math. I'm pretty good at both of them. I've been studying on them for weeks."
        "Maybe I really should be going to bed early tonight."

        stop music fadeout 3.0

        scene black
        with endchapter

        if _in_replay:
            return

    return

label sh_heartpulsefast:
    play sound sfx_heartfast

    show heartattack alpha
    with Dissolve(0.1)

    hide heartattack alpha
    with Dissolve(0.2)

    pause 0.15

    return

label sh_heartpulseslow:
    play sound sfx_heartslow

    show heartattack alpha
    with Dissolve(0.1)

    hide heartattack alpha
    with Dissolve(0.2)

    pause 0.7

    return