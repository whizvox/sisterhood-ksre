label sh_ch26:
    label .s1:

        $ set_window_tint(TINT_HISAO)

        scene bg inverness_field
        with nextchapter

        play music music_soothing fadein 4.0
        play ambient sfx_bikeride fadein 2.0

        hi "So we're heading for some old battlefield?"
        ka "Well, that place is part of the local history so I was hoping I'd get an opportunity to show it to you. There's a monument in the middle of the moor, but I don't think having a picnic there is a good idea. Not enough shade."
        "After traversing the road through one of the nearby villages, we're now crossing the countryside again with nothing but open fields all around us."
        hi "Whew."
        "I don't think we've gone on for that many kilometers yet, but all of us (with the exception of Lilly's mother) are nevertheless starting to get a little winded."
        "The wind provided some pleasant relief from the heat while we were riding through the streets of the village, but here in the middle of the open field, it's strong enough to start wearing us out."
        ka "Are you okay? We can take a break any time you like."
        "That's the second time Lilly's mother has asked me that in 5 minutes."
        hi "I think I'll manage. I do hope that wind dies down soon though."
        ka "It's a bit stronger than they predicted. It'll get less when we get to the road north of the moor since it's lined by a small forested area on one side."
        "Though the ride is more taxing than I anticipated, I can't deny I'm somewhat enjoying it."
        "It feels good to engage in some physical activity after two days of mostly sitting and sleeping and the route so far has offered plenty of interesting sights."
        "Karla's statement that she likes to take bike rides around the countryside in her free time has been confirmed several times while we were riding through the village, and several people who seemed to recognize her waved at us when we passed by."
        hi "Damn, we might have to stop somewhere soon anyway. I see rationing water isn't really my strong suit."
        "As I notice my water bottle being nearly empty already, I mutter this to myself without intending anyone to hear it, but moments later I nevertheless feel something poke me in the back."

        show hanako defarms_worry at tworight
        with charaenter

        "When I carefully look behind me I can see Hanako offering me hers. I nod in acknowledgement."
        hi "One little sip then. But that's all."
        "I take a small sip from Hanako's bottle, which is still about half-full, and then hold it out behind me until I can feel it being taken from my hand."
        hi "Thanks."

        hide hanako
        with charaexit

        "The road goes on for a much longer time, and pedalling starts getting heavier and heavier."

        scene bg inverness_culloden
        with locationchange

        "Finally, as we reach a wide open plain that looks different from the fields we've seen so far, Lilly's mom raises her hand as a sign to stop."
        
        stop ambient fadeout 2.0
        queue ambient sfx_windy fadein 2.0 volume 0.6

        "She gets off her bike and makes a sweeping gesture in the air."

        show karla basic_cheerful_cas at center
        with charaenter

        ka "What lies before you right here is the Culloden battlefield."
        ka "About 260 years ago, this moor was the site of a rather brutal battle between the rebels attempting to help the exiled prince Charles Edward Stuart claim the British throne and the loyalist army led by the son of the British King at the time."
        ka "The battle has the dubious honor of being the last full-scale battle taking place in this country."
        "She does sound a bit like a tourist guide reciting stuff like this."
        hi "I assume Scotland sided with prince Charles?"

        show karla basic_smile_cas
        with chchange

        ka "Some of the clans opposed him, but the Highlands area here was certainly one of the places containing a large number of supporters to his cause."

        show karla basic_smug_cas
        with chchange

        ka "Said cause being an absolute monarchy based on the Stuart dynasty's divine right to rule. Not exactly a popular point of view these days anymore, but the Stuart house has ruled this country for centuries, so they had quite the following back in the day."
        hi "So, who ended up the victor?"

        show karla basic_wistful_cas
        with chchange

        ka "Well, the prince may have been many things, but a military genius he was not."
        ka "Against the advice of his commanders, he went with a defensive strategy in a wide open marshland that hampered quick offensive charges while being faced with an opponent who had superior artillery."
        ka "It worked about as well as you'd expect. In the end, the Stuart followers ended up slaughtered in less than an hour. Most football riots these days last longer."
        hi "And the prince?"

        show karla basic_ponder_cas
        with chchange

        ka "He got away to France, though he never attempted to organize another uprising, pretty much guaranteeing the eventual decline of the Stuart dynasty and marking the definite end of an era for Scotland."
        ka "Many of his followers weren't so lucky though. The son of the King, the Duke of Cumberland, was more concerned about squashing the insurrection than about appearing gracious in victory."
        ka "After the battle, he had his soldiers search the battlefield for enemy survivors and execute anyone who was still capable of breathing. Afterwards his troops were sent out to hunt down the escaped enemy soldiers."
        ka "They were particularly vicious about it, burning suspect settlements to the ground and killing all soldiers believed to be rebels. All in all, not a day fondly remembered around here..."

        show karla basic_resigned_cas
        with chchange

        stop music fadeout 2.0

        "As Lilly's mother finishes her story she looks in our direction and suddenly trails off."
        ka "Hey, are you okay?"
        hi "Eh, sure. Why?"
        ka "I meant Hanako."

        play music music_rain fadein 4.0

        hide karla
        show hanako emb_downtimid at tworight
        with charaenter

        "I look behind me and notice that unlike Lilly and me, Hanako hasn't gotten off the bike during Karla's story and something about her posture seems off."
        "She's a bit hunched over her handlebar and she hangs her head as if she's on the verge of falling asleep."
        hi "Hanako?"

        show hanako emb_sad
        with chchange

        ha "I'm... o-okay."
        "She doesn't look or even sound okay."

        show bg:
            zoom 1.02
        show hanako emb_sad_close
        with characlose

        with vpunch

        "She lifts her leg in an attempt to get off the bike, but then wobbles a bit and the only reason she doesn't end up falling on her face is because I manage to make my way over to her and catch her before she loses her balance completely."

        hide hanako
        with charaexit

        "Gently lowering her to the ground, I'm startled when I notice her complexion is paler than when we left, her forehead is covered by numerous tiny beads of sweat, and her breathing seems slightly shallower than it should be."
        hi "Hey, what's wrong?"

        show karla basic_annoyed_cas
        with charaenter

        "Lilly's mother kneels down next to us and gives Hanako an analyzing look that makes her instinctively avert her head. Karla doesn't back off though, and after a few moments she turns to me."
        ka "I think we just found our picnic spot. Let's head over to that patch of trees on the other side of the road, give her some shade and start unpacking things."
        ka "Hisao, you get her there. Lilly, can you help me unpack the saddlebags?"
        li "Ah... Yes, of course."

        scene bg inverness_cullodenpicnicspot
        show hanako emb_downtimid at center
        show lilly cane_sad at left
        show karla basic_distant_cas at tworight

        "I take one of Hanako's arms, put it around my neck and lift her up from the ground. Acting as her crutch, I walk her to the trees Lilly's mother pointed out and get her settled with her back leaning against the largest tree of the bunch."
        "Karla moves the tandems over to our side of the road, and Lilly spreads the blanket and starts unpacking the various sandwiches and salads she and Hanako made earlier today."
        "Suddenly, Lilly's mother takes a bottle from the blanket, holds it to her ear and shakes it a few times."
        ka "Hmmm, did you happen to put ice cubes in this thermos bottle?"
        hi "Yes. They were meant to go with the soft drinks we took along."
        ka "Great. I'll borrow a few if you don't mind."
        "Lilly's mom takes a handkerchief out of her pocket, puts some icecubes on top of it which she chips into tiny pieces with the handle of one of the spoons we brought along, folds it and then hands it to Hanako."
        ka "Just keep this pressed against your forehead and neck. It'll help."
        hi "Help against what?"
        "Lilly's mother turns to me."
        ka "It looks to me like she caught a minor case of heat exhaustion. Or at least the beginnings of one."

        show karla basic_angry_cas

        "For a moment a stern expression appears on her face."
        ka "When I said that it was important for you guys to drink plenty this morning after your little party last night, I wasn't joking around."
        "I hope she's not blaming me for Hanako's condition. If I had known, I wouldn't even have accepted a sip from her water bottle."
        "Come to think of it, I really hope she wasn't saving half of her own bottle for me while neglecting herself. It's not something I'd completely put past Hanako."
        hi "She did drink until she wasn't thirsty anymore this morning."

        show karla basic_ponder_cas

        ka "Not being thirsty anymore and being properly rehydrated are two different things. Anyway, there's no point in griping about that now. I suggest we simply go on with the picnic and see how things proceed for now."

        show hanako emb_timid

        "I can hear Hanako sighing in relief. I know she'd seriously feel bad if this picnic were to be cancelled over her. Lilly's mother gives her a determined look."
        ka "But you'll be drinking an additional share of the beverages, and if you're not feeling any better within 30 minutes, I'm going to call someone to pick us up. Okay?"

        show lilly cane_displeased

        "Karla's words are emphasized by a rather strict nod from Lilly. Hanako's face drops a bit again, but she nevertheless nods meekly."

        show hanako emb_sad

        ha "O-Okay."
        "Lilly's mother relaxes upon hearing Hanako's reply and fishes the remaining food out of our saddlebags. She then raises a bottle of juice before tossing it to Hanako."

        show karla basic_smile_cas
        show lilly cane_weaksmile

        ka "Well cheers then."

        scene black
        with Dissolve(2.0)
        scene bg inverness_cullodenpicnicspot

        play music music_tranquil
        show hanako basic_bashful at twoleft
        show karla basic_cheerful_cas at right
        show lilly basic_smileclosed at left

        ka "Could I have some more of that macaroni salad?"
        "Fortunately, the beverages, shade and cold handkerchief did end up improving Hanako's condition, and 30 minutes later our picnic is in full swing."
        "Lilly has taken a seat next to Hanako, and both are lazily leaning back against the tree we're sitting under. Lilly's mother and I have made ourselves comfortable on the other ends of the blanket just out of range of the sun."
        ha "S-Sure."
        "Hanako reaches out and hands Lilly's mother the bowl of macaroni salad. She really seems to like the stuff, which hasn't escaped Lilly's attention either."

        show lilly basic_smile

        li "You seem to have a taste for it, Mother."
        ka "It's delicious. What exactly are these little light-green pieces?"

        show lilly basic_listen
        show hanako basic_distant

        li "Hmmm..."

        "Both Lilly and Hanako think for a moment."
        ha "They're... um... c-chopped olives with pimiento."
        ka "They really add to the flavor."

        show karla basic_smileclosed_cas

        ka "You're a pretty good cook, dear."

        show lilly basic_cheerful

        "Lilly beams upon hearing those words."
        li "Thank you. But Hanako deserves credit as well. She's put in a lot of work too."

        show hanako def_worry

        ha "..."
        "For a moment, Hanako and I share a confused look. I could be mistaken but I could swear Lilly's mother looked at Hanako while delivering her compliment. But before any of us can say anything, Karla has already filled up the momentary silence."
        ka "Thumbs up to both of you then."

        show hanako basic_normal
        show lilly basic_smileclosed

        "Deciding not to dwell on the subject, I ask Lilly's mother the question that's been on my mind since the little history lesson she gave us earlier."
        hi "You seem to know a lot about the area. Are you originally from Inverness?"

        show karla basic_cheerful_cas

        "Lilly's mother nods proudly."
        ka "Yep. Born and raised in the Highlands. Though before I moved to Japan, my work used to take me all over the UK."

        show karla basic_smug_cas

        ka "If this is about those history lectures I've been throwing around; I've had practice in the last few days. I've been playing tour guide all weekend for that business delegation that came to visit."

        show lilly basic_surprised

        "Lilly cocks her head slightly."
        li "Akira has told us about that. It must have been... something major for you and Father to spend the whole weekend like this."

        show karla basic_wistful_cas

        "Lilly's mother gives her daughter a slightly guilty smile."
        ka "Your father and I weren't happy about not being able to pick you guys up from the airport, but... Yes, it kind of was. Probably the biggest event that's happened to the company in over a decade."

        show lilly basic_weaksmile

        li "Akira mentioned a takeover."
        ka "That's right."

        "Sensing that this subject is going over our heads, Lilly's mother looks at Hanako and me."
        show hanako basic_worry
        show karla basic_smile_cas

        ka "I'm not sure how much Lilly and Akira have told you about the family business."
        hi "Not much. Akira hardly ever talks about her job. I only know from Hanako that Akira's a lawyer in your husband's company."

        show karla basic_smileclosed_cas

        ka "It's not really his company, at least not yet, but he does run it for all practical purposes. Are you guys interested in a short summary?"
        hi "Sure."
        "Karla grabs one of the sandwiches Lilly and Hanako prepared, takes a big bite out of it and thinks for a moment."

        show lilly basic_smileclosed
        show karla basic_ponder_cas

        ka "The name of the company is Satou Medical Technology and it's a family company that was founded by my husband's grandfather."
        ka "Eventually his son inherited the business and expanded it using capital provided by his two younger brothers who both married into banking families and went into the business of investment banking."
        ka "The three of them are still the only members of the company's board of directors and officially have the final say on everything."

        show lilly basic_concerned
        show karla basic_smug_cas

        ka "In practice however, it's my husband, who was appointed CEO 6 years ago, who makes just about all the daily decisions and not the old men club in Japan."
        ka "From what I've heard, their board meetings are little more than social events these days. None of them are really in a good condition anymore to go from business meeting to business meeting abroad to begin with."

        show hanako basic_distant

        "Lilly cringes a bit at her mother's playful, and not overly respectful, choice of words, but doesn't interrupt her explanation."

        show karla basic_smile_cas

        ka "The company started out producing medical devices like EKG's and respirators for hospitals though nowadays we're also involved in the production of heart rate monitors and AEDs, which can be also sold to consumers and businesses."

        show lilly basic_weaksmile
        show karla basic_sheepish_cas

        ka "I guess there's no need for me to explain those abbreviations, is there?"
        hi "No, I guess not."

        show hanako basic_worry
        show lilly basic_smileclosed
        show karla basic_ponder_cas

        ka "Our company has had business contacts in the UK and in Inverness in particular for a long time, and eventually we managed to open a second branch by taking over an existing company here."
        ka "There's a well-developed medical industry around these parts and the Scottish government has taken steps to stimulate the sector, so eventually our Scottish branch outgrew its Japanese counterpart."
        ka "That's when the board decided to move head office to Scotland with my husband, as the family's heir, being instated here as CEO."
        hi "And now you're planning to open another branch in the US?"
        ka "It's not exactly a done deal yet, but that's what we're shooting for."
        ka "Ever since we got here, my husband and I have been working hard at setting up a network of contacts in the US, and we're scheduled to travel there and take part in the final negotiations a few days after you guys return to Japan."
        ka "If everything goes well, we'll be able to enter the North American market, and my husband will have honored an important family tradition."
        hi "Family tradition?"

        show lilly basic_weaksmile

        show karla basic_lost_cas

        "Karla's face becomes more serious as she continues."
        ka "The Satou family places a lot of pressure on its heirs to perform and perform well."

        show karla basic_distant_cas
        with chchange
        show karla basic_wistful_cas
        with charachangealways

        "For less than a second she averts her eyes as if wanting to voice silent disapproval, but she then directs her gaze back to us."
        ka "My husband's grandfather started the business and my father-in-law expanded it significantly with the opening and maturing of the Scotland branch as his crowning achievements."
        ka "With another branch opening in yet another part of the world, my husband feels like he will have brought honor to his family and to the achievements of his predecessors. To say that this whole thing is extremely important to him is an understatement."
        ka "It isn't just about work to him anymore, but about being able to face his family and the memory of his ancestor with pride. The Satous are kind of traditional, and family honor is a big thing with them. Heh, samurai spirit and all."
        "She's probably talking about her extended family as I know that neither Lilly nor Akira are happy about their parents having moved here."

        show lilly basic_smileclosed

        hi "What's your job in the company? Are you your husband's secretary? You seem to be closely involved with his activities."

        show karla basic_laugh_cas

        "Lilly's mother laughs and then shakes her head."
        ka "Heh, you think he'd take an office lady along to his business meetings? Him being married to his secretary would be kind of cliché, wouldn't it?"

        show karla basic_cheerful_cas

        ka "It's actually not that far from the truth. Especially when we first moved here I often acted like his secretary while he was still getting the hang of western business culture."
        ka "But my official position is being in charge of public relations. I have accumulated a fair bit of unofficial clout on the workfloor though."
        ka "I've been extremely involved in this whole deal as well, which is why I'll be accompanying my husband in a few weeks to see this thing through."
        "I'm a bit surprised to hear that Lilly's mother's working alongside her husband - almost like an equal business parter from the sound of it."
        "If the Satous are really this traditional, wouldn't they consider a married woman working to be inappropriate? Especially at such an influental position."
        hi "Did you already work for the company before you moved here?"

        show karla basic_sweet_cas

        "Lilly's mother shakes her head."
        ka "No, I've been a stay at home mom the whole time during my married life in Japan. I didn't even know I had a knack for this thing until I came back here and joined the PR department."

        show karla basic_ponder_cas

        "She pauses for a moment, takes a bite out her sandwich, sips from her can of soda and then fidgets a bit with the blanket before continuing."
        "I recognize this gesture as an indication of unease, since Lilly occasionally shows the same trait when she's about to talk about an uncomfortable subject."
        ka "Before our Inverness branch also became our head office, we used to have a local manager running things here. When head office relocated, the board determined that a Satou had to be in charge of it."

        show lilly basic_sad

        ka "Shortly after moving here, my husband indicated that he needed someone to help him bridge the culture gap between himself and his employees, so he that could become a better manager for his personnel."
        ka "Someone with personal experience with both the Western and Japanese culture. Someone he felt he could trust and have his best interests at heart."
        ka "He chose me to fill that role, the board eventually complied with his request, and I ended up answering his summons, eventually joining the PR department."

        show lilly basic_weaksmile

        li "I'm glad you've been doing so well for yourself, Mother."
        ka "Thanks."

        show hanako basic_distant
        show karla basic_wistful_cas

        "I notice Karla's eyes are not directly looking at Lilly during her daughter's comforting words, and for a moment her smile seems extremely forced. Their migration is obviously still a sensitive subject to her."
        li "In a way, it's not very surprising you ended up performing so well. Your old job and your current one have much in common, after all."

        show karla basic_sheepish_cas

        "Lilly's mother lets out a playful laugh at her daughter's remark."
        ka "Hehehe, don't go telling that to any of my old colleagues. We used to believe that going into public relations was equal to selling your soul."

        show lilly basic_smileclosed

        hi "If you don't mind me asking, what exactly was your previous occupation?"
        show karla basic_smileclosed_cas

        "Karla's face brightens as if she had been waiting for me to ask that question."
        ka "Journalism. I used to be a business correspondent writing for the economic and business pages of The Herald, a newspaper located in Glasgow. Later, I moved to Japan and became a foreign correspondent for the BBC."

        show hanako emb_timid

        "Journalism huh? That's quite the recurring topic these days. I can see Hanako, who's been quiet for pretty much the entire time we've been here, perking up ever so slightly at Karla's words."
        ha "J-J-Journalism...?"
        ka "Yep."
        "I can tell that the conversation subject has caught Hanako's attention, but it's clear that she's not yet comfortable enough around Lilly's mother to ask her for details about her former job. Fortunately, Lilly takes this moment to come to Hanako's aid."

        show lilly basic_smile

        li "Hanako has recently joined the newspaper club at Yamaku and has already been involved in the production of two issues. She seems to enjoy the activities so far and has been playing with the thought of studying journalism or something related to it."

        show karla basic_laugh_cas

        "Lilly's mother's smile grows brighter."
        ka "Ah... Japanese school club life. Shame we didn't have a newspaper club at my old high school. That would have been fun."

        show karla basic_cheerful_cas

        "She looks at Hanako with a curious twinkle in her eye."
        ka "I suppose you didn't bring one of those issues along with you, did you? I would have liked to read a copy."

        show hanako basic_bashful

        "Hanako meekly shakes her head, but Lilly takes her handbag, zips it open and casually takes a copy of the lastest school newspaper out of it."

        show hanako def_worry
        show lilly basic_planned

        li "Coincidentally, I happen to have one on me."

        show karla basic_smileclosed_cas

        "Lilly's mother chuckles briefly at the dumbfounded look on my and Hanako's faces and then takes the newspaper from her daughter."

        show karla basic_smile_cas

        "She takes a pair of reading glasses out of her pocket, puts them on and starts thumbing through it. While she's doing so, I roll my eyes at Lilly."
        hi "That may very well have been the most inappropriate use of the word 'coincidentally' I've ever heard in my life. It isn't even a Braille edition for crying out loud."

        show lilly basic_cheerful

        "Lilly grins mischieviously, but doesn't say anything back. Her mother, on the other hand, looks up from the paper."

        show hanako basic_bashful
        show karla basic_cheerful_cas

        ka "You also print your copies in Braille?"
        "Hanako nods."
        ha "It's...p-pretty tough at times. W-We... ummm... c-convert the f-files with a computer program. The c-copyshop's Braille p-printer can then w-work with them. We h-have l-large font editions too... ah... f-for s-students with l-limited vision."
        ka "That's pretty neat. Is it a lot of work making all those different editions?"

        show hanako emb_emb
        show lilly basic_smileclosed

        ha "The... ah... Braille e-edition can t-take a few hours. We usually... just p-print the large f-font edition on larger p-paper to s-save time."

        show karla basic_lost_cas

        "Lilly's mother gives Hanako a slightly worried look. She's probably noticing how much Hanako is stumbling over her own words."
        ka "I can get a bit carried away on the subject at times. Is it okay for me to be asking you these questions?"

        show hanako def_worry

        ha "Of c-course."
        "Hanako immediately nods her head, not wanting her shyness to be taken the wrong way. Lilly's mother seems satisfied with that reaction and proceeds to skim through the paper. A few minutes later, she closes the newspaper and turns to Hanako again."

        show karla basic_smile_cas

        ka "It reads here that you were involved with both the editing and the writing. What articles did you work on?"
        ha "Ummm... O-only one s-so far. The c-column about the science c-club."

        show hanako emb_timid

        "Lilly's mom opens the newspaper again and starts reading through Hanako's column a second time. Hanako visibly tenses up a little bit, and she's looking at Karla with a slightly worried expression. Eventually, Lilly's mother closes the newspaper again."
        ka "Would you be open to some constructive criticism, dear?"

        show hanako emb_downsad
        with chchange
        show hanako emb_timid
        with charachangealways

        "Hanako's eyes widen for a moment before her face drops, and her gaze wanders towards her feet. Eventually though, she nods softly."
        ka "First of all, the language use and sentence structure are good. I really can't complain about that. But I do have one question. Does your boyfriend happen to be a member of the club this article is talking about?"

        show hanako defarms_shock
        show lilly basic_smile

        ha "Ah... ummm..."

        show karla basic_smug_cas

        "Lilly's mother flashes us a cheeky grin as Hanako's mouth falls open for a moment."
        ka "Haha, looks like I hit the bullseye."
        ha "H-How...?"

        show hanako emb_timid
        show lilly basic_smileclosed
        show karla basic_cheerful_cas

        ka "To be honest it was a bit of a guess. The impression I got from your article is that you were trying to convince readers to join the science club. You aren't blatant about it, but the message is still there when you read between the lines a bit."
        ka "I figured you were trying to surprise your boyfriend. It's a really sweet gesture, but you need to be careful not to adopt bad habits."

        show hanako cover_worry

        ha "B-Bad habits?"

        show karla basic_ponder_cas

        ka "A journalist's primary duty is to report the news and inform the public. People like to think of the news as a tool to help them form their own opinion."
        ka "If you subtly start making a case for something in your article, no matter how noble, people might become wary of reading your work because they don't like the idea of you trying to steer their opinion in a specific direction."
        ka "Now, some news organisations are leaning heavier towards certain political mindsets than others, but as a rule you want to try and be as objective as possible. Especially as a journalist who is still starting out."

        show hanako basic_normal

        "Wow, she's pretty passionate about this subject. Hanako seems taken aback by her response, but also somewhat impressed."
        ha "Ummm... N-Naomi... I-I mean the editor-in-c-chief w-wanted to p-promote c-club membership."

        show karla basic_cheerful_cas

        ka "Really? Well... In that case, I guess it's alright. I could tell you to forget what I said, but I still think it's sound advice to keep in mind. Although... If you actively start promoting something, you're not really practicing journalism anymore, but..."

        show hanako basic_bashful

        "Lilly's mother trails off before completely finishing her sentence, but I realize with some amusement what she's trying to say and fail to resist a chuckle."
        hi "You'd be practicing PR instead of journalism. Perhaps the two are closely related after all."

        show karla basic_sheepish_cas

        "Lilly's mother lets out a sigh of defeat."

        ka "I guess backed myself into a corner with that one. To tell you the truth, I'm not completely innocent myself."
        ka "When my husband and I were still dating I wrote a series of articles about the Satou company, distributed over several magazines and newspapers here. Though I did put more effort than usual into making them as objective as I could."
        "Lilly smiles at her mother's remark."

        show lilly basic_satisfied
        show karla basic_sweet_cas

        li "I never knew that. What did Father think of that?"
        ka "It was a joint effort on our part. He supplied me with whatever information I needed, and I ended up letting his company take advantage of the network I built here over the years."
        "She shrugs."
        ka "I was also hoping it would give me a positive standing with my future in-laws."

        show lilly basic_smileclosed
        show karla basic_wistful_cas

        hi "Ahah."
        ka "After our marriage my husband and I lived with his parents and grandmother for quite some time until we moved to a house two streets away from where they lived."
        ka "Heh, they used to say that even when not living in the same home, extended family should still live near enough to carry over a bowl of hot soup. I think it's a Japanese proverb of some kind they were reciting."
        "She pauses briefly while thinking to herself for a moment."
        ka "A bit ironic that they ended up giving my husband a job that sent him off to the other end of the earth, isn't it?"
        hi "What became of them afterwards?"

        show karla basic_ponder_cas

        ka "My husband's grandmother passed away before Lilly was born, and I doubt even Akira remembers much of her."
        ka "The care of my in-laws was a bit of a problem when we moved, since it was also my husband's task as the oldest son in the household to take care of them."
        ka "The company took priority though, and we ended up hiring housekeepers and a private nurse to look after them in our place."
        hi "A private nurse?"
        ka "Their physical condition started deteriorating around the time my father-in-law retired. In fact, his retirement was a result of something that took a major hit on his health. My husband decided to better be safe than sorry."
        ka "In the end, they ended up moving to a smaller residence somewhere else shortly after we left. They're both still alive, but I don't think they get out much anymore."

        show lilly basic_weaksmile

        "Lilly smiles sadly."
        li "It's a shame. I was looking forward to getting to know Grandfather better after he finally got around to retiring as head of the company. He was absent so often while he was still working that I barely got to know him at all."
        li "It also felt strange at first to no longer have Grandmother drop in unexpected to see how we were doing or take us for walks like she had been doing for as long as I could remember. After they moved, contact faded out sooner than I expected."

        show karla basic_distant_cas

        "Lilly's mother appears lost in thought for a moment after hearing her daughter's words but then turns back to us."
        show karla basic_smile_cas

        ka "Let's not dwell on depressing subjects for too long."

        show hanako basic_worry
        show lilly basic_smileclosed

        "She gives Hanako a quick nod."
        ka "Hanako, do you mind if I ask you another question?"
        ha "Ummm... N-no."
        ka "Not everyone interested in journalism is drawn to it for the same reasons. Some simply want to be able to travel and see the world. Others do it out of idealism. There are probably a ton more reasons. I'm really curious about yours."

        show hanako basic_distant

        ha "Ermmm..."
        "It's possible Hanako never really thought about that herself yet as she remains in thought for a long time before replying to Lilly's mom."

        show hanako emb_smile

        ha "I... enjoy working on our n-newspapers. Right now it's m-mostly editing and c-correcting, but it made me think... I'd... like to s-start w-writing myself. I usually get... g-good marks f-for essays."

        show karla basic_sweet_cas

        ka "You like writing, huh? That's a pretty good motivation."

        show hanako emb_downsad

        ha "But I... d-don't think I'd b-be a good journalist. I'm... r-really bad with p-people."
        ka "I did notice you're rather soft-spoken. There are some ways around that though. I've had some colleagues who were rather introverted."

        show hanako emb_sad

        ka "They usually teamed up with a more talkative partner and conducted their interviews in pairs with one doing the talking and the other observing and taking the notes. Or they let their partner do the interviews while they did the research at the office."

        show hanako basic_normal
        show lilly basic_smile

        "Lilly takes this moment to chip in."
        li "Perhaps being out in the field approaching people would not be the ideal occupation for Hanako. If she likes writing so much, maybe she should try become a writer instead. But is there a specific study for that?"

        show karla basic_smile_cas

        ka "Are you talking about fiction? Writing fiction for a living is nice work if you can get it, but it's definitely not the most stable career in the world."
        ka "Writing non-fiction is more predictable though. There are many people who want to publish something but lack either the time or the skills to write up something themselves, so they hire a ghost writer or biographer to do the job."
        ka "Then there's copywriters, whose activities are somewhat related to what I do these days, content writers, report writers, technical writers and speech writers."

        show hanako basic_worry
        show lilly basic_smileclosed

        ha "That's... a l-lot of options."

        show karla basic_ponder_cas

        ka "Indeed. On the journalistic side there are the options of editing, copy editing and research or fact checking. Now, there are probably studies that deal with these areas. Let me think..."
        "Lilly's mother absentmindedly twirls with one of her hair locks for a moment before suddenly snapping her fingers, causing Lilly to flinch."

        show lilly basic_surprised

        li "Please don't do that anymore, Mother. It's a really grating sound."

        show hanako basic_smile
        show lilly basic_smileclosed

        show karla basic_smile_cas

        ka "Hmmm? Oh, alright. Anyway, dear, a lot of writers here have a background in either English or journalism. There are universities here that offer a degree in English and Journalism. That's one study, mind you."
        ka "It covers various topics related to media in general, its role in society and various aspects of literature. There might even be an option to take a minor in creative writing."
        ka "Now, I'd be VERY surprised if they didn't offer a similar degree in Japan. You should ask when you're back at Yamaku."
        ha "O-Okay."

        show karla basic_cheerful_cas

        ka "Also remember that it always pays off to practice your writing skills. Have you ever engaged in any writing other than that column and essays for Japanese classes?"

        show hanako emb_emb

        "Hanako softly shakes her head."
        ha "N-No. I r-read a lot, but..."
        ka "It pays off to be well-read, but it's no substitute for actual practice. Maybe this week would be a good moment to start."

        show hanako emb_sad

        ha "S-Start? I... ah... am working on a n-new column for the n-next newspaper, but..."
        ka "I'd love to read it when it's done, but that wasn't really what I was talking about. This may be an intimate question, but... do you keep a diary or a journal?"

        show hanako emb_timid

        ha "N-No."
        ka "Maybe you shoulder consider keeping one. At least for the time you're here. Not for peer-review of course, but simply to start some good habits."
        ha "Good h-habits?"

        show karla basic_smile_cas

        ka "Yep. See it as writing your own little private newspaper summarizing everything that happens during your stay here. Take an hour or so a day to update it. Stick with that one hour so you train yourself to work within the bounds of a limited timespan."
        ka "If you take it seriously, processing and sorting information about events as they happen and memorizing the relevant details while dismissing the unimportant clutter will quickly become a second nature to you."
        ka "These are skills that both journalists and writers greatly benefit from. If you're interested I probably have some unused diaries and notebooks lying somewhere in the study or the attic. Maybe you could take pictures too."

        show hanako emb_smile

        "Hanako seems to have trouble keeping up with Karla's enthusiasm, but eventually she nods with a small smile on her face."
        ha "Maybe it's w-worth the t-try."

        show karla basic_smileclosed_cas

        "Lilly's mother sends us a triumphant grin and shoots a glance at the place where Hanako's handbag is lying."
        ka "Excellent. Is that camera still in your bag, dear?"

        show hanako basic_bashful

        ha "Ummm... Yes."
        ka "Good. Hisao, could you sit down next to her for a moment? Lilly, could you get a little closer?"

        show lilly basic_cheerful

        "Lilly's mother takes Hanako's handbag, fishes the camera out of it and takes a few steps back to make certain that everything that's on the blanket is in frame. As Lilly and I take a seat on both sides of Hanako, Karla aims the camera at us."

        show karla basic_laugh_cas

        ka "Smile people! It's essential to get front page pictures right."

        stop music fadeout 2.0
        scene black
        scene bg inverness_cullodenpicnicspot
        play music music_pearly
        show lilly basic_smileclosed at center

        hi "So,Lilly..."

        nvl show dissolve
        n "{vspace=60}If I readjusted my watch to Greenwich Mean Time correctly, it should be six o' clock right about now. Lilly and I are busy collecting the various bowls and plates that were strewn across the blanket and putting them back in the saddlebags."
        n "{vspace=60}Hanako is still sitting in the spot she's been occupying all afternoon, gently rubbing her calves with a slightly uncomfortable expression on her face. She appeared alright during most of the picnic, but got slight cramps shortly before we decided to head back home."
        n "{vspace=60}Lilly's mother is standing some distance away from us, engaged in a phone call on her cell phone."
        nvl clear

        li "Yes, Hisao?"
        hi "That hour-long journalism-based sales pitch... Was that all 'part of the plan'?"

        show lilly basic_giggle

        "Lilly puts her hand in front of her mouth to suppress a giggle."
        li "Would you believe me if I said it was not?"
        hi "You'll at least have to tell me that with a straight face if you want to convince me."

        show lilly basic_smileclosed

        "Lilly chuckles briefly."
        li "Hanako told me about her plans for the future during one of our nights on the town a few weeks ago. I knew Mother used to be a journalist, so I hoped she'd have some advice for Hanako."
        li "That's also why I asked Naomi for an additional copy of the newspaper. But... I hadn't anticipated this."
        hi "Not anticipated what?"

        show lilly basic_weaksmile

        li "You may not believe me, but before she left Japan Mother hardly ever spoke about her old profession at all. I was just as surprised by her passion as you were."
        hi "That's kind of hard to believe."

        show lilly basic_concerned

        "Lilly pauses for a second, then briefly turns her head in Hanako's direction."
        li "Hanako must have been overwhelmed by Mother's reaction."

        show lilly basic_smile

        hi "Yeah she was, but she also seemed interested in what your mother had to say. That's certainly a good thing."
        li "I agree."

        scene bg inverness_cullodenbattlefield
        show karla basic_smile_suit at tworight

        "Having finished packing up, Lilly walks back to Hanako's location and sits down next to her best friend. I notice that Karla has finished her phone conversation while Lilly and I were talking and walk up to her."
        hi "I know we're getting ready to head back, but I don't think Hanako's in good shape for another bike ride just yet."

        show karla basic_lost_cas

        ka "She's not hurting badly, is she?"
        hi "She seems uncomfortable, but not in a lot of pain."
        ka "We won’t be riding our bikes back. I phoned Allison a few minutes ago and she's on her way to pick us up."

        show karla basic_distant_cas

        "Lilly's mother shoots a brief glance in Lilly's and Hanako's direction."
        ka "Light heat cramps, it seems. They'll subside on their own. All she needs is some rest, a nutritious meal and plenty to drink. She'll have all of that when we get back home."
        hi "Good thing we had shade, ice and drinks nearby."
        ka "True. Maybe we shouldn't have focussed our concerns on just you the way we did."
        "She takes another brief glance at Hanako and then looks me straight in the eyes."

        show karla basic_lost_cas

        ka "Hisao, this is probably an intimate question, but... Hanako's scarring... It's not just on one side of her face, is it?"
        "I'm taken aback for a second by her sudden mention of a subject this delicate."
        hi "She really doesn't like it when people bring it up."
        ka "I can imagine. It’s not really morbid curiosity or anything. It’s just…"
        hi "Yes?"

        show karla basic_distant_cas

        "She opens her mouth to say something, but then suddenly raises her arm and waves. When I turn around, I can see a car with a familiar trailer behind it approaching us from the west."

        show karla basic_wistful_cas

        ka "I'll tell you later if you're still interested. The gist of it is that I just confirmed that I've been a total idiot today. And I sincerely apologize for that."
        "She walks over to the side of the road, exchanges some words with the housekeeper as she exits the car and then nods in my direction."
        ka "Allison and I will handle the bikes and the saddlebags. You just get Hanako and Lilly in the car, okay? If all goes well, we'll be home in less than 15 minutes."

        stop music fadeout 2.0
        scene black
        with Dissolve(2.0)

        return