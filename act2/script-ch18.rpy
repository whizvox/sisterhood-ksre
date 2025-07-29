label sh_ch18:
    label .s1:

        $ set_window_tint(TINT_HANAKO)

        call sisterhood_timeskip

        scene bg school_gate_ss:
            yalign 0.5 zoom 1.02
        with Dissolve(2.0)

        play music music_night fadein 4.0

        "I nervously pace back and forth in front of the gate, occasionally checking my phone to re-read the message Akira sent me. It said: ‘Can we talk for a bit? Front gate.’"

        nvl clear
        nvl show dissolve

        n "Lilly may be staying here, but Akira is still leaving tomorrow. Even though Lilly's decision to remain here has softened the blow a lot, I'm still going to miss Akira."
        n "I can't say I'm as close with her as I am with Lilly, and I often felt a bit like a third wheel when Lilly and her sister were hanging out in her room, but nevertheless it was nice to have someone else who'd occasionally talk to me besides Lilly."
        n "Even though Lilly is planning to visit Scotland again in the near future, we still decided to hold a small goodbye party for Akira this evening. Lilly, Hisao, and I went to town earlier today to shop for a few things—unfortunately neither of us are old enough to buy a few cans of beer for Akira—and we were busy setting things up in Lilly's room when I received Akira's message."
        n "{vspace=60}I'm still not completely sure how Akira really feels about Lilly's change of heart. I know how close she and her sister are. Akira practically raised her during the most recent third of her life. Suddenly being half a world apart from her can't be easy."

        nvl hide dissolve

        play sound sfx_impact
        with vpunch

        aki "Yo!"
        "I let out an involuntary cry when someone suddenly pats me on the left shoulder from behind."

        show akira basic_smile
        with charaenter

        ha "A-Akira! Ummm, I mean… Hello, Akira."
        "I must have been pretty distracted by my thoughts for Akira to be able to sneak up on me like that."

        show akira basic_laugh
        with chchange

        aki "What's with the jumpiness? You knew I was coming, didn't you?"
        "I merely nod as I look her over as we start walking back."

        scene bg school_gardens2_ss
        show akira basic_resigned
        with locationchange

        "Her jacket does a decent job at hiding it, but I can still tell that her blouse and tie are far more wrinkled than I've ever seen them before. I have my doubts Akira came here straight off of work."

        show akira basic_sheepish
        with chchange

        "Akira seems to catch my gaze and smiles to confirm my suspicion."
        aki "Haven't been in the office for a week. I spent most of the time relaxing and hanging out with my little cousin. It was a nice change of pace."
        aki "Too bad I'll be expected to make up for it when I start at main office in a few days."
        ha "Ummm… Y-you w-wanted to talk?"

        show akira basic_smile_close
        with characlose

        "Akira gives a cheerful nod and moves over to one of the nearby benches. After sitting down, she reaches into the bag she's been carrying and gets out a can of beer."

        show akira basic_ending_close
        with chchange

        "She chuckles at my dumbfounded stare."
        aki "Didn't think they were gonna sell these to you kids, so I got my own. They should get me through the night. Sit down."

        play sound sfx_can

        "I carefully sit down next to her as she casually opens the can and takes a sip."
        "I don't think she's allowed to drink that on the school grounds, but right now there doesn't seem to be anyone around here but us."

        show akira basic_smile_close
        with chchange

        aki "I bet you're really happy about Lilly staying here. I mean, you looked pretty crushed before when she announced she considered leaving."
        "I try to gauge Akira's tone for any signs of hostility."
        "I was exhilirated yesterday when Lilly made the decision to stay here, but when I received Akira's message half an hour ago, I was reminded of the fact that I also played a part in separating two sisters who've been extremely close over the last six years."
        ha "I'm s-sorry, Akira."

        show akira basic_resigned_close
        with chchange

        aki "Huh? For what?"
        ha "I… uh, m-might have p-played a part in Lilly's decision t-to stay h-here. S-so I'm p-partially at fault for you l-losing her."

        show akira basic_boo_close
        with chchange

        "Akira takes a swig of her beer and smirks."
        aki "Is that why you're so on edge? You thought I was gonna shout at you for helping Lilly reach the conclusion that she'd rather stay here instead of going to Scotland with me?"
        "Something like that, although the way Akira puts it makes it sound like a pretty unreasonable thing to think."

        show akira basic_wistful_close
        with chchange

        aki "Let's get one thing out of the way. I'm gonna miss Lilly, of course, but I'm not upset that she chose to stay here. So stop worrying about that, okay?"
        "I meekly nod and take a deep breath in an attempt to relax."
        "I feel a bit embarrassed by my occasional habit of assuming the worst about people. Seeing how friendly Akira has always been to me, she certainly deserved the benefit of the doubt."
        aki "Seeing that Sis told me that you two reconciled yesterday, I had a hunch that you were involved in her change of heart somehow. And you pretty much confirmed that just now."
        
        show akira basic_resigned_close
        with chchange
        
        aki "So I'm really curious… What exactly happened?"
        ha "Ummm…"
        "That's a pretty tricky question. I'm not really sure whether Akira got the specifics about my outburst last week that nearly drove Lilly away from me. I'm pretty ashamed about it in hindsight. If Akira is in the dark about the details, I'd like to keep it that way."
        ha "She t-talked to me about your parents. And about them w-wanting to make a new s-start. S-she supported that, but d-didn't want to give up what s-she had here. B-but s-she didn't want to feel responsible f-for keeping you all apart either."

        show akira basic_angry_close
        with chchange

        aki "Giving up everything she has here is a pretty damn high price for something that might not even happen. A price that I agree isn't even hers to pay."
        aki "I don't think she's right in blaming herself for our family's failure to come together again. I'm not even sure how viable it was in the first place."
        ha "Lilly s-said she wanted to t-try."
        aki "It's always surprised me how loyal she remains to our parents, for all the good they did us."
        "I cannot help but take note of how bitter Akira sounds while she's saying it. It makes me wonder about their parents."
        ha "What are t-they l-like?"

        show akira basic_resigned_close
        with chchange

        aki "Huh?"
        ha "Hisao said your m-mother s-sounded very friendly on the phone."

        show akira basic_distant_close
        with chchange

        "Akira doesn't immediately answer. Instead, she looks pensive, and for a moment I can see her eyes stare into the distance."
        aki "I think that if you'd meet them, you'd find them to be pretty friendly and amiable. I don't think it'd be just Lilly's upbringing that causes her to be as loyal to them as she is. But…"

        show akira basic_lost_close
        with chchange

        "She pauses for a moment and then looks straight at me, causing me to flinch instinctively."
        aki "…sometimes problems in a family are more subtle than people shouting at each other or acting like abusive assholes."
        ha "What do you mean?"

        show akira basic_distant_close
        with chchange

        aki "When we had our first dinner together in six years, Mom asked Lilly if she was still in contact with Kumi. Kumi was Lilly's best friend at the time Mom and Dad left Japan."
        aki "Lilly merely answered she wasn't."

        show akira basic_smug_close
        with chchange

        "Akira pauses for a moment and then smiles an impish grin."
        aki "At that point I decided to point something out that Lilly deliberately kept to herself in order to avoid an awkward moment."
        aki "I mentioned that a few months after Mom and Dad left Japan, Kumi and her family moved to another town, and contact between Lilly and her fizzled out after a few phone calls over the weeks thereafter."

        show akira basic_annoyed_close
        with chchange

        aki "Before that evening, maybe Mom and Dad were telling themselves they could pick up where the four of us left off at anytime. But that moment did a pretty good job at highlighting how out of touch we've gotten with one another."
        "That must have been beyond excruciatingly uncomfortable. I'm really thankful I wasn't there to witness it."
        ha "W-what happened next?"
        "Akira gives an annoyed shrug."
        aki "There was a painful pause for a second or two, Dad gave me a sharp glare for a moment and then we started talking about the weather."
        aki "Well, not literally the weather, but a safe subject. I decided not to be the bad guy twice in one evening, so I went along with it. But that tendency to avoid conflicts is pretty telling of how I think our parents plan to get us back together."
        aki "By encouraging us to pretend they never left us alone in the first place. I don't think it's gonna work like that, and I'll be damned if I'm gonna play along with that."
        ha "Avoiding conflicts?"

        show akira basic_sad_close
        with chchange

        aki "Dad's from a traditional Japanese family, and maintaining peace and harmony through avoidance of conflicts—even ones that shouldn't be avoided—was pretty much the law of life there."
        aki "But for a family trying to get back together, being good at avoiding uncomfortable subjects is actually a bad thing."

        show akira basic_annoyed_close
        with chchange

        aki "I don't know if this is some sort of official compensation for the past six years or if they really want to be with Lilly."
        "I take a moment to let Akira's words sink in. Always dodging conflicts is pretty much how, until recently, I often classified Lilly. But yesterday, I was forced to reconsider that view."
        "I don't know about Lilly's parents, but Lilly herself has proven yesterday that, although she's reluctant to move out of her usual diplomatic comfort zone, she's more than capable of speaking candidly about problems if that's the only way to solve them."
        "Since Akira doesn't seem to be aware of the specifics of Lilly's phone call with her mother, I feel the need to speak up on her behalf."
        ha "Lilly… was very d-direct yesterday while s-speaking with her m-mother. She w-wasn't very comfortable, but she still pulled through."

        show akira basic_resigned_close
        with chchange

        aki "What exactly did she say then?"
        "It's not easy for me to give out the exact details of the conversation, since I've only heard Lilly's half of it myself, but her remarks about the state of her family are still etched in my memory."

        show akira basic_sweet_close
        with chchange

        "As I tell Akira about Lilly's words involving the emotional distance in their family, I can see an expression on her face that's partially amusement, partially surprise, but above all pride in her sister."
        aki "Wow, she really said all that?"
        ha "Yes."

        show akira basic_laugh_close
        with chchange

        "Akira chuckles at her sister's uncharacteristic boldness."
        aki "Man, I'm not that surprised to hear that that's what she's been thinking, but for her to say that out loud and to our parents of all people."
        ha "I t-think she can continue to r-reach out to her parents if she makes the effort."

        show akira basic_sad_close
        with chchange

        aki "It all depends on whether she can continue to be straightforward with them or only when her back is against a wall."

        show akira basic_distant_close
        with chchange

        aki "{size=*0.7}And if it's the former, maybe I'll just get lucky, and she'll save some of that straight-forwardness for me.{/size}"
        "That last part of her sentence comes out as a soft mumble, but it's still loud enough for me to detect it."
        ha "W-what?"

        show akira basic_sheepish_close
        with chchange

        aki "Sorry, that came out worse than I meant it to. I'm just talking to myself a bit."
        ha "You're not… angry w-with her, are you?"

        show akira basic_distant_close
        with chchange

        play sound sfx_can_clatter

        "Akira empties her can and casually tosses it into the nearby wastebin. As she continues, I can sense a touch of gloom in her voice."
        aki "Mostly a tad angry with myself. I never got the impression that Lilly was very enthusiastic about moving, but I've never been able to get her to outright admit that she'd rather stay here either."

        show akira basic_sad_close
        with chchange

        aki "Seeing that you did manage to get that confession out of her, I kinda feel that you picked up a ball that I dropped. A ball I really shouldn't have dropped."
        aki "Since my choice probably influenced hers a lot, it was my responsibility to be the one to coax her into that decision she made yesterday."

        show akira basic_lost_close
        with chchange

        aki "If she'd have entrusted me with how she felt, that's exactly what I would have done. But she didn't, and that kinda stings."
        "I can't help but feel a little bit surprised at Akira's tone, which is so different from her usual confident-yet-playful attitude. I knew from the fact she practically raised Lilly for years that Akira has a responsible side, but this is one of the first times I've witnessed it myself."
        ha "She d-didn't tell m-me about it until the l-last moment either. So erm…"
        "I think in fact she only told me because her ‘back was against the wall’ at the time and she couldn't bear the thought of us parting with me harboring ill feelings towards her."

        show akira basic_ending_close
        with chchange

        "Akira gets the point though, and a teasing smile slowly appears back on her face."
        aki "So I guess a major chewing out is in order here, and I'll be happy to administer it before I leave."

        show akira basic_smile_close
        with chchange

        aki "But what she did wasn't extremely out of character for her."
        aki "She's always been reserved about disclosing her own feelings to others or show any signs of vulnerability. Kinda like Dad. And Mom… in her own way. I could have been more—one hell of a lot more—vigilant."
        ha "I… think what's most important is that Lilly ended up d-doing what she wanted for herself. Who m-made it happen, d-doesn't really matter that much."
        aki "You're probably right."

        show akira basic_wistful_close
        with chchange

        aki "Sorry to make you listen to all of this."
        ha "That's okay. That's… w-what f-f-friends… are f-for."
        
        stop music fadeout 2.0
        
        "I can't manage to make myself look Akira in the eyes as I say this, but Akira merely gives me a soft slap on the shoulder as if to accept and acknowledge what I just said."

        queue music music_friendship fadein 4.0

        show akira basic_sweet_close
        with chchange

        aki "Yup, that's what friends are for."
        aki "You know, I kinda feel bad I'm set to leave the country while you're getting more and more out of your shell. I hope you can keep this up, I really do. I guess I'll find out the next time I drop by here. Which I'm sure I will at some point."
        ha "I'll t-try."
        aki "Good. We should probably head off to Lilly's room. She's likely wondering what's keeping us."

        show akira basic_smile
        with charadistant

        "We get up, and Akira reaches for the bag that's been sitting next to the bench, then stops as if she just remembered something."
        aki "Before we go, there's one more thing I think I should say."
        ha "Y-yes?"

        show akira basic_sweet
        with chchange

        "Once again, Akira looks me straight in the eye, and when I reflexively look away, she moves a bit to re-establish eyecontact."

        show akira basic_peaceful
        with chchange

        aki "I really appreciate what you did for Lilly the other day. Thanks Hanako. Really."
        "She finishes her statement with a bow that contains far more grace than I ever suspected Akira of possessing."
        "I fidget nervously. How am I supposed to react to something like that?"
        "Hisao, Miss Yumi, and now Akira seem to regard me as some sort of hero, but all I did was give Lilly a small peptalk. It was Lilly who did the hard part afterwards."
        ha "Lilly d-deserves most of the c-credit for m-making the phonecall."

        show akira basic_sweet
        with chchange

        aki "You both ended up doing the right thing at the right time. But I'll be sure to praise her for her part as well."

        scene bg school_dormext_full_ss
        show akira basic_smile
        with locationchange

        "We start heading towards the girls dorm, and I take advantage of the moment to address something that caught my attention earlier."
        ha "You said… you were going to… d-drop by?"
        aki "Well, I still wanna see Lilly from time to time. Hopefully I'll be able to join the occasional business trip to the Japanese branch every now and then."
        ha "That would be nice."
        aki "It's still too early to make promises. In the meantime…"

        show akira basic_pleased_close
        with characlose

        "She playfully gives me a poke with her elbow."
        aki "…you don't mind keeping an eye on my sis while I'm gone, do you?"
        ha "W-W-WHAT?"
        "My eyes widen in shock as I try to digest Akira's seemingly ludicrous statement."
        "Me keeping an eye on Lilly? Not too long ago, Lilly was nothing less than a human crutch for me—my only connection to the rest of the student body and, most likely, to the rest of the world as well."
        "I've been trying to change our relationship lately, and I feel yesterday was a big milestone for both of us, but for Akira to suggest me to suddenly look out for Lilly seems like reality turned upside down."
        ha "I… um…. don't think Lilly needs l-looking after."

        show akira basic_wistful
        with charadistant

        "Akira seems to have been expecting that reaction and gives a short shrug."
        aki "Most of the time she doesn't. Lilly's a strong person, but she's not infallible."
        aki "She may be able to handle things herself 99 out of a 100 times, but that one time when she's struggling with something and she's too damn stubborn to call on anyone else, it'll be good to know that there's someone around who has her best interests at heart."
        aki "Someone to whom she feels close enough to confide things in. I'd say that description fits you to a tee. Probably more than anyone else around here."
        ha "R-really?"

        show akira basic_sweet
        with chchange

        "Akira stops walking and gives me a cheerful smile."
        aki "Let me tell you something that happened a little while back."
        aki "Lilly and I were speaking on the phone, and she noted how much you've changed recently. She liked the change in you, but it was also a bit uncomfortable for her."
        aki "She didn't want to go back to the times where you were clinging to her as if your life was depending on it, but the fact that the role she was playing in your life was changing so suddenly and rapidly made her feel awkward."

        show akira basic_ending
        with chchange

        aki "Hehe, I didn't tell her, but I could relate to how she felt. I've been there myself after all."
        ha "What do you mean?"

        show akira basic_ponder
        with chchange

        aki "Your relationship with Lilly is almost exactly like my relationship with her, except it's one stage behind. Even when we were still living with our folks, I was often the one who had to keep an eye on Lilly, helping her navigate everywhere and occasionally worrying about her."
        aki "But eventually she started growing more independent, and I was left with the nagging feeling that she was drifting away from me."
        aki "That was a bit of a rough time for me until I accepted that she wasn't gonna stay my little kiddie sister forever and we should try and become each other's responsibility instead if we didn't want to grow apart."

        show akira basic_ending
        with chchange

        aki "I think in the end we did pretty well, even though part of me will probably always think of her as my younger sister."
        "That's probably an understatement. On many occasions, Lilly and Akira seem more like best friends than sisters to me, and, at times, it made me a little envious. I think I would have loved having a sister like Lilly or Akira myself."

        scene bg school_girlsdormhall
        show akira basic_peaceful
        with locationchange

        aki "Maybe what happened yesterday was needed to make Lilly realize she has to adapt as well. With luck, the two of you'll soon be at the point where Lilly and I have been for the last couple of years."
        "I can't help but smile broadly at that suggestion."
        ha "I… really hope so."

        show akira basic_smile
        with chchange

        play sound sfx_doorknock2

        "Having reached the door to Lilly's dorm room, Akira delivers a few loud taps to announce her presence."

        stop music fadeout 1.0

        if _in_replay:
            return
    
    label .s2:

        $ set_window_tint(TINT_HANAKO)

        scene bg school_dormlilly
        show akira basic_smile:
            xalign 0.75
        show lilly basic_cheerful
        show hisao basic_grin_uni:
            xalign 0.15
        with locationskip

        queue music music_ease fadein 4.0

        aki "A first aid course?"

        nvl clear
        nvl show dissolve

        n "We've spent the last two hours hanging out in Lilly's room, eating the cake and sweets we obtained from the store in town this afternoon."
        n "{vspace=60}Despite it being a supposed farewell party, the mood has been surprisingly relaxed. Akira and Lilly spent most of the time exchanging cheerful banter with Hisao and each other."
        n "I, for my part, have been content to just sit and listen to the rest, treasuring the fact that, even though Hisao, Lilly and I went through a week from hell, we were able to reconcile and we are able to sit here and spend time together once more, our bonds not just repaired but actually strengthened."
        n "Due to the fact that just a week ago I had been convinced that I'd never be able to face Lilly or Hisao again, I've grown to value the time we're spending together even more."
        n "{vspace=90}Eventually the conversation turned to my upcoming training courses which Akira was keen on learning more about."

        nvl hide dissolve

        show hisao basic_smile_uni
        show lilly basic_smile
        with chchange

        ha "Y-yes. It's usually for staff members only, but the trainer will make an exception for me."
        aki "Sounds interesting. Or at least useful. Especially around here. How long is it gonna take?"
        ha "Five days."
        aki "For just the basics? That seems kinda long."
        ha "I think they want to reserve a lot of time f-for practice."
        aki "And when will this training be taking place?"
        ha "Next week."

        show akira basic_sweet
        with chchange

        aki "Well, good luck. Let's hope you'll never be forced to make use of it."

        show akira basic_boo
        with chchange

        "Akira gives Lilly a soft poke in the ribs with her elbow to get her attention."
        aki "Hey Sis, can I have another beer?"

        show lilly back_smileclosed
        with charachangealways
        show lilly basic_weaksmile
        with charachangealways

        "Lilly reaches into Akira's bag, which is lying next to her, takes out a can of beer and hands it to her sister."
        li "It is a bit of a shame that you didn't bring any of that tasty wine along this time. We could have performed a toast to your promotion."
        "Akira smirks at her sister's remark as she opens her can with a popping sound."
        aki "A toast, huh? Didn't take you long to get hooked on the grape."

        show lilly basic_smileclosed
        with chchange

        li "I will admit I like a glass every once in a while, but hooked is probably a bit of an exaggeration."

        show hisao cross_grin_uni
        with chchange

        "That remark causes Hisao and me to exchange amused glances. Both of us remember the occasions when Lilly invited us to share a glass of wine together during our time in the Satou summerhouse, her eagerness pretty apparent even then."

        show akira basic_smug
        with chchange

        "Akira doesn't miss our gesture and lets out a soft snicker at her sister's expense."

        show akira basic_laugh
        with chchange

        aki "Tell you what. We'll save the toasts until you get to Scotland, and I'll take you out for some truly tasty drinks."
        "This is the first time this evening that Lilly's upcoming trip to Scotland has been brought up."
        "Yesterday, after telling her mother she wanted to stay in Japan, Lilly promised to come over again in an attempt to bridge the divide between herself and her parents that was created over the last six years. Eager to hear more details, Hisao addresses Lilly."

        show akira basic_smile
        show hisao basic_speak_uni
        with chchange

        hi "So, you're really going back there for a little while, huh?"

        show lilly basic_smile
        with chchange

        li "Yes. I don't believe things are as black and white as me having to choose between sacrificing my life here or sacrificing the bond with my family."
        li "I hope I can do my part to repair the bond I used to have with my parents while I'm there and then maintain it through contact over the phone while I'm attending school here."
        hi "So do you have any idea when you'll be going? Vacation is about to start, and you don't travel to the other end of the world for just a few days, do you? You'd want to stay for at least two weeks."
        li "Akira has looked into the possibilities, and I'll be leaving on Saturday next week. I intend to stay for three weeks or so."
        "Three whole weeks. That's pretty much my entire vacation, seeing that I'll be attending those first aid courses during the entire upcoming week. I was really hoping to have some time during the vacation to spend with Lilly myself, but I guess it can't be helped."
        "It's not like she can visit her parents at any time she chooses. I suppose I should be glad she'll be here for the rest of the school year."

        show hisao basic_smile_uni
        with chchange

        hi "I hope you'll have fun there."

        show lilly basic_smileclosed
        with chchange

        li "Thank you Hisao. Do you and Hanako have any plans for the vacation?"

        show hisao basic_neutral_uni
        with chchange

        "Hisao and I share a quick look, and then we both shake our heads."
        hi "Not really. We've saved enough to go on a few dates, but other than that, I don't have any plans."
        ha "Me neither."

        show akira basic_sheepish
        with chchange

        "Akira gives us a sheepish grin in response."
        aki "We'd let you borrow the keys to the summer home, but unfortunately that place was sold around the time Lilly announced her departure to you guys, {w=0.5}{cps=10}sooooo…{/cps}"

        show lilly basic_planned
        with chchange

        "Lilly finishes her sister's sentence as if the two have been practicing the part."
        li "…we were wondering if you two would consider accompanying me to Scotland for a few weeks instead."

        show akira basic_ending
        show hisao cross_neutral_uni
        with chchange

        "Hisao and I exchange a puzzled glance, both of us trying to figure out if Lilly's serious or not. A round trip to Scotland is way beyond the budget of either of us, and Lilly must know that."
        hi "Err, Lilly… I'm not sure about the exact price of a plane ticket, but I'm positive they'd cost Hanako and me an arm and a leg. Not that we'd be hurting for potential buyers around here, but still…"

        show akira basic_laugh
        show hisao basic_smile_uni
        show lilly basic_giggle
        with chchange

        "Lilly, Akira and I all share a laugh at Hisao's remark, but then Lilly indicates that she likes to say something."

        show akira basic_smile
        show lilly basic_smile
        with chchange

        li "Intercontinental flights are never particularly cheap, but would you two be willing to come along if the costs were not a concern?"

        show hisao cross_speak_uni
        with chchange

        hi "What do you mean?"

        show lilly basic_smileclosed
        with chchange

        li "What I mean is that my family is willing to cover the costs of the flight for the two of you."
        "WHAT?"
        "I take a look at Hisao to see if his reaction is anything like mine, and his shocked expression tells me Lilly's announcement took him completely off guard as well."
        ha "B-but… H-how did you… W-why w-would they…?"

        show akira basic_laugh
        show lilly basic_giggle
        with chchange

        "The Satou sisters seem to have a lot of fun taking in our baffled reactions, and it feels like minutes until Akira speaks up, still grinning at the look of shock on Hisao's and my own face."

        show akira basic_sheepish
        show hisao basic_neutral_uni
        show lilly basic_smile
        with chchange

        aki "Well, you probably knew this already, but our family's pretty well-off financially. Heck, the sale of the summer home alone probably brought in enough money to invite half the school along if we wanted to. So the costs of the tickets aren't that big a deal here."
        aki "And Lilly's going to need someone to accompany her to make sure she boards the right plane at the right time. We could try and arrange for people from the airline to do that, but that's kind of a hassle."
        aki "Our folks would feel better if she's accompanied by friends instead who accompany her from Yamaku, through London Heathrow, all the way to Inverness Airport. Frankly, I would too."
        "That's a pretty good point. Lilly can get around Yamaku and the nearby town just fine and can even navigate the city with some effort, so I completely forgot about the fact that an airport would still be a daunting obstacle to her."

        show akira basic_boo
        with chchange

        aki "I would have liked to stay in Japan for another one and a half weeks and accompany her myself, but since I've already postponed my departure for a week, I can't afford any more delays."
        aki "Heck, the folks are probably already out for my blood enough as it is."

        show lilly basic_concerned
        with chchange

        "Lilly's smile drops for a moment."
        li "Was Father very upset?"
        aki "You know he has this thing about running a really tight ship. Me suddenly deciding to stay away for a week longer has messed up several people's schedules, and the person who's going to teach me the ropes might have to delay his summer break for a week."
        aki "If Dad had his way, I'd be over there already. I called my future colleague myself last week to apologize for the inconvenience, and he said it wasn't a problem."
        aki "Dad will just have to learn that not every inconvenience I cause creates a permanent blemish on our family's good name, and what he perceived as a major loss of face was actually a minor issue for the people concerned."
        "Akira shrugs."

        show akira basic_wistful
        show lilly basic_weaksmile
        with chchange

        aki "But I {i}will{/i} be under pressure to make up for lost time once I'm there, and I won't be in a position to take two days out of my schedule to fly over to Japan and pick up Lilly. Not during the impeding takeover."

        show lilly basic_surprised
        with chchange

        "I can see Lilly perk up at the last part of Akira's statement."
        li "Hmmm? A takeover? You've never mentioned that before. When did you hear about that?"

        show akira basic_boo
        with chchange

        aki "I didn't mention it before because it didn't seem relevant before. I've known about the plans for quite some time, even though this doesn't directly concern the Japanese branch of the company. Head office is planning to acquire a business similar to ours located in the United States."
        aki "They're in the middle of negotiations with that company's board of directors and with possible investors. Things are bound to get pretty hectic for them and for me, it seems."
        aki "While Mom said she and Dad are going to try their hardest to shuffle their schedule around to spend some time with you, I wouldn't count on getting to hang out with them 24/7—particularly not with Dad. Some additional company may be desirable from time to time."

        show akira basic_smile
        show lilly basic_satisfied
        with chchange

        "Lilly smiles her warmest smile at both of us."
        li "And no company could be more desirable than present company. For me, it would make the difference between a good vacation and a wonderful vacation."
        li "So, what do you think? Will you come to Scotland with me?"
        "I'm still trying to come to terms with Lilly's completely unexpected proposal. I shoot a quick glance at Hisao who turns to Akira."

        show hisao cross_speak_uni
        with chchange

        hi "Are you expecting a definite decision from us right now?"

        show akira basic_sheepish
        show lilly basic_weaksmile
        with chchange

        aki "I know it's sudden, but yeah, that'd be great. If you're not feeling up to it then no harm done, but then I'll have to arrange something else on a short notice."

        show akira basic_smile
        show lilly basic_smileclosed
        with chchange

        aki "If you are, I'll be able to make all the necessary arrangements while I'm at the airport tomorrow. There's a lot of work piling up on my desk on the other side of the world as we speak, and I'd like to get this thing over and done with before I get there."
        "I start feeling a bit uneasy by the sudden pressure to make such a big decision here and now, but Hisao turns to me with an excited smile on his face."

        show hisao cross_smile_uni
        with chchange

        hi "Hey Hanako, what do you say? Want to go on vacation to Scotland together with Lilly and me?"
        "It sounds like one of us has already decided."
        "This would be the first time for me to travel this far away from home. I've never even been out of the country before, and now we're given the opportunity to literally travel to the other end of the earth, to stay in an unfamiliar place."
        "The Satous' summer home in Hokkaido was also unfamiliar at first, but that was just the three of us. Now we'll be staying with other people, in a country with a completely different culture and a language I don't speak fluently."
        "And before we get there, we'll have to travel through several crowded airports, including one of the busiest airports in the world."
        ha "Um… well…"
        "But then again, ever since I joined the newspaper club, I've been playing with the thought of studying journalism. I'd never be able to stand in front of a camera or push a microphone in someones face, but I think I'd like the writing aspect of it."
        "But what would I write about if I'm too nervous to go and explore the world beyond my familiar little room? If I can't even visit an unfamiliar place with my two closest friends by my side, I'd probably be best off seeking another educational road altogether."
        "If anyone can ease my nerves, it's Lilly and Hisao. And I think I'd genuinely enjoy taking a vacation with the two most important people in my life."
        ha "I…I think I'd l-like that."

        show akira basic_ending
        show hisao cross_grin_uni
        show lilly basic_cheerful
        with chchange

        "The three dazzling smiles I get in return to my answer confirm I made the right decision."

        stop music fadeout 3.0

        scene black
        with Dissolve(3.0)

        if _in_replay:
            return

    return