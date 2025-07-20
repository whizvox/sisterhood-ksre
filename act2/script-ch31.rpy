label sh_ch31:
    label .s1:

        $ set_window_tint(TINT_AKIRA)

        call sisterhood_timeskip

        scene bg smt_reception
        with nextchapter

        play music music_normal fadein 4.0

        "Receptionist" "Miss Satou!"
        "I turn my head and look at the reception desk where a woman in her early 30s is beckoning me."
        "Receptionist" "Good morning, Miss Satou."
        aki "Good morning... {w=0.5}erm... Wendy?"
        "Receptionist" "Jenny."
        "Crap."
        aki "Sorry, I'm still in the process of remembering everybody's name. Please humor me for a little while longer."
        "Receptionist" "Not a problem. How is your father doing? Is he still sick?"
        "Most of the employees still don't know why Dad hasn't shown up at the office in two days straight and assume that it's a common illness, but it's probably not my place to spill the beans."
        "I can see how the truth could create a fair share of commotion around here."
        aki "Yes, I'm afraid he's still a bit under the weather."
        "Receptionist" "Hopefully he'll be better soon. It feels rather odd not to see him come in here each morning."
        aki "Here's hoping."
        "Receptionist" "Anyway, Mister Ferguson wanted to see you before you start this morning."
        aki "Thank you for telling me. I'll go and pay him a visit, then."

        scene black
        with locationchange

        "I leave the reception area and head over to the office of the person who's in charge of this branch after Dad. I haven't really spoken with him much since I arrived here."
        
        play sound sfx_doorknock2

        "As I knock on the door of his office, I hear a soft ‘come in’ and enter. I think I already know what this is going to be about."

        play sound sfx_dooropen

        scene bg smt_office
        with locationchange

        fer "Ah, good morning, Miss Satou."
        aki "Good morning, Mister Ferguson. How are you doing?"
        fer "As well as I can, given the circumstances. Have you been managing to get settled in a bit already?"

        nvl clear
        nvl show dissolve

        n "I still feel a bit like a fish out of the water at times."
        n "{vspace=60}Dress code is all over the place. Lots of people come to work in their casual attire, rather than a business suit. The higher ups still dress formal as usual, as do the people from sales and marketing, although even those show up every now and then in their casual clothes, presumably on days when they don't have any activities planned that involves contact with customers or business partners."
        n "Most people are also on first-name basis with one another, though there are some exceptions here and there, too. It's still a bit confusing at times. The Japanese branch's corporate culture may have been overly traditional and formal, but at least it was consistent."

        nvl hide dissolve

        aki "I think I'm doing fairly well with that. My direct colleagues have been very helpful. I'm still trying to convince people to address me by my first name, though."
        fer "Are you comfortable with that?"
        aki "I think I could easily get used to it. Everyone around me uses first names to address the others. I can't fall behind."
        "Mister Ferguson gives me a sheepish smile."
        fer "One of the first things we teach employees here who get to deal with people from your former branch on a regular basis is to always address Japanese co-workers by their family name even after having built a working relationship with them."
        aki "Hmmm, does that also apply to Japanese who gain Scottish citizenship?"
        fer "That is up to you to decide. People will learn as long as you're not afraid to keep correcting them."
        aki "If I may ask, how do you address my parents?"
        fer "I always address your mother by her first name. She'd probably think something was wrong if I called her by her last name, especially since she also plays bridge with my wife and two others every two weeks, so I also know her socially a bit."
        aki "Mother really seems to be living an extremely busy life. Not only has she been working a full-time job, but she's also on the neighborhood committee and goes on bike rides with friends."
        aki "I sometimes wonder if she's ever at home at all."
        "Mister Ferguson chuckles."
        fer "I sometimes wonder about that too."
        fer "She once told me that she occasionally gets involved in various charity events and that she's also been working on rebuilding and expanding the old network of contacts she had when she was still a business reporter."
        fer "I believe she regularly submits columns to various local magazines and newspapers. Personally, if I had that kind of life, I'd burn myself out in weeks, but she seems to handle it just fine."
        "Seems like it. And the only thing that had to go was her interaction with her children. Small sacrifice, really." #damn, akira
        aki "How about my father?"
        fer "To be honest, we tried first names for some time, but I could tell he wasn't very comfortable with it, so eventually, we switched back."
        fer "I have to admit, interaction became stilted from time to time whenever he called me Norris and then gave me a look as if apologizing for insulting me."
        "He smirks."
        fer "I've always been fascinated by how different your parents are as people."
        aki "Different?"
        fer "Your mother's an extraverted woman, always on the go, involved in a hundred things at once, and with a knack for quickly spotting and immediately pouncing on opportunities that present themselves."
        fer "Your father's more of an introvert, content to sit in his study and read through his book collection in the little free time he permits himself, and I've never seen him make decisions on a whim..."
        fer "He always tries to get to the bottom of whatever issue he faces before deciding on it and he usually pays a large amount of attention to the long-term consequences of whatever action he takes. More than anyone else I've ever met."
        aki "I see."
        "A gloomy expression appears on his face."
        fer "Which is why this came as such a shock."
        fer "I could see your father brushing off warning signs with explanations like ‘rsi’ or ‘indigestion’ in order to avoid worrying others, but I find it impossible to believe he failed to consider the possibility of a heart affliction, himself."
        fer "Especially since he, like many of us at the office, has taken the same first aid training we also offer our larger customers as part of our service. He must have known. And yet, he kept going."
        aki "He probably thought he would be able to hold on for a few more weeks. Mother had a vacation planned afterwards that he could use to get his bearings back."
        aki "I don't think she'll have much opportunity to take it easy any time soon. We don't even know when he's going to be released from the hospital yet."
        fer "How is he? Have you spoken to him already?"
        aki "My mother, my sister, and I dropped by the hospital yesterday, but he was asleep while we were there, and they wouldn't let us see him."
        aki "We have an appointment with his cardiologist later today. Perhaps we'll get lucky afterwards."
        fer "Give him my regards, and tell him not to worry too much about the company. We're going to do our best to succeed in the next few weeks, even if he's not there to participate."
        aki "If I may ask, has there already been word from the board of directors in Japan on what they want to do with the delegation that is heading for the US in a few weeks?"
        fer "Not yet. I think they will send a few people from the Japanese branch along."
        fer "Just between you and me, I just hope those people aren't going to end up getting in the way. The Japanese branch has focused completely on the local market during the last 6 years and has barely been involved in the expansion process at all. That's been head office's task."
        fer "Part of me is hoping your mother will still come along. She's just as familiar with the involved parties as your father is and could partially compensate for his absence, but the board is not going to put a PR manager in charge of an operation this major."
        fer "They'll want someone higher up the chain of command to act as the leader."
        aki "Kojima?"
        fer "Probably. Has your mother said anything about what she intends to do? I wouldn't blame her if she decided to stay by her husband's side."
        fer "Of course, it would have been rather inappropriate to ask her about that when she called yesterday, but perhaps you've picked something up."
        aki "I'm afraid I haven't really spoken to her much."
        fer "I just wanted to let you know that nobody here would question your loyalty to the company if you followed your mother's example and decided you need some time off to deal with this. We'd be happy to accommodate you."
        "I don't think there'd be much of a point in me taking time off. If Mom needs comfort, she still has Lilly around. And Lilly has Hanako and Hisao... for the time being."
        "Mom decided it was probably best for them to return to Japan ahead of schedule, since Dad's incident pretty much put a permanent damper on their vacation. They're set take a flight back in three days."
        "If Lilly wants me to spend more time with her afterwards, I can always take a day off or so, but I think I know her well enough already to know she probably wouldn't want me to take a leave of absence purely for her sake."
        aki "I think I'll be fine, sir. But I appreciate your concern. I'll be sure to let you know if I change my mind."
        "He nods."
        fer "Good. I won't claim any more of your time. I hope the cardiologist brings good news this afternoon. You and your family have my well-wishes."
        aki "Thank you, sir. Good day."

        scene black
        with locationchange

        play sound sfx_doorclose

        "I leave Mister Ferguson's office and hurry to my own place. If I skip my lunch break and work extra hard, I'll be able to leave earlier for that appointment without getting behind in my work."

        if _in_replay:
            return

    label .s2:

        $ set_window_tint(TINT_AKIRA)

        scene bg raigmore_waitroom
        with shorttimeskip

        "I check my watch as I walk through the entry hall of the hospital for the third day in a row."
        "I'm a little later than I should be due to me having to take a phone call a minute before I was supposed to be leaving."
        "Spotting a pair of elevator doors slowly closing in the distance, I hurriedly sprint towards it and stick my hand in between them before they close completely, counting on the sensor to detect my arm, and reopen the doors."

        scene bg raigmore_elevator
        with locationchange

        play sound sfx_elevatoropen

        nvl clear
        nvl show dissolve

        n "The doors do indeed open, and rather than amputating my hand on the spot, they reveal the elevator's sole occupant: a wrinkled old man dressed in pajamas and a bathrobe, holding a pack of cigarettes in one hand while holding onto a movable IV pole with the other. He gives me an annoyed glare for briefly stalling the trip back to his room, and I mutter a quick apology in return."
        n "{vspace=60}As I look at the elevator's control panel, I notice that my fellow passenger has already pressed the button leading to the floor where I need to be as well."

        play sound sfx_elevatorclose

        n "{vspace=60}The elevator doors close again, and as the elevator starts rising, I sneak a quick look at the old man."
        n "I'm not sure what makes him a more pitiful sight: that IV pole he's dragging around, or his slumped posture in general. I wonder if this is what Dad'll look like in a few weeks, assuming all goes well. Heck, the guy sharing the elevator with me might have been a strict patriarch himself before some illness did a number on him."

        play sound sfx_elevatorchime
        
        nvl hide dissolve

        scene bg raigmore_waitcard
        show lilly basic_weaksmile at twoleft
        show karla basic_sweet_cas at tworight
        with locationchange

        "After arriving at my destination floor, I hurry over to the cardiology ward's waiting area and am relieved to see Lilly and Mom still sitting there."
        aki "Yo!"

        show lilly basic_smile
        with chchange

        li "Oh, hello Akira."
        kamo "Akira! I'm glad that you could still make it. How was your work day?"
        aki "Okayish. Aside from a few exceptions, people at the office haven't caught on yet, though I had to bite my tongue a few times."
        aki "With both Dad and you suddenly absent, several people suddenly remembered that another Satou recently moved in, and I had to feign obliviousness several times. I can't say I like doing that."

        show karla basic_ponder_cas
        with chchange

        "Mom gives a nod."
        kamo "I'm planning to drop by the office tomorrow and let people in on the situation. I wanted to hold that off until after our appointment today. I want to at least know what to tell people."
        aki "Are you coming back to work tomorrow?"

        show karla basic_distant_cas
        with chchange

        kamo "I don't know about that yet. I kinda feel like I should be at your father's side throughout this ordeal."
        "I'm not sure what irks me more: Mom's hypocritical statement or Lilly's understanding nod that follows it, but before I can determine whether or not to react to it, a young nurse comes walking in and takes a look around the room."
        "Nurse" "Satou?"

        show karla basic_lillyface_cas
        with chchange

        "Mom gets up and nods."
        kamo "That's us."
        "Nurse" "Doctor McElroy is ready to see you. This way, please."
        "Lilly gets up as well, and I allow her to take hold of my sleeve."

        hide karla
        show lilly cane_smileclosed_close
        with charaexit

        "As we head for the doctor's office, I whisper to her."
        aki "And how are you, Sis? You look a bit better than two days ago, with the emphasis on ‘a bit’. Are you still holding up?"

        show lilly cane_reminisce_close
        with chchange

        "Of course, when I met up with her in the hospital the day before yesterday, she looked about ready to break down. It makes sense that she's managed to compose herself a bit since then."
        "She gives me a tired smile."
        li "I'm doing okay, given the circumstances. Still, I'd feel a lot better if the doctor were to reassure us that Father will make a full recovery."
        aki "How are Hanako and Hisao doing?"

        show lilly cane_concerned_close
        with chchange

        li "The whole situation was as much a scare for them as it was for me. What happened hit a very raw nerve with both of them."
        "Yeah, that's not particularly surprising."
        aki "Maybe we'll have some good news today and they'll be able to return to Japan with a sense of optimism."

        show lilly cane_weaksmile_close
        with chchange

        li "I really hope so."

        stop music fadeout 2.0
        queue music music_nurse fadein 4.0

        scene bg raigmore_office
        show lilly basic_smileclosed at twoleft
        show karla basic_lillyface_cas at tworight
        with locationchange

        "We follow the nurse and Mom into the doctor's office, and I quickly guide Lilly to one of the chairs."

        show lilly at twoleft_sittingpos
        show karla at tworight_sittingpos
        with charamove

        "As the nurse leaves the room and Mom and I sit down, the doctor gives us a quick look-over and then addresses Mom."
        dc "Good afternoon. I am doctor McElroy."
        kamo "Good afternoon. I am Karla Satou. These are my daughters Akira and Lilly."
        "An inquisitive glint appears in the doctor's eye."
        dc "Satou isn't exactly a common name around here. Are you perhaps related to Satou Medical Technology? I don't deal with them directly, but I've heard that it's a family company."
        kamo "My husband actually runs that company. I'm an employee myself as well. Raigmore is a very valued customer of ours. Particularly this ward."
        dc "Yes, our ambulance team probably even used one of your AED's to correct your husband's heart rhythm. Hmmm... Perhaps he can appreciate that."

        show karla basic_wistful_cas
        with chchange

        "Mom smiles sadly."
        kamo "He probably would. Or rather... He'd probably be very troubled if it had been the competition's equipment that saved his life..."
        "She sighs before continuing."
        kamo "The CEO of a company specializing in heart equipment suffering a heart attack... It sounds unreal, doesn't it?"
        "Doctor McElroy chuckles briefly."
        dc "Not to me, to be honest. I've worked in a hospital in the past where I worked alongside another cardiologist who ended up suffering a minor heart attack himself."
        dc "One of my old friends from university is a respiratory physician who's also an avid smoker whenever he's not on duty. And plenty of dentists have cavities from time to time."
        dc "All of us are still only human, Mrs Satou. It's not uncommon to be knowledgable about illnesses or conditions and still fall prey to them, yourself."
        dc "In fact, sometimes merely being knowledgable about something helps us fool ourselves into believing it won't happen to us..."
        "His expression turns slightly more serious."
        dc "...even in the face of overwhelming evidence to the contrary. But we can talk about that later. It's probably best if I give you an update on his condition first."

        show karla basic_lillyface_cas
        show lilly basic_listen
        with chchange

        kamo "Yes, that would be appreciated."
        dc "The gist of it would be that your husband has been extremely lucky. Lucky that an ambulance was called immediately and that the ambulance crew was warned beforehand that it was probably a heart attack."
        dc "Lucky to quickly receive CPR. And lucky that you live so close to the hospital."

        show lilly basic_smile
        with chchange

        "Lilly immediately perks up at the doctor's words."
        li "Doctor, are you saying that my father will probably make a full recovery?"
        dc "From what we've been able to see, he doesn't appear to have suffered any brain damage. He can truly thank his lucky stars for that. However, I'm not sure if I can call his upcoming recovery process a ‘full recovery’."

        show lilly basic_displeased
        with chchange

        dc "His fractured ribs will hurt him for some time, but they will heal completely eventually. His heart is a more complex story. A heart simply cannot get away from an event such as this completely unscathed."
        dc "Under the right circumstances, such as a healthy lifestyle, he will be able to avoid this sort of thing from ever repeating itself."
        dc "But the fact remains that someone who suffers from a heart attack will run an increased risk of further heart attacks in the future. That is something he cannot afford to ever ignore."

        show karla basic_ponder_cas
        with chchange

        "Mom nods."
        kamo "A healthy lifestyle... Stress-free, I presume?"
        dc "Yes. A heart attack caused by stress-related high blood pressure is a worst-case scenario, but as you have learned, even worst-case scenarios take place from time to time."
        dc "I understand that your husband has been under a lot of stress?"
        kamo "I'm afraid so. We're on the verge of taking over a company abroad, and there's been a second interested party who hasn't completely left the picture yet. All in all, it's been a very trying time."
        kamo "We were planning a vacation after this was all over, but until then, things would be extremely busy. The knowledge that he couldn't afford to fall ill right now may even have been an additional factor of stress."
        dc "Your health starts faltering, you start worrying about what happens if you were to be put out of commission, you become more stressed, your health starts dropping more, so you start worrying more, etcetera, etcetera."
        dc "That sort of thing can indeed create a vicious circle that is quite hard to get out of."

        show lilly basic_concerned
        with chchange

        "Lilly sighs."
        li "And despite everything he also committed to a trip with my friends and me, despite the fact that it required him to squeeze his workload into an even smaller timespan. If only..."
        "The doctor scrapes his throat to cut off Lilly's remark."

        show lilly basic_displeased
        with chchange

        dc "Please do not oversimplify the situation, Miss Satou. Maybe what you mentioned was the straw that broke the camel's back, and maybe it wasn't."
        dc "Maybe he could have lasted until that vacation your mother spoke of, or maybe something else would have caused things to fall apart."
        dc "I think the right thing to contemplate on right now isn't that last straw, but all the others that were already there."
        aki "I think the doctor has a point, Lilly. The responsibility for this ultimately lies with Dad and not with you. He must have had at least a minor suspicion of where he was headed."
        aki "I mean, when you spoke to his general practitioner on the phone, the man immediately told you to have a cardiologist look at Dad."
        aki "That's a pretty quick conclusion to jump to without any context, so my gut says he knew about Dad's situation. It may have been going on for some time."
        "The doctor nods his head."
        dc "We spoke to his general practitioner to get his account of things, too. The last time he saw your father was quite some time ago, but your father was somewhat of a risk case even then."

        stop music fadeout 2.0

        dc "According to doctor Thompson, your father has had high blood pressure for years. The only thing that surprised doctor Thompson was how long your father still managed to last."

        play music music_drama fadein 4.0

        show lilly basic_concerned
        with chchange

        "Son of a bitch! Years? I shake my head in disbelief. How stupid can a person get? How important was this company expansion for him to go this far?"
        "Lilly barely manages to conceal a shocked gasp. Mom's face, on the other hand, is completely neutral."
        "I wonder how much she knows..."
        "It feels inappropriate to ask with the doctor nearby, so I swallow the remark I was about to make. After a moment of silence, Mom speaks up."
        kamo "I suppose your comment about how tempting it is to believe these sorts of things only happen to others is particularly true here."
        dc "...I suppose so."

        show karla basic_sad_cas
        show lilly basic_sad
        with chchange

        kamo "So... What will happen now? And when do you think he can go home?"
        dc "He is going to need a lot of time to recover. If you like, it's okay for you to go and visit him after you leave here if he's awake."
        dc "How long we decide to keep him here will depend on how well his recovery progresses. It's still too early to make an accurate prediction."
        kamo "He'd probably feel more comfortable recuperating at home than in a hospital room. We could hire a private duty nurse to keep an eye on him while he recovers."
        kamo "We live very close to Raigmore, so dropping by for a daily checkup would not be impractical."
        dc "We can consider that once he has recovered a bit. At this point, we still like to keep a close eye on him ourselves. We will reevaluate his situation in a week or two."

        show karla basic_lillyface_cas
        with chchange

        kamo "Of course."
        dc "We can make an appointment next week to discuss the future. We will probably have a better idea of when he can leave the hospital."
        dc "When you schedule a new appointment with the desk workers down the hall, they will be able to provide you with some pamphlets about how to adjust one's lifestyle in order to prevent further heart attacks."
        kamo "I'll be sure to read them. But, doctor..."

        show karla basic_distant_cas
        with chchange

        "She pauses for a moment, almost as if not entirely sure if she's prepared for the answer."
        kamo "...will he be able to return to work eventually, or is this the definite end of his career?"
        dc "Given how far he's gone, I can only imagine that his job is very important to him."

        show karla basic_sad_cas
        with chchange

        kamo "It's a bit complicated. He runs a family company, and family companies don't stop being part of one's life after retirement, voluntary or otherwise."
        kamo "In fact, I think the company's always been part of his life, even when he was still attending school."
        dc "We try to encourage people who are recovering from a heart attack to try and lead a life that's as normal as possible after their recuperation. Having a daily rhythm and interaction with colleagues is part of that."
        dc "But the lifestyle your husband used to live cannot be described as normal or healthy. That lifestyle will have to change. He will have to pay more attention to his own needs from now on."
        dc "It will be up to him to determine whether his current job and a healthy and stress-free lifestyle are two things that can be reconciled with one another or not."

        show karla basic_lillyface_cas
        with chchange

        kamo "We will keep that in mind. Thank you for your time, doctor."

        scene bg raigmore_waitcard
        show lilly cane_reminisce
        with locationchange

        "We leave the office, and Mom heads over to the information desk to schedule a new appointment."
        "I look at Lilly and notice she has a troubled look on her face. I give her a subtle nudge."

        show lilly cane_reminisce_close
        with characlose

        aki "I bet I know what's bugging you, Sis. This whole meeting was pretty run-of-the-mill, except for that one revelation."
        "Lilly nods sullenly."

        show lilly cane_concerned_close
        with chchange

        li "He knew... for years..."
        aki "He knew he was a risk case for years, but the question remains whether anybody else besides that general practitioner knew about this."
        aki "Well, I'm curious about one person in particular. She put on one hell of a poker face just now."
        li "I... don't want to believe that she knew... and did nothing. When I spoke with her on the phone that evening, she even said..."
        aki "Yeah, if she knew then that's a real problem. But would it really be a relief to you if she didn't know, Lils?"

        show lilly cane_reminisce_close
        with chchange

        li "What do you mean?"
        aki "If she didn't know, that has implications too. You might not like those either."
        li "..."
        aki "How much do we really know about Mom and Dad? It's been six years, and back when we were living with them, we were living in a completely different environment."
        aki "Things have changed. They've changed, too, that much is obvious. Especially Mom."
        aki "Maybe... that new start they talked about earlier wasn't just about patching things up between us and them. Maybe.."
        li "Maybe...?"
        aki "She's coming back. We might as well ask her now."

        show lilly cane_concerned_close
        with chchange

        li "I'm not sure if now is the appropriate time."
        aki "Well, I'd sure as hell like to make sense of all this."

        show karla basic_resigned_cas at tworight
        show lilly cane_sad at twoleft
        with charaenter

        stop music fadeout 2.0
        queue music music_rain fadein 4.0

        "As Mom comes back from the desk, she has a weary expression on her face."
        kamo "I've made an appointment for next week. You can come along again if you like, but I won't force you to."
        aki "So what now, Mom? We're gonna walk out of here and pretend the elephant in the room is just part of the furniture? The doctor played along just now, but that's not gonna work a second time. What the hell is going on here?"

        show karla basic_sad_cas
        with chchange

        kamo "What indeed..."

        show lilly cane_reminisce
        with chchange

        li "Mother, do you remember that phone call we had on the evening of...? You said things would probably be fine. That he'd be able to handle a few more weeks."
        aki "If Lilly had taken your words at face value back then instead of calling a doctor, we'd probably be arranging a funeral right now. How much did you know about Dad's condition?"

        show karla basic_lost_cas
        with chchange

        kamo "If I had known that your father's had high blood pressure for years, do you really think I would have told Lilly not to worry? What kind of person do you think I am?"

        show lilly cane_sad
        with chchange

        "Lilly breathes a soft sigh of relief, but I'm not done with Mom yet."
        aki "I'm not sure what kind of person you are. I believe you when you say that what doctor McElroy just said was new to you, too, but that does beg the question why you didn't know and how you couldn't have known about it."
        aki "The two of you lived in the same house and worked at the same office. When he went to see doctor Thompson, didn't you bother to ask why he went or what the doctor said?"
        kamo "I would have, if I had known he went there in the first place. He must have gone there at a time I was away from the home."
        aki "Well, he certainly wasn't hurting for opportunities in that case."

        show karla basic_frown_cas
        with chchange

        "Mom folds her arms in a slightly defensive manner."
        kamo "Akira, what is this about?"
        aki "I haven't been here for very long, but one thing everyone at the office who knows you agreed upon is that you always seem to be involved in a thousand things at once."
        aki "Committees, social events, charity work, you name it. But I also got the impression that there's one thing you weren't very involved in at all, and that was your interaction with Dad outside the office."
        aki "You two have been living completely separate lives over the years. So it's not that surprising that he didn't tell you. Why would he? You've been just as neglectful of him as you've been of us."

        show lilly cane_concerned
        with chchange

        "Lilly's expression becomes pained upon hearing my harsh words."
        li "Akira... Please, not now."
        "Mom averts her eyes for a second."

        show karla basic_distant_cas
        with chchange

        kamo "I'm not gonna try and justify the lack of contact between the three of us, but your father... was actually okay with the way we lived our lives."
        kamo "He knew that... if he ever needed me to be there for him... I'd drop everything else immediately. I swore a solemn oath to him, and I have reminded him of it... several times."
        "I shake my head in disbelief."
        aki "You'd drop everything else and be a wife to him as long as he asked you? What kind of sorry marriage has agreements like that? Was that part of your wedding vows?"
        aki "Heck, why did you even marry Dad to begin with? Did you even like him, or did you just want to marry into a wealthy and prestigious family?"

        show karla basic_angry_cas
        with chchangefast

        kamo "Oh, shut up Akira!"
        "I might have gotten carried away a bit. Mom's eyes narrow, and she clenches her right hand into a fist."
        "From the shaking of her hand, I get the impression she's at least playing with the idea of punching me."
        "She holds back, but she shoots me a death glare that is intense enough to send a shiver up my spine before spitting out a vicious retort."
        kamo "Stop ignorantly lecturing me on things you know nothing about!"

        show lilly cane_cry
        with chchange

        "Even though Mom limited herself to merely hitting back with words, Lilly reels as if someone slapped her in the face."
        li "M-Mother, Akira... Please... just... stop this."
        "The distressed look on Lilly's face makes my anger fade a bit and replaces it with embarassment. Judging from the expression on Mom's face, she's probably feeling the same."

        show lilly cane_concerned
        show karla basic_sad_cas
        with chchange

        aki "Sorry, Sis."
        kamo "Yes, sorry dear."
        kamo "{i}*sigh*{/i} Let's not make a scene here, okay?"
        aki "Okay."
        "She hesitates for a bit."
        kamo "If the two of you want to pay him a visit, now's probably a good time."

        show lilly cane_sad
        with chchange

        li "Yes."
        kamo "Akira, you don't mind dropping off Lilly afterwards, do you?"
        li "Excuse me, but... You're not coming along, Mother?"

        show karla basic_resigned_cas
        with chchange

        kamo "I'll pay him a visit this evening. Right now, I need to think about a few things. I don't want to end up saying something to him in front of you two that I might regret later."

        show lilly cane_concerned
        with chchange

        li "..."
        aki "...Fine. I'll give her a ride afterwards."
        kamo "Alright. I'll talk to you later, then."

        hide karla
        with charaexit

        "She gives us a nod and then walks off."

        scene bg raigmore_hallway
        with locationchange

        "As we start walking towards the hospital room where Dad's staying, I take a look at Lilly and notice she looks extremely troubled."
        "I sigh."
        aki "Do you believe her?"

        show lilly cane_displeased
        with chchange

        li "I... I do. She seemed sincerely offended at your words."
        "I notice a slightly accusing tone in her voice. It's only barely noticable, and I might have missed it if I wasn't so used to the subtleties of my sister's way of speaking."
        aki "You think I went too far?"

        show lilly cane_sad
        with chchange

        li "It... wasn't very respectful."
        aki "Maybe not. But they're probably already used to this kind of thing from me."
        li "I don't think that's true, or Mother wouldn't have sounded so angry."
        aki "Listen, I get that I'm being confrontational, but someone has to call them out on their actions, Sis. And if I'm doing this, that means you don't have to."
        aki "Anyway, this kinda confirms that you made the right decision earlier, doesn't it?"

        show lilly cane_reminisce
        with chchange

        li "What do you mean?"
        aki "You came this close to giving up your life and new little surrogate family at Yamaku under the assumption that at least you'd get your old family back in return."
        aki "Now it turns out that, instead of a family, there's just two people here who were doing whatever the hell they wanted without paying much attention to what the other was up to."
        aki "That wasn't worth giving up your life at Yamaku for, Sis. Not by a long shot. In the end, it still would have been you and me here, just like back in Japan six years ago."

        show lilly cane_concerned
        with chchange

        li "I... I need to let all of this sink in. I need to think... about things."
        aki "There'll be time for that later. We're here."
        "Just as we arrive at room 702, I see a nurse walking out of it."
        aki "Excuse me, miss. Is Mister Satou awake right now?"
        "She nods."
        "Nurse" "He is. You can go and visit him if you like."

        show lilly cane_sad
        with chchange

        "I look at Lilly."
        aki "Well, here goes nothing."

        if _in_replay:
            return

    label .s3:

        $ set_window_tint(TINT_AKIRA)

        scene bg raigmore_room
        with locationchange

        play sound sfx_doorclose

        play ambient sfx_ekg volume 0.8 fadein 2.0

        if _in_replay:
            play music music_rain fadein 4.0

        "As we enter the room and close the door behind us, the bustling of the hallways fades away and is replaced by an almost oppressive silence that's only disrupted by the steady high-pitched beep of a nearby EKG monitor."
        "I get a strange feeling of déjà vu as we walk further into the room and towards the bed housing the room's only occupant."
        "I remember visiting Hisao while he was hospitalized together with Lilly, Shizune, and Misha and feeling a similar atmosphere when I entered his room. That feels so long ago, despite it only being like a month away."

        scene ev bedridden_akira_lilly
        with charachangeev

        "Hisao did look a lot less sordid than the person lying before us here."
        "Unshaven, an IV needle sticking in his arm, and the movement of his chest betraying a strained breathing, Dad looks at least a decade older than he really is."
        "The expression in his eyes is less sharp and probing than it usually is, probably due to the painkillers he's on, but he's definitely conscious as I can see his gaze following us as we make our way over to the bed."
        "He gives a short sigh as an indication that he's aware of our presence."
        li "Hello, Father."
        aki "Nice to see you're awake, Dad."
        hyd "..."
        "There's a soft sound, but if it was a mumble, it was too soft for even Lilly to comprehend. That familiar worrying expression appears on my sister's face in response."
        li "Father... Are you in a lot of pain?"
        hyd "{cps=20}I... fine.{/cps}"
        "Those fractured ribs of his probably make even taking deep breaths painful, and his first reaction is to claim he's fine. I shrug."
        aki "His definition of ‘fine’ is still the same as it was just before this whole mess started, Sis. I'll leave it up to you to decide whether you want me to describe what he looks like, but ‘fine’ is not a word I'd use right now."
        "Lilly merely smiles sheepishly and then goes back to her worrying tone."
        li "You don't have to talk, Father. If you really need to say something, just whisper. Please don't strain yourself."
        hyd "{cps=20}Your... mother... not here?{/cps}"
        "Lilly smiles and shakes her head."
        li "Mother will be keeping you company this evening."
        "That's leaving out one heck of an important detail."
        aki "Maybe in the meantime, you could think about what you're gonna tell her. We just had a talk with your cardiologist who in turn had a talk with your general practitioner."
        aki "Turns out he knew you were a risk case, and you knew that too. What on earth were you thinking?"
        "A long silence follows."
        "I wonder if he expected us to find out about this. I can see Lilly fidgeting a bit. She obviously doesn't really like where this is going, but at the same time, I bet she's curious herself."
        hyd "{cps=20}I... could not... just stop... just before... the... end. My... honor... was at... st-stake... here.{/cps}"

        show ev bedridden_akira_shout
        with charachangeev

        aki "Honor? Give me a break! You think you're some sort of samurai who'll be fondly remembered by everyone who knew him if he bravely dies in the line of duty while serving his lord or something?"
        aki "I bet most people at the office here would have thought of you as a fool."
        aki "Heh, maybe those guys on the board of directors would have put a memorial plaque in place in your honor at the Japanese branch, assuming the ambulance crew wouldn't have ended up thwarting things."
        hyd "{cps=20}What... do... you... mean?{/cps}"
        aki "You ever thought of what would have happened if Hanako hadn't been there to give you CPR on the spot, but the ambulance team would still have arrived just in time to save some of your basic brain functions?"
        aki "You would have spent the next decade or two mumbling random gibberish at your wife and daughters while they're busy changing your daily diapers. The board members would have denied your very existence out of embarrassment."
        aki "If you think that's an exaggeration, then maybe we can take a look around here at the hospital. They may have heart attack victims here who weren't as lucky as you've been."
        hyd "..."
        "I can see that his medication hasn't left him fuzzy enough to miss the implication of my comment, and he looks uncomfortable upon imagining that scenario. Looks like that wasn't part of his risk calculation after all."
        aki "Besides, this isn't about the last couple of weeks or the last couple of months. You were told you had high blood pressure years ago. Why on earth didn't you take it easier back then?"
        hyd "{cps=20}Could... not... afford to... yet...{/cps}"
        aki "Could not afford to? Even a couple of years ago, you could have retired and lived out the rest of your days in comfort. This was simply about your ego."
        hyd "{cps=20}...no way... to... speak to... a parent... Akira.{/cps}"
        hyd "{cps=20}You... show... respect... for once... This was... about... your... education... and... financial future... too. And es... especially... Lilly's.{/cps}"
        "That excuse again. Lilly looks a bit distressed upon hearing Father's words."
        li "My financial future, Father?"
        hyd "{cps=20}We... have been... setting... trust fund... for your... cial future... during our... time here.{/cps}"
        li "A trust fund?"
        hyd "{cps=20}Yes... so even... in... the long run... you will... always be... well... provided for.{/cps}"
        hyd "{cps=20}Even... if you... would not... find a... husband... at some point, you... would still... be able... to live... without worry, L-Lilly.{/cps}"
        "Well-provided for? I wonder if he realizes how extremely patronizing he's sounding."
        "Lilly certainly realizes it, too, and I can see an angry expression on her face."
        "She's making an active effort to keep her composure. The sight of her hurt expression suddenly pisses me off to no end, and I sling an angry retort back at the old man."
        aki "She doesn't want your damn trust fund."

        stop music fadeout 4.0

        hyd "{cps=20}But... she... will... probably... need... it.{/cps}"

        scene bg raigmore_room
        with locationchange

        queue music music_sadness fadein 4.0

        show lilly cane_mad_close
        with charaenter

        pause 1.0

        show lilly cane_offended_close
        with charachangealways

        pause 1.0

        show lilly back_listen at left
        with charachangealways

        pause 0.5

        play sound sfx_dooropen

        hide lilly
        with charaexit

        "Lilly doesn't answer, but I can see the corner of her mouth twitching slightly, and just when I start expecting her to either give Dad a piece of her mind or send him a fake smile, she turns around and walks out of the room without saying a single word."
        "I recover from the surprise sooner than Dad and give him a dirty look."
        aki "When Mom comes here this evening, it'd be smart to treat her with more respect, or you'll burn what might be the last bridge you have left."
        "And with that, I leave the room."

        stop ambient fadeout 1.0

        scene bg raigmore_hallway
        with locationchange

        play sound sfx_doorclose

        "I go after my sister, who's already half-way down the corridor before I catch up with her."

        show lilly back_listen_cas_close at twoleft
        with charaenter

        aki "Sis?"
        "Lilly doesn't immediately respond and merely sighs."

        show lilly back_sad_cas_close
        with charachangealways

        "For a moment I think she's going to turn around and walk back to Dad to apologize to him, but that doesn't happen."
        aki "I'll take you to the car, okay?"
        li "Yes..."

        scene bg raigmore_entrance
        with locationchange

        show lilly cane_displeased_cas_close at twoleft
        with charaenter

        "I allow her to take my sleeve, and we walk back to the parking lot."
        "I notice she seems to move with a little bit more hesitation than before, but she doesn't stop walking for a single moment."

        scene bg akira_car
        with locationchange

        "We make our way to the car, but before I start the engine, I give an exasperated sigh."
        aki "Well, this was certainly illuminating. I wonder if what happened just now is courtesy of those painkillers he's on."

        show lilly basic_displeased_cas_close at twoleft
        with charaenter

        li "Do you mean to say he may have... not been himself?"
        aki "He wasn't completely out of it or anything, but he was probably a little too fuzzy to be able to carefully choose and weigh his words like he usually does."
        li "The mindset behind it is still the same though, isn't it? Whether it's sugarcoated or not doesn't really matter."
        aki "Yeah. Crap with cream on top is still crap."
        "I start the car, and we head to our parents' home."

        scene bg satou_entrance
        with shorttimeskip

        "After a short drive, we arrive. Lilly hasn't said a single word the entire time, which is a bit worrying."
        aki "Okay, we're back. The front door is at twelve o' clock when you get out."

        show lilly cane_sad_cas_close at twoleft
        with charaenter

        li "Thank you."
        aki "Hey Sis, you've been kind of quiet. You... uh... want to talk about this?"

        show lilly cane_concerned_cas_close
        with chchange

        li "...Thank you, Akira. But I'd like to think some more first."

        show lilly cane_displeased_cas_close
        with charachangealways

        "We get out and we say our goodbyes, but as Lilly turns around and heads for the front door, I suddenly think of something and put a hand on her shoulder."
        aki "Hey Sis, I've been thinking... Have you considered the option of accompanying Hanako and Hisao back to Japan? I could drop by the airport and see if I can secure an additional ticket for that particular flight."
        aki "It might be better than having to put up with stuff like what just happened for an extended amount of time. A premature departure might just send a hint with enough impact to last."
        "Curiously enough, Lilly doesn't immediately react."

        show lilly cane_offended_cas_close
        with charachangealways

        pause 1.0

        show lilly back_listen_cas_close
        with charachangealways

        pause 0.5

        "Just when I'm about to repeat my question, she unexpectedly shrugs off my hand in an almost mechanical way, and her parting words, uttered just before she opens the front door and walks in, sound cold enough to send a tingle down my spine."
        li "...have a nice evening, Akira."

        hide lilly
        with charaexit

        play sound sfx_doorclose

        "The fact that my younger sister gave me the cold shoulder, probably for the first time in her life, takes a moment to sink in."
        "When I get back in the car I feel exhausted and just a bit unsettled as well."

        scene bg akira_car
        with locationchange

        "As I start the engine, I let out a weary sigh."
        aki "This situation is getting messier with every passing moment..."

        stop music fadeout 3.0

        scene black
        with endchapter

        if _in_replay:
            return

    return