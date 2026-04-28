label sh_ch45:
    label .s1:

        $ set_window_tint(TINT_LILLY)

        call sisterhood_timeskip_broken(silent=True)

        scene bg school_roof at left
        with locationchange

        play music music_daily fadein 4.0
        play ambient sfx_rooftop volume 0.6 fadein 4.0

        li "Hanako?"

        play sound sfx_rustling

        "As I reach the roof of the school, I hear some shuffling sounds nearby, suggesting that someone's up here."
        "I softly call out, hoping it's my best friend."
        "The cramming classes are having lunch break right now, and since Hanako wasn't in the tea room, I came up here to determine if she decided to retreat here instead."

        nvl clear
        nvl show dissolve

        n "Since there are only a handful of weeks left before the exams, cramming season is in full swing. Those who did well on the mock exams are free to determine where they want to study, be it their dorm room, the library, or some of the classrooms reserved for that purpose."
        n "{vspace=30}I usually prefer the peace and quiet of my dorm room, so the only time I'm in the school building these days is early in the morning or late in the afternoon in order to get exercises or exam questions from previous years from the teachers."
        n "But this morning, I made some tasty curry rice for lunch for myself, and since it turned out to be too much to eat on my own, I decided to see if I could find Hanako and offer to share the rest of my lunch with her. It'd be a good opportunity for us to talk or—if she didn't feel like talking—at least spend some time together. The opportunities for us to spend time with one another have started to become exceedingly rare these days."

        nvl hide dissolve

        show misha perky_smile at twoleft
        with charaenter

        mi "Hey Lilly!"
        "It's not Hanako who answers me, but the voice is nevertheless one I recognize. Still, I find myself wondering who's calling out to me."
        "Shizune and I aren't really hostile towards each other anymore these days, but we're still not exactly close friends either. I don't think Shizune would greet me in such a casual manner, though."
        li "Hello, Misha. Is it just you up here?"

        show misha hips_grin
        with chchange

        mi "Yup. Just me."

        show misha hips_grin_close
        with chchange

        "Misha's probably taking supplementary lessons as well. Her grades have been average for about as long as I've known her, and she probably didn't do much better on the mock exams."
        li "Are you taking a break from supplementary courses?"

        show misha hips_laugh_close
        with chchange

        mi "Pfff, yeah! They're really intense. My brain gets overheated, so fresh air is needed to cool it off. Wahaha~!"
        "It's fairly nice up here, although I'd probably get cold if I stuck around for too long."

        show misha hips_smile_close
        with chchange

        li "It might help to remind yourself that the upcoming exams are a worthy cause."

        show misha perky_sad_close
        with chchange

        mi "Except... I won't be going to any university here, so I can't even say that to myself."
        li "Hmmm? You're not? Then why take the national test?"

        show misha perky_confused_close
        with chchange

        mi "I want to try and transfer to a school in America, but Yamaku won't give me a recomendation unless I improve my grades. So this is kind of my last chance."
        mi "I have to take the test, and the teachers here are going to compare my answer sheet with the national test's answers when they're published. If I do well enough, they'll give me a recomendation anyway."
        li "I think it's great that you have such adventurous plans for the future. I feel that such a dream is definitely worth studying hard for."

        show misha perky_smile_close
        with chchange

        mi "You think so?"
        "I nod my head."
        li "I do. I hope you succeed."
        "Under other circumstances, I would have offered to help Misha improve her English—a vital skill if you want to transfer abroad—but right now, I need to get my own grades in order first."

        show misha perky_weaksmile_close
        with chchange

        mi "Aw, thanks. I hope you guys do well too~!"
        "Now that I think about it, Misha's probably been attending the extra courses together with Hanako and might have seen where she went."
        li "Misha, may I ask if you have seen Hanako today?"

        show misha perky_smile_close
        with chchange

        mi "Yeah, we had English just now, and she was there too."
        li "Do you have any idea where she is now? I've been in our tea room already, but she wasn't there. And since there are so many people using the library to study, I don't think she's there either."

        show misha perky_confused_close
        with chchange

        mi "I think I saw her walk towards the exit after class ended. I'm not sure where she went."
        "I sigh in disappointment."
        li "That's too bad. I wanted to share some of my leftover curry rice with her. But if Hanako's not in the building right now, there's little chance of me finding her before the end of lunch break."

        show misha perky_sad_close
        with chchange

        mi "Sorry."
        li "It's fine. Are you interested in having some instead?"

        show misha perky_confused_close
        with chchange

        mi "Huh? Really?"
        "Why not? I'm already stuffed myself, and it's a waste to throw it away."
        li "Yes."
        "I hold the container with the food in front of me until I feel Misha taking it off my hands."

        show misha hips_grin_close
        with chchange

        mi "Wow, this smells really good. Thanks, Licchan~!"
        "I grin a bit as I hear Misha use the nickname she used to address me with in the early days of the student council."
        "That was obviously before Shizune and I had our falling out. I don't think Misha'd be this forward with me if Shizune had been anywhere nearby."
        li "It's been quite a while since I've heard that nickname. Our early student council days seem so far away now that the exams are nearly upon us, don't they?"

        show misha perky_weaksmile_close
        with chchange

        mi "Makes you feel nostalgic, doesn't it. Don't you sometimes wish you could turn back time?"
        "I would. I'd love to return to the days before Hanako had her breakdown. How carefree those days now feel. What I wouldn't give to go back to that afternoon and talk myself out of making that horribly ill-timed phone call."
        li "It would be wonderful to be able to turn back time and correct mistakes one has made in the past."

        show misha perky_confused_close
        with chchange

        mi "Mistakes?"
        "Misha sounds puzzled and almost a little bit suspicious."

        show misha perky_suspicious_close
        with chchange

        mi "Something related to Hanako, Licchan?"
        "That's a surprise. As far as I know, only Hisao, Naomi, Hanako and myself are aware of what happened at Kasshoku University that day. I don't think Naomi would have told anybody but her best friend about it, seeing that she was really rattled as well."
        li "I'm afraid so. But... Did you hear anything from anyone, Misha?"

        show misha perky_sad_close
        with chchange

        mi "Just some rumors. But everyone can see that something bad happened to Hanako. Even if you don't count her exam results, it's like she's turning back to the way she was... before."
        mi "Like she's started avoiding people again, and she's not working or talking with others in class. It's almost like she never met Hicchan."
        li "Oh dear..."
        "It was obvious from the start that Hanako's confidence and behavior started regressing after that incident, but the notion that pretty much the entire school has noticed this, too, is an unexpected dose of salt in my wounds."
        mi "And you and Hicchan seemed to be kind of down too. Like you were involved in whatever's bothering Hanako. And then the mock exams."
        li "..."
        "That's a sharper deduction than I thought Misha to be capable of. She's usually a little bit oblivious to these kind of subtleties."

        show misha perky_suspicious_close
        with chchange

        $ _sh_mus_pos = renpy.music.get_pos()
        
        stop music fadeout 1.0

        mi "Licchan, you didn't sleep with Hicchan, did you? You wouldn't do such a thing, right?"
        "WHAT ON EARTH?{w} I take back what I just thought."
        li "I beg you pardon?"

        play music f"<from {_sh_mus_pos}>{music_daily}" fadein 2.0

        show misha perky_confused_close
        with chchange

        mi "Well, people were wondering since Hanako started becoming more outgoing after she became Hicchan's girlfriend, maybe she and Hicchan broke up, and that's why she's been so down lately."
        mi "Since the three of you are together so often and you just said that you made a mistake, I thought..."
        "I can't deny there's some logic in that theory, but it still feels wrong on so many levels that I nearly trip over myself in my attempts to deny it."
        li "That isn't even remotely what happened. I'd never do such a thing. Hisao is like a brother to me, and I'd never hurt Hanako by making advances on her boyfriend. Hanako and Hisao are still together, and they're doing fine."
        "To be honest, “doing fine” is probably too positive a spin on things. Hanako's been steadily growing more reclusive over the last few weeks, and I don't think she and Hisao stay over at each other's place anymore, nor do they see each other much."
        "I keep telling myself that we're all simply too busy studying to spend much time with one another, but I'm nevertheless starting to get a little worried at how isolated Hanako is becoming."

        show misha perky_weaksmile_close
        with chchange

        mi "That's a relief. I'd have been disappointed if you did anything that low."
        li "Something happened when we visited an open house day that caused Hanako to become the center of attention, which was very... frightening for her."
        li "I'd rather not go into much more detail, but I hope that's enough to satisfy your curiosity, Misha."

        show misha perky_smile_close
        with chchange

        mi "Oh, sure Licchan. So is that why Hanako did so badly in the mock exams?"
        li "Misha, how did you learn about Hanako's exam results?"

        show misha perky_confused_close
        with chchange

        mi "Oh, uh... There was a list with the exam results among the paperwork in the student council room. Hanako's mark kinda stood out."
        li "Was it really that bad?"

        show misha perky_sad_close
        with chchange

        mi "She scored... ah... a twenty six on average on the exams."
        "That's even worse than I thought. I'm shocked into silence for several seconds."
        li "Oh my god..."
        mi "Kinda of makes you wonder if she had a blackout during the tests."
        "Or a panic attack. Or several. That might have been what happened."
        li "Perhaps."

        show misha perky_weaksmile_close
        with chchange

        mi "If that's what happened, then she might still do well on her exams as long as she can prevent that kind of thing from happening again, right? Right?"
        li "I hope so, Misha. I really hope so."

        play sound sfx_normalbell

        show misha perky_smile
        with chchange

        "The ringing of the school bell makes Misha get up, and it also reminds me that I'd better get back to my studies as well."
        "I say goodbye to my unexpected conversation partner and make my way back to my dorm room."

        stop ambient fadeout 2.0
        stop music fadeout 2.0
        stop sound fadeout 2.0

        if _in_replay:
            return

    label .s2:

        $ set_window_tint(TINT_LILLY)

        scene bg school_dormlilly
        with locationskip

        queue music music_dreamy fadein 4.0

        play ambient sfx_phonering

        "I manage to get two hours of cramming in until my concentration is broken by the ringing of my cell phone."

        stop ambient

        play sound sfx_phonepickup

        li "Good afternoon. Lilly Satou speaking."

        show hisao basic_smile_uni_phone at phonebox
        with charaenter

        hi "Hi, Lilly."
        li "Hello, Hisao. How is your studying coming along?"

        show hisao basic_speak_uni_phone
        with chchange

        hi "Okay, I guess. I've been studying non-stop since eleven. I'm probably about ready to take a break."
        "In other circumstances, I would have asked him to come over so we could have a drink together, but it wouldn't feel right to do so without Hanako."

        show hisao basic_neutral_uni_phone
        with chchange

        li "Perhaps a little walk will do you good. It's a good idea to keep some daily physicaly activity now that you've temporarily suspended your morning runs."

        show hisao basic_speak_uni_phone
        with chchange

        hi "Maybe, but today I've got other plans already."

        show hisao basic_neutral_uni_phone
        with chchange

        li "What is it that you have planned then?"
        hi "I'm paying a visit to Miss Takawa in 20 minutes."
        li "You've made an appointment with her?"

        show hisao basic_speak_uni_phone
        with chchange

        hi "Yeah. I approached her this morning, and she said she'd be able to make some time this afternoon. Would you like to come too?"

        show hisao basic_neutral_uni_phone
        with chchange

        "Why would Hisao want to see Miss Takawa? Is there something specific he wants to talk to her about?"
        li "Ah... If it's not a problem..."

        show hisao basic_speak_uni_phone
        with chchange

        hi "No, I think I'd actually like you to come along."

        show hisao basic_neutral_uni_phone
        with chchange

        li "Hisao, is this about anything in particular?"

        show hisao basic_speak_uni_phone
        with chchange

        hi "I'm not sure. Maybe. Shall we meet in front of the nurses' building in 15 minutes?"

        show hisao basic_smile_uni_phone
        with chchange

        li "I'll be there."

        hide hisao
        with charaexit

        stop music fadeout 2.0

        scene bg school_therapist
        show hisao basic_neutral_uni_close at left
        show takawa smile at tworight
        with locationskip

        queue music music_another fadein 4.0

        ta "Please enjoy."
        li "Thank you."

        show takawa smile_close
        with chchange

        "I put the bowl of tea I just received to my lips and take a careful sip."
        "It's remarkably tasty and has a very unique flavor. I'm almost tempted to ask if Miss Takawa brews her tea herself."

        nvl clear
        nvl show dissolve

        n "I've been in this office once before, the day after our Kasshoku trip, to brief Miss Takawa about the events of the day before, hoping she'd be able to do something for Hanako."
        n "She thanked me graciously for letting her in on what happened to Hanako, but so far, I haven't noticed any moves on the school's part to give her a helping hand. In fact, it seems the opposite has happened."
        n "{vspace=30}While Hisao and I were given exemption from the supplementary lessons most people with our exam results would have been expected to follow, the school has put Hanako in every single supplementary class they had available, and as a result, she's away from the dorms from dawn until dusk."
        n "{vspace=30}It's almost as if they took the lessons Hisao and I were exempted from and put them on Hanako's shoulders. The thought alone is enough to upset me."

        nvl hide dissolve

        ta "Now then..."
        "I hear Miss Takawa put her bowl down and pick up the sound of Hisao impatiently shuffling in place as if he's been forced to stay silent for too long already."

        show takawa weaksmile_close
        with chchange

        ta "How can I be of assistence to the two of you?"
        "I turn towards Hisao slightly in order to let him know he can go ahead. I'm a bit curious about what he has to say myself."

        show hisao basic_speak_uni_close
        with chchange

        hi "Miss Takawa, I realize that Hanako's your client and you're bound by client confidentiality, but what exactly is it that you can and cannot tell us about Hanako?"

        show hisao basic_neutral_uni_close
        show takawa serious_close
        with chchange

        ta "To be honest, just about anything Miss Ikezawa confides in me during our sessions is considered confidential, and divulging any of that would break our bond of trust. I can be a little bit more open regarding my own impressions and opinions."

        show hisao cross_speak_uni_close
        with chchange

        hi "What about treatment?"

        show hisao cross_neutral_uni_close
        show takawa calculating_close
        with chchange

        ta "I'm not overly fond of discussing treatment of my clients with people who aren't part of the school's medical staff."

        show hisao cross_worry_uni_close
        with chchange

        hi "Oh..."

        show takawa serious_close
        with chchange

        ta "I realize that the two of you are here out of concern for Miss Ikezawa, so I'll try to be as accommodating as I can afford to be. Is that okay, Mister Nakai?"

        show hisao basic_neutral_uni_close
        with chchange

        hi "Yeah."

        show takawa smile_close
        with chchange

        ta "Why don't you start at the beginning?"

        show hisao cross_speak_uni_close
        show takawa serious_close
        with chchange

        hi "I ran into Hanako two days ago while at the school's apothecary in order to get a new batch of some of my medication."
        hi "She was startled when she walked in and saw me there, and instead of talking to me, she just nodded nervously and then quickly walked off, almost as if she was fleeing."
        "I frown."
        li "Fleeing? Maybe she went there to... ah..."
        "Get her birth control pills. I used to get them for her, but the last two months before that trip to Kasshoku, Hanako actually managed to work up the courage to get her own. Well, together with me at least."
        "I'm relieved that Hisao manages to grasp my meaning without me having to finish my sentence, but the soft sigh he lets out to dismiss my suggestion stings more than I expected."

        show hisao basic_worry_uni_close
        with chchange

        hi "I don't think so. Besides, I doubt she'd try to avoid me over that. Also, uh..."

        stop music fadeout 2.0

        show takawa calculating_close
        with chchange

        ta "Please proceed, Mister Nakai."

        queue music music_moonlight fadein 4.0

        show takawa serious_close
        with chchange

        hi "Yesterday, I briefly spoke with Hanako. She returned some of my notes that I allowed her to copy. When she took them out of her bag, I noticed a small bottle of pills in there."
        hi "It was only a split-second, but for me that was enough. I know a pill bottle when I see one. I doubt they were sleeping pills either. She'd keep those in her nightstand."
        li "Hisao, are you saying that Hanako's on medication?"

        show hisao cross_worry_uni_close
        with chchange

        hi "When I put two and two together, it's kinda hard to come to any other conclusion. I was hoping to get confirmation here, as well as what this says about Hanako's current condition."

        show takawa devious_close
        with chchange

        ta "Mister Nakai, as a woman I feel compelled to point out that it is rather ungentlemanly to rummage through a lady's handbag, even with your eyes. Don't you agree, Miss Satou?"

        show hisao cross_frown_uni_close
        with chchange

        "I hear Hisao let out a soft grunt of frustration as Miss Takawa playfully deflects his question. I force a smile as I reply."
        li "I... agree on that, Miss Takawa. But since we now know about it, perhaps you can give us some reassurance instead of leaving us to draw our own conclusions which might be worse than her actual situation."

        show takawa worried_close
        show hisao cross_neutral_uni_close
        with chchange

        ta "Hmmm..."
        "A long silence."

        show takawa calculating_close
        with chchange

        ta "Very well, then. What I prescribed Miss Ikezawa is some medication to help her sleep better at night and some light antidepressants to stabilize her mood."
        ta "Both are light dosages and we're only supplying her with very small batches at a time, so the chance of her growing dependent on them is extremely slim. We're keeping a close eye on things."

        show hisao basic_worry_uni_close
        with chchange

        hi "So, Hanako's... officially suffering from depression?"

        show takawa serious_close
        with chchange

        ta "Things are what they are, with or without some stamp from a mental health official. If what I'm saying is anything but a confirmation of what you must have known already, I may have overestimated your friendship with her."
        "I shake my head."
        li "It isn't. But it still hurts to hear you confirm it."

        show takawa weaksmile_close
        with chchange

        ta "Now that you know, perhaps I could ask you to... pay attention to Miss Ikezawa whenever you interact with her and let me know if you notice anything that could be a side-effect of the medication."

        show hisao cross_speak_uni_close
        with chchange

        hi "We will. But Miss Takawa..."

        show takawa smile_close
        with chchange

        ta "Yes, Mister Nakai?"
        hi "I think I speak for Lilly as well when I say that we'd really like to do more for Hanako than just watch out for potential side effects of her medication. We want to help her through this in any way we can, but it's getting harder and harder to get through to her."
        hi "During Hanako's last crisis, you had some very useful advice. We were hoping you could help out this time as well."
        "I nod decively as a sign of agreement with Hisao's words."
        li "Whatever it takes."

        show hisao basic_neutral_uni_close
        show takawa worried_close
        with chchange

        ta "I'm glad to hear that from the two of you. In addition to simply being there for her during the sparse moments she may desire company, there is one specific thing you two can do that would greatly help."

        show hisao basic_speak_uni_close
        with chchange

        hi "And what is that?"

        show takawa sweet_close
        with chchange

        ta "Study hard and pass your exams."

        show hisao cross_frown_uni_close
        show takawa happy_close
        with chchange

        "The sigh in stereo that results from both of us causes the old lady to chuckle."
        ta "It sounds like that wasn't quite what you were expecting to hear."
        hi "It's not that we don't understand that our own exams are important too, but..."

        show takawa stern_close
        show hisao basic_worry_uni_close
        with chchange

        "The old woman sighs."
        ta "You two managed to solve your falling out with Miss Ikezawa the last time by saying the right things at the right time, and I suppose you were expecting me to point out a similar approach that could make all the pieces fall into place and solve this crisis that Miss Ikezawa is going through."
        ta "But the last time it was a crisis directly related to your relationship with her. This situation is about..."

        show takawa worried_close
        show hisao basic_neutral_uni_close
        with chchange

        "She pauses shortly."
        ta "...something else. There are simply no ‘right words’ to quickly solve this situation. Not this time. I'm sorry if I dashed your hopes just now."

        show takawa serious_close
        show hisao basic_worry_uni_close
        with chchange

        hi "About a week after that open house day, Hanako told me that all she managed to adapt to was life at this particular school and that she still wouldn't be able to function beyond the safe confines of Yamaku."
        hi "She felt that when she leaves here after graduation, she'll still be the same person who came here nearly three years ago."

        show takawa stern_close
        with chchange

        ta "I don't share that opinion, and I'm certain that you don't either."

        show hisao cross_speak_uni_close
        with chchange

        hi "I don't."
        li "Me neither."

        show hisao basic_neutral_uni_close
        show takawa calculating_close
        with chchange

        ta "There's probably another factor that plays a role here. This is just a theory of mine, but try to look at things from her point of view. This school is where she has lived for the last three years. Until recently she barely ever left the premises."
        ta "Most of the pleasant memories she's had this decade are all connected to this school in one way or another. All the people who are part of her life right now are connected to this school in one way or another as well."

        show takawa worried_close
        with chchange

        ta "When you take away the connecting factor that all things have in common, wouldn't you feel anxious at the thought of leaving here, wondering just how much of your life will remain intact once you graduate?"
        ta "I imagine that that realization must have dawned on Miss Ikezawa during the open house day while she was wandering about the campus of a strange school that, assuming she passes her exams, will become her new world very soon."

        show takawa weaksmile_close
        with chchange

        "I never really thought of that before, but it does make sense. Yamaku has literally been Hanako's world for the last three years, and after graduation, she'll be forced to leave its safety."
        "I wonder if, had Mother and Father not returned to Japan, I would have felt something similar right about now."

        show hisao cross_worry_uni_close
        with chchange

        hi "I can understand why she'd feel uneasy about that. But... Lilly and I are still here. We're studying so hard because if we all pass our entrance exams, we can still attend the same university. We can still hang out with her."

        show takawa happy_close
        with chchange

        ta "Yes. You and Miss Satou could be... sources of stability... in Miss Ikezawa's life. But you can only fulfill that role if your own situation is stable. And there is another motivation to study hard as well."
        "Sources of stability?"

        show hisao basic_speak_uni_close
        with chchange

        hi "What motivation?"
        "Sources of stability..."

        show hisao basic_neutral_uni_close
        show takawa calculating_close
        with chchange

        ta "May I ask whether Miss Ikezawa knows about your own mock exam results?"

        show hisao cross_speak_uni_close
        with chchange

        hi "She does. We looked her up in her room the day we got them back and mentioned our grades to her."

        show hisao cross_neutral_uni_close
        with chchange

        ta "And how did she react to them?"

        show hisao basic_worry_uni_close
        with chchange

        hi "Kind of horrified. And then guilty. When we left the room she actually apologized to us."

        show takawa worried_close
        with chchange

        ta "I was afraid of that. You may be worried about Miss Ikezawa, but it's clear that she's also worried about you."
        ta "I can see her blaming herself for what happened at Kasshoku, and she is very likely to blame herself for anything that happened as a result of the fallout of that incident. Which included your recent grades, unfortunately."
        "Even though it isn't her fault. She wasn't the one who made that phone call. That was me."

        show hisao basic_neutral_uni_close
        with chchange

        hi "I suppose we got lucky we both got exemption from the supplementary courses or Hanako probably would have blamed herself for that as well."

        show takawa smile_close
        with chchange

        "The old therapist doesn't immediately respond, almost as if waiting for something, and suddenly I have a flash of insight that causes me to let out a small gasp."
        li "Miss Takawa. Did you have a hand in arranging the exemption Hisao and I received?"
        ta "Hmm, hmmm. Clever deduction, Miss Satou. I was indeed the one who put in a request with your homeroom teachers to let the two of you off the hook this time."

        show hisao cross_speak_uni_close
        with chchange

        hi "So this was done for Hanako's benefit?"

        show takawa devious_close
        show hisao cross_neutral_uni_close
        with chchange

        ta "Indeed. We cannot reverse Miss Ikezawa's current situation, but we can make it easier on her by making sure she isn't feeling guilty about the two of you being forced to attend cramming sessions in class."
        ta "Like the medication, it's a measure on the part of the school to make the upcoming time easier for her to get through."
        ta "Of course, this puts some additional responsibility on your shoulders to perform well, even without those extra lessons, so be sure to honor this gesture of goodwill."
        li "Thank you."

        show takawa serious_close
        show hisao basic_frown_uni_close
        with chchange

        hi "It's appreciated alright, but why give us exemption and not Hanako? You're talking about the school doing its part to help Hanako through this, but she's nevertheless being punished for doing badly at the mock exams, even though she studied really hard beforehand."
        li "I agree with Hisao. It seems like the school is overloading Hanako with supplementary lessons even though I suspect she's already familiar with most of what's being taught there."
        li "Those low grades weren't her fault. It wouldn't surprise me if she had a blackout or panic attack during the mock exams that caused her to fail them."

        show takawa calculating_close
        show hisao basic_neutral_uni_close
        with chchange

        ta "I agree with your reasoning about the probable cause of Miss Ikezawa's low grades, but please don't regard Miss Ikezawa's participation in the extra classes as a punishment of some sort. The school is merely doing what we deem best for her."
        li "I'm not sure I understand."

        show takawa serious_close
        with chchange

        ta "The alternative to what we did would have been to exempt her, too, and allow her to study on her own. But the worst thing you can do to someone suffering from depression is giving them the opportunity to stay in their room all day long."
        "My thoughts return briefly to Mother and how she complained to me before about how Father would just stay in bed nearly all day long and didn't seem to have motivation to do anything."
        li "That makes... sense, I suppose. But still..."
        ta "It is important for her to maintain a daily routine for as long as possible as this has a beneficial effect on people suffering from depression."
        ta "In addition to that, this approach allows us to guarantee that there will be a teacher keeping an eye on her throughout the day who can also verify how well she's doing with the various subjects."

        show takawa calculating_close
        with chchange

        ta "I realize that forcing all these lessons on her may seem a harsh thing to do, but I believe that this is the best way to give her a chance of succeeding at next month's test."
        ta "And as an added benefit, the two of you will be able to concentrate on your own studies without needing to worry about her for most of the day. The last thing we need is some kind of worry feedback loop between you and Miss Ikezawa that puts your own exam performance at risk."
        hi "You seem really worried about how we do on our exams."

        show takawa serious_close
        show hisao cross_neutral_uni_close
        with chchange

        ta "I wouldn't have asked your homeroom teachers for an exemption if I didn't have faith in your ability to pass the exams. The reason I'm emphasizing the importance of passing your exams is the fact that this situation has upped the stakes significantly."
        li "The stakes?"

        show takawa worried_close
        with chchange

        ta "If you two fail the upcoming National Center Test, either due to a lack of proper preparation or due to the situation with Miss Ikezawa acting as a distraction, Miss Ikezawa will inevitably hold herself responsible for it."
        ta "It will be next to impossible to get the idea out of her head that she caused her two best friends to fail and lose a whole year. It will almost certainly strain her relationship with you."
        ta "Do you two understand what's at stake now?"

        show hisao basic_worry_uni_close
        with chchange

        "A very long silence as the two of us digest what Miss Takawa just told us."
        "I have a pretty good idea of how awful Hanako would feel if Hisao or I were to flunk now. It's the same kind of guilt that's been tugging at me ever since that trip to Kasshoku."
        "Finally, Hisao softly speaks up."

        show hisao cross_worry_uni_close
        with chchange

        hi "I understand."
        li "So do I. We'll do our best to pass the exams. You have our word."

        show takawa weaksmile_close
        with chchange

        ta "Thank you. I hate to put pressure on you like this, but please do whatever you can to keep this particular burden off Miss Ikezawa's shoulders."

        show hisao basic_sweet_uni_close
        with chchange

        hi "We will."

        show takawa stern_close
        show hisao basic_neutral_uni_close
        with chchange

        ta "I give you my word here and now that I will do whatever I can to stabilize and improve Miss Ikezawa's mood."
        ta "This situation does not have any easy solutions and it's not impossible that her mood will degrade as graduation day gets closer, but I will do my best to make certain that doesn't happen. We take care of Miss Ikezawa and you take care of yourselves. Agreed?"

        show takawa weaksmile_close
        show hisao cross_smile_uni_close
        with chchange

        hi "Yes."
        li "Thank you, Miss Takawa."

        show takawa happy_close
        show hisao basic_smile_uni_close
        with chchange

        ta "The pleasure was all mine. I'm happy we had this conversation. Perhaps we can have a more uplifting talk at some point in the future."

        play sound sfx_doorclose

        scene bg school_hallway4
        with locationchange

        stop music fadeout 2.0

        "We say our goodbyes and leave Miss Takawa's office and the nurses' building."

        scene bg school_dormext_full
        with locationchange

        "As we reach the dorm, Hisao sighs."

        show hisao cross_worry_uni
        with charaenter

        hi "I went to see Miss Takawa hoping for her to say that things weren't quite as bad as I thought, but to be honest, I feel worse now than when we went in there."
        li "I'm afraid that goes for me as well. But there's no use complaining about it. We now have an additional reason to give our all at the exams. Let's both do our best."

        play music music_friendship fadein 4.0

        show hisao cross_smile_uni
        with chchange

        hi "Yeah. Maybe we could still do a few extra things as well. Like making her dinner so she won't need to cook after she comes back from a long day of supplementary classes."
        li "I've already been doing that for the past few weeks. I felt it was the least thing I could do for her."

        show hisao cross_speak_uni
        with chchange

        hi "Maybe we could... you know... treat her to a little outing this weekend. Just for a few hours. Just to cheer her up a bit."

        show hisao cross_neutral_uni
        with chchange

        li "I'm not sure if that's a good idea. We don't have that many days left until the national exam, and Christmas and New Year are coming up soon as well. I don't think Hanako will be put at ease if she sees us taking some time off. It might actually make her worry more."
        hi "You're probably right."
        "Suddenly, an idea pops into my mind."
        li "Hisao, do you have any plans for the upcoming Christmas?"

        show hisao basic_speak_uni
        with chchange

        hi "Well, I'm going home on the 24th and stay at my family's place while still trying to get in as much studying as I can while I'm there. I'm planning to take Hanako along, too. My parents said that it was okay."
        hi "I'm not sure what it feels like for an orphan to attend someone else's family activity, but I think just leaving her in her dorm room will be even worse."
        li "I'll be going home for a few days as well. Akira said she won't be able to make it home for Christmas this year, so it'll be up to me to compensate for her absence. I was thinking that it might be a fun idea for you and Hanako to come over the day after Christmas Eve."
        li "We'll have to study of course, but we can also probably spend an hour or two just hanging out and relaxing. It's not exactly an outing, but it will still allow the three of us to spend some time together outside the school."
        li "I'm sure my parents won't mind. They'll be pleased to see the two of you again."

        show hisao basic_smile_uni
        with chchange

        hi "Hey, I'd love to."
        li "Then let's follow through with it. I'll talk to my parents. You should invite Hanako."

        show hisao basic_grin_uni
        with chchange

        hi "Deal."
        li "Let's get back to our books, Hisao. And let's study as hard as we can. We have to pass the exams."

        show hisao basic_smileclosed_uni
        with chchange

        hi "I'll make it through, Lilly. I promise."
        li "I promise as well."
        "After swearing our little oath, we part ways."

        scene bg school_dormlilly
        with locationskip

        "I hurry back to my room and return to my books, throwing myself into the subject with a new-found fervor."
        "With luck, I'll be able to get in at least two more hours before it's time to make dinner."

        stop music fadeout 2.0

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return

    return
