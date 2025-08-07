label sh_ch34:
    label .s1:

        $ set_window_tint(TINT_HANAKO)

        scene bg satou_stairs
        with shorttimeskipsilent

        play music music_dreamy fadein 4.0

        play sound sfx_doorknock2 volume 0.5

        ha "L-Lilly?"
        "Upon receiving no response to my knocking, I hesitantly open the door of my friend's room and look inside."

        play sound sfx_dooropen

        scene bg satou_guest2
        with locationchange

        "Surprisingly enough, there's nobody there. That's a bit unexpected. Lilly's hardly been out of her room for days, except to eat dinner. Where could she be?"

        play sound sfx_doorclose

        "Just as I close the door, I hear the sudden sound of something clattering on a tile floor."
        "Unless Hisao just had a moment of clumsiness in the shower area of our bedroom, the sound I just heard probably came from the bathroom."

        scene bg satou_changingroom
        with locationchange

        "I walk up to the door of the bathroom, gently push down the door handle, and discover that it's not locked."
        "I peek inside and notice that Lilly's sandals are on one of the shelves, and I hear some movements from behind the changing area's inner wall. Lilly's definitely in here."
        "I take off my shoes and socks and put them next to Lilly's sandals on the shelf."

        scene bg satou_bathroom
        with locationchange

        "I walk into the bathing area, and sure enough, Lilly's kneeling near the small shelves underneath the mirrors."

        show lilly back_surprise at twoleft
        with charaenter

        "There are several bottles and flasks around her, and Lilly's sweeping the ground with her hands in an attempt to locate them all."

        show lilly back_listen
        with chchange

        "She suddenly stops and tilts her head as I approach, probably having picked up the pattering sound from my bare feet on the tiles."
        ha "Lilly?"

        show lilly back_smileclosed
        with chchange

        "A tiny smile appears on her face as she recognizes my voice."
        li "Oh, welcome back, Hanako."
        ha "Uh... Did you drop a few things, Lilly?"

        show lilly back_giggle
        with chchange

        "Lilly sheepishly nods."
        li "I wanted to put some bathing supplies on the little shelf in front of me, and I discovered too late that someone still left his or her own supplies in that exact spot. The result is this little mess."
        ha "Oh... uh..."
        "I think I have a good idea of who created this little inconvenience for Lilly."
        ha "S-sorry, Lilly. That m-may have been me."
        "Hisao and I took a bath together the day before Lilly's father had his incident. I meant to clean up after ourselves afterwards, but we got... distracted by other things while we were here."

        show lilly back_smileclosed
        with chchange

        li "It's not a problem, Hanako."
        ha "Let me help you."
        "I walk up to Lilly and quickly pick up the bottles and flasks around her. I take one of each and neatly arrange them on the shelf near her."
        ha "Lilly? I arranged the bottles on the shelf in front of you in the... uh... usual order."

        show lilly basic_smileclosed
        with chchange

        "Lilly gives me a grateful smile."
        li "Thank you, Hanako. Your thoughtfulness is greatly appreciated."
        ha "So, Lilly, were you planning to take a bath just now?"

        show lilly basic_weaksmile
        with chchange

        li "That was the idea, Hanako. I've only taken a bath once during this trip, and the circumstances were less than ideal back then."
        li "Maybe a pleasant soak will help to ease my mind. There should still be plenty of time before dinner."
        ha "I suppose I... came at a bad time then. But... do you have some time to spare... after dinner?"

        show lilly basic_smile
        with chchange

        li "I do. Do you have any plans, Hanako?"
        ha "Not really. I just thought... after tomorrow... we won't see each other again for some time. Maybe we could... spend some time together until Hisao and I leave?"

        show lilly basic_weaksmile
        with chchange

        li "That sounds like a good idea, Hanako. I apologize for having neglected you and Hisao over the last few days."
        ha "That's okay, Lilly. There's no need to explain anything. We understand completely."

        show lilly basic_smileclosed
        with chchange

        li "I'll be sure to keep you and Hisao company after dinner this evening. Let's make the most out of your remaining time here."
        ha "Um... Lilly?"
        li "Yes?"
        ha "M-maybe... the t-two of us could spend some time... together? We could... talk for a bit, if you like. I'm sure that Hisao... wouldn't mind."

        show lilly basic_surprised
        with chchange

        li "Are you sure about that, Hanako?"
        ha "I... haven't really done a very good j-job s-supporting you, but... maybe I can still do that for the little bit of time I'm here."

        show lilly basic_weaksmile
        with chchange

        "Lilly looks in deep thought for a moment. Then, she gives a small nod."
        li "I... would probably welcome that, Hanako."
        ha "G-great."
        "Lilly gets up, and I allow her to take hold of my sleeve before helping her return to the changing area."

        scene bg satou_changingroom
        with locationchange

        "She then feels her way over to one of the baskets on the shelves and starts taking off her blouse. I figure that this would probably be a good time to take my leave."
        ha "Lilly, if you don't need my help for anything else, I'll b-be going, okay?"
        li "Hmmm, Hanako?"
        ha "Yes?"
        li "You... said that you wanted to spend some time alone with me, didn't you?"
        ha "Yes."
        li "Perhaps we should take the opportunity to do that now. It's not like we have that much time left."
        ha "Huh?"
        li "If you were to stay here right now, you could keep me company."
        "I give Lilly a baffled look as she takes off her skirt."
        "Keep her company?"
        ha "Uhhhhhhh.... Is t-that okay?"
        "Lilly, who is now wearing nothing but her bra and panties, gives me a playful look."
        li "Why wouldn't it be?"
        ha "You'd b-be... n-naked... in f-front of me."
        "Lilly giggles."
        li "We're both girls, aren't we? I don't think it'd be that big a problem."
        ha "If it's... not a big p-problem with you then... I'll stay here."
        li "I appreciate that, Hanako."

        # TODO Play lock door SFX

        "I quickly walk to the door and lock it."
        "When I turn around, Lilly has already taken off the last of her clothes and is brushing the shelf with her hand in search of a towel."
        ha "I just l-locked the door, Lilly."
        li "Could you help me to my stool, Hanako?"
        ha "Sure."
        "Averting my eyes, I place Lilly's outstretched hand on my arm and lead her out of the changing area."

        scene bg satou_bathroom
        show lilly behind_smile_nak at twoleft
        with locationchange

        "But before we reach the corner with the mirrors and the stools, Lilly suddenly stops."
        li "Hanako, what will you do?"
        ha "I'll just sit on the edge of the bath."

        show lilly behind_smileclosed_nak
        with chchange

        "Lilly nods but doesn't move or say anything. I wonder what she's thinking right now."
        li "Hanako... I apologize if this seems a bit forward, but... I wouldn't mind if you joined me. Would you like to?"
        ha "W-w-what?"

        show lilly behind_giggle_nak
        with chchange

        "Lilly seems to have expected my shocked reaction and shows me an amused smile."
        li "If you wouldn't mind, that is. You and Hisao took a bath several days ago, didn't you? Didn't you like it?"
        ha "I... uh... d-did."

        show lilly behind_smileclosed_nak
        with chchange

        li "To be honest, I had been hoping for a chance to take a soak together with you since we came here. I don't see us visiting a hot spring resort or anything like it anytime soon in Japan. Maybe this would be a good opportunity."
        ha "Ah... r-really?"
        "Lilly nods."
        li "It's also easier to talk to each other when you're sitting next to me instead of half-way across the room. And as you may have noticed yourself, the bath is a bit on the large side for just one person."
        li "It seems to have been built with group activity in mind. Or rather, family activity."
        ha "F-family activity?"

        show lilly behind_reminisce_nak
        with chchange

        li "Yes, bathing was very much a family activity back in the days. I used to take baths with Mother and Akira all the time when I was young. Occupying such a large bath on one's own feels... off somehow."
        ha "If it's a f-family activity to you, then..."
        "Lilly quickly shakes her head before I can finish my sentence."

        show lilly behind_smileclosed_nak
        with chchange

        li "Then sharing a soak with you would definitely not feel inappropriate to me. You... feel very much like family to me right now, Hanako."
        ha "L-Lilly..."
        "I can't help but smile at Lilly's kind words. Lilly's expression quickly saddens though."

        stop music fadeout 2.0

        show lilly behind_reminisce_nak
        with chchange

        li "In fact... You may feel more like family to me right now than... anyone else I know."
        "The impact of that statement isn't lost on me, and I reel back in shock for a moment."
        "This isn't something I ever expected Lilly to say. Are things really this bad?"
        "This would probably be a good moment to try and put my shyness aside and focus on more important things."
        "If Lilly really feels this way, then is it okay for me to be flying back tomorrow? Shouldn't I stay and be there for Lilly, instead?"
        "I'd best take this one step at a time, though."

        play music music_serene fadein 4.0

        ha "Ummm... I'll... j-join you, then. O-okay? I'll b-be r-right with you."

        show lilly behind_smileclosed_nak
        with chchange

        "Lilly gives me a relieved smile."
        li "Thank you, Hanako."

        scene bg satou_changingroom
        with locationchange

        play sound sfx_rustling

        "Still a bit uneasy, I walk back into the changing area and nervously start undressing."
        "While I'm busy doing so, Lilly doesn't say a single word and the only sound audible in the room is the rustling of my clothes."
        "I eventually take off my underwear, pick up a towel, and with my shaking legs, walk out of the changing area to face Lilly."

        scene bg satou_bathroom
        show lilly behind_smile_nak at twoleft
        with locationchange

        "I blush a bit at the sight of her as we come face to face. Lilly isn't even bothering to try and cover herself up. She just casually stands there as if she was fully clothed."
        "As my eyes briefly wander over Lilly's body, I feel the painful sting of envy for a moment."
        "Lilly is gorgeous. Her vibrantly blonde hair is hanging loosely over her shoulders, her figure is slim, and yet her curves are ample. And her skin is both smooth and spotless. It makes the condition of my own blighted skin all the more jarring."
        "I'd better move on with things before I get depressed."
        ha "Lilly... could you h-hold out your right h-hand?"

        show lilly behind_smileclosed_nak
        with chchange

        "She calmly extends her hand towards me, which I place on my left arm."

        hide lilly
        with charaexit

        "I guide her to the stools while at the same time keeping a bit of additional distance between us so she can't accidentally touch any of my scarred areas. When we sit down, I also make sure that my stool isn't too close to hers."
        "I get a bit of a weird feeling when I pick up one of the shower heads, but then shake the sensation out of my mind and dutifully fill both Lilly's bucket and my own."

        # TODO play washing SFX

        "We quietly proceed to drench ourselves, soap ourselves up and then wash ourselves."
        "I feel a bit bad about not offering to wash Lilly's back, but I'm a bit afraid of doing so since I know she'd offer to return the favor, and me declining it would just lead to another awkward moment."
        "It takes me quite a while to get my hair over and done with, and when I finally rinse the remaining shampoo out of my hair and look at Lilly, I notice she's been absentmindedly toying with her bangs. I wonder how long she's been waiting without saying a word."
        ha "Lilly?"

        show lilly behind_smileclosed_nak at twoleft
        with charaenter

        li "Hanako, are you finished as well?"
        ha "Y-yes. Sorry to keep you waiting. My hair usually takes a little while."
        li "Almost everyone I know says you have very beautiful hair, Hanako, so it goes without saying that it's important to take good care of it."
        ha "Ah... oh.... R-really?"

        show lilly behind_giggle_nak
        with chchange

        "Lilly merely grins."
        li "Really. Are you ready? I must admit I'm getting a bit chilly."
        ha "Okay. C-could you give me your right hand again?"
        "I take Lilly's hand again and guide her to the large bath."

        hide lilly
        with charaexit

        "I help her step in, then get in myself and start considering where to sit. Lilly doesn't seem to have much trouble picking a spot as she walks up to one of the corners, turns around, and beckons me to sit next to her."
        "I hesitate. If Lilly sits down in that corner, I'll have to sit on her left side and my scarred side will be facing her."
        "Maybe it'll be okay if I simply don't sit too close to her. I can't offer support to Lilly and then appear to be distant. I'll simply sit just far enough away to avoid accidental physical contact."
        "I make my way over to Lilly, and we allow ourselves to sink slowly into the water."

        scene ev sharedsoak_lilly_relax
        with mediumflash

        li "Aaaaaahhhhh..."
        ha "Hmmmm..."
        "We both let out a long sigh as we make ourselves comfortable, and the water fills our bodies with a pleasant warmth. Then, we both giggle."
        li "The water feels good, doesn't it?"
        ha "Yes, it's just the right temperature."
        "It feels like the water is still set at the temperature Hisao and I picked when we took a bath here. I'm happy that Lilly likes this temperature too because a bath is quickly too hot or too cold for me."
        "..."
        "For a long time neither of us says anything, and we are content to just hang back and relax."
        "..."
        "Eventually though, Lilly breaks the silence."

        show ev sharedsoak_lilly_lillysmile
        with charachangeev

        li "So, Hanako... How was the visit to the hospital?"
        ha "When we arrived, we briefly saw your mother and a person who just arrived here from Japan. Akira said he was the manager of the Japanese branch. Then, we went to s-see your father and... umm..."
        "I hesitate for a moment. I don't think Lilly needs to hear about Akira's verbal scuffle with her father."
        ha "...he... uh... still seemed to have a lot of difficulty speaking, but he talked to us, even though it hurt."
        ha "He... thanked us for helping him and said to l-let him know if there was ever something he could do back. Then, he wished us a safe journey."
        li "I see."
        li "Did... Akira say anything in particular? When Hisao came back upstairs, he said that she invited you for a stroll along the shore."
        ha "She... wanted to spend some time with me before I leave tomorrow. She wasn't sure when we'll meet each other again, after all."
        "She's also worried about you, but I don't think I should let that one slip. I don't like being so secretive, but if Lilly mistakenly believes that I'm only here because Akira sent me, she might clam up."
        li "That makes sense."
        ha "...Lilly?"
        li "Yes, Hanako?"
        "Maybe I should ask her straight out."
        ha "W-what d-did you mean when you said that... I f-felt more like f-family than anyone else? D-did you... mean that?"

        stop music fadeout 2.0

        "Lilly doesn't immediately answer. I briefly wonder if she's just going to smile and dismiss the whole thing."
        "But then she sighs softly."

        queue music music_moonlight fadein 4.0

        show ev sharedsoak_lilly_lillyspeak
        with charachangeev

        li "After Mother and Father left Japan, I've been telling myself for a long time that this was only temporary and that when they'd return, everything would be as it was before. But when Akira and I visited here in July, I think everyone could feel the distance."
        li "When I offered Mother to visit here, I thought all that we needed to do was spend a bit more time in each other’s company. But... I've recently started feeling that things are nowhere that simple."
        li "If anything, I feel that this trip has merely widened the distance between myself and the rest of my family. It's like all my efforts have the opposite effect. It's... very disheartening to say the least."
        ha "Widened the distance?"
        "Lilly nods."
        li "You've known Akira for some time now. Surely you must have noticed as well."
        "I think I have, even before Akira herself pointed it out to me."
        ha "Akira... really doesn't get along with your p-parents, does she?"
        li "Akira and I have always been very close and only grew closer after our parents left Japan. We used to be able to share everything with the other. Only the subject of our parents has always been a troublesome issue."
        li "Akira would usually get angry or bitter whenever this subject came up, so I'd usually let her blow off steam and then change the subject. It didn't really become a problem until recently."
        ha "Until... the summoning?"
        li "Even slightly before that. When we visited Scotland in July, I didn't really know how to act around our parents, but I tried to just make the best of an awkward situation."
        li "Akira, however, would often be either distant or hostile whenever we interacted with them. It made the situation with the summoning a lot more difficult for me than it already was."
        ha "How so?"
        li "In the past, whenever I ran into a situation I had trouble dealing with by myself, such as... hmmm... turning down a confession or dealing with conflicts in the student council, I would take comfort in the fact that I could always approach Akira as a last resort."
        li "She'd always listen to me and give me sisterly advice. But when we visited Scotland, I started feeling alienated by Akira's attitude towards our family."
        li "I used to trust her opinions unconditionally because I knew she always had my best interests at heart. But in this case, I can't deny that I felt a sense of distrust towards her."
        li "So I ended up trying to deal with our parents' summoning on my own. I felt... very alone... in that."
        ha "Oh, Lilly..."

        show ev sharedsoak_lilly_lillysmile
        with charachangeev

        "Lilly gives me a guilty smile."
        li "Of course, that's a little bit my own fault as well. I should have realized sooner that I also had you to confide in. I just hope you understand that usually what happens in the family is meant to stay in the family."
        ha "I understand."

        show ev sharedsoak_lilly_lillyspeak
        with charachangeev

        li "I had been hoping that Father's hospitalization would have resulted in a truce or even a new start, but it seems that even an event as major as this wasn't enough. I'm not really sure how to deal with Akira now."
        "For a moment Lilly looks mildly frustrated."
        li "I... really want to be understanding of Akira. She's endured a lot of hardships of her own. But... {i}*sigh*{/i} what kind of person starts a fight with someone who only just got off life support?"
        "And today was pretty much a rematch of the confrontation Lilly referred to."
        ha "It... is indeed a bit harsh."
        li "Of course, Father is hardly blameless himself. He took an unacceptable risk. And... when he mentioned that he did it for Akira and me, it almost made me feel partially responsible for what happened."
        li "As if having him in my life is somehow less important than a large sum of money in the bank."
        "She sighs again."
        li "I keep thinking back on what he said. About wanting to make sure I'd always be ‘well-provided for’. I wonder if I'm a bad person for believing that that's a really condescending thing to say."
        ha "I don't think you are."
        li "Now I just keep wondering if that's how he's always seen me. I keep wondering if the biggest achievement he expects out of me is to be noticed by some potential husband so I don't end up living off his money by myself."
        li "I wonder if he'd laugh off my dreams of becoming a teacher. If he's not willing to pay any university tuition, there's probably not much hope of me getting into a university after I graduate."
        "Wow, she's really in a downer mood."
        ha "It's p-probably a little early to w-worry about that already."
        li "Hanako... Do you think I'm an ungrateful daughter for feeling this way?"
        ha "N-no. I'd probably f-feel a little bit offended, too."
        li "That's somewhat of a relief to know."
        "Lilly thinks for a moment."
        li "I'm also not sure what to think of what Akira said about the way Mother and Father live their lives. Especially Mother."
        li "To be honest... I'm not really sure what to think of her to begin with."
        ha "I... noticed that things sometimes seemed a little awkward between your m-mother and you, but I didn't really understand why because your mother has been very friendly from the start."

        show ev sharedsoak_lilly_lillysmile
        with charachangeev

        "Lilly nods and smiles sadly."
        li "It's probably just me. But even so..."
        ha "I... don't really understand the problem."
        "Lilly turns to me."
        li "Hanako, if you don't mind me asking... What do you think about my mother?"
        ha "Huh?"
        li "Please just give me your honest impression. Surely you must have come here with certain expectations."
        ha "Hmmm. She was... different from what I was expecting, but she was nevertheless very nice. I think I like her."
        li "May I ask what exactly you were expecting?"
        ha "I think I was expecting to meet an older version of you. Like... a formal and graceful upper-class woman with impeccable m-manners. Maybe, unlike you, even a bit haughty or s-snobbish. I know it's a bit silly."
        ha "But your mother actually reminds me quite a bit of Akira. I think I simply made the wrong guess."
        li "You were expecting a so-called proper lady?"
        "I think I’ve heard Lilly's father utter that phrase a few times."
        ha "Yes. But it doesn't really matter that much to me. Why do you want to k-know all this?"

        show ev sharedsoak_lilly_lillyspeak
        with charachangeev

        "Lilly pauses for a second and then sighs."
        li "Because the way you imagined her is also the way I remember her."
        ha "The way you remember her?"
        li "I know it must be difficult for you to believe this, but Mother was a completely different person when she was still living with us in Japan."
        li "She was... graceful, gentle, friendly—though also just a little bit distant—and always very proper and appropriate. And she was completely devoted to Father and the family. While growing up, Mother was the person I always tried to emulate and resemble."
        ha "R-really?"
        li "Being around her has been a very strange experience. I... have no idea how to act around her. Living abroad can change a person, I suppose, but..."
        "It's still very odd. And something doesn't make sense."
        ha "But Lilly, what about y-your first trip?"
        li "During our first trip to Scotland, Mother took up her days off from work to spend time with her bedridden sister and us. Back then, she was still acting like her old self whenever she was with us. Well, for the largest part, anyway."
        li "She didn't start acting this casual until I returned here."
        "Lilly lets out an unhappy sigh."
        li "I could put up with the more casual way of interacting with me, but what really bothers me is the fact she seems to have been neglecting Father. That's... just so not her."
        li "I... really don't know what to think or what to do. This isn't the family I expected to find here."
        ha "I... I'm sorry, Lilly."

        show ev sharedsoak_lilly_lillysmile
        with charachangeev

        li "It's okay, Hanako. Thank you for listening to me complaining like this."
        ha "Oh, d-don't worry about that."
        li "What would you do in my situation?"
        "I'm not sure. Knowing myself, I'd probably run away, take the first plane back to Japan, and hide away in my dorm room for the rest of the year. But that's not what Lilly needs to hear."
        "Okay, Hanako. Think..."
        ha "I'm... n-not really sure, but..."
        "I try to recall the things Akira told me earlier today."
        "She said something along the lines of not wanting to trouble Lilly with her issues any further."

        show ev sharedsoak_lilly_hanakospeak
        with charachangeev

        ha "Akira... umm... talked to me earlier and... she's not happy with the situation either. She said... she was going to try and b-back off a little. I don't think there's a lot you can do for her. This is probably something she'll have to... sort out herself."
        li "Did Akira appear angry with me over our lack of interaction the last few days?"
        ha "Not to me. Maybe you can call her. Or spend some time with her after work without bringing up your f-family. I think she'll like that, and you might enjoy it too. You've always enjoyed each other's company so much."
        li "It may feel odd to ignore the elephant in the room just like that, but if she meant what she told you, then there may be no harm in trying."
        "Akira isn't the tricky issue though. Lilly's bond with her sister is strong enough for it to withstand a few hurdles. The issues with her parents are more difficult. I can imagine how Lilly must have felt. I think I've been there myself."
        ha "L-Lilly?"
        li "Yes?"
        ha "I... I think I know how you must have felt."
        li "You do?"
        ha "When I was... still getting to know Hisao, I used to worry a lot about what he thought of me. I was often afraid that he looked d-down on me. That I was j-just someone for him to worry over."

        show ev sharedsoak_lilly_lillygrimace
        with charachangeev

        "Lilly suddenly looks very uncomfortable. This used to be a sensitive point between the two of us as well."
        li "I don't think that was all he saw you as, Hanako."
        ha "I don't know. I still remember that night when Akira took us to that jazz club. Hisao and I played a game of pool in the back and it was really fun... until he said something to me that r-really hurt."
        li "He did?"
        ha "While I was trying to ease my nerves, he said: ‘Don't worry. Even with Lilly away, I'll be there to protect you.’"
        ha "It was then that I realized that... to him... I was just a pitiful and helpless person who couldn't do anything on her own. Someone who would always have to b-be looked after."

        show ev sharedsoak_lilly_hanakospeak
        with charachangeev

        li "I don't think he really meant it like that, Hanako. He may have acted in a bit of a misguided manner, but in the end, I believe he meant well. He simply didn't know you well enough yet."
        ha "I... think he meant well t-too, but it still hurt back then. I wanted him t-to respect me, b-but he didn't."
        li "I think he respects you now. And I think he also loves you very much. So he obviously came around, wouldn't you agree?"
        ha "Y-Yes, it... took a lot, but... he came around eventually. And he apologized and c-confessed to me. I'm r-really happy that he did."
        li "Was there anything specific that triggered this?"
        "I blush briefly upon hearing Lilly's question."
        "I think if I told Lilly that I let Hisao sleep with me in order to make him come around, she'd probably faint in shock."
        "Actually, in the end it wasn't really Hisao and me taking each other's virginity that broke down the walls between us, but the painfully awkward talk we were forced to have the day after."
        ha "A... um... painfully awkward talk at some point. It's n-not really important."

        show ev sharedsoak_lilly_lillysmile
        with charachangeev

        li "I think you're right, Hanako. The important thing is the result."
        ha "Umm... L-Lilly?"
        li "Yes?"

        show ev sharedsoak_lilly_hanakospeak
        with charachangeev

        ha "I was thinking... maybe... maybe the same is true with you and your father. Maybe your father... didn't really mean to d-disrespect you, but... he s-simply didn't know you well enough yet either. Maybe he's simply... ignorant."
        "There's a long silence as Lilly ponders my words."
        li "Do you really think the two cases are similar, Hanako?"
        ha "I... think so. I think your father cares about you in his own way or he w-would not have offered to take us to Edinburgh while things were still so busy at work."
        ha "M-maybe if you show him how strong and reliable you can be, he'll see past his current view of you."
        "In fact, you'll probably pull it off without jumping into the kind of irrational actions I took part in."
        li "Show him?"
        ha "I think this is a good opportunity. Maybe... the best chance you're going to g-get. Your f-father is probably going through a very d-difficult time right now. He could... really use someone like you by his side."
        li "Someone like me?"
        ha "You're... very good at... comforting people and making them f-feel better."
        ha "Giving emotional support to people who need it, whether they're classmates or newly arrived transfer students, or even p-panicky neighbors with whom you never even spoke before, is simply what you do. It's like a s-second nature to you."
        ha "It was... the first thing I learned about you."

        show ev sharedsoak_lilly_lillysmile
        with charachangeev

        li "That's a very nice thing of you to say."
        ha "If you... look after your f-father like you've looked after Hisao and me, he'll have no choice but to respect you."
        li "You make it sound more simple than it probably is."
        "I probably do. Lilly's pride was hurt in this whole mess, and I know that that's not something she can easily let go or overlook."
        ha "If anyone can bring your f-family together, it's probably you. Also... I think if you give things your all while you're here, you can say that you've t-tried your best no matter what happens during the rest of your stay."
        ha "If you... don't do that, then you might feel regrets when you're back at Yamaku."
        "I wonder if I myself would be able to practice what I'm preaching right now. I feel a bit hypocritical talking to Lilly about swallowing her pride and reaching out to her parents in good faith while I myself am frequently prone to bouts of cynicism."
        "But there's no doubt in my mind that if Lilly just allowed things to stay the way they are, she'd feel awful about her inactivity later."

        show ev sharedsoak_lilly_hanakospeak
        with charachangeev

        li "Maybe..."
        ha "You... d-don't really have much to lose. If you... m-manage to still get closer to your f-family, you'll have achieved what you c-came here for."
        ha "And if... despite your best efforts, you s-still feel distant f-from them b-by the time you get back, then... uh... ummm..."
        li "Yes?"

        stop music fadeout 2.0
        queue music music_friendship fadein 4.0

        ha "Then... uh... I'll b-be your f-family... instead. Either way, you w-won't be alone."

        scene ev sharedsoak_lilly_shoulder
        with charachangeev

        "Lilly lets out a happy laugh at my remark."
        li "Hmmm, hmmm... Promising someone such a reward for failing is not a good way to motivate them, Hanako. But nevertheless, I really appreciate your kindness."
        ha "Also... uh... This is just m-me, but I t-think that...!"

        stop music fadeout 0.2

        show black
        with Dissolve(0.2)

        "While I'm still in the middle of my sentence, I suddenly become aware that Lilly has softly put her hand on my shoulder."
        "{i}My right shoulder!{/i}"

        play music music_rain

        "I gasp and in a sudden fit of panic, I lunge forward in an attempt to get away."

        # TODO play splash SFX

        hide black
        show ev sharedsoak_lilly_lunge:
            yalign 0.5 zoom 1.02
        with vpunch

        "However, due to the resistence of the water reaching to just above my knees, I promptly fall over, producing a loud splash in the process. In other circumstances, it'd probably be comical."
        "The splash gets some water in my nose, and I snort and cough a few times before I can regain my composure."
        "I finally calm down enough to realize that I just made an utter fool of myself in front of Lilly and anxiously look over my shoulder at my friend."

        show ev sharedsoak_lilly_recover
        with charachangeev

        "Lilly's smile has vanished and in its place is a worried, almost frightened, expression."
        li "H-Hanako! Are you alright?"
        ha "I... I'm... okay... S-sorry... I'm... alright..."
        "My panting and stammering attempts at reassurance don't do much to put Lilly's mind at ease."
        li "Hanako, did I hurt you just now?"
        ha "D-don't worry. You didn't."
        li "Honestly?"
        ha "I... I d-didn't even f-feel it at f-first. S-several of m-my... m-my s-scarred places are n-numb."
        li "..."
        ha "It's o-okay, really. You j-just startled me a little."
        "Lilly seems to consider it and then slowly nods."
        li "I apologize. What was it that you wanted to say before I interrupted you?"

        stop music fadeout 2.0

        scene ev sharedsoak_lilly_hanakospeak
        with charachangeev

        "Having recollected myself, I return to my spot next to Lilly and swallow a lump in my throat before replying."
        ha "What I w-wanted to say was... that s-supporting your father is also simply the r-right thing to do. B-being stuck in the hospital after s-surgery is hard on everyone."
        ha "Your f-father probably f-feels he can't show it, b-but I think that d-deep down, he's feeling a little bit l-like Hisao m-must have felt. Or..."
        "An uneasy feeling starts welling up in my stomach before I can finish my sentence, but Lilly seems to have guessed what I was about to say."
        li "Or how you must have felt... Does this situation remind you of your own hospitalization, Hanako?"

        play music music_hanako fadein 4.0

        show ev sharedsoak_lilly_historyspeak
        with charachangeev

        ha "B-being stuck in the hospital after s-something like this is a very miserable experience. In addition to the p-pain, there's the loneliness."
        ha "And there's all the t-time you have. S-so much time—too much time—and nothing to s-spend it on except w-wondering."
        ha "W-wondering why t-this happened to y-you and what you d-did to deserve t-this. Wondering what y-your life will b-be like afterwards and r-realizing it will probably never b-be the same again."
        li "Was that what it was like for you, Hanako?"
        ha "I... d-don't really remember m-my own first week very well. I... w-was on very heavy medication at first. The strongest they had. M-my room was one of those s-sealed pods that w-was completely s-sterile. I b-barely survived the f-fire."
        ha "They s-said a s-simple infection could kill me until m-my injuries healed up a bit more. They usually c-couldn't b-bring in toys or b-books because there could be g-germs on them."
        ha "D-doctors or nurses wouldn't c-come in unless really necessary and I w-wasn't allowed out of the r-room. But then again, I c-could barely move b-back then, so I wouldn't h-have been able to leave anyway."
        li "That must have been terribly lonely..."
        ha "I preferred to b-be alone, eventually. Whenever the n-nurses came into my room, it was usually to change the b-bandages or to move and s-stretch my injured arm and b-back."
        ha "Burned skin becomes really t-tight and it has to be s-stretched several times a day or I wouldn't be able to use those p-parts of my body at all anymore, eventually. That's what they s-said. But... I didn't s-see it that way at first."
        ha "All I knew was that several t-times a day, p-people would come into my room to cause me terrible pain."
        "For a moment my thoughts fly back to my time in the hospital. The constant pain that became unbearable when my limbs were moved or the wound dressing was changed."
        "The fear and panic I felt when I saw the nursing staff enter my room again. Their continuing reassurances how important it was to start these exercises as soon as possible."
        "I suddenly find myself shivering."
        li "Hanako..."
        ha "S-sometimes, after the nurses w-were finally done f-for the day, I w-wondered why my m-mother did what she d-did. Why she didn't j-just let me..."
        li "Your mother?"
        ha "The fire happened when I was eight years old. It was night, and I was s-sleeping when it started. I... curled up into a ball... when the f-fire swept over me."
        ha "My mother... tried to shield me. Th-that's the reason... I lived... and she... d-didn't."
        li "..."
        ha "I was... still on intensive care... f-fighting for my own l-life when the... c-c-cremation took place."
        ha "M-maybe it w-was for the best. If... If I h-had been there when they... when they... I d-don't think I w-would have... "
        "I sniffle and it takes all the willpower I have to swallow the sudden lump in my throat, and when Lilly speaks up, her voice is rather tiny as well."
        li "H-Hanako... your parents' ashes... are they... kept at a grave somewhere? Because if so... perhaps I could go there with you some time and pay my respects."

        show ev sharedsoak_lilly_historysmile
        with charachangeev

        "That comment makes me smile despite the mood of the moment. It's just so much like Lilly to say something kind like that."
        ha "Th-they're not. The funeral w-was already very costly, and it w-was decided not to s-spend additional money on a grave with just m-me to maintain it."
        ha "After I... recovered enough to be able to walk and d-dress myself again, the m-matron came to visit m-me in the hospital. She told me she worked at an orphanage in t-town and that I'd be living with them from then on."
        ha "They... kept my p-parents' ashes while I w-was recovering in the hospital, and after I was allowed to l-leave, we took a long ride to a place n-near the ocean with a really b-beautiful coastline."
        ha "The matron s-said I could pick the prettiest spot I could f-find and that's where we would... s-s-see them off."
        li "She sounds kind."
        ha "She w-was. All the staff members at the orphanage w-were nice, and it felt a bit like Yamaku does. But the staff was also always b-busy."
        ha "Since they w-were already h-helping me with my... exercises and other m-medical needs, I t-tried not to burden them further. The place had a small library, so I started reading to p-pass the time."
        ha "S-sometimes I'd play a game with one of the other c-children if the staff suggested it."
        li "Did you ever consider getting in touch again with some of the children you got to know there?"
        ha "I didn't r-really get to know anyone. The other c-children didn't really t-talk much to me, and I didn't r-really talk much to them. I... d-didn't really mind."
        li "But you were all in the same boat, weren't you?"

        show ev sharedsoak_lilly_historyspeak
        with charachangeev

        ha "I'm n-not sure. As th-the years went on, I realized... I was different. M-most of the children there were up for adoption, just like I was. But unlike me... they gradually left, o-one by one."
        ha "By the time I went to Yamaku, I was... among the oldest ch-children there. For a while, I h-helped with some of the y-younger children, but... I n-never really got to know them either."
        li "That must have been very lonely."
        ha "I d-don't like interacting w-with p-people very much, so I didn't m-mind."
        li "But everybody needs friends, don't you think so?"
        ha "Friendship... was something I thought I'd g-given up on. I s-stopped believing in others... after what happened after the accident... B-before my accident happened, I got on well with p-people and other children."
        ha "I d-didn't have many friends, but... I didn't m-mind. I t-treasured the ones that I had. Afterwards, though..."
        "I swallow with some difficulty. For some reason just the mere mentioning of this brings back fragments of the desperation I felt back then."
        ha "...I was c-called names by the others and t-teased a lot. It hurt... really deeply. The teachers t-tried to help s-sometimes, but they c-couldn't do much, and even many of them r-recoiled just at the sight of me."

        show ev sharedsoak_lilly_historycry
        with charachangeev

        ha "Among t-those c-calling me names and t-teasing me... were the ones that I t-thought were m-my closest friends."
        ha "{i}*sniff*{/i} Up to that point, I had been hoping I c-could still maintain... just a little bit of m-my former life, but... it was then that I r-realized that my former life was truly gone for good."
        "I feel a few tears flow down my cheek, and I see them create small ripples as they hit the surface of the water."
        ha "Middle school... was even worse. I g-got bullied... a lot. I was c-called names and got excluded f-from work groups. There were... worse things, too. Especially when tests came up and p-people started f-feeling pressure."
        ha "I s-started skipping class. I knew I wasn't s-supposed to... M-my grades were already r-rather low, but... I became more and more f-frightened to go there each day."
        ha "After m-middle school, Yamaku was one of the options the s-staff brought up. It was... isolated and m-most students there were d-disabled. I d-didn't expect to m-make any friends there, but... at least p-people would leave me be."
        ha "That was... g-good enough for me. That was… even m-more than I c-could hope for."
        "I rub my eyes a few times, trying to wipe away the tears."
        "When I take a brief look at Lilly, I see that she's softly crying as well."
        "For a long time, neither of us says a word."
        "When Lilly finally opens her mouth, there's a sad but tender tone in her voice."

        show ev sharedsoak_lilly_historyspeak
        with charachangeev

        li "Hanako, you said you gave up on friendship, and yet I think that deep down you never stopped desiring other people in your life. The fact that our friendship came to be is proof of that because it was you who approached me."
        li "You chose me as a friend—your first real friend judging by what I just learned—and I feel very honored by that, even if I haven't always been able to live up to your expectations."
        ha "I'm... n-not sure. I think... I really d-didn't believe in real friendship... back then. But... I think I still wanted to believe, even though I couldn't."
        ha "I thought... since you couldn't s-see what I looked like... t-things would be... different... somehow."
        li "And were they?"
        ha "I'm... not really sure. Even though... you couldn't see my appearance, there... were still plenty of things wrong w-with me that you c-could notice."
        ha "And sometimes... I wondered if it w-was just a m-matter of time before... you found out m-more about me and then d-decided you could... do better."
        "Lilly considers this for a moment."
        li "Hanako, would you do something for me?"
        ha "Yes?"
        li "Can you... take my hands? Both of them?"
        ha "Uh...?"
        "Lilly sits up a little, faces me and holds out both her hands in front of her. A little hesitant, I get a little closer and carefully take her hands in mine, trying to avoid contact with the scar tissue on my wrist."
        "Lilly gives a pleased nod."
        li "Thank you. Don't be afraid."
        ha "Huh?"
        "Lilly gently pulls her hands away and then puts them on top of my own. She gives me a reassuring smile."
        "Then, without waiting for my reaction, she moves her hands upwards along my arms until they're resting on my shoulders."

        stop music fadeout 0.5

        show ev sharedsoak_lilly_hugshock:
            yalign 0.5 zoom 1.02
        with vpunch

        "A moment later she leans forward, wraps her arms around me, and before I realize what's happening, Lilly has locked me in an embrace."
        ha "Aaah!"
        "I let out a cry of surprise, and my body completely freezes up in panic, and time seems to stop for a long time as I wait for Lilly's horrified gasp."
        "But as more and more seconds pass, a realization starts slowly sinking in."

        play music music_twinkle fadein 4.0

        show ev sharedsoak_lilly_hugtimid
        with charachangeev

        "Lilly hasn't flinched."
        "Not even once."
        "I finally manage to hold back my anxiety long enough to stammer out a reaction."
        ha "L-L-Lilly?"
        li "Hanako... Try to relax..."
        ha "Uh..."
        "She lowers her voice to a whisper."
        li "Just relax..."
        ha "I..."
        "As my anxiety slowly—very slowly—starts ebbing away, I become aware of Lilly's hands gently feeling my back and running through my hair."
        "As I slowly start to relax, Lilly pulls me even closer, letting her chin rest on my right shoulder and gently pressing the side of her face against my scarred cheek. Her hug is firm yet oddly tender."
        li "A blind girl and a burn victim being best friends... Several of my sighted friends at Yamaku have pointed out to me how strangely fitting it seems."
        li "And yet, it also feels a bit off-putting, to hear our friendship being defined by this single thing. Don't you agree?"
        ha "I... d-don't know..."
        li "Would you abandon our friendship if some miracle caused your scars to disappear, Hanako? Would you feel you could do better if that were to happen?"
        ha "No, I... I would never do that."
        li "Likewise, if some miracle gave me eyesight, it still wouldn't change anything between us, Hanako. You are a wonderful person. The scars on your body don't change that. In fact..."
        "She gently runs her fingers across the side of my face."
        li "You will probably disagree with my assessment, but I think you look fine."
        ha "I... I... don't..."
        "I stammer a half-hearted denial, but leave it at that. There was such sincerity in Lilly's words that it feels disrespectful to loudly decry her words."
        "As a strangely comfortable silence falls, I try to sort out what I'm currently feeling."
        "It feels strangely pleasant, but it's not passion or desire, like I felt when Hisao and I were in here and he hugged me."
        "The gentle sensation of the warm water and Lilly's close presence feel vaguely familiar, a little bit like whenever Hisao is holding me after we make love. It's the same comfortable sense of safety and security, yet also different somehow."

        show ev sharedsoak_lilly_hugback
        with charachangeev

        "I slowly feel the tense feeling leaving me as my past demons who were awakened briefly by my story are lulled back to sleep, and I eventually gain enough courage to wrap my arms around Lilly and return her hug."
        "Again, she doesn't cringe like part of me expected her to."
        "Inexplicably, something Lilly said to her mother on that fateful day she decided to stay in Japan comes back to mind."
        "“I have a very good friend here who is like a sister to me in all but blood. If I need help with something, I can always count on her to be there.”"
        "I wonder if my presence is also soothing Lilly's anxieties right now."

        show ev sharedsoak_lilly_leanclosed
        with charachangeev

        "Eventually, Lilly lets go of me, and we break off our embrace. I sit down next to her, although this time, I no longer bother to stay an arm's length away from Lilly."
        "When she gently leans against me and puts an arm around me, I'm able to return the favor with no hesitation."
        "After another long silence, Lilly finally speaks up."
        li "Hanako, how are you feeling right now?"
        ha "B-better. How about you?"
        li "Better as well. Thank you for entrusting me with all of this, Hanako."
        ha "It's... okay. I felt it was... only fair... to do so."
        li "Fair?"
        ha "This week, I've seen you... during some v-very vulnerable moments. I've also... learned a lot about your f-family. A lot that... you probably didn't want me to learn."
        ha "It was only fair that... I also allowed you to l-learn a bit more about me, even though it isn't pleasant."
        li "To be honest, I feel a little embarrassed. You've been through so much, and yet here I am, feeling sorry for myself and complaining about parents to someone who no longer has her own. I must really look spoiled to you."
        ha "I think you were right to feel upset."
        li "Still, my problems must look so trivial in your eyes."
        ha "I... don't think they are, and even if they were, it's still okay to feel bad about them. I... uh... g-get upset about what are p-probably trivial things to you... all the time."
        "Lilly giggles."
        li "Thank you for cheering me up, Hanako. You're a true friend."
        ha "Lilly... What will you do now?"
        "Lilly doesn't immediately answer. She merely closes her eyes and seems deep in thought for what feels like several minutes."

        show ev sharedsoak_lilly_leansmile
        with charachangeev

        "Eventually a mysterious smile appears on her face for a second as if she's enjoying some private joke. Then she opens her eyes and turns her head in my direction."
        li "The right thing, Hanako. I'll do my best to support my parents to the best of my ability and hopefully get them to see me in a new light as well."
        li "I will do what I can to change this family for the better and do my part to turn it into what I feel it should be."
        "There's a determination on Lilly's face and in her voice that's unlike anything I've ever seen. It's a stronger determination than she's ever shown before. I can't help being a little awed."
        ha "I hope... No, I know... t-that you'll succeed."
        "Lilly smiles and nods."
        li "Shall we go?"
        ha "Okay."

        # TODO play water splash SFX

        scene bg satou_bathroom
        with locationchange

        "We stand up, and Lilly once again holds out her hand."
        "This time, I don't feel frightened to let Lilly take hold of my arm as I guide her out of the bath and back to the changing area."

        scene bg satou_changingroom
        with locationchange

        "As we dry ourselves off and start putting our clothes back on, Lilly flashes me a playful grin."

        show lilly basic_smileclosed_cas
        with charaenter

        li "Hanako, what happened here will stay between us, won't it? For the sake of Hisao's heart, it might be better if he doesn't know all the details."
        "We let out a mutual giggle to confirm our mutual oath of confidentiality, and once dressed, we make our way out of the bathroom and down the stairs."

        scene bg satou_livingroom
        show lilly cane_smileclosed:
            xanchor 0.5 xpos 0.25
        show karla basic_lost_cas:
            xanchor 0.5 xpos 0.6
        show hisao basic_neutral_polo at right 
        with locationchange

        "As we enter the living room, I see Lilly's mother and Hisao sitting there. Karla gives her daughter an unsure look."
        ka "Hello, Lilly. How are you doing?"
        "Lilly answers her mother's question with a polite bow."
        li "Much better now, Mother. How about you?"
        ka "Okay... I guess. I hope you're not too hungry yet. I didn't know when you would be finished, and I've yet to tell Allison to start preparing dinner."
        li "Actually, Mother, would it be okay to give Allison the rest of the day off?"

        show karla basic_resigned_cas
        with chchange

        ka "Huh?"
        li "This is Hanako's and Hisao's last day here in Scotland. If it's okay with you, I would like to cook for them myself, just this once."
        ka "Uh... Well, I don't mind. But..."

        show lilly cane_smile
        with chchange

        li "Perhaps you could help me get the ingredients ready. I'm still not too familiar with the location of everything."

        show karla basic_wistful_cas
        with chchange

        ka "Well, alright then."

        scene black
        with locationchange

        stop music fadeout 15.0

        nvl clear
        nvl show dissolve

        n "And with that, Lilly and her mother disappear into the kitchen."
        n "{vspace=30}An hour later the four of us share a simple, but delicious meal. Afterwards, Lilly accompanies Hisao and me on one last long walk through the neighborhood before the two of us retire for the evening."

        nvl hide dissolve

        pause 2.0

        if _in_replay:
            return

    label .s2:

        $ set_window_tint(TINT_HANAKO)

        scene bg airport_inverness
        show hisao cross_smile_polo:
            xanchor 0.5 xpos 0.15
        show lilly cane_cheerful_cas:
            xanchor 0.5 xpos 0.4
        show akira basic_pleased:
            xanchor 0.5 xpos 0.6
        show karla basic_sweet_suit:
            xanchor 0.5 xpos 0.85
        with Dissolve(2.0)

        play music music_daily fadein 4.0

        "The next morning, after a filling breakfast, Lilly and her mother take us to Inverness Airport where we're pleasantly surprised by a chipper Akira who's been waiting for us there."

        scene bg airport_baggageclaim
        show hisao cross_smile_polo:
            xanchor 0.5 xpos 0.15
        show lilly cane_cheerful_cas:
            xanchor 0.5 xpos 0.4
        show akira basic_pleased:
            xanchor 0.5 xpos 0.6
        show karla basic_sweet_suit:
            xanchor 0.5 xpos 0.85
        with locationchange

        "After checking in our luggage, the five of us have a cup of tea at one of the coffee shops near the security gate."
        "The atmosphere is surprisingly relaxed with Lilly interacting in her usual way with Akira and Akira not displaying any outward signs of hostility towards her mother."
        "Eventually, Lilly's mother checks her watch and gives us a sad smile."
        ka "Well, I think it's time for you two to head to your gate. You probably want to be among the first to board."
        "Hisao sighs."

        show hisao basic_speak_polo
        with chchange

        hi "Well, I guess we'll be off then. Best of luck to all three of you. And maybe until some other time, Akira."
        "Akira grins."

        show akira basic_ending
        with chchange

        aki "Hey, I'll still be in Japan from time to time. I'll try to accompany whatever business delegation is heading east. And whenever I'm in the country, I'll be sure to stop by at Yamaku. So we'll definitely meet again. "

        show karla basic_cheerful_suit
        with chchange

        "Karla smiles."
        ka "So will we. I'll probably be the one accompanying Lilly to Japan on her way back, so we'll probably meet again soon. Take care of yourself in the meantime, okay? And uh... Since you're in her class, be sure to tell Shizune that I said hello."

        show hisao basic_smile_polo
        with chchange

        hi "We will."
        "Hisao gets up from his seat and looks at me."
        hi "Shall we then?"
        "I nod uneasily. Saying goodbye to Lilly and Akira suddenly feels very hard."
        ha "O-okay."
        "We all get up, and Lilly's mother gives us a respectful bow."

        show karla basic_lillyface_suit
        with chchange

        ka "We’ve put you through quite a bit of trouble. Sorry for that. I hope you enjoyed your time here regardless."

        show hisao basic_grin_polo
        with chchange

        hi "Oh, we definitely have. Right, Hanako?"
        ha "Yes. It was great fun."

        show hisao basic_smile_polo
        with chchange

        "Karla smiles and then reaches into her wallet. She takes some banknotes and puts two of them in each of our hands."
        "I look at them and there's a large 50 on each of them. That's 200 pounds in total. I'm not completely sure how much that is in yen, but I bet it's quite a bit."

        show karla basic_smile_suit
        with chchange

        ka "When you get back to Japan, please change this and use it to go on a couple of fun dates together. It's on us."

        show hisao basic_speak_polo
        with chchange

        hi "We couldn't..."

        show akira basic_laugh
        with chchange

        "Akira cuts off Hisao by giving him a playful shove."
        aki "Just take it, you two."

        show lilly cane_giggle_cas
        with chchange

        "Lilly smiles."
        li "You can tell me all about it when I get back."

        show hisao basic_sweet_polo
        with chchange

        "Hisao and I exchange a resigned look. I don't think there's time for us to argue over this. We both put the banknotes away."
        hi "Thank you."

        show akira basic_cheerful
        with chchange

        "Akira steps forward and gives Hisao a friendly pat on the shoulder."
        aki "Have fun, you two. See ya later."
        "Then she walks up to me and gives me a warm hug while giving me a knowing look."

        show akira basic_wistful_close
        with characlose

        aki "See ya, Hanako. Don't be afraid to call sometime."

        show akira basic_sheepish_close
        with chchange

        "She leans in and whispers."
        aki "And thanks for yesterday."
        ha "Uh... O-okay."

        show akira basic_sweet
        show lilly cane_satisfied_cas
        with charadistant

        "Lilly briefly puts her hand on Hisao's shoulder."
        li "Hisao, please take good care of Hanako today, okay?"

        show hisao basic_smile_polo
        with chchange

        hi "Will do, Lilly. Be sure to hang in there yourself."

        show lilly cane_weaksmile_cas
        with chchange

        li "Hanako, will you be alright?"
        ha "D-Don't worry about me, Lilly. I'll... make it."

        show lilly cane_cheerful_cas_close
        with chchange

        "Lilly steps forward and gives me a loving hug, followed by a light kiss on the cheek."
        li "Thanks for everything, Hanako. We'll keep in touch, okay?"
        ha "Y-yes."

        hide hisao
        hide lilly
        hide akira
        hide karla
        with charaexit

        "We walk out of the coffee shop, and Hisao and I join the queue near the security gate. We turn around and wave goodbye one last time to the Satous."
        "The crowds and security checks will no doubt ruin my day today, but until it's our turn to pass through I want to hold on to that image of Lilly and her family."

        show lilly cane_giggle_cas at twoleft
        show akira basic_ending
        show karla basic_smileclosed_suit at tworight
        with charaenter

        "The sight of Lilly, Akira, and their mother all wearing a smile."
        "Maybe things will turn out alright after all."

        stop music fadeout 5.0

        scene black
        with Dissolve(5.0)

        if _in_replay:
            return

    return