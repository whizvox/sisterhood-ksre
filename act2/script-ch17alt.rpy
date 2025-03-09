label sh_ch17alt:
    label .s1:

        $ set_window_tint(TINT_HISAO)

        scene bg school_track_on
        with Dissolve(2.0)

        "I wonder how Hanako is doing right now."
        "That thought keeps returning to me as I casually stroll along the running track with my hallmate Kenji in tow."
        "The official excuse is to catch up on what transpired at the science club during my week of absence and fill Kenji in on the reason I was out of commission."
        "But more importantly, my dorm room is being used by Lilly right now to try and patch up her damaged friendship with Hanako."
        "While I'm not completely sure how much of it can be salvaged in the 24 hours that remain until Lilly's departure to Scotland, I don't want to risk things being ruined by my eccentric neighbor bursting into my room unannounced."
        hi "I'm sorry. What did you say?"

        show kenji neutral
        with charaenter

        play music music_kenji fadein 4.0

        ke "How can you be so sure that the person who assaulted you wasn't a woman? A feminist or perhaps a lackey hired to take you out."
        "I wonder how Hanako and Lilly are doing right now."
        hi "It was a guy. A slightly older man on a bicycle."
        hi "Hana… I mean, people at the scene confirmed it to me later. I don't think he was a feminist."

        show kenji tsun
        with chchange

        ke "The whole thing still smells extremely fishy to me. I mean... Getting body checked in the middle of the street and carried off to who-knows-where... Does that sound normal to you?"
        "Hanako at least seems relieved that she and I have managed to reconcile after last week's events. I think she's going to need my support after Lilly leaves tomorrow."
        "Despite having pushed Lilly away last week, I have no doubt that Hanako's going to miss her terribly."
        hi "We were in the middle of a downpour, and neither one of us was paying attention. The rainstorm made it kinda hard to see far ahead. It was just a stupid little accident with big consequences."
        "I sigh inwardly."
        "The idea was to just get an update on what Mutou and Kenji discussed at the science club meetings last week, but it turns out that after my accident, Kenji came to his own conclusions about my absence and shut himself in for the rest of the week."
        "It's still a mystery to me how Kenji can act so ordinary during club meetings and so irrational when we're alone."

        show kenji rage
        with chchangefast

        ke "Accident my ass! You were on somebody's hit list, man. It was a coordinated operation."

        show kenji neutral
        with chchange

        ke "The feminist movement is onto you. I bet that wasn't even a real ambulance that picked you up."
        "I can't really judge that since I was out like a light at that time, and what I know about that moment is from Hanako's recollection."
        "Since she's still very reluctant to talk about what happened that afternoon, I can't really get into the details."
        hi "It was a pretty real hospital I woke up in though."

        show kenji happy
        with chchange

        ke "They sent some goons the day after to ransack your room. Or maybe to bug the hell out of it. They're watching you now, man."
        "That would be Shizune and Misha who asked the dormkeeper for a spare key and got me my possessions and some books to make my stay in the hospital more comfortable."
        "So it turns out that Kenji spotted them. I wonder what he would say if he knew there are two other girls in my dorm room right now."
        "I feel once again that getting Kenji away from the dorm building today has been a very wise move."
        hi "Those were just some girls from my class, picking some stuff up for me."

        show kenji tsun
        with chchange

        ke "You really think I can't tell the difference between students and trained spies? They were dressed like female students for sure, but their mannerisms gave them away."
        hi "How so?"

        show kenji happy
        with chchange

        ke "They didn't say a single word during the whole operation. They were only communicating in coded gestures, like commandos on a mission."
        hi "Could it be that one of them was a deaf-mute and they were communicating in sign?"
        ke "Maybe. It makes sense to pick a mute person for an infiltration job. When they're captured and interrogated they at least can't blab. Unless you untie their hands first. That's what they're counting on. They're trained for those kinds of situations."
        "You're completely missing the point."

        hide kenji
        with charaexit

        "I fiddle with my cell phone for a bit. I asked Hanako to send me a little text message when they're done."
        "In less than half an hour, I have a talk coming up with Hanako's therapist who asked me to come and see her, if Hanako and I managed to reconcile."
        "She was seeing a client earlier this day though and made it clear she didn't want me to wait outside her office, presumably for the sake of her client's privacy."
        "So until her last appointment is over, at four o' clock apparently, I'm stuck playing along with Kenji's conspiracy theories."

        show kenji tsun
        with charaenter

        ke "After they left your room, I knew they'd be coming for me next. I knew they were gonna kidnap me, imprison me somewhere and then send a squad to my room to steal my blueprints and plans for resistance activities."
        ke "So I locked my door, moved my bed in front of it and got to work on developing a defense mechanism. It's not finished yet, so maybe you can take a look at the designs at the next club meeting."
        hi "Really?"

        show kenji happy
        with chchange

        ke "It's a very clever contraption. I've hidden my papers in a secret compartment in my desk drawer."

        show kenji neutral
        with chchange

        ke "To open it, you gotta lift the compartment lid through a hole in the bottom of the drawer using a pen or pencil."
        ke "If you open the compartment any other way, an electronic circuit is closed that causes the flammable substance inside the contraption to ignite which in turn causes all the incriminating evidence to go up in smoke."
        ke "I saw it on TV once and thought it was a stroke of genius."
        "I make a mental note to sabotage that insidious thing (if it even exists) the first chance I get and keep any and all flammable substances far away from Kenji before he accidentally sets the guys' dorm building on fire."
        hi "Sure, I'll help."

        show kenji happy
        with chchange

        ke "Hey, thanks!"

        show kenji tsun
        with chchange

        "Kenji seems delighted at my quick offer of assistence, but then suddenly narrows his eyes and takes a step back."
        hi "Something's wrong?"
        ke "You're way too eager to agree all of a sudden. You're usually far more reserved about my plans. This doesn't sound right. Didn't you say they operated on you?"
        hi "Yeah."
        ke "How can I be sure that they didn't install a mind control device while you were out? Maybe you were merely being ordered to agree to help me just now and they'll make you sabotage my device the moment I turn my back."
        "I'm not quite sure whether to be impressed by Kenji's justified suspicion of me or baffled by the leap of logic he took to explain it."
        hi "They operated on my chest. Doesn't a mind control device usually go in the brain?"
        "Why am I even arguing with him as if this is a serious conversation topic?"

        show kenji neutral
        with chchange

        ke "Hmmm… Maybe not a mind control device then. Probably a tracking device. Definitely a tracking device."
        hi "Why definitely a tracking device?"
        ke "Last Saturday that tall blonde from my class came knocking and told me that you'd be arriving at noon and that they were going to ‘welcome you back’. They knew exactly where you were going to be and when."
        ke "If they were confident enough of the success of their ambush to go and taunt me with it, they had to have placed a device on you somehow that allowed them to pinpoint your location."
        "It's kinda scary how seamlessly he manages to fit all of last weeks events into one big narrative and still get things completely wrong."
        hi "I'm not sure I want to know but… Since you knew they were setting up an ambush for me, did you do anything to try and thwart them?"

        show kenji tsun
        with chchange

        ke "Sorry man, but I had to set up my own defenses first. In this harsh world, it's every man for himself."
        hi "That's okay. I managed to survive."
        ke "Maybe you were worth more to them alive. With that tracking device inside you, they may be monitoring us right now."
        ke "Maybe we shouldn't be seen together."
        "I do my best to supress a groan and check my watch."
        "It's almost time for my meeting with Miss Takawa. It'll take some time for me to reach the building where the medical staff resides, especially since I'm still forced to take it slowly for a little while, and I think I've heard enough crazy for one day."
        hi "Maybe you should do a perimeter check if that's what worries you. I have an appointment at the nurse's building. I'll have them check me for tracking devices."
        hi "Why don't you stay behind and make sure I'm not followed? Then you can check your theories for yourself."

        show kenji happy
        with chchange

        ke "Hey man, that's a great idea. Go ahead and leave. I'll watch your back and then check this place for spies or bugs."
        hi "Sure thing."

        hide kenji
        with charaexit

        play sound sfx_bushes

        "As I start making my way to the staff building and see Kenji sneak off into the nearby bushes, I feel a bit guilty about sending him off on a wild goose chase, but after what I've just heard, I can't have him return to the dorms just yet."
        "I can't help but roll my eyes at the irony of it all."
        "There's a guy out there who believes in mind control devices searching the bushes for spies and cameras right now, and yet I'm the one about to see a therapist."

        stop music fadeout 1.0

        if _in_replay:
            return

    label .s2:

        $ set_window_tint(TINT_HISAO)

        scene bg school_therapist
        show takawa smile at center
        with locationskip

        queue music music_another fadein 4.0

        "As I reach out to take the bowl of hot tea from the old lady, she gives me a playful smile before putting the bowl in my hands and making a polite bow to indicate it's okay to drink."

        show takawa happy
        with chchange

        ta "Herbal tea without caffeine. Miss Ikezawa would probably be upset with me if I did anything that might endanger your health. I can't really afford damaging my bond of trust with her."
        "I take a few careful sips as I look the old woman in front of me over."
        "Last week while I was in the hospital, she dropped by and convinced me to try and reach out to Hanako who shut me out after she broke down a few days earlier. And she asked me to let her know about the outcome."
        hi "When you and Lilly left my hospital room last week, you asked me to come see you if I managed to reconcile with Hanako."

        show takawa calculating
        with chchange

        ta "And since you're here now, I presume you succeeded."
        hi "We're back together again. It turned out I was wrong to think she tried to end our relationship because she couldn't deal with the idea of having a boyfriend who might die on her at any moment."
        ta "Am I correct when I assume that she felt she could no longer uphold your mutual promise of supporting each other in times of need?"
        "For a second I'm taken aback by the accuracy of her claim. Did she know this the whole time?"
        hi "Did Hanako tell you this after you picked her up from the hospital?"

        show takawa serious
        with chchange

        "Miss Takawa shakes her head and gives me a sad smile."
        ta "Miss Ikezawa's… mindset is not very different from people who've been in… similar circumstances. I've worked with several of them over the years."
        ta "Eventually you get a feeling on how they react to certain situations and how they experience them."
        hi "Like boyfriends with heart conditions?"

        show takawa smile
        with chchange

        "She chuckles."
        ta "Especially boyfriends with heart conditions."
        "I take another sip of the hot, but tasty drink and wait for the old lady to continue."
        "I know she didn't merely want to see me to hear the news of our reconciliation. Sensing that I'd like her to get to the point, Miss Takawa scrapes her throat."

        show takawa calculating
        with chchange

        ta "Ahem... whenever a client has a breakdown like Miss Ikezawa had last week, we try to identify the possible causes and do our best to come up with ways to prevent those situations from ever occurring again in the future."

        show takawa smile
        with chchange

        "She smiles sheepishly at me for a moment."
        ta "I suppose one way would be to ask you to try and not have any more episodes, but that's probably not a very helpful suggestion."
        hi "I probably could have thought that one up myself."

        show takawa calculating
        with chchange

        ta "So what we should probably focus on is not so much trying to influence your condition, but rather Miss Ikezawa's reaction to it."
        hi "You mean her panic attack?"
        ta "Correct. Her breakdown can be traced to multiple factors."

        show takawa serious
        with chchange

        ta "Painful memories resurfacing. Desperation. A feeling of helplessness. Once what was happening to you started sinking in, all those things effectively paralyzed her. And that in turn created a strong sense of guilt afterwards."
        hi "So what are you suggesting?"

        show takawa calculating
        with chchange

        ta "Even though this school has a nursing staff that's on-site 24 hours a day, all employees here such as teachers and other non-medical staff members are still expected to know some basic emergency first responder skills."
        ta "And every few years they're required to brush up on them. We hire a professional trainer from the nearby hospital a few times a year to instruct our people."
        ta "The next courses happen to take place the upcoming week. I took them myself last year, but I was thinking it might be a good idea for me to sign up for them again this time…"
        hi "I don't see how that…"
        ta "…and let Miss Ikezawa go in my place."
        hi "What?"

        show takawa smile
        with chchange

        ta "They're not really meant for students, but I see no practical problems in letting Miss Ikezawa attend. I'll need to consult with the trainer to be sure, of course."
        "I take a moment to consider the old woman's proposal."
        "Hanako taking first aid classes? I have to admit the idea might have merit."
        "She'd at least no longer feel helpless in a case of emergency. That's assuming she'd remain composed enough to remember whatever it is they'll end up teaching her."
        hi "Do you really think that'll prevent another panic attack from taking place in a situation like last week?"

        show takawa calculating
        with chchange

        ta "No. That's probably unavoidable the way things are right now. The best we can probably hope for is trying to delay it."
        ta "With luck, and keep in mind there are no guarantees, it'll allow her to keep herself occupied and distracted until the ambulance arrives and it'll prevent her from feeling guilty over any inaction on her part."
        ta "It would make a massive difference in the aftermath, I believe."
        hi "I think we should take whatever we can get. If Hanako is okay with this, I am too."
        ta "Seeing that this is something that could potentially benefit you in the future, there is no doubt in my mind that Miss Ikezawa will agree to participate in the training."
        hi "Why exactly are you telling me this instead of her?"
        ta "Because if we're going to do this, I might need your signature for something."
        hi "Fair enough."
        ta "Then let's proceed."

        show takawa:
            ease 2.0 right
        with None

        "Miss Takawa gets up, takes the phone on the table in the corner of the room and makes two phone calls; one to sign herself up for next week's training and another longer one to explain Hanako's situation to the trainer."

        show takawa smile
        with chchange

        ta "The instructor has agreed to let Miss Ikezawa attend in my place and he will do his best to let her get in as much practice as possible."
        hi "That's good to hear. Let's hope she won't get too nervous about attending a class with people she's not familiar with."
        ta "There will only be 7 other people attending from what I've just heard, so it's a relatively small group this time around and there may be a few familiar faces among them."

        show takawa at center
        with charamovefast
        show takawa serious
        with charachangealways

        "We finish our tea, and as Miss Takawa takes my bowl from me, she gives me a sincere look."
        ta "The instructor asked me if he could have a look at your medical file before the courses start."
        ta "Since he's not directly affiliated with Yamaku and this is not an emergency situation, I'm going to need your written consent before I can oblige."
        hi "That's not a problem."

        show takawa smile
        with chchange

        ta "Good. Let's head down to the administration office and get ourselves a form for you to fill in."
        hi "By the way, do you have any tips on how to act in case she shuts down again?"

        show takawa serious
        with chchange

        ta "If she does so as a result of you having an episode, I doubt there's much you can do. But if it's something else that causes her to break down, I'd suggest simply holding her."
        hi "Just holding her?"

        show takawa calculating
        with chchange

        ta "Calming her down with words may not help much if she's in a state of irrational stress."
        ta "Activities such as cuddling cause oxytocin to be released in the brain that will allow her to relax and will lower the sense of stress and fear that she's feeling."
        ta "In fact, I believe the practice has a benevolent effect on symptoms of post traumatic stress in general, so if she has trouble sleeping or is feeling anxious, this is probably the first thing you should try."
        hi "I certainly don't mind that kind of advice. Anything else?"

        play sound sfx_phonenotif

        "Before she can reply, my phone suddenly lets out two loud beeps to indicate a new text message."
        hi "I'm sorry. Can I just…?"

        show takawa smile
        with chchange

        ta "Would that be Miss Ikezawa?"
        "I take a look at the screen of my phone. It's from Hanako alright."
        "But there's no word on how things turned out. Just a simple “Where are you right now?”."
        "I let out a disappointed sigh and send a quick “Nurse staff building, heading for administration office.” back."
        hi "I convinced Hanako to give Lilly a chance to smooth things over between them. She and Lilly… Well…"

        show takawa serious
        with chchange

        ta "I am aware of what happened between Miss Ikezawa and Miss Satou."
        ta "After we left your room last Friday, Miss Satou offered to treat me to a cup of tea in the hospital's cafeteria, and she took the opportunity to fill me in on her… falling out with Miss Ikezawa and ask me for suggestions."
        ta "But it's a difficult situation to advise someone on."

        hide takawa
        with charaexit

        "She gets up and makes a beckoning motion towards the door to indicate she wants me to follow her downstairs."

        scene bg school_hallway4
        with locationchange

        play sound sfx_doorclose

        "We leave the office, Miss Takawa locks its door, and we head down the hallway towards the elevator."
        hi "You don't sound particularly optimistic."

        show takawa serious at tworight
        with charaenter

        ta "If it hadn't been for Miss Satou's imminent departure, this would have been an ideal opportunity for them to sort out the latent issues in their friendship and come out of it as closer friends."
        ta "But in order to take those difficult steps, I think they'd need a more inviting prospect than simply a parting on somewhat friendlier terms."
        "That's pretty much what I've been thinking as well, though I still hold out hope that they can resolve things in some way or another."
        hi "Hanako isn't one to easily trust people. I suspect a part of her has always remained suspicious of Lilly's motives for being so devoted to her."

        show takawa calculating
        with chchange

        ta "Establishing a bond of trust as friends often involves being able to show your vulnerable side to the other person, and I suspect that's not something that comes naturally to Miss Satou."
        hi "She has one alright, but it wasn't until last week that I actually got to see it, and I might have been the only one who witnessed her like that in years."
        hi "The lengths she goes to to keep up appearances can be pretty unsettling at times."
        ta "It's something we encourage as a society, even in situations where it makes matters more difficult."
        ta "In addition, Miss Satou has a strong sense of pride. You can tell by the way she behaves and carries herself. And I'm sure it serves her well most of the time. Just… not always."

        scene bg school_nursehall:
            yalign 0.5 zoom 1.02
        with locationchange

        "As we reach the administration area near the building's entrance, the old lady heads up to the desk, exchanges a few words with the girl behind it and is given a form that she signs and then hands over to me before taking a small note for herself."

        show takawa calculating
        with charaenter

        ta "By signing this form, you'll give me permission to inform Miss Ikezawa's trainer of the specifics of your condition."

        show takawa smile
        with chchange

        ta "That's the short version. You can look it over yourself before putting a signature down there."
        "I do so, but as expected a lot of the wording on there seems mumbo jumbo to me."
        "I quickly give up on trying to make sense of the whole thing and put my signature on the dotted line near the bottom."
        "I give the form back to Miss Takawa who's still in the process of writing a note to go with the form."

        hide takawa
        with charaexit

        stop music fadeout 2.0

        "As she takes the form from my hands, her gaze suddenly shifts from me to something behind me."

        show hanako emb_downtimid
        with charaenter

        "I look and see Hanako entering the room, looking somewhat winded."
        "It's been only a few minutes since I sent back that text message. Did she run all the way here?"
        hi "Hanako?"

        play music music_romance fadein 4.0

        show hanako basic_bashful_close:
            center
            ypos 1.02
        with characlose

        with vpunch

        "Spotting me, Hanako takes a second to catch her breath, then struts over to me and hugs me so tightly I groan in discomfort, her body causing pressure on the wound from the surgery I had last week."
        hi "Ouch! Take it easy. Watch the chest wound!"
        "Hanako's uncharacteristically bold gesture takes me off guard. The last time she did something like this was after our confession in the park that started our relationship."
        "Does this mean she worked out her differences with Lilly completely?"
        "No, it must be something more. Hanako doesn't just look happy, she looks elated. Possibly happier than I've ever seen her before."
        hi "Hanako?"

        show hanako emb_smile_close
        with chchange

        ha "Hisao! She's… she's staying! She's r-really staying!"
        hi "Slow down a bit. What are you talking about?"
        ha "Lilly's… staying here. She changed her mind about moving."
        hi "W-what?"
        "I'm admittedly shocked by this sudden development."
        "Lilly and I have talked a lot over the past week—mostly about what could still be done to repair her bond with Hanako after the latter lashed out at her."
        "But Lilly's never even once mentioned having second thoughts about her decision to leave Japan, and I never suggested to stay here at Yamaku because Hanako has told me in the past that she didn't want Lilly to stay here for her sake alone."
        hi "That's… How? What happened?"

        show hanako basic_normal_close
        with chchange

        ha "She… was afraid of d-disappointing her parents. But she n-never really w-wanted to leave herself."
        hi "And you… convinced her to do what she wanted for herself and stay here?"

        show hanako emb_downsmile_close
        with charachangealways

        "Hanako doesn't answer and merely stares at the floor, but her smile tells me all I need to know."
        hi "Hanako, you're amazing! You're the best friend Lilly could ever wish for!"

        show hanako emb_smile_close
        with chchange

        "She looks flustered by my exclamation, but I mean every word of it."
        "Of course I'm happy for Hanako, but Lilly has become a close friend to me as well over the last months, and I was very disheartened to see her go myself."
        "Hearing about her decision to stay here after all is a huge relief for me as well. I give Hanako a quick kiss on the cheek to emphasize my approval."

        show hanako emb_blushing_close
        with charachangealways

        "Hanako, predictably, blushes profusely and stammers a half-hearted denial."
        ha "N-not r-really… I… um…"
        ta "Miss Hanako?"

        show takawa smile at tworight
        show hanako emb_blushing at twoleft
        with charaenter

        "The voice of Miss Takawa behind us reminds us there are still other people in the room, and we quickly let go of one another as we turn to face the old woman who's been watching the whole spectacle with an amused smile on her face."

        show hanako basic_bashful
        with chchange

        ha "M-Miss Yumi!"
        ta "That's not what we've been practicing together. I think it's very important that you accept the praise you've earned today. I agree with Mister Nakai that Miss Satou is very lucky to have you."
        "Her words, spoken in a warm, grandmotherly tone are emphasized by a deep and respectful bow."

        show hanako emb_blushing
        with charachangealways

        "For a moment, Hanako seems unsure on what to do, fidgeting uncomfortably and unable to look at Miss Takawa directly."

        show hanako emb_downsmile
        show takawa happy
        with chchange

        "Then, after several painfully quiet seconds, she gives a barely visible and meek nod, her gaze still firmly focussed on the floor."
        ta "Congratulations, dear. I'll see you again at the usual time the upcoming weekend. I'm sure we'll have plenty of things to discuss."

        hide takawa
        hide hanako
        with charaexit

        "After making one more bow for good measure, Miss Takawa takes her leave, and I decide it's better if we get out of here as well after the rather public show we just put on."

        show hanako basic_normal_close
        with charaenter

        "As we exit the building, I turn to Hanako."
        hi "I have some interesting news for you too, but first I'd really like to hear a few more details on how you reconciled with Lilly."
        ha "Okay."
        hi "Oh… and Hanako?"

        show hanako basic_bashful_close
        with chchange

        ha "Yes?"
        "I gently take her hand as we walk along."
        hi "I'm very proud of you."

        stop music fadeout 3.0
        scene black
        with Dissolve(3.0)

        if _in_replay:
            return

    return