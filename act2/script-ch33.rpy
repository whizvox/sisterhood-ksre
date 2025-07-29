label sh_ch33:
    label .s1:

        $ set_window_tint(TINT_HANAKO)

        scene bg akira_car
        with shorttimeskipsilent

        play music music_soothing fadein 4.0

        hi "Will you be the one seeing us off, or should we say our goodbyes right now?"
        "For a moment, it appears as if Akira didn't hear Hisao's question."
        aki "What? Oh, if possible I'll try to be at the airport when you guys leave. It was eight o' clock in the morning, right?"
        hi "That's right. We'll hope to see you tomorrow, then."
        "We get out of Akira's car and wait for her response."

        scene bg satou_entrance
        show akira basic_distant at tworight
        show hisao cross_speak_polo at twoleft
        with locationchange

        aki "Yeah..."
        hi "Is everything alright?"
        "Seems like Hisao also noticed Akira's voice trailing off. She's also been awfully quiet since we left the hospital after paying a visit to her father."

        show akira basic_sweet
        with chchange

        aki "Yeah, I'm alright. I was thinking it's probably not worth it to return to the office. Maybe I'll just go and get some fresh air. Take a little walk along the bay shore."

        show hisao cross_smile_polo
        with chchange

        hi "That sounds good."
        aki "I think I wouldn't mind a bit of company."

        show hisao cross_speak_polo
        with chchange

        hi "Do you want us to come with you?"
        aki "If it's okay, I'd like to borrow Hanako for a bit."
        "She turns to me."
        aki "You don't mind, do ya?"
        ha "M-me?"

        show hisao cross_neutral_polo
        with chchange

        "Hisao makes a face."
        hi "Just Hanako?"
        aki "Yup. Girl talk."

        show hisao cross_smile_polo
        with chchange

        hi "I didn't know you liked that."

        show akira basic_annoyed
        with chchangefast

        aki "Hey!"
        "Akira glares at Hisao and rolls her eyes."

        show akira basic_smile
        with chchange

        aki "From time to time."
        "I wonder if that's all there is to it. Akira obviously wants to talk about something with me in private. I'm just not sure what it could be."
        "I have to admit, it piques my curiosity a bit."
        ha "Ummm... Okay, I'll come with you."

        show hisao basic_neutral_polo
        with chchange

        "Hisao shrugs."
        hi "Guess I'll just go and continue packing our stuff in preparation for tomorrow."
        ha "Thanks."

        hide hisao
        hide akira
        with charaexit

        "As Hisao turns around and disappears into the house, Akira and I walk down the driveway, cross the road, and walk up to the shore."

        scene bg inverness_shore
        show akira basic_smile
        with locationchange

        play ambient sfx_waves volume 0.7 fadein 2.0

        "This area has slowly started becoming familiar terrain to me as well. The sound of the shore tends to put my mind at ease. Maybe the same is true for Akira."
        ha "You... like this place?"
        aki "When Lilly and I first visited here, I'd often take little walks along the shore whenever I didn't feel like hanging around the house."

        show akira basic_sweet
        with chchange

        aki "Most of the time alone, but sometimes Lilly would come with me, and we'd talk about... stuff. This place makes you relax, doesn't it?"
        ha "It does. I... used to come here daily to write in my journal."

        show akira basic_pleased
        with chchange

        aki "Right, Lilly mentioned that. But I'm picking up a past tense here. Did you stop writing?"
        ha "The last few days have been a bit... uneventful, and the one major thing that has happened is s-something I'd rather forget as soon as possible."

        show akira basic_sheepish
        with chchange

        "Akira gives me a playful grin."
        aki "That major thing you're trying to forget about involves you saving an old man from what was probably either death or existence as a vegetable. And from what I learned today, he seems awfully determined to not let ya forget about that, no matter how hard you're gonna try."
        ha "Do you... think he was serious?"

        show akira basic_ending
        with chchange

        aki "Oh yeah, definitely. In fact, I was secretly hoping you'd ask for something like half of the family fortune or something equally outragous. You know, just to see how far you could stretch that gratitude of his."
        ha "I don't want that sort of thing."

        show akira basic_smile
        with chchange

        aki "Hmmm?"
        ha "I read a book once, about a man who won the lottery. And suddenly... everyone wanted to be his friend. He didn't even know who his real friends were anymore, because everyone just seemed to want to take advantage of his newfound wealth."
        ha "I... would hate for something like that to happen to me. It w-would... drive me crazy."
        aki "Well, it's true that as convenient as it is, money can't buy you happiness. I speak from experience. Still, maybe you can think of something."

        show akira basic_smug
        with chchange

        aki "Heh, if you don't want the old man to keep stalking you for the rest of your life, that is."
        ha "Uhhhh..."
        aki "Relax, I was only joking. Still, I doubt this is the last you'll hear about this. Dad's got this old-fashioned ‘you saved my life, so now it belongs to you forevermore’-type of samurai mindset going."
        "Akira's exaggerated eyerolling makes me giggle a bit."
        ha "It's actually a rather... romantic mindset, don't you think?"

        show akira basic_resigned
        with chchange

        aki "Only if you ignore the secondary implications of that kinda mindset."
        ha "Secondary implications?"

        show akira basic_annoyed
        with chchange

        aki "Since a child owes her life to her parents, she's obliged to show livelong respect and reverence to them no matter how badly they deserve the opposite. No doubt Dad sincerely believes that. Heck, he couldn't resist rubbing it in my face during your visit."
        "I think I remember what she's talking about."
        ha "So... that's what he meant."
        
        show akira at twoleft
        with { "master": charamovefast }

        "Akira bends down and picks up a few smooth stones."
        "She flicks one away, and I see it bounce along the water surface several times before it sinks."

        play sound sfx_rockskip

        "{i}*splash* *splash* *splash*{/i}"

        show akira basic_sad at twoleft
        with chchange

        aki "I must be coming across as very petty, complaining so much about my parents to a person who no longer has her own."
        "I cringe a bit. Even after all this time, Akira's statement of the obvious still hurts inside."
        ha "It's o-okay."

        show akira basic_distant
        with chchange

        aki "Ya know... Hisao probably had a point when we were at the hospital. I wouldn't blame you if you agreed with him."
        "It comes across as weird for the usually up-beat and assertive Akira to suddenly sound this way."
        ha "I'm not s-sure. M-maybe, but you... probably have your reasons."
        "Akira nods absentmindedly and flings another stone along the surface before sitting down on a large rock near the shore."

        play sound sfx_rockskip

        "{i}*splash* *splash* *splash*{/i}"

        stop music fadeout 2.0
        queue music music_night fadein 4.0

        show akira basic_resigned
        with chchange

        aki "You know, this has been a very weird time for me. Over the last six years, I can't say my life's been very easy, but it was fairly stable at least."
        aki "After Mom and Dad left and our grandparents moved to a place more suitable for Granddad's dwindling health, I ended up concentrating completely on both my job and looking after Lilly. Nothing else mattered."
        aki "Eventually, I ended up cutting both Mom and Dad out of my thoughts for the most part. Aside from the money that was wired to our account on a monthly basis and the increasingly rare phone calls, I started feeling like they didn't really exist anymore."

        show akira basic_lost
        with chchange

        aki "I considered the matter dead and buried. It was easier this way."
        "She absentmindedly tosses one of the stones in her hand in the air and then catches it again."

        show akira basic_depressed
        with chchange

        aki "What I've learned over the last couple of weeks was that the matter may have been buried, but it was far from dead."
        aki "After six long years, Mom and Dad were suddenly part of my daily life again and acting like nothing friggin happened. As you can see, I haven't been dealing with that very well... at all."
        "She gives me a guilty look as I sit down next to her."
        aki "When I told you guys in the hospital that I simply screwed up, that was the truth. I didn't really mean to start a fight with the old man when he was in such a sorry state, but... well... it simply happened anyway."

        show akira basic_lost
        with chchange

        aki "I guess that... there are a lot of buried grievances suddenly clawing their way back to the surface."
        ha "Like... them l-leaving."
        aki "Uh-huh..."
        "She sighs."

        show akira basic_ponder
        with chchange

        aki "To be completely honest, it's not just bad memories I have of them. There's been a few good ones, too."
        aki "Like the annual New Year, when our parents, our grandparents, Lilly, and I would visit a shrine to pray for good luck the upcoming year and play games afterwards. Also, our trips to the summer house..."
        ha "The one we visited?"
        aki "It was a different one back then, but in the same area. The three—and later the four—of us would go there from time to time, and that was also the place where Lilly and I'd get in touch with the British part of our heritage."

        show akira basic_wistful
        with chchange

        aki "Our own home was kind of traditional, but the summer house was more like... Well, the residences here in the UK. We'd speak English all the time, eat with cutlery instead of chopsticks, and Mom would read us Scottish folk tales or parables as bedtime stories."
        aki "It was also like... that intangible pressure I often felt didn't exist there. The atmosphere was simply different. Dad, and especially Mom, seemed different."

        show akira basic_sad
        with chchange

        aki "Of course, things'd revert to normal the moment we got in the car, but I still have good memories of those times, even though they became more and more rare as Dad advanced up the corporate ladder."
        ha "...pressure?"

        show akira basic_angry
        with chchange

        aki "Before our parents allowed me to make my own barber appointments, I used to have slightly longer hair. Other than that though, I've always been the way I am now."
        aki "In other words, a long shot away from the kind of person the daughter of an upstanding family is supposed to be."
        ha "Your p-parents d-disapproved of who y-you were?"

        show akira basic_resigned
        with chchange

        aki "It's always been kind of subtle. It's not like they weren't nice to me, but there was often that subtle undertone of sadness like they were expecting me to be more... I dunno... elegant... lady-like... the whole shebang."

        show akira basic_lost
        with chchange

        aki "For a long time I felt like they expected something of me, but I didn't know exactly what that something was."
        aki "I found out eventually what that was as Lilly grew up. I think in the end, Mom and Dad always rued the fact that I couldn't be more like Lilly."
        "I get an uneasy feeling in my stomach as I attempt to determine if there's any bitterness in Akira's words."
        "If she felt like she lived in Lilly's shadow, how does she feel about her sister?"
        ha "Uhhh... H-how d-do you feel about Lilly?"

        show akira basic_wistful
        with chchange

        "Akira sees the distressed look on my face and lets out a reassuring chuckle."
        aki "I guess lots of people would grow to secretly resent their sibling in that case, wouldn't they? Interestingly enough, that never happened with me."
        aki "Besides, it's not like Lilly was the perfect daughter to Mom and Dad, or they wouldn't have left her behind six years ago."

        play sound sfx_rockskip

        "{i}*splash* *splash* *splash* *splash*{/i}"

        show akira basic_distant
        with chchange

        aki "I think the reason we've always been so close is due to the fact I often spent time looking after Lilly, even when our parents still lived in Japan."
        aki "Mom often asked me to keep an eye on my sister. And there was the fact that, while I've often felt a bit like an outsider even in my own family, Lilly was nevertheless always unconditionally accepting of me."
        
        play sound sfx_rockskip

        "{i}*splash* *splash* *splash*{/i}"

        show akira basic_sad
        with chchange

        aki "Probably one of the very few I can say that about."

        play sound sfx_rockskip

        "{i}*splash* *splash* *splash*{/i}"

        show akira basic_pleased
        with chchange

        aki "She was also a really cute kid when she was younger. If I'd show you a picture of her when she was like three, you'd probably develop a girl-crush on her in an instant."

        play sound sfx_rockskip

        "{i}*splash* *splash*{/i}"

        show akira basic_sweet
        with chchange

        aki "Heh."
        "Akira's light-hearted remark about toddler-Lilly's cuteness was probably meant to lighten the mood, but it doesn't draw my attention away from the rest of her words, especially since this is a sensitive issue for me, myself."
        "Didn't Akira make school friends or something? She's pretty sociable, if a bit rough. I always imagined her to have lots of friends, like Lilly."
        ha "Uh... Akira... H-how about y-your school days?"

        play sound sfx_rockskip

        "{i}*splash* *splash* *splash* *splash*{/i}"

        show akira basic_sheepish
        with chchange

        aki "Elementary school was... I think mixed is the right word. Heh, get it?"
        ha "Uh... N-no."
        aki "Sorry, didn't have time to make up a better punchline. Anyway, in the same way I've always been a bit of an outsider in the family, I've also been a bit of an outsider at school."
        ha "Outsider?"

        show akira basic_distant
        with chchange

        aki "When I started attending elementary school, I quickly discovered that I was the only kid in the school with a biracial background. I found that there were few convenient things about standing out in a crowd like that, but several downsides."
        aki "Some of the reactions I'd get were amusing in a stupid way. Like others asking me how on earth I was able to speak Japanese or being amazed that my blood was red like theirs instead of yellow. Other times, less funny things happened..."
        ha "You were... b-b-bullied?"

        show akira basic_annoyed
        with chchange

        aki "Picked on, from time to time. I mean, I looked pretty different from the rest, so I naturally attracted attention from all sorts of kids."

        show akira basic_angry
        with chchange

        aki "Now, before you start worrying about me, let me say that I've always been pretty strong for my size, and back in elementary school, I could even take on many of the boys."
        aki "Bullies don't like running the risk of a black eye when they pull their crap. So, all in all, things hardly ever truly escalated since I wasn't an easy target."
        ha "That's... g-good."
        "I'm happy for Akira she that was able to stand up for herself like that, though it also makes me feel inadequate myself. I was never able to stand up for myself."

        show akira basic_sweet
        with chchange

        "Akira takes a brief look at me and seems to guess my thoughts. A sympathetic expression appears on her face."
        aki "No such luck for you, huh?"
        "I meekly shake my head."
        "When I was finally released from the hospital, I was still learning how to use my right arm for even basic stuff like lifting and opening a lunchbox."
        "In addition, my scars and the pressure garments I was forced to wear day and night for the first few years made my movements stiff and awkward. Any physical confrontation, even with kids younger than me, would have been over within seconds."

        show akira basic_wistful
        with chchange

        aki "Figures. I think from the moment I first met you there was something in your eyes and body language that told me you were given a hard time at school."
        "I'm not sure how to respond to that, so I merely nod my head."

        show akira basic_wistful_close at center
        with characlose

        "Suddenly, my depressing train of thought is interrupted by a hand on my shoulder."

        show akira basic_sweet_close
        with chchange

        ha "Ya know... uh... Even though Lilly's usually the one to do this kind of thing, I just wanted to tell you that if you ever wanna talk to someone about this sort of thing, I'm there as well. Don't be a stranger."
        "Akira puts on a slightly awkward but sincere smile on, and I can't resist smiling back for a moment."
        "I'm not sure if I'd ever accept Akira's offer, but her gesture of emotional support nevertheless feels extremely good to me."
        ha "T-thank you."
        "After confirming that my mood has cleared a bit, Akira continues."

        show akira basic_sweet at twoleft
        with chchange

        aki "Anyway, I can't say my elementary school time was smooth surfin', but aside from the occasional incident every now and then, I was okay. I was still able to hang out with other kids from time to time, though I didn't really make any deep friendships."
        aki "Then again, a lot of friendships in that time are kinda shallow, anyway. I mean, kids in that phase of their lives often become friends simply because they sit next to each other in class or wear the same color ribbon in their hair, not because their personalities are extremely compatible."
        ha "Ummm... Akira?"
        aki "Yeah?"
        ha "Uh... D-did Lilly ever... get... picked on?"

        show akira basic_smile
        with chchange

        aki "I was really worried about that myself when she started attending school, but I don't think that ever happened, and thank heavens for that."
        aki "Due to her blindness, teachers were always keeping a close eye on her, and two random students from her class were picked every day to help her out with... whatever she couldn't do herself."

        show akira basic_resigned
        with chchange

        aki "Sometimes I felt weird about that arrangement, almost as if Lilly was the class pet instead of a classmate, but in practice, it probably meant she wasn't an easy target for bullies since she was hardly ever unsupervised."
        aki "I also think... well... most students eventually forgot about it."
        ha "Forgot?"

        show akira basic_distant
        with chchange

        aki "You know what the funny thing is about the labels we human beings tend to stick on others? We usually pick one label and run with it, ignoring everything else about a person."
        aki "In this case, I think people were so focussed on the very obvious fact that Lilly was blind, they quickly forgot that she was half-foreign. It's weird, but I think it played a role."
        "I wonder what label ended up sticking in people's minds for me: the one about my burn scars or my disfunctional behavior?"
        aki "Anyway, by the time I was about to leave elementary school, I wasn't having that many conflicts anymore, and I was keeping my fingers crossed that things wouldn't get difficult once I'd get into middle school. Turns out I was right to worry."
        ha "You... went to the same school as Lilly, d-didn't you?"

        show akira basic_angry
        with chchange

        aki "Yeah. It was expensive, prestigious, all-girls, and hella strict. The worst place to be for someone like me in other words."
        aki "I spent a large part of elementary school playing mostly with boys. Lots of stuff people thought of as typical girl-stuff didn't really interest me. When I was suddenly thrown into Princess U, it wasn't just my mixed blood that made me stand out, but everything else about me, as well."
        aki "I was suddenly having run-ins with obnoxious fellow-students and teachers alike left and right. Less than three weeks into the first year, I was already firmly stuck into the pariah role. Those were some very lonely and miserable three years, let me tell ya."
        "Looks like I wasn't the only one whose middle school time was hard."
        ha "Didn't you t-tell your parents how you f-felt?"

        show akira basic_pissed
        with chchange

        aki "Surely you don't think they tossed me into a friggin' Japanese wife factory by accident? They were probably simply tired of relying on subtle correction attempts all the time, so they tried a more drastic method of molding me into a better daughter."
        aki "Of course I told them that I hated it there, but all they said was to please hang in there and keep going. Dad even had the audacity to suggest that this was in my best interests and that I'd be grateful one day."
        aki "It's been about ten years since I was released from that hellhole, and so far, I haven't had any sudden epiphanies of gratitude."
        "It's a little frightening how bitter Akira sounds, but there's one thing that scares me more than her tone."
        ha "Ummm... J-Japanese wife factory? D-does that m-mean that Lilly...?"

        show akira basic_lost
        with chchange

        "Akira's expression turns genuinely remorseful."
        aki "Sorry, I kind of went overboard with my venting. I didn't mean to imply anything about Lilly. To reassure you, middle school gave Lilly an additional layer of classy manners, but underneath, she's still the same person she's always been."
        aki "I still wouldn't have sent her there myself, but I'm relieved that she doesn't have the same horrid memories I have of that place."
        
        play sound sfx_rockskip

        "{i}*splash* *splash* *splash* *splash*{/i}"

        show akira basic_sad
        with chchange

        aki "Well, as you can see things between me and the folks weren't exactly peachy even before they left Japan, but things might have worked out if they hadn't upped and left just like that."
        ha "You were... 19 when they left, right?"
        aki "Yeah. It was after I graduated from high school, which was fortunately not the same kind of place middle school was. I didn't really know what I wanted to do afterwards."
        aki "Dad pulled a string or two at the company, and I was allowed to work at the legal department of SMT as a secretary. Back then, there were apparently already office rumors about a big change being in the wings."
        ha "Your parents moving?"

        show akira basic_distant
        with chchange

        aki "It was a little more complicated than that. Back then, Granddad was still in charge of the company, though he was ill during the last months before the big change. Eventually, Granddad revealed his plans for the company's future at the dinner table."
        aki "He and his brothers on the board of directors wanted to expand our clientele, but we weren't having a lot of success getting a foot in the door in China."
        aki "Business was booming in Inverness though, and the people there were doing a good job getting the European mainland to warm up to our brand."
        aki "So the board made the decision to make Inverness the new headquarters and have the Japanese branch concentrate completely on the domestic market from that point on."
        aki "Of course, a Satou had to be in charge of headquarters, and that's how Dad finally got his promotion to number one executive of the company."

        show akira basic_angry
        with chchange

        aki "A promotion and a plane ticket. He immediately accepted the offer, too. He said he was honored by the responsibility placed on him."
        aki "I wonder if he even considered how Lilly must have felt. I remember everybody applauding. I wondered even back then how many of those ovations were actually real."

        play sound sfx_rockskip

        "{i}*splash* *splash* *splash*{/i}"
        aki "The actual shocker came during his visit to Japan a few weeks after moving to Inverness. It turned out that he was going to live there permanently, and he mentioned Mom's help being needed in Scotland and that she'd need to come along with him for some time."

        show akira basic_pissed
        with chchange

        aki "The board apparently already approved. Hah, ‘for some time’ being a euphemism for forever."
        aki "The true bombshell was when we were told that Lilly had to stay behind. For her education, so to speak. She was gonna lose her parents for a friggin' education. At least, that was the story."
        
        play sound sfx_rocksplash

        "{i}*SPLOOSH*{/i}"
        "I'm startled by an unusually loud splash. That must have been quite a rock she just threw."
        ha "You still don't believe it?"

        show akira basic_annoyed
        with chchange

        aki "I'm not sure what to make of Dad's reaction, but one thing I know for sure is that there are also prestigious private schools in the UK. I don't think the quality of her education was a good argument to leave her in Japan."
        aki "Heck, and judging from what the old man said the other day, he wasn't even expecting Lilly to get a job anyway, even with that education."

        show akira basic_resigned
        with chchange

        "She shrugs and gives me a sad look."
        aki "Ya know, I always thought there was something creepy about Yamaku, or rather the idea behind it. It's like this place in the middle of nowhere so ‘proper society’ doesn't have to see or hear those attending there."
        aki "I still wonder if Mom and Dad didn't rue the fact that Lilly couldn't be shoved there until she finished middle school."
        ha "I... actually like that about Yamaku. M-middle school was h-hard for me. I'm n-not sure w-what would have happened at an ordinary high school. M-maybe something terrible."
        ha "I... didn't function all that well at Yamaku, but at least I wasn't b-bullied anymore. I'm... r-really thankful for that."

        show akira basic_sad
        with chchange

        "Akira thinks for a moment."
        aki "I never really thought much about that. I guess it's a good point, though it didn't apply to Lilly."
        "I don't really have an answer to that, so I decide to shift the conversation to the earlier subject."
        ha "A-anyway, after your parents left... you... decided to look after her?"

        show akira basic_resigned
        with chchange

        aki "Either I stayed with her or she'd be left with an ailing grandmother and grandfather. Shizune's family wasn't an option. Dad and Shizune's Dad hate each other. He wouldn't have permitted it."
        ha "W-what are y-your grandparents like?"

        show akira basic_distant
        with chchange

        aki "To be honest, I never really knew Granddad. He was at work even more often than Dad was. Of course, he ranked higher than Dad. On Sundays he'd be out golfing with business pals or reading in his study."
        aki "The rest of the days he was at work or hanging out with co-workers. The company was his life as well since he stayed at its helm for a very long time, even though he could have retired years earlier."
        aki "He even considered it a few years earlier, before ultimately reconsidering. He was a pretty heavy smoker, and it came back to bite him six years ago when he developed lung cancer."
        aki "He was lucky they discovered it before it spread, but they still ended up removing a part of his right lung and with it an equally large part of his stamina."
        aki "Grandpa and Grandma used to live in the same neighborhood as ours in a house on a rather large incline with stone steps leading up to the front door."
        aki "After his surgery, it'd take him half an hour just to reach his own porch. Even Lilly could run circles around him at that point. So he and Grandma moved to another town, and we haven't had much contact with them ever since."
        
        play sound sfx_rockskip

        "{i}*splash* *splash* *splash*{/i}"

        show akira basic_resigned
        with chchange

        aki "As for Grandma, when I was a child she'd drop by our home on a daily basis. She was nice enough. She was formal, polite, proper, and friendly, but also a bit distant and stoic."
        aki "She was more responsible than Mom, though. She'd always be the one to take me to the park to play when I was a kid. She was also the one who went to PTA meetings during Lilly's elementary school years instead of Mom."
        aki "Heh, somehow Mom always managed to come up with a reason to be busy with something else."

        show akira basic_sad
        with chchange

        aki "Thinking back on it, it's possible she was already going her own way even then, just on a smaller scale. Although, ironically, she didn't really get out of the house much back then. I remember Grandma scolding her about it a few times."
        aki "Heh, of course when I asked Grandma about that, I got a major scolding myself about how impolite it is to listen in. She was pretty strict, all in all."
        "Akira toys with one of her locks of hair for a moment."
        aki "Save for a few bad periods once in a while, Grandma's always been in pretty good health, but after Granddad's surgery, her physical condition took a nosedive as well. High blood pressure, ulcers, shortness of breath."
        aki "I guess his condition hit her harder than any of us expected. Between her declining health and the fallout of grandpa's surgery, I didn't feel it was responsible to leave Lilly in their care."

        show akira basic_lost
        with chchange

        aki "Of course, it's not like I was really all that more fit as a caretaker..."
        ha "I think Lilly would disagree. You did a r-really good job l-looking after her while..."
        "I pause for a moment."
        "If Akira left for a job right after high school, when did she earn her law degree?"

        show akira basic_smile
        with chchange

        "Akira seems to read my mind as I trail off and smirks."
        aki "You're wondering how I became a lawyer without visiting a university, right?"
        "I nod."
        aki "Before 2004, becoming a lawyer in Japan didn't require a university degree. All you had to do was pass the official bar exam, which... heh... had a 3%% passage rate at the time."

        show akira basic_cheerful
        with chchange

        aki "While at work, I heard a couple of guys at our department going on about taking a shot at it. It gave me the idea to give it a try myself, which was naturally met with ridicule."
        aki "But I figured that if I could pass it, I'd be able to get a career without having to attend some university located somewhere far away from my home and my sister."
        ha "You p-passed such a difficult exam without having attended a university?"
        "Just how much of a genius is Akira if she pulled that off?"
        aki "Without a university, but not without preparation. There are cram schools that specialize in preparing people for that particular exam. I attended one before taking the exam."

        show akira basic_depressed
        with chchange

        "A sad and slightly guilty look appears on Akira's face."
        aki "I didn't think Dad was going to sponsor an attempt like that, so Lilly suggested letting go of our housekeeping staff and using the money Mom and Dad wired us every month to employ them to get me into one of those cram schools."
        aki "She was already a lot more independent at the time, but I still had a bad feeling about it."

        show akira basic_angry
        with chchange

        aki "Eventually, she managed to convince me to give it a try, and I gave in after swearing a solemn oath to her that if things became too much for her, I'd drop everything immediately and we'd go right back to the way things were."

        show akira basic_smug
        with chchange

        aki "I ended up passing the bar exam on the first try, apparently being one of the few ones who pulled that off."
        ha "W-wow..."

        show akira basic_sweet
        with chchange

        aki "In order to officially practice as a lawyer, I would have had to spent over a year training at the Supreme Court's training center in Tokyo, but since that involved leaving Lilly behind, I passed on that."
        aki "Practically speaking, it wasn't a big loss since they focus almost completely on litigation training there anyway, and hardly spend any time on contract drafting and other corporate practices."
        aki "I could do my job as a corporate lawyer even without it. Officially, it did mean I probably wouldn't be able to do my job at any place other than the family company."
        aki "Still, I promised myself to spend all the free time I had with Lilly if I passed the bar exam, and I did my best to keep it. She was the one who was rooting for me and making sacrifices for me that entire time. It was the least I could do for her."
        ha "I've... always been a b-bit envious of how c-close you and Lilly are."

        show akira basic_wistful
        with chchange

        aki "I suppose that with our parents out of the picture, we were the only true constants in each other's lives for a long time. That creates a bond."

        show akira basic_lost
        with chchange

        aki "But bonds have to be maintained, too. And right now, I can't shake the feeling that our bond used to be in a better condition than it is now..."

        play sound sfx_rockskip

        "{i}*splash* *splash* *splash* *splash* *splash* *splash*{/i}"
        "I'm distracted for a moment by a particularly skillful throw on Akira's part, and it takes me several seconds to digest what she just said."
        ha "W-wait! What?"

        show akira basic_cheerful_close at center
        with characlose

        "Akira doesn't immediately respond and merely puts a few flat stones in my hand."
        aki "Go ahead and have a try yourself. It's not that difficult when you get a feeling for it."
        
        play sound sfx_rockskip_fail

        "{i}*splash*{/i}"
        "“Not that difficult” is probably still pretty subjective."

        play sound sfx_rockskip_fail

        "{i}*splash*{/i}"
        aki "You gotta throw sideways a bit. Make them spin like a discus. As long as they keep spinning, they keep bouncing."

        play sound sfx_rockskip_fail

        "{i}*splash*{/i}"

        show akira basic_smile_close
        with chchange

        aki "Maybe you ought to try using your left hand instead of your right."
        "That might work. My left wrist is a lot more supple than my right."

        play sound sfx_rockskip

        "{i}*splash* *splash*{/i}"

        show akira basic_laugh_close
        with chchange

        aki "See?"

        play sound sfx_rockskip_fail

        "{i}*splash*{/i}"

        show akira basic_smile_close
        with chchange

        "I sigh in frustration. This is still harder than Akira made it out to be."

        play sound sfx_rockskip

        "{i}*splash* *splash*{/i}"
        ha "Ummm... W-why do you think that your bond with Lilly is... in worse condition?"

        show akira basic_distant
        with charadistant

        stop music fadeout 2.0

        pause 1.0

        show akira basic_resigned
        with charachangealways

        "Akira merely looks at some point in the distance before turning to me with a sad look in her eyes."

        queue music music_moonlight fadein 4.0

        aki "It's not just Dad Lilly's been keeping at arms' length over the last two days."
        ha "H-how can you be so sure?"

        show akira basic_lost
        with chchange

        aki "The way we parted after our last visit to the hospital gave me that idea already, and the fact that she's neither answered nor returned any of my phone calls merely reinforces my hunch."
        aki "I probably screwed up one too many times. I've been screwing up ever since Lilly and I first came here."
        ha "B-but..."
        "I start denying Akira's suggestion, but she stops me with a gesture that indicates she has more to say."

        show akira basic_resigned
        with chchange

        aki "Ya know, I've been thinking a little bit. Back when I learned that Lilly didn't want to migrate to Scotland after all and that she came this close to going there against her will, I was upset with her for not letting me in on how she really felt."
        aki "Lilly's rather reserved by nature, but she and I have had very few secrets between us since we started living together without our parents. I was shocked that she kept me out of something this major."
        aki "When I confronted her with this, she merely apologized, so I dropped it without pressing her for the reason."
        aki "I... think I know the reason now."
        ha "You do?"

        show akira basic_lost
        with chchange

        aki "Back when it was just the two of us, I'd occasionally vent my frustration with our parents in front of Lilly. She'd never argue with me or defend them. She'd just sit there nodding her head. No nods of agreement, but simply of acknowledgement."
        aki "This was the one area we never shared a wavelength on. Most of the time, it didn't matter. Until our folks entered our life again. Then it suddenly became a huge deal."

        show akira basic_depressed
        with chchange

        aki "I hate to admit it, but I think the truth is that Lilly simply kept me out of the loop because she didn't think my input could be trusted."
        ha "..."
        "Even though Akira's words are harsh, I can't bring myself to deny them, either."
        "I've witnessed Akira's bitterness towards her parents, and based on what she just told me, she's probably justified to feel that way."
        "Still, her bitterness has made me very uncomfortable recently. Perhaps it's because I've had quite a few bouts of cynicism myself, and Akira has felt like a reflection of myself at times. It didn't make me feel very good."

        show akira basic_distant
        with chchange

        aki "I'm not particularly worried about my long-term relationship with my sister. This situation will end in one way or the other, and when it's over, I don’t doubt that she'll let me back in."
        aki "In the meantime, the best thing I can probably do is keep my mouth shut in her presence whenever the subject of our parents comes up, so I don't end up making things worse anymore."
        "I meekly nod."

        show akira basic_sad
        with chchange

        aki "Still, the rut Lilly's currently in is about our parents, and I hate the fact that I can't do anything to offer her emotional support like I'm supposed to. She won't talk to me about this, but she might confide in someone else."

        show akira basic_wistful
        with chchange

        aki "Someone who isn't blood-related to her, yet with whom she feels a strong bond."
        "Akira gives me an expectant look to remove any doubt about what person she's talking about."
        ha "M-me?"

        show akira basic_pleased
        with chchange

        aki "Who else?"
        ha "Hisao and I... already visited Lilly in her room a few times, but all s-she does is make small talk."

        show akira basic_ponder
        with chchange

        aki "Your boyfriend's a good friend to Lilly, but you're the one she probably trusts most. Maybe if you spend some time with her alone..."
        ha "Then what...?"

        show akira basic_sheepish
        with chchange

        "Akira smiles awkwardly."
        aki "Dunno."
        ha "I... don't really understand what you want me to do."

        show akira basic_ponder
        with chchange

        aki "If I knew what had to be done to sort out this whole mess and make Lilly happy again, I'd tell you. But I'm not so sure myself."

        show akira basic_resigned
        with chchange

        aki "Maybe you could spend a little bit of time with her before you leave tomorrow. Just you and her. Maybe cheer her up a little. Get her to stop moping in that room of hers."
        aki "Would you be willing to do that for me?"
        ha "I... uh... Okay. I was... already hoping to t-talk to her a little before we go tomorrow."

        show akira basic_sweet
        with chchange

        "Akira smiles broadly."
        aki "Thanks. That means a lot."
        "I shyly shake my head."
        ha "It... might not m-make much of a difference."

        show akira basic_ending
        with chchange

        "Akira grins in response."
        aki "You shouldn't sell yourself short like that. The last time you had a candid talk with Lilly, she reversed a life-changing decision just like that. That's no small feat. And just today, you got some impressive results with the old man, too."
        ha "W-what?"
        aki "You told him how wrong he was about Lilly and also suggested for him to apologize to her, all of that without being so direct as to cause him to get butthurt."
        # TODO probably should add an internal line of dialogue about hanako being unsure about Akira's words

        show akira basic_sweet
        with chchange

        aki "Hey, don't give me that look. It was pretty easy to pick up if you read between the lines a bit. I don't think Dad missed it either. He said he'd think about it. That's much more of result than anything I've been able to get done."
        ha "I... just w-wanted to make Lilly happy."

        show akira basic_lost
        with chchange

        aki "And I guess you think that reconnecting with Mom and Dad in some way will make Lilly happy, or you wouldn't have asked our old man to apologize. Do you still feel this way, even knowing everything I just told you?"
        ha "I'm... n-not sure. I... think... so. When I... met them, they seemed... not so bad. They still seem to care about Lilly. Maybe... it's possible for... someone to be a bad parent... but not a bad person."

        show akira basic_resigned
        with chchange

        aki "You think so?"
        ha "Besides... n-not having p-parents at all... is still worse, I think."
        "Akira gives me a sympathetic look."

        show akira basic_wistful
        with chchange

        aki "I'd feel like a real bitch arguing against that with you."
        "She gets up to indicate she's ready to start walking back."

        hide akira
        with charaexit

        "We walk side by side along the beach until we get back to the Satou home's driveway."

        stop ambient fadeout 2.0

        scene bg satou_entrance
        show akira basic_ponder at tworight
        with locationchange

        "Ever since we started walking, Akira's had a pensive look on her face, and she hasn't said a single word the entire time."
        "It isn't until we reach her car and I get ready to go back inside that she turns to me."

        show akira basic_resigned
        with chchange

        aki "Hey, Hanako?"
        ha "Yes?"

        show akira basic_peaceful
        with chchange

        aki "Maybe... well... You should try and convince Lilly to do one more patching up attempt."
        aki "Who knows? It might just work out."

        stop music fadeout 3.0

        scene black
        with endchapter

        if _in_replay:
            return

    return