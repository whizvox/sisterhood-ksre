label sh_ch25:
    label .s1:

        $ set_window_tint(TINT_HISAO)

        scene ev tipsyfun_bellytoback_nauseous
        with Pause(3.0)

        "I wish I was dead."
        "Was it this bad the last time?"
        "It might have been but there's no way to know for sure. Even digging through my memory feels like smashing my head into a wall."
        "Or into a pile of broken glass."
        "Or into a wall with broken glass embedded in it."

        play music music_serene fadein 4.0

        scene bg satou_guestroom
        with locationchange

        nvl clear
        nvl show dissolve

        n "I grit my teeth as I try to bear the painful pounding inside my head. It doesn't really help, although I am getting slightly more aware of my surroundings."
        n "I notice a lot of light around me. A painful lot of light. Too much light. I roll onto my back, use both hands to shield my eyes, and carefully open them."
        n "Even the small rays of light slipping through the cracks between my fingers manage to hurt my eyes, but I nevertheless keep them open. Eventually my vision has adapted enough for me to look around the room through squinted eyes."
        n "{vspace=60}The torturing light turns out to be sunlight from the nearby window. My eye falls on the nearby curtain. If I could get to that curtain and close it that would make things a lot more bearable."

        nvl clear

        n "Damnit."
        n "Of course, the curtain's too far to close from where I'm lying, so I'll have to get out of the bed and make my way over there, which is easier said than done. My arms and legs feel like someone snuck up to me in my sleep and injected lead into my veins."
        n "I really don't want to get out of bed, but that light isn't going away by itself."
        n "{vspace=60}I manage to make my way to the edge of the bed, but as I prepare to step out of the bed I notice that something is somehow keeping my legs stuck together."

        nvl clear

        play sound sfx_rustling

        n "I pull away the covers just a little bit so my feet become visible and I notice that I'm still wearing my socks and that my boxers and pants are around my ankles. I groan softly in exasperation."
        n "The way I'm feeling right now, even the effort of having to pull up my pants and underwear comes across as an excruciating task. Still, I'll have to do it if I want to make it over to the window."
        n "{vspace=30}Trying my hardest to ignore my body's protests, I manage to sit up, reach out and pull up my pants. The window is only four to five steps away, but it feels more like fifty."
        n "When I finally reach the window, I give a sharp pull on the curtain and sigh as the lighting in the room dims."
        n "{vspace=60}It does little to diminish the throbbing sensation under my skull, but I do feel a bit of relief now that I can open my eyes without getting the sensation of someone rubbing them in with pepper extract."

        nvl clear

        n "Now that I can look around the room without squinting, I notice a motionless form on the bed. I faintly recall waking up partially lying on top of something warm and soft before rolling onto my back."
        n "Hanako's still largely covered by the bedsheets, but I can see her long dark hair stick out on one end and her socks and pants sticking out at the other end."
        n "I let out another soft groan. It hurts to think too much right now, but I manage to remember just enough of last night's events to blush a bit."

        nvl clear

        n "Despite feeling sick and exhausted, I hesitate to get back between the sweat-soaked sheets and opt to take a quick shower instead."
        n "The warm water running over me feels good, although it does less to ease my hangover than I was hoping for. It does ease my hurting brain a bit, allowing me to think back on last night's events."
        n "{vspace=60}It's not the first time a few drinks have left Hanako a bit clingy, but it's definitely the first time she's gone this far. It's not like I've been acting like the adult in the room though."
        n "After last time, I thought I'd be able to handle Hanako just fine, even if she got like this. But now it turns out that that Hanako is able to handle me just fine as well."
        
        nvl clear

        n "I get out of the shower, not really feeling any better but certainly feeling more awake. I still have a headache and feel rather exhausted. While it took me very little time to fall asleep, my sleep was restless for most of the night."
        n "I wonder if getting back into bed will be a good idea. I take a look at Hanako who's still lying on her stomach in exactly the same position as before and probably hasn't moved a muscle since I went to take my shower."
        n "I faintly remember pretty much collapsing on top of her last night and somehow managing to get my hands on a sheet to pull over us."
        n "{vspace=30}Under other circumstances, I'd have no seconds thoughts about getting back in bed. Hanako's sleepy smile in the morning is one of the most beautiful things in the world to wake up to."
        n "This morning, however, it's pretty likely she'll feel as queasy as I’m feeling right now, and I'm not so sure how she'll react to the memory of last night's events, but smiling about the whole thing will probably be the least likely reaction."
        
        nvl hide dissolve

        "I think the best thing for me to do is give her the opportunity to recall the whole thing herself and let it sink in without my presence adding an extreme amount of awkwardness to the situation."

        play sound sfx_dooropen

        "With some effort, I put on some clothes, unlock the door and leave our room."

        scene bg satou_stairs
        with locationchange

        "As I close our bedroom door behind me, I realize I'm not even sure what to do now. I find that I even lack the energy to think up ways to keep busy."
        "The pounding feeling inside my head has subsided to give way to a still slightly unpleasant throbbing, and my throat is unusually dry. I wonder if I'd be allowed to get something to drink from the fridge."

        stop music fadeout 2.0

        # TODO play Concord (refined) cello ver.
        queue music music_lilly fadein 6.0
        $ renpy.music.set_volume(0.5)

        "While searching the kitchen for snacks last night, I remember having seen several bottled drinks there. While making my way down the staircase, I slowly become aware of music coming from somewhere in the house."
        "As I stop to listen, I realize that I've heard both that song and that instrument before."

        scene bg satou_livingroom
        show karla basic_cheerful_cas at tworight
        with locationchange

        $ renpy.music.set_volume(1.0, delay=1.0)

        "I follow the melody to its source and end up in the living room where I see that the cello is now being played by its actual owner."
        "Compared to yesterday, Karla is dressed a lot more casually this morning. Instead of her business suit, she's wearing a pair of sporty jeans and a light blouse."
        "Upon noticing me, Lilly's mother gives me a cheerful nod and a smile."
        ka "Good morning, Hisao."
        hi "Good morning. I hope you don't mind an audience."

        show karla basic_smile_cas
        with chchange

        "She makes a quick gesture with her head."
        ka "I already have an audience, but I don't mind a larger one."

        show karla basic_cheerful_cas
        with chchange

        "When I look behind me, I notice that the large couch on my side of the table isn't as unoccupied as it seemed when I entered the room. Lying on the couch with her eyes closed is Lilly."
        "She's wearing the exact same clothes as yesterday, making me wonder if she's been to her room at all last night."
        "She hasn't really acknowledged my presence since I entered the room, though with Lilly it's sometimes difficult to tell whether she's asleep or not since she also has her eyes closed half the time when she's awake."
        "With Lilly taking up all the space on the couch, I simply take a seat on one of its armrests and listen to Karla's playing. I recognize the song as the same melody Lilly played for us last night."
        "Even in the rather sorry state I'm currently in, I can make out the subtle difference between Lilly's playing last night and Karla's performance right now."
        "Somehow Karla's playing seems to flow more naturally, and there's an effortlessness about her movements that hints at quite a bit of experience. The melody itself is subdued and soothing to listen to, but also a bit melancholic."

        stop music fadeout 1.0

        "Eventually, the song ends, and I think about clapping for a moment, but then decide that the noise would probably hurt my brain and settle for an appreciative bow."
        hi "That sounded good. Is it a Scottish piece?"

        show karla basic_wistful_cas
        with chchange

        "Karla shakes her head."
        ka "The name of the song is ‘Concord’, and I believe it's originally Canadian. I picked it up before I first moved to Japan. It's always been one of my favorite pieces, though it's kinda lacking without a piano accompaniment."
        hi "Do you often practice in the mornings?"

        play music music_lilly fadein 4.0

        show karla basic_smileclosed_cas
        with chchange

        "Karla grins and shakes her head."
        ka "I wasn't practicing. When I came home last night, I caught my daughter examining my cello, and she asked for a performance."
        ka "I wasn't dressed for the occasion at the time, so I put it off until today, and when we found her on the couch this morning, I decided a morning concert was a nice way to wake her up."
        hi "Is she awake now?"
        "Lilly answers my question by letting out an uncharacteristically loud yawn. Karla grins mischievously."

        show karla basic_smug_cas
        with chchange

        ka "‘Awake’ is probably stretching the definition."
        
        show lilly basic_sleepy at twoleft
        with chchange

        "Lilly groans softly and slowly sits up, gently massaging her forehead. Looks like what's ailing me is also wreaking havoc on Lilly."
        "Wait... Did Karla just say that Lilly spent the night here in this very spot?"
        "I take a look and notice a particularly large drool stain on a part of the couch near Lilly's head that escaped my attention before."
        hi "Did you say she slept on the couch? Why?"

        show karla basic_smile_cas
        with chchange

        ka "Beats me. She was rather tipsy when we came home last night, so we were quick to call it a night. We took her upstairs, and she mentioned wanting to take a lavatory break."

        show karla basic_laugh_cas
        with chchange

        ka "Haha, I thought she was maybe going to offer a little prayer at the porcelain altar, so we decided not to wait until she was done and bid her goodnight. Her room was right next door, so we figured she'd be able to find her way there."

        show karla basic_sheepish_cas
        with chchange

        ka "But for some reason she decided to go back downstairs and pass out on the couch instead. The housekeeping staff found her here when they arrived. My husband has been really grumpy about that this morning."
        "Lilly groans as if even formulating words is already unbearably painful."
        li "{cps=*0.5}Like I... said... before. My bedroom... door was... locked.{/cps}"

        show karla basic_lost_cas
        with chchange

        "Karla shrugs her shoulders with a puzzled expression."
        ka "She says her door was locked when she went for her bedroom, but when I checked this morning that didn't turn out to be the case."
        "I'm about to dismiss the whole thing when I suddenly remember something that Lilly told me yesterday."
        hi "Lilly didn't sleep in that particular room the last time she stayed here, did she?"

        show karla basic_smile_cas
        with chchange

        ka "No, she stayed in the room you and Hanako are currently using. We decided to let you two use that room since it's larger and more suitable to accommodate two people."
        "If I remember correctly that restroom is situated right between our bedroom and Lilly's."
        hi "I locked our door last night before we went to bed. Perhaps... err..."

        show lilly basic_displeased
        with chchange

        li "..."
        "Lilly doesn't respond, furrowing her brow instead as if trying extremely hard to remember her exact train of thought from the night before and not quite succeeding."
        hi "Which door were you trying to open after you got out of the restroom? The one on your left or the one on your right?"

        show karla basic_smug_cas
        with chchange

        li "..."
        hi "You didn't forget that you changed rooms this time around, did you?"

        show karla basic_smileclosed_cas
        with chchange

        li "..."
        "Karla has watched the one-sided conversation with more than a small hint of amusement and takes this moment to chip in."
        ka "Hahaha, you're lucky you locked your door last night, or you'd have had one hell of an awkward awakening."
        "She has no idea just how awkward."

        show lilly basic_sleepy
        show karla basic_cheerful_cas
        with chchange

        "Lilly seems to have given up trying to figure out how she ended up mistaking our room for hers and lets out another tortured yawn. Karla shrugs."
        ka "Well, at least that little mystery is now solved. That leaves us with the matter of getting you back to the land of the living."
        li "I'm... okay."
        ka "Not convincingly so. Why don't you go and take a bath? It might make you feel better. Let me take you there."
        "Lilly slowly gets up from the couch, her movement stiff like an old-fashioned robot. I turn to Karla."
        hi "So much for the effectiveness of using a cello as an alarm clock."

        show karla basic_smug_cas
        with chchange

        ka "My own mother used the the good ol' ladle and frying pan combination to get people out of bed. I should give that a try next time. I've always wanted to wake someone up that way."

        show lilly basic_reminisce
        with chchange

        "That may very well be the cruelest thing I've heard in my entire life, and from her visible cringe, it appears that Lilly completely shares that impression."
        li "Please... don't... ever..."

        show karla basic_smileclosed_cas
        hide lilly
        with charaexit

        "Karla playfully chuckles at the comically terrified expression on her daughter's face and then takes her daughter's hand and starts guiding her towards the exit."
        "Before leaving the room she turns around to address me."
        ka "Just make yourself comfortable, Hisao. I'll be right back."
        
        hide karla
        with charaexit

        "As Lilly and her mother leave the room, I take a seat on the couch Lilly was occupying earlier."
        "Looks like Lilly's not in any better shape than I am, though it appears her parents at least remained unaware of last night's events."
        "Lilly's mother didn't seem to mind the fact that we're all feeling rather queasy, although it seems her father didn't take it quite so well."
        "I feel a bit bad about that. It seems unfair that Hanako and I got away with our little act last night, and Lilly might get into trouble for an innocent, if rather dumb, mistake."
        "That's of later concern though. I should probably focus on how to act around Hanako when she wakes up."

        show karla basic_smile_cas at center
        with charaenter

        "As I'm pondering the matter, I hear footsteps behind me and see Lilly's mom enter the room with a glass of water in her hands that she hands over to me."
        ka "You're looking a bit worse for wear yourself, so I got you something to drink."
        hi "Thanks."

        hide karla
        with charaexit

        "The water doesn't do much to dull the throbbing sensation in my head, but it eases my throat a bit and makes speaking a bit less painful."
        "Karla sits down on the love seat across from me and starts putting her cello back into its case."

        show karla basic_sweet_cas at sittingpos
        with charaenter

        ka "Just give it a bit of time. You'll probably feel better in a few hours."
        hi "I suppose there aren't any effective folk cures for this?"
        ka "There's this old Scottish remedy of putting poultices of onions under the armpits to draw toxins out of the body. But I wouldn't recommend that."
        hi "...good."

        show karla basic_smile_cas
        with chchange

        ka "Last night we could already tell that Lilly had several glasses, so we left a message in the kitchen asking Allison to make and leave you some BLT sandwiches and plenty of juice in case you guys'd be suffering from a hangover."
        ka "They'll help getting you back on your feet."
        hi "They actually help?"
        ka "They'll make you feel a little bit better."
        hi "Ummm... Not to pry into your affairs, but... was your husband very upset about Lilly drinking?"

        show karla basic_sheepish_cas
        with chchange

        "Karla frowns for a moment and gives me a sheepish look."
        ka "He wasn't upset that you guys had a few glasses or even that you got a little drunk. We felt that if Lilly failed to mind her tolerance threshold, the resulting hangover would be enough of a punishment already."
        ka "What rubbed him the wrong way was that it was the housekeeping staff who found Lilly sleeping on the couch this morning, and they seemed to find it extremely funny."
        ka "My husband felt his daughter embarrassed him and caused him to lose face in the eyes of his personnel. "
        hi "Is she going to get into trouble?"
        ka "He said she's not going to be allowed to do any more drinking for the remainder of her stay here."
        "Knowing Lilly and how much she enjoys the occasional sip of wine, that seems extremely harsh, especially since getting her hands on wine back in Japan is going to be tough with Akira now having moved away."
        "Of course, since Lilly's parents presumably don't know that about their daughter, they probably don't think it's that severe a punishment."
        hi "Really?"
        ka "You think that's too severe, don't you?"
        "I don't think it's my place to tell parents how to deal with their children. Even if those parents haven't had contact with their children for years."
        hi "I'm not sure."

        show karla basic_wistful_cas
        with chchange

        "Lilly's mother gives me a tired smile."
        ka "My husband hails from a rather traditional Japanese family, and he was taught from an early age that causing a family member to look bad or embarrassing them in any way is pretty much the biggest sin you can possibly commit."
        hi "I don't think Lilly would ever embarrass her parents on purpose."
        ka "I don't think so either. My husband's been rather tired and anxious the last few weeks. Work-related stress, no doubt. He hasn't been sleeping well either. It's making him more irritable than he usually is."
        ka "I'll talk to him later. He might change his mind."

        show karla basic_smug_cas
        with chchange

        ka "You guys aren't looking like you're going to hit the bottle again anytime soon anyway..."
        "She has a point there. Just the idea of drinking alcohol again is enough to worsen my headache."

        show karla basic_ponder_cas
        with chchange

        ka "...but enough about that for now. There's something I wanted to ask you."
        "All of a sudden, her playful look seems to have turned serious."
        ka "As you know, we have a picnic scheduled this afternoon. I was thinking of combining it with a bit of physical activity. You two know how to ride a bike, don't you?"
        "I've never asked Hanako, but it's fairly safe to assume she knows how to ride one. Lilly on the other hand..."
        hi "I do and Hanako probably does too. But how about Lilly? She won't be sitting on the rear rack of your bike, will she?"
        ka "Leave that to me. What I wanted to know is if you're up for it. Lilly didn't give me a lot of details, but I do know you've had an accident recently that resulted in a short hospital stay."
        ka "Something to do with your heart? It was the reason Akira postponed her flight. There's a hospital only a few miles away from here, but I wager it's not among the sights you're planning on seeing during your stay here."
        hi "Seems like a good goal to shoot for."

        show karla basic_smile_cas
        with chchange

        ka "Do you think you'll be able to handle it? The weather predictions for this afternoon say it's gonna be fairly hot, but we'll have plenty of time, so we can take it as easy as we like."
        "I can't say I take to hot weather very well, but between the three of us, I'm the only one working out on a daily basis. I wouldn't be surprised if I'm in better shape than Lilly and Hanako, despite my heart condition."
        hi "I might be able to handle it. I work out nearly every morning at school. I've gotten a fairly decent idea of where my limits lie."
        ka "You work out, huh? We have a home trainer in the attic. I like to take bike rides around the countryside when the weather's good, but I make a lot of use of it during the winter."
        ka "If you want to continue your daily regimen, you're more than welcome to use it."
        hi "Thanks for the offer. I'll keep it in mind."
        ka "If you think it won't be too much for you, we'll leave the car at home today."

        show karla at center
        with charamove

        "She takes a look at her watch and gets up from the couch."

        show karla basic_cheerful_cas
        with chchange

        ka "I have to stop by the office for a few hours. Today's officially my day off, but I promised I'd drop by to ensure everything's going well. I have to make a little arrangement for our picnic trip too."
        ka "I'll be back shortly after noon. Can I give you guys some advice?"
        hi "Sure."
        ka "Make sure to get rehydrated and restock on the nutrients. Help yourself to the sandwiches Allison left in the kitchen, drink plenty, get some fresh air, and then get some additional rest. You'll feel a lot better afterwards."

        stop music fadeout 2.0

        play music music_serene fadein 4.0

        hide karla
        with charaexit

        "As Karla leaves, her hand held high in a parting gesture, I take some time to reflect on what she said. What she suggested had better be nothing short of a miracle cure."
        "We agreed to prepare the food for the picnic, and now there's a bicycle ride through the countryside to get ready for as well. The way I'm feeling right now, I don't really feel up for even one of these activities, but Karla's enthusiasm is hard to refuse."

        scene bg satou_kitchen
        with locationchange

        "Fighting the lethargic sensation that's still weighing me down, I get up and make my way to the kitchen."

        show hanako defarms_shock at tworight
        with Dissolve(0.2)

        stop music fadeout 1.0

        "Not hearing any sounds coming from there, I assume it to be empty and walk in letting out an unrestrained yawn that dies abruptly as the person standing near the kitchen sink unit turns around and gasps."
        hi "Hanako! Ummm... I mean, good morning Hanako."
        "I hadn't expected Hanako to be up already. She probably went straight down to the kitchen to get something to drink. She doesn't look in much better shape than Lilly or myself, but as we spot each other, our hangovers are quickly made irrelevant by a more pressing matter."
        
        play ambient sfx_ticktock

        "Looking at her promptly brings back the memories of last night's events, and I cannot help but blush a little. There's no questioning whether Hanako picked up on my reaction as she instantly flowers into a full blush herself, followed by a desperate whimper."
        "At least this removes any doubt about whether either of us has had enough drinks last night to suffer a convenient memory loss, and with it my hopes of being able to settle this matter by simply denying it even happened in the first place are cruelly dashed."

        show hanako emb_downsad
        with chchange

        "For a moment I can see Hanako's gaze dart around the room as if looking for an escape route, and upon concluding that I'm standing in front of the quickest way out of here, she pitifully crosses her arms in front of her chest and lets her head sink, unable to look me in the eyes."
        "I don't think there's ever been a more awkward moment between us, and we've had several over the course of the few months we've known each other."
        "How do you deal with a situation such as this?"
        "Apologize?"
        "Laugh about it?"
        "Avoid the subject?"
        "I'm probably not going to get a lot of input from Hanako on this one. She seems completely preoccupied with fighting the urge to bolt from the room."
        "While I'm still deciding on how to act towards Hanako, I notice something moving from the corner of my eye, and when I look through the window I can see a person in her twenties approaching the house. She must be part of the cleaning staff."

        show hanako defarms_strain
        with chchange

        "I look back at Hanako who has noticed the woman as well and is looking slightly panicked."
        "If people see us acting the way we currently are, they're surely going to suspect something fishy is going on. We'll need to get this matter settled before the picnic this afternoon. We're going to need some privacy."
        "Maybe the nearby beach Lilly showed me during the initial tour she gave me. We could eat at the same time."
        "I notice the sandwiches Karla spoke about lying on the kitchen sink unit. I turn to Hanako and do my best to sound as casual as I can."
        hi "Hanako, Lilly's mother said those sandwiches were prepared for us. We could have some drinks as well. I'd like to take a short walk to get some fresh air. Will you please join me?"

        show hanako emb_timid
        with chchange

        "Hanako doesn't react at first, but right before I'm about to repeat my question, she gives me a barely visible nod."

        hide hanako
        with charaexit

        "I take a small shopping bag that's hanging from a hook on the wall, put several sandwiches inside, and then open the fridge to look for drinks."
        "I'd really rather not address this matter at all, but if Lilly notices how awkward we are with each other right now, she'll almost certainly jump to conclusions."
        "I don't think we'll have much of a choice but to settle matters before Lilly gets back. She was probably puzzled enough already by our sudden escape from the living room last night."
        "As I reach out for one of the several small bottles of juice labelled ‘Irn-Bru’ or something, I suddenly have a flash of insight."
        "What if Lilly heard us? We tried really hard not to make any sounds, but we couldn't supress everything. Her hearing can't be that good, can it? But she did hear the sound of her parents' car. I don't think I picked it up myself, and neither did Hanako."
        "Crap! What were we thinking anyway?"
        "Doing my best to put these thoughts aside, I help myself to a few of the bottles, put them in the bag, close the fridge and beckon Hanako to follow me outside."

        stop ambient fadeout 1.0

        scene bg inverness_shore
        show hanako emb_downsad at right
        with locationskip

        play music music_serene fadein 4.0
        play ambient sfx_waves volume 0.2

        hi "This looks like a good spot."
        "The crisp morning air coupled with the gentle sound of the water lapping against the shore gives the area a calming atmosphere. There are a few large rocks nearby that seem perfect to use as a place to sit down."
        "I look at Hanako and gesture her to sit down next to me."

        show hanako:
            ease 5.0 center
        with None

        "Since we left the kitchen she's been meekly following me without saying a single word like a bad pupil following a teacher to the detention room. Even as she sits down next to me, I notice she's sitting several paces away from me."

        show hanako at center
        with None

        "Deciding that the elephant in the room can wait until after we've had breakfast, I take a bottle and a sandwich and hand them to Hanako who quietly takes them."

        show hanako emb_sad
        with chchange

        "As we sit there, nibbling our sandwiches and then flushing the bread and meat down with the soft drinks we got, I can tell from her posture that Hanako is slowly relaxing a little bit."
        "I figure now would be a good moment to start a conversation."
        hi "I guess we're both a little under the weather after yesterday. How are you feeling right now?"
        ha "...M-My h-head hurts."
        hi "Same here. You're not nauseous, are you?"
        ha "A b-bit. But I c-can eat without b-being sick, I think."
        hi "Me too, though the meat's a bit much. Lilly's mom said these sandwiches will ease hangovers though."
        ha "I h-hope so."
        hi "If it's a consolation, Lilly isn't any better off from the looks of it. At least we slept in a bed this night."

        show hanako emb_timid
        with chchange

        ha "W-What?"
        "I briefly tell Hanako about Lilly spending the night on the couch."
        hi "Heh, so it's a good thing I locked our door, or we'd have had a really uncomfortable moment in there."

        show hanako emb_downsad
        with chchange

        ha "Ahahaha."
        "That has to be the most joyless laugh I've ever heard out of Hanako. I'm not sure if this is something Hanako will be able to laugh about later, but she certainly hasn't reached that stage right now yet."
        "Still, now that the subject's come up, it's probably best to press on."
        hi "So... um... About what happened between us last night..."

        show hanako emb_blushing
        with chchange

        "Hanako lets out a dejected sigh that makes me feel guilty about even finishing my sentence."
        hi "It's kinda awkward for me too, but Lilly's probably going to think strange stuff if we're this jumpy around one another all day long."

        show hanako emb_downtimid
        with chchange

        "That seems to get through to Hanako since she turns to me and gives me a resigned nod."
        ha "I'm... s-s-sorry."
        hi "It's okay. I giddily went along with it. We're both equally to blame."

        show hanako emb_sad
        with chchange

        ha "But I... s-started it."
        hi "You don't really see Lilly as a rival, do you? Lilly's far too loyal to you to even consider trying to steal me away from you. And I wouldn't trade you in for her either."
        hi "She's a good friend. A wonderful friend. Like an older sister. But nothing more than that."
        ha "I...I know."
        "I think Hanako's gotten to the point by now where she can believe my words if she stops to think about them rationally."
        "But on some deeper level, a part of her is probably still convinced that Lilly could easily seduce me away from her if she made even a half-hearted effort—which is probably why she got so territorial when Lilly praised my looks."
        "I'm positive, however, that that fear will eventually disappear as we continue our relationship."
        hi "This could have created an awkward situation with Lilly's parents, but in the end, we got away in time and nothing bad happened. That's what matters."
        hi "I don't think any less of you after last night. The two of us will probably be able to laugh about this later."

        show hanako emb_timid
        with chchange

        "Hanako doesn't seem too sure about that last part, but she still looks relieved by my words."
        ha "I'm... h-happy about that, but... w-we still s-shouldn't have d-done what we d-did."
        hi "Aside from the place where we started this, do you regret the act itself, Hanako?"

        show hanako emb_blushing
        with chchange

        "Her face turns as red as the tomatos on the sandwiches, but eventually she manages to softly shake her head."
        ha "N-no, b-but I... d-don't w-want to do it... l-like that again. Umm... Y-you...?"
        "Since we're boyfriend and girlfriend now and since we've had sex before, I assumed that what we did was as consentual as we could make it, but maybe I'm wrong about that."
        "She seemed to be enjoying it a lot last night, but now that I think about it, I doubt a sober Hanako would ever let me do it with her in a position that puts just about all her scars on full display like that. She's still really sensitive about them."
        "I hope I didn't overstep my bounds. That would give this whole thing a very bitter aftertaste."
        hi "I can't exactly say I hated it, but I get that we got a little carried away. I enjoyed the act itself though."
        ha "M-me too, b-but if... If your chest s-started hurting, w-would you have stopped?"
        "Suddenly I get where she's going with this."
        "I hadn't even thought about that, but it's clear that Hanako did. At least, after the fact."
        hi "I'd like to say I would have stopped in time, but I'm not so sure about it now that I think about it. "

        show hanako emb_downtimid
        with chchange

        ha "I'm... n-not sure about m-myself either, s-so..."
        "I recall what the nurse told me some time back when he gave me the talk about keeping the big head in charge at all times. That certainly wasn't the case last night."
        "Damnit! Looks like that stunt in the living room wasn't even the most irresponsible thing we did that night. Given the way we went at it last night, I could have ended back in the hospital here. That would have been hard to explain."
        "I really should have known better. Still, even though something could have happened, that wasn't the case."
        "I put a hand on Hanako's shoulder."
        hi "I get what you're saying. We took a risk that we shouldn't have taken. But nothing happened, so it's probably best not to worry about what could have occurred. There's no point in that. At least we now that know my heart can handle it."
        "I suddenly remember something Hanako said a few days earlier."
        hi "I... guess this wasn't exactly the slow and romantic experience you wanted..."

        show hanako emb_downsad
        with chchange

        "Seems like Hanako remembers that as well, and she seems genuinely disappointed."
        hi "...but let's take a rain check on it. We have weeks ahead of us, we have our own private bedroom, and Lilly's not gonna be around all the time. I'm sure we'll get plenty of opportunities."

        show hanako emb_blushing
        with chchange

        ha "O-Okay then."
        hi "Cheer up. Nobody but us knows about this little incident, and we'll just keep it that way. They say that shared secrets strengthen a couple's bond with one another."

        show hanako emb_downsmile_close
        with chchange

        "I give Hanako a kiss on the cheek, and for the first time this morning, there's a little smile on her face."
        ha "Okay. No telling anyone."
        hi "How are you feeling right now?"

        show hanako emb_sad_close
        with chchange

        ha "My h-head still hurts."
        hi "Let's take another sandwich and another soft drink."

        show hanako emb_downtimid
        with chchange

        ha "I'm not really that hungry."
        hi "Lilly's mom said it helps against hangovers. Let's share this one."
        "I break the sandwich in two and give Hanako one half."
        "After eating my half, I finish my bottle of juice. I notice Hanako has only finished half her bottle."
        hi "You're not going to drink anymore?"
        ha "One bottle was enough for me. I'm not r-really thirsty anymore."
        "We take a moment to just sit here and enjoy the fresh breeze blowing over the bay."
        "It's still relatively early in the morning, and the picnic won't take place until after noon. I'm not really sure how long it'll take for Lilly and Hanako to prepare the snacks, but I doubt it'll take hours even in their current condition."
        hi "Hanako?"

        show hanako emb_sad
        with chchange

        ha "Yes?"
        hi "I'm still kinda tired. What do you say we head back to our bedroom and get a few more hours of sleep. We'll probably feel better afterwards."
        ha "What about the snacks?"
        hi "It's not going to take hours, and I'll help out if necessary. I'll set the alarm function of my cell phone to wake us up at half past 11. Lilly's mother won't be back until noon anyway."
        ha "Just a few hours then."
        hi "Let's go."
        "I take Hanako's hand, and we walk back to the mansion."

        stop ambient fadeout 1.0

        scene bg satou_stairs
        with locationchange

        "As we enter, we're greeted by the housekeeper who informs us that Lilly went back to bed for a little while as well."
        "Deciding to follow her example, we make our way up the stairs. Let's hope we'll feel better at noon."

        stop music fadeout 2.0

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return

    label .s2:

        $ set_window_tint(TINT_HISAO)

        scene bg satou_kitchen
        show hanako basic_bashful at tworight
        show lilly basic_weaksmile at twoleft
        with Dissolve(1.0)

        play music music_daily fadein 4.0

        hi "Are you certain you don't need my help preparing all of this? There's a truckload of food on this table."
        li "Very certain, Hisao. You know what they say. Too many cooks in the kitchen spoil the broth. We might end up getting in each other's way."
        hi "I could help Hanako sort all this stuff out."

        show hanako basic_normal
        with chchange

        ha "Ummm..."
        li "The offer's appreciated, Hisao, but I think it won't be necessary. If I can think of something, I will let you know."
        "I sigh softly and sit back down in the kitchen chair near the fridge."

        show lilly at center
        with charachangealways

        "Lilly and Hanako do look like they can handle themselves with the picnic food, but I don't really like feeling like dead weight."
        "Either Lilly's mother was right, and those sandwiches really helped or those hours of additional sleep worked their magic on us, but the gist of it is that all three of us are now feeling good enough to actually be looking forward to a little outing into the countryside."
        "Nevertheless, I can still feel the occasional painful throb dance around the insides of my skull, and I would welcome having something to do to distract from the sensation."

        show hanako basic_worry
        with chchange

        ha "Ummm, Lilly... What's a f-ficelle?"
        "The kitchen table is filled with enough ingredients to prepare a buffet of, from pieces of bread to bottles filled with stuff like mustard and vinegar, to various pieces of fruit and vegetables."
        "We spent the last 15 minutes unpacking everything in the shopping bags supposedly left here by the housekeeper, and now Hanako is frantically switching back and forth between checking the pieces of paper in her hand containing recipes and putting the various items in order."

        show lilly basic_smileclosed
        with chchange

        li "It's a thinner variation of a baguette: a French loaf of bread."

        show hanako basic_distant
        with chchange

        ha "Ah, okay."
        li "Has the oven already reached the right temperature? I believe it should be at 200 degrees."
        ha "Not just yet."
        li "We should put the bread in as soon as we can or we won't be able to finish the sandwiches in time."

        show hanako basic_worry
        with chchange

        ha "I'll keep an eye on it."
        "We ended up getting out of bed slightly later than planned, and as a result, Lilly seems to have stepped up her usual pace a bit, carving loaves of bread so quickly it makes me feel it's a miracle she hasn't cut her fingers off yet."
        "Hanako, in the meantime, is working hard at fulfilling her role as Lilly's first mate, repeatedly reading the various recipes out loud and putting all the ingredients in a specific order on the table while cutting up pieces of bread, fruit, and vegetable whenever she has the chance."

        show lilly basic_surprised
        show hanako basic_normal
        with chchange

        li "It'd be best if we made sure the ingredients for the tartines and sandwiches are ready by the time we take the bread out of the oven so we can apply the butter while the bread is still hot."
        ha "For both the radish tartines and the avocado and ham sandwiches?"
        li "Do you think it's possible?"
        ha "If we both work to get the avocado and radishes c-cut up in time. But we must make sure the water with the macaroni d-doesn't boil over."
        
        show lilly basic_smile
        with chchange

        li "Hisao, could you please keep an eye on the macaroni? It's supposed to cook for... ah... Hanako?"
        ha "Mmm... Four more minutes."

        show lilly basic_smileclosed
        with chchange

        li "Four more minutes. If you could drain the water afterwards and put the macaroni in the bowl near the sink, that would be much appreciated."
        hi "I'm on it. Anything else?"
        li "Not at the moment."
        "It's hardly active work, but it's better than nothing."

        play ambient sfx_boilingwater

        "I get up from my chair and get over to the kitchen island where a pan filled with water and macaroni is boiling on the fire."

        show lilly basic_smile
        show hanako basic_bashful
        with chchange

        li "What more do we need again for the radish tartines, Hanako?"
        ha "Ah... Six tablespoons of soft, salted butter, sea salt and freshly ground pepper. Um... I was t-thinking that maybe we could add a bit of black pepper as well. We have plenty for the melon slaw."

        show lilly basic_weaksmile
        with chchange

        li "I'm sorry, Hanako, but for this occasion I'd like to stick strictly to the recipes we have. This is the first time my mother gets to experience my cooking."
        ha "Oh... ummm... Okay."

        show lilly basic_smileclosed
        with chchange

        "That certainly explains why Lilly is taking this whole thing so seriously and why she insisted on Hanako playing merely a supportive role in the whole thing. This isn't just a picnic to her, but an opportunity to prove herself to her mother."
        "It kind of makes sense that she doesn't want to throw an unnecessary risk into the mix by going along with Hanako's hit-and-miss culinary instincts. Fortunately, Hanako doesn't take Lilly's comment personally, or at least she doesn't show it."
        
        stop ambient fadeout 0.5
        play sound sfx_boilingwater_pour
        
        "I pour off the water and fill the bowl Lilly mentioned with the contents from the pan."
        hi "I'm finished with the macaroni, Lilly. Where do you want me to put it?"
        li "Just leave it with Hanako, Hisao."

        show hanako defarms_worry
        with chchange

        play sound sfx_ovenbeep

        "Before I can approach the kitchen table, a high-pitched whine from the oven draws our attention. Hanako gets up from her chair, places the bread she and Lilly prepared into the oven, and then takes the bowl of macaroni from my hands."
        "She places it on the table some distance away from Lilly and herself."

        show lilly basic_cheerful
        show hanako basic_worry
        with chchange

        li "Thank you, Hanako. Shall we proceed with the radishes for the tartines and the avocado and ham for the sandwiches?"
        li "If it's not a problem with you, you can do the radishes and move on with the cucumber and pear for the melon slaw when you're done with them. I will handle the avocado, ham, and shallots."
        ha "Okay."

        play sound sfx_cuttingboard

        "Having nothing more to do, I get back to watching Lilly and Hanako work. They do seem to work well together, and someone looking at Lilly without paying attention to her eyes probably wouldn't be able to tell that she's blind."

        play sound sfx_cuttingboard

        "Eventually, another sound from the oven alerts us to the fact the bread is ready, and after Hanako—armed with two oversized oven mitts—retrieves it, she gets back to cutting up the vegetables and fruit while Lilly starts working on putting the sandwiches together."

        show lilly basic_satisfied
        with chchange

        li "Hisao?"
        hi "Yes, Lilly?"
        li "If you're still looking for something to do, would you be so kind as to get some cellophane wrapping from the drawer near the oven and wrap up the snacks as I finish them? Allison said that Mother left some saddlebags in the hallway. Would you...?"
        hi "Sure, I'll go and get them."
        "I retrieve the saddlebags from the hallway, take a seat near Lilly, and start wrapping up the snacks."
        "With Hanako preparing the ingredients, Lilly putting everything together, and me wrapping up the snacks and putting them in the bags, it's almost as if we're running a miniature assembly line."
        "Although my activities take considerably less time, and I'm still spending a lot of time watching the girls perform their respective tasks."
        li "That should be all for the radish tartines. How far are you with the ingredients for the melon slaw, Hanako?"

        show hanako basic_smile
        with chchange

        ha "I'm finished with them."

        show lilly basic_listen
        with chchange

        li "Good. Could you walk me through the steps one more time?"

        show hanako basic_normal
        with chchange

        ha "The s-shallots, mint, vinegar, honey, salt, and pepper have to be whisked together. The pieces of pear, cucumber, jicama, and watermelon are added afterwards."
        "As she says this, Hanako gets up and starts putting the various bowls, bottles, and cans with ingredients in front of Lilly, occasionally thinking for a moment before swapping two."
        "She finishes up by putting a large bowl and a whisk in front of Lilly."
        ha "I put all the ingredients in front of you. Anything else you w-want me to do?"
        li "How far are the preparations for the macaroni salad?"

        show hanako basic_worry
        with chchange

        ha "Ah... Everything's done except for the cheese."
        li "If you could melt the cheese and mix it with the macaroni, that would probably save me a lot of time. I'll finish the rest once I'm done with the melon slaw."
        ha "Okay."

        play sound sfx_whisking

        "With that, Hanako and Lilly get back to work, and since the melon slaw Lilly's working on will be contained in just one large bowl, there's not a lot for me to do until she finishes."
        "As I watch Lilly getting started on the meal in front of her, something suddenly draws my attention. Lilly's hands are sweeping across the surface of the bowls, but she doesn't put her hands inside to feel the contents."
        "Come to think of it, while she was working on the avocado and ham sandwiches, she also seemed to immediately know what bowl contained which ingredients yet I didn't hear Hanako instruct her beforehand."
        hi "Ah... Lilly?"

        show lilly basic_smileclosed
        with chchange

        li "Yes, Hisao?"
        hi "How do you know which bottles and bowls contain what? I don't recall Hanako telling you in advance."

        show lilly basic_planned
        show hanako emb_downsmile
        with chchange

        li "Hmmmm..."
        "Lilly's only answer is an amused smile. There's a little smile on Hanako's face too as if they're enjoying some private joke at my expense."
        hi "It's not a secret, is it?"

        show lilly basic_giggle
        show hanako emb_smile
        with chchange

        "Lilly lets out an amused giggle."
        li "Don't worry, Hisao. It's not. Hanako made sure to order the ingredients by type of container first and then alphabetically."
        li "The ingredients required for the first step were placed at ten o' clock from my point of view and those required for the second step were placed at two o' clock."
        hi "You mean to say you two have got a system in place for ordering this kind of stuff?"
        li "We do. It's not the first time we've cooked together. Having a fixed location for everything isn't just important when cooking without sight."
        li "It's also essential in keeping your life in general in order when you're unable to see. Hanako knows almost exactly how I like things ordered, both in the kitchen and in my dorm room. She's one of the very few who do."
        hi "So that's why you didn't want me helping her with this?"

        show lilly basic_weaksmile
        show hanako basic_smile
        with chchange

        li "...Indeed. I appreciated the offer, but we weren't given a great deal of time to prepare everything, and it was important to work as efficiently as possible."
        hi "I guess there are some things that are better left to the pros, huh?"

        show lilly basic_giggle
        show hanako emb_smile
        with chchange

        "Lilly laughs cheerfully at that remark, even though it makes Hanako blush a little."

        show lilly basic_surprised
        show hanako basic_normal
        with chchange

        play sound sfx_phonering

        "Lilly opens her mouth to say something, but before she can do so she's interrupted by a sudden sound that I recognize as the ringtone from her cell phone."

        show lilly back_listen
        with chchange

        li "Please excuse me... Good morning. Lilly Satou speaking."

        show lilly back_smileclosed
        with chchange

        li "Good morning, Mother."

        show lilly back_pout
        with chchange

        "I hear Lilly letting out a sigh at the obvious question."
        li "Yes, I feel much better now."

        show lilly basic_weaksmile
        with chchange

        "She puts down her phone for a moment and briefly turns her head in our direction."
        li "How about you?"
        hi "I'm okay. My head still feels a little heavy, but nothing severe enough to stay in bed for."
        ha "M-Me too."

        show lilly back_smileclosed
        with chchange

        li "Mother?... We're all looking forward to this afternoon."
        li "No, we're in the kitchen right now. We've been preparing the food for the picnic."

        show lilly back_listen
        with chchange

        li "I'm sure Allison would have made some wonderful snacks too, but she's not the only person in the world who can cook. I'm sure it'll taste all the better for it."

        show lilly back_smileclosed
        with chchange

        li "Half an hour? Yes, that's more than enough time."
        li "We will see you soon then. Bye."

        show lilly basic_smile
        with chchange

        hi "She'll be here in half an hour?"
        li "Yes, she's just left the office, but still needs to arrange our transportation for today."
        hi "Half an hour isn't that much time to finish the remaining food."

        show lilly basic_cheerful
        show hanako basic_smile
        with chchange

        "Lilly replies with an eager smile on her face."
        li "Let's get started quickly then."

        stop music fadeout 2.0

        scene bg satou_grounds
        with shorttimeskip

        play music music_tranquil fadein 4.0

        play sound sfx_car_driveup

        hi "It sounds like we're right on time."
        "As we exit the house, we hear the noise of a car approaching, and moments later we can see a car with an open trailer behind it coming up the driveway."

        show karla basic_cheerful_cas
        with charaenter

        "Stopping the car near the garage door, Lilly's mother gets out and looks at our fully-packed saddlebags approvingly."
        ka "Looks like you went all-out with the food. I can't wait to taste it. Well, I guess I'll have to since we'll still have to make our way over to a suitable picnic spot."
        ka "Hisao, would you mind giving me a hand with the vehicles? They're kinda troublesome to handle on my own."
        hi "Sure."
        
        hide karla
        with charaexit
        
        "Lilly's mother walks up to the trailer, climbs inside, and pulls one of the vehicles lying inside upright."
        "I smile as I see what she's holding."
        hi "Tandem bikes. Nice."

        show karla basic_smileclosed_cas at tworight
        with charaenter

        "Lilly's mother smiles cheerfully."
        ka "I figured I'd rent two of them so you and Hanako won't have trouble keeping up with us. It might take a bit of getting used to at first, but I'm sure you'll pick it up in no time."
        "I walk up to her, and together we lift the two bikes out of the trailer. Lilly's mom reaches inside the car, retrieves a plastic bag and takes four water bottles out of it."

        show karla basic_smile_cas
        with chchange

        ka "One water bottle per person isn't really all that much but we should have plenty of beverages to fall back on if needed and we might be able to refill on the way. Anybody's willing to go and fill these up?"

        show lilly cane_smile at twoleft
        with chchange

        li "I will do it. Perhaps you can get the saddlebags attached in the meantime?"
        "Lilly steps forward and takes the bag from her mother."

        hide lilly
        show karla basic_lost_cas
        with charaexit

        "As Lilly disappears into the house and we get started on putting the saddlebags on the tandems' baggage racks, Karla turns to me with her expression turning serious again."
        ka "Hisao, yesterday's weather reports predicted reasonably warm weather for today, but the impression I got just by being outside for a little while is that they might have been off by several degrees."
        ka "It's not too late to call this off and take the car. It has a pretty solid air conditioning system if I say so myself."

        show hanako emb_timid at twoleft
        with chchange

        hi "I haven't had problems with my heart since I got out of the hospital. I'll probably be fine."
        ka "It's not necessarily your heart you need to watch out for in this kind of weather. Have you experienced heat stress recently?"
        hi "Heat stress?"
        ka "I've heard once that people with heart conditions run an increased risk of heat illnesses. A heat stroke may not sound as nasty or deadly as a heart attack, but it can still mess you up pretty badly."
        "I notice our discussion has attracted Hanako's attention, and she's currently looking at me with a slightly worried expression."
        "It's true that I felt some signs of discomfort while taking walks through the city near Yamaku on hot days in the past, but I think prematurely calling off our bike ride is a bit of an overreaction."
        hi "I'll be sure to drink sufficiently and give a call if I'm feeling unwell."

        show karla basic_smile_cas
        with chchange

        play sound sfx_snap

        "Lilly's mother gives a satisfied nod and then suddenly snaps her fingers."
        ka "This might help as well. Just a second."

        show hanako basic_worry
        hide karla
        with charaexit

        "She walks over to the car and gets some items from the backseat."

        show karla basic_smile_cas at tworight
        with charaenter

        "As she walks back to us, I notice she's carrying two large sun hats in addition to a cap, the latter of which is promptly pressed on my head."
        "The sun hats, both of them made out of straw and each of them having a decorative ribbon wrapped around the top half, look very elegant."

        show hanako basic_smile
        with chchange

        "However, when I take off the cap to take a closer look at it, I can see it's a rather cheap piece of headwear that's probably part of a promotional campaign or something. I read the letters on the front and give Karla an unsure look."
        hi "‘Boyd's bike rental’?"

        show karla basic_sheepish_cas
        with chchange

        ka "They gave me this one after I rented those two tandem bikes. The visor'll at least keep the sun out of your eyes."
        "That's probably its one redeeming quality. I hesitantly put it back on again and look at Hanako."
        hi "This makes me look silly, doesn't it?"

        show hanako emb_downsmile
        with chchange

        "Hanako quietly shakes her head, but the fact that she's using her hand to try and cover her smile indicates she's probably thinking something else entirely."
        "Karla gives me a playful slap on the shoulder."
        ka "I'd say it's still better than wearing a sun hat designed for ladies."

        show karla basic_smile_cas
        with chchange

        "It's hard to argue with that. Neither of us seems to have much to add to the discussion so we focus on attaching the saddlebags to the bicycles until we see Lilly returning to us carrying four filled-up water bottles."

        show lilly cane_smileclosed
        show hanako basic_smile:
            xalign 0.17
        with charaenter

        "Karla takes the bottles from her daughter, places them in the bottle cages located on the frame and hands her one of the sun hats she took out of the car. She then gestures us to take our bike. I turn to Hanako."
        hi "So, do you want to go in the front or in the back?"
        ha "What w-would you like?"
        hi "I'll do the steering if you don't mind."
        ha "Okay."

        show hanako defarms_worry at center
        hide lilly
        hide karla
        with charaexit

        "With that out of the way we both get in the saddle and I flip the kickstand."
        hi "Alright, on the count of three... {w=0.5}One... {w=0.5}two... {w=0.5}three."

        show hanako defarms_strain:
            parallel:
                ease 0.2 ypos 1.05
            parallel:
                ease 0.05 xpos 0.49
                ease 0.1 xpos 0.51
                ease 0.05 xpos 0.5
        with persistent.charachangefast

        ha "Ah!"
        hi "Whoa!"
        "That proved trickier than I thought. Keeping your balance is quite difficult when someone on the same bike is trying to do the same at the exact same moment."
        "Lilly and her mother seem to be doing slightly better mostly due to Karla seeming better at anticipating her daughter's movements."

        show hanako defarms_worry at center
        with Dissolvemove(0.5)

        hi "Okay, let's try that again. Try to stay straight up, Hanako. Let me do the correcting. {w=0.5}One... {w=0.5}Two... {w=0.5}Three."

        show hanako:
            ease 0.2 ypos 1.02
        with Pause(0.2)

        "Much better. As long as we keep moving at a decent pace we won't have to worry about our balance. Going around corners will still be tricky with such a long vehicle, so we'll just have to make sure to take wider turns."
        "As we reach the end of the driveway, Karla stops her bike and gives us an approving look."
        ka "It looks like you're doing okay. It might take some time to find a cadence that suits both of you, but I'm sure you'll figure out what works best."
        hi "So where are we headed?"
        ka "We'll go east to the village of Culloden, and then we'll head south from there."
        hi "Lead the way then."

        stop music fadeout 2.0

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return

    return