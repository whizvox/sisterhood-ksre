label sh_ch37:
    label .s1:

        $ set_window_tint(TINT_LILLY)

        call sisterhood_timeskip

        scene bg satou_kitchen
        with Dissolve(2.0)

        play music music_normal fadein 4.0

        nvl clear
        nvl show dissolve

        n "The sounds of footsteps approaching the kitchen draws my attention away from the cupboard containing what I believe to be various cooking implements. I've been trying to memorize the layout of the kitchen and the contents of the cupboards and drawers since the start of this week. Due to the size of the kitchen, this is not exactly a small task."
        n "{vspace=30}As the footsteps get closer, I softly tilt my head to try and determine the identity of the person approaching me. From the sound of the heels, it must be a woman, so that rules out Father. The footsteps' pace is also too quick and steady to be his."
        n "It could be Allison. Or perhaps Fiona, the cleaning lady. From what I've noticed, Fiona's pace is more energetic than this, so that must mean Allison has returned from her shopping trip."
        n "{vspace=30}I turn around and try to face the doorway so I can greet the person walking into the room."

        nvl hide dissolve

        li "Good afternoon, Allison. You're back sooner than I expected."
        "Allison" "Good afternoon, Miss Lilly. I was lucky it wasn't very busy at Raigmore's apothecary, so it only took a few minutes to get your father's latest batch of medication."
        li "I greatly appreciate it. May I ask you a question?"
        "Allison" "Of course."
        li "When we have visitors here, do we usually serve green or black tea?"
        "Allison" "It depends on the visitors. We offer both out of courtesy, but people from around here usually stick with black and the few times your father has Japanese visitors over they usually prefer green."
        li "Do you often have visitors here?"
        "Allison" "Your mother has visitors almost weekly. There are friends with whom she goes on bike rides around the countryside, and they usually have tea before and after the ride. She's also chairwoman of the neighborhood association, and meetings often take place in this house."
        li "Mother certainly lives an active life. Doesn't she ever take it easy?"
        "Allison chuckles as if I just told her a very funny joke."
        "Allison" "I do not think your mother is the type for that."
        "I smile wistfully. Mother has changed so much from the way I remember her. Back in Japan she hardly ever left the house and wouldn't even go to my school's PTA meetings or take us to the park."
        "Would I change this much if I had decided to move here? It's a bit of a creepy thought. I like the way I am."
        li "How about visitors for Father?"
        "Allison" "People from the Japanese branch occasionally stop by in Inverness, and your father lets them spend the night here instead of at a hotel."
        "Allison" "He always looks forwards to their visits, and when they stay here, we are asked to treat them like royalty. But such a thing only happens once every four months or so."
        li "We will be getting a visitor from Father's office later this day. He called earlier today, and he asked if it was okay if he stopped by after work to drop off some equipment for us."
        "Allison" "I see. That means he will probably be here within 40 minutes or so. But I don't think your father would appreciate it if we let that colleague come up into the master bedroom."
        li "No, he would not. I think it would be best if we receive him in Father's study. Isn't that where he usually has his guests?"
        "Allison" "It is. So what would you like me to do, Miss Lilly?"
        li "Ahem..."

        nvl clear
        nvl show dissolve

        n "This is a bit awkward. Two days ago, Mother took a flight to the United States together with a business delegation consisting of Akira, Kojima, and a few more colleagues, leaving Father and me as the sole residents in this house."
        n "Allison was supposed to be responsible for running the day-to-day things here, but only minutes after we left Inverness airport, she started getting slightly more formal than usual and explained that as far as she was concerned, I was the lady of the house right now and officially in charge of the household."
        n "{vspace=60}I was taken aback by that at first, but over the last two days, I've slowly started growing into the role that had been handed to me."
        n "{vspace=90}Although I'm not about to admit it out loud, I am somewhat enjoying it."

        nvl hide dissolve

        li "Perhaps it would be good if Fiona could make certain that the room is cleaned and vacuumed. Because of its distinct appearance, our visitor is certain to pay close attention to the state of its interior."
        "Allison" "As you wish. If I give Miss Wilson a hand, I am certain we'll be able to have it looking prim and proper in 10 minutes."
        li "Wonderful. After Father's colleague called, I made a phone call to the nurse we hired to do Father's daily checkup, and she thinks he should be able to handle a short meeting as long as he rests up afterwards."
        li "When our visitor arrives, I could perhaps do the serving while you wake up Father, make certain he looks presentable, and help him down the stairs. I might have trouble with some of those tasks myself."
        "Allison" "Not a problem. Do you wish me to help you make the tea, Miss Lilly?"
        li "I think I can manage. Assuming everything is still in the same place as it was yesterday."
        "Allison" "It should be. I brought some tasty biscuits along to go with the tea. I put the box containing them on the second shelf of the cupboard next to the fridge."
        li "Shall we get started then?"

        scene bg satou_stairs
        with shorttimeskip

        li "Good afternoon. May I help you?"
        "After the doorbell rang, I made my way over to the front door, while Allison went to help Father get out of bed."
        "I do hope he will be okay. It's only been about two weeks since his heart attack and he's only been home for a few days."
        "Visitor" "Good afternoon. Geoffry McLaughlin. We spoke on the phone two hours ago."
        "I make a gracious bow towards him."
        li "Welcome, Mister McLaughlin. I am Lilly Satou. This way please. My father will be with you shortly."
        "Mr. McLaughlin" "Thanks."
        "I make my way back to the study with McLaughlin following close behind."
        "Mr. McLaughlin" "Wow, nice place you've got here."
        li "You're flattering us."
        "He chuckles briefly at my response, but doesn't say anything back."

        scene bg satou_study
        with locationchange

        "When we reach the study and I open the door for him, he lets out a soft ‘holy shit’ under his breath."
        li "Please take a seat while I get you some tea. Would you prefer black or green tea?"
        "He pauses for a bit, probably wondering whether it's okay to let a blind person serve him hot tea, but then responds."
        "Mr. McLaughlin" "Black with just a dash of milk, please."
        li "Certainly. I will be right back."
        "Mr. McLaughlin" "One question if you don't mind."
        li "Of course."
        "Mr. McLaughlin" "Do you have Wi-Fi in this place?"
        li "Ah... Wi-Fi?"
        "Mr. McLaughlin" "Wireless network. I'd like to start setting things up, and it'd be good to know if I have to use the ethernet cable I brought along or if I can set up a wireless connection. Either way's fine."
        "My smile becomes a little more forced."
        "I have no idea what he's talking about. He's probably assuming that every teenager, even a blind one, knows what a ‘Wi-Fi’ is."
        li "Ah... I'm afraid I... can't help you."
        "Mr. McLaughlin" "That's fine. I'll just power up the laptop and see if it can detect any wireless routers around here. If I can find any and authorization is needed, I can ask your father for the password. Okay?"
        "{i}Translation!{/i}"
        "I force the brightest smile I can muster."
        li "That would be... good. I will be right back."

        scene bg satou_kitchen
        with locationchange

        "I quickly make my way out of the room and head over to the kitchen. I take the kettle from the stove, fill the tea pot, and think back on what just happened."
        "That was painfully embarrassing. I thank God that Father's not here right now, because he would certainly feel that I brought shame on him by my blatant display of computer illiteracy."
        "I can't let this throw me off though. After preparing the tea—and some fruit juice for Father—I carefully head back to the study, making sure not to accidentally drop the tray while reaching for the door handle."

        play sound sfx_dooropen

        scene bg satou_study
        with locationchange

        li "I apologize for taking so long."
        "Mr. McLaughlin" "That's fine. I doubt I'd be able to prepare tea if I wasn't able to see what I was doing."
        "I pour a bit of milk into his cup and carefully fill it. Then I fill my own. I hold his cup out to him until he takes it from my hands."
        li "Please enjoy."
        "Mr. McLaughlin" "Thanks."
        li "It might take Father a few minutes to get ready. Sorry for the inconvenience."
        "Mr. McLaughlin" "No need to apologize. Suffering from a heart attack isn't something anyone would do on purpose, now is it?"
        li "That is certainly true. May I inquire what exactly do you do at the company, Mr. McLaughlin?"
        "Mr. McLaughlin" "You know, you can call me Geoffry if you wish. No need to be formal."
        "I merely smile at him."
        "If Father heard me address one of his colleagues with his first name, I'd probably get in trouble."
        "Mr. McLaughlin" "Anyway, I'm a system administrator. My colleague Alec and I are in charge of the department that maintains the computers, company network, and servers at the office. We also take care of whatever issues people have with their computer systems."
        "Mr. McLaughlin" "Hehe, in a way we're the most powerful people in the company."
        "I politely chuckle at his remark, but remind myself I'd better try and steer the conversation away from his area of expertise if I don't want to embarrass myself again."
        "Mr. McLaughlin" "Your mother came to us last week with the request to set up a digital conference system."

        nvl clear
        nvl show dissolve

        n "Indeed. During the days I spent at Father's side after he was hospitalized, it quickly became clear to me that the matter of him now missing out on the final steps of the company's expansion wasn't a passing problem. And while I was thinking on how to help him, Hanako's suggestion of a teleconference came back to mind."
        n "I first spoke to Akira about the feasibility and then later to Mother and Father as well. Mother wasn't extremely enthusiastic about going to the U.S. without Father at first, and I don't think her reluctance was out of insecurity. Rather, she seems to partially blame Father's condition on the company and wasn't eager to stick her neck out for it instead of remaining by her husband's side."
        n "{vspace=30}Eventually, I managed to convince her that helping Father tie up this loose end would be the best way to get the four of us together again."
        n "As for Father, he was reluctant as well because he considered not showing up in person to an important meeting to be an insult to his business partners—although when Mother assured him that these were special circumstances and that the people we'd be meeting wouldn't think less of him for it, he eventually relented."

        nvl hide dissolve

        li "I am glad you managed to obtain the necessary equipment so quickly."
        "Mr. McLaughlin" "Well, we've worked with stuff like this before, so it wasn't that big of a deal."
        "I hear him take a careful sip from his cup."
        "Mr. McLaughlin" "By the way, how is your dad?"
        li "He's getting better. Though it is unlikely he will be seen in the workplace any time soon."
        "I pause for a moment and then continue."
        li "Mr. McLaughlin... It is probably best to tell you in advance that my father will not be able to talk at length and can only be present for a very short while. It would be good if you could take that into account."
        "Mr. McLaughlin" "...Fair enough. I'll try not to waste any time. I kind of need to get home quickly, too."
        "Mr. McLaughlin" "Lord knows it's going to be a long night for me as well. Alec's gonna owe me quite a few pints when he gets back."
        li "Your colleague accompanied our business delegation to the United States, didn't he?"
        "Mr. McLaughlin" "Yeah, we drew straws to determine who was going to stay here and who was going to take a trip to the U.S. and stay in a luxury hotel. Three guesses who took the short one."
        "I giggle a bit at his remark."
        li "That's unfortunate for you, but I assume that someone had to stay behind."
        "Mr. McLaughlin" "Yeah, and to be honest, this was for the best. Alec's a bit of an eternal bachelor, and he can afford to go there for a week or two. I have a wife and a seven-year old waiting for me at home, and my boy has football training at six each Wednesday."
        "Mr. McLaughlin" "It'd be kinda hard to drive him there when I'm on the other side of the world. His mom could do it if necessary; I get called on emergencies from time to time, but there's usually nothing but fathers on the sidelines. Football is really a guy thing, you know?"
        li "Of course."

        nvl clear
        nvl show dissolve

        n "He's talking about it like it's normal for him to be home around that time each day. Maybe it is over here, but if that's the case, then that's a pretty big contrast from the way things were in my childhood."
        n "Even before he left the country, Father's job often kept him away from the home for six days a week and he wouldn't return from work until way after my bedtime."
        n "{vspace=60}It was this way with all fathers in the neighborhood. During these weeks where I've been by his bedside, we've probably had more extended interaction than any other time in my life I remember."

        nvl hide dissolve

        "I consider asking him about his son, but my ears suddenly pick up the sound of approaching footsteps."
        "I instinctively rise to my feet when they stop on the other side of the door, and when it opens, I greet my father with a graceful bow."

        show hiroyuki serious at right
        with charaenter

        li "Hello Father. I'm glad you could join us."

        show hiroyuki at tworight
        with charamove
        show hiroyuki bow
        with charachangealways

        hyf "Lilly. Mister... McLaughlin. Good afternoon."
        "I can tell that he's doing his best to speak at normal volume. Since speaking too loudly or even breathing too deeply is still painful and very exhausting, I doubt he will last very long."
        "There is, however, no doubt in my mind that he'll do whatever it takes to make certain his colleague won't notice."

        show hiroyuki serious
        with chchange

        "Mr. McLaughlin" "Good afternoon, sir. How are you feeling?"

        show hiroyuki thinking
        with chchange

        hyf "I am well... thank you. I apologize for the delay."
        "Mr. McLaughlin" "Not a problem. Your daughter's an excellent host."

        show hiroyuki serious_close
        with chchange
        show hiroyuki at tworight_sittingpos
        with charamove

        "I wait until he's seated, pour him a glass of fruit juice, and hand it to him."
        li "Would you like some more tea, sir?"
        "Mr. McLaughlin" "I haven't finished my first cup yet, but thanks."
        "He scrapes his throat."
        "Mr. McLaughlin" "I'll try not to take up too much of your time. Shall I start explaining how we've set up things?"

        show hiroyuki thinking_close
        with chchange

        "A short pause before responding. I know that Father prefers to start meetings off slowly with some polite small talk and that getting down to business immediately feels rude to him, but at the same time, he seems to remember the importance of saving his strength."
        hyf "Please proceed."

        stop music fadeout 2.0

        queue music music_daily fadein 4.0

        show hiroyuki serious_close
        with chchange

        "Mr. McLaughlin" "First of all, I notice there's a wireless network set up here. I can log the laptop onto it, but I will need the network password."

        show hiroyuki eyebrow_close
        with chchange

        hyf "Please... check under... the table."
        "I hear the sound of fingers probing the underside of the table surface."

        show hiroyuki serious_close
        with chchange

        "Mr. McLaughlin" "Ah! A network cable. I didn't realize that table leg was hollow. That'll do fine, too."
        "I hear a soft click as the cable he spoke of is inserted into a device on the table."
        "Mr. McLaughlin" "Looks like we have a connection to the web. This laptop here runs the conference software we've installed. This little unit next to it is the transmitter for the wireless headset."
        "Mr. McLaughlin" "The headset should be able to pick up the signal from just about anywhere inside the house. I also have a normal headset ready on the off chance of the transmitter failing."

        show hiroyuki speak_close
        with chchange

        hyf "I... beg your... pardon, but do... you have... a spare head... set?"
        "Mr. McLaughlin" "Would you like someone else listening in, too?"

        show hiroyuki thinking_close
        with chchange

        hyf "If... she is... interested."
        "I realize that Father's talking about me. I was planning to remain by his side this night, but I didn't expect being given a chance to actually listen in."
        "I doubt I'll understand much of what's discussed, but this is quite the chance to hear my parents “working”."
        li "I'd be honored, Father."
        "Mr. McLaughlin" "I have several more headsets back at the office. I'll stop by there and fetch one later this evening."
        hyf "Thank you."

        show hiroyuki serious_close
        with chchange

        "Mr. McLaughlin" "This laptop is part of a pair. Alec took the other one along to the U.S. He has a transmitter just like the one here, except it's connected to a collection of microphones."
        "Mr. McLaughlin" "Since some of those meetings in the upcoming week will be held over dinner, we felt that putting a teleconference unit on the table might be cumbersome."
        "Mr. McLaughlin" "The microphones we'll be handing out to the participants are the small, unintrusive kind. You clip them onto your lapel and then forget they are there."
        "Mr. McLaughlin" "They have a noise filter too, so you shouldn't have any problems making out what is said even if there are other discussions going on nearby, and if the volume is too soft, the conferencing software has the ability to amplify the incoming voices."

        show hiroyuki thinking_close
        with chchange

        hyf "That is good. After... all, I will not... be able... to ask them to... repeat themselves."
        "Mr. McLaughlin" "That's true. Everyone in the room will be getting a microphone, but only your oldest daughter will have an earphone, so she'll be the only one who can actually hear you."
        "Akira's job will be to act as Father's proxy. If at any point, Father wants to bring up his own points, he will mention them to Akira and it'll be her task to relay them to the rest of the room."
        "Mr. McLaughlin" "We also took the possibility into account that people might want to share documents. Alec has a small scanner with him, and I have a wireless printer in the trunk of my car. Any documents or graphs they want you to look at can be transferred from there to here in a matter of moments."

        show hiroyuki speak_close
        with chchange

        hyf "Quite convenient. I... suppose all that is... left is to ex... plain to me how to set... up the connection."
        "Mr. McLaughlin" "I think I actually have a better idea, sir."

        show hiroyuki thinking_close
        with chchange

        hyf "..."
        "I silently cringe. I'd be very surprised if Father didn't take that as an insult and the fact that I'm present here as well probably only made things worse."
        "But to my surprise, there isn't even a subtle change in tone when my father answers."

        show hiroyuki eyebrow_close
        with chchange

        hyf "What exactly... did you... have in mind?"
        "Mr. McLaughlin" "Well, I was thinking about changing the plan and being present here myself to operate the equipment. I could get things running over here while you and your daughter can relax in the room of your choosing and leave the technical stuff to me."
        "Mr. McLaughlin" "You can focus on the meetings while I keep the connection running, handle the receiving and printing of incoming scans, and immediately jump in in case of a malfunction."

        show hiroyuki serious_close
        with chchange

        hyf "You would... work from this room... then?"
        "Mr. McLaughlin" "Yeah. I can take over and control the laptop from my desk at the office, but in case of technical issues, I'd still need to drive over here, and that could take up to 10 to 15 minutes."
        "Mr. McLaughlin" "If I'm allowed to handle things here, that will also mean there won't be any need for me to spend time teaching you the ropes about setting up the connection and working with the software."

        show hiroyuki speak_close
        with chchange

        hyf "...Very well, then."
        "Mr. McLaughlin" "Great. I believe the first meeting is set to take place at ten o' clock our time, so I could be here at nine to set things up. We'll have plenty of time to run some tests and talk to our guys on the other side."

        show hiroyuki thinking_close
        with chchange

        hyf "It has... been decided then."
        "Sensing that there's not much more business to discuss, I take advantage of the moment of silence to address Father's colleague."
        li "Can I pour you another cup of tea, sir?"
        "Mr. McLaughlin" "Just one then. I don't want to impose on you longer than necessary."

        scene bg satou_entrance
        with shorttimeskip

        "Mr. McLaughlin" "Should I take the printer out of my car now or is it just going to get in the way?"
        "The meeting ended with a minimum of small talk, and I have taken it upon myself to see our visitor out while Allison guides Father back to the master bedroom."
        li "Is there a need to do... something... with it before it can be used?"
        "Mr. McLaughlin" "No. Your father can turn it on and press the connect button and my laptop will find it as long as it's within range. I assume you'll want to remain in a bedroom upstairs this evening?"
        li "Yes, it would indeed be most convenient if he remains in bed. If you leave the printer in the hallway, our housekeeper will take it upstairs."

        # TODO play trunk open and close sfx

        "I hear the sound of the trunk opening and then being slammed shut. After putting his cargo in the hallway, he walks up to me again."
        "Mr. McLaughlin" "I could tell he was straining himself earlier on. I'll set your dad's microphone's output volume a little higher than usual so he won't need to raise his voice as much."
        "Mr. McLaughlin" "I have a buddy who broke a few ribs in a rugby match once, and he spoke in little more than single syllables while he was recovering. It's a real pain when you can't breathe well."
        li "Thank you for going through the trouble of accommodating him."
        "Mr. McLaughlin" "Don't sweat it. I'll be back in a few hours."

        # TODO play car driving off sfx

        "I remain near the front door until the sound of his car's engine is no longer audible and then make my way back inside."
        "Father is probably resting right now, which gives me time to get started on today's dinner. This is probably going to be a long night, so it'll be best to be well prepared."

        stop music fadeout 2.0

        if _in_replay:
            return
    
    label .s2:

        $ set_window_tint(TINT_LILLY)

        queue music music_lilly fadein 4.0

        scene bg satou_masterbed_ni
        with shorttimeskip

        hyf "I did not even hear the doorbell. Your sharp... sense of hearing never ceases to amaze me."
        "I smile humbly upon re-entering the master bedroom after briefly going downstairs to let the system administrator in and making certain he was provided with a cup of tea."
        "The housekeeping staff all went home two hours ago, but Allison made sure that everything she thought I'd need for tonight would be in a place where I could easily find it."

        scene ev bedside_sit
        show lilly basic_smile at twoleft
        show hiroyuki basic_thinking at tworight
        with Dissolve(2.0)

        li "It wasn't really the doorbell itself. I heard the sound of a car outside."
        hyf "Nevertheless."
        "As inconvenient as my blindness is at times, I'm thankful for the fact that it has honed my sense of hearing to a greater degree."
        "Speaking at length still tires and discomforts Father, but as long as he keeps his voice down to a whisper, he can communicate without it hurting too much. That does mean people other than me are forced to ask him to repeat himself every two sentences or so."
        hyf "Has Mister McLaughlin gotten settled in there?"
        li "Yes. I've made sure to serve him some tea and left the water boiler and a supply of tea bags in the study so he can make some additional tea for himself if he feels like it."
        li "I also asked him to knock and wait for me to come out rather than walk into this room if he needs to talk to us. He's currently on the phone with his fellow administrator, but he said everything will be ready in half an hour."
        hyf "So we still have about half an hour... of time to kill."
        li "Would you like to rest for a little bit more?"
        hyf "I do not think I would... be able to sleep in the current situation. But perhaps you could give... me another bowl of your hot soup. It is truly on... par with the rest of your cooking."
        li "I will."

        scene bg satou_masterbed_ni
        with changelocation

        "I walk over to the corner of the room where a small electric stove is keeping the large pan of miso soup that I made this afternoon to get us through the night warm with its single heated plate."
        "I went through a lot of effort to make the soup myself, but the result is apparently quite pleasing to Father. I fill a bowl with the contents of the pan, slowly walk back to the bed and carefully place it in Father's hands."

        scene ev bedside_soup
        show lilly basic_smile at twoleft
        show hiroyuki basic_thinking at tworight
        with Dissolve(1.0)

        li "Let's hope everything goes well, and we'll have no difficulties."
        hyf "Mister McLaughlin seems capable enough. We... should be fine."

        show lilly basic_displeased
        with chchange

        "My thoughts return to the talk we had with him earlier today."
        li "Father, may I ask something?"
        hyf "What is it?"
        li "What did you think of his proposal?"

        show hiroyuki serious
        with chchange

        hyf "To handle his duties in here instead of from the office? I am not... overly fond of others using my private study... without me being present, but his suggestion was the most practical and riskfree one."
        li "I understand, but there was something that caught my attention."
        hyf "You are referring to the way he brought it up, are you... not?"
        li "If his words offended you, you did a good job of hiding it."

        show hiroyuki thinking
        with chchange

        "Father lets out a self-deprecating sigh."
        hyf "Welcome to western civilization, Lilly. It is quite... a different world over here."
        li "I imagine."
        hyf "A subordinate telling his superior that he ‘has a better idea’, especially in... the presence of others, would be a massive transgression in our home country."
        hyf "But westerners... are a lot more tolerant and sometimes even encouraging when it comes to questioning or challenging... people in positions of authority."
        hyf "As long as the challenge has merit... and is voiced in a civil way, it is deemed acceptable and the person being challenged... is expected to acknowledge it without feeling slighted or shamed. I was told in advance to expect this, but... it takes some getting used to."
        hyf "It helps to realize the people here weren't... brought up with our value system. I think... I would probably still expect Japanese employees to stick to our own etiquette."
        "That probably explains why he puts up with an employee making him lose face in front of his family without even a change in heartbeat while I get put on prohibition for falling asleep in the wrong place."
        li "Are there any other Japanese working here besides Akira?"
        hyf "None that I know of at the... moment. We have good relations with several universities... in the region, so there has been little need to borrow talent... from the Japanese office."
        hyf "People from here sometimes travel to Japan and we get visitors from their branch, but we are not involved in each... other's day-to-day activities."
        hyf "This branch was... initially only intended as a production plant. Assembling and later also manufacturing the equipment that was sold to our clients in the region here... was cheaper than producing it in Japan and then shipping it to Europe."
        hyf "Eventually... it started picking up more and more... customers and became a full-fledged sister company."
        hyf "The board... has been playing with the idea of sending managers from the Japanese branch here to make them familiar... with this part of the company, but did not want to immediately replace the Scottish managers who have been doing a good job serving this company for years."
        hyf "I became... manager of this branch six years ago because that was when the former local manager here retired, and I could take his place without pushing away someone else."
        hyf "One of my tasks was to... test which aspects of Japanese management style could be succesfully implemented here and which ones would merely... cause frustration."
        hyf "You cannot just lead... a western company like... a Japanese one or a Japanese company like a western one... and expect it to work out."
        li "That sounds like a tough job. Japanese management style and company culture are very different from the western one, aren't they?"
        hyf "They are. Japanese... management emphasizes loyalty and insight gained through... seniority, long-time goals, risk avoidance, maintaining harmony and decision-making through well-crafted consensus."
        hyf "Western management emphasizes quick... returns on investment, individual decisiveness, efficiency and calculated risks. Many times the... two seem incompatible."
        hyf "I have found that many people... here often do not have the patience for sitting in meetings for hours on end until a consensus is made on how... to deal with a problem."
        hyf "Westerners... also have a very different definition of company loyalty than Japanese, and that is not something you can ignore when leading a company."

        show lilly basic_weaksmile
        with chchange

        li "I'm sure both cultures have their merits."

        show hiroyuki speak
        with chchange

        hyf "Hmmm... It was not really my intention to complain. There is something interesting about the carefree way... they can go about their lives without the burden of what others... might or might not think of them. They also admittedly handle diversity a lot better than we do."
        "I wonder if that's truly a touch of envy I hear for a moment. I feel a bit taken off guard by his words."
        li "That's a rather frank assessment..."
        hyf "On the other hand, many could... be more loyal. You would be surprised how... many western managers seem unwilling to impose a... pay cut on themselves while their company is going through hard... times. Too many people, workers and managers alike, only seem to be in... it for themselves."
        hyf "It is hard for me to understand that attitude. I... try not to condemn them though. Nor am I saying that their culture... is better... or worse. I believe it is best to keep an open mind about the differences... between our society and theirs."
        hyf "It would be very difficult for... me to lead a branch consisting of almost nothing but Scotsmen and... deal with American businessmen on an almost daily basis if I let everything about western culture get to me."
        "I suppose what he says makes sense. When moving to another country, it's logical to try and adapt a little to fit in with the local people better. It just feels a little off to hear my father, who I've always seen as very traditionally-minded, say these things. It clashes with the image I had of him."
        "I initially thought it was just Mother who changed during her time here, but perhaps Father has changed in his own subtle way as well."
        "Still, managing a company with a completely different business culture must have been a very harrowing job for Father, and I'm starting to suspect that the stress he's been under may have been caused by more than just social pressure to live up to his own father's accomplishments."
        "His job here has probably been sapping a lot of his energy from the very beginning. That would explain why the doctors said that he's had high blood pressure for years."
        li "It still sounds like it must have been very stressful for you. How do you think Akira will handle the culture shock?"
        hyf "I think she will... do fine. Your sister can be very straight-forward when... she feels she needs to be and westerners value that trait as long as... it is combined with a modicum of respect. Young people tend to be more adaptable to... begin with."
        hyf "I suspect she will do a better job at integrating... into western culture than I could ever hope to do. I have... heard that her transferring here required some sacrifice, but I feel... fairly confident that in the long run she will not regret her decision to move here."

        show lilly basic_displeased
        with chchange

        li "Ah... Father? About that..."
        hyf "Yes?"
        li "Were you... very disappointed in me when you learned I decided to stay in Japan?"

        show hiroyuki thinking

        hyf "Hmmm..."
        "There's a long pause after I pose my question, and for a moment I'm starting to suspect he's not going to answer in order to avoid hurting my feelings. But just before I can apologize for asking him, he answers."
        hyf "When we invited you and Akira to join... us here, I used to believe that if anyone would reject our offer, it... would be Akira rather than you. I was... rather shocked when your mother told me the news. But, on the other hand..."
        li "Y-yes?"

        hyf "...From what I have heard from... you about your life in Japan over the last two weeks, I know that you had your life set up well there. You had a school... you enjoyed attending, a position of responsibility among... your classmates and friends you enjoyed spending time with."
        hyf "All of those are valuable things. To... give all of that up, just to make a brand new start on the other end of the... world in a country with a culture completely different from your own... is quite a gamble."
        li "Father...? Are you saying...?"
 
        show hiroyuki smileclosed
 
        hyf "All I am saying is that while it is most regrettable that you decided to stay there, I do understand why you chose to do so."
        li "I..."

        show hiroyuki thinking

        "I don't know what to say for several seconds. What I feel right now is a strange mixture of relief and befuddlement."
        "I've always assumed that Father would be dismayed by the fact that I turned down the summons. He was always the one who would talk to us about the benefits of respecting and deferring to your elders. Did he start getting second thoughts about having me move here?"
        li "Thank you for your understanding, Father."

        show lilly basic_concerned

        nvl clear
        nvl show dissolve

        n "Or is this about something else? Is it possible his words earlier weren't merely a reflection on my situation, but also on his own? I've learned from Father's and Akira's stories that the work culture between Japan and Scotland is radically different."
        n "In Japan, working overtime is pretty much a daily occurrance and leaving before the boss goes home is considered rude and bad for the team spirit, so people like Father would usually remain at the office until late in the evening."
        n "Afterwards, the various teams would go out drinking together or visit karaoke establishments. Since so little time is spent at home, people's entire circle of friends tends to consist of the same colleagues they spent a large part of their week with."

        nvl clear

        n "But judging from what Akira has told me, people here often immediately go home at the end of their official work day, and they only do overtime when there's an approaching deadline to meet."
        n "While it's not uncommon for friendships to form on the workfloor here, most people here develop their friendships outside the workplace through social activities like sport clubs, hobbies or pub visits."
        n "Mother quickly developed a big social network here and has been partaking in a large number of activities outside her working hours, but how well did Father adapt here?"
        n "After over 25 years of having all his social interaction through the workplace, how quickly could someone like him switch gears?"

        nvl clear

        n "Was him doing all that overwork here on his own purely out of loyalty to the company and to his own father or was it also because any time outside his office was simply spent at home in that study of his, reading one of the countless books he keeps there?"
        n "Is the quantity of books in there an indication of how much of his free time he spent on his own without the company of others? Did he want Akira and me here because he desired more company?"
        n "Was loneliness part of the stress factors that nearly ended up killing him? Did he say what he just said because of the possibility that I might have ended up feeling lonely here as well?"

        nvl clear
        nvl hide dissolve

        li "Father?"
        hyf "Yes?"
        "I skim the surface of the bed with my fingers until I locate his hand and gently place my own on top of it."
        li "How about the life you had in Japan? And the friends you had there? Aren't you... lonely here?"

        show hiroyuki stern

        "An uncomfortable pause. I can sense his hand stiffening for a moment. Was that question out of line?"
        hyf "Is that... pity I hear in your voice, Lilly?"

        show lilly basic_weaksmile

        li "Just a bit of concern for your well-being, Father."
        hyf "I have been fine, Lilly."

        show lilly basic_displeased
        show hiroyuki serious

        "The tone in his voice pretty much confirms what I've been thinking."
        "But he probably feels that over the last few weeks he's already shown enough vulnerability to his children, so I doubt that prying further into his personal feelings will achieve anything other than making him uncomfortable."
        "So I drop the subject, but not before giving his hand a gentle comforting squeeze."
        "Not really knowing how to continue the discussion, we simply stay like this for a little while, neither of us bothered by the prolonged silence, until my attention is drawn to a static noise coming from the nearby nightstand."

        show lilly basic_smileclosed
 
        li "The headsets. It sounds like it's starting. Would you like one more bowl of miso soup, Father?"

        show hiroyuki basic_thinking
        with chchange

        hyf "That would be appreciated."

        show ev bedside_headset
        with Dissolve(1.0)

        "I refill Father's bowl and take the two headsets off the nightstand. We both put one on and I carefully speak into the microphone."
        li "Ah... is this thing on already?"
        "Mr. McLaughlin" "It is and I can pick you up loud and clear, Miss Satou."
        li "Mister McLaughlin. How are things proceeding so far?"
        "Mr. McLaughlin" "We've succesfully got a session running. The clip-on microphones have all been distributed to the meeting's participants, but we're keeping their microphones muted until the meeting has officially started. It'd be kind of a cacophony otherwise."
        hyf "Could we... speak to... my daughter... or Mrs. Satou?"
        "Mr. McLaughlin" "Sure. I'm adding you two to the session right now. Then I'm going to take a short bathroom break. I'll be back in five minutes."
        li "Hello?"

        play music music_pearly fadein 4.0

        show akira basic_smile_phone at phonebox
        with charaenter

        aki "Hey Sis! Will you be listening in too?"

        show lilly basic_smile
        with chchange
 
        li "Akira! It's so nice to hear you again. How was the flight?"

        show akira basic_cheerful_phone

        aki "Kinda long, but our airline had some very luxury business class seats, so I can't complain. Heh, they have some pretty good liquor too."
        hyf "Akira. Is everything... ready? I do not... hear anyone else... nearby."

        show akira basic_smile_phone

        aki "That's because I just retreated to one of the empty meeting rooms here. I figured that in case you wanted to discuss some last minute stuff, it'd look weird if others see me talking to thin air."
        li "Wouldn't they notice the headset? It seems like something that would be hard to miss."
        aki "I'm not wearing a headset. I have the same microphone on my lapel as everyone else and I'm listening to you through one of those earpieces that secret agents often wear in movies."

        show akira basic_laugh_phone at phonebox

        aki "Hehe, I was just thinking... between the earpiece and the business suit, all I'd be needing right now would be a sidearm and maybe some sunglasses, and I'd be ready to join the secret service."

        show lilly basic_cheerful
        show hiroyuki stern

        "I laugh at Akira's wacky remark, but hear a soft groan coming from Father. It seems Akira's playful attitude isn't inspiring confidence in him."
        hyf "Akira... can I... count on you to take... this a hundred... percent seriously?"

        show akira basic_smug_phone

        aki "Dad, it's not like I've never been part of business meetings before. Everything will be fine, I promise."
        hyf "Just act... like the person... standing in... for me is... expected to act.\n{size=*0.7}And I will have your... mother buy you a vodka martini afterwards."

        show akira basic_lost_phone

        aki "Hmmm? I didn't catch that last part."

        show lilly basic_smileclosed
        show hiroyuki serious

        hyf "Never mind. Am I sufficiently... audible to you?"

        show akira basic_smile_phone

        aki "You are. You can probably speak a bit softer if that feels more comfortable."
        hyf "That might... cause problems if... someone else is... speaking at the same time."
        li "Father? Perhaps you should lower your voice a bit more so that speaking is less painful for you. If at any point Akira didn't hear you clearly, maybe she could softly clear her throat as a cue and I will repeat your words to her."
        aki "That's a pretty good idea, Sis. Something like this?"
        "We hear her let out a soft “hrmm” under her breath."
        li "That will probably suffice. Father?"

        show hiroyuki thinking

        "Father lets out a resigned sigh."
        hyf "Very well. Let us... give that a try."
        aki "I'll be heading back to the rest. Mom's finished giving everyone a mic, and she's explained your situation. Without getting too specific, of course."
        aki "I'll leave it to her to give you the details, but so far everyone's reacted very positively, and Mom got word from just about everyone that they're willing to go out of their way to accommodate you."
        hyf "I really hope... that will not be necessary."

        show akira basic_sweet_phone

        aki "By the way, Kojima will be seated at the head of the table in your place despite you being ‘present’. We figured the board wanted a senior in that seat instead of me, despite him only being an observer in a practical sense and me representing you directly."
        hyf "I agree with... that decision."
        "While Akira's speaking, I become aware of a slight background noise appearing on the line, indicating the vicinity of other people. I faintly hear Mother's voice asking Akira if she's ready."

        show akira basic_smile_phone

        aki "Yeah, I'm ready and so is Dad. Let's go in."

        show hiroyuki serious

        "The next moment, we're startled by a wave of voices as the microphones of the meeting room's occupants are turned on. I cringe a bit as the room suddenly appears to be filled with people."
        "Just as I prepare to take off the earphones, the fragments of conversation suddenly fade out and then increase in volume again. I fiddle a bit with the dial on my headset until the sound volume's comfortable."
        "I notice that some voices sound further away than others and certain people are specifically audible through either the left or the right speaker. I suppose the administrators set this up in some way or another and smile in appreciation of their effort to make the experience feel more natural to us."

        scene ev bedside_papers
        show lilly basic_displeased at left
        show hiroyuki serious at right
        show akira basic_smile_phone at phonebox
        with Dissolve(2.0)

        nvl clear
        nvl show dissolve

        n "And then finally, the meeting begins. Kojima opens the meeting with a short introduction, followed by a word from Father, consisting mostly of an apology for not being able to be there in person and a statement of appreciation for his business partners."
        n "I personally think he might have stressed the apologetic part too much, yet Akira delivers his words without a single trace of insincerity nor do I hear even a hint of the usual defiance in her voice that's almost always there when she's dealing with our parents."
        n "I suppose in her mind right now Akira isn't representing her father, but rather representing her boss. It's impressive how much of a difference that makes with her."

        nvl clear
        nvl hide dissolve

        hide akira
        show karla basic_speak_phone at phonebox
        show lilly basic_displeased
        show hiroyuki thinking

        "What stands out most for me, however, is hearing Mother."

        nvl clear
        nvl show dissolve

        n "Unlike Father, who merely listens most of the time and only rarely takes the opportunity to provide a quick summary or offer his own opinion, Mother turns out to be the member of the delegation who seems to be handling most of the questions and counterproposals."
        n "Her tone right now isn't the energetic and casual one I've been struggling to get used to over the last few weeks. Instead, it's polite and relaxed, yet confident and in charge at the same time. I've never heard Mother speak this way before."
        n "I realize I have to remain focussed in order to assist Father, so I try not to think about it too hard."

        nvl clear
        nvl hide dissolve

        hide karla

        "The meeting ends up taking two hours with only a short coffee break near the middle."
        "For the most part, I've simply sat by and listened, repeating Father's words to Akira when necessary, handing Father scanned graphs and proposal summaries as they roll out of the nearby printer and refilling our bowls of soup once or twice."

        show lilly basic_concerned

        "Still, after two hours of taking in a continuous stream of information, I feel drained. When the microphones are turned off, I let out an exhausted sigh."

        show hiroyuki smile

        hyf "Tired?"

        show lilly basic_weaksmile

        li "Only a little bit. This will be good practice for the months prior to the exams though, which will involve cramming as much information as possible into my head."
        hyf "That is one way of looking at it."
        li "I suppose I should show Mister McLaughlin out. It's probably late for him as well."
        hyf "That would be appreciated. Since there... are a meeting and a business dinner planned for tomorrow, it... will be okay for him to sleep in tomorrow morning. He... will probably have to be up for most of the night."
        li "I will tell him so."

        stop music fadeout 2.0
        queue music music_twinkle fadein 4.0

        scene bg satou_masterbed_ni
        with Dissolve(1.0)

        li "He will be back here at eight o' clock tomorrow evening."
        "After showing the system administrator out, I returned to Father's room."
        "Judging by the sound of his voice, he's either feeling less tired than I am right now or he's simply doing a better job at hiding it."
        hyf "That is good to hear."

        scene ev bedside_sit
        show lilly basic_smileclosed at twoleft
        show hiroyuki serious at tworight
        with Dissolve(1.0)

        li "He was quite relieved when I told him he could sleep in. He said that this had to have been one of the longest working days of his career."
        hyf "Hmmm. I suppose it would be ungrateful to... point out to him that at our Japanese branch we used... to consider any working day shorter than 11 hours to be an unproductive one on general principle."

        show lilly basic_cheerful

        li "Looking on the bright side, he at least didn't leave before his boss went home today."

        show hiroyuki smileclosed

        hyf "Touché."
        "He chuckles a bit at my remark, then groans in discomfort. Laughing too much will probably be out of the question for the time being."

        show lilly basic_smileclosed

        li "Father, can I get you anything before we retire for the night?"
        hyf "Hmmm..."
        "There's a long pause as if he's considering something to himself."

        show lilly basic_smile
        show hiroyuki smile

        hyf "If I still had been at our Japanese... office, my co-workers and I would have headed over to a drinking establishment... to drink and celebrate today's events right about now..."
        li "Do you want me to fetch you some wine, Father?"
        hyf "I suppose a little nightcap cannot hurt. You have been to the cellar before, have you not? Is it not too difficult to navigate?"
        li "Not overly so."
        hyf "One of the bottles of wine on the second shelf from the top will probably do. I am certain you already know where to find some glasses."
        li "I'm sorry, but...did you say glasses?"

        show hiroyuki smileclosed

        hyf "You know what they say about people who... drink alone. You may not be a co-worker, but you did do your... best to help out this evening. It is okay... with me for you to have a drink or two...as long as it is under the supervision of an adult."

        show lilly basic_cheerful

        "My smile widens a bit. This is certainly one pleasant and unexpected surprise."
        li "Thank you, Father."

        scene black
        with Dissolve(2.0)

        "With a bit of effort, I manage to get a bottle from the wine rack in the cellar and two glasses and a corkscrew from the kitchen and get them all to the master bedroom in one piece."

        scene ev bedside_wine
        with Dissolve(2.0)

        show lilly basic_smileclosed at left
        show hiroyuki serious at right

        "Father takes the bottle and corkscrew from my hands, and moments later, I hear the distinct sound of a bottle being uncorked, and the smell of white wine teases my nostrills."
        "I sit on the side of the bed, hold out my glass and hear a sloshing sound as it's being filled."
        hyf "Just remember... that a proper lady does... not pass out on the couch."
        "I playfully raise my hand."
        li "It will not happen again. The Lord is my witness."

        show lilly basic_smile
        show hiroyuki smileclosed

        hyf "Very well. To the success of your mother and... your sister then."
        li "And to your speedy recovery as well, Father."
        hyf "That too."

        show lilly basic_smileclosed
        show hiroyuki smileclosed

        "I carefully balance the glass in my hand, bring it up to my face and slowly breathe in in order to sample the wine's aroma. I continue taking in the smell until it leaves a subtly sweet taste in my mouth and then take a few soft sips. The wine's taste turns out to be as pleasing as its fragrance."
        li "Father, I suppose this nightcap indicates that the meeting went well overall?"
        hyf "Things matched my expectations. Aside from Akira, who performed better than I expected."
        li "How about Mother?"
        hyf "She did as expected. She has... been part of everything since this all began, so she... knows how to handle herself."
        li "Really?"

        show lilly basic_displeased
        show hiroyuki thinking

        hyf "Your mother has been an true asset to the company from the... moment we came here. She did an excellent job helping the staff and... me get used to one another's mindset and bridge the cultural... divides."
        hyf "She has also always been ready with advice on how... to best deal with our Scottish staff and how to best interact... with American business contacts."
        hyf "I also quickly discovered that her knack... for networking and connecting with business people has remained as sharp as it... undoubtedly was in her days as a business reporter."

        nvl clear
        nvl show dissolve

        n "There's an unmistakable hint of admiration in his voice, and I'd probably feel a sense of pride if all of this wasn't so new to me."
        n "Shortly after Father was hospitalized, Akira suggested his and Mother's marriage was in ruins, but from the way they speak about one another, I think she was sorely mistaken."
        n "Still, Father's words once again make me wonder who Mother really is. The quiet and graceful homemaker I remember from my childhood? The energetic woman I've been spending time with here? Or the confident businesswoman I heard through my headset this evening?"
        n "Perhaps a combination of all three? Is that even possible?"

        nvl clear
        nvl hide dissolve

        li "Father, how... do you see Mother?"
        hyf "Akira was incorrect about us... Lilly. Please just take my word for that."
        "He doesn't really seem to be eager to discuss that particular subject, so I decide to drop it and move to a different topic."

        show lilly basic_smile
        show hiroyuki serious

        li "Mother certainly handled herself well from what I could tell. I don't think I'd be capable of such a thing. But then again corporate business isn't really where my own interests lie."
        "I hear Father let out a soft 'hmmm' as he hears this."
        hyf "You have... plans for the future then?"
        li "I would like to study English after I graduate and become a teacher after finishing my higher education."
        hyf "I had a very good English teacher back in... university. It is a valuable job. You would... be surprised about how many businessmen in our country, even senior... ones, are insecure about their own English skills. And yet it... is important in staying relevant in this age of globalisation. But... ah..."
        "I give him a reassuring smile."
        li "You can ask, Father. I won't be offended."

        hyf "Is that not hard? How would you prevent... students from cheating on a test for example? Or handle discipline?"

        show lilly basic_smileclosed
        show hiroyuki thinking

        li "I would seek the help of another English teacher. At times when my class has to take a test, I'll ask him to switch classes. He keeps an eye on my class for an hour while I teach his."
        li "As for discipline, I would make a seating chart so that I know where each pupil is sitting and I would walk around the classroom while teaching, so I can keep students in check through force of proximity."
        hyf "How about tests? How would you grade them?"
        li "I would again engage in a deal with a fellow English teacher. I would prepare and write up both my own tests and his, as well as the corresponding answer keys and he would do the grading."
        li "I'm...ah...still trying to think up how to deal with essays. If I wanted to check a specific pupil's homework, I'd have them read it to me out loud."
        "I take another sip of the delicious wine before continuing."
        li "I would also attempt to create a sense of team spirit in each class I'd teach, so pupils could eventually be relied on to grade each other's homework."
        li "I acknowledge that school teachers have duties that require sight, but there are just as many which do not."
        li "By volunteering to take some tasks of the latter category off my colleagues' hands, I can get away with asking them to help me with things I cannot do myself."
        "My explanation is followed up by a long silence on his end. I can almost hear the gears in his head turning as he weighs and evaluates every word I just said. Then, just before I am about to break the silence..."
        hyf "You seem to have put... a lot of thought into this."
        "I wonder what he thinks about my plans for the future. I weigh the tone in his voice for traces of skepticism, but the only thing I can pick up is a sense of honest curiosity."
        li "It's been a dream of mine since middle school, so I've had some time to think about it."
        hyf "You learn something new every day."

        "As I empty my glass, he takes it from my hand and pours a bit more wine into it. When I take it back, I notice it's lighter than the first time. It's probably only half-full this time around."
        "We gently touch our glasses together and then slowly sip the contents."

        show lilly basic_displeased

        "After noticing a failed effort to supress a yawn on my part, Father decides that enough is enough for today and bids me good night."

        show hiroyuki smileclosed

        "I prepare to make my way to the door, but before I can get up, I hear a soft chuckle coming from the bed."
        li "Father?"
        hyf "It is nothing. Just an... amusing thought that came to me just now."
        li "Hmmm?"
        hyf "I just thought about how... different it felt, holding... a meeting this way."
        hyf "Interacting with people without being... able to see their faces. Having to determine who is... talking purely by the sound of their voice, their accent and... the direction their speech is coming from."
        hyf "I suppose... you can relate... to this?"

        show lilly basic_giggle
        show hiroyuki smileclosed

        "I cover my mouth to mask a cheerful giggle. For some reason it feels really good to hear him say something like this."
        li "Trust me when I say that it's not so bad once you get used to it."

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return
        else:
            pause 2.0
    
    return