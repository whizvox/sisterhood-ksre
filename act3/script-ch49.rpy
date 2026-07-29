label sh_ch49:
    label .s1:

        $ set_window_tint(TINT_HISAO)

        call sisterhood_timeskip_broken

        scene bg school_nursehall
        with Dissolve(2.0)

        play sound sfx_doorknock2

        "Voice" "Come on in."
        "As the person behind the door responds to my knocking, I reluctantly open the door and walk into the office."
        "I'd rather not be here, but as things are I think I'm going to need the peace of mind in order to study better."

        play sound sfx_dooropen

        scene bg school_nurseoffice
        with locationchange

        play music music_nurse fadein 4.0

        show nurse neutral
        with charaenter

        nk "Good to see you, Hisao. Please take a seat."
        "The nurse makes a welcoming gesture towards one of the chairs and then goes back to typing on his computer."
        nk "Just have to finish this report. I won't be long."
        hi "Perhaps I can come back some other time?"
        "It's not like I have a lot of free time right now."

        show nurse fabulous
        with chchange

        nk "Actually I've wanted to see you for some time now, so I'd appreciate it if we could get it out of the way now that you're here."
        hi "Oh?"

        show nurse serious
        with chchange

        nk "Earlier this school year, we'd see each other on a daily basis, and I thought that was a good habit. It allowed me to keep a close eye on the state of your condition and keep you in optimal shape."
        nk "I haven't really seen you for over two months and I'm quite curious about how you're doing."
        "I'm kind of put off by the flat business-like tone in his voice. He usually only adopts that tone whenever he's upset about something."
        "The occasion just now was pretty much perfect for a remark like ‘I've missed you and our daily intimacies’ or something else embarrassing—but for some reason, he doesn't seem in the mood for stupid jokes."
        "And whenever he's not in the mood for stupid jokes, I automatically get kind of worried."
        hi "Well, I guess I'm doing okay, though also very busy studying for my entrance exams."
        hi "I didn't do all that well on the mock exams, but I studied hard to make up for that and I managed to get a sufficient score on the National Center Test to be allowed to take part in the entrance examinations for the university I applied to."
        nk "Well, that's a relief."
        hi "Lilly and Hanako also made it through the Center Test. I'm especially relieved about Hanako, because her mock exam results were really bad."
        hi "It's a shame that one of Hanako's best friends flunked. Or actually rather than flunk she didn't even make it to the test. She really had rotten luck."

        show nurse concern
        with chchange

        nk "Oh yes, I know all about Inoue."
        "He sounds a bit annoyed."
        hi "Excuse me?"

        show nurse serious
        with chchange

        "He shakes his head as if dismissing the matter."
        nk "Never mind. So now you're preparing for the university-specific exam?"
        hi "Yes. It's pretty stressful. I mean, it's largely focused on science, which I'm not too bad at, but I'll be competing with nothing but people who are good at science."
        nk "Yes, I remember my own examination period. Very hectic time. And at least I had the luxury of only having to be concerned about getting into my university of choice."
        "He finishes his report with a dramatic keystroke and then turns to me."

        show nurse concern_close
        with chchange

        nk "I didn't have to worry about endangering my health."
        hi "As you can see, I'm still here."
        nk "So I see."
        "He opens one of his drawers and takes out a stethoscope."

        show nurse serious_close
        with chchange

        nk "It's been a while since you've been here, but I'm sure you still remember where we go from here."
        "I nod and remove my shirt. I shiver a bit as the cold metal of the chest piece is pressed against my body."
        "The nurse listens intently for several seconds, then moves the piece slightly upwards and repeats the process."
        "After going through this procedure several more times, he puts the stethoscope away and gestures that I can put my shirt back on."
        hi "So... did it still sound okay?"

        #show nurse annoyed_close
        #with chchange

        nk "I'm afraid it didn't. I could hear an irregularity in your heart rhythm. But you probably knew this yourself already, and that's why you came here. Am I right?"
        hi "Yeah, that's kind of the case."

        show nurse concern_close
        with chchange

        nk "Why don't you start at the beginning?"
        hi "I actually had a rather nasty heart flutter on the night before the Center Test. I was busy cramming, a hallmate came to borrow some notes, he knocked on my door rather loudly, I got startled, and then my heartbeat suddenly went completely out of control."
        hi "It passed eventually, but it was pretty scary. It's been such a long time that I actually forgot how frightening that kind of thing is."
        "The nurse groans."

        # show nurse annoyed_close
        show nurse serious_close
        with chchange

        nk "The Center Test was on January the 19th. That was nearly a week ago, and you didn't think it was important to tell us until now?"
        hi "I had exams that weekend and I went to bed rather early the night afterwards. After hearing that I passed the exams, I figured I'd take it slightly easier for a few days and things would be okay, but..."
        "The truth was probably that I also didn't want a lecture about how I had to slow down. I already know the problem without someone having to rub it in for good measure."

        show nurse concern_close
        with chchange

        nk "The same thing happened again today?"
        hi "Not yet. I actually figured I got away with it. But I have this feeling of restlessness and the memory keeps buzzing around in my head, even though it's been days."
        hi "I'm starting to lose sleep over it. I was hoping you could give me some peace of mind."
        "The nurse gives me a very stern glare."

        # show nurse annoyed_close
        show nurse serious_close
        with chchange

        nk "Well, I'm afraid I can't. Something definitely sounded off just now. You're walking an extremely fine line here, Hisao."
        hi "I know that."

        show nurse concern_close
        with chchange

        nk "How much sleep are you getting on a daily basis?"
        hi "Between five and six hours a day. I realize it's not much, but a lot of other students I've spoken to have similar schedules."
        nk "Are you still eating enough and is the food healthy?"
        hi "Yes. The juniors and the students who failed the Center Test are preparing the meals and doing the shopping for the 3rd years who are still in the running. It's a pretty convenient initiative on the school's behalf."
        nk "How much physical exercise do you still partake in?"
        hi "Emi has probably told you already."

        show nurse serious_close
        with chchange

        nk "I know that you haven't visited the track in quite some time. Any other physical activity at all?"
        "I think I get what he was referring to. Under other circumstances, that question would probably have been accompanied by a knowing wink, and he would have snickered at my embarassment."
        "It's a good thing his tone is so neutral this time around, because I feel the answer kicking me in the teeth while it's leaving my mouth."
        hi "...none whatsoever."

        nvl clear
        nvl show dissolve

        n "Ever since Hanako lapsed into a depression following the incident in that lecture hall, our sex life has pretty much been dead in the water."
        n "During the last time we did it, it became clear that she wasn't able to get into it or even enjoy it, so we basically ended up putting that part of our relationship on hold until Hanako is able to pick herself up again, whenever that is."
        n "{vspace=30}The sudden bout of abstinence initially left me feeling inadequate, and it used to feel immensely frustrating, but at this point in time I feel that maybe it's a good thing. That's because I'm having sincere doubts right now about my ability to get into bed with her and not have my heart act up. At least now I won't have the need to make excuses to Hanako."

        nvl hide dissolve

        show nurse concern_close
        with chchange

        nk "Sleep deprivation, stress and no physical exercise make a pretty toxic combination for a person with your condition, Hisao. I hope you can bring yourself to admit at least this much."
        "I know all about that. It's the same poisonous cocktail that caused Lilly's father to nearly end up visiting his ancestors."
        hi "I know."
        "Kenji's defense about how he didn't knock louder than usual left me thinking."
        "He should have restrained himself more, but the experience that night left me forced to admit that I've been allowing my condition to slowly but steadily start deteriorating, kind of like how Hanako's mood started regressing slowly but steadily after that traumatic incident last year."
        "For the first time in months, I've started considering my own mortality again."

        show nurse serious_close
        with chchange

        nk "I could draw you up a training schedule and a study planning that involves a responsible amount of sleep and a modest amount of physical activity, but I'm only going to do that if I know you're actually going to adhere to it."
        hi "I'd have to see the schedule before I can decide that."

        show nurse concern_close
        with chchange

        nk "The last person I made such a planning for ended up ignoring it altogether, and my hunch is that you'd find it too strict as well."
        "I wonder if that person was Naomi. That would explain the annoyed tone in his voice when I brought her up."
        hi "Maybe. It's just... I really don't want to flunk my exam and find out that I could have passed it if I had spent just a little bit more time studying."
        nk "I hear that one all the time. But it's going to be tricky doing something about your problem if you're going to just disregard whatever advice I have for you."
        hi "I was wondering... could you perhaps prescribe some additional medication? Like the medication I was on shortly after my last release from the hospital? I reacted pretty well to that and don't recall any major side effects."

        # show nurse annoyed_close
        show nurse serious_close
        with chchange

        nk "Is that why you came here? Drugs are no substitute for healthy living habits, Hisao. If they were, I wouldn't have been pushing so hard for you to get yourself in proper shape."
        hi "It's only for a few more weeks. I feel I'm really close. I can't afford to trip up just before the finish line."
        "The nurse nods at my words, but I can tell from his expression that he's not convinced, so I continue."
        hi "Look, it's really important for me to get into this university. Lilly and Hanako are going there too. I don't want to fall behind them. If I fail now, not only will everything have been for nothing, but I'll be forced to go through this again next year."
        hi "Not at Yamaku with its full-time nursing staff, but probably at some random cram school that won't even know how to deal with my condition. That's going to be even more risky. If I'm going to push myself, this school would still be the safest place to do it."
        hi "I've already made it through the Center Test. I just need a few more weeks to finish this."
        "The nurse rolls his eyes."

        show nurse serious_close
        with chchange

        nk "It sounds like you've been rehearsing this little speech."
        "A little bit. I suspected I was going to need it."
        hi "I'm only trying to put into practice what the school has been encouraging us to do."

        show nurse concern_close
        with chchange

        nk "What the teaching staff have been encouraging you to do. And even they wouldn't go around encouraging you to kill yourself or do anything else that might make you miss your exams."
        "He lets out an exasperated sigh before proceeding."

        show nurse serious_close
        with chchange

        nk "To tell you the truth, entrance examination season is my least favorite time of the year."
        nk "Of course the teachers' arguments are perfectly valid, and it makes sense for all the students attending here to go for the best academic credentials they can get, but the stress of examination hell can cause some real trouble at a school like this."
        nk "Sometimes I feel that the teachers are a bit too eager to lean on the medical staff for damage control."
        hi "I guess I'm not the only student who's having a bit of a struggle with his health right now then."
        nk "Sleep deprivation, stress, and high blood pressure are bad for anybody's health, but some people take it worse than others: heart patients, epileptics, diabetics—just to name a few. This is always a hectic time for the nurses here."
        hi "So situations like the one with Naomi are not uncommon around here at this time of year?"
        nk "We've had years where nobody was forced to drop out prematurely, and we've had years where worse happened."
        hi "Worse? Nobody died, I hope."

        show nurse concern_close
        with chchange

        nk "Fortunately not. But a few years ago, before I was employed here, we had a student with epilepsy here, like Inoue. He made it through the Center Test just fine, but things went wrong when he went to take his university-specific entrance exam."
        nk "Back then, our students still went to take their entrance exams at the university they applied at, just like everyone else."
        hi "He had a seizure during the exam itself?"

        # show nurse annoyed_close
        with chchange

        nk "Yes. Now imagine a hall packed with students who have probably been cramming non-stop for months and are wound extremely tight due to crushing pressure from their family to succeed that day."
        nk "Can you imagine the results when all of a sudden a person in that hall falls off his chair and appears to be dying with no medical professional nearby to quickly jump in?"
        hi "I can imagine getting spooked like that could cause a blackout or at least a negative effect on one's performance. Were there a lot of failures that year?"
        nk "Certainly a lot more than usual. Yamaku received quite a few complaints from angry parents that year."
        nk "From that point on we got around that problem by making arrangements with the universities our students applied for so our 3rd years can take their entrance exams here under the supervision of a representative from the National Center of University Entrance Examinations."
        nk "That way, we can have our nursing staff on stand-by and they can take immediate action if a similar incident were to happen again."
        hi "That's a pretty nice arrangement."
        nk "Of course, our own students would still be impacted if a student were to have a seizure or a heart attack in their presence in the middle of an exam. That's probably a good thing to keep in mind, Hisao. Being reckless may not just put yourself at risk, but could also cause trouble for others."
        "I didn't really think of that, but it doesn't change the way I feel."
        hi "Would it be selfish of me to say that I'd still like to take the risk?"

        show nurse serious_close
        with chchange

        nk "Probably. But it's not like I can stop you from taking it."
        "He gives a resigned sigh, takes a note from his desk, and starts writing a short list of medication on it. He then holds it out to me, but when I take it he doesn't let go of it."

        show nurse concern_close
        with chchange

        nk "I'd like you to get one hour of sleep a day more than you've had over the last few weeks. That's not a request, that's a condition."
        hi "Okay."
        nk "If you feel anything out of the ordinary—anything at all—come back here and let me know about it. Not the week afterwards or even the day afterwards, but as soon as humanly possible!"
        hi "I will."
        "He finally lets go of the note, and I quickly put it in my pocket before he can change his mind after all."

        show nurse serious_close
        with chchange

        nk "Good luck with your cramming sessions, and try not to do anything that'll cause my head to end up on the principal's chopping block."
        hi "Thanks."

        play sound sfx_dooropen

        show nurse concern
        with charadistant

        "I get up and walk out of the office, but before I can close the door, he scrapes his throat to get my attention one more time."
        nk "Hisao?"
        hi "Yes?"
        nk "I'm still going to draw up a training schedule and a dietary plan. I want you back in adequate shape before this year's graduation ceremony, so prepare yourself for workout hell the day after your entrance exams are finished."
        hi "I'll be looking forward to it. Go ahead and tell the workout imp to go and sharpen her pitchfork."

        stop music fadeout 5.0

        show nurse grin
        with chchange

        pause 1.0

        play sound sfx_doorclose

        scene bg school_nursehall
        with locationchange

        "I close the door before he has a chance to reply, but the last thing I see is that familiar grin of his. Which honestly feels like a relief."

        play music music_dreamy fadein 4.0

        "Voice" "Oh, hey there."

        show naomi basic_neutral at center
        with charaenter

        "But when I turn around, I find out that I'm not alone in the hallway. Standing in front of me and looking me over is a familiar face."
        hi "Naomi!"
        na "'scuse me."

        show naomi basic_neutral at tworight
        with charamove

        play sound sfx_doorknock2

        pause 1.5

        hide naomi
        with charaexit

        play sound sfx_doorclose

        "She nods at me and then walks past me, knocking on the nurse's door before opening it and walking in."
        "I wonder what she's here to see the nurse for."
        "Dammit, did she just hear the nurse's last comment?"
        "I'd like to drop by at the apothecary and get back to my books as soon as possible, but the fact that Naomi just saw me leaving the nurse's office troubles me a bit, so I decide to wait for her and make sure she's not going to pass this event on to Hanako."
        "The last thing I want is for her to get worried over me."

        play sound sfx_dooropen

        show naomi basic_neutral at tworight
        with charaenter

        "Surprisingly, Naomi comes walking out of the office less than five minutes after entering. Whatever she wanted to talk about probably didn't take long."
        "As she closes the door, I notice a note in her hand not completely unlike mine."
        hi "Hey there."

        show naomi basic_confused_close
        with characlose

        na "Oh, didn't think you'd still be around. Hey there."

        show naomi basic_neutral_close
        with chchange

        "I shoot a brief look at the door of the nurse's office."
        hi "That didn't take very long."
        "Naomi rolls her eyes."

        show naomi basic_serious_close
        with chchange

        na "He used to make small talk, but I don't think he likes me very much anymore at this point."
        hi "You got on his bad side?"

        show naomi basic_sad_close
        with chchange

        "Naomi lets out a weary sigh."
        na "My parents were pretty pissed when I missed my exams that day and made an angry phone call to the principal, who in turn went to chew out the nurse, but he said he gave me a daily planning I didn't bother to follow, so now both my parents and the nurse are mad at me."
        na "And all I did was try and prepare myself well for my exams so they'd be proud of me. So much for appreciation of my efforts, huh?"
        hi "I'm really sorry to hear that."

        show naomi basic_serious_close
        with chchange

        na "It's so easy for everyone to say I've been too rash. But if you were running in a race on the track or something and you tripped and fell on your face, would you take it easy or would you double your efforts so you could catch up with the rest?"
        na "That stupid schedule required me to sleep for a total of eight to nine hours a day. How on earth can I compete with people who have so much more time to study than I can?"
        hi "I think I know how you feel. I hope your parents weren't too upset."

        show naomi basic_sheepish_close
        with chchange

        na "We'll be okay. They just need a little bit of time to let it sink in. Deep down they know I didn't fail my test on purpose or anything."
        "I point at the note in her hand."
        hi "Looks like we're both headed for the same place."

        show naomi basic_smile_close
        with chchange

        na "Yeah, I guess I'll come along."

        scene bg school_staircase3
        show naomi basic_smile_close
        with locationchange

        "We start walking down the hallway, and I take another look at Naomi."
        "She's probably still bummed about missing the Center Test, but she looks to be in better shape now than the last time I saw her."
        hi "Have you already decided what you're going to do now?"

        show naomi basic_ponder_close
        with charaenter

        na "Welllll... I'd like to give it another try next year. I mean... If I'm destined to crash and burn, I'd at least like to properly fail my tests instead of missing them altogether."
        hi "Do you think your parents are going to go along with that?"

        show naomi basic_sheepish_close
        with chchange

        na "I think so. I remember they were really proud when Hanako, Jun, and I won a prize in that writing contest. I think they'll support me in the end."
        na "At least for one more year. I'd better not press my luck after that. It's not like university preparation cram school is cheap."
        hi "So you're probably going back home after graduation, right?"

        show naomi basic_smile_close
        with chchange

        na "Yeah, I think I'm going to move back in with my parents for a year and attend cram school in my hometown. I'm gonna miss the freedom of the dorms here, but it's not like I have anywhere else to go."
        hi "Cram school, huh?"

        show naomi basic_grin_close
        with chchange

        na "Yeah, at least for part of the year. But until the graduation ceremony, I'll be sticking around here and help out wherever I can. Both at the newspaper club and at the dorms."
        hi "You're helping the juniors taking care of the 3rd years who are still studying?"

        show naomi basic_smileclosed_close
        with chchange

        na "Yeah, the usual stuff like cooking meals and doing shopping. I try to give Natsume some extra priority. She can use all the help she can get?"
        hi "She's struggling?"

        show naomi basic_neutral_close
        with chchange

        na "She's applied for a university that has a pretty tough entrance exam. She's clever enough to make it in, but the stress is causing her arthritis to act up and that's making it harder for her to study. I dropped by the nurse today to get her some additional medication."
        hi "So... Natsume too?"

        show naomi basic_serious_close
        with chchange

        na "Yeah. I think my episode last month only worsened the pressure on the rest. Like... It showed everyone that many of us can still fail through no real fault of our own. That the deck is still stacked against us. It's kind of depressing."
        na "Maybe that's why the nurse was looking so glum. I bet his people are really busy right now."

        show naomi basic_neutral_close
        with chchange

        hi "On the other hand, it's pretty clear this entire school is doing its best to reshuffle the stacked deck. They're making arrangements with universities so we can take our tests here on campus with the nurses close by. Junior classmen are taking daily chores off our hands."
        hi "It's motivating to see that this entire school is working so hard as a community to get its 3rd years to succeed."

        show naomi basic_grinclosed_close
        with chchange

        na "Hey, that's true. It does make me feel kinda sorry that we won't be there to support them when it's their turn."
        hi "There'll be others looking out for them."

        show naomi basic_smile_close
        with chchange

        na "Yeah..."
        "As we get to the doorway leading to the apothecary, Naomi takes a look at the note I'm holding."

        show naomi basic_grin_close
        with chchange

        na "I bet that unlike mine, that note you're holding isn't for someone else."
        hi "I convinced the nurse to raise the dosage of my medication a bit. I'm hoping it's gonna be enough to carry me through the upcoming weeks."

        show naomi basic_ponder_close
        with chchange

        na "Figured as much. I considered something similar myself back in January, but I've been on the same meds for close to three years, and there's a lot of stuff I don't react well to, so there was no time to experiment. Might be an option for the upcoming year though."
        hi "By the way, I was hoping you could be so kind as not to mention to Hanako that I was here. I don't want to worry her."

        show naomi basic_tongue_close
        with chchange

        na "And here I was thinking you were waiting for me because you desired my exciting company."
        hi "Promise?"

        show naomi bend_grin_close
        with chchange

        na "Well, okay. Fine with me."

        scene black
        with locationchange

        "We give our notes to the nurse on duty at the apothecary, and after a few minutes, we're handed our fresh batch of medication."
        "As we leave the nurse's building, Naomi turns to me."

        play sound sfx_doorclose

        scene bg school_courtyard
        show naomi basic_neutral_close at tworight
        with locationchange

        na "Have you talked to Hanako recently?"
        hi "I'm afraid I haven't. Do you have any idea how she's doing?"

        show naomi basic_confused_close
        with chchange

        na "Huh?"
        hi "What is it?"

        show naomi basic_ponder_close
        with chchange

        na "She's your girlfriend and you don't know how she's doing? You two don't have relationship problems, do you?"
        hi "Don't be ridiculous. We don't have a very active dating life right now, but there's a good reason for that."
        "Truth be told, I do feel like we've been growing apart a little bit lately. Hanako started secluding herself after the mock exams and lately, I've been doing exactly the same."
        "Still, I'm convinced it's nothing we won't be able to patch up after graduation when we'll finally be able to take it easy and relax."

        show naomi basic_serious_close
        with chchange

        na "Yeah, I get that you guys are all busy with studying, and it's really important, but I remember that the three of you used to study together all the time. It'd be a good opportunity to spend some time with one another and still get some studying done, right? Why not continue that?"
        hi "We did that until the mock exams, but afterwards the school started dumping all those supplementary lessons on Hanako, and she was usually too tired to do a lot of studying with us afterwards."
        hi "I didn't feel comfortable just studying with Lilly all day long, so we all ended up studying on our own."
        na "But those supplementary courses ended after the Center Test, didn't they?"
        hi "Yeah, but... uh... since we're all studying for an entrance exam in a completely different subject, studying together wouldn't really add much anymore."

        show naomi basic_ponder_close
        with chchange

        na "Hmmmm..."

        nvl clear
        nvl show dissolve

        n "Naomi gives me an investigative look that tells me she's clearly not buying it, but I don't really feel like discussing the real reason with her right now, despite the fact that she can probably guess what it is based on her own experiences."
        n "{vspace=30}After what happened just before the Center Test, I simply don't fully trust my body anymore. If I had an unexpected heart flutter in front of Hanako or Lilly, it'd be extremely likely that they'd lose what little sleep they're still getting worrying over me. I don't want to be responsible for putting even more stress on them than they're already under."
        n "{vspace=30}I'll have time to hang out with them after the exams—after I've gotten back into shape a little bit."

        nvl hide dissolve

        hi "Of course I'm a little worried about Hanako, but I'm not sure if there'd be much I could do to help her at this point. I'm kind of walking on thin ice as it is and worrying too much about her would be bad for me too."
        hi "So I'm concentrating on my own exam as much as possible, and I'm trying to maintain faith that she'll do the same. She did really badly on the mock exams, but she surprised everyone when she made it through the Center Test with adequate grades all around."
        hi "I think she can pass her entrance exams too if she really wants to."

        show naomi basic_shock_close
        with chchange

        na "Entrance exams? As in more than one?"
        hi "Hanako filed an application for an additional university that holds its entrance exams on a different day."
        hi "I'm still not sure whether she did this simply to appease Mutou or because she's trying to keep as many options open as she can, but the gist of it is that she'll be participating in two entrance exams, rather than just one."

        show naomi basic_neutral_close
        with chchange

        na "Whoa! How does she do it?"
        hi "Well, they're two exams about exactly the same subject, so it's not like she'll need to study twice as much material."
        hi "But we're getting kind of off-topic. You still haven't answered my question."

        show naomi basic_ponder_close
        with chchange

        na "I went to see Hanako after the answers to the Center Test were posted. I mean, failing sucks, but it would have been worse if I had also dragged Natsume and Hanako down with me. When I heard that they both made it through, it felt like part of me passed anyway."
        na "I looked Hanako up that evening and told her that. She was... like... beaming when I told her how relieved I was. But..."
        hi "Yes?"

        show naomi basic_serious_close
        with chchange

        na "Just when I was heading out the door, that smile of hers turned sad again. I made me uneasy. I don't think we're out of the woods yet. I haven't seen her a single time over the last two days. I always leave her meals at the door."
        na "I can't help but feel like she's starting to seclude herself again. Maybe she's just busy. I hope this is not a sign of a relapse coming up."

        nvl clear
        nvl show dissolve

        n "It's obvious that Naomi is worried about her friend. I'm getting a little worried myself by listening to her."
        n "{vspace=30}Is Hanako still okay? How is she doing? Is she studying diligently, or is she just sitting in her room all day long?"
        n "If she's keeping her door locked, is she going to open up for me? Or would my presence merely make things awkward?"
        n "{vspace=30}I remember Miss Takawa's words that Hanako's mood might drop as we get closer to graduation day."
        n "{vspace=30}And what's Lilly doing? Wouldn't she step in if she suspected that Hanako was struggling?"
        n "No, that's not fair to Lilly. She has her own exams to worry about too."

        nvl hide dissolve

        "I think I have an idea to cheer up Hanako a bit. I hope it works."
        hi "Naomi?"

        show naomi basic_neutral_close
        with chchange

        na "Yeah?"
        hi "Do you happen to have a pen and paper on you?"

        show naomi basic_grin_close
        with chchange

        na "Of course! I'm a journalist, so I always carry a pen and blocknote."
        hi "Could I use them for a moment?"

        show naomi basic_serious_close
        with chchange

        na "Uh...sure."
        "Naomi opens her handbag and takes the pen and blocknote out of it. I take them from her and start scribbling a little note."

        show naomi basic_neutral_close
        with chchange

        call screen written_note(_("Hey Hanako,\n\nSorry for not having been around lately. I hope you're doing well. Things are pretty hectic for me right now, but I'm still managing.\n\nWhenever I'm not thinking about aerodynamics, electric circuits, or quantum mechanics, I'm thinking of all the fun times I'm intending to have together with you after we've graduated together. It really keeps me going.\n\nLet's both hang in there,\n\nHisao."))

        "After finishing it, I neatly fold it up and hand it to Naomi."
        hi "Could you deliver this to Hanako?"

        show naomi basic_smile_close
        with chchange

        na "Well, she's probably not going to let me in even if I knock, but I could slide it under the door."
        hi "Actually, I'd like you to include it with her meal. Maybe wrap it around her chopsticks?"

        show naomi basic_smileclosed_close
        with chchange

        na "Awww, that's a really cute gesture. Yeah, I'll do that. No problem."
        hi "Could you also... like... try to avoid reading it?"

        show naomi basic_grin_close
        with chchange

        na "You're no fun at all."

        show naomi basic_smile_close
        with chchange

        "I say my goodbye to Naomi and quickly head for the boys' dorm."

        show naomi bend_laugh at right
        with chchange

        "...though not quickly enough to prevent Naomi's ‘D'awwwwwww’ from catching up with me."

        stop music fadeout 3.0

        scene black
        with endchapter

        if _in_replay:
            return

    return
