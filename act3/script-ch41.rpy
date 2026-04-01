label sh_ch41:
    label .s1:

        $ set_window_tint(TINT_HANAKO)

        call sisterhood_timeskip_broken

        play sound sfx_alarmbeep volume 0.7 fadein 2.0 loop

        pause 4.0

        scene bg school_dormhisao_blurred_ni
        with openeye

        "An earpiercing whine comes from the alarm clock near the bed, and I annoyedly swat at it in an attempt to make it shut up."

        stop sound

        hi "Ouch!"
        "Unfortunately, somebody else was in the process of turning it off already, and as a result my hand ends up slapping his."

        scene bg school_dormhisao_ni
        with locationchange

        ha "S-sorry!"

        show hisao basic_frown_nak_superclose at tworight
        with charaenter

        play music music_serene fadein 4.0

        hi "That's not exactly a nice way to say good morning."
        ha "Then... maybe this makes up for it?"

        show hisao basic_smile_nak_superclose
        with chchange

        "I give my boyfriend a quick kiss as a means of apology. He smiles in response."

        show hisao basic_grin_nak_superclose
        with chchange

        hi "Yeah, that ought to do it."

        show hisao basic_neutral_nak_superclose
        with chchange

        play sound sfx_rustling

        "He yawns, stretches out and, then slowly gets out of bed."
        "I look at his alarm clock. It's still really early in the morning. Hisao always sets his alarm clock this early during the week, so he can go running on the track before class."

        show hisao at left
        with charamove

        "At least, when the weather permits it. As autumn gave way to winter, he's been forced to put off his track visits more and more. And now he's carefully brushing aside his curtain to see if that will be the case today as well."
        ha "And...?"
        hi "I don't know. It's not exactly dry, but it's not exactly pouring either."

        $ renpy.music.set_audio_filter("ambient", renpy.audio.filter.Lowpass(880))

        play ambient sfx_rain fadein 1.0 volume 0.4

        scene bg school_dormext_full_ni
        show drizzle
        with locationchange

        "I get out of bed, walk over to where he's standing and peek through the gap between the curtains."
        "I can clearly see raindrops falling from the sky. It might just get worse before it gets better. I bet it's kind of cold outside as well."
        ha "It's raining again."
        hi "It's not really raining, it's merely drizzling."
        ha "Are you really planning to go running?"
        hi "I'm not sure yet. I don't want to risk catching a cold, but I doubt I'll have much opportunity for running in the upcoming months."
        ha "You could maybe use the fitness facilities in the auxiliary building after classes."
        hi "I would if they were open in the morning. I'd rather use the afternoon to study."

        $ renpy.music.set_volume(0.2, delay=1.0, channel="ambient")

        scene bg school_dormhisao_ni
        show hisao basic_neutral_nak_superclose at left
        with locationchange

        show hisao basic_neutral_nak_superclose at right
        with charamove

        "He walks over to the shelf holding his medication and starts opening the various bottles standing there."
        "I'm not sure if that means he has decided to go to the track anyway or if he simply feels he might as well get that part of his daily routine out of the way."

        $ renpy.music.set_volume(0.4, delay=1.0, channel="ambient")

        scene bg school_dormext_full_ni
        show drizzle
        with locationchange

        "In the meantime, I keep looking out the window."
        ha "I think... it's starting to rain harder."
        "He walks back to the place where I'm standing and peeks past me."
        hi "I don't really see anything different. Maybe it just seems to you that way."
        ha "Huh?"
        "He grins."
        hi "Maybe you'd just like me to get back to bed."
        "I smile."
        ha "Wouldn't... you... too?"

        $ renpy.music.set_volume(0.2, delay=1.0, channel="ambient")

        scene bg school_dormhisao_ni
        show hisao basic_neutral_nak_superclose at left
        with locationchange

        "He chuckles and nods, but doesn't really say anything. He just keeps staring out the window, still trying to make up his mind."
        "I hesitate for a moment and then decide to help him a bit."

        hide hisao
        with charaexit

        "Before I can have second thoughts, I walk back a few steps and put my hair clip in, a small attempt to make my bed hair look a little bit more orderly."
        ha "H-Hisao...?"
        hi "Hmmm?"

        stop music fadeout 2.0

        "He waits for me to reply, and when I don't say anything back, he turns around to look at me."

        scene ev morningpractice_undress
        with mediumflash

        play music music_one fadein 4.0

        "As he does so, I straighten myself out, pull the shoulders of my nightgown away, and let it slowly slide down to the ground."
        "I can see his eyes grow wide at the sight of this bold gesture."
        "I avert my eyes and blush heavily as I feel his gaze wander up and down my body, but I resist the urge to cover myself up again."
        ha "Ummm..."
        "He doesn't say anything. He just keeps looking at me. He probably doesn't even know how to react. Nevertheless, there's a small trace of a smile on his face."
        "Trying hard to ignore the shaky feeling in my legs, I slowly walk up to him, press myself against him, and start kissing him deeply."
        "During a breathing pause, I look into his eyes and do my best to give him my best smile."
        ha "Hisao... I-instead of going to the t-track, maybe... s-stay here? With m-me?"

        scene ev morningpractice_seduce
        with charachangeev

        "As I say this, I gently press my index finger against the side of his face, using it to tickle his earlobe before moving to a little spot on the side of his neck."
        hi "Ah!"
        "I giggle as I watch him shudder."
        hi "So... alternative morning practice?"
        ha "Uh huh..."
        "I remain focused on his neck for a little while longer before running my finger down to the inside of his elbow."
        "Over the course of the last four months, I've discovered countless little spots I can tickle or stroke to get a reaction out of him or get him aroused, and I can find most of them even with my eyes closed."
        hi "We... probably shouldn't..."
        "A playful kiss on his cheek."
        ha "...Hisao?"
        "I wrap one of my legs around his and use my toes to tickle his calf."
        hi "...but it does sound tempting... some variety in practice activities... ahhh... and practice partners..."
        "I tickle his side and the area below his belly button."
        hi "Aah! H-Hanako..."
        "His breathing speeds up as I tickle his nipples before moving downward and putting my hand on the part between his legs."
        hi "Y-You're not giving me a great deal of choice, are you?"

        scene ev morningpractice_reciprocate
        with charachangeev

        "He starts thrusting his lower body against my hand, and his own hand starts wandering across my body before stopping between my legs."
        ha "If you... really don't want to..."
        "I instinctively grind my private area against his hand as well."
        hi "You can't say that after teasing me like that."
        "I giggle again, withdraw my hand and then, as a final tease, sneak it into his boxers and softly tickle him between his legs for just a split-second before withdrawing again."
        "From what I just felt, I could tell that a visit to the track is the last thing on his mind right now."
        hi "In 15 to 20 minutes, this place... is going to be too active to easily sneak out... if we take too long..."
        ha "We could... keep it s-shorter than... usual."
        hi "A quickie here and now then?"
        "I blush and nod, averting my eyes for a moment as I let my underwear drop to the floor. He shoots me a slightly uncomfortable grin as he follows my example."
        hi "Well, it's pretty clear I'm not exactly in good shape for running at the moment anyway."
        ha "Pffffffff..."
        "It's true that running would probably be uncomfortable for him right now and just the brief mental image of him trying anyway causes a laughing fit that I quickly stifle by pressing my hand against my mouth."
        hi "Shall we?"

        scene ev morningpractice_grimace
        with charachangeev

        "I shyly nod, hug him tightly and gently nudge him against the wall. But when I reach down and try to guide him inside me, the resulting sensation is uncomfortable enough to make me grimace."
        ha "Mgh!"
        "My boyfriend lets out an amused snicker at the face I made just now and gives me a quick peck on the nose."
        hi "Heh, can I share a little nugget of wisdom that my usual practice partner drilled into me over the course of several months?"
        hi "No matter how badly you want to get started, you can never skip the warm-up."
        "His hand wanders down and tickles the inside of my thighs, forcing a gasp out of me."
        hi "May I?"
        ha "W-wait."

        scene ev morningpractice_rub
        with charachangeev

        "I reach down and take hold of him again, but instead of guiding him inside, I simply take his tip and rub it against my most sensitive area—carefully at first, then faster and firmer as I get used to the sensation, making sure to move my hand to let him share in the experience with me."
        "I place my other hand on his shoulder to stabilize myself and give him a quick kiss. I close my eyes and block out everything except for the sensation down below and the feeling of his hands wandering between my sides, chest and collarbone."
        ha "Mmm... Mmm... Mmm..."
        hi "Hana—... Mmmm..."
        "For a little while I allow myself to get lost in the experience, occasionally giving him a little squeeze as well, my arousal steadily building up, until a shudder in my legs forces me to brace myself."

        scene ev morningpractice_ballet
        with charachangeev

        "Without saying anything, I put his tip against my entrance again and this time, when he slides into me, it feels a lot smoother."
        "Wrapping both arms and one of my legs around him, I look him in the eyes and give him an awkward nod."
        hi "Try not to lose your balance, okay?"
        ha "Y-you too."
        "He grabs hold of my leg, wraps another arm tightly around my waist and starts moving his hips, doing his best to match his movements with mine."
        "I do my best to keep up, grinding my pelvis against his every time he thrusts into me."
        hi "H-Hanako..."
        "We're moving more vigorously than usual, driven by a mutual eagerness to finish this before our leg muscles get too tired."
        ha "H-Hisao..."
        "Holding on tight with one arm, I start caressing his back and side with the other."
        hi "Ah..."
        "He tightens his grip on my leg and pulls me even closer, intensifying the sensation of our lower bodies grinding against each other."
        ha "Mmm..."
        "I start rubbing my upper body against his."
        hi "{i}*sigh*{/i}"
        "He sneaks his hand down and tickles the area between my buttocks."
        ha "{i}*gasp*{/i}"
        "I respond in kind by doing the same to him."
        hi "Hhhh..."
        "He starts kissing and licking the most sensitive part of my neck."
        ha "Nngg... mmgm..."
        "My limit is rapidly approaching. He's clearly getting close as well."
        "I push my hand in between us and use my thumb to carress the tip of his nipples."
        hi "Gggg...ahhh..."
        "He grinds against me even harder and then licks and gently nibbles my left earlobe."

        scene ev morningpractice_climax
        with charachangeev

        ha "Aaaah! I... I can't..."
        "That last bit of stimulation is too much for me, but just before the first contraction hits me, I manage to reach down and briefly stroke him just underneath the place where we're joined, dragging him over the edge along with me."

        scene ev morningpractice_climax
        with Fade(1.0, 0, 0.3, color="#FFF")
        with Pause(1.0)
        scene ev morningpractice_climax
        with mediumflash

        #"Hanako & Hisao" "Nnnnnnnggg!!!"
        "We let out an involuntary grunt in unison as jolts of pleasure surge through us and although our bodies quiver from the experience we somehow manage to remain standing."

        scene ev morningpractice_cooldown
        with charachangeev

        "When the climax and aftershocks subside, Hisao lets go of my leg and then quickly wraps both arms around me before my knees give out."
        "As the adrenaline rush dies down, I look him in the eyes. We're both out of breath and his panting is heavier than usual, but after a few moments, he still smiles and gives me a reassuring nod."
        ha "H-Hisao?"
        hi "Whew... I... I think we can afford to stay like this for a little while, Hanako. Warm-up's important, but you can't skip the cooldown lap either."
        ha "{i}*pant*{/i} Heehee. A-alright then."
        "We let out a long satisfied sigh and continue to hold onto each other, taking a moment to just bask in post-orgasmic bliss while we're trying to catch our breath."
        "While our exchange of physical affection just now was a lot less drawn-out than usual, it was arguably a lot more physically taxing as well, and I can tell we're both a little unsteady now that the heat of the moment has passed."
        "It would be a good idea to just stay like this until my upper legs stop shaking. Since Hisao appears to make no attempt to let go of me, he's probably thinking the same thing."
        ha "H-Hisao, did you... ummm..."
        hi "It was great, Hanako. I want you to know that if Emi convinces the Nurse to spike my meds as punishment for bailing out on morning practice one too many times, I'll still die a happy man after this."
        ha "Haha. You... d-didn't really skip out on morning practice. You just... ummm... p-picked a different type of exercise, with a different p-practice partner, right?"
        hi "A much cuter practice partner, yeah."
        "I blush before using one of my hands to wipe a stream of sweat from my forehead and neck."
        ha "And one who's m-much less atlethic..."
        hi "Well, that has its upsides too."
        ha "Huh?"
        "He throws me another one of his sheepish smiles."
        hi "I'd never in a million years manage a photo finish with Emi."
        ha "Pffffffff!"
        "That has to be the dorkiest thing he's said all month, but with the oxytocin still raging through my system, it just feels like the funniest thing in the world to me and I break into a giggling fit before I can stop myself."
        "Hisao just grins and continues to hold onto me while my laughter and our heart rates slowly die down."
        "What a way to start the morning."

        if _in_replay:
            return
        else:
            stop music fadeout 2.0
            stop ambient fadeout 2.0

            $ renpy.music.set_audio_filter("ambient", None)

    label .s2:

        $ set_window_tint(TINT_HANAKO)

        scene bg school_girlsdormhall
        with shorttimeskipsilent

        queue music music_normal fadein 4.0

        nvl clear
        nvl show dissolve

        n "After sneaking out of the boys' dorm, rushing back to the girls' dorm, and having a shower and a quick bite, I put my books for today in my backpack and get ready to make my way to the school building."
        n "{vspace=30}Recounting this morning's events, I quietly giggle to myself as I realize that me hurrying back to my own dorm combined with our activity earlier probably meant I might have burned more calories than Hisao this morning."
        n "I suppose it was an interesting experience, but I still prefer slow, steady, and drawn-out."

        nvl hide dissolve

        "Just when I'm about to head to the dorm's exit, I hear someone calling my name."

        show natsume basic_neutral_close at twoleft
        with charaenter

        nt "Hanako!"
        ha "Natsume."

        show natsume basic_neutral_close at center
        with charamove

        "My classmate and clubmate slowly walks up to me as I turn around to face her. I notice she's still using a crutch to get around, just like last week."

        show natsume basic_smile_close
        with chchange

        nt "Good morning."
        ha "Good morning."

        show natsume basic_neutral_close
        with chchange

        "Natsume looks past me at the rainy weather outside."
        nt "I don't think it's going to stop raining before classes start. I take it that you're not planning to sprint through it?"
        "I pulled a sprint through the rain from the boys' dorm to the girls' dorm this morning, but I'd rather not arrive in class completely winded and out of breath, so I shake my head."
        ha "I have an umbrella in my room. M-maybe it's a good idea to go and get it."
        nt "If you're heading out now, you can share mine."
        "She opens her backpack and takes a rather small folding umbrella out of it."
        ha "Oh... ah... Thanks."
        nt "It might be better if you hold the umbrella. It's a bit awkward to hold a crutch in one hand and an umbrella in the other."
        ha "Sure."
        "I take Natsume's umbrella from her and fold it open. As I do so, I notice it's moist."
        ha "You've... already been out this morning?"
        nt "Yes, for a little walk. It's difficult, but the nurse said that it's especially important to remain physically active even during the bad times."

        play ambient sfx_rain volume 0.2 fadein 1.0

        scene bg school_dormext_full_rn
        show natsume basic_neutral_close_rn at right
        show drizzle
        with charaenter

        show natsume basic_neutral_close_rn at center
        with charamove

        "We start walking, and I do my best to match Natsume's slow pace while holding the umbrella above our heads."

        scene bg school_gardens_rn
        show natsume basic_neutral_close_rn
        show drizzle
        with locationchange

        nvl clear
        nvl show dissolve

        n "Natsume's reason for attending Yamaku is because she has rheumatoid arthritis, and if Naomi is to be believed, she's had a particularly bad spell last week."
        n "I don't really have as much interaction with Natsume as I do with Naomi, but she, Naomi, and I usually join up these days whenever we're required to work in groups of three, and we also have to work on stuff together during our activities at the newspaper club from time to time."
        n "All in all, even though we're not extremely close we still get along pretty well."

        nvl hide dissolve

        ha "How... ah... is your arthritis today?"

        show natsume basic_serious_close_rn
        with chchange

        nt "A little better than last week, though maybe that's just because I've had a higher dose of medication over the last few days. I think I'll manage as long as it doesn't get any worse. If it does, however, I'll be in big trouble."
        ha "Because of the upcoming National Center Test for University Admissions?"

        show natsume basic_sad_close_rn
        with chchange

        nt "Yes. I can't cram if I'm in constant pain, but I won't be able to study if I'm completely drugged up on painkillers, either."
        ha "I'm... sure you'll do fine. You've always had very good grades in class."

        show natsume hands_neutral_close_rn
        with charachangealways

        pause 0.5

        show natsume hands_smile_close_rn
        with charachangealways

        "Natsume gives me a surprised look for a second or two, but then catches herself and smiles."
        nt "Thanks."
        ha "I-is something wrong?"

        "She shakes her head and smiles again."

        show natsume basic_cheerful_close_rn
        with chchange

        nt "It's nothing. I never realized you paid attention to my grades. I sometimes just forget that we've spent nearly three years in the same class already. Sorry."
        "I get where she's coming from. Until last July I wasn't really that much of a classmate to Naomi and Natsume, but more someone who was present in class without really being part of it. Like a phantom of some sort."
        "Looking back, I feel a sense of regret that it's taken me this long to start opening up to my neighbors in class."
        ha "It's okay."

        scene bg school_courtyard_rn
        show natsume basic_neutral_close_rn
        show drizzle
        with locationchange

        "Natsume nods, and her smile slowly disappears again."
        nt "Good grades aren't really enough though. More important is the upcoming National Center Test. From what I've seen of it, they call the preceeding period ‘examination hell’ for a reason."
        ha "From what you've seen?"

        show natsume basic_serious_close_rn
        with chchange

        nt "I have an older cousin who went through this thing four years ago. He eventually made it into the university he wanted to attend, but near the end he was really hanging on for dear life."
        nt "He was, like, sleeping only a few hours a day, and he lost several kilos of weight in the process. He was afraid that if he slept more than four hours, he was guaranteed to fail the tests. My aunt said he looked like a zombie by the time the exams started."
        ha "That sounds... really excessive."
        nt "Well, we are competing on a national scale, you know?"
        ha "I guess... all we can do is our best."
        "It probably helps that while I'm aiming for a good university, I'm not trying to get into the really famous ones like Tokyo University or Kyoto University, which are usually restricted to the cream of the national crop."
        nt "I guess you're right."

        stop ambient fadeout 1.0

        scene bg school_lobby
        show natsume hands_neutral_close
        with charaenter

        "We reach the school building, and I shake the raindrops off Natsume's umbrella before folding it up again and giving it back to her."
        nt "Thanks. By the way... Were you away from the school grounds yesterday?"
        ha "Huh?"

        show natsume basic_neutral_close at center
        with chchange

        nt "Naomi wanted to stop by your room yesterday, and she went there several times over the course of the day, but she said that neither you nor Satou answered her knocking."
        ha "Lilly spends most of her Sundays at her parents' home since they moved back here, and Hisao and I went on a d-date yesterday that lasted for most of the day."
        "We decided that yesterday was going to be the last date we'd go on until the exams are over, so we took our time and spent most of the day away from Yamaku."
        nt "Oh, okay. Well, I'm sure we'll hear what it's about when she gets to class this morning."

        scene bg school_hallway2
        show natsume basic_neutral_close at center
        with charaenter

        ha "She didn't tell you already?"
        nt "No, she said she wanted to tell you first. So if I had to make a guess, I'd say that it's related to that unofficial writing club the three of you started."
        ha "The Broken Quills?"
        "Natsume rolls her eyes at the name that Naomi came up with for our club, but then nods."
        nt "Yes. Naomi said I didn't need to wait for her this morning. It's possible she's somewhere around here telling Jun about it as we speak."
        ha "I'm a little curious now."
        nt "It's probably something good. We spent most of yesterday studying together, and there were several moments where she'd start grinning like a loon completely out of the blue. Still wouldn't tell me what was going through her mind."

        scene bg school_scienceroom
        with locationchange

        "We make it to the classroom, and I take a quick peek inside before entering."

        show hisao basic_neutral_uni at left
        with charaenter

        "I notice Naomi's not here yet, but Hisao is, and he already seems absorbed in one of his study books."

        show hisao basic_bashful_uni_close at twoleft
        with chchange

        "I quietly walk up to him, whisper a quick “hey”, and then quickly move to my own seat while hoping that nobody caught the knowing look we shared."

        hide hisao
        with charaexit

        "I take out my books, but before I start studying, my thoughts return to this morning's earlier events."
        "Before today, my way of taking the initiative was simply dropping a hint or two and then leaving things up to him, only taking the active role if he asked me to."
        "Today has been the first time that I've actively seduced him. I wonder what he thinks of me now that the adrenaline rush has settled down."
        "Did I act inappropriately? As fun as it was, I do feel a little embarrassed about it in hindsight."

        stop music

        play sound sfx_impact2

        show naomi basic_grin at offscreenright
        with None

        show naomi basic_grin at right
        with MoveTransition(0.2, time_warp=_warper.easein)

        na "There you are!"

        play music music_comedy fadein 4.0

        "My gaze jumps from my study books to the doorway, and I see my friend with the bleached blonde hair standing there sporting the biggest grin I've ever seen in my life. Natsume wasn't kidding when she said Naomi was in high spirits."
        "I'd probably be happy for her if her attention wasn't focused directly on me right now. As it is, I'm feeling very uncomfortable."

        show naomi bend_grin
        with Dissolve(0.2)

        show naomi at center
        with charamovefastest

        show naomi bend_grin_close
        with characlose

        na "Guess what? Guess what?"

        play ambient sfx_crowd_indoors

        show crowd behind naomi
        with charaenter

        "Naomi, without breaking stride, walks right up to me, and I'm completely aware of the fact that all the students who already made it to class are looking at us right now."
        "I instinctively get up and back away. Naomi, however, seems too excited to notice."
        ha "W-what?"

        show naomi bend_laugh_close
        with chchange

        na "We totally rock!"

        show naomi bend_laugh_superclose
        with characlose

        na "Mwah!"

        show naomi basic_smile_close
        with charadistant

        ha "Eek!"
        "I yelp in surprise as my upbeat neighbor steps forward and lands a big wet smacker on my left cheek. My face instantly turns bright red, and my classmates' gazes, which were aimed at the two of us until just now, are now all directed squarely at me."
        "Feeling like a deer in the headlights, I back away until I'm pressed against the wall."

        show naomi basic_smile
        with charadistant

        ha "Ah... I... ummm..."

        show hisao basic_frown_uni at left
        show naomi basic_confused
        with charaenter

        hi "Hey Inoue!"
        "Just when I'm about to consider making a break for it, the annoyed voice of my boyfriend cuts through the murmur."
        hi "Why don't you go and get yourself a girlfriend of your own instead of hitting on somebody else's?"

        show naomi basic_tongue
        with chchange

        "I'm not sure if this remark was intended to divert attention away from me or if he's simply voicing his annoyance with Naomi's behavior, but regardless of the intention, the class bursts into laughter and people focus back on Naomi, who grins sheepishly and sticks her tongue out at Hisao."
        na "Is that jealousy I smell, Nakai?"

        show natsume basic_annoy at tworightsit behind naomi
        with charaenter

        "Natsume groans and gives Naomi a hard poke in the ribs with the handhold of her crutch."
        nt "Stop being such a bonehead. What's this all about, and why is it necessary to make such a spectacle out of it?"

        show naomi basic_grinclosed
        with chchange

        "Naomi excitedly smiles at her best friend and produces a piece of paper from her handbag."

        show naomi bend_wink
        with Dissolve(0.2)

        show naomi at right
        with charamovefastest

        show natsume basic_neutral
        with chchange

        na "Tadaah! Check this out!"

        show natsume:
            "natsume hands_neutral" with charachangealways
        with None

        show naomi bend_laugh
        with Dissolve(0.2)

        show naomi at center
        with charamovefastest
        
        show naomi bend_laugh_close
        with Dissolve(0.2)

        "Natsume leans forward to read the paper Naomi's holding, but before her eyesight can focus, Naomi turns and presses it into my hands."
        na "Oh, right! You read it first, Hanako!"

        show natsume basic_neutral
        with chchange

        "Still feeling a little nervous, I take the piece of paper from Naomi and attempt to read it without letting my classmates' stares get to me."
        "Despite my frantically beating heart and nervousness, I manage to keep myself together long enough to read the piece of paper."
        "It turns out to be a certificate. I let out a surprised cry as I realize what it means."
        ha "Oh!"

        show hisao basic_speak_uni
        with chchange

        "A proud smile appears on my face for a moment, and Hisao's previously annoyed frown gives way to a curious expression as he notices this."
        hi "What is it, Hanako?"
        ha "Umm... W-we won something in one of the writing contests we signed up for."

        show hisao basic_smile_uni
        with chchange

        hi "Really?"

        show hisao basic_smile_uni_close
        show naomi bend_smile
        with charadistant

        "He walks up to me, and I hand him the certificate."
        hi "It says here that your contribution made third place in the writing competition for high school students organized by a section of the Letters Faculty at Osaka University. The prize money is a sum of 20,000 yen."

        show naomi basic_laugh
        with chchange

        "Naomi once again gives an excited thumbs-up."
        na "Isn't it awesome?"
        "Takashi Maeda, who sits in front of me in class, gives Naomi a grumpy glare."
        "Takashi" "You raised all this ruckus for third place?"

        show naomi basic_annoy
        with chchange

        "Naomi narrows her eyes and shoots a withering look of her own right back at her classmate."
        na "Tell me Maeda, how many contests have you participated in? Ever won anything? Have your artistic talents already been recognized by people in the field? Holding expositions already?"

        show natsume hands_cheerful at tworight:
            xpos 0.65
        show naomi basic_neutral
        with charachangealways

        "Natsume rolls her eyes, gets up, and puts a hand on her best friend's shoulder."
        nt "Alright, relax already. You could have been more subtle about this whole thing, but I think it's a great achievement for both of you."
        nt "I mean, it's not like you girls have had years of experience, right? I really am impressed."

        show naomi basic_smileclosed
        with chchange

        "Naomi beams at her friend's words."
        na "That's kind of what Hoshino said. He reminded me that there were close to 200 participants, so in the end we still did well."

        show natsume hands_smile
        show hisao basic_smileclosed_uni_close
        with chchange

        "Hisao gives me a proud look."
        hi "I'd love to hear more about that, but..."

        stop ambient fadeout 3.0

        show muto normal at right behind natsume
        show hisao basic_smile_uni_close
        show naomi basic_smile
        hide crowd
        with charaenter

        "He looks at the doorway, and we notice that Mutou has just arrived in class."
        hi "...it looks like it'll have to wait."

        stop music fadeout 2.0

        scene bg school_scienceroom
        show muto normal at tworight
        with shorttimeskip

        queue music music_daily fadein 4.0

        mu "...and I don't think I need to stress the importance of being well-prepared for the next week. You are all free to spend this hour and the afternoon studying for whatever subject you believe will need the most attention. Be sure to make the most of the time you still have."
        "I can hear a few soft sighs. Mutou isn't really telling anyone anything new, but I suppose it's part of his job to keep harping on this."

        nvl clear
        nvl show dissolve

        n "Somewhere around the middle of next week, we'll have mock exams. They're the closest thing to a dress rehearsal for the National Center Test we'll be taking in January that we're going to get."
        n "Like the real ones, they'll be held over the course of two days. Even though the results officially don't matter, students who underperform will be expected to take part in a heavy dose of supplementary lessons until mid-January to catch up in the subjects they did badly in."
        n "That alone seems to be a good motivator for everyone to study as hard as they can in order to get a good grade next week."

        nvl hide dissolve

        mu "If you want to study in small groups, that's fine as well."
        "I can distantly hear Misha asking Hisao to explain a math problem to her, so I open my own study book without waiting for my boyfriend to join me."

        hide muto
        with charaexit

        show natsume basic_smile at tworight
        show naomi basic_smile at right
        with charaenter

        "As I resume reading through the chapter I started on earlier this morning, I hear Natsume whisper to her best friend."
        nt "So, what was your winning story about?"

        show naomi bend_grin
        with chchange

        na "Hehehe, no more rolling your eyes this time? I see you're finally starting to take The Broken Quills seriously. Better late than never."

        show natsume hands_neutral
        with chchange

        "Natsume sighs impatiently."
        nt "Very well... Hanako?"

        show naomi bend_grinclosed
        show natsume hands_cheerful
        with chchange

        "I look up from my work to see Natsume smile playfully at me."
        ha "Ah. Yes?"
        nt "Can you help me with this chapter here?"
        ha "Uh? Ummm... Sure."

        show natsume hands_smile
        with chchange

        show natsume at twoleft
        with charamove

        show natsume hands_smile_close
        with charaenter

        "Natsume moves her chair next to mine and sits down at my desk."

        show natsume basic_cheerful_close
        with chchange

        nt "So, about that story of yours..."

        show naomi basic_shock
        with chchange

        "Naomi gives her friend a mock-offended look."
        na "Hey, don't ignore me like that. I was going to tell you already."

        show naomi basic_smile
        with chchange

        show naomi at tworight
        with charamove

        show natsume basic_smile_close
        show naomi basic_smile_close
        with charaenter

        "She takes her own chair and joins us at my desk before nodding at me to indicate it's okay for me to tell Natsume what she wants to know."
        ha "Ummm... The name of the story is ‘The Missing Star’. It's about a blind student who joins his school's astronomy club. It's... a short story we submitted for that particular contest."

        show natsume hands_smile_close
        with chchange

        nt "A blind student, huh? Based on somebody we know?"
        ha "Not really, although we did ask Hideki for some input."

        show natsume hands_cheerful_close
        with chchange

        nt "That's pretty neat. So, do you two literally write such a story together? Or do you write stories on your own and share the credit?"
        ha "They're all... team efforts."

        show natsume basic_smile_close
        show naomi bend_smile_close
        with chchange

        na "We kinda work like this: one person submits a proposal or a rough draft and the other fills in the blanks for a bit before handing it back. We then switch it back and forth once or twice more, each time refining it a bit more before letting Jun give it a final check for errors or plotholes."

        show naomi bend_wink_close
        with chchange

        na "We have a couple of rules in place. No scrapping the other person's ideas, merely refining them, or asking them to be reconsidered. No new ideas after the story's been switched back and forth once. And no mechas, zombies, ninjas, pirates, or characters belonging to existing works."
        "Natsume grins."
        nt "You've really been restraining yourself."

        show naomi basic_smile_close
        with chchange

        "I was pleasantly surprised about that as well. Jun insisted on the zombie-ninja-pirate-mecha rule because she was worried that Naomi would spend all our meetings coming up with inane and clichéd ideas, but it turned out that a lot of her proposals were remarkably sensible."
        ha "Naomi's really put forth a lot of good ideas. Most of the ideas we ended up using were hers."

        show naomi bend_laugh_close
        with chchange

        na "Aw, everyone has ideas. Making something workable out of them is another thing altogether and Hanako's got a real knack for that."

        show natsume hands_cheerful_close
        with chchange

        "Natsume smiles at our little exchange of praise."

        show naomi basic_smile_close
        show natsume basic_smile_close
        with chchange

        nt "Sounds like you girls really grew into your roles. You may be a natural team. It's nice to see your efforts paid off. But have you actually turned a profit? Those contests need entry fees to pay for the prizes, don't they? And I recall that you signed up for several over the last few months."

        show naomi basic_grinclosed_close
        with chchange

        na "Well, Hoshino secured a small budget to pay for part of it and we got ourselves a sponsor for the rest."

        show natsume basic_neutral_close
        with chchange

        nt "A sponsor?"
        "I nod."

        show naomi bend_smile_close
        with chchange

        ha "Lilly's mother spoke to us before our second meeting, and she agreed t-to sponsor us as long as we didn't go overboard."

        show natsume hands_smile_close
        with chchange

        nt "Wow, that's really generous of her."

        show naomi bend_laugh_close
        with chchange

        "Naomi enthusiastically nods."
        na "Yeah, she's a really awesome person."

        show natsume basic_evil_close
        with chchange

        "Natsume giggles and gives her best friend an evil smile."
        nt "And a really smart investor as well. Since she's paid nearly all of your entry fees, she's probably entitled to nearly all of your winnings too."

        show naomi basic_shock_close
        with chchange

        na "B-b-b-b-but....!"

        "I just barely manage to hold back a giggle myself at Naomi's mortified expression. I don't think that Karla's even a tiny bit interested in our prize money. Our winnings are probably little more than pocket change to her."

        show natsume basic_smile_close
        with chchange

        ha "Hmmm... We should probably tell her that we won something... and offer her a share. I don't think she'll accept it. Lilly's family is... not poor. But it's the p-polite thing to do."

        show naomi basic_smile_close
        with chchange

        "Naomi sighs and then nods."
        na "I guess we should. Could you call or mail her about it?"
        ha "Sure. I'll send her an e-mail this lunch break."

        show naomi basic_smileclosed_close
        with chchange

        na "Great. Be sure to thank her again from us."
        ha "Okay."

        show natsume hands_smile_close
        with chchange

        "Natsume gently nudges Naomi's side to get her attention."
        nt "So, assuming your sponsor rejects her share, what do you intend to do with the spoils? And who is going to get to keep the certificate?"

        show naomi basic_focus_close
        with chchange

        na "Hmmm..."
        "Naomi takes a moment to think about that."
        na "I guess we could draw straws to determine who gets to keep the certificate. Or maybe we could pass it from one member to the other every week. Or maybe..."

        show naomi bend_smile_close
        with chchange

        "Her face suddenly lights up, and a smile appears on her face as she holds out the certificate to me."
        na "...we could simply let Hanako have it."
        ha "M-me? But why me?"

        show naomi bend_wink_close
        with chchange

        na "Jun and I have plenty of posters hanging on the walls of our rooms and lots of other decorations as well. It'll stand out more in your room, and while you're studying, you can look at it as a reminder that we can do anything if we put our mind to it!"
        "I think she's trying to say that my room's the one most in need of additional decorations, and I might be the one most in need of motivational means to stay positive. I could be wrong though. It's not really like Naomi to be this diplomatic."
        "Still, the hint about my room's atmosphere aside, it's a pretty sweet gesture."
        ha "Ah..."

        show naomi bend_smile_close
        with chchange

        na "Go ahead, take it. Just don't forget it belongs to all three of us."
        ha "Well... Okay then. But... I'll just k-keep it safe on behalf of our club."

        na "Works for me. Now about our prize money, do you have any idea what to do with your share?"
        "Not really. Hisao and I went on our last date before the exams yesterday, and I'm not sure if my share will be enough to treat him anyway."
        ha "No."

        show naomi basic_smile_close
        with chchange

        na "Are you coming to our little get-together on Friday?"

        "I'm not sure yet. The newspaper club always goes to a little coffee shop in town to hang out after a new issue has been printed. I've been avoiding those outings up until now, due to my difficulty in socializing with my fellow clubmembers."
        "But Naomi's never stopped inviting me, and now that I've gotten slightly more familiar with the various people in the club, coming along with her is slowly starting to lose its intimidation factor."
        ha "I'm... not sure yet."

        show natsume basic_neutral_close
        show naomi basic_neutral_close
        with chchange

        na "It's the last outing we'll have. That makes it kind of special. Also..."
        "That's a good point. After this week's release, Naomi, Natsume, Hideki, and I will be officially putting our club membership on hold in order to focus completely on our exams."

        show natsume basic_smile_close
        show naomi basic_smile_close
        with chchange

        na "...we'll be taking a group photo that afternoon, and it just wouldn't feel right if some of the members weren't there."
        "I guess I could give it a try this once. I don't want the other members to regard me as a spoilsport either."
        ha "...I'll c-come along this time then."

        show natsume hands_cheerful_close
        show naomi bend_laugh_close
        with chchange

        na "Awesomesauce!!! It's a date! Friday afternoon after we finish printing! Don't forget! And afterwards..."

        $ sh_mus_file = renpy.music.get_playing()
        $ sh_mus_pos = renpy.music.get_pos()

        stop music fadeout 0.5

        show natsume basic_neutral_close
        show naomi basic_confused_close
        with { "master": chchangefast }

        mu "Inoue!"

        hide natsume
        hide naomi
        show muto irritated at right
        show shizu cross_angry at center
        show misha cross_frown at twoleft
        show hisao cross_grin_uni at left:
            xpos -0.06
        with charachangealways

        "We look up from our books and notice that Mutou is staring at Naomi, along with half of the class."
        "Seems like Naomi delivered her last statements a little bit too loudly. Natsume exasperatedly shakes her head, and Mutou gives Naomi an admonishing glare."

        hide shizu
        hide misha
        hide hisao
        show muto at center
        show naomi bend_grinclosed_close at right
        with charaexit

        mu "It didn't sound like you were discussing any subject matter just now."

        show naomi basic_laugh_close
        with chchange

        na "Sorry teacher. We just had to make an arrangement for our club's group photo, and I suddenly wondered..."
        mu "Is this relevant to this class's homeroom session?"

        show naomi basic_smile_close
        with chchange

        na "...since homeroom classes will be replaced with cramming sessions after next week, would this week be a good opportunity to have a class photo taken?"

        show muto normal
        with chchange

        play music f"<from {sh_mus_pos}>{sh_mus_file}" fadein 4.0

        "Mutou looks puzzled."
        mu "Is something wrong with the class photo that was taken at the start of the school year?"

        show naomi bend_grin_close
        with chchange

        na "Well, not every student in this class is in that one. Maybe it's worth taking another one."
        mu "Hmmm..."
        "I can see Mutou's eyes shift briefly to my boyfriend. I can tell that he's not fond of the idea of having his star pupil missing from the class photo that'll probably appear in the yearbook."

        show naomi basic_smile_close
        with chchange

        mu "...seeing that every pupil of this class is currently present, are there any objections to having a photo taken this afternoon?"
        "No reactions. I presume that that's a silent approval."

        show muto smile
        with chchange

        mu "We'll reserve some time in the afternoon for it, then."

        stop music fadeout 2.0

        if _in_replay:
            return

    label .s3:

        $ set_window_tint(TINT_HANAKO)

        scene bg school_scienceroom
        show muto smile at right
        with shorttimeskip

        queue music music_dreamy fadein 4.0

        mu "Thank you, Kawana. You can tell your friend that he took a good picture."
        "Mutou nods at Misaki who came to show him a copy of the class photo she printed out. About 20 minutes ago, we took the class photo Naomi proposed this morning."
        "Misaki Kawana, the girl who sits in front of Natsume during class and who is a member of the photography club, took a friend from her club along who was willing to operate the camera and quickly dropped by the copyshop afterwards to print out a preview for our teacher."
        "Misaki" "Should we send the picture to the student council, teacher?"

        show muto normal
        with chchange

        mu "Yes, they're the ones who'll be in charge of the tasking people to put the yearbooks together."
        "Misaki" "We'll do that then. Have a nice day, sir."
        "Misaki makes a stiff bow and leaves the room. Now it's just Mutou and me."
        "After the photo shoot, Mutou approached me and asked if he could speak to me after class. I wonder what it's about. I really hope it's nothing bad."

        show muto smile_close at center
        with characlose

        mu "Go ahead and take a look."
        "He hands me the printout, and I look it over."

        show newclassphoto at displayitemshow

        "A smile appears on my face. I think it looks pretty good. I'm standing next to Hisao of course, and I'm turned slightly towards him so my right side is less visible."

        show newclassphoto at displayitem

        "We're standing fairly close to each other, so I'd like to think that people who pay close attention to the photo can deduce that we're a couple. Then again, this might just be wishful thinking on my part."
        mu "It appears you approve of it."

        show newclassphoto at displayitemhide

        "My gaze shifts back to Mutou, who appears to have been observing me while I was looking at the picture."

        hide newclassphoto

        ha "It's a... nice photo, I think."

        show muto normal
        with chchange

        "Mutou nods and takes the printout back."
        mu "If I recall correctly, this is the first time you've taken part in this sort of thing."
        "I nod."
        ha "I've been... thinking l-lately that... maybe... it's okay if people... look back on that photo in the yearbook and remember... that I was part of this class too."

        show muto smile
        with chchange

        mu "I think that would be more than fine and not just with me. I suspect that you were the reason for Inoue to make that suggestion about having another photo taken and not Nakai."
        ha "P-probably."

        show muto eyebrow
        with chchange

        "He smirks."
        mu "I must admit that I find you and Inoue an odd pairing."
        "I've heard that before. And in truth, I do still have difficulty dealing with Naomi's occasional antics from time to time, like that smacking kiss earlier this morning."
        "And yet for each impulsive thing she does, there's usually another sweet and kind action to make up for it, like lending me that camera for my vacation or suggesting that class photo to Mutou."
        "I also learned from Natsume that part of Naomi's restlessness is a mild side effect of the medication she's taking, so I do my best to take Naomi's personality quirks in stride and focus on the good parts."
        ha "She can be... quirky, but she means really well."

        show muto normal
        with chchange

        "Mutou nods curtly."
        mu "It's good to see you making some more friends. How are you doing these days? In a general sense, that is."

        nvl clear
        nvl show dissolve

        n "The last few months have been very good to me. Not only am I still in a relationship with Hisao and greatly enjoying the time we spend together, I've also managed to strengthen my friendship with Lilly."
        n "{vspace=30}I was initially worried that Lilly and I would start drifting apart now that her parents are living in Japan again. We do see each other slightly less often now that Lilly spends each Sunday at her parents' home and I attend meetings of the writing club several evenings per week."
        n "But while Lilly keeps the Sundays open for her parents, she keeps the Saturdays open for me, and over the last few months we've gone on several “girl dates” together, just like the ones I took her on when she was still in the process of deciding whether to move to Scotland or not."

        nvl clear

        n "In addition, I've started to enjoy the little meetings of our writing club, and even when we don't end up writing a lot, I still feel it was at least good hanging out. I never really talk a lot during those sessions, but they're still rather fun to attend."
        n "I'm slowly warming up to my fellow newspaper club members, too, and we recently started exchanging greetings whenever we run into one another in the hallways."
        n "{vspace=90}After nearly three years, I'm slowly starting to become part of this school and its student body, and I've found myself feeling sincerely sorry that it'll all end at the start of next spring."
        # foreshadowing is a literary device...
        n "I never expected to ever feel this way again after my accident, but surprisingly enough, I'm feeling rather happy with my life right now."

        nvl hide dissolve

        ha "I'm doing... fairly well... at the moment."
        "Mutou waits for a moment to give me the chance to say more, but when I remain silent, he continues."

        show muto smile
        with chchange

        mu "Your Japanese teacher informed me of the prize you and Inoue won. He was quite pleased. He said you have potential."
        "I blush a bit. Seems like news spreads quite quickly around here."

        show muto normal
        with chchange

        mu "Of course, potential in itself is hardly enough to land a good job. A good education will be vital in order to build on and refine that potential. I heard that you've been considering your options and that you've picked two universities to potentially attend."
        "I meekly nod. Naomi and I both plan to study Journalism and Media after graduation. Mister Hoshino said that he was certain that we'd get plenty of opportunities there to take creative writing courses if we were interested."

        show muto eyebrow
        with chchange

        mu "He looked through your application forms and was puzzled by what he saw. Your first choice of university is Kasshoku University, a large and well-regarded university."
        mu "But your second choice is a school that most students of your capabilities wouldn't consider unless they had no other options. He wanted me to present you a list of alternatives he deemed more fitting to your level."
        ha "Ummm...."
        mu "I looked at your picks myself, and I picked something up that I believe Hoshino overlooked. Both schools of your choice are located in Chiba. And that happens to be the very city Nakai's school of choice is located in."
        mu "In fact, you two are aiming to attend the same university after graduation, although you're shooting for different faculties."

        nvl clear
        nvl show dissolve

        n "Looks like he found me out. I embarrassedly nod my head."
        n "{vspace=60}Hisao was the first person to take interest in Kasshoku, and while its science program is supposedly well-regarded, this choice was also one of practicality as the university is located in the same city his parental home is located in, meaning he can move back in with his parents to cut down on living costs."
        n "Lilly and I looked up the university as well and found that it'd also be able to suit our educational needs, so we both decided to try and get in there as well. Neither Hisao nor Lilly has put forth a second option, but since both are really good at the subject they'll be studying, I don't think they'll have that much trouble making it in as long as they can pass the national test."

        nvl hide dissolve

        mu "If you make it into the same university as he does, there won't be a problem, but if you end up going to that second school you're planning to apply for, I believe you'll be doing yourself a serious disservice."
        ha "Ummm..."

        show muto normal
        with chchange

        mu "As your homeroom teacher, I can understand your reasoning here. But as a teacher, I still feel compelled to point out that the choice of whether and where to continue studying after high school is one of the most important decisions of one's life."
        mu "It's a decision with very long-term consequences. More so than anything else right now."

        nvl clear
        nvl show dissolve

        n "I'm getting a vague feeling of what he's trying to say without actually saying it."
        n "{vspace=60}{i}I'm in a relationship right now, but not every high school relationship lasts all the way until marriage.{/i}"
        n "{vspace=60}I don't want to think about it too deeply, but what if I picked a university of lower calibre so I could stay around Hisao and he ends up breaking up with me at some point?"
        n "But if I went off to study in another city, would our relationship even last? I'm not so sure how well either of us would do in a long distance relationship."

        nvl hide dissolve

        show muto eyebrow
        with chchange

        mu "Think of it this way, Ikezawa. The decision of many companies to hire you will depend for a large part on whether you've attended a reputable university. The other factor involves interviewing skills."
        mu "As it is, someone else may be better at sweet-talking his way through a job interview, but if you have better credentials than the competition, you'll still have a good chance of being hired. You should see this as an opportunity to even the odds in your favor."
        mu "Here at this school we make it a point to push all our students to try for the very best universities they can possibly get into in order to compensate for possible disadvantages they might have on the job market later."
        mu "It is always better to attend a reputable university and appear slightly overqualified for the job of your choice later than to be passed up again and again."
        "That's not a bad point. One of the selling points of attending a prestigious university used to be that it came with an almost guaranteed job offer afterwards. That's not really the case any longer, but the name of one's university still carries an extreme amount of weight."
        "And if there's one thing I don’t have faith in, it's my ability to not bungle up a job interview, so I guess I really don't have much choice except to try and compensate in the credentials department as much as I can."
        ha "So... Another alternative option then?"

        show muto normal
        with chchange

        mu "If you're going to pick alternatives, then they should at least be serious considerations. They'll have additional entrance exams, but you'll be studying the same material for all the ones you partake in, so it shouldn't cost you extra time to prepare."
        mu "I have a few pamphlets in my desk, so if you have time, we can go over them and get this out of the way before the afternoon is over. I know of a few universities that hold entrance exams on a day you won't already be taking one."
        ha "O-okay then."

        show muto smile
        with chchange

        "He gives me an awkward smile that is meant to be reassuring, but I think his smile is a bit weird. If anything, it makes me slightly nervous."
        mu "It's good to keep in mind that if everything goes well, your second choice won't matter much in practice. Hoshino believes you have what it takes to make it in as long as you study hard enough, and I have no reason to doubt his assessment."
        mu "Your grades have really picked up over the last few months—particularly your Japanese. I wonder if that's because of your social life is improving or if it's simply because you seem to have a clear idea of what you want after you graduate here."
        ha "M-maybe both. But... it also helped that I have one tutor who wants to b-become an English teacher and another who is planning to teach science."
        "A proud expression appears on my homeroom teacher's face."
        mu "So... Nakai has made a definite decision?"
        ha "For now..."

        nvl clear
        nvl show dissolve

        n "Lilly's opinions about teaching may have influenced him to some degree, but the deciding factor has undoubtedly been the fact that he's already been acting as a science teacher to some degree over the last several months. Not just to Lilly and me, but also to his fellow clubmates."
        n "The science club currently counts eight members, which is quite impressive considering the fact that it was just Hisao, Mutou, and Kenji before the summer break. The majority of the new members are junior students since most third years at this school have either already joined a club or have no intention of becoming part of one regardless of what it is about."
        n "As club president and Mutou's star pupil, Hisao's dutifully taken it upon himself to help his fellow club members out whenever a subject gave them trouble. He usually did these tutoring sessions during club hours, but there were also times when he'd drop by a member's room to help them get a better grasp on the material."

        nvl clear

        n "Lilly and I were very impressed when we learned how serious Hisao was taking this task, sometimes even dropping by the computer lab or library to read up on a subject some more in order to better help his fellow club members. That was also the time when Lilly first started putting the idea of teaching science as a career into Hisao's head."
        n "And despite the fact that Hisao first took to his new activities in an attempt to compensate for his mentor's confusing lectures, Mutou seems to have taken Hisao's career aspirations as a personal compliment and has been all too happy to encourage his protegee's plans for the future."

        nvl hide dissolve

        mu "Too many students simply go to university because they feel that it's expected of them, not because they want to develop themselves and hone their specific interests into talent."
        mu "But the best students know that passion, ambition, and a clear goal give all their efforts meaning and are a better source of motivation than a mere desire to go with the flow of society."
        "I really managed to get him going. I don't think this is really meant to be a discussion, so I obediently nod my head."

        show muto normal
        with chchange

        mu "Speaking of motivation, have the two of you considered visiting the open house day this weekend?"
        ha "Open house day...?"

        show muto eyebrow
        with chchange

        "He probably said something about it, but I'm not exactly sure when. Was it this morning while Natsume was interrogating Naomi and me?"
        "Mutou sees the blank expression on my face and shakes his head."
        mu "I brought it up during homeroom classes two weeks ago. Kasshoku University is organizing an open house day for high school students who are thinking about enrolling there."
        mu "They're probably hoping to get a few more last-minute applications before the Center Test starts in January. The event takes place this upcoming Sunday."
        "Now I remember. Hisao and I did take note of that, but never made an actual decision on whether to go or not."
        ha "We're... not sure yet."

        show muto normal
        with chchange

        mu "If you're serious about enrolling there, being able to take a brief look around and get a feel for the place may just provide you with an additional boost of motivation. You will both need to study hard to pass your exams, and every bit of motivation should be welcomed."
        ha "We'll... consider it."

        show muto smile
        with chchange

        mu "Very well. Let's look at some of your alternative options then and hope it will turn out to be nothing but a formality."

        if _in_replay:
            return
        else:
            stop music fadeout 2.0

    label .s4:

        $ set_window_tint(TINT_HANAKO)

        scene bg school_dormlilly
        show lilly basic_surprised_paj_close at tworight
        show hisao basic_neutral_uni at left
        with shorttimeskip

        queue music music_lilly fadein 4.0

        li "You're considering attending a university in another town if you don't get into Kasshoku?"
        "Lilly and Hisao seem surprised as I tell them about the talk I had with Mutou."
        ha "Well... M-my first choice hasn't changed, but Mutou said that I shouldn't underestimate the importance of getting into a good university."

        nvl clear
        nvl show dissolve

        n "I'm not exactly standing 100\% behind my decision, but when Mutou made his point, I didn't really have a solid argument against it. Besides, with some luck, I'll do well on my exams and I won't have to worry about alternatives."
        n "{vspace=60}Unlike Hisao and Lilly, however, I do feel that I need alternatives. After all, if I don't get into some university or another, I'll be homeless after graduation. I'm trying not to worry too hard about that for the time being, knowing I could probably stay with my friends for a while, but it's not a matter I can easily ignore."
        n "I looked up what renting a place would require, and it seems most estate agencies demand a tenant to have both a steady job and a family member willing to act as a guarantor in case of a layoff."
        n "I don't qualify for either criterium. And then there's the high costs..."

        nvl hide dissolve

        show lilly basic_smileclosed_paj_close
        show hisao cross_speak_uni
        with chchange

        hi "I suppose that is a good point. What university you attended still matters greatly to many companies."

        show hisao basic_neutral_uni
        show lilly basic_displeased_paj_close
        with chchange

        nvl clear
        nvl show dissolve

        n "With the conversation dried up, we get back to studying."
        n "{vspace=60}The last months, Lilly, Hisao, and I have made it a habit to study together so we can compare notes, help each other on difficult subjects, and keep each other motivated."
        n "I was worried at first that we'd just end up chattering all night long, but it turned out that we've been able to exercise enough self-restraint to make these cramming sessions productive. Lilly and I are sitting on Lilly's bed, our backs against the wall, while Hisao's sitting at Lilly's desk."

        nvl hide dissolve

        show lilly basic_sleepy_paj_close
        with chchange

        "As I finish another chapter about the late Edo period, I hear Lilly sigh softly and shake her fingers."
        ha "Are your fingers getting tired?"

        show lilly basic_weaksmile_paj_close
        with chchange

        li "A little bit. How long have we been studying since our last tea break?"

        show hisao cross_speak_uni
        with chchange

        "Hisao instinctively looks at Lilly's braille alarm clock before rolling his eyes and checking his watch."
        hi "About an hour. Maybe another short break is in order."

        show lilly basic_smileclosed_paj_close
        show hisao basic_smile_uni
        with chchange

        li "Very well then. But let's continue within 15 minutes."
        "Hisao gets up and gets us both a cup of tea from the thermos bottle we've been using during these studying sessions to keep our drinks warm. I take a sip from my cup, being careful not to spill anything on my nightgown, and turn to Lilly."
        ha "Your mother already replied to the mail I sent during the lunch break."

        show lilly basic_smile_paj_close
        with chchange

        li "About your prize? What did she say?"
        ha "She said she was very proud of us and that we didn't need to worry about splitting the prize money with her."

        show lilly basic_planned_paj_close
        with chchange

        li "I wouldn't have expected any other reaction from her. Do you already have any idea what to do with your share?"
        "I nod."

        show lilly basic_smile_paj_close
        with chchange

        ha "We're not splitting the money. Naomi said that since we've earned the money as a team, we should also spend the money as a team."
        li "So what will you be spending it on?"
        ha "A... ‘girls night out’... as Naomi called it."
        ha "The next issue of our newspaper comes out the upcoming Friday, so our club members go to a coffee shop in town to celebrate the release as usual. Naomi, Jun and I will go there too, but leave early and take a bus to the city."
        ha "We're going to look for a nice p-place to have dinner and then do k-karaoke afterwards. Whether we do anything else depends on how much of the prize money we'll have left."

        show lilly basic_satisfied_paj_close
        show hisao cross_smile_uni
        with chchange

        hi "Wow Hanako, that sounds like a lot of fun."
        "I think it does. I still prefer the quietness of the nearby town over the bustling of the city, but things will probably be okay as long as I stick close to my friends."
        "Natsume pointed out that Naomi tends to sing off-key, but said she thought we'd nevertheless have a good time."
        "I am kind of looking forward to it. Since we won't be submitting anything else for the time being due to the exams, this will be a good way to bring closure to the activities of our little writing group."
        ha "I... hope so."

        show lilly basic_smileclosed_paj_close
        show hisao cross_grin_uni
        with chchange

        "Hisao smiles playfully."
        hi "That does mean you'll have to study twice as hard during the weekend to make up for the fact that you won't be able to do much cramming on Friday."
        ha "I'll d-do my best to catch up on Saturday."
        "That reminds me about what Mutou said earlier about that open house day on Sunday. Maybe it's a good idea to bring this up with Hisao and Lilly."

        show lilly basic_surprised_paj_close
        show hisao basic_neutral_uni
        with chchange

        ha "Ummm... Do you remember that open house day that Mutou talked about before?"
        "Hisao frowns and then nods."

        show lilly basic_smile_paj_close
        show hisao cross_speak_uni
        with chchange

        hi "Right, he brought that up during homeroom some time ago. Are you planning on going there?"

        show lilly basic_weaksmile_paj_close
        show hisao cross_neutral_uni
        with chchange

        ha "I'm not sure. Mutou mentioned it again today and recommended going. As a source of motivation."
        li "Even though we can't really spend too much time away from our study books, it might be a very good idea to go there and have a look. I agree with Mutou's suggestion. It might motivate us to try even harder."

        show lilly basic_smileclosed_paj_close
        show hisao cross_worry_uni
        with chchange

        "Hisao doesn't look convinced yet."
        hi "It's pretty far away from here. We'd have to get up really early and we'd be back really late."

        show lilly basic_smile_paj_close
        show hisao basic_neutral_uni
        with chchange

        li "Maybe I could ask my father to take us there by car. I will need someone to help me navigate the area, and I can't ask any of you since each of us will be visiting a different faculty."
        hi "If it's not inconvenient for him, and he'll be able to handle a lot of walking..."

        show lilly basic_reminisce_paj_close
        with chchange

        "Lilly's smile fades for a moment."
        li "My own pace isn't very fast, so I'm sure he'll be able to keep up. And he has... plenty of free time right now."

        show lilly basic_sad_paj_close
        show hisao basic_worry_uni
        with chchange

        hi "Sorry."

        show lilly basic_weaksmile_paj_close
        show hisao basic_neutral_uni
        with chchange

        "Lilly's smile returns, and she makes a quick hand gesture in order to dismiss the matter."
        li "It's fine. I'm sure it'll be a great experience for all of us."

        show hisao basic_speak_uni
        with chchange

        hi "Hanako? Shall we go there the upcoming Sunday then?"

        show hisao basic_neutral_uni
        with chchange

        "I'm not really sure about the great experience part, but I don't think Hisao and Lilly will go there if I don't come along."
        "I was pretty nervous before the trip to Scotland, and that turned out really well, Mister Satou's incident notwithstanding."
        ha "O-okay then."

        show lilly basic_smile_paj_close
        show hisao cross_smile_uni
        with chchange

        hi "Maybe this would be a good opportunity for you to check out the dorms there as well, Lilly. You can determine how easy they are to navigate."

        show lilly basic_weaksmile_paj_close
        with chchange

        li "Hmmm..."
        "Lilly doesn't immediately respond to Hisao's remark, and I happen to know why. She told me recently during one of our outings, but I suppose she hasn't told Hisao yet."
        li "I'm not certain about that yet. I've been trying to convince my parents to let me live on my own after graduation. I'm used to handling life in a dorm by now. I'd like to take another step towards independence."

        show lilly basic_smile_paj_close
        with chchange

        li "I feel that my time at university is the perfect time to brush up my domestic skills a little more. After graduation from university, I want to be able to focus completely on my job without having to worry about still getting used to running my own household."

        show lilly basic_smileclosed_paj_close
        with chchange

        li "College time is probably the perfect time to get this matter out of the way."
        "I silently smile. It's typical of Lilly to be planning this far ahead already."

        show hisao basic_sweet_uni
        with chchange

        hi "So what did your parents say?"

        show lilly basic_sad_paj_close
        show hisao basic_neutral_uni
        with chchange

        "Lilly's smile falters a bit."
        li "Convincing them hasn't been very succesful so far. Mother seems... willing to give the possibility some consideration, but Father hasn't reached that point yet."

        show hisao cross_speak_uni
        with chchange

        hi "Well, letting a child live on his or her own would be kind of scary for any parent at first and surely there are plenty of additional challenges for someone who can't see."

        show lilly basic_concerned_paj_close
        show hisao basic_neutral_uni
        with chchange

        li "I am well aware of that. However, I've faced many of these challenges already when Akira and I were living together, and I was able to handle myself decently."

        show hisao cross_neutral_uni
        with chchange

        hi "Did you remind them of that?"

        show lilly basic_displeased_paj_close
        with chchange

        li "It's a bit tricky to make that point without coming across as offensive. There may be another way to ease their minds a bit."
        hi "How?"

        show lilly basic_weaksmile_paj_close
        with chchange

        "Lilly pauses for a moment."
        li "Perhaps they'd reconsider if I had a roommate to keep an eye on things. I was wondering..."

        show lilly basic_satisfied_paj_close
        show hisao basic_neutral_uni
        with chchange

        "She suddenly turns to me and puts an arm on my shoulder."
        li "Hanako, I realize this is getting ahead of things a bit, but assuming we'd both do well on our exams, would you be willing to consider becoming that roommate?"

        show hisao basic_sweet_uni
        with chchange

        "I reel in shock. Is Lilly really asking me to share an apartment with her? I didn't see this coming at all."
        ha "B-but... M-me?"
        li "I think you would certainly be the most suitable person. I've been meaning to ask you this at some point anyway. I wouldn't mind a bit of company, and we could split household chores between us."
        li "That way, I can still get in whatever practice I need. And it will be good to have someone around that I trust in case there are things that need to be done that require eyesight."
        ha "B-but..."

        nvl clear
        nvl show dissolve

        n "I stop myself before I can comment that I wouldn't be able to afford my half of the rent for something as expensive as an apartment. I doubt Lilly and her family would even accept my money to begin with."
        n "{vspace=30}Maybe I should give this some consideration. It would certainly be the best solution to my approaching housing problem, and it would probably help with my studies if I have a nice, quiet place to return to after school hours, rather than a dorm filled with people I don't know."

        nvl hide dissolve

        ha "...roommates..."

        show lilly basic_weaksmile_paj_close
        show hisao cross_smile_uni
        with chchange

        li "I cannot give you a guarantee that you moving in with me would be enough to sway Father's mind, but it's worth a try. And it would be the ideal way for the three of us to stay in contact with one another without having to neglect the new people we'll be meeting."
        ha "I... ah..."
        "I cannot argue with any of Lilly's points. I'd like to stay in contact with Lilly no matter what, and if we become roommates, that means Lilly can spend time with me at home and I won't have to worry about me preventing her from hanging out with the new friends she'll make on campus."

        stop music fadeout 2.0

        queue music music_friendship fadein 4.0

        ha "I... ah... would like that."

        show lilly basic_satisfied_paj_close
        show hisao basic_smileclosed_uni
        with chchange

        "Lilly beams at those words."
        li "Really?"
        "I recall what Miss Yumi once said about taking advantage of opportunities as they present themselves. This is probably one of those opportunities, and if Lilly can pull this off, I don't think I'll feel sorry about it afterwards."
        ha "R-really."

        show lilly basic_cheerfulblush_paj_close at center
        with charamovefastest

        li "I am truly happy to hear that Hanako."

        show hisao cross_pout_uni
        with chchange

        "Lilly smiles happily and pulls me into a loving hug. I giggle as I return the embrace, and we cuddle for a little while."
        "Lilly and I are close enough now for me to not feel uncomfortable about displays of affection of this kind. Hisao, on the other hand, rolls his eyes."

        show lilly basic_cheerful_paj_close
        with chchange

        hi "What is it with all those girls throwing themselves at you today?"

        show lilly basic_planned_paj_close
        with chchange

        "Lilly playfully grins at Hisao."
        li "Jealous?"
        hi "The answer's still no."

        play ambient sfx_phonering

        show lilly basic_surprised_paj_close
        show hisao basic_neutral_uni
        with chchange

        "Lilly opens her mouth to reply, but her words are cut off by a noise that I recognize as Lilly's ringtone."

        show lilly basic_weaksmile_paj_close
        with chchange

        li "Would you mind if I take this?"
        ha "Go ahead."

        show lilly basic_smileclosed_paj
        with charadistant

        "Lilly breaks off our hug and makes her way to the phone which is lying on top of her dresser."

        stop ambient

        show lilly basic_smile_paj
        with chchange

        li "Good evening, Lilly Satou speaking."

        show lilly basic_smileclosed_paj
        show hisao cross_smile_uni
        with chchange

        li "Hello, Mother."
        li "I'm doing well. We're currently studying for next week's mock exams."
        li "Yes, like a dress rehearsal for the real ones."
        li "Yes, all three of us."

        show lilly basic_giggle_paj
        with chchange

        li "She told me that you replied already. It's great, isn't it?"

        show lilly basic_planned_paj
        show hisao cross_grin_uni
        with chchange

        li "I have been told that the money will be put to very good use."

        show lilly basic_displeased_paj
        show hisao basic_neutral_uni
        with chchange

        li "Yes, I've been with Father all day yesterday. We actually went to visit Grandmother and Grandfather together. It's a shame you couldn't be there. I asked Father to postpone the visit until you were back in the country, but he said rescheduling might be inconvenient."
        li "Hmmm... Perhaps it would be best to talk about that later."

        show lilly basic_satisfied_paj
        show hisao basic_smile_uni
        with chchange

        li "You're coming back on Sunday already? That's good to hear."

        show lilly basic_weaksmile_paj
        with chchange

        li "Ah... Making it to the airport to welcome you back may be a problem. We just made plans for the upcoming Sunday."

        show lilly basic_cheerful_paj
        show hisao basic_smileclosed_uni
        with chchange

        li "We're going to see what our future looks like."

        stop music fadeout 3.0

        scene black
        with endchapter

        if _in_replay:
            return

    return
