label sh_ch23:
    label .s1:

        $ set_window_tint(TINT_HISAO)

        scene bg inverness_street
        with Dissolve(2.0)

        play ambient sfx_crowd_outdoors fadein 2.0 volume 0.4

        aki "Let's get out here. The place should be around the corner."

        # TODO play car door close SFX

        show hanako cover_bashful_ss at tworight
        show lilly cane_smileclosed_ss at twoleft
        show akira basic_smile_ss at center
        with charaenter

        "Akira takes out her wallet, pays the cab driver and motions us to get out. She then takes Lilly's hand, puts it on her arm and carefully starts guiding her down the street."
        "Hanako and I take a moment to look around. The airport and the green hills of the countryside could have been mistaken for being located somewhere in Japan, but that's definitely not the case with the town."
        "Especially the older buildings we pass feel extremely foreign to us. They serve as an unavoidable reminder, aside from the cab driver's incomprehensible dialect, how far away from Japan we are."
        hi "Shall we?"

        show hanako emb_smile_ss
        with chchange

        "I playfully take Hanako's hand and place it on my arm similar to what Akira just did. Hanako giggles, wraps her arm around mine, and we start following Akira's lead."
        "After less than a minute, we reach the entrance of what seems to be a bar."

        queue sound [sfx_camerashutter, sfx_camerashutter, sfx_camerashutter]

        "Before we enter, Hanako turns around, pulls her photo camera from her bag and takes several pictures of the picturesque buildings lining the street."

        stop ambient fadeout 1.0

        play sound sfx_dooropen
        queue sound sfx_storebell

        scene bg inverness_pubdoor
        with locationchange

        play music music_jazz fadein 4.0
        play ambient sfx_crowd_indoors fadein 2.0

        show hanako cover_bashful at tworight
        show lilly cane_smile at twoleft
        show akira basic_smile at center
        with charaenter

        aki "Want me to make some recommendations?"
        "As we enter, Akira cheerfully points to the bottle-filled shelves behind the bar."
        "The place has a bit of an old-fashioned quality to it with most of the furniture made from unpainted wood and a stuffed head of a stag on the wall near the bar. The front of the room is fairly crowded, but there are several free stools near the bar itself."
        "Near one wall is a small podium, and I think I can see something resembling a pool table in one corner on the far side of the room."
        hi "They probably have soft drinks here, don't they?"

        show lilly basic_planned
        with chchange

        "Lilly throws us a slightly mischievous smile as she folds up her cane and takes a seat on one of the bar stools."
        li "Would the two of you object to a glass of wine so we can perform a proper toast to Akira?"
        "I sit down one seat away from Lilly so Hanako can sit in between us and not worry about other patrons staring at her."
        hi "Have you forgotten that the three of us are only 18, Lilly?"

        show lilly basic_giggle
        with chchange

        "Lilly chuckles, obviously having expected that answer."
        li "18 is old enough in this part of the world, Hisao. You can order whatever you like here."
        hi "That's pretty convenient, though we'd still better moderate ourselves. I'd hate the idea of one of us getting sick in the cab on the way back."

        show lilly basic_smile
        with chchange

        li "We won't be taking a cab, Hisao. We'll have a private transport to take us back to our parents' place. Even so, you make a good point. Let's not get carried away while we're here."

        show hanako cover_smile
        with chchange

        "I throw a look at Hanako, probably the one among us with the lowest alcohol tolerance, to ask her opinion. She gives a brief nod to indicate it's okay, and I turn back to Akira."
        hi "So I guess we'll have four glasses of wine. Would you mind ordering? I bet I'm incapable of even pronouncing half of the names on those bottles."

        show akira basic_cheerful
        with chchange

        aki "Heh, would you believe lots of those brands are new to me too? Fortunately I've had a taste of several ones during our last time here. You won't be disappointed."
        "She beckons to the barkeeper and points to one of the bottles on the shelf behind him."
        "After the barkeeper finishes handing us all a glass, Lilly takes hers, sniffs carefully to take in its scent and then raises it with an appreciative smile."

        show lilly basic_satisfied
        show akira basic_sweet
        with chchange

        li "I would like to perform a toast to my hard-working and wonderful sister, who has started working her way up the ranks here at head office. May her new job be met with great success and ample satisfaction. And may it be known that I admire and respect her very much."

        show hanako basic_smile
        with chchange

        hi "Cheers!"
        ha "C-Cheers."

        show lilly basic_cheerful
        with chchange

        "We raise our glasses, perform a toast and each take a sip. The slightly sweet taste of the white wine Akira has gotten us is surprisingly similar to what we had during Hanako's birthday party. Akira seems to have a knack for picking tasty drinks."

        show akira basic_sheepish
        with chchange

        "While Hanako, Lilly and I down our drinks in small, measured sips, Akira manages to empty her entire glass in a single gulp. Upon putting her glass back on the bar, she flashes Lilly a sheepish smile."
        aki "Man, you may have a knack for speeches, Lils. Though I feel kinda compelled to point out that my current position probably has less to do with my work record than it has to do with me being a Satou."

        show lilly basic_smileclosed
        with chchange

        "Lilly gives her sister an encouraging smile."
        li "I know Father pulled a few strings to get you that recommendation, but I also know that now you're here you will do everything in your power to prove yourself."
        li "You'll push yourself to excel until everyone at the office is convinced that putting you where you are now was not a special favor, but rather an act of foresight."

        show akira basic_wistful
        with chchange

        "Akira gives Lilly an amused look, but when she speaks, her tone is somewhat wistful."
        aki "Probably... I guess... that's part of being a Satou as well, isn't it?"

        show lilly basic_weaksmile
        with chchange

        li "I wouldn't be at all surprised if Father felt the same when he first came here."

        show akira basic_boo
        with chchange

        aki "Heh, from his reputation at the office I'd say he's still in the middle of that process. People seem to regard him as some kind of one-man army over there."
        li "You had better not become such a workaholic that our phone calls start getting phased out over it."

        show akira basic_sweet
        with chchange

        "While Lilly's tone is playful, both she and Akira fall silent for a moment. Until now, it appears that they met up with one another whenever they could and contact took place on a regular basis."
        "When Lilly returns to Japan however, their contact will be limited to carefully timed international phone calls and there's no doubt in my mind that both of them are painfully aware of this right now."
        aki "Don't worry about that, Sis. I'll be sure to keep my priorities in order. Let's ditch the depressing thoughts tonight and have a good time."

        show lilly basic_surprised
        with chchange

        "Akira raises her hand and affectionately ruffles Lilly's hair, surprising her for a moment and then gestures to the barkeeper for another drink."

        show lilly basic_smileclosed
        show akira basic_smile
        with chchange

        "While he's refilling her glass, the barkeeper says something to Akira that I can't quite make out but causes Lilly to ‘hmmm’ quietly. Akira then nods and passes him several bills from her wallet."
        hi "What was he saying?"
        aki "There's pub quizzes being held here during the weekends and the next one's about to start. I just paid him the admittance fee. You two interested in teaming up with us?"

        show hanako basic_worry
        with chchange

        "I exchange a glance with Hanako."
        "I don't think I'll be able to pull my weight here. I probably won't even understand the questions, let alone know much about what probably passes for common knowledge around here. Hanako seems a bit hesitant as well."
        hi "I think we'll pass. I noticed a pool table in the corner over there and Hanako still owes me a rematch after our last game in the jazz bar."

        show hanako emb_downsmile
        with chchange

        "Hanako nods with a small smile, eager to get farther away from the din in the front area and have a small competition with me."
        ha "I accept t-the challenge."
        aki "Have fun you two. We'll be at the table near the podium if you need us."
        li "Would it be okay if I paid a visit to the restroom first? I doubt we'll be allowed to leave our table during the quiz itself."
        aki "Sure Sis. Let me show you the way."

        scene bg inverness_pubback
        with locationchange

        show hanako basic_smile at tworight
        show lilly cane_smile at twoleft
        show akira basic_smile at center
        with charaenter

        "Lilly folds out her cane and places her hand on Akira's arm. We follow them to a small corridor near the back."
        aki "Ladies room is the door on the left."

        hide lilly
        with charaexit

        "As Lilly nods and navigates down the corridor, we turn to Akira."
        hi "Lilly sure knows how to perform toasts. Sisterhood must be a wonderful thing."

        show akira basic_wistful
        with chchange

        "Akira nods and smiles warmly."
        aki "Several of my colleagues can’t stand their siblings. I think I just got lucky. We've always gotten along well despite the 7-year age gap. We got even closer when it was just the two of us living together."

        show hanako basic_normal
        with chchange

        hi "That couldn't have been easy, a 19-year old and a blind 12-year old living on their own, even with Lilly being as independent as she is."
        aki "Don't mention to her that I told you this, but back when our parents first moved to Scotland, Lilly wasn't independent at all."

        show akira basic_ponder
        with chchange

        aki "I mean, whenever one of our parents wanted something done that they couldn't do themselves, they'd ask me to do it. Before our parents left, they liked pampering Lilly."
        hi "So you taught her how to do stuff like laying the table and cooking?"

        show hanako emb_smile
        show akira basic_sheepish
        with chchange

        "Hanako suddenly stifles a soft giggle. Akira grins broadly."
        aki "In case that didn't tip you off, cooking isn't exactly where my talent lies, to use Lilly's words. That's as polite as she can be about it. That ought to tell you something."
        hi "If you didn't then who did?"

        show hanako basic_smile
        show akira basic_ponder
        with chchange

        aki "After our parents left, we hired a housekeeper who stuck around for some time. "
        hi "And this housekeeper taught Lilly?"
        aki "At my request in exchange for a very generous bonus. I wanted some peace of mind. I wanted to be able to sleep peacefully at night and do my job without worrying all the time. The burden of responsibility was enough as it was."
        aki "I could have hired someone else. Heck, I could have easily hired two... Mom and Dad never really left us strapped us for cash. But..."
        hi "Yes?"

        show hanako basic_normal
        show akira basic_depressed
        with chchange

        aki "I really hated still depending on our folks' money all the time—as if things were alright as long as they just kept paying."
        aki "If we'd get independent enough for the two of us to get by without additional help, I wanted to shoot for that. And we reached that point eventually. Lilly was a very diligent pupil and a fast learner."
        "Akira seems aware of the fact that her own pride played a role in this whole thing and looks at the floor for a moment."
        "I quickly move in to fill the moment of silence."
        hi "Lilly's probably more self-sufficient than many of her classmates who have partial eyesight."

        show akira basic_sad
        with chchange

        aki "That's a good thing. University probably ain't gonna be as accommodating to blind people as Yamaku. If she wasn't as independent as she is, she'd have had no choice but to follow me to Scotland."

        show akira basic_cheerful
        with chchange

        "Noticing the door of the ladies room opening, Akira points at the pool table nearby."

        show lilly cane_smileclosed at twoleft
        with charaenter

        aki "We'll be heading to our seats. You two have ever played English billiards before?"
        hi "English billiards? I thought this was a pool table."
        aki "Look at the case on the wall. You can't play pool with only three balls."

        scene bg inverness_pubbilliards
        with locationchange

        "I look into the direction Akira's pointing and notice a device on the wall with three balls, a white, a yellow and a red one, resting in three indentations at the top and a coin slot on the front."

        show akira basic_cheerful
        with charaenter

        "Akira walks over to it and takes one of the balls."
        "Immediately, a high-pitched buzzer sounds, causing Lilly to flinch a bit. She quickly puts a coin into the coin slot and the noise stops."

        show akira basic_smile
        with chchange

        aki "First game's on me. When the buzzer goes off you'll either have to insert another coin or return the balls to the case. You guys know the rules?"

        show hanako basic_worry at tworight
        show lilly basic_smileclosed at twoleft
        with charaenter

        "One look at Hanako tells me she's as much in the dark about how to play as I am."
        "Akira seems to read our expressions."
        aki "One player uses the white ball and one player uses the yellow one. You score points by hitting the other balls with your cue ball in various ways."
        aki "You get points for bumping the other balls into a pocket with your cue ball which is called a ‘winning hazard’ or by pocketing your own cue ball after contact with another ball which is called a ‘losing hazard’."
        aki "It's 3 points for moves involving the red ball and 2 points for moves involving the other player's cue ball."
        aki "You also get points if you hit both other balls with your own cue ball in one shot. I believe they call that a...er..."

        show lilly basic_cheerful
        with chchange

        li "A cannon."

        show hanako basic_smile
        show akira basic_smug
        with chchange

        "Akira shoots Lilly a smirk after the latter finishes the explanation for her."
        aki "Heh, showoff. Let's hope your recollection of trivia is also gonna help us win that quiz."

        show lilly basic_smileclosed
        show akira basic_smile
        with chchange

        "After giving us an explanation about where to put the balls after pocketing them and what constitutes a foul, Akira points at the scoreboard on the wall."
        aki "You can decide for yourself whether to make up a winning score or just play until the time runs out. Everything clear?"

        show hanako basic_bashful
        with chchange

        hi "I think so."
        ha "Yes."
        aki "Great. Have fun. And wish us luck."
        hi "I'll keep my fingers crossed for you."
        ha "Good luck."

        hide akira
        hide lilly
        with charaexit

        "As the Satou sisters make their way to the front of the pub, Hanako hands me a cue."

        show hanako at center
        with charaenter

        "We each shoot a ball across the table to see who gets the first turn."

        play sound sfx_billiards

        hi "Looks like you're closer to the front area than I am. Do you want to play with white or yellow?"

        show hanako basic_smile
        with chchange

        ha "Hmmm... I'll take white."
        hi "I think it's best if we simply play until our time is up. Okay?"
        ha "Okay."

        play sound sfx_billiards_break

        "Taking a moment to plan her move, Hanako shoots her cue ball forward and hits the red ball with considerable force, but then misses the yellow one by only a few centimeters."
        hi "My turn."

        play sound sfx_billiards

        "Hanako's shot has left the balls in an advantageous position for me, and after taking careful aim, I manage to knock my own cue ball into the pocket after just barely grazing the red ball."
        "This game is definitely gonna be trickier than that time we played pool. Since we're both new at this, the odds should be fairly even, but I learned last time that Hanako has slightly better form than me. Beating her isn't going to be easy."
        ha "Good shot."
        hi "Thanks."

        play sound sfx_billiards

        "I put my cue ball on the designated spot on the table and try to shoot a repeat of my previous shot. This time, however, my aim is slightly off and my ball lands in the pocket without hitting any others."
        hi "Ugh, a foul. That means you get 2 points, doesn't it?"

        show hanako basic_bashful
        with chchange

        ha "Y-Yes."
        "I move the sliders on the scoreboard and watch Hanako lining up her shot. The expression on her face is that same mixture of concentration and relaxation she had during that last game of pool we played."
        "There are quite a few people in the pub at the moment, but now that the quiz has started, almost everyone is gathered in front of the stage on the other side of the room, and nobody seems to be paying us any attention."
        "I try to make out what the quiz host is saying, but can't really catch more than a few words here and there. We probably made the right decision in not going along with Lilly and Akira. The whole situation gives me a slight feeling of déjà vu."
        hi "This sure brings up memories, doesn't it? The four of us going out and Lilly and Akira doing their thing while the two of us spend the evening knocking billiard balls around."

        show hanako emb_downsmile
        with chchange

        play sound sfx_billiards

        "As she hits her cue ball and bounces it off both other balls, I can see Hanako smile at the memory."
        ha "Let's h-hope this evening will b-be just as fun."
        "I had fun at the time as well, though in a moment of naïvete, I also made a mistake that evening that nearly sank my chances with Hanako."
        "When I told her, while she was in the process of opening up to me, that I was happy to protect her, it was a remark said with nothing but the best intentions."
        "It wasn't until our confession in the park that I realized just how denigrating that must have sounded to her."
        hi "I'll try not to mess up and say anything hurtful this time around."

        show hanako basic_worry
        with chchange

        ha "W-What?"
        "Hanako was preparing an attempt to pocket my cue ball with her own, but upon hearing my words she looks at me and gives me a confused look."
        "She thinks for a moment, then realizes what I was referring to."

        show hanako basic_bashful
        with chchange

        ha "Oh... ummm... It's okay. I nearly f-forgot a-about that already."
        hi "Sorry for bringing it up."

        play sound sfx_billiards_break

        "Hanako reaims her cue and takes the shot, but misses her intended target, though her ball manages to touch the red ball before coming to a standstill."
        ha "I'm... trying n-not to ponder the p-past while I'm here."
        hi "You're right. Better to focus on the present."
        "As I move in to take my turn, I notice Hanako shaking her head with a shy smile."

        show hanako emb_smile
        with chchange

        ha "I... really... like the present as it is r-right now. I think I can... enjoy it more if I don't think too hard about things. But I still n-need to figure out what I want in the f-future."
        "That's the first time I’ve heard from her about that. I've asked her about it before, but she always told me she didn't know yet, and I'd drop the subject in order to avoid putting pressure on her."
        hi "Good to hear you're giving it serious thought."

        show hanako basic_bashful
        with chchange

        ha "I... I'd like to have it sorted out before c-classes start again."
        hi "Do you have a general idea already?"
        "I've made an effort to come up with suggestions myself before, but it's kinda difficult because Hanako doesn't seem to have any subjects she naturally excels in, unlike Lilly and myself."
        "However, also unlike Lilly and myself, Hanako doesn't have any subjects she's particularly bad at either. It's almost as if even Hanako's test scores are focussed on the purpose of not standing out. That does make planning a future a tricky activity."
        ha "Maybe."

        play sound sfx_billiards

        "I take a shot and manage to nudge Hanako's cue ball into a pocket."
        hi "Care to tell me about it?"

        show hanako basic_distant
        with chchange

        "Hanako doesn't respond, but merely looks at me. I know that look on her face. It's her ‘quid pro quo’ expression."

        play sound sfx_billiards

        hi "I'll tell you about my plans in return, okay?"

        show hanako basic_smile
        with chchange

        ha "Okay."

        play sound sfx_billiards

        "I make an attempt to pocket the red ball this time, but my shot is too soft, and my target stops mere centimeters away from the pocket in the corner."
        hi "After starting the club with him, I think I'd seriously break Mutou's heart if I didn't pursue science as a career path. That part is pretty much a done deal."
        hi "Unfortunately, I'm not sure yet about the specifics. That's why I asked Mutou to cover a wide range of topics at the club during the upcoming months."
        ha "You're hoping to... c-come across a subject eventually that you feel a c-click with?"
        hi "That's the idea. Also, there are several universities in my hometown that offer wide selections of scientific studies and whose entrance exams I should be able to handle."
        hi "If I could make it into one of those, I could save on the costs of renting a dorm room on campus by moving back in with my parents. I have to be mindful of my family's financial situation."
        "Hanako nods understandingly and prepares to finish the shot I failed to get right."
        hi "So how about you?"

        show hanako emb_emb
        with chchange

        ha "Ummm... Did you... like my article? About the science club?"
        hi "I loved it, and it seems like Mutou did too. Why?"
        ha "Naomi wants m-me to write the next ones too."
        hi "Will you?"
        ha "Yes. The next one is about our own club, so I can use my own experience. There's no need to contact a teacher or club president, which makes it easier."
        "Personally, I'd still be at a loss on what exactly to write and how to word it. Writing essays was never my strong suit, but Hanako doesn't seem worried about that."
        "Come to think of it, when I woke up I saw her scribbling on a notepad."
        hi "Were you busy writing your next column when I was waking up?"

        show hanako basic_normal
        with chchange

        ha "Just b-brainstorming a bit. But I want to have it finished before we fly back to Japan."
        hi "I suppose this is related to your plans for the future, isn't it?"

        play sound sfx_billiards

        "Hanako takes aim and knocks both the red ball and her own cue ball into the corner pocket."

        show hanako emb_downtimid
        with chchange

        ha "Maybe... I could... do something related to that."
        hi "You mean... study journalism?"
        "Hanako doesn't answer immediately. She merely gives me a long look as if to try to read my thoughts and determining whether I think she's gone crazy."
        "After a few silent seconds, she slowly nods."

        show hanako emb_timid
        with chchange

        ha "What do you think?"
        "I'm not sure. No matter how hard I try, I'm completely unable to picture Hanako pushing herself through a thick crowd in order to shove some celebrity a microphone in their face."
        "On the other hand, from what I've learned about her activities at the newspaper club, she's been genuinely enjoying them, and people are always more eager to push their boundaries when they're working on something they're interested in."
        "And pushing boundaries and devising workarounds to our limits is what every student at Yamaku is encouraged to do."
        "I'd never imagine Emi's friend Rin to be an artist either, seeing that she has no arms, yet she has learned to transcend that limitation, and now she's supposedly one of the best painters in the art club."
        "Could it be the same with Hanako?"
        hi "To be honest, it comes a bit out of the blue. It's not anywhere near the direction I thought you'd be heading into."

        show hanako basic_bashful
        with chchange

        "Putting the balls back on the table, Hanako smiles meekly while preparing to strike her cue ball."

        show hanako basic_distant
        with chchange

        ha "Ummm... What d-direction did you{w=0.5}—AH!"

        play sound sfx_billiards_blunder

        "I'm having the impression Hanako's mind wasn't really into that last strike, since it's way too hard and as a result her cue ball flies off the table and rolls towards the bar, coming to a stop underneath one of the occupied barstools."

        show hanako emb_sad
        with chchange

        "I look at Hanako, and she gives me a pleading look back. I suppose it's up to me to be a gentleman."
        hi "I'll go get it."

        show hanako emb_smile
        with chchange

        "Hanako smiles in relief and gives a silent nod."

        scene bg inverness_pubback
        with locationchange

        "I put down my cue and walk over to the people seated at the bar. I can see a businesswoman, a redheaded man dressed like a tourist and an older woman wearing a rather expensive beige jacket."
        "As I approach, the two women turn around and look me over."
        hi "{font=times}Ah... please excuse me.{/font}"
        "I instinctively bow before remembering that's not exactly a common practice in this country. I then bend down and reach out to grab Hanako's cue ball which has rolled under one of the women's barstools."
        "But before I can take the ball, I hear the occupant of the barstool clear her throat. With a puzzled look I get back up."
        "She gets off the barstool, reaches down, takes the ball and drops it into my hand."

        # show karla smile
        # with charaenter

        ka_ "{font=times}There you are.{/font}"
        hi "{font=times}Thanks, but it really wasn't... necessary to...{/font}"

        # show karla laugh
        # with chchange

        "The woman stops me with a gesture and gives me a mischievous smile."
        ka_ "{font=times}You were just… retrieving something you dropped, correct?{/font}"
        hi "{font=times}Yes?{/font}"
        "I wonder what exactly she's getting at? She chuckles as if I just said something hilarious."
        ka_ "{font=times}Every Scotsman is... familiar with that old trick, lad.{/font}"
        "What does she...{w=0.5} {i}wait a second!{/i}"
        "As I realize what she's insinuating, I visibly reel in shock."
        hi "{font=times}I wasn't trying to...{/font}"
        "The bartender and the other woman both laugh as they watch me blush."

        # show karla smile
        # with chchange

        ka_ "{font=times}It's a joke, lad. I hope you're not angry.{/font}"
        "Not really knowing how to respond to her, I simply shake my head and walk back to the billiards table."

        scene bg inverness_pubbilliards
        show hanako emb_smile
        with locationchange

        hi "I had to go through a lot to get this back for you."
        "Hanako smiles and plants a soft kiss on my cheek."
        ha "Thank you."
        "Since Hanako got a foul by striking a ball off the table, it's now my turn again. I retrieve my cue and take careful aim."

        show hanako basic_normal
        with chchange

        hi "By the way, what was it you were about to ask before you bounced that ball off the table?"
        ha "Hmmm? Oh, I wanted to know... what direction you thought I h-had in mind for myself."
        "I strike the cue ball and manage to hit both other balls, but my ball ends up resting against one of the edges of the table, making the next shot a tricky one."
        hi "Well, my reasoning was that since you seem to handle computers pretty well you could perhaps try for a career in the IT sector. There's a pretty high demand for people with experience in that area."
        "Not to mention the fact that that area also draws people with slightly less well-developed social skills, meaning Hanako would stand out less. I decide not to mention this though."
        ha "I did... think about that. There's this girl at the n-newspaper club who does the editing together with me."
        hi "The girl with the large cast on her arm?"

        show hanako basic_worry
        with chchange

        ha "Yes. Jun. She really likes computers. The few times we speak, she usually speaks about them. About v-video games and computers in general. It made me realize... I l-like working with them, but they d-don't interest me enough to make a career out of it."
        "I am about to reply to her when we're surprised by a sudden buzzing noise."
        hi "Time is up."

        show hanako basic_bashful
        with chchange

        ha "And you've won."

        show hanako basic_normal
        with chchange

        "I have, though only by a few lucky shots. We are only a few points apart. If we play another game, it might very well end differently."
        "We both look at the buzzing case with a look of annoyance."
        "Hanako starts gathering the balls in order to return them to the case while I start searching my wallet for coins to insert into the slot."
        "Before either of us can finish, the buzzing suddenly stops."

        show hanako cover_worry
        with chchange

        "I look up and notice the patron who flustered me earlier standing next to the time clock. She must have put some coins of her own into the slot."
        "She gives us a friendly smile."

        # show karla smile at tworight
        # show hanako at twoleft
        # with charaenter

        ka_ "{font=times}To make up for {shader=wave:u__amplitude=2.0:u__frequency=0.5}????????? ?????{/shader}.{/font}"
        hi "{font=times}Ah, excuse me?{/font}"
        "Hanako seems to have caught the patron's meaning as she whispers into my ear."
        ha "She said it's to make up for embarrassing you. What d-did she do?"

        show hanako cover_bashful
        with chchange

        "I briefly tell Hanako what happened when I went to retrieve her cue ball. Hanako looks a bit sheepish. I can tell she finds it somewhat amusing, but doesn't want to laugh since I went to get the ball back that she shot off the table."
        hi "I have no idea if this is the famed British humor or if this person is just plain weird."

        show hanako cover_distant
        with chchange

        "The patron watches our conversation with an amused expression, though she obviously can't understand what we're saying."
        "When we stop talking, she shrugs her shoulders."
        ka_ "{font=times}Well... it... was a rather bold action.{/font}"
        hi "{font=times}Sorry... err... We're on... vacation here. My English... is not very... good.{/font}"
        "This gets her to smile."
        ka_ "{font=times}It's not that bad. I can understand you well. Your… pronunciation is good.{/font}"
        hi "{font=times}That's... ah... good.{/font}"
        "I'm finding her rather easy to comprehend compared to most people here, and suddenly I realize why."
        "Instead of a Scottish dialect, she's been speaking to us in common English without a very noticable trace of a local accent and it sounds like she's been doing her best to speak slowly and clearly."
        hi "{font=times}You're... not from around here?{/font}"
        ka_ "{font=times}I am, but I deal with many people from abroad at my work so I try to speak plain English when talking to people who aren't Scottish themselves. I can speak Scottish if you like.{/font}"
        hi "{font=times}Please don't.{/font}"
        ka_ "Or maybe I should speak in Japanese instead. It'll probably make it easier for us to understand one another."

        show hanako def_shock
        with chchangefast

        "Both Hanako and I gasp in surprise since that last statement was delivered in accented but otherwise completely fluent Japanese."
        hi "Y-Y-You speak Japanese?"

        # show karla laugh
        # with chchange

        "The woman allows herself a brief laugh at our astonishment."
        ka_ "Hmm hmmm. I've lived in Japan for over 20 years. "

        show hanako def_worry
        with chchange

        "The woman makes a polite bow."
        ka_ "I'm very honored to meet my daughter's best friends."
        hi "Are you...?"

        show hanako at twoleft
        with charaenter

        show karla smile at tworight
        with Dissolve(1.0)

        ka_ "...Lilly's and Akira's mother? I am. Here in Scotland we're not as formal as people are in Japan. Would you mind if I address the two of you by your first names while you're here?"
        "I share a quick look with Hanako, who is still trying to digest what just happened and can only manage a flabbergasted nod."
        "When in Rome..."
        hi "Err... That's okay."

        show karla basic_smile_suit
        with chchange

        "The woman smiles broadly and extends her hand."
        ka "Then I will address you as Hisao and Hanako, and you can call me Karla. Pleased to meet you."
        "Despite my dumbfoundedness, I manage to extend my hand and am given a firm, confident handshake."

        show hanako defarms_worry
        with chchange

        "After a subtle nod in her direction, Hanako remembers to follow my example and hesitantly sticks out her hand for a handshake as well."
        hi "Karla?"

        show karla basic_cheerful_suit
        with chchange

        ka "Yes. Karla Satou."
        "After shaking Hanako's hand, Lilly's mother turns to me."

        show hanako def_worry
        with chchange

        ka "It seems I caught you two by surprise. Didn't Lilly tell you that I'd be picking you up tonight?"
        hi "She did mention we'd get ‘private transport’, but I didn't expect anyone to turn up this early. I also wasn't quite sure what either of you looked like."

        show karla basic_sheepish_suit
        with chchange

        ka "I suppose I did get here sooner than initially planned. I was getting a bit tired of courting investors, and my husband and the colleague who was with us seemed to be handling things fine without my input."
        ka "I was already slated to leave early in order to pick all of you up, so I figured I could be missed for a little while longer. I don't get many opportunities to see my two daughters together."

        show hanako emb_timid
        show karla basic_smile_suit
        with chchange

        "She gives the two of us a long analyzing look that makes Hanako fidget nervously."
        ka "I wasn't sure what either of you looked like either. We spoke briefly on the phone before, didn't we? I think you look a little like I imagined you to look like."
        hi "You look quite a bit more like your youngest daughter than I imagined."

        show hanako basic_normal
        show karla basic_smileclosed_suit
        with chchange

        "She chuckles modestly."
        ka "I'll take that as a compliment."
        "My words were more an honest appraisal than an attempt at flattery. I can instantly tell that Lilly gets most of her looks from her mother."
        "Karla Satou is a tall woman, probably as tall or even slightly taller than Lilly with a similar figure and similar wavey, blonde hair, although I can spot a slight streak of grey near the roots."
        "Her eyes are deep blue like Lilly's, but unlike Lilly's cloudy and unreadable stare, Karla's eyes have a sharp and curious gaze to them, and I can see a twinkle in there that I've seen in Akira's eyes as well."
        "While looking just as formal, Karla's attire looks a lot more feminine than Akira's office clothing. She must be in her fifties already, but she's still quite good-looking."
        "Unlike Lilly, who has a rather pale complexion, Karla has a rather obvious tan, suggesting she's an outdoor person. It would explain her rather fit and healthy appearance."
        hi "Do Lilly and Akira know that you're here already?"

        show karla basic_smile_suit
        with chchange

        ka "They do. I made sure Akira spotted me when I came in here. Unfortunately I can't just walk up to them to say hello while the pub quiz is still going on. People might think I'm feeding answers to my daughters."
        ka "So until that quiz is finished, it'll be just the three of us—if you don't mind some company while playing billiards, that is. I promise not to intrude."

        show karla basic_smug_suit
        with chchange

        ka "I can even retrieve stray cue balls for you if you like."
        "{i}Ouch!{/i}"

        show karla basic_smileclosed_suit
        with chchange

        hi "I... don't mind."

        show hanako basic_worry
        with chchange

        ha "M-Me neither."
        ka "Wonderful. I'll go and get my beer from the bar. Can I get you two anything to drink? It's on me."
        hi "Really? Could you please get me an orange juice then?"
        ha "F-For me too, please."
        ka "Coming up."

        hide karla
        with charaexit

        "As Lilly's mom walks back to the bar, I turn to Hanako with a slight smirk."
        hi "Lilly’s figure coupled with beer and a business suit. I'm shooting for a 50/50."

        show hanako emb_smile
        with chchange

        "Hanako presses her hand to her mouth to hide a giggling fit."
        "Looks like I wasn't the only one appraising Karla and trying to determine whether she's more like Lilly or Akira."
        ha "Yes."
        hi "So, wanna go for another game? I believe I now owe you a rematch."

        show hanako basic_smile
        with chchange

        ha "Let's play again."

        show karla basic_sweet_suit at tworight
        with chchange

        "As we put the balls in position, Karla comes back and places two glasses on the edge of the billiards table."

        show hanako basic_bashful
        with chchange

        ka "Lilly told me the flight was kind of a taxing experience. Have you two gotten your bearings back already?"
        hi "I'm still suffering from jetlag, but I'm pretty well-rested right now. The accommodations have been really good."
        "Karla smiles appreciatingly."
        ka "Don't hesitate to ask if you need anything. If I'm not around, feel free to approach the staff. I take it you've met Allison?"
        hi "We have. She's a very good cook."

        show karla basic_smileclosed_suit
        with chchange

        ka "She is. If you get homesick, be sure to ask her to cook up some Japanese meals. She may not speak your language, but she knows a truckload of Japanese recipes. She {i}is{/i} employed by my husband after all. And don't be afraid to ask her if you need anything else."
        "It's nice to hear we're essentially having our own private restaurant. This vacation just keeps getting better and better."

        show karla basic_smile_suit
        with chchange

        "Hanako and I resume our game, and true to her word, Karla mostly goes back and forth between watching our game and listening to the quiz host's questions without making a lot of conversation aside from occasional small talk."
        "We hear the buzzer again after what turned out to be an intense neck-and-neck race, and I let out a sigh as I realize that I'm a handful of points behind Hanako."
        hi "Well, at least we kept the suspense going until the very end."

        show hanako basic_smile
        with chchange

        "Hanako permits herself to show a proud little smile."
        ha "It was a good game."
        ka "I guess you two are even now, huh?"
        "Karla picks up the balls and puts them back on top of the time clock device, shutting down the annoying buzz."
        hi "We are. We may need a third game to break the tie."
        "Hanako's expression tells me she'd be up for that, but Karla motions toward the front area and I notice the quizmaster is no longer on stage."
        ka "You might want to wait with that for a moment. It looks like they're checking everyone's answers right now. We'll probably hear who has won in a few minutes."
        hi "I wonder how they did."
        ka "What team name did they come up with?"
        hi "Team name?"

        show karla basic_sheepish_suit
        with chchange

        ka "Not familiar with pub quizzes, are you? It's sort of a tradition for each participating team to think up a creative name. Like erm... ‘Knuckleheads’ or ‘Intellectually Challenged’ or ‘B for Dyslexic’. That sort of thing."
        hi "They've probably picked one without us. We'll just have to see."

        show karla basic_smile_suit
        with chchange

        "Knowing Lilly, it might very well be a play on blindness of some kind... That'd be the sort of thing she'd do, though that wouldn't apply to Akira, so maybe they went with something else."
        "Suddenly the quizmaster gets back on stage and gives a few taps on the microphone in order to make clear he has something to say."
        "I try my hardest to make out what he's saying, but his accent and our distance from the stage make that somewhat of a lost cause. Lilly's mom seems to read my mind."

        show karla basic_cheerful_suit
        with chchange

        ka "Right now he's simply thanking everyone for participating. The people who came in third will get a free drink, the ones in second place will get three free drinks, and the winners will get a special prize."
        hi "And what would that be?"

        show karla basic_sweet_suit
        with chchange

        ka "Usually just drinks. This is a pub after all."

        play sound sfx_applause

        "The quizmaster makes an enthusiastic gesture, and the people in the room burst into applause at his words."

        show karla basic_smile_suit
        with chchange

        ka "Third place goes to ‘The Masters of Romance’. I don't think that's them."
        hi "Doesn't sound like it. Who on earth would think up such a name anyway?"

        play sound sfx_applause

        "Another announcement from the quizmaster and another applause follows."

        show karla basic_smug_suit
        with chchange

        ka "Second place goes to ‘The Master Baiters’. That had {i}better{/i} not be them."
        hi "Naw. Lilly's too classy for that."

        show karla basic_cheerful_suit
        with chchange

        play sound sfx_applause

        "Finally the winner is announced and Karla brightens up."
        ka "Well, well. Winner of tonight's quiz is ‘Oriental Express’. Heh, clever."

        scene bg inverness_pubdoor
        with locationchange

        "Sure enough, I can see Akira and Lilly getting up as a thunderous applause fills the room. Karla, Hanako and I are happy to join in with the applauding crowd."
        "Akira takes Lilly's hand and carefully guides her up the stage."
        hi "That’s pretty amazing. Two people who’ve lived in Japan their entire life beating what’s probably a bunch of locals."
        ka "Heh, the questions they use here are never about local tidbits during the summer break. Gotta give the tourists a fair chance, after all. It’s still impressive though."

        show lilly basic_weaksmile at twoleft
        show akira basic_laugh at tworight
        with charaenter

        "After the quiz host gives both of them a firm handshake, Akira feistily throws her hand up in the air and gives a ‘V for victory’ sign. Lilly merely gives a few modest waves as she's handed a bag presumably containing their prize."

        play sound sfx_applause

        "Their presence on stage results in another wave of applause and more than a few wolf whistles as well."
        "Lilly and Akira seem to take the attention pretty well, but I'm happy Hanako and I decided not to join the team. I don't think getting up on stage would be Hanako's idea of a great time."
        "Knowing that Akira will eventually go back to where she left us, I decide to stay near the billiards table rather than meeting the sisters in the middle of a noisy crowd."

        scene bg inverness_pubbilliards
        show hanako basic_smile at right
        show lilly cane_smileclosed at left
        show akira basic_smug at twoleft
        show karla basic_smile_suit at tworight
        with locationchange

        stop sound fadeout 1.0

        "Eventually they get down from the podium and slowly make their way back to where we are."
        aki "Man, those guys were no challenge at all. Imagine how easily we'd kick their asses if we'd take them on on our home turf."
        hi "Well done you two."

        show hanako basic_bashful
        with chchange

        ha "Congratulations. What d-did you win?"

        show akira basic_cheerful
        with chchange

        aki "Let's have a look, shall we?"
        "Akira takes the bag from Lilly and looks inside, then fishes up a bottle with a honey-colored liquid inside."

        show akira basic_smile
        with chchange

        aki "Heh, Scotch whisky. Two bottles. I should've guessed."
        "I take a look at the name on the bottle's label and promptly get a headache."
        hi "Geez, can people around here actually pronounce that name?"
        aki "Auchentoshan? Can't say I've tasted that one before, but this is not cheap liquor we've got here. Looks like we just won back our entry fee big time."

        show akira basic_smug
        with chchange

        aki "Although..."

        show lilly cane_cheerful
        with chchange

        li "I wonder..."

        show karla basic_angry_suit
        with chchange

        "I'm sure I know what Lilly's thinking. I'm not sure how serious she is, but I can see her mother's eyes narrowing."
        ka "Lillian!"

        show lilly cane_oops
        with chchangefast

        li "Mother!"

        show hanako emb_downsmile
        show akira basic_laugh
        with chchange

        "Lilly's pout and the slightly whiny tone of her reply, as if she just got caught with her hand in the cookie jar, seem so out of place for her that Hanako can't hold back a giggle."
        "Lilly quickly recovers though and puts on her usual composed smile."

        show lilly cane_weaksmile
        with chchange

        li "Please use my real name, Mother."
        ka "I hope you weren't seriously considering drinking that."

        show hanako emb_smile
        with chchange

        "Lilly doesn't answer immediately. I know from experience that she has a habit of carefully choosing her words before speaking, but the slight delay seems to annoy Karla a bit."
        li "I admit it might be a little bit irresponsible."

        show karla basic_annoyed_suit
        with chchange

        "Karla shrugs her shoulders."
        ka "Only if you haven't been carefully and gradually building up your alcohol tolerance while you were in Japan."

        show lilly cane_listen
        with chchange

        li "I have not."
        "No carefully considered reply this time. Lilly seems to recognize the importance of quickly denying Karla's suggestion. I wouldn't be surprised if Lilly's mother thinks that Lilly never even drank alcohol before."

        show akira basic_ending
        show karla basic_smile_suit
        with chchange

        "Akira grins an amused grin before coming to her sister's rescue."
        aki "She does have a point, Lils. This Scotch contains 40%% alcohol. That's a bit much if you're not used to alcohol or don't know exactly where your limits lie."
        aki "Since it's a shame to waste our prize, why don't you let me try exchanging it at the bar for something milder? Like a few bottles of quality wine."

        show lilly cane_smileclosed
        with chchange

        li "Would that be acceptable, Mother? There's still a toast I have to perform when we get back."

        show karla basic_sweet_suit
        with chchange

        "Karla considers it for a moment and then gives a resigned nod."
        ka "I'm personally fine with that. Just remember that we have a picnic scheduled for tomorrow, and you're coming along, whether you're feeling up to it or not."

        stop music fadeout 2.0
        stop ambient fadeout 2.0
        scene black
        with Dissolve(2.0)

        if _in_replay:
            return

    return