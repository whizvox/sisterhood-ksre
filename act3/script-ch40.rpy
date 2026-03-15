label sh_ch40:
    label .s1:

        $ set_window_tint(TINT_AKIRA)

        call sisterhood_timeskip_broken
        scene bg yuichi_intercom
        play music music_pearly fadein 4.0

        "Yuichi Imai."

        nvl clear
        nvl show dissolve

        n "I hesitate for a moment before pushing the buzzer after typing in his apartment number."
        n "{vspace=30}The last time I visited this place things went downhill pretty quickly. I kinda wonder if it was a good idea to come here."
        n "Still, I guess it beats spending the Sunday evening in my hotel room or at some random bar. Besides, if I hadn't told Lilly last night that I'd be having dinner at Yuichi's place today, she probably would have spent the entire evening trying to convince me to visit our parents' home together with her today."
        n "At least now we got to spend that evening relaxing, catching up, and hanging out in her dorm room together with Hanako and Hisao. I had a pretty good time. It's good being back in Japan for just a little while. The weather's nice too. Octobers in the UK are a lot colder and wetter from what I've heard."

        nvl hide dissolve

        "I hear the intercom crackle a bit and then a familiar voice greets me."
        yui "Akira?"
        aki "Yo."
        "A high-pitched beep sounds, and the door to my left slowly swings open."

        scene black
        with locationchange

        "Last night while hanging out with my sister at Yamaku, I was able to pretend that nothing had changed. For a little while at least."
        "Can I do the same with my ex-boyfriend? Would that even be a good idea? I'm not sure."
        "I make my way up the stairs until I reach the front door of his apartment."

        play sound sfx_dooropen

        "It opens as I approach. My former boyfriend steps out, gives me a friendly wave, and we move inside."

        scene bg yuichi_genkan
        show yuichi neutral
        with locationchange

        play sound sfx_doorclose

        "As he closes the door we stand there awkwardly for a moment."
        "This used to be the point in time where we'd share a kiss, but since we've broken up that's not exactly appropriate anymore."
        yui "...Dinner's almost ready."
        aki "...Neat."
        "I take off my shoes and get ready to put them away, but before I do so I turn to my ex and give him a determined look."
        aki "Yuichi, I appreciate you inviting me over, but let's get one thing out of the way first."
        yui "...You don't have to say it."
        aki "Yeah, I do. I just want to make it clear that me accepting your invitation does not mean I'm here to rekindle our relationship. Okay?"
        yui "Fair enough."
        "I wonder. Personally I'd be surprised if we get through the evening without him trying to convince me to give things another chance."
        yui "So Akira, why did you come here?"
        "I anticipated that question."
        aki "Well, I never hated hanging out with you. As long as we keep expectations realistic there's no reason for us not to have a good time this evening."
        "I fidget a bit. The next part is more difficult."
        aki "Also... I feel kinda bad about the crappy way we parted last time. I've promised myself to leave here as a friend tonight."
        yui "Friend, huh?"
        aki "Well, we used to be friends before we started dating. I get that not a lot of couples can manage to remain friends after a breakup, but this breakup wasn't about anything related to you as a person, so maybe we can make this work. I'd like it to."
        yui "Guess we'll have to see. This way please."

        hide yuichi
        with charaexit

        "He's a little bit more distant than usual, but given the manner in which we parted ways last time that's understandable."
        "Heck, keeping the reason I broke up with him in mind, he has plenty of reason to be bitter."

        scene bg yuichi_dining
        show yuichi neutral
        with locationchange

        "As I enter his living room, a very pleasant smell makes its way up my nostrils. It smells like he went out of his way to make something delicious."
        aki "Hey, that smells pretty good!"
        yui "I'll probably be done in a second. Make yourself comfortable."
        aki "Want me to... ummm... help?"
        "It's not a serious offer. Yuichi's family runs a small restaurant, and he's a pretty good cook in his own right while I'm a pretty lousy one. We both know it. He still finds it extremely funny that my blind sister is better at this than I am."

        show yuichi smile
        with chchange

        yui "Not unless my neighbors calling the bomb squad again is your idea of a pleasant evening."
        "I give him an angry glare, mostly because it's expected of me, but inside I'm actually relieved."
        "Usually, I'd be semi-annoyed by his playful jabs at my sordid cooking skills. But right now, this familiar little ritual between us feels comfortable and reassuring."
        "If he hadn't reacted the way he did after such a tempting lead-in, I'd probably have been concerned."
        aki "Hohoho, very funny. Let's see if this food of yours is worth tasting or if it merely smells good."

        show yuichi neutral at right
        with Dissolvemove(1.0)

        "He gets back to the kitchen counter, and I take a seat at the table. I take a moment to look him over while his back is turned."

        nvl clear
        nvl show dissolve

        n "Yuichi and I have known each other for several years, though it wasn't exactly love at first sight between us."
        n "{vspace=60}I'd like to think my colleagues at the Japanese branch consisted of four groups: those who were friendly to me mainly because I was a Satou, those who silently resented me mainly because I was a Satou, those who were part of both the previous groups, and those who made an attempt to pretend I was an ordinary colleague."
        n "The latter category consisted of far fewer people than the former three, although since even I will admit that the sole reason I even got a job at the company was due to my family ties, I can't say I'm surprised about this. Yuichi was one of the people who fit into the last category."
        n "We worked at different departments, and he was often away from the office, but we occasionally exchanged small talk during lunch when he wasn't visiting clients."

        nvl clear

        n "Shortly after meeting me for the first time, when my colleagues went for a drinking party and I, as usual, turned down the offer to join them, Yuichi approached me."
        n "He confided in me that he heard some people thought I believed myself “too good” to associate with ordinary coworkers despite being a junior employee and that it was probably a good idea to hang out with my colleagues from time to time after work and at least make an attempt to become “part of the team just like everybody else”."

        nvl clear

        n "I was annoyed and even a bit angry at his words and told him that “everybody else” didn't have a blind kid sister waiting for them at home and that I considered it more important to spend my limited free time with her than hanging out with coworkers and pretending to have fun."
        n "He apologized and left, and I later realized that it probably wasn't fair of me to blame him for pointing out what I already knew many people around the office thought about me. In fact, I came to appreciate the fact that he at least tried to do something about a bad situation instead of resigning himself to it and trying to avoid making waves, and he seemed to be understanding of my reasons to stay away rather than dismissive."
        n "So the next lunch break, I approached him and sincerely thanked him for his concern. We ended up befriending each other soon afterwards."

        nvl clear

        n "At some point, he asked if I was interested in having a drink with him. I accepted, and I learned that evening that his alcohol tolerance was the exact opposite of mine. While I wasn't even feeling fuzzy yet, he was already three sheets to the wind."
        n "That evening, I ended up receiving a drunk love confession that was both excruciatingly awkward and highly amusing."
        n "That next day he tried to avoid me of course, but I ended up telling him that I'd be happy to give it a try when the time was right. At that point I simply wanted to be there for Lilly, and I'd feel guilty about spending what little free time I had maintaining a dating life, but if Lilly was old enough to live on her own at some point and he was still interested at that time, I'd be happy to pursue a relationship with him."
        n "{vspace=30}So for some time, we remained friends, and after Lilly moved into the dorms at Yamaku, Yuichi and I started dating."

        nvl hide dissolve

        "Yuichi is rather up-front in private which makes our relationship occasionally combatitive, but most of the time we both do a good job at limiting ourselves to playful teasing and banter."
        "I sincerely like Yuichi and felt genuinely rotten when I had to break up with him, but after having spent some time at head office in Scotland, I've become convinced that my decision to migrate to Scotland was the right one."

        show yuichi smile at center
        with Dissolvemove(1.0)

        yui "I hope you haven't gotten so hooked on chips and sausages that you're no longer able to appreciate a good Japanese dish."
        "Having finished his preparations, Yuichi walks up to the table carrying a delicious dish of rice, fried vegetables, and pieces of fish."
        aki "I think I'll be okay. And besides, I've got something to flush it down with."
        "I fish a bottle of Scotch out of my bag and triumphantly put it on the table."

        show yuichi annoy
        with charaenter

        "His eyes widen a bit as he reads the label."
        yui "40\%? Are you trying to poison me?"
        aki "Some of my new colleagues would probably take offense at you insulting their favorite liquor."

        show yuichi neutral
        with chchange

        yui "Has it become your favorite liquor as well?"
        aki "Nah, I still like beer more whenever I visit one of the local pubs during the weekend. This is more of a special occasion drink. Except there haven't been many special occasions for some time and I don't like drinking alone anyway. I figured I'd bring it along as a gift."
        yui "You're gonna perform a toast?"
        aki "Not unless me having to calling the ambulance again is your idea of a pleasant evening."

        show yuichi annoy
        with chchange

        "I give him an overly cheerful smile, and am rewarded with an annoyed glare. He doesn't like being confronted with the fact that I can hold my liquor so much better than he can."

        show yuichi neutral
        with chchange

        yui "I guess that makes us even now. How about a truce? At least until we finish the meal."
        aki "Fine with me. I was actually thinking you could give this bottle to your dad. He's really into ‘exotic’ liquors, isn't he? You offer this to him, and you'll be his favorite person in the world for weeks on end."

        show yuichi smile
        with chchange

        yui "Hey, that's actually a pretty good idea. I think I'll do that. Thanks."
        aki "Well, let's dig in before it gets cold."

        show yuichi neutral
        with chchange

        "We quietly start eating, and I make sure to give a few satisfied nods during the meal to let him know it tastes very good."

        if _in_replay:
            return
        else:
            stop music fadeout 2.0

    label .s2:

        $ set_window_tint(TINT_AKIRA)

        scene ev justfriends_sit
        with shorttimeskip

        queue music music_night fadein 4.0

        # show yuichi neutral at right
        # show akira basic_wistful at left

        "After finishing the food, we head over to the couch. I make sure to sit some distance away from him in order to accentuate the point I made earlier."
        "He rolls his eyes for a moment but then shrugs his shoulders."
        yui "I guess a lot has happened at head office since you moved, huh?"
        aki "My arrival didn't really have anything to do with any of that. But yeah, it's been an eventful time."
        yui "Care to share some about it?"
        aki "I think you know most of it yourself by now. Your colleagues seemed informed enough when I dropped by the office two days ago. The rumor mill's still going as strong as it was the first time I came back from Scotland. It's worse than a sewing circle."

        show yuichi think at right
        with chchange

        yui "Well, I got the gist of it. Your father got sudden health problems, so he ended up taking part in the negotiation meetings from his sickbed, and several folks over here shifted up the chain of command because Kojima got a promotion. A very significant one from what I've heard."

        show akira basic_annoyed
        with chchange

        aki "Sudden health problems, huh? Is that what they're calling it?"

        show yuichi neutral
        with chchange

        yui "What would you call it?"
        aki "Health problems is one hell of a euphemism. Chronic back pain is a health problem. That heart attack came this close to killing him. He was lucky Hanako recently picked up CPR."
        yui "Who's Hanako?"

        show akira basic_ponder
        with chchange

        aki "Lilly's best friend. Lilly and two of her best friends from school were visiting at the time. They were with him when he collapsed. Hanako managed to keep him going until the ambulance arrived. Thank goodness the hospital wasn't far."
        yui "He got a heart attack out of nowhere?"
        aki "Hardly out of nowhere. He had been under the weather for weeks. We figured it was just the stress of the takeover process. We didn't think they were symptoms of an impending heart attack. He didn't bother to tell us."

        show yuichi annoy
        with chchange

        yui "Wait... He knew?"

        show akira basic_pissed
        with chchange

        "I give him a strong stare from across the couch."
        aki "None of this is gonna leave this room, right?"

        show yuichi neutral
        with chchange

        yui "Of course not."

        show akira basic_annoyed
        with chchange

        aki "He's had high blood pressure for years. His general practitioner was only surprised he lasted as long as he did."

        show yuichi annoy
        with chchange

        yui "And nobody else knew?"

        show akira basic_distant
        with chchange

        aki "Nope, not even Mom. I think it's taken her quite a while to forgive him for that. She took it really hard when she found out that the he knew he was a risk case."

        show yuichi neutral
        with chchange

        yui "Why didn't he tell anyone?"

        aki "In the end I think it came down to his legacy. It took ages before Granddad retired as head of the business. Dad probably wanted to leave his own mark on the company."
        aki "He figured that if people knew about his health, they'd start pressuring him to take it easy—or even step down. He was probably afraid of not being able to live up to his father."

        show akira basic_annoyed
        with chchange

        "I smirk briefly."

        aki "The funny thing is that the work culture in Inverness is completely different from the office here, and none of his direct colleagues would consider his actions a noble sacrifice on behalf of the company. They'd all think he was crazy for putting his health at risk for a mere job."

        show yuichi think
        with chchange

        yui "Eventually you and your mother ended up helping him take care of his legacy, didn't you? Together with Kojima."

        show akira basic_distant
        with chchange

        aki "Mom initially didn't feel like flying to the US with Dad still bedridden, but Lilly eventually managed to convince her to bring the whole thing to a close while she stayed behind in Inverness to look after Dad."
        aki "Kojima went along in order to reassure the board back in Japan, but in practice, he was little more than an observer."
        aki "Mom was the one who has been involved in the negotiation talks since the beginning, and she was most familiar with the people and the American business culture, so she was the one who did most of the speaking with me chipping in on frequent occasions."

        show yuichi neutral
        with chchange

        yui "You?"

        show akira basic_ponder
        with chchange

        "I tell him about his trouble speaking due to his busted ribs and the conference system we set up so he could still take credit for taking part in the whole deal without having to be present or feel ashamed for barely being able to talk."

        show yuichi smile
        with chchange

        yui "In the end you managed to reach a deal, right? This will probably look good on your resume too."
        aki "I didn't really do much besides act as Dad's voice. He and Mom deserve the credit."
        yui "So, how was it spending over a week with your mom?"
        aki "I didn't really interact much with her. I spent more time with the rest of my colleagues. It was a pretty good opportunity to get to know them better."

        show akira basic_wistful
        with chchange

        aki "The system administrator who came with us was a bit socially awkward, but ridiculously knowledgable in the realm of Japanese manga. Made for quite a bit of relaxing conversation for a recent immigrant like myself."

        show yuichi neutral
        with chchange

        yui "You don't think it would have been an opportunity to reconnect with your mother?"

        show akira basic_distant
        with chchange

        aki "I think she had enough on her mind already as things were."

        show yuichi think
        with chchange

        yui "..."

        nvl clear
        nvl show dissolve

        n "I can tell from his stare that Yuichi thinks I'm making excuses, but that's not the case this time. While we were in the US, I could tell that there was something on Mom's mind."
        n "Something that bothered her enough to have several restless nights and the occasional absent-minded look whenever we were alone. It could have been her just worrying about Dad, but since Lilly gave us daily updates on his condition, there was probably more to it than that."
        n "{vspace=30}Maybe she knew all along how things were going to play out with Dad at the company. If she and I had been closer, I probably would have asked her to confide in me. As things were, the only thing I could do was avoid imposing on her too much."

        nvl hide dissolve

        show akira basic_wistful
        with chchange

        aki "Anyway, it still felt very satisfying to return to Inverness and report that our company now had three branches."

        play sound sfx_whiteout

        scene bg satou_entrance at flashback
        show lilly basic_smile_cas at twoleft, flashback
        show hiroyuki serious at tworight, flashback
        with Fade(0.5, 0, 0.5, color="#fff")

        "When Mom and I returned to the mansion, Lilly and Dad were waiting for us. Dad was still in a pretty sorry state, but he nevertheless went outside together with Lilly to greet us."

        show lilly basic_weaksmile_cas_close
        show hiroyuki bow_close
        with { "master": Dissolve(0.5) }

        "When we got out of the car and stated to Dad that the trip had been a success (which he knew already of course since he had taken part in the meetings), he bowed deeply to us and started saying how proud he was of both of us—now that we'd dragged his bum out of the fire."

        show lilly back_listen_cas_close:
            xpos 0.35
        show karla basic_laugh_close at center, flashback behind lilly
        show hiroyuki scold_close behind lilly:
            xpos 0.6
        with { "master": Dissolve(0.5) }

        "He was being really formal about it, and it turned out that Mom wouldn't have any of that at that moment. Before he could finish his speech, she stepped forward and hugged him with one arm while embracing Lilly with the other."

        show lilly back_giggle_cas_close
        show karla basic_cheerful_close
        show hiroyuki awkward_close
        with { "master": Dissolve(0.5) }

        "He seemed surprised and awkward about it, but didn't resist or protest. Lilly, on the other hand, looked happier than I've seen her in a very long time."

        show karla basic_smileclosed
        show hiroyuki awkward at tworight, flashback
        show lilly back_smileclosed_cas at twoleft, flashback
        with { "master": Dissolve(0.5) }

        "I didn't really feel like being part of the whole thing, so I took that moment to say goodbye and return to my apartment. They didn't try to stop me, and I'm happy they didn't let me ruin their little moment."

        play sound sfx_whiteout

        scene ev justfriends_sit
        show yuichi think at right
        show akira basic_wistful at left
        with Fade(0.5, 0, 0.5, color="#fff")

        yui "So I guess your dad's honor was saved. Though from what I heard it didn't exactly last."

        show akira basic_ponder
        with chchange

        aki "It didn't. It still took us by surprise though. At least it took me by surprise. I wasn't there when he heard the news."
        yui "About Mr. Kojima?"
        aki "That's not his name anymore. He's called Koji Satou now."

        show yuichi neutral
        with chchange

        yui "So you now have a new uncle?"
        "I do. The head of the Japanese branch more or less got the ultimate promotion when Granddad adopted him as a son, heir and new head of the family - and adopted his wife along with him."
        aki "Yeah... Still feels weird to call him that though. I usually settle for his name with a honorific attached to it when we're alone."

        show yuichi think
        with chchange

        yui "He's kind of old to be adopted though."

        show akira basic_wistful
        with chchange

        aki "What are you talking about? Last time I heard nearly 98\% of all adoptees in this country are adult guys."

        show yuichi neutral
        with chchange

        yui "That's not what I'm talking about. Aren't adoptees usually in their late twenties?"

        show akira basic_ponder
        with chchange

        aki "Yeah and if Dad had been replaced when he was still around that age, they would have plucked a fresh prodigy out of Tokyo University's graduate pool and planted him in the company to learn the ropes."
        aki "But whoever was going to transfer to another continent where they couldn't teach him the ropes or keep an eye on him had to be a senior executive with experience and loyalty to the company."
        aki "Koji's worked for the company for decades, and his dad was a friend of the family. They trust him, and they probably felt he earned the opportunity. Even Dad doesn't seem to begrudge him his promotion, though it's possible he's merely putting on an act. It's hard to tell."

        show yuichi think
        with chchange

        yui "Still sucks for your dad though. At least they didn't expect him to adopt his own successor."

        show akira basic_wistful
        with chchange

        aki "Koji's two years older than Dad. It's not possible to adopt people older than yourself unless you're willing to use loopholes..."

        show yuichi smile
        with chchange

        "He snickers."

        yui "You're the lawyer. I'll take your word for it. It would have been weird having an adopted brother old enough to be your father."

        show yuichi neutral
        show akira basic_distant
        with chchange

        aki "Besides maybe they figured this was already enough of a blow to him as it was. No need to rub even more salt in his wounds."
        yui "He wanted to keep going after his recovery?"
        aki "I think so. His job and what he called his 'responsibilities' have always been everything to him. I think he thought he'd be able to pull it off as long as he kept himself under close medical surveillance."

        show yuichi think
        with chchange

        yui "But not everybody agreed with him, it seems."

        aki "I guess they felt he wouldn't be able to give his all to the company anymore. Or worse, have another heart attack and die from it."

        show akira basic_wistful
        with chchange

        aki "The British would actually find that kind of thing morbidly amusing: The CEO of a company making heart monitors being a heart patient. But black comedy isn't exactly something I think the board enjoys. They'd probably see it as a massive loss of face."
        aki "Since the company is still a family business, and a Satou had to be in charge, they simply made Koji a Satou and adopted him and his wife into the family."

        show yuichi neutral
        with chchange

        yui "How did your dad take the news that he was laid off?"

        show akira basic_distant
        with chchange

        aki "They didn't fire him directly. Granddad simply adopted Koji and Dad was told his new brother would be assisting him with his duties from now on, and he was asked to teach his new second-in-command the ropes."
        aki "They probably expected Dad to take the hint and resign of his own - which he did. I'm not sure how he reacted to the news when he got it since I wasn't there when it was broken to him."

        show akira basic_wistful
        with chchange

        aki "When I spoke to him he seemed resigned to it, and he said they told him that at least he'd be well provided for."
        "I can't help but crack a sad smile at that. Of course Dad received a significant percentage of the company shares in compensation and a position on the board, although since he's so much younger than the rest, he'll have very little say in practice."
        "Still, the hidden meaning behind that way he worded his answer to me was quite clear. Yuichi doesn't need to know that story though."

        show akira basic_ponder
        with chchange

        aki "Lilly worries about him though. She says he's taking it a lot harder than he likes to let on."

        show yuichi think
        with chchange

        yui "She's probably right about that."

        show akira basic_resigned
        with chchange

        "I look at my former boyfriend with an inquisitive look."
        aki "You're a former family heir too, aren't you?"
        yui "Yeah, but our simple family restaurant wasn't what you'd call a multinational. I was meant to take it over, but I was never really much of a manager to begin with. So eventually my parents adopted someone who had shown interest in managing it and who ended up getting married to my sister."

        show akira basic_wistful
        with chchange

        aki "What was that like?"

        show yuichi neutral
        with chchange

        yui "It's never fun to be replaced, and it kind of hurts your ego. Oldest sons have a special status in the family. It's like an identity you grow up with since early childhood."

        show akira basic_distant
        with chchange

        yui "I was lucky I was never that interested in taking over the business and came to that conclusion early. Your dad spent decades in that role."
        aki "Yeah."
        yui "Losing your employment at a company you've worked your entire life at sucks to begin with. You lose the environment you formerly spent nearly 80 hours a week in. You lose pretty much your entire social circle and all your friends. And you lose your daily routine..."
        aki "I think several of those already vanished when he moved to Scotland. Working culture is different there. People usually work only around 40 hours a week and often seek their friends outside the workplace."

        show yuichi think
        with chchange

        yui "...but losing your status as patriarch at this point is way more than that. In addition to your inheritance suddenly dropping down from 'everything' to 'nothing' it also comes with a sense of shame and failure. And a loss of purpose."

        show yuichi neutral
        with chchange

        yui "He probably feels like part of his identity has been stripped away and given to someone else."

        "I don't have much experience with adoptions, so I'll take Yuichi's word for it. If what he says is remotely accurate, it's kind of hard not to feel pity for the old man at this point, despite the fact that I'm still not overly fond of him."

        show akira basic_ponder
        with chchange

        aki "Well, at least he still has Mom and Lilly to cheer him up. They seem pretty determined not to let him sink further into a depression."

        show yuichi think
        with chchange

        yui "And parts of their efforts to cheer him up involved moving back to Japan, huh?"

        show akira basic_wistful
        with chchange

        aki "Yeah, they moved back here permanently not long ago. The decision wasn't made easily."

        show akira basic_ponder
        with chchange

        aki "Mom was initially hesitant to leave her homeland again and mentioned that several companies there would have welcomed Dad and would even offer him part-time employment if his health wouldn't allow full-time work."

        show akira basic_wistful
        with chchange

        aki "Koji wasn't eager to see them move either. But Lilly and I made a pretty strong plea for moving, and Dad eventually took our side."
        aki "When she flew to Japan to drop Lilly off, Mom even went to look at some houses afterwards, so she probably expected this outcome already. Our old house was sold some time ago, and they've moved into a new neighborhood. Made a brand new start as it were."

        show yuichi neutral
        with chchange

        yui "So, aren't you considering moving back here as well?"

        show akira basic_annoyed
        with chchange

        aki "I didn't move to Scotland for my parents. I moved there for my job. And my job wasn't shipped back to Japan."
        yui "But both your parents and your sister are now living here."

        aki "And I'm happy for her. Lilly still needs her parents despite the grownup appearance she puts on, and now that she's given them another chance I sincerely hope they don't blow it. If she spends enough time with them, they might actually become a family again."
        yui "She's decided to give them another chance, but you obviously haven't."
        aki "They never even apologized for just walking out on us. A heart attack sucks a lot, but it's not an apology. A thank you to me would be appreciated too."

        yui "A thank you?"

        show akira basic_pissed
        with chchange

        aki "Thank you Akira, for being there for Lilly in our place during her puberty and some of the toughest school years of her life. We appreciate the fact that we can pick things up again now that the hardest part is largely over."

        show yuichi think
        with chchange

        yui "...you're still pretty bitter about that."

        show akira basic_distant
        with chchange

        aki "...I guess I am."
        "I'd be lying if I denied that this is how I feel. Lilly has her life pretty well in order right now and is hardly in need of any parental oversight anymore. Mom and Dad can now tell themselves that they're good parents by merely hanging out with her. How easy."
        "I noticed that this train of thought kept returning to me whenever I saw my sister and our parents interact lately."
        "I guess it's not healthy for me to think or feel like that, but it's been on my mind a lot, and it's one of the reasons I decided not to accompany Lilly to our parents' new place today. I realized I just don't feel comfortable seeing them interact."
        yui "You think you'll get an apology?"

        show akira basic_annoyed
        with chchange

        aki "Naw. Especially not from Dad. He'd probably feel it'd weaken his position as head of the family. As if his failures don't exist as long as he doesn't admit them. Doesn't work that way with me."
        yui "Well, offering apologies isn't exactly a family trait to begin with."

        show akira basic_pissed
        with chchange

        aki "Okay, what does that mean?"

        show yuichi annoy
        with chchange

        yui "That palm print was still on my cheek the morning after you left last time."

        nvl clear
        nvl show dissolve

        n "I sigh. Last time we were together was when I came by his place to invite him to a weekend trip to our family's summer home in Hokkaido."
        n "I planned to tell him about the job offer I took while we were there, but the damn office rumor mill had already caught up with me by that time, and Yuichi was quick to confront me with what he learned about my upcoming departure."
        n "I wasn't proud of my decision to move, and when we got into an argument I was prepared to take his reproaches in stride. I managed that just fine at first until the moment he argued that I was a lot more like my parents than I cared to admit."
        n "That was the one thing he shouldn't have said. I lost my temper, gave him a hard slap across the cheek and stormed out of his apartment with the intention of never speaking with him again."
        n "I felt crappy about it afterwards but still didn't speak to him until we ran into each other this week while 'uncle' Koji and I were at the Japanese office for a few days."

        nvl clear
        nvl hide dissolve

        aki "Who exactly used to like leaving hickeys on my neck?"
        yui "I know which one of the two I'd rather receive."

        show akira basic_distant
        with chchange

        aki "Fine. I guess I shouldn't have slapped you. I'm really sorry about that. But that remark you made was still way out of line."

        show yuichi think
        with chchange

        yui "It wasn't really an intentional attempt to hurt you. It was more like... an angry observation."

        show akira basic_pissed
        with chchange

        "I narrow my eyes at his words, but he shows no sign of backing off."

        show yuichi annoy
        with chchange

        yui "What exactly was it you said back then? It was something like: 'Life isn't a fairy tale. You can't set it up and expect it to stay that way forever; sometimes stuff happens that you have to roll with, even if it means hurting yourself or others.', wasn't it?"

        show akira basic_annoyed
        with chchange

        aki "My job would have hit a pretty abrupt dead end if I hadn't taken that offer. Heck, at least over there people won't start pressuring me to quit my job and start making babies when I turn 30. You said before that you understood my situation. Has that changed?"
        yui "It hasn't, but I kind of wonder if maybe your dad has been in a similar situation in the past and thought the same thing as you at the time."

        show akira basic_distant
        with chchange

        aki "He was worried about his job if he had refused? Is that what you're saying?"

        show yuichi think
        with chchange

        yui "Is it that hard to believe, given what's happened recently? As head of the company he could at least guarantee you a job long enough for you to learn the ropes and pass the exams required to get your law degree, but only for as long as he maintained that position."
        yui "Maybe that's part of what he meant when he said he'd be guaranteeing your financial future by accepting his promotion and moving to Inverness. Who knows what his replacement would have done."
        yui "People usually aren't given a job in a legal department without a solid university degree, so maybe your dad figured that giving up his influence in the company would have made things complicated for you too."

        "I never really thought of it that way. I always assumed that they had no choice but to stick with Dad and that he could do whatever he pleased, but maybe that wasn't the case after all."
        aki "You think that the threat of replacement was an issue even then?"

        show yuichi neutral
        with chchange

        yui "In most other countries family businesses underperform compared to their competitors. Over here it's the exact opposite. There are two reasons for that."
        yui "The first one is the fact you can pick an heir from the academic cream of the crop if none of your own sons is up to the challenge."
        yui "The second one is that the biological heirs who do take over their father's business are extremely motivated to perform well because they know that their job and family position can be given to someone else if they mess up."

        show yuichi annoy
        with chchange

        yui "One of the reasons I wasn't eager to take over my dad's restaurant was the fact I didn't like the idea of living with that kind of pressure for a job that didn't even catch my interest."
        yui "But yeah, I think he knew. You can't motivate someone if he doesn't know that he has a lot to lose."
        yui "And a company heir who willingly tosses aside his responsibilities doesn't easily get a second chance, here or anywhere else, because he'll be seen as unreliable from then on. And with two daughters to provide for, including a blind one..."

        show akira basic_ponder
        with chchange

        aki "...okay, okay, makes sense, I guess. But even so..."

        show yuichi neutral
        with chchange

        yui "Hmmm?"

        aki "It's not like Mom and Dad saw each other that often during their marriage. Dad has had to deal with long working hours for as long as I can remember."

        show akira basic_distant
        with chchange

        aki "Usually when someone gets promoted and has to move and his family can't come along, he just goes to live on his own and visits his family on Sunday every weekend or whenever he has the time."

        show akira basic_annoyed
        with chchange

        aki "Why did he have to request Mom to accompany him and not us? I get that Mom's been a great help in getting him settled there but she could have advised him over the phone or simply spent some weeks there."
        aki "I get that he was probably lonely there, but they've been slowly growing apart ever since they moved, so in the end it might have done more harm than good to his marriage."

        show akira basic_pissed
        with chchange

        aki "Or they could have taken Lilly along with them. There are good schools in Scotland too. Heck, they could have phoned her more often."

        yui "I won't try to justify any of that."

        show yuichi think
        with chchange

        "A brief silence. He tosses me a can of beer that I catch and open with a grateful nod. Looks like he still remembers my favorite brand."

        show akira basic_distant
        with chchange

        aki "You're angry that I walked out on you like this?"
        yui "You said your father was rather lonely. Are you happy over there?"

        aki "I think so. I still try to speak with Lilly over the phone twice a week or so. Company culture at work couldn't be more different. I start at half past 8 each day and go home at 5 in the afternoon. That's 6 hours less than I used to work here."
        aki "There's overtime from time to time, but it's an exception rather than a rule. Meetings are quick and people skip the small talk. There's a lot of focus on efficiency. People are pretty direct and not afraid to respectfully challenge their superiors."
        aki "We're expected to give our all, but overall I think I like it there. I've had more free time in these last two months than I had in my last two years here."
        aki "Colleagues generally don't hang out after work and get-togethers aren't mandatory, but I've joined a gym that some of my new colleagues go to, and there's some people I met there that I sometimes visit a pub with during the weekends."
        aki "All in all, I think I've managed to adapt well and fairly quickly, even though I still feel like a fish out of the water at times. But I felt the same at the Japanese branch, so that makes no difference."

        show yuichi neutral
        with chchange

        yui "How about your new boss? How's he doing? He's older than you, so the change must be bigger for him. "

        show akira basic_wistful
        with chchange

        aki "There's a lot of competent people there, but the place has to be managed like a western company because that's what the employees are used to."
        aki "Even for Dad it was a massive culture shock and he had Mom to advise him on how to deal with things. I think that's part of the reason the job was so stressful for him."
        aki "Mom has a deal with Koji that she'll give him all the advice he wants when he needs it and will frequently drop by in Scotland to help keep an eye on things and to help smooth over any conflicts or misunderstandings."
        aki "In return, Koji's wife will be taking care of Dad's parents instead of Mom."
        yui "She didn't come along?"

        show akira basic_distant
        with chchange

        aki "Koji's wife doesn't even speak English. She'd be utterly isolated and miserable there. That does make it more lonely for him though. I've been trying to occasionally spend time with him and keep an eye on him so he doesn't end up in the same situation as Dad."

        show yuichi smile
        with chchange

        yui "That can't be bad for your career prospects."

        aki "I want to go and get a good deal of experience here, but I'm not sure if I wanna work there forever. I've spoken with some of my colleagues, and I've learned that it's pretty socially acceptable in the UK to leave your job if you get a better offer somewhere else."

        show yuichi annoy
        with chchange

        yui "No company loyalty huh?"

        show akira basic_ponder
        with chchange

        aki "Not to the point of working several hours of unpaid overtime a day and sticking around until the boss goes home. People see the whole thing as a way to earn a living, rather than as a social obligation to their boss."

        show akira basic_wistful
        show yuichi neutral
        with chchange

        aki "I've done some thinking, and maybe I'll leave the company someday as well. I still like it there, but I'd also like to tell myself I got somewhere without having needed to use my family relations as a crutch."
        aki "I'd even be willing to take a slight drop in pay for the ability to tell myself I'm in a certain position solely because my boss thinks I'm more qualified for it than any other person."

        show yuichi think
        with chchange

        yui "So all in all you've settled yourself pretty nicely over there."
        "From the tone of his voice that's not merely a neutral conclusion."

        show akira basic_distant
        with chchange

        aki "...maybe I'll return to Japan someday, but certainly not now. This isn't just about Mom and Dad. I want to know if I'll be able to set up a life there and feel like I'm at home there. Like I belong."
        aki "It's something I've wondered about for a long time. Lilly was sad to hear that but nevertheless said she'll be supporting me all the way. I get that you're angry because I took this decision so quickly, but..."

        show yuichi neutral
        with chchange

        yui "I don't blame you for taking the job in Scotland without a moment's hesitation. It sounds like you made the right decision back then and that you still stand behind your choice."
        aki "But...?"

        show yuichi annoy
        with chchange

        yui "What stung was the fact that you probably made the decision to end our relationship in that same split-second. Like it didn't matter to you at all."

        show akira basic_lost
        with chchange

        aki "That's not true."
        yui "Last time you came here you didn't visit me to tell me about your decision to migrate. You visited me to break up with me. You already decided for the both of us by that point."

        "I sigh wearily."

        aki "Don't tell me you were going to suggest a long distance relationship, Yuichi. Like I said I have no idea when and even if I'm going to return to Japan."
        aki "And we barely had enough free time to maintain a normal relationship when I was still living here. Why set ourselves up for disappointment?"

        play music music_drama fadein 4.0

        show yuichi think
        with chchange

        yui "I was more thinking along the lines of asking for a transfer myself."

        show akira basic_resigned
        with chchange

        aki "What?"

        show yuichi annoy
        with chchange

        yui "I would have mentioned that to you last time if you hadn't been in such a hurry to break up with me."

        show akira basic_lost
        with chchange

        aki "You'd give up all your friends and family here just to make a new start there?"
        yui "Don't tell me that's a crazy idea because you've done exactly that yourself."
        aki "Your situation is completely different from mine and besides... I couldn't possibly ask that of you."

        show yuichi think
        with chchange

        yui "You could have. You just didn't. Or wouldn't. Look, I'm a pretty worldly person, I'm a good English speaker, my parents aren't expecting me to take care of them anymore after they retire so it could have worked."
        yui "Heck, a temporary working visa just to test the waters for a while could have worked as well."

        show akira basic_resigned
        with chchange

        aki "Could have worked?"

        show yuichi annoy
        with chchange

        yui "You already broke up with me and insisted on being just friends. I'm not going to drop on my knees and plead for a second chance. Not when it was never my wish to see our relationship shot down to begin with."

        show akira basic_distant
        with chchange

        "I came here prepared for attempts to convince me to give things another try, but this is not something I saw coming. Is he really serious about this? Seems like it."

        show yuichi think
        with chchange

        "Maybe he's right. Instead of wondering if there was a chance to save our relationship after accepting Dad's offer, I immediately started thinking of ways to break up my relationship with Yuichi without hurting him too badly."
        "I kinda wonder if he doesn't deserve someone better than me. Still, the way he worded it suggests he's still open to giving it a try. Practically speaking it shouldn't be too hard. It would just take a little time to arrange a working visa."
        "Koji will almost certainly greenlight the transfer if I ask him. He knows what it's like to live far away from one's partner."

        "I can't believe I'm actually seriously considering this. At the start of the evening I was loudly insisting I wasn't here to revive our relationship. So much for my determination."

        show akira basic_lost
        with chchange

        "His words are loud and clear. He wants to transfer too and give our relationship another try if I apologize profusely and tell him that I want him back. That'll be a serious blow to my pride, though it might just be worth it. Maybe."

        show akira basic_resigned
        with chchange

        "I need to think. Somewhere. Without him staring at me."
        aki "I'll... uh..."

        show yuichi neutral
        with chchange

        yui "Sleep on it?"
        "I let out a resigned sigh."

        show akira basic_distant
        with chchange

        aki "Maybe. But not here."
        yui "Fair enough."

        "I don't think we'll be able to have any more small talk after this. Yuichi must have read my expression as he gets up and tosses me another beer can."
        yui "One for the road."
        aki "...Yeah."

        scene black
        with Dissolve(2.0)

        "As I put my shoes back on and walk out the door there's a painful silence between us. I give him an awkward wave and then walk down the hall to the elevator with a very confused feeling in my gut. Before entering my car I take out my cell phone and dial the top-most number on my contact list."

        scene bg akira_car

        aki "..."

        show lilly basic_smile_phone at phonebox
        with charaenter

        li "Good evening. Lilly Satou speaking."

        aki "Yo..."

        show lilly cane_satisfied_phone
        with chchange

        li "Akira. So good to hear from you. "
        aki "Had fun with the folks today?"

        show lilly basic_smileclosed_phone
        with chchange

        li "Your presence was missed here. The three of us went on a rather long walk today. Long for Father at least. He needs to rebuild his stamina, and Mother and I also felt that he needed to get out of the house more."

        show lilly basic_reminisce_phone
        with chchange

        li "It just doesn't seem right that he spends most of his days doing little more than sleeping in and reading on occasion."

        "Sounds like the old man is still struggling. My thoughts return briefly to Yuichi's words earlier about losing one's position as heir at this point in life. I make a mental note to tell Lilly about what my boyfriend said this evening since I think she'll find it interesting."

        aki "It's only natural he'll need some time to sort things out and fill that sudden void in his life."

        show lilly basic_weaksmile_phone
        with chchange

        li "How was your dinner with Yuichi?"
        aki "...are you busy right now?"

        show lilly basic_smileclosed_phone
        with chchange

        li "Just drinking tea with Hanako."
        aki "I know it's already late, but err..."

        show lilly basic_smile_phone
        with chchange

        li "...when do you think you can be here?"
        "Wow, she caught on pretty quickly."
        aki "In 35 minutes. No, make that half an hour."

        show lilly basic_cheerful_phone
        with chchange

        li "We'll be waiting."
        "A grateful smile appears on my face."
        aki "Thanks Lils. You're the best."

        hide lilly

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return

    return
