label sh_ch27:
    label .s1:

        $ set_window_tint(TINT_HANAKO)

        call sisterhood_timeskip

        scene bg satou_guestroom
        with Dissolve(2.0)

        play music music_serene fadein 4.0

        nvl clear
        nvl show dissolve

        n "I'm woken from my sleep by the sunlight coming from the small gap between the curtains and the momentary stirring of the person sharing the bed with me. Letting out a yawn and rubbing the sleep out of my eyes, my attention shifts to the sleeping form of my boyfriend whom I've been using as a human hug pillow over the course of the last few nights."
        n "{vspace=60}I cannot help but smile as I look upon his face. I was worried initially that with the combination of his jetlag and altered medication he was going to spend most of the nights wide awake, but after the first two nights he's been sleeping very peacefully. I carefully bring my face close to his until it's hovering mere centimeters above him."
        n "If he wakes up now I'll probably startle him, and he'll end up headbutting me."
        n "As I conclude that he's not going to wake up suddenly, I move in and carefully kiss the tip of his nose."
        n "{vspace=60}With some amusement, I notice that he reflexively sniffs with his nose a few times in response and I giggle at this cute sight."

        nvl clear

        n "I turn around and look at the clock resting on one of the dressers. It appears to be eight o' clock in the morning right now. Looks like it's still early."
        n "I guess I could stay in bed and wait until Hisao wakes up so we can pamper each other a bit. Then again, there's something I've been planning to do for a while, and I've been putting it off for several mornings."
        n "I don't think I should keep postponing it, so I slowly get out of bed, get my clothes off the nearby chair, make my way over to our private little bathroom, and take a quick shower."
        n "After drying myself off and finishing my daily ritual of stretching in order to get rid of my scarred areas' morning stiffness and putting moisturizer cream on them, I put on my clothes, take the photo camera out of my handbag, and quietly sneak out of the room."
        
        nvl hide dissolve

        scene bg satou_stairs
        with locationchange

        nvl clear
        nvl show dissolve

        n "We've been here in Scotland for a little over a week, and so far I can say I'm enjoying our stay immensely."
        n "{vspace=60}I decided to heed Karla's advice and start keeping a journal. I'm also aiming to take enough pictures to fill at least one of the memory cards Naomi gave me."
        n "One of the things I've wanted to take an ample amount of pictures of is the mansion we've been staying in to go with my diary, and I've been waiting for an opportunity to do so without being confronted by too many people."
        n "Early in the morning seems like a perfect time to do this."

        nvl hide dissolve

        "I can photograph our bedroom at any time I like, so I decide to start with the landing outside our room and work my way to the patio from there."

        play sound [ sfx_camerashutter, sfx_camerashutter ]

        "As I pass the door to Lilly's room, a thought occurs to me."
        "I'm not going to ask if I can enter the master bedroom, but maybe Lilly won't mind if I take some pictures of her room."

        scene bg satou_bathroom
        with locationchange

        play sound [ sfx_camerashutter, sfx_camerashutter, sfx_camerashutter ]

        "I take my time snapping pictures of the bathroom which, as Hisao mentioned to me on our first day, is traditional Japanese and looks quite a bit out of place in the western styled house."

        scene bg satou_livingroom
        with locationchange

        "I make my way downstairs to the cozy living room, making sure not to miss the cello case."

        play sound [ sfx_camerashutter, sfx_camerashutter ]

        "I take a mental note to ask Lilly if she can convince her mother to give us a demonstration of her musical talents one of the upcoming days."

        scene bg satou_kitchen
        with locationchange

        "I then proceed to the kitchen, which I believe is about as large as the kitchen at the orphanage, despite this mansion having only two permanent residents."

        scene bg satou_stairs
        with locationchange

        "I hesitate for a moment before entering the study."
        "Lilly's mother said it was okay for me to take pictures so it's not like I'll be violating any unwritten rules, but there's still something about the room that makes it feel vaguely off-limits."
        "According to Lilly's mother, this is where her husband spends most of his time whenever he's at home."

        stop music fadeout 2.0

        scene bg satou_study
        with locationchange

        queue music music_happiness fadein 4.0

        "The study itself feels very oriental and in some way vaguely reminds me of Miss Yumi's office."
        "The floor is covered with traditional rice straw mats and the room itself is very sparsely decorated with a low table surrounded by cushions in the middle and a few modest wooden cabinets occupying the corner."
        "Traditional Japanese shoji cover the windows, and one of the walls is decorated with several elegant wall scrolls containing carefully calligraphed kanji."
        "The other wall is what draws most of my attention as it's almost entirely covered by a large bookcase containing what look like hundreds of books."
        "Before I can aim my camera to take a picture of it, I'm startled by a cheerful voice behind me, and as I jump back and turn around in surprise, I can see a young woman in her twenties standing behind me."
        "I can't recall her name, but I know she's part of the cleaning staff here. The maid gives me a curious glance, probably not having expected my reaction, and then repeats her greeting while probably trying not to stare past my hairlock."
        "Maybe it's because she startled me and I didn't get the chance to carefully listen to her words, or maybe her accent is rather strong, but I can make neither heads nor tails of what she's saying, so I stammer out a reply."
        ha "{font=times}Ah... erm... E-excuse m-me? C-Could y-you repeat y-yours-self?{/font}"
        "The maid seems to have trouble picking up on what I'm saying. Would she consider it rude if I just get out of here?"
        mystery "She is wishing you a good morning and hopes you had a pleasant night's rest."
        "A calm voice interrupts my plans for a hasty escape attempt, and the next moment a tall figure appears in the doorway behind the maid, who quickly steps aside with a quick bow."

        show hiroyuki basic_neutral_suit
        with charaenter

        ha "Ah... umm... G-Good m-morning, M-Mister Satou."
        "I make a stiff bow, mostly out of instinct, to which he responds with a graceful bow of his own."
        hy "Good morning, Miss Ikezawa. I hope you do not mind if I repeat Miss Wilson's question."
        "Miss Wilson? Ah, the maid. I shyly nod in response."
        ha "I... ah... slept w-well. Thank you. H-Have you?"
        hy "Quite well, thank you."
        "He says something in English to the maid that I can't quite make out, but she smiles briefly, nods, and then gets to work dusting the table."
        hy "I apologize on behalf of Miss Wilson. She is originally from the countryside nearby, and her accent can be difficult to understand for those who are unaccustomed to the Highlands' dialect."
        ha "It's... okay."
        "Lilly's father walks into the room, waits for the maid to finish cleaning the table, puts the laptop he was carrying down and then turns to me."
        hy "Miss Ikezawa, I came here for the purpose of answering a few mails and verifying my schedule for today. Would it be a problem if I started addressing these matters? I am afraid I have a lot of work on my plate for today."
        ha "S-Should I leave?"
        hy "There is no need for you to. "
        ha "T-Thanks."

        hide hiroyuki
        with charaexit

        "I turn around and ready my camera to take a picture of the windows and the shoji in front of them, waiting for the maid to finish cleaning them and leave."
        "She suddenly seems to remember my presence again, looks me over, and giggles. She then strikes a pose and nods in my direction to indicate it's okay to take a picture."
        "A photo with a person in it, a maid no less, may actually be more interesting than just a picture of an empty room, so I raise the camera and press the shutter-release button on its top to take the picture."

        play sound sfx_camerashutter

        "She then walks over to another spot in the room and strikes another pose."

        play sound sfx_camerashutter

        "I chuckle to myself. She seems to enjoy acting as my model, so I take another picture, this time one of her pretending to dust the cabinets."
        "It looks like she's getting into it for this time she takes up position near the bookcase and next to Mister Satou."

        show hiroyuki basic_stern_suit
        with charaenter

        "Before I can aim the camera however, Lilly's father turns his head, gives her a stern look, and whispers something to her, causing her to look a bit sheepish before walking out of the room, giggling to herself as if enjoying some joke I wasn't let in on."

        show hiroyuki basic_smile_suit
        with chchange
        show hiroyuki basic_neutral_suit
        with charachangealways

        "Mister Satou watches her leave, a smirk appearing on his face for less than a second, and then his gaze turns stern again before refocussing on his laptop."
        "I'm not quite sure what to think of what just happened. Upon realizing I'm not immediately resuming my previous activities, Mister Satou's gaze briefly shifts to me."
        hy "I told her it may be better if she resumed her chores here at a later time. I will not pretend to know for certain what Miss Wilson found so amusing, but I have a slight suspicion."
        ha "Ummm... W-was it me?"

        show hiroyuki basic_thinking_suit
        with chchange

        "He thinks for a moment as if needing some time to rehearse his answer and then replies."
        hy "When I moved to Europe, I quickly learned that there are quite a few stereotypes about the Japanese circulating here."
        hy "I have been able at times to point out that many of those stereotypes are either exaggerations or blatant falsehoods."

        show hiroyuki basic_smile_suit
        with chchange

        hy "Heh, one of these stereotypes happens to involve the... ah... inseparability of Japanese tourists and their photo cameras."
        "I blush a bit. Looks I just came across as a walking stereotype, like an obese American tourist in a cowboy hat and Hawaiian shirt asking for directions in English to the nearest McDonalds."
        ha "I'm... s-sorry."
        hy "Think nothing of it."

        show hiroyuki basic_thinking_suit
        with chchange

        hy "{size=*0.7}Although I do hope she will at least still take my word for it that not all Japanese are covertly trained in ninjutsu during childhood.{/size}"
        "I didn't quite pick up what he just mumbled to himself. His voice was too low to hear it clearly."

        show hiroyuki basic_neutral_suit
        with chchange

        ha "E-Excuse me?"
        hy "If you need anything, please let me know."
        ha "O-Okay, thank you."
        "Lilly's father once again starts typing on his computer, and I take a moment to look him over."
        "Mister Satou is in many ways a sharp contrast with his wife. Appearance-wise, save for his above-average height, he looks just like the hundreds of salarymen you see every day around the city's train station."
        "Sporting silver-grey hair, bespectacled, and wearing a neat business suit, he is a dignified and extremely formal man in appearance, manners and speech."
        "He's about as tall as his wife and, although he's been very friendly in his interactions with us, there's nevertheless something stern about him."
        "His polite and reserved tone seems almost jarring compared to the up-beat personality possessed by his wife. And unlike Karla's energetic and fit appearance, Mister Satou comes across as though he hasn't slept in weeks."
        "Unless he always has bags under his eyes, I suspect he was merely being polite when he assured me he had a good night's rest."
        "From what I've learned this week, he's been under a lot of work-related stress lately. And despite that, he's been rapidly typing on his laptop throughout our entire conversation, his eyes barely ever leaving the screen."
        "I turn around and get into position to take a shot of the scrolls adorning the wall, trying to fit them all into frame."
        "As I do so, I let out a slight yawn that I quickly stifle with my hand upon remembering I'm not alone in the room."
        hy "Are you usually an early riser, Miss Ikezawa?"
        ha "Ummm... M-mostly. Earlier t-than Lilly."
        hy "Sleeping in has never been a habit in this family. Lilly seems to be the only one who occasionally has trouble getting out of bed in the morning."
        ha "I think... It m-makes s-some sense."

        show hiroyuki basic_raiseeyebrow_suit
        with chchange

        "Lilly's father gives me a slightly puzzled frown."
        hy "May I ask you to elaborate on that?"
        ha "Early in t-the morning... It's u-usually the s-sunlight that w-wakes me up. But Lilly..."

        show hiroyuki basic_thinking_suit
        with chchange

        hy "My daughter cannot see the sunlight and thus has only her biological clock to rely on. That certainly does make some sense. "

        hide hiroyuki
        with charaexit

        "I nod quietly and walk up to the bookcase. I initially intended to merely take a quick photo of it, but when I look a little closer, I notice something I hadn't picked up before."
        "I previously expected the books to be about management techniques or business practices, but a closer look reveals that the shelves are almost completely filled with Japanese fiction with only the occasional foreign title here and there."
        "My interest piqued immediately, I eagerly start skimming the shelves and it turns out there are many authors and titles in there that I recognize."

        show hiroyuki basic_neutral_suit
        with chchange

        hy "Do you approve of my collection, Miss Ikezawa?"
        "Mister Satou's voice drags me back to earth, and I realize with some embarassment I must have spent nearly 10 minutes checking the bookcase without saying a single word."
        ha "Umm... Are y-you a c-collector?"
        hy "What you see here is mostly a side effect of Inverness Library not really possessing any fiction in Japanese."
        hy "I do borrow novels written by English or American authors there, but whenever I wish to read something written by a Japanese author, I have a copy imported from Japan."
        hy "I prefer reading the original material over a translated copy."
        "I agree completely with that sentiment. It's nearly impossible to translate something and keep all the details and subtleties intact."
        "Unfortunately, my English isn't good enough yet to comfortably read complete novels in English as a relaxation and grasp all the details. Hopefully it will be one day. What a world that would open up to me."
        ha "It's very impressive."
        hy "Think nothing of it. Is there anything in there by an author that you like?"
        "I think for a moment."
        ha "Ummm... Is t-there anything by Haruki Murakami?"

        show hiroyuki basic_smile_suit
        with chchange

        "Mister Satou replies with a nod that seems part confirmation and part approval."
        hy "Near the lower left corner. I have most of his works with the exception of ‘Dance, Dance, Dance’, ‘Kafka on the Shore’ and ‘Pinball, 1973’. Do you have a favorite title?"
        ha "I... haven't r-read all his b-books yet, but I r-really liked ‘Dance, Dance, Dance’. It’s… one of m-my favorite titles."

        show hiroyuki basic_raiseeyebrow_suit
        with chchange

        hy "Would you recommend it?"
        ha "Ummm… Y-yes."

        show hiroyuki basic_thinking_suit
        with chchange

        hy "If you have not read it yet, and your tastes are anything like mine, you will probably like ‘Sputnik Sweetheart’ a lot. It happens to be one of my favorite titles."
        ha "I haven't read it yet. I will k-keep it in mind. I'm s-still in the middle of another book."

        show hiroyuki basic_neutral_suit
        with chchange

        hy "Do you mind if I ask what you're reading right now?"
        ha "The... ummm... ‘The Ark Sakura’."
        hy "By Kobo Abe? Have you read his work before?"
        ha "J-Just one piece aside from this. I f-found it... interesting."
        "Interesting and thought-provoking, but a bit depressing at times, though that's probably for personal reasons."
        "I wonder where Mister Satou is going with this conversation. I don't think he's trying to boast to me about his collection even though he'd have every right to brag in my eyes."
        hy "If you run out of books to read during your stay here, please feel free to borrow whatever you like here. There is no need to ask permission beforehand."
        hy "All I ask is that you return a book to the place where you found it after you are done with it."
        ha "Wow... R-really? T-Thank you."
        "Wow! There's enough reading material here to last a year! This vacation just keeps getting better and better!"
        hy "No need to thank me. It is the least I can do as a host."
        hy "Of course, now that you know this, please make certain not to spend all your time here reading. That would be a waste. "
        ha "We're going to... t-take a small boat trip near some p-peninsula today."

        show hiroyuki basic_raiseeyebrow_suit
        with chchange

        hy "Chanonry Point, I assume. A very nice area to visit if you enjoy watching wildlife."
        ha "Wildlife?"

        show hiroyuki basic_neutral_suit
        with chchange

        hy "I will not ruin the surprise, but you should take along a pair of binoculars before you leave. My wife owns a pair of them. Allison probably knows where they are. You should ask her."
        ha "T-Thanks."
        "Having finished taking pictures, I press the viewing button in order to see how the photos turned out."
        "Although the camera's tiny screen won't show a great amount of detail, I can see that the angles and lighting turned out alright. Satisfied, I put the camera away."
        ha "Umm... T-thanks for letting m-me t-take pictures."

        show hiroyuki basic_smile_suit
        with chchange

        "Lilly's father smiles for a moment and then gives me a curious glance."
        hy "If you do not mind me asking; are you interested in all the rooms in the house or merely those that stand out like a sore thumb?"
        "I blush a bit. I did pay the most attention to the bathroom and the study because of their sheer contrast to the rest of the house and now I feel found out."

        show hiroyuki basic_thinking_suit
        with chchange

        hy "You would not be the first visitor to take note of the considerable difference in style between the oriental rooms and the rest of the house. We get strange looks from any visitor who is given a tour here."
        hy "What can I say? I may have left Japan, but Japan has never truly left me."
        hy "I find that these little touches go a long way in easing the occasional pangs of homesickness. I try to spend my time here whenever I have reading or work to do."

        show hiroyuki basic_neutral_suit
        with chchange

        "He turns to me for a moment as if suddenly remembering something."
        hy "They do not have Japanese baths at Yamaku, do they?"
        "They don't. At least not in the dorms. We just have showers, though most of the showers have shower seats attached to the wall in order to accommodate students with mobility issues."
        "They do have a few baths in the nursing staff building that are used for therapy, but I've never used them."
        ha "N-No."

        show hiroyuki basic_stern_suit
        with chchange

        hy "You are free to use the bath while you are here. If you have not already done so, you should consider taking a soak some time. It is a great way to relax if you take the time for it—and have the time to spare."
        "The way he says it suggests that last part doesn't apply to him right now, and he's not particularly happy about it."
        ha "M-Maybe."
        "I think it's time for me to leave here and take a few shots of the patio and outside of the house. Maybe the nearby beach too."
        "Before I can think about saying goodbye, Lilly's father closes his laptop, gets up, and curtly bows to me."

        show hiroyuki basic_neutral_suit
        with chchange

        hy "I am afraid I will have to take my leave, Miss Ikezawa."
        "Taking his laptop under his arm, he heads towards the door and turns around to address me one last time."
        hy "It was good being able to speak Japanese for a little bit outside the business environment. My wife and I usually speak English here out of respect for the staff."

        show hiroyuki basic_smile_suit
        with chchange

        hy "I am also pleased to have had the opportunity to speak with the person who has been looking after my daughter. No doubt we will get the opportunity to speak some more when I am able to take some time off."
        hy "Please enjoy the rest of your day and goodbye for now."

        hide hiroyuki
        with charaexit

        "With that he turns around and exits the room, leaving me to digest what he just said."
        "How on earth should I have reacted to {i}that{/i}?"

        stop music fadeout 3.0

        scene black
        with Dissolve(3.0)

        if _in_replay:
            return

    return