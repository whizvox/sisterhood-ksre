label sh_ch11:
    label .s1:

        $ set_window_tint(TINT_HANAKO)

        call sisterhood_timeskip

        play ambient sfx_carsambient fadein 2.0
        play sound sfx_crowd_outdoors loop fadein 2.0
        play music music_pearly fadein 2.0

        scene bg city_street2_ni
        show lilly basic_oops_cas_close
        with locationskip

        ha "C-could you let me check the directions one more time?"
        li "I don't think there's any need to hurry. I'm sure they'll have a table for us even if we don't show up exactly on time."
        "Lilly must have sensed the hint of frustration in my voice. She has a point of course, but I don't want to risk them giving our reserved table to someone else."
        "I take another look at the small map I printed out and try to pinpoint our current location."
        "My orientation skills aren't particularly bad. In fact, they're probably better than my boyfriend's, but walking through an unfamiliar (and {i}crowded{/i}) part of the city keeping a keen eye on the surroundings while keeping my head down to avoid people's gazes has proven to be tough."
        "The fact that I'm holding onto Lilly, both for her benefit and my own assurance, and the fact that Lilly tends to attract people's attention due to her height and hair color aren't making things easier."
        ha "I… I think I have our location. We n-need to take the s-street we just passed and it should be to the right somewhere."

        show lilly basic_smile_cas_close
        with chchange

        li "Let's go then."

        stop ambient fadeout 1.0
        stop sound fadeout 1.0
        stop music fadeout 1.0

        scene bg fanres_entrance
        with locationskip

        play music music_waltz fadein 2.0 volume 0.5

        "Receptionist" "Welcome to our humble establishment. Do you wish to have a table for two?"
        "The young man at the door makes a deep bow before noticing Lilly's cane and fidgeting a bit, unsure on how to proceed."
        ha "I arranged the reservation in your name."
        "I keep my voice barely above a whisper, but Lilly replies with a subtle nod and bows to the man who addressed us."

        show lilly basic_smile_cas_close at twoleft
        with charaenter

        li "Good evening. My name is Lilly Satou. I believe a reservation was made in my name."
        "Receptionist" "Satou? Ah yes, an e-mail was sent specifically requesting a table in the corner."
        li "…That's correct. Would that be a problem?"
        "Receptionist" "Not at all. Please walk this way."
        "He makes a motion to follow him, then realizes again that Lilly can't see him, and I can see him ponder whether he should take Lilly's arm or not."

        show lilly basic_planned_cas_close
        with chchange

        "Lilly seems to pick up on the man's dilemma as she gives him a reassuring smile."
        li "Please lead the way. My friend will assist me."
        "Receptionist" "As you wish. Please follow me."

        scene bg fanres_table
        with locationchange

        $ renpy.music.set_volume(1.0, 2.0)

        "As we get seated in what is indeed a relatively quiet corner of the restaurant, I let out a relieved sigh."

        show lilly basic_satisfied_cas_close
        with charaenter

        li "I think the hardest part is over now. Let's have fun for the rest of the evening."
        ha "Y-yes."

        show lilly basic_smileclosed_cas_close
        with chchange

        show lilly:
            yanchor 1.0 ypos 1.1
        with charamove

        "We fall silent, and I spend some time getting my bearings back and taking in the room."
        "When I look at Lilly, I can tell she's doing the same, carefully and structurally taking in and categorizing the various sounds around us."
        "After listening to a few songs that are being played, she smiles."

        show lilly basic_cheerful_cas_close
        with chchange

        li "Ballroom music. How nice. Was this an informed or an educated guess on your part, Hanako?"
        ha "A little bit of both."
        "It's true. We found out some time ago that Akira's a stickler for jazz music, but I always believed Lilly's musical taste, like nearly everything else about her, was slightly more traditional."
        "Of course, I ended up sending a text message to Akira to make sure, but she merely confirmed my hunch was correct."

        show lilly basic_smile_cas_close
        with chchange

        li "Hanako, can you describe our surroundings to me, please?"
        ha "Hmmm, okay."
        "I take a careful look around."

        show lilly basic_listen_cas_close
        with charachangealways

        ha "The room itself is rather large and tall…"
        ha "…there's a spacious dance floor near the center of the room…"
        ha "…the tables for the patrons are in a semi-circle around it…"
        ha "…on the other side is the ensemble playing the music…"
        ha "…the furniture and decorations are a bit old-fashioned, but practical…"
        ha "…lighting is modest. There is some lighting equipment on the ceiling pointing at the dance floor, but it's not being used for this type of music."
        ha "According to their website, they play different kinds of music on different days…"
        "I pause for a moment, wondering how detailed Lilly wants me to be."

        show lilly basic_smile_cas_close
        with chchange

        "She seems to be satisfied with my description so far."
        li "Thank you, Hanako."
        "I take a look at the menu. It's far too extensive to read entirely."
        ha "Would you like me to read the categories on the menu, Lilly? Or should I make a few recommendations myself?"
        li "Could you tell me what salads they have to offer, Hanako?"
        ha "Ummm, let's see…"

        show lilly basic_listen_cas_close
        with chchange

        "I can't say this place has the cheapest food in the world on offer. It's a good thing Lilly offered to pay for a large share of the costs or my funds would have been completely drained by now."
        ha "Lilly?"

        show lilly basic_smile_cas_close
        with chchange

        li "Yes, Hanako."
        ha "Thanks for footing such a large part of the bill. I… appreciate it."

        show lilly basic_cheerful_cas_close
        with chchange

        li "Thank you, Hanako, for having spent such a large amount of time with me lately. I've really been enjoying these outings."

        show lilly basic_oops_cas_close
        with chchange

        li "I… really hope this hasn't come at the cost of your relationship."
        ha "Don't worry, it hasn't. I still spend time with Hisao whenever I can and ummm…"
        "I hesitate to continue, not wanting to make things too awkward."

        show lilly basic_cheerfulblush_cas_close
        with chchange

        "Lilly, however, completes my sentence with more than a hint of amusement in her voice."
        li "…you two stay over at the other's place regularly, don't you?"
        "I giggle shyly."
        ha "Y-yes, but p-please don't tell that to anyone."
        li "Don't worry about that."

        show lilly basic_smileclosed_cas_close
        with chchange

        "Our food is brought in, and Lilly starts eating in that carefully measured manner of hers, using her chopsticks to feel and probe each piece of food before picking it up and putting it in her mouth."

        show lilly basic_giggle_cas_close
        with chchange

        li "It's funny. I never imagined you to outpace me in the boys department. Perhaps someday it'll be me approaching you for relationship advice."
        "I can't help but chuckle at that before rolling my eyes in a self-deprecating way."
        ha "I-I don't think you'll want to go about things the way I did. It's a miracle everything worked out the way it did."
        li "A miracle or perhaps merely fate."
        ha "It'd be nice to think so."
        "Taking a sip of tea, my mind realizes the implication she made before."
        ha "Lilly, you said I outpaced you. Does that mean you've never had a boyfriend before?"

        show lilly basic_smile_cas_close
        with chchange

        li "Does that surprise you?"
        "It does indeed. Lilly's one of the most popular girls in school, and it's a miracle nobody ever set up a fan club at Yamaku dedicated to her."
        ha "You've never received any confessions?"

        show lilly basic_cheerfulblush_cas_close
        with chchange

        li "I did. And not all of them from boys. Puberty can be a funny thing, particularly at an all-girls school."
        "{i}Holy crap!{/i}"
        ha "And you turned them all down?"
        li "I suppose I am… very particular… about the people I get close to."
        "I guess she is. I remember Hisao pointed out that he and I are the only people she spends her evenings with."
        "I suppose a lot of the people she's on good terms with share a more superficial bond with her."
        ha "But you did let me get close… and Hisao, who's a boy."

        show lilly basic_smileclosed_cas_close
        with chchange

        li "I did."
        ha "Lilly… Did you… like… Hisao?"

        show lilly basic_weaksmile_cas_close
        with chchange

        li "That question brings back memories."
        "It does. A few days after the festival, I asked Lilly what she thought of Hisao. But she ended up reversing the question, and I ended up admitting I had a crush on him."
        "That was something out of the ordinary for me. I'm not someone who quickly takes a liking to other people, and yet I developed feelings for a person whom I had known for only a little more than a week."
        "I've never been able to completely explain it. He was kind to me, of course, but there was something else that probably played a larger role."
        "Even before I came to know that he faced a few circumstances similar to my own and that we shared several hobbies, there was something about him that felt familiar… comfortable. Like a kindred spirit."
        ha "Y-you never really answered back then."

        show lilly basic_giggle_cas_close
        with chchange

        li "You are asking me if I've ever considered Hisao potential boyfriend material?"
        ha "Y-yes. You… said you are particular about who you let close."
        ha "If I hadn't admitted I liked Hisao, would you have… approached him at some point?"

        show lilly basic_smile_cas_close
        with chchange

        li "I will admit he is the type I could see myself falling for, so to speak."

        show lilly basic_smileclosed_cas_close
        with chchange

        li "Maybe if circumstances had been different…"
        ha "You mean, if it hadn't been for me…"

        show lilly basic_displeased_cas_close
        with chchange

        "Lilly makes a gesture to indicate she wants to say something, and her expression becomes a bit more stern than usual."
        li "Hanako, I feel it's important to make a few things clear before you draw your own conclusions."
        li "I merely said I could have fallen for Hisao under the right circumstances."
        li "But those circumstances haven't taken place."
        li "I am not in love with your boyfriend, nor has that ever been the case. The two of us have never been rivals in love."
        ha "I don't really understand."

        show lilly basic_giggle_cas_close
        with chchange

        "Lilly lets out a chuckle."

        show lilly basic_smileclosed_cas_close
        with chchange

        li "As you can probably imagine, I am not one to fall in love with someone at first sight."
        li "In order for me to fall in love with someone, I have to come to know and like him over time, he must show an interest in me, and I must be open to the possibility of a relationship myself."
        ha "And that wasn't the case?"

        show lilly basic_smile_cas_close
        with chchange

        li "I've come to know and like him, but it quickly became clear to me he was more interested in you than in me, so I did not allow myself to be open to the possibility. Thus, I did not fall in love with him."
        "That sounds so rational. I still feel Lilly dismissed the opportunity prematurely because she wanted me to have a chance at love. And she didn't stop there."
        ha "L-Lilly… I… I feel my relationship with Hisao would… never have happened without your efforts. And I never really thanked you for that."

        show lilly basic_surprised_cas_close
        with chchange

        li "That isn't true, Hanako. The two of you fell in love on your own accord and started a relationship through your own choices and efforts."
        ha "But he never even would have spent enough time near me to start liking me if it hadn't been for you."
        ha "You're the one who was so nice to him and had him join our lunch breaks, and you're the one who started inviting him to our tea parties in the evening…"
        ha "…and you got him involved in shopping for my presents and took us along for that night on the town, and he told me you were also the one who convinced him to keep having faith in me after I locked myself up in my room, and…"
        "…"
        "I suddenly realize I've started to ramble. I cut myself off and take a deep breath."
        ha "Lilly, is there… anything I can do for you in return? Anything at all?"

        show lilly basic_weaksmile_cas_close
        with chchange

        "Lilly smiles at my offer, but shakes her head."

        show lilly basic_smile_cas_close
        with chchange

        li "It's okay, Hanako. I don't need anything. If my actions led to something good, that in itself is enough of a reward."
        li "Besides, getting a relationship started is one thing, but maintaining it is another, and so far, I can tell you've been doing a very good job."

        show lilly basic_cheerful_cas_close
        with chchange

        li "I've heard Hisao has been looking into brochures for different universities."
        li "The last time I asked him what he wanted to do after Yamaku, he said he didn't know. Now he seems to have a clear idea on what to do after graduation."

        show lilly basic_smile_cas_close
        with chchange

        li "I think your support played a large role in that."
        ha "I… did encourage him as much as I could. But I think Mutou deserves a lot of credit too."

        show lilly basic_giggle_cas_close
        with chchange

        li "Is Hisao still enjoying those one-on-one discussion sessions with Mutou?"
        ha "I believe so, though they're not one-on-one anymore since last week."

        show lilly basic_satisfied_cas_close
        with chchange

        li "More people joined?"
        ha "Yes, Hisao convinced his hall-mate to give the science club a try. He's the person from your class who worked with us on the main banner for the festival."
        li "Kenji Setou? Fascinating. His science marks aren't bad, but I never knew he had a special interest in the subject."

        show lilly basic_surprised_cas_close
        with chchange

        li "Then again, I don't really know him very well. He rarely speaks in class."
        ha "I don't know him well either, but apparently he's rather talkative in private."
        ha "He's kind of a friend to Hisao, I think, but Hisao usually asks me to wait outside earshot range when Kenji comes up to talk, so I don't know what they talk about together. ‘Guy talk’ is what Hisao calls it."

        show lilly basic_cheerful_cas_close
        with chchange

        li "I wonder how Hisao managed to convince him."
        ha "Ummm… I… might know. While Hisao was talking to Kenji, I tried listening in a bit."
        ha "I couldn't hear very well, but suddenly Kenji raised his voice and said something like ‘Alright! If it's really an all-guys club, I'd be crazy not to join.’ Or something similar."

        show lilly basic_giggle_cas_close
        with chchange

        li "Hmmm… I had no idea Kenji was into men. You learn something new and interesting every day."
        ha "When I asked Hisao about it, he got really awkward and just asked me to forget I ever heard that."

        show lilly basic_surprised_cas_close
        with chchange

        li "Hisao's not uncomfortable with homosexuality, is he? I always thought he was too easy-going to be offended by that."
        ha "I don't think so. Maybe it's just Kenji."
        ha "He likes to get really close to people when speaking to them, and… heh… they do have to share a bathroom and shower."
        li "Do you think Hisao knows about his neighbor in class?"
        ha "Misha? I don't think he does, even though he's pretty good friends with her."
        ha "He wasn't around when she changed her haircut. He probably thinks she's always had her hair like that. I didn't tell him about it."

        show lilly basic_reminisce_cas_close
        with chchange

        li "After all this time I still wonder at times what that girl sees in Shizune."
        "Lilly's reaction feels a bit awkward."
        "For all her lady-like behavior, the subject of Shizune still never fails to get her uncharacteristically worked up."
        ha "T-the two of you haven't always been at odds, have you?"

        show lilly basic_weaksmile_cas_close
        with chchange

        li "We haven't. We used to get along in the past, and when Mother and Father left Japan, we even got closer to each other."
        ha "Really?"
        li "My father and Shizune's father dislike each other, so while my parents were still living in Japan we rarely met with the Hakamichis."
        li "But Akira has a great fondness for Shizune's little brother, so after we started living on our own, we'd drop by at their house whenever we had the opportunity to."
        li "I'd like to think Shizune and I got along with each other pretty well despite our inability to communicate with one another without Shizune using written notes and Akira acting as a medium or writing letters into each other's hand using our fingers."

        show lilly basic_displeased_cas_close
        with chchange

        li "But when Shizune became student council president and I had to deal with her, things changed very quickly. "
        ha "P-power corrupts and absolute power corrupts absolutely?"

        show lilly basic_giggle_cas_close
        with chchange

        "Lilly laughs heartily for a moment at the silly use of a term like ‘absolute power’ in combination with the student council presidency, before taking a sip of her drink and continuing."

        show lilly basic_weaksmile_cas_close
        with chchange

        li "I do not think so in this case. I don't think Shizune has ever really changed at all. She's still the exact same person she was half a decade ago."

        show lilly basic_smileclosed_cas_close
        with chchange

        li "Maybe it is I who have changed."
        ha "You?"
        li "Shizune has always been ambitious and full of ideas."
        li "When we spent time together in the past, she'd often go over her plans for the future in detail, and we enjoyed chattering about them."
        ha "Such as…?"
        li "Organizing a charity festival, setting up our own orphanage, setting up a school for the disabled similar to Yamaku… taking over the world one city council at a time."
        ha "Pffff…w-what?"

        show lilly basic_weaksmile_cas_close
        with chchange

        "That last part was so absurd I nearly choke on my drink. Judging from Lilly's sheepish smile, she's fully aware of this."
        li "I am aware that last part was a bit childish. We got a little carried away every now and again. We were only fourteen at the time."
        ha "And when she became student council president, she still had all her ambitions?"

        show lilly basic_displeased_cas_close
        with chchange

        li "Yes, but not the means to fulfill them."
        li "To most of its members, the student council was like a school club to put a few daily hours in after class and then devote the rest of their time to homework and relaxation."
        li "Not every member had Shizune's good grades that allowed her to get by with only a minimum of studying, nor did every member want to spend all their time in the council room until sundown, relying on take-out food each day because the cafeteria and shops closed already."

        show lilly basic_reminisce_cas_close
        with chchange

        li "Shizune would consistently dismiss these concerns and charge ahead with her plans without taking others into account."

        show lilly basic_displeased_cas_close
        with chchange

        li "It's been like this since she took over as president, and it will most likely remain that way until she graduates."
        ha "And you took it upon yourself to point out those reservations to her on other people's behalf?"
        li "Yes, at first I did it because I was the person who knew her best."

        show lilly basic_reminisce_cas_close
        with chchange

        li "Eventually, it became somewhat of an unspoken agreement that I'd usually be the one to deal with Shizune if conflicts arose in any way, which often happened seeing that Shizune likes to regard conflicts as challenges to win rather than as situations to resolve through compromise."
        li "But at least others could remain on semi-amicable terms with her this way while my relationship with her was already in a broken state anyway."
        li "It has remained this way even after I left the student council and limited my activities to class representative duties."
        ha "And she didn't take your objections to her policies very well?"

        show lilly basic_weaksmile_cas_close
        with chchange

        li "Before we enrolled at Yamaku, I used to cheer her on all the time and encourage her to follow her dreams."

        show lilly basic_displeased_cas_close
        with chchange

        li "These days she regards my attempts to convince her to slow down and look before leaping as hypocritical."
        "Lilly's story has made me think. I don't have exactly great chemistry with Shizune and Misha; Shizune's brashness and Misha's loudness are traits that tend to put me off."
        "But I don't dislike them either. Hisao is on very good terms with both of them, a good thing since he often has to do assignments with them, even if he admits Shizune is sometimes a pain to deal with."
        "Still, even though Hisao tends to butt heads with Shizune on a very regular basis, neither seems to walk away from those conflicts with hard feelings towards the other."
        "It's a pity the same can't true for Lilly and Shizune. Someone who dreams about setting up orphanages can't be a bad person in my book."
        ha "It's… ummm… a s-shame things have gotten so p-personal between you two."
        ha "Y-you might still get along with each other as long as you weren't f-forced to work on something together."

        show lilly basic_weaksmile_cas_close
        with chchange

        li "It's nice to believe so, but I don't think a lot is bound to change anytime soon."
        li "It's a whole lot more likely that the science club will soon overshadow the student council in terms of membership."
        "Funny she says that, because if my “secret project” succeeds that could be the case soon."
        ha "Ummm… Lilly, can you… k-keep a secret?"

        show lilly basic_surprised_cas_close
        with chchange
        with Pause(0.5)
        show lilly basic_smile_cas_close
        with charachangealways

        li "Of course, Hanako."
        ha "What you said about the science club membership… might happen. At least, I hope it does. For Hisao."
        li "Does Hisao have recruitment plans then?"
        ha "N-no. But I'm p-planning something that might get him a few new members."

        show lilly basic_surprised_cas_close
        with chchange

        li "Really? What are you planning?"
        ha "Ummm… I… approached Mutou last w-week and conducted an interview with h-him."
        ha "Using the information he gave me, I've written a short article about the club that'll appear in the next issue of the school newspaper. With l-luck, students with interest in the subject will take notice."
        ha "B-but it's supposed to be a surprise, so you can't tell Hisao about it."

        show lilly basic_listen_cas_close
        with chchange
        with Pause(1.0)
        show lilly basic_satisfied_cas_close
        with charachangealways

        "Lilly is silent for a moment before breaking out into a huge smile."
        "I see something on her face that I haven't seen there before. A look of admiration."
        li "Hanako… What a clever initiative. I never would have thought of that myself. Hisao will love this."
        ha "T-thanks. I really hope so."
        li "What did the newspaper club say about your idea?"
        ha "Naomi liked the idea. However she said that only club members are allowed to submit articles."
        ha "So, I officially joined three days ago. Though… Hisao doesn't know that either."

        show lilly basic_cheerful_cas_close
        with chchange

        li "Congratulations, Hanako. You're turning into quite a reporter."
        ha "D-do you… really… think so, Lilly?"

        show lilly basic_smile_cas_close
        with chchange

        li "I do."
        ha "B-because, I've been thinking."
        ha "Mutou said… he was pleased to see I was developing m-my interests and s-suggested to think about… doing something with it after graduation and talking to the teacher in charge of the newspaper club about it."
        li "And will you?"
        ha "M-maybe. I still want to think it through a little more."
        ha "I mean… I'd never stand in front of a c-camera, but things like writing articles and columns or doing research and fact checking or editing… I think I'd enjoy doing all of those."

        show lilly basic_smileclosed_cas_close
        with chchange

        li "It sounds like you've given it quite some thought already."
        li "I think you can take your time and come to a decision with plenty of time to spare. Graduation is still many months away."
        ha "I… I plan to think things over during summer break. Hopefully, by the end, I will have made up my mind."
        ha "If I decide against it, m-maybe something like technical writer or copywriter would be a good alternative."

        show lilly basic_smile_cas_close
        with chchange

        li "That seems like a very good idea. Do you have any plans for summer break?"
        "I repress the temptation to tell her that depends on her decision."
        "The truth is I have some plans, but none of them are really viable right now."
        ha "N-not really. I've thought about travelling a bit… seeing things."
        ha "Naomi's mentioned that's what she's going to do during the summer, and I liked the idea as well."
        ha "But I don't think I can spare the money right now. I want to keep some money aside so Hisao and I can keep going on dates."
        "I sigh wearily."
        ha "A relationship is a really wonderful thing to have, b-but it's not always cheap."

        show lilly basic_weaksmile_cas_close
        with chchange

        "Lilly merely reacts with a nod and a smile; a sign that I'm not going to get a lot of sympathy from her for no longer being single."
        li "Hanako?"
        ha "Hmmm?"

        show lilly basic_smile_cas_close
        with chchange

        li "Approaching Mutou for that interview… Was that hard for you to do?"
        "It was actually."
        "Even though I'm familiar with Mutou and think highly of him as a homeroom teacher, the thought of approaching him for a favor still caused me to have at least one sleepless night."
        "Yet strangely enough, it was also easy in a way."
        ha "It was… really hard, yet also really easy."
        ha "I just kept reminding myself that I was doing this for Hisao."
        ha "And it helped. It really helped."
        li "What if it had concerned a favor for yourself?"
        ha "I wouldn't have been able to do it."
        "A quick and definite answer, but I know myself well enough to sense that it's true."
        ha "T-they say it's easier to be selfish than to be selfless."
        ha "If it was for Hisao's sake I… I… I feel like I'd be able to do anything, but…"
        "That was the worst ad lib ever."

        show lilly basic_listen_cas_close
        with charachangealways

        "Lilly's reaction isn't the amused smile I was expecting though. Instead, she just looks lost in thought. Lost in thought and just a little bit sad."

        show lilly basic_weaksmile_cas_close
        with chchange

        li "…but not for yourself."
        ha "N-no. I guess nobody's perfect."
        li "I know exactly what you mean."

        show lilly basic_listen_cas_close
        with shorttimeskip

        "Our dinner and conversation finished, we hang back and relax, Lilly listening to the music and me watching the patrons on the dance floor."
        "It's gotten a bit crowded there, and I giggle as two couples making a flashy turn at the same time accidentally bump into each other."

        show lilly basic_surprised_cas_close
        with chchange

        li "Did something amusing happen?"
        ha "Just… four people having an awkward collision on the dance floor."

        show lilly basic_giggle_cas_close
        with chchange

        li "That brings back memories."
        "I think I just learned another thing about Lilly."
        "Although I'm hardly surprised to learn Lilly has participated in style dancing before, given the fact she likes the kind of music that's used for the activity. It fits in neatly with the image I already had of her."
        "She's probably pretty good at it too, seeing that even her normal manner of moving already has a certain amount of grace."
        ha "You know how to dance?"

        show lilly basic_cheerful_cas_close
        with chchange

        li "I do. I had dance courses in middle school."
        ha "Was it hard to learn? I mean, harder for you than… for the rest?"

        show lilly basic_smileclosed_cas_close
        with chchange

        li "I don't think it was. One doesn't need eyesight in order to memorize what body parts to move at what moments."
        li "Of course, at least one partner being able to see certainly makes things easier."
        ha "I… think I would have liked to see it. You're probably a very graceful dancer."

        show lilly basic_smile_cas_close
        with chchange

        "Lilly playfully twirls one of her blonde locks around her finger and smiles at me."
        li "Am I correct when I assume you're asking me for a demonstration, Hanako?"
        ha "T-that's probably… a bit difficult right now. But I would have liked to see you dance."
        li "Are you serious?"
        ha "O-of course."
        li "Really?"
        ha "Yes."

        show lilly basic_planned_cas_close
        with chchange

        li "Very well then. I hear they're playing a slow waltz right now."
        li "That's fortunate, for that's a rather easy one to perform."
        ha "Ummm… but, don't you need a partner to…"

        show lilly basic_smile_cas_close at center
        with charamovechangefaster

        "Before I can finish my sentence, Lilly gets up and extends her hand to me with a playful expression on her face."
        li "May I have this dance, Miss Ikezawa?"
        "{i}Wait a minute!{/i}"
        "I curse myself for not seeing this one coming after such a shamelessly obvious lead-in."
        ha "W-w-wait Lilly, w-w-we're two g-girls, aren't w-we?" # even better, hanako

        show lilly basic_planned_cas_close
        with chchange

        li "That's not a problem for me. I know the steps for both the male and the female partner."

        show lilly basic_giggle_cas_close
        with chchange

        li "My middle school was girls-only, so I've had nothing but female dance partners. I'm used to it."
        ha "T-this isn't m-middle school. W-we'll attract a-a-attention."

        show lilly basic_smile_cas_close
        with chchange

        li "Just as one person teaching the other a few dance steps. Most people will have to focus on their partner to avoid tripping."
        ha "B-but… but…"
        li "You asked for a demonstration, and I think the best way to go about it is to show you up close and teach you a few steps myself."
        li "We could go over to the dance floor and see if there are any open spots away from the seated patrons."
        "I sigh."
        ha "J-just a look then."

        hide lilly
        with charaexit

        "I get up, take Lilly's arm and slowly lead her to the area bordering the dance floor."

        scene bg fanres_entrance
        with locationchange

        "As we circle the area in search of a bit of space, I try to wrap my head around this uncharacteristically forward move."
        "It isn't like Lilly at all to try and push against my boundaries like this. For as long as I've known her, she's been protective—sometimes even over-protective—of me."
        "But tonight, more than ever before, I feel like we've been interacting as equals. We both spoke candidly about ourselves; Lilly of her past and I of my future."
        "This kind of interaction between us wouldn't have been possible two months ago. This kind of outing wouldn't have been possible two months ago."
        "Is Lilly trying to find out how far I will go in defying my own anxieties?"
        "Is she… testing me?"

        show lilly basic_smile_cas_close
        with charaenter

        li "Do you want to give it a try?"

        scene ev ballroomdance_emb_large:
            align (0.5, 0.1) zoom 1.1
            ease 5.0 zoom 1.0
        with mediumflash

        "We reach a corner of the dance floor near the ensemble and away from the tables that isn't particularly crowded."
        "My eyes warily skim the crowd, but nobody seems to be paying us any attention."
        ha "V-very quickly then."
        "Picking out a somewhat secluded spot near the edge, I walk Lilly in place and turn to face her."
        "She's wearing a reassuring smile on her face that's not quite catching on yet."

        show ev:
            zoom 1.0
            ease 4.0 xalign 0.4

        li "Could you give me your right hand, Hanako?"
        "I place my hand in hers, shivering a bit as her fingers briefly touch my scar tissue."
        li "Now, can you place your left hand on my shoulder?"
        "I do so, but can't help feeling really weird. A feeling worsened by the fact she's wearing her off-the-shoulder sweater and my hand is touching her bare skin."
        ha "A-and now?"
        li "Please place your right foot between my feet."
        "I follow suit and stiffen for a moment as Lilly places her right hand onto my left shoulder blade."
        "I look around nervously, but it doesn't seem like people around us are taking notice of us. Either that or they really don't care."

        show ev:
            xalign 0.4
            ease 2.0 xalign 0.45

        li "Let's begin. Could you take a step back with your left foot, count to two and put your right foot beside it?"
        ha "Umm… Like this{cps=3}...? {/cps}{nw}"

        show ev:
            linear 0.05 xalign 0.455
            linear 0.05 xalign 0.45
            repeat 5

        extend "Eek!"
        "The moment I take a step back, Lilly lifts her right foot, presumably to let me drag her forward a bit and determine the length of my steps."
        "Since I wasn't expecting this lack of resistance, I try to put my foot back and almost lose my balance, which would have resulted in me dragging us both to the floor and her ending up on top of me."
        "That'd be enough reason for me to run out of here and deny this evening ever happened."
        ha "I-I-I'm sorry!"
        "Lilly doesn't seem to be put off by my blunder and gives me a reassuring smile."
        li "Don't worry. Everybody tends to stumble a bit at first."
        li "Let's try again. Take a step back as slowly as you can now."
        "I take another step back, trying to move in slow motion this time."

        show ev:
            ease 30.0 xalign 0.5 zoom 0.75

        "Sure enough, Lilly moves her foot again and fluidly advances to close the distance. I move my other foot back and Lilly follows up, lightly brushing her foot against mine."
        li "Much better, Hanako. But try to keep the distance between your feet consistent."
        ha "Like this?"
        "One more step back and this one goes without incidents."
        "Lilly gives me a pleased nod."
        li "Very good. Now we'll try the reverse. Take a slow step forward with your right foot."
        "This time Lilly leans slightly back and I'm pulled forward a bit, but before I can lose my balance, she straightens herself out."
        "This is like some odd balancing game she's playing."
        li "One more time."
        "I take another step forward, trying hard not to bump into Lilly by accident."
        "She seems satisfied with the distance and speed of my movement."
        li "Let's try to go back and forth a few times to see if we can get a movement rhythm down that feels natural for both of us."
        ha "O-okay."
        "I carefully try to retrace the steps I took earlier."
        "After about half a minute of moving back and forth, Lilly signs for a break."
        li "Are you up for some variation, Hanako?"
        ha "Ummm… what do you mean?"
        li "Next, try making a slow sidestep to your right, followed by a sidestep to the left."
        ha "That doesn't s-sound too difficult."

        show ev:
            xalign 0.5 zoom 0.75
            ease 30.0 zoom 0.5

        "I move left and right several times, letting Lilly get used to the steps I take."
        "This is much easier than the backwards and forward movement."
        li "Not too hard, is it?"
        ha "N-no."
        li "Then let's combine the two to create a counter-clockwise movement."
        ha "W-what?"
        li "Back, right, forward, left."
        ha "B-back, right…"
        "I slowly try to adopt the new pattern, struggling at first to memorize the order."
        ha "Forward, left…"
        "After several minutes, Lilly stops me."
        li "You have very consistent movement, Hanako. That's a good thing. I think I'll be able to take it from here."
        ha "T-take it from here?"
        li "The steps I'm taking belong to the leading partner. I needed to get used to your movement patterns a bit, but I think I have the timing down now. Just continue as you did before."
        "We resume, but this time Lilly starts making more active movements instead of going along with mine, occasionally shifting her weight to correct me."
        "At first, I'm positive we're going to trip and fall, but as we continue I realize that as long as I don't deviate from the step length I've been going with, our movements are nearly perfectly synchronized."
        "I can't believe that Lilly got a feeling for my movements that quickly. She really is good at this."
        li "Left, back, right, forward."
        "I'm starting to risk the occasional glance away from our feet. Nobody's paying us any attention, thank goodness."
        "I giggle nervously."

        show ev ballroomdance_smile_large:
            zoom 0.5
            ease 30.0 zoom 0.4
        with Dissolve(1.0)

        ha "R-right, forward, back…"
        li "Try to relax your upper body a little bit more, Hanako."
        ha "R-right."
        ha "Left, back…"
        ha "Right, forward…"
        ha "Left…"
        ha "Back…"
        "This is starting to become fun."
        "When I look up at Lilly, I notice she's wearing a beaming smile."
        "I can't help but smile back, even though she can't see that."
        "Maybe I misjudged her earlier, and she really wanted to merely share some of her experience with me."
        "Lilly is one of those people who'd probably pay to be a teacher. Whenever she gets the opportunity to help someone brush up on something she's knowledgeable about, she's overcome with a childlike eagerness that's actually very endearing."
        "This seems to be one of those opportunities."
        li "Hanako?"
        ha "Yes?"
        li "Let's try a natural turn next."

        stop music fadeout 2.0

        scene bg school_girlsdormhall
        with Fade(1.0, 0, 1.0)

        play music music_twinkle fadein 4.0

        "I patiently wait as Lilly runs through her bag in search of her room keys."
        "Tonight was great fun. The dancing part was maybe a bit much, but I'd be lying if I said it wasn't interesting to try."
        "Moreover, I feel that I've gotten to know Lilly a little better tonight."

        show lilly basic_cheerful_cas_close
        with charaenter

        li "Hanako, thank you very much for tonight. I truly had a great time."

        play sound sfx_dooropen
        show lilly:
            ease 1.0 twoleft

        "Lilly has found her keys and has opened her door."

        show lilly at twoleft

        ha "Same here. I also think I've learned a few things about you I didn't know before."
        "Before she enters her room, she turns to address me."

        show lilly basic_smile_cas_close
        with chchange

        li "The same goes for me. You've… really changed lately, Hanako."
        ha "F-for the better?"
        li "Definitely."
        "Lilly's smile is warm and genuine, but I don't think it's my imagination that there's a subtle trace of wistfulness in her voice, and that for a moment, no more than a split-second, there's a hint of sadness on her face."

        show lilly basic_sad_cas_close
        with chchange
        show lilly basic_cheerful_cas_close
        with charachangealways

        "But when I blink my eyes, it's gone already, and Lilly's mouth curls into a playful grin."
        li "I don't think Hisao needs to know everything that took place tonight."
        "I giggle."
        ha "I agree."
        li "Good night, Hanako. I'll meet you at school tomorrow."
        ha "Good night, Lilly."

        hide lilly
        with charaexit

        play sound sfx_doorclose

        "Our farewells behind us, Lilly closes the door, and I take a glance at the door of my own dorm room, check the time on my cell phone and then briskly walk down the hallway."

        stop music fadeout 2.0
        scene black
        with Dissolve(2.0)

        if _in_replay:
            return

    return