label sh_ch20:
    label .s1:

        $ set_window_tint(TINT_HANAKO)

        call sisterhood_timeskip

        scene bg school_firstaidclass
        with Dissolve(2.0)

        play music music_daily fadein 4.0

        nvl clear
        nvl show dissolve

        n "My eyes go back and forth between three illustrations of a person lying on the ground, each one in a slightly different position."
        n "The idea is to cross off the picture of the optimal recovery position, but picture B and C look really similar except for a slight difference in the angle of the head. Doing my best to recollect the position of the practice dummy during our excercises last Monday, I pick illustration B and move on to the next question."
        
        nvl clear
        
        n "I'm currently the only person in class right now, except for the trainer. Everyone was present during the first three days, but the day afterwards, only Yuuko, a staff member whose name I forgot, and I were there, the three of us obviously being the only ones completely new at this."
        n "And today, the last day of the training, it's just me. Mister Nakamura took the opportunity this morning to make good on his promise and give me a private course through the chapter I skipped earlier this week—that being the chapter about burns and how to act in situations like someone's clothes catching fire or coming into contact with boiling water."
        n "The fact nobody else was in the room was probably the reason I didn't run out, lock myself in my room and hide under my bed."
        n "{vspace=30}Even so, I felt utterly miserable and ready to start screaming throughout the whole ordeal and was happy Nakamura did his best to go through it as quickly as possible without showing pictures or going into any more detail than absolutely necessary."
        n "{vspace=30}Now I'm busy taking a few small written tests to see how much of the whole thing stuck in there."

        nvl hide dissolve

        "The next question I get to involves the correct procedure to follow when someone has gotten a corrosive substance in his eyes…"

        play sound sfx_alarmbeep

        "…but before I can take a good look at the corresponding illustrations, I hear a sharp beep coming from the trainer's desk."
        "I get up as fast as I can, run over to a practice dummy in the corner, put my ear to its mouth, put my fingers on its throat, and finally put my hands on its chest before pressing down hard several times."

        show nakamura smile
        with charaenter

        nak "Well done. You're doing it faster and more fluidly each time."

        show nakamura neutral
        with chchange

        nak "Just remember to keep pressing down hard. You're not a muscle-bound PE teacher, so it's best not to hold back."
        "I give a subdued nod at the teacher's praise and get back to my desk to resume work on the test."

        hide nakamura
        with charaexit

        "This rather unusual practice drill was an idea of Mister Nakamura who thought that, instead of structured rehearsals, I'd be better off practicing at random intervals so I could learn how to act when taken by surprise."
        "So we agreed that every time he set off his ringtone, I'd run up to one of the dummies and go through the motions until they become a second nature."
        "Back at my desk, I pick up my pen again and hurry to finish the remaining four questions on my answer sheet."

        show nakamura smile
        with charaenter

        "I quietly drop it on Nakamura's desk, which results in a satisfied nod."
        nak "It won't take too long to correct this last one, Ikezawa. Why don't you wait around a bit until I'm finished and we can tie this whole thing up with a nice bow around it?"
        ha "O-okay."
        "I return to my desk, fiddling with my hair a bit."
        ha "N-no more practice drills?"
        nak "You've done more than enough of them throughout the week already. I think you have the motions down. I doubt doing any more drills will benefit you much."
        nak "All that's left would be an actual emergency to test you. And I hope you won't ever get into that situation."
        "I really hope so too. I'm still not too confident in my ability to handle such a situation."

        show nakamura speak
        with chchange

        nak "If it makes you feel better… panicking is a pretty common reaction to someone suddenly collapsing. It happens to a lot of people."
        "That doesn't make me feel better at all. If Hisao has a heart attack in front of me and I shut down because of it, it won't matter to me if it's a common reaction or not. It won't make my failure any more acceptable to me."

        show nakamura smile
        with chchange

        nak "By the way, your previous test was 81%%. That's a pretty good score. Looks like you've done your homework."
        ha "T-thanks."
        nak "So, do you have any plans for the upcoming three weeks of summer break you have left?"
        ha "I… ummm… am going to S-Scotland together with my b-best friend and my b-boyfriend."
        nak "Sounds fun. Any reason for Scotland specifically? Most tourists from Japan try to visit multiple countries while in Europe."
        ha "M-my best friend's p-parents live there. She's visiting them, and we're a-allowed to come along."
        nak "Well, I hope you'll have fun."

        show nakamura neutral
        with chchange

        nak "By the way, could you check out page 156 of your binder?"
        ha "Huh?"
        "I curiously turn to the page Nakamura mentioned and suddenly smile."
        ha "Oh!"

        show nakamura smile
        with chchange

        nak "Just in case."
        "On the page in front of me is a large table containing the emergency phone number of each country, sorted by continent. I quickly take out my cell phone and save the emergency number for the United Kingdom in its memory."
        ha "Thank you."
        "The trainer takes out a handkerchief, wipes his forehead, then smiles at me."
        nak "You're welcome."

        hide nakamura
        with charaexit

        "I start to casually browse through the binder, not really reading but mostly keeping myself busy."
        "As I look up, I can see Nakamura is again wiping his forehead."
        "What's going on? It's not that hot here, is it?"
        "After a few minutes, I catch him again taking out his handkerchief."
        "He's looking a bit uncomfortable. Is he unwell or something?"

        stop music fadeout 2.0

        ha "Ummm… A-are you… o-okay?"
        "He lets out a chuckle in order to dismiss the matter."

        show nakamura awkward
        with charaenter

        nak "I'm fine. I might be coming down with something. My luck, of course. Right around the start of my own summer break."
        "He slowly gets up, an uncomfortable expression still on his face."

        show nakamura strain
        with charachangealways

        nak "I… think I'm going to take a small bathroom break. I'll be right back. Could you open the window in the meantime? Let in some fresh air?"
        ha "S-sure."

        hide nakamura
        with charaexit

        "As I head towards one of the windows, I notice Nakamura is walking a bit hunched over. It gives me an uneasy feeling in the pit of my stomach."

        play sound sfx_collapse

        "I turn towards the window and am about to push it open when I hear a soft groan behind me."

        show black:
            alpha 0.8
        show n_vignette:
            alpha 0.5
        with Dissolve(1.0)

        play music music_tension fadein 4.0

        "As I look behind me, I'm shocked to see that Nakamura is lying face-down on the floor, about 10 steps away from the door."
        "I physically reel from a sudden and almost overwhelming sense of dread that spreads through my body."
        "What's going on? Did he just collapse? What's wrong with him? What am I supposed to do?"
        ha "Mister Nakamura?"
        "My voice barely reaches above a whisper as I struggle to control my breathing."
        ha "Mister Nakamura?!"

        show bg:
            align (0.0, 1.0) zoom 1.2
        with locationchange

        "Somehow, I'm capable of making it across the room without my shaking legs giving out and I kneel next to him, rolling him onto his back."
        ha "Mister Nakamura!!"
        "No reaction. What should I do now? Go and get help? But it's already nearly a week into summer break and the building is nearly deserted."
        "What if he dies while I'm away? Why isn't anyone else here?"
        "I guess I can't leave him alone."
        "Doing my best to righten his head, I suddenly remember the first step of the drills I've done."
        "Putting two fingers beneath his jaw, I {i}think{/i} I can feel a pulse."

        play sound sfx_heartslow

        "Of course, it's almost impossible to be sure with my own heart pounding like a jackhammer, but it's a small relief."
        "Putting my ear to his mouth, I can't hear any breathing, though. Am I supposed to give him mouth-to-mouth or mouth-to-nose now?"
        "I really hate the idea of anyone's face but Hisao's getting close to mine—close enough to peek past my bangs and see the damage. Still, do I have a choice?"
        "I suddenly have an idea."
        "I carefully move his head back and open his mouth further, then carefully use my other hand to cover his eyes."

        hide black
        hide n_vignette
        with dissolve

        stop music fadeout 2.0

        "As I move my head downward though, Nakamura suddenly exhales loudly, causing me to jump up with a startled cry."

        show bg:
            align (0.0, 0.0) zoom 1.0
        show nakamura neutral
        with locationchange

        "As I look on, Nakamura casually gets up, dusts himself off and gives me a concerned look."
        nak "Are you alright, Ikezawa? Just sit down and take a few deep breaths. I'm fine. I was just faking it. I was holding my breath on purpose."
        "Faking it? He was just pretending to…?"
        "I barely manage to stammer what's on my mind."
        ha "W-why?"

        show nakamura smile
        with chchange

        play music music_nurse fadein 4.0

        "After making sure I'm not going to faint, Nakamura walks back to his desk and gives me a sheepish look."
        nak "I figured one more practice drill was in order."
        nak "Sorry to have frightened you. I wasn't even sure if it was going to work. I'm not exactly a seasoned actor. I'm surprised you didn't merely roll your eyes at me."
        "I should have known. He was testing me. He wanted to see if I'd call for help or go through the motions I practiced so many times or if I'd just run away or collapse in a shivering heap."
        "I was dangerously close to doing the latter, that much is certain."
        "And then what? Then my first aid certificate would be worth less than the paper it's printed on. I'd know in advance that this whole week had been a waste of time."
        "I'd end up feeling utterly worthless and more frightened of the prospect of Hisao's heart acting up than ever."
        "For a moment I feel angry with Nakamura for drawing out my weakness with such little effort."
        nak "I just finished your last test and your score is 84%%. Very well done."
        "I nod in response, but don't really say anything. I'm still busy fighting off the adrenaline that's racing through my system."

        show nakamura neutral
        with chchange

        "Nakamura frowns, gets up and sits on one of the desks in front of mine."

        show nakamura speak
        with chchange

        nak "I guess what I did was a bit thoughtless, but I thought it was important to get an idea on how you'd react in a real emergency situation… or at least as real as possible."
        nak "The truth is that Mrs. Takawa asked me to give her my opinion on whether this training would be any use to you in such circumstances, and I thought this would be a good way to see for myself."
        nak "If you'd have broken down just now, that would have given this week a real downer ending, but at least I could have reported to your therapist that this training wasn't sufficient on its own and that she'd best go and try something else."
        nak "I figured the last thing you needed was a sense of security that'd prove to be false at the worst possible moment. I hope you can understand and that it helps to make you a little bit more confident about what you've learned here this week."
        "I can't say I don't understand his motivation, but I'm nevertheless unsettled at how panic-prone I just proved to still be, even though it didn't paralyze me this time."

        show nakamura smile
        with chchange

        nak "You hesitated a bit, but you still reacted within an acceptable timespan. So I think you really deserve this."
        "He takes a fancy piece of paper from behind his back that I can see has my name on it and puts his signature on the dotted line near the bottom before handing it to me."
        nak "Congratulations on succesfully finishing the training, Ikezawa."
        "I take it from him, still a bit shaky but also filled with a modest sense of pride."
        ha "T-thank you."

        show nakamura speak
        with chchange

        nak "If you still have any questions for me, now would probably be a good time to ask. If not, I'm going to start packing up the dummies and get ready to head home."
        "I do have one question."
        ha "Umm…. W-were y-you enacting an actual h-heart a-attack just now?"

        show nakamura neutral
        with chchange

        nak "A little bit. Unlike what movies would like you to believe, heart attacks are rarely instantanous. But warning signs may vary from person to person."
        ha "Warning signs?"
        nak "You can find a list of the more common ones on page 34 of your binder. Though if you're currently thinking of your boyfriend, please be aware that what sent him to the hospital last time wasn't a traditional heart attack."
        ha "Ah…"

        show nakamura instruct
        with chchange

        nak "Remember that actual heart attacks involve the coronary artery getting clogged, resulting in part of the heart being deprived of oxygen and being damaged as a result. Your boyfriend's arteries are probably fine."
        nak "His problem is that his heart occasionally starts a disfunctional rhythm. It's a different problem altogether. That doesn't mean he never experiences any warning signs, but… I think it's best if you try not to worry about those."
        "Not worry about them? Is he joking?"

        show nakamura neutral
        with chchange

        nak "Your boyfriend is probably well aware of his condition, and if any warning signs pop up that indicate an approaching episode, I'm willing to bet my life on it that he'll be aware of them long before you start noticing them."
        nak "Ultimately, it's his responsibility to take action and either slow down or warn others. If you sound the alarm each time he looks a little bit unwell, instead of trusting his judgement on it, you'll probably drive him and yourself crazy sooner or later."
        nak "He's still as susceptible to colds and stomach aches as any other person after all."
        "That's a pretty good point, though I've never been good at applying the ‘no worrying’ advice to my own life."

        show nakamura speak
        with chchange

        nak "If his heart gets into a disfunctional rhythm it won't come out of, the best thing you can do is be aware of the location of the nearest AED."
        nak "I've noticed this school has quite a few of them hanging on the walls. I'm sure the head nurse here can get you a map of their locations."
        ha "And outside of the s-school?"
        nak "I'd like to suggest him getting an AED of his own at some point, but that's easier said than done. The one you've been practicing with this week costs as much as I pay in rent over the course of two months."
        nak "Still, in the long term, it'd be a good investment."
        ha "A-anything else?"

        show nakamura smile
        with chchange

        nak "Try not to worry too much, and don't forget to enjoy life. Compared to other heart conditions, people with your boyfriend's condition still tend to live fairly long lives. And new scientific discoveries are made every day."
        "That cheers me up a little."
        "I give him a tired smile and pick up my bag from my desk."
        ha "T-thank you… f-for everything."
        nak "Glad to be of service. Have fun in Scotland."
        ha "I w-will."

        stop music fadeout 2.0

        if _in_replay:
            return
    
    label .s2:

        $ set_window_tint(TINT_HANAKO)

        scene bg school_newspaper
        show naomi bend_smile at tworight
        show jun cast_smile at twoleft
        with locationskip

        queue music music_tranquil fadein 4.0

        ha "E-excuse me?"
        "After leaving the classroom, I decided to stop by at the newspaper club for just a few minutes and was greeted by Naomi and Jun who seem to be the only members still around the school grounds."
        "When I entered the room, Naomi greeted me with a series of sounds that sounded like total gibberish to me."
        na "I said: ‘Awrite! Hou's it gaun?’ You don't know what that means?"
        ha "S-should I?"

        show naomi bend_laugh
        with chchange

        na "It means ‘Hi! How are you?’ in Scottish. You were supposed to answer with something like ‘A'm fine, slainte!’"

        show jun cast_weaksmile
        with chchange

        "Naomi looks very pleased with her performance, but Jun gives me a tired look."
        jun "I looked up some Scottish phrases on the internet for her this morning, and she's been practicing them out loud ever since. Hopefully she'll stop now."

        show naomi basic_smile
        with chchange

        "Naomi playfully sticks her tongue out at Jun."
        na "You're just jealous because my Scottish is better than yours."

        show jun cast_eyeroll
        with chchange

        "Jun just rolls her eyes and Naomi takes the opportunity to continue the conversation."
        na "You haven't been practicing your Scottish?"
        "I haven't. Lilly assured me that our English would suffice, so I can probably communicate with the locals if—and only if—I absolutely have to."
        ha "This week was busy for me."

        show naomi bend_smile
        with chchange

        na "Oh, right. Still that first aid training, huh? How'd it go?"
        ha "I finished it today."

        show jun cast_happy
        show naomi bend_laugh
        with chchange

        "I produce the certificate I got earlier from my bag and hand it to Naomi and Jun. Naomi looks it over for a second before passing it to Jun."
        "They then smile and break out into a short but sincere applause. Or rather, Naomi's clapping while Jun's mimicking the motion as best as she can."
        na "Great job. I bet it's a little easier to go on vacation now with that one behind you, isn't it?"
        ha "Yes. I'm happy the two didn't overlap."
        na "Looking forward to it?"
        ha "I am. Do you h-have any vacation plans?"

        show naomi basic_smile
        show jun cast_serious
        with chchange

        "Jun just shakes her head. Naomi, on the other hand, nods enthusiastically."
        na "I'm going on a trip across Japan. Natsume's coming, too. We'll head north first, stay in Hokkaido for a bit, then head south towards Kyoto."
        ha "That sounds enjoyable, too."
        na "It will be. I'll be sure to take plenty of pictures. We can swap photos afterwards."
        "That might be a problem. My cell phone has a camera function, but it doesn't have enough capacity to store a large amount of photos, and I don't have an actual photo camera myself."
        ha "I could… buy a g-guidebook while I'm there."

        show naomi basic_neutral
        with chchange

        "Naomi makes a face as if I just offered her a spoiled sandwich."
        na "That won't do. You're a member of the newspaper club now. That means you gotta walk the walk. No taking shortcuts."
        ha "Ah… B-but I…"
        na "Just a sec."

        show naomi at offscreenright
        with charamovefastest
        hide naomi
        with None

        "Naomi gets off the desk she's sitting on and sprints into the room we use as our archive."

        show jun cast_speak
        with chchange

        "Jun scratches her arm and turns to me."
        jun "Naomi asked me to come along with her, but I need to have this cast removed next week. They're probably going to wrap it in stiff bandages if it's healed sufficiently."
        jun "I hate these heavy things. They really itch."
        ha "I'm s-sorry to hear that."

        show jun cast_smug
        with chchange

        jun "It's okay. I have plenty of video games I still need to finish."

        show naomi bend_smile at offscreenright
        with None
        show naomi at tworight
        with charamovefastest
        show jun cast_smile
        with { "master": charachangealways }

        na "Tadaah! Check this out!"
        "Naomi comes running back in, carrying a black bag in her hands."

        show hanako_camera at displayitemshow
        with Pause(1.0)

        show hanako_camera at displayitem
        with None

        "She opens it and fishes a slick-looking camera out of it, along with several small plastic containers with memory cards inside."

        show naomi bend_laugh
        with chchange

        na "You don't have a camera yourself, do you? Well, what do you think of this baby? There's at least twelve gigabytes worth of memory cards in here too. You can take enough photos to wallpaper the entire classroom with and still have space to spare."
        "Wow! Is she really lending me this? That camera looks really expensive."
        ha "F-for m-me?"

        show hanako_camera at displayitemhide
        with Pause(1.0)

        hide hanako_camera
        with None

        "Naomi simply gives a cheerful nod."

        show naomi basic_smile
        with chchange

        na "I was thinking of taking it myself, but since I'm dropping by at my parents' place before my own trip, I can simply take their camera instead."
        na "You can't fly to the other end of the world and not take any pictures. That's journalistic malpractice. And we won't have any of that around here."
        ha "T-thank you s-so much."
        na "You're welcome. If you want to thank me, maybe you could take some requests from me."
        ha "Requests?"

        show naomi basic_grin
        with chchange

        na "Since you're going to Scotland, are you going to visit that lake? You know, Loch Ness?"
        ha "I hope so. It's only a few kilometers away from Inverness."
        na "They say there's a monster in there. It would be grand if you could snap a picture."

        show jun cast_eyeroll
        with chchange

        "Jun promptly makes a facepalm gesture with her hand, which looks rather absurd due to the huge cast wrapped around it."
        jun "You know that's an urban legend, don't you?"
        "Naomi shrugs."

        show naomi basic_smile
        with chchange

        na "How about a picture of a Scotsman? You know, in traditional garb."
        ha "I might be able to do that."

        show naomi bend_wink
        with chchange

        na "Great. But no phonies. It has to be a true Scotsman."
        ha "Ah… O-okay."
        "Naomi lets out a pleased giggle."
        na "Wonderful."

        show naomi basic_smile
        show jun cast_smile
        with chchange

        "Naomi puts the camera back into its bag and hands it to me. I take it from her and put it into my own bag, being as careful as I can with it."
        "This is a really pleasant surprise. I'm so happy I decided to drop by the club today."
        na "Now, in case taking those pictures gets your journalistic juices flowing, there's something you can brainstorm about. I've decided what the next club you'll be covering in your column will be."
        ha "Which one is it?"

        show naomi basic_neutral
        with chchange

        "Naomi makes a face as if I just asked her a very stupid question."
        na "This one, of course. You'll have the advantage of not having to put together a question list for an interview."

        show naomi bend_smile
        with chchange

        na "Just write something up using your own experiences here, and we can take a look at it after the summer break to see if there's anything missing. Try to emulate the style of your previous column for consistency's sake."
        ha "I'll do that."

        show naomi bend_wink
        with chchange

        "She winks at me."
        na "Don't make us look bad."
        "I smile as I take my bag and get ready to head to my dorm room."
        ha "I'll p-put some extra l-love into it."

        show naomi bend_laugh
        with chchange

        "Naomi gives me a thumbs-up."
        na "Attagirl. Well, guid cheerio the nou then."
        ha "Eh?"
        na "Means goodbye. In Scottish."
        ha "Bye."

        hide naomi
        show jun cast_happy_close at center
        with charachangealways

        "As I leave the room, Jun comes after me with a conspiring expression on her face."
        jun "If you {i}do{/i} take a picture of Loch Ness, could you mail it to me?"

        show jun castraise_laugh_close
        with chchange

        jun "I can probably photoshop a monster in there."

        stop music fadeout 2.0

        if _in_replay:
            return

    label .s3:

        $ set_window_tint(TINT_HANAKO)

        scene bg school_dormlilly
        show lilly basic_smile at twoleft
        show hisao basic_smile_uni at tworight
        with locationskip

        queue music music_dreamy fadein 4.0

        li "I'll let you handle the tickets, Hisao."
        "Hisao takes the envelope containing our flight tickets from Lilly and carefully puts them away."
        hi "I'll make certain not to lose them, Lilly."
        li "Good. Have the two of you finished packing all your luggage already?"
        hi "I have. Hanako?"
        "Fortunately, I have too. Knowing this'd be a busy week, I've already tried to pack whatever I could last weekend."
        ha "Me too."

        show lilly basic_cheerful
        with chchange

        "Lilly gives a satisfied nod."
        "As I look around her room where we've spent the last half hour drinking tea and discussing the final preparations, I notice that Lilly's own suitcase is still only half-full, though I doubt I'd be able to even pack a single thing without being able to see."
        ha "Do you need some help with packing, Lilly?"

        show lilly basic_smileclosed
        with chchange

        li "No, thank you, Hanako. I know exactly what items I still have left to pack, and I'll be sure to finish things up soon."
        ha "Okay then."

        show lilly basic_weaksmile
        with chchange

        "Lilly lets out a short sigh."
        li "In other circumstances, we would be celebrating you getting your first aid certificate right now. I feel bad we lack the time for that at the moment."
        ha "It's okay. It's for a good reason after all."

        show lilly basic_smile
        with chchange

        li "We will hold a celebration for you once we're in Scotland, Hanako. That is a promise."
        ha "T-Thank you, Lilly."

        show hisao basic_speak_uni
        with chchange

        hi "I think it's probably best if Hanako and I take our leave now, Lilly. That'll give you time to wrap things up and get some rest."

        show lilly basic_smileclosed
        with chchange

        li "That might not be a bad idea, Hisao. Let us assemble in my room tomorrow morning at ten o' clock. That'll leave us enough time to get to the station and take the train to the airport."

        show hisao basic_smile_uni
        with chchange

        hi "Sounds like a plan. Good night, Lilly."
        ha "Good night, Lilly."

        show lilly basic_cheerful
        with chchange

        li "Good night, Hanako, Hisao. Rest well. Tomorrow will be a very exhausting day for sure."

        scene bg school_girlsdormhall
        show hisao basic_smile_uni
        with locationchange

        play sound sfx_lock

        "As I unlock the door to my dorm room and turn around to kiss Hisao goodnight, he puts one arm around me."
        hi "Can I come in for a while?"
        ha "Sure."

        scene bg school_dormhanako
        show hisao basic_neutral_uni
        with locationchange

        play sound sfx_doorclose

        "We enter the room, and I take a seat on my bed. I feel tired and tense at the same time."
        "Today was stressful and exhausting. First the lesson on burns that hit several sensitive nerves, and then the trainer's faked heart attack right in front of me. And tomorrow might even be more nervewracking."

        show hisao basic_worry_uni
        with charaenter

        hi "Wow, your shoulders are still really stiff. I guess that little get-together with Lilly didn't really help?"
        "Hisao has placed a hand on my shoulder and gives me a worried frown."
        ha "It helped… a little bit."

        show hisao basic_smile_uni
        with chchange

        hi "Maybe this will help a little bit more."

        hide hisao
        with charaexit

        "He sits down behind me and gently starts massaging my shoulders."
        ha "That would be nice."
        "I let my head hang forward and try to relax as much as possible as Hisao massages the muscles of my neck and shoulders."
        "This is something he's been doing for me since we started dating—a way to take away whatever stress I built up over the day."
        ha "You can… d-do it a little more forcefully."
        hi "This might make a difference too."
        "Hisao reaches around and unbuttons my blouse. I let it slide off my shoulders while he rubs his hands together to warm them. Moments later, I feel a warm hand on my bare left shoulder stroking it and then kneading it firmly."
        "Minutes pass without either of us saying anything, but the silence fortunately isn't too uncomfortable."
        "I've told Hisao all I cared to share about today earlier when I visited his room while he was in the process of packing his suitcase."
        "Right now, there simply isn't much to say."
        "After a while, Hisao gets off the bed."
        hi "Hanako, can you lie on your stomach now?"
        "I comply with his request and feel my hips being pressed down as Hisao straddles me. Then I feel his hands press down on my upper back and make long, firm strokes."

        show hisao basic_sweet_uni_close
        with charaenter

        hi "Hanako, I really appreciate the fact that you've made such a large effort this week on my behalf."
        ha "It… wasn't just for you. It was also for myself."
        hi "Well, regardless, I already feel a bit safer now than I did before."
        "I don't really share his optimism yet. This afternoon I've just barely managed to hold off a panic attack, and that involved someone I hardly even knew."
        "I'm still not very confident in my ability to hold things together if something were to happen to Hisao. Still, I feel a bit of happiness from his words."
        ha "T-thanks."

        show hisao basic_speak_uni_close
        with chchange

        hi "You know, the last time I spoke with her, I asked Miss Takawa for advice on what to do if you got overwhelmed by stress or fear again. Because I don't want to feel helpless either, like that time you had an episode in science class."
        ha "What d-did she s-say?"
        "Hisao stops the backrub he's been giving me until now and gets off the bed."

        show hisao basic_grin_uni
        with charadistant

        hi "I really liked her advice."
        ha "What w-was it then?"

        hide hisao
        with charaexit

        play sound sfx_rustling

        "He doesn't respond, but I hear a bit of rustling behind me."

        stop music fadeout 2.0

        play sound sfx_pillow

        "The moment I turn around, however, I feel a pleasant and warm sensation that elicits a surprised gasp from me."
        ha "Hisao!"

        play music music_heart fadein 4.0

        "It takes me a moment to realize that the rustling sound I heard earlier was Hisao taking off his shirt and while I was turning around to face him, he got back onto the bed and is now lying next to me and hugging me tightly."

        show hisao basic_sweet_nak_superclose
        with charaenter

        hi "She suggested something like this."
        "I giggle."
        ha "She s-suggested taking your shirt off?"

        show hisao basic_grin_nak_superclose
        with chchange

        hi "Hehe, not exactly. She suggested cuddling, though I don't think she'd object to some added intimacy if it helps the cause."
        "I wouldn't know about that, and I doubt I'll ever find out. My sex life is the one thing I've kept my therapist out of and, if possible, I'd like it to stay that way."
        ha "E-even if she'd… object, I w-wouldn't."

        # TODO Use pillowtalk CGs

        scene ev pillowtalk_placeholder_large

        "Hisao laughs softly and then plants his lips on mine. At first, our kisses are gentle, and we're content to just hold on to each other tightly, but soon our kisses become more feverish, and we're rubbing our bodies against each other."
        "Suddenly, Hisao moves his hand down and playfully squeezes my butt which causes me to let out a yelp and reflexively thrust my hips forward, causing my crotch to press against his."

        nvl show dissolve

        n "{vspace=60}Hisao chuckles at my gasp and stops our makeout session to let his forehead rest against mine and look into my eyes for several seconds before giving me a quick peck on the lips."
        n "{vspace=60}I know what that gesture means. He's used it several times in the past to get a question across that'd be too embarassing to ask with words. 'Do you want to have sleep together?'"
        n "{vspace=60}I also know how to give the affirmative response. If I respond with a quick peck back, the way things are now, it'll probably take less than 15 seconds for the last piece of clothing to hit the floor."
        n "{vspace=60}Yet there's a small sense of anxiety I feel that prevents me from immediately reciprocating his invitation. Maybe it's written on my face or maybe Hisao has noticed the pause."

        nvl clear

        hi "…Hanako. Would you… like to…?"
        "I merely lower my gaze, trying to work out my feelings."
        ha "Ummm…"
        hi "It has been some time."
        "That's certainly true. Between that night in a hotel where we had intercourse for the first time since the start of our relationship and the moment when Lilly announced her departure, Hisao and I did it several times."
        "While I tried to keep the afternoons and evenings open for Lilly during that time, I made sure to save the nights for Hisao. I learned two things about myself during that period in time."

        nvl show dissolve

        n "{vspace=60}The first was the fact that I actually possess a sex drive. I still prefer the lights to be either dimmed or off altogether and Hisao's always the one taking the initiative, but I've been seeking him out all those times knowing full well that we'd probably end up between the sheets together, and, while we were busy doing the deed, I found myself welcoming the experience."
        n "{vspace=60}The second thing I learned, however, was that my sex drive is also rather closely tied to my state of mind. So while I was busy taking Lilly on all sorts of outings, Hisao and I were far from hurting on the physical intimacy front. After Lilly announced her departure however, I quickly found I was unable to get into the mood."
        n "{vspace=60}And during Hisao's time in the hospital, well, I didn't think I'd even get so much as a kiss out of him anymore ever again. Even though we reconciled nearly two weeks ago, Hisao's been forced to take it slowly ever since, and I obviously haven't been eager to push him past his limits."

        nvl clear

        ha "I… I know."
        hi "And you seemed to be in the mood just now."
        "I was and part of me still is. My mood isn't really the issue. If it hadn't been for the fact Hisao was just released from the hospital a few hours earlier, I would have been happy to have my first experience with make-up sex the very day we reconciled."
        "What weighs upon my heart is his current condition."
        ha "It's n-not that. It's j-just…"
        "He seems to guess where this is going. Which is not surprising since we've had this kind of discussion before."
        hi "I've worked hard the last one and a half week to get back into shape. I did a light jog this morning without any troubles. My stamina's not at the point where it was prior to my accident just yet, but it's getting there. I'll probably be fine."
        ha "Did you… t-talk to the nurse?"
        hi "Not about this."
        "I let out a soft but still audible sigh. I can't say I blame him very much. I certainly wouldn't be able to do it. But Hisao's a lot more confident than I am, and he sees the nurse on an almost daily basis. But still…"
        hi "Look Hanako, I'm not gonna ask him if he feels I'm physically ready to start sleeping with you again. Because that feels to me like I'm asking him for permission to have sex with my girlfriend. And I bet he'd feel the same way."
        ha "How c-can you b-be sure?"
        hi "Because I know him. I'll have to spend months listening to his immature jokes."
        "He squeezes his eyes shut and contorts his face into a broad grin like the nurse's."
        hi "Just let me check your heartbeat, Hisao. If you're good, I'll give you a lollipop. Or a night with your girlfriend. Which one would you like best?"
        "I giggle. There's something bizarre about Hisao's impression."
        ha "I d-don't think…"
        hi "Hisao, guess what? I'm having a sale right now. Get one night between the sheets and you'll get a second one for free. Today only. What do you think?"

        "I press my hand to my mouth to hold back a laugh."
        ha "That's…hee hee…"
        hi "Yeah, when you're not the one being made fun of."
        "Realizing we're getting off track, Hisao gives me another peck on the lips and genly presses my chin up so I'm looking right into his eyes again."
        hi "Look Hanako, the nurse isn't going to stick around for the rest of my life, so in the end my own judgement will eventually be the thing I'll have to rely on."
        "That sounds a lot like what Nakamura told me earlier today… about not worrying about him too much."
        ha "Hisao… I… I've been s-startled once a-already today, b-but if you really think you'll b-be okay, I'll t-trust your judgement."

        "I can see Hisao think for a moment, weighing the odds of his heart acting up. I'm not really that frightened he'll die on me if we end up doing it, but after today, I don't think I'd take even a flutter very well. Hisao seems to pick up on my thoughts and gives a short nod."
        hi "Okay then, Hanako. We'll put it off for now."
        "I give him a quick kiss, feeling a bit guilty about getting cold feet, but also a bit relieved."
        hi "Can I stay here tonight?"
        ha "I'd really like that. We can still c-cuddle, if you like."
        hi "That sounds good."

        scene ev pillowtalk_placeholder_normal

        "I get off the bed, take off my clothes and then lie down and pull the covers up to my chin. Hisao follows my example, settles down next to me, grabs me in a tight hug and whispers in my ear."
        hi "I really missed this."
        ha "Me too."
        "We spend some time snuggling up against each other while exchanging sweet kisses. We keep this up for some time until Hisao takes my face in both his hands and presses a quick peck on the tip of my nose."
        hi "You know, I'm the one who has to take it easy, but I can still tend to you, Hanako."
        "He starts fondling my breasts and runs one finger up and down the front of my panties once."
        ha "Ah…"
        "Part of me would probably like that, but another part feels guilty about the idea of me having a good time without Hisao."
        "Ever since the first time we started our physical love life, we've done it on a strict give-and-take basis and even when we started having actual intercourse, we always tried to make certain that neither of us was missing out in any way."
        "Hisao seems to guess what I'm thinking."
        hi "Let's face facts, Hanako. You've had a trying day. Heck, you've had a trying week and tomorrow will be another day that'll probably push you way beyond your comfort zone."
        hi "Why not let me help you unwind a bit - get everything out of your system? I'd say you've earned it. Forget about the equal exchange thing for once."
        ha "Ummm… I-I think I'll b-be fine with c-cuddling."
        hi "You sure?"
        "I take some time to figure out how to reply."
        ha "I… want m-my first experience s-since we got back together to be a little bit special."
        hi "Special?"
        ha "Taking our t-time, s-sharing the experience, building things up gently and slowly…"
        hi "Like that night in the hotel?"
        ha "Yes, like that."
        hi "You want it to be a bit romantic?"
        "Something like that. I like romance. At least, I think I do. But since silences between us are still awkward, our dates have centered around doing things that don't leave many silences such as watching a movie or playing video games."
        "Fun, but not the most romantic way to spend time together. I'd argue that the most romantic moments we've shared are when we're together like this and we can communicate our affection for the other through cuddling, kisses and other non-verbal means."
        ha "Yes."
        hi "Okay then."
        "I snuggle up to him and give him one last kiss."
        ha "Good night, Hisao."
        hi "Good night, Hanako. Sleep well. We have a big day ahead of us tomorrow."
        stop music fadeout 3.0

        scene black
        with Dissolve(3.0)

        if _in_replay:
            return

    return