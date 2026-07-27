label sh_ch47:
    label .s1:

        $ set_window_tint(TINT_AKIRA)

        call sisterhood_timeskip_broken

        scene bg satoujp_ext
        with Dissolve(2.0)

        play music music_pearly fadein 4.0

        aki "This seems to be the place..."

        nvl clear
        nvl show dissolve

        n "I check the address in my business organizer one last time and then steer my rental car up the driveway. After parking the car, I take a long look at the house in front of me."
        n "{vspace=30}It's nowhere near the size of the mansion-like place they had in Inverness, though still larger than the average Japanese home. The neighborhood I just drove through doesn't have that same conservative upper-class feel our childhood neighborhood had either."
        n "{vspace=30}I wonder what made Mom and Dad pick this place."

        nvl clear
        nvl hide dissolve

        # TODO play buzzer noise

        "I sigh and then reluctantly push the buzzer. I wasn't really planning to drop by here today or... well... any day soon, but due to certain circumstances I ended up changing my mind."
        "It'll probably be okay though. I brought along a couple of manga to keep busy. And I really do want to see Lilly while I'm here. Lilly and..."

        scene bg satoujp_entryway
        show karla basic_cheerful_cas
        with locationchange

        kamo "Akira! Good to have you here."
        "Unsurprisingly, it's Mom who opens the door and greets me."
        aki "Yo."
        "She steps aside, and I walk past her into the entryway area where I start removing my shoes and prepare to put on some slippers. While I'm doing so, I take another look at Mom."
        "She's wearing a sky-blue kimono that doesn't look familiar to me, meaning she probably bought it after she and Dad moved back to Japan."
        "It feels weird seeing her wear one again after having gotten somewhat used to seeing her in her business attire on the workfloor. Which in turn felt strange when I first got to Scotland, because before Mom and Dad left Japan Mom used to wear kimonos quite often."
        "As I finish putting on my slippers Mom makes a graceful bow."

        show karla basic_smileclosed_cas
        with charaenter

        kamo "Welcome home, Miss Satou. Please enjoy yourself."
        aki "Home, huh?"
        kamo "Since you've never been here before, remind me to show you around later. Ah, and happy New Year, of course."
        aki "Yeah, the same."

        scene bg satoujp_livingroom
        with locationchange

        "I follow Mom through the hallway into the living room. A pretty cozy living room from the looks of it. A low table, two large couches, some dressers near the wall and a huge Christmas tree near the corner."
        "One of the cabinets probably contains a stereo, for I can hear soft classical music coming from somewhere."

        show hiroyuki thinkraised at tworight
        show karla basic_sheepish_cas at right
        with charaenter

        "Seated on the couch, dressed in a dark kimono himself and cradling a book in his lap (no surprise there) is Dad."

        show hiroyuki bow
        with charachangealways

        pause 0.3
        show hiroyuki thinking
        with charachangealways

        "As I approach, he calmly puts his book down, gets up and makes a formal bow."
        hyd "Glad you could join us, Akira. Happy New Year."
        "I make a polite bow myself."
        aki "You too."

        show karla basic_smileclosed_cas
        with chchange

        "Mom gives me a light pat on the shoulder."
        kamo "So, what can I get you?"
        aki "I suppose you don't have beer?"

        show karla basic_cheerful_cas
        with chchange

        kamo "You supposed wrong. Have a seat and I'll go and get you one."
        aki "...Thanks."

        show karla basic_sheepish_cas
        with chchange

        show karla at offscreenright
        with charamove

        hide karla

        "Mom walks out of the room, and I'm about to sit down when I hear a shuffling sound behind me, followed by a familiar voice."
        li "Father, I just heard the doorbell. Was that...?"

        show lilly basic_listen at twoleft
        with charaenter

        "I instantly break out into a smile which grows even bigger when I see my sister carefully navigating into the room."
        aki "Hey there, Lils!"

        show lilly basic_concerned_close at center
        with chchangefast

        play sound sfx_impact

        with vpunch

        show hiroyuki smileclosed
        with chchange

        "I walk up to Lilly and grab her in a not-so-gentle bear hug, chuckling to myself when she lets out an involuntary whimper."
        "Yup, still a wimp."

        show lilly basic_overjoyed_close at center
        with chchange

        "After recovering from the surprise, Lilly happily hugs me back."
        "We stay like that for a second, and then I break off the embrace and give my sister a long look-over."

        show lilly basic_smileclosed at twoleft
        show hiroyuki thinking
        with chchange

        aki "Well, don't you look gorgeous?"
        "My words aren't empty flattery. Lilly truly looks beautiful in her dazzling white kimono. Mom must have bought it for her after they moved back here."

        show lilly basic_smile
        with chchange

        li "Hello Akira. I'm so glad you could make it here. Happy New Year."
        aki "Happy New Year to you as well. It's really good to see you again too. How's the studying coming along?"

        show lilly basic_weaksmile
        show hiroyuki smile
        with chchange

        li "We've set a goal to get at least six hours of studying in today, despite it being New Year. For now, we're still on schedule. Hopefully it'll allow us to catch up later."

        show hiroyuki thinking
        with chchange

        aki "‘We’, huh?"

        show hanako emb_timid at left
        with charaenter

        "I look past Lilly and spot another kimono-clad figure partially hiding behind the doorway. I walk up to her and give her a hug that's slightly more gentle than the one I just shared with Lilly."
        "There's a soft gasp, but then, moments later, the embrace is awkwardly returned."
        aki "Hi Hanako. Nice to see you as well. Happy New Year."

        show hanako emb_smile
        with chchange

        ha "H-Happy N-New Year, Akira."
        "I give Hanako a look-over that's quick enough to avoid making her uncomfortable."

        show lilly basic_smileclosed
        with chchange

        aki "I'll be damned if you aren't the cutest sight I've seen in months."

        show hanako emb_downtimid
        with chchange

        ha "Uhhh..."
        "Hanako fidgets uncomfortably, but I meant what I just said. Cute is probably the most accurate way to describe Hanako."
        "The pink kimono she's wearing is a nice contrast with Lilly's, and her hair is done up in such a way that it still manages to hide most of the scarring on her neck. That all-too-familiar lock covering the right side of her face is still there, but it doesn't look too jarring."
        "The kimono itself is probably just a little bit on the large side, though that might have been intentional, seeing that a good part of Hanako's wardrobe is slightly too large so she can hide her scars better."
        "On the other hand, when I hugged her I couldn't shake the impression that she's gotten slightly skinnier. I do hope she's still eating enough these days."
        aki "Did you do up your hair yourself?"

        show hanako emb_downsmile
        with chchange

        "She shyly nods."
        "I'm kind of impressed. That couldn't have been easy, though the alternative, letting someone else close enough to clearly see her scarring, was probably a much worse prospect for Hanako."
        "All in all she still did a good job, aside from one spot near the back where it seems just a little bit uneven."
        aki "Color me impressed."

        show lilly basic_displeased
        show hanako emb_downtimid
        with chchange

        nvl clear
        nvl show dissolve

        n "My thoughts return to several weeks ago, when Dad made a surprise phone call and abruptly dropped a bombshell. He and Mom had decided to adopt Hanako into our family, and he wanted to know if I had any objections to the idea of having another sister."
        n "{vspace=30}The way Dad phrased it gave me the impression that the decision had already been made, though at least he gave me an opportunity to voice my opinion, which is more than he himself got when Koji Kojima was adopted by Granddad."
        n "I told Dad back then that I had no issues with Hanako being my sister, and I still stand behind those words, even though my feelings about this situation are more complex than just that."

        nvl clear

        n "Lilly told me that Hanako would be visiting this place the day after Christmas together with Hisao and that our parents were planning to use that occasion to make her the offer. I made Lilly swear a solemn oath to phone me and tell me how things went as soon as she was able to, even if that meant calling me in the middle of the night."
        n "{vspace=30}From what I heard, the proposal came so out of nowhere for Hanako that she was shocked into a silence that lasted for several minutes. Lilly eventually broke said silence by telling Hanako that it was probably a good idea to take as much time as she thought she needed to think about it. With the pressure somewhat relieved, the subject was dropped and the conversation went back to the upcoming exams until it was time to go, and Dad dropped Lilly, Hanako, and Hisao off at the nearby train station."

        nvl clear

        n "That was a little less than a week ago."
        n "I'm pretty confident that if Hanako had signed those adoption papers at any point between then and now, Lilly would have phoned me about it immediately, so it seems like this whole thing is still very much up in the air."
        n "{vspace=60}Two days ago, Lilly managed to talk Hanako into accompanying her and spending New Year's Eve and New Year's Day at this place instead of going along with Hisao. No doubt there was the unspoken intention of trying to get her to warm up to Mom and Dad."
        n "But I wonder how Hanako really feels about all of this..."

        nvl hide dissolve

        show karla basic_confused_cas at right
        with charaenter

        kamo "Akira?"
        aki "Huh?"
        "My thoughts are suddenly interrupted by Mom entering the living room with a glass of beer in her hand."
        kamo "A penny for your thoughts."
        aki "Eh, it's nothing."
        "I take the glass of beer and sit down on the couch across from Mom and Dad."
        "I look at Lilly and Hanako from over my shoulder, but notice that neither of them has moved from their spot."
        aki "No desire to catch up with me, girls?"

        show hiroyuki thinkraised
        with chchange

        "Dad readjusts the pair of glasses resting on the tip of his nose."

        show karla basic_sheepish_cas
        show lilly basic_weaksmile
        show hanako emb_timid
        with chchange

        hyd "Your timing was a bit unfortunate. They had a short break 15 minutes ago and just resumed studying when you arrived here. Taking another break this soon would be irresponsible."

        show hiroyuki serious
        with chchange

        "Boy, the old man is really staying on top of them with this. Lilly smiles awkwardly."

        show hiroyuki thinking
        with chchange

        li "We have two more hours of cramming planned. There will probably be plenty of opportunity to catch up later. I'm looking forward to it."
        aki "Well, okay then. Give it your best shot, you two."

        show hiroyuki serious
        with chchange

        show lilly basic_smileclosed at offscreenleft
        show hanako basic_normal at offscreenleft
        with charamove

        hide lilly
        hide hanako

        "Lilly and Hanako nod and then walk out of the room, leaving me alone with Mom and Dad."
        "Great."

        show karla basic_smile_cas
        with chchange

        kamo "So, Akira, how are things in Inverness these days?"
        aki "Okay, I guess. Not really all that different from the way they were when you were there three weeks ago."

        show karla basic_distant_cas
        with chchange

        "Mom rolls her eyes at my response."

        show karla basic_confused_cas
        with chchange

        kamo "And how are things with your boyfriend? Has he already made a decision whether to stay in Scotland or not?"

        nvl clear
        nvl show dissolve

        n "Just over two months ago, I apologized to Yuichi, and we decided to give things another try."
        n "With Koji's help, I managed to arrange a temporary transfer for him, so he could check things out, rather than immediately moving permanently."
        n "{vspace=30}We decided against him moving in with me. Not only is my apartment a bit too small for two people to live there comfortably, but we both felt that it was best to let our relationship recover a bit from the previous breakup rather than immediately spend 24/7 around each other. He's living in an apartment a few kilometers away from my own."

        nvl hide dissolve

        aki "Well, he's still working on getting settled. The new work culture took him longer to adapt to than he thought, but he responded pretty well to my attempts to get him... you know... a bit integrated."

        show karla basic_sheepish_cas
        with chchange

        kamo "What kind of attempts?"

        nvl clear
        nvl show dissolve

        n "After moving to Inverness, I went out of my way to engage in activities that involved a lot of other people so I wouldn't end up like Dad: doing nothing with my life except working or sitting at home."
        n "Since I knew that getting to know people in the workplace was probably not going to cut it anymore, I joined a fitness club and started taking part in pub quizzes during the weekend."
        n "{vspace=30}When Yuichi joined me in Inverness, I dragged him along whenever I could, but we're both at a point now where we know a few people we can hang out with in our free time if we want to. If he'd decide to stay there permanently, he probably wouldn't be lonely."

        nvl hide dissolve

        aki "Just general stuff."

        show karla basic_displeased_cas
        show hiroyuki eyebrow
        with chchange

        "Mom and Dad raise an eyebrow at my non-answer, but neither seems eager to start prying. Maybe that's a good thing."

        show karla basic_confused_cas
        show hiroyuki serious
        with chchange

        hyd "What do his parents think about the option of him moving?"
        aki "They said they'd leave the choice up to him."
        "They'd certainly miss his presence, but since there's already someone else helping out with the family restaurant, I don't think they'd demand for him to stay in Japan."

        show karla basic_smile_cas
        show hiroyuki thinking
        with chchange

        kamo "And up to you. I hope the two of you can manage to make this work. Maybe you can officially introduce him to us next time."
        "I can’t help rolling my eyes at that. Yuichi's an employee of the company. Surely they’ve checked him out already."
        aki "Uhuh..."

        show karla basic_troubled_cas
        with chchange

        "Mom frowns."
        kamo "You don't seem extremely talkative."
        aki "Never mind me. I'm just a little tired. It was a long drive."

        show karla basic_sheepish_cas
        show hiroyuki thinkraised
        with chchange

        "Dad makes a gesture towards the doorway."
        hyd "You can rest in one of the guest rooms if you like."
        aki "That'd be good."

        scene black
        with locationchange

        "I drink the remainder of my beer and then follow Mom, who gives me a little tour of the kitchen and the dining room..."
        kamo "Well, how about it? Do you think you could make yourself feel at home here?"
        aki "...Who keeps this place clean whenever you're in Scotland? Does Dad have hidden homemaking skills he's never shown until now?"
        kamo "We have a housekeeper employed who helps me out with keeping the house in order and who's also been willing to take care of breakfast and dinner in my absence, at least until your father starts his new job."
        "...the study..."
        aki "That room sure looks familiar."
        kamo "Almost as if he packed the old room in his suitcases and brought it along, isn't it? The actual room is a little bit smaller, so some of his books are stored in the attic, but overall we made this place identical to his study in Scotland."
        "...the bathroom..."
        aki "It's still larger than I thought. Instead of two families, that bath can now only house one, which is still way larger than the tub I have in my apartment."
        kamo "Your father has always liked relaxing soaks, though we don't need a bath like the one in Inverness anymore."
        aki "Have you ever needed a bath that large during those years you lived in Scotland to begin with? Why get a bath that can house like seven or eight people when it was just you and Dad living there?"
        kamo "Because we had business delegations from Japan on occasion, and your father would often let them stay at our home instead of letting them sleep at a hotel."
        kamo "Since Inverness has no Japanese communal bath houses, it was not uncommon for the members of such a delegation to have a shared soak at our place. Obviously, this bathroom here will only be used by our family."
        aki "Okay, that kind of makes sense."
        "...the attic..."
        aki "This place kind of looks like a small office."
        kamo "The study is your father's place to retreat to to do some work or reading, so I decided to claim this little room for myself. I'd like to start working again at some point, after things have settled down for Lilly and your father, and when I do, this place'll be my little base of operations."
        aki "What on earth do you need an old typewriter for?"
        kamo "Heh, I wrote pretty much all of my articles on a typewriter like this one back when I was still in the reporting business. I like the nostalgic feel it adds to the place. I'll be using a personal computer for actual work, of course."
        aki "Oh."

        scene bg satoujp_guest
        show karla basic_smileclosed_cas
        with locationchange

        "...and finally the bedrooms."
        aki "Didn't get around to properly furnish this one yet, huh?"

        show karla basic_sheepish_cas
        with chchange

        kamo "It's not that we didn't have time to give this room a personalized touch. It's just that we weren't sure what kind of touch you'd want."
        aki "Me?"

        show karla basic_sheepishclosed_cas
        with chchange

        kamo "This house has three bedrooms in addition to the master bedroom, so you can all have your own room. Lilly has already given a few pointers on what she'd like her room to look like. We were hoping you'd be willing to do the same."
        aki "Lilly visits this place almost weekly. It makes sense to give her her own room. It's not like I'll be in Japan that often."

        show karla basic_sheepish_cas
        with chchange

        kamo "We have enough bedrooms available. If you don't have any immediate suggestions, I could also drop by your apartment the next time to see what your interior tastes are like."
        aki "Uh..."

        show karla basic_smug_cas
        with chchange

        "Mom gives me a teasing smile."
        kamo "Or I could just decorate this place exactly like your bedroom of 20 years ago. I remember that one vividly."
        aki "I hope you're not being serious."

        show karla basic_confident_cas
        with chchange

        kamo "I hope it won't be necessary. Anyway, I'll let you have some peace and quiet now. You can rest up a little bit for an hour or two."
        aki "Two hours?"

        show karla basic_sheepish_cas
        with chchange

        kamo "We're planning to pay one of the nearby shrines a little visit together later today. It's been a tradition in this family for as long as I can remember."
        aki "It hasn't really been a tradition over the last couple of years."

        show karla basic_distant_cas
        with chchange

        kamo "All the more reason to pick it up again now that we're back in Japan. I know your father's really looking forward to it. I really hope you're coming along as well."
        aki "Well... Okay then."

        show karla basic_cheerful_cas
        with chchange

        kamo "Great. See you in two hours then."

        show karla basic_wink_cas
        with charachangealways

        "Mom starts walking out of the room, but turns around once more before closing the door behind her."
        kamo "Oh, by the way... Take a look in the closet for a little surprise."

        play sound sfx_doorclose

        hide karla
        with charaexit

        "And with that, I'm left alone in a bedroom that has little more than a bed, a closet and a desk in it."
        "With nothing better to do, I walk up to the closet and take a curious look inside. The only thing in there is an admittedly impressive bright red kimono."
        aki "Geez, how do you put these things on again?"
        "Suddenly those two hours feel ridiculously short."

        stop music fadeout 2.0

        if _in_replay:
            return

    label .s2:

        $ set_window_tint(TINT_AKIRA)

        scene bg misc_hiroyukicar at sh_carbob
        with locationskip

        # TODO play car driving SFX

        queue music music_soothing fadein 4.0

        aki "Is that shrine far from here?"
        "Dad looks at me from the rearview mirror and shakes his head."
        hyd "A minute or ten at most. We will be there soon."
        "Lilly smiles."
        li "I still remember how we used to celebrate New Year by visiting the nearby shrine together with Grandfather and Grandmother and then go home to play games, eat rice cakes, and listen to Mother playing Beethoven's 9th Symphony on her cello."
        "Mom shrugs."
        kamo "I always thought it sounded bland without an orchestra to play along. You can't really play symphonies on your own and make it sound right."
        li "Still, it's a pleasant memory for me. I suppose I can't convince you to give us a little performance later today?"
        kamo "Sorry dear, but it's been a long time since I've played that piece, and I'd like at least a bit of practice before I'd feel confident about playing it again. Maybe next year."
        li "That's a shame. It is something that stands out in my New Year memories."
        "Mom nods and then suddenly snickers."
        li "Is something the matter, Mother?"
        kamo "Just digging through my own New Year memories, and I remember how we'd always go and buy those little sheets of paper that'd tell you your fortune for the upcoming year at the shrine. Those... eh... I think they were called o-mikuji. And you were always pretty anxious about that."
        "Lilly shifts a bit uncomfortably in her seat, but I let out a chuckle. I think I know what Mom's referring to."
        aki "Oh right. There was that one time when Lilly burst into tears in the middle of the shrine because she picked an o-mikuji that predicted bad fortune."
        li "Akira! That was the third year in a row I picked bad luck, and I was only seven at the time."
        aki "Heh, I did feel kind of sorry for you back then, you know."
        "Mom turns her head around and grins playfully at me."
        kamo "It's not like New Year was always kind to you. I remember when you were seven you convinced us to buy you a kite to fly on New Year. But after only a few minutes, you accidentally let go of the flying line, and the kite ended up stranded in one of the tallest trees in the neighborhood."
        kamo "You were so upset about that that you spent about an entire month throwing pebbles at it every day in an attempt to dislodge it."
        li "Oh my. I never knew. How horrible."
        "Lilly giggles and I hear way more amusement than sympathy in her voice. I roll my eyes and give her a poke in the ribs with my elbow."
        aki "You be quiet. That was my first kite ever, and I only ended up having a total of five minutes to enjoy it. It was a very traumatizing experience, so don't make light of it."
        li "Hahaha. Did you ever manage get it out of that tree?"
        aki "Not really. One day it was simply gone. There was probably a storm the night before that took off with it. Maybe it's for the better, or I'd still be chucking pebbles at it."
        kamo "The two of you will have to save the rest of the memories for tonight's dinner, girls. The parking lot belonging to the shrine is just down the road."

        scene bg shrine_entrance
        with locationchange

        $ renpy.music.set_audio_filter("sound", renpy.audio.filter.Lowpass(1200))

        play sound sfx_crowd_outdoors volume 0.2 fadein 2.0

        "As Dad parks the car near the stairs beyond the shrine gate, I let my eyes sweep across the parking lot. I see quite a few cars here, and there's a bus nearby whose passengers have just disembarked and are now making their way up the stairs."
        "We might end up having to wait in line for quite some time. Thank goodness it's not too cold right now."

        show hiroyuki thinking at tworight
        show karla basic_smileclosed_cas at right
        show lilly basic_smileclosed at twoleft
        show hanako basic_distant at left
        with charaenter

        "We get out, and I turn to Hanako, who's been silent for pretty much the entire trip."
        aki "Hey Hanako, would you mind helping Lilly up the stairs? Tripping up and tumbling down would be a really rotten way to start the new year."

        scene black
        with locationchange

        "Hanako gives me a nod, and we start walking up the stairs with me in the front, Mom and Dad just behind me and Lilly and Hanako bringing up the rear."
        "I can hear the bustling of the crowd of visitors ahead and the ringing of the bell before I make it to the top, but when I reach the shrine gate, I'm still overwhelmed by how many people are visiting here right now."

        $ _sh_mus_pos = renpy.music.get_pos("sound")
        stop sound fadeout 1.0
        play ambient f"<from {_sh_mus_pos}>{sfx_crowd_outdoors}" fadein 1.0
        $ renpy.music.set_audio_filter("sound", None)

        scene bg shrine_ext
        show crowd
        show hiroyuki thinking at tworight
        show karla basic_smileclosed_cas at right
        with charaenter

        aki "Geez, how did all these people get here? There weren't that many cars in the parking lot."
        "Mom, who followed close behind, gives me a silly grin."

        show karla basic_smug_cas
        with chchange

        kamo "Either those were clown cars down there or most of the people here used the public transport. You tend to forget how popular it is here when you live abroad for some time, don't you?"

        show karla basic_cheerful_cas
        with chchange

        aki "Yeah, kind of..."

        hide hiroyuki
        hide karla
        show lilly basic_smile at twoleft
        show hanako emb_downtimid at left
        with charaenter

        "My attention quickly shifts from Mom to Lilly and Hanako who have now also reached the top of the stairs and pause for a moment some distance away from us to catch their breath and take in their surroundings."
        "The contrast between their reactions couldn't be larger."

        stop music fadeout 4.0

        show lilly basic_cheerful
        show hanako emb_downsad
        with chchange

        "Lilly takes a deep breath and seems to enjoy the scent from the nearby trees and the murmur of the people nearby. Hanako, on the other hand, only seems to have eyes for one thing... the crowd standing between us and the hall of worship where shrine visitors can do their prayers."

        queue music music_rain fadein 4.0

        "The serenity on Lilly's face seems to make the terror and panic welling up in Hanako's eyes even more jarring."
        "Damnit!"

        nvl clear
        nvl show dissolve

        n "From what I've seen of her myself, the extent of Hanako's trouble with crowded places is hard to pin down. When she was visiting the indoor marketplace in Inverness, she seemed capable of traversing the place with a minimum of discomfort despite the fact that there were quite a few people there."
        n "{vspace=30}Of course, that was during a vacation that, from what I've heard, she enjoyed a lot and she was probably in a good mood. The last month hasn't been exactly good to her—quite the opposite, from what Lilly has told me. I'm not sure if anxieties work that way, but it wouldn't surprise me if the rut she's been in lately has made her more vulnerable to things that trigger her apprehensions."
        n "{vspace=30}The idea of having to stand in the middle of a mass of people for what would probably be over an hour has to be intimidating to her even on her good days."

        nvl hide dissolve

        show lilly basic_reminisce
        with chchange

        li "Hanako, are you alright?"

        "Perhaps Lilly has picked up a change in Hanako's breathing, since she turns towards her friend with a worried expression."
        ha "I'm... okay."

        show hanako emb_downsad_close at twoleft
        show lilly basic_reminisce_close at tworight
        with characlose

        "I walk up to the two of them, eager to clarify the situation."
        aki "It's pretty crowded here, Lils. Somewhere between 150 and 250 people who get to go before it's our turn. We'll probably be here for a little while."

        show lilly basic_concerned_close
        with chchange

        li "...Oh."
        "A pained expression appears on Lilly's face as she realizes the situation."
        li "Do you think we should... ah...?"
        "I turn to Hanako."
        aki "You say you're okay, but the look on your face says something else entirely, Hanako."
        ha "Please d-don't w-worry about me."

        show lilly basic_sad_close
        with chchange

        aki "I'm not worried. I just wonder if spending an hour with hundreds of people all around you is really your idea of a good time. Because from what I can see, to most people here it is."

        show hanako emb_downtimid_close
        with chchange

        ha "Uhh..."
        "Hanako fidgets nervously. I think responses like ‘I'm okay’ and ‘Don't worry about me’ are kind of reflexes for her whenever someone shows concern for her. She hates the idea of burdening others."
        "But I don't think that she's good enough at lying to tell me to my face that she trusts herself not to panic at some point if we were to join the crowd in front of us."
        ha "I'll... b-b-be okay. R-really."
        aki "Hanako, whenever people do things as a group, the amount of fun they're having is partially based on how much the rest is enjoying themselves."
        aki "If one person in the group is feeling miserable, then it takes some really willful obliviousness for the rest to have a good time. If you're gonna try and reassure me that you really are going to be perfectly fine, at least look me straight in the eyes while telling me that you'll be okay."

        show hanako emb_downsad_close
        with chchange

        "Hanako sighs loudly. She's obviously not convinced she can pull off what I just asked her to do."

        show lilly basic_reminisce_close
        with chchange

        ha "I could... m-maybe w-wait in the car?"
        aki "I dunno. Maybe we should simply call the whole thing off."

        show hanako emb_sad_close
        with chchange

        "Hanako's widen in panic."
        ha "B-But, it's a f-family t-tradition, isn't it? You and L-Lilly s-should..."

        show lilly basic_concerned_close
        with chchange

        "I don't think it was Hanako's intention, but she effectively shut the argument down. I'm not going to navigate this particular minefield until I know exactly how she feels about this matter and this isn't the right opportunity to pry."
        aki "I'll go and consult the folks. Let's hear what they have to say."

        hide lilly
        hide hanako
        with charaexit

        "As I walk up to Mom and Dad, I find myself wondering how they're gonna react to this whole thing. How aware are they about Hanako's various anxieties? Lilly doesn't usually talk about them, and I had to figure out most of Hanako's issues through personal interaction with her."

        show hiroyuki smileclosed_close at twoleft
        show karla basic_smile_cas_close at tworight
        with characlose

        aki "Hey, I've been thinking... How important is this to you two?"

        show hiroyuki eyebrow_close
        show karla basic_confused_cas_close
        with chchange

        "Mom and Dad give me a puzzled look."
        aki "Because this place is kind of busy, and it may be better to visit another shrine or maybe come back later when the crowd has thinned out a bit."

        show hiroyuki speak_close
        with chchange

        hyd "It is true that there are many people here, but it does not seem to be busier than it usually is on New Year's Day. I do not think you will find a shrine that does not have a lot of visitors right now, and I suspect that things will remain that way until closing time."
        aki "Then maybe we should leave and come back tomorrow or something."

        show hiroyuki eyebrow_close
        with chchange

        "Dad shoots me an incredulous look."
        hyd "Visiting a shrine on New Year's Day has been a family tradition for a very long time."
        aki "Except during the last six years."

        show hiroyuki stern_close
        show karla cross_displeased_cas_close
        with chchange

        "This earns me a scolding glare from Dad. Mom gives me a quizzical stare."
        kamo "Why? Why now? You were okay with this before."
        "I had other things on my mind earlier, so I completely forgot about the possibility of this happening. I would graciously accept blame for that."
        aki "Hanako..."

        show hiroyuki awkward_close
        show karla basic_distant_cas_close
        with chchange

        "Mom and Dad throw a quick glance in Hanako's and Lilly's direction. It's hard to make out Hanako's expression from this distance, but her slumped posture is easy enough to see, even from here."
        "They exchange a glance, and I can see realisation dawning on them. Mom gives me an unsure look."
        kamo "Hanako and that crowd...?"
        aki "...yeah."
        kamo "She wants to leave here?"
        aki "Part of her wants to get away from here as soon as possible, I can tell that much just by looking at her. But she also hates feeling like she's a burden on others, so she's not going to ask us to cater to her."
        aki "She offered to wait in the car, but I'm not sure if that's a good idea. She'd have nothing to do for over an hour except sit there and feel bad about herself."

        show karla basic_troubled_cas_close
        with chchange

        kamo "What do you think, dear?"

        show hiroyuki thinking_close
        with chchange

        pause 0.8

        show hiroyuki awkward_close
        with chchange

        "Dad looks pensive for a second and then lets out a disappointed sigh. He reaches into his pocket and hands me his car keys."

        show karla basic_sad_cas_close
        with chchange

        hyd "Go ahead and take her back to the house. Then come back here afterwards to pick us up."
        aki "Sure."

        show hiroyuki serious at tworight:
            xpos 0.63
        show karla basic_troubled_cas at right
        with charadistant

        show lilly basic_sad at twoleft
        show hanako emb_downtimid at left
        with charaenter

        "We make our way back to Lilly and Hanako."
        aki "Hey Hanako... uh... Dad's given me the car keys and I'm going to go back to their place. Shall we go?"

        show hanako emb_downsad
        with chchange

        "She doesn't immediately respond and merely shuffles her feet for a moment while doing her best to avoid our gaze. There's a very guilty look in her eyes."
        "Suddenly, Lilly speaks up."

        show lilly basic_reminisce
        with chchange

        li "Father... would it be okay with you if I... went along as well?"

        show hiroyuki awkward
        show karla basic_distant_cas
        with chchange

        hyd "...go ahead then. Your mother and I will offer a few additional prayers for your good fortune in your place."

        show lilly basic_weaksmile
        with chchange

        li "Thank you, Father."

        stop ambient fadeout 2.0
        stop music fadeout 4.0

        scene black
        with locationchange

        "Without much ado, we pass back down the stairs, through the gates and to the parking lot. This time, though, it almost feels like Lilly is helping Hanako navigate. We get in the car, and I drive back to our parents' home without anyone really saying anything."

        scene bg satoujp_livingroom
        show lilly basic_sad at twoleft
        show hanako emb_downsad at center
        with charaenter

        show hanako emb_downsad at right
        with charamove

        "When we enter the living room, Hanako slumps down on the couch and holds her head in her hands."
        ha "L-Lilly... Ak-Akira... I'm s-so sorry."

        play music music_comfort fadein 4.0

        show lilly basic_weaksmile
        with chchange

        aki "Don't apologize, Hanako. It's really not that much of a big deal. Let's just relax a little bit before you two get back to your books. I can afford to hang out here a little bit before I have to pick up the folks."
        ha "B-but..."
        aki "You know... back in the day, we used to play games on New Year's Day after a shrine visit. Card games, backgammon, Lucky Laugh. Of course, Lilly would always win the latter."
        aki "It's as much of a family tradition as the shrine visit was, and this one actually makes sense in my opinion. I don't see any reason for us not to honor this tradition right now."

        show lilly basic_smile
        with chchange

        "Lilly smiles."
        li "Hanako, don't you have a deck of playing cards in your backpack? Why don't you go and get it? The two of us against Akira."
        "I grin."

        show lilly basic_cheerful
        with chchange

        aki "Bring it on."

        show hanako emb_timid
        with chchange

        pause 0.8

        show hanako emb_timid at offscreenright
        with charamove

        "Hanako looks a little doubtful, but then nods and walks out of the room."
        "I wait until I think she's out of earshot and then turn to Lilly."

        show lilly basic_reminisce
        with chchange

        aki "I hope I wasn't being too overbearing with her back there. I kinda went with my gut instinct here."
        aki "Given the number of people there, we would have been in the middle of that crowd for a long time and... If she had a panic attack ten or twenty minutes in, it would have been very difficult to quickly get her out of there, and we might have had a public spectacle right there with us at the center."
        aki "Who knows how Dad would have reacted to that. Ever since that screw-up at Kasshoku University, Hanako's probably more paranoid around crowds than ever before. Maybe we should be too."

        show lilly basic_sad
        with chchange

        "Lilly nods her head."
        li "I... think you did the right thing. I just feel bad about disappointing Father."
        aki "Don't be too hard on yourself, Lils. Set the good example for Hanako."

        show lilly basic_weaksmile
        with chchange

        li "I'll try."

        scene black
        with locationchange

        "We wait until Hanako returns with her deck of cards and then start playing, with Lilly and Hanako occasionally whispering to one another on which card to play."
        "As the game goes on, I can see Hanako slowly starting to relax."

        scene bg satoujp_livingroom
        show lilly basic_smileclosed_close at twoleft
        show hanako basic_bashful_clip_close at tworight
        with locationchange

        li "Akira?"
        aki "What is it, Lils?"
        li "Why do you feel a family visit to the nearby shrine doesn't make sense? I'm not sure why you feel that way."
        aki "I didn't say it doesn't make any sense at all, Lils. It makes some sense, just not that much."

        show lilly basic_weaksmile_close
        with chchange

        li "I still don't really understand why you would say that."
        aki "Those shrine visits were a family tradition because the three people in charge of the family, that being Dad, Granddad and Grandma, are Shintoists. With Granddad and Grandma not being here right now, we might very well have more Catholics than Shintoists in the home right now."

        show lilly basic_surprised_close
        with chchange

        "Lilly raises an eyebrow."
        li "Do you still count yourself among those Catholics, Akira?"
        aki "Naw, I haven't been much of anything for years."

        show hanako basic_worry_clip_close
        with chchange

        "Hanako gives me a midly curious look."
        ha "You were... um... Catholic, Akira?"
        aki "Used to be. Mom's a Catholic, though it mostly translated into her giving us a pretty cross-shaped necklace to wear and sometimes telling us bedtime stories with a moral."
        aki "Like a shepherd who left his herd in order to look for one lost sheep or a traveller who was severely injured by bandits and saved by a member of an enemy tribe who had him nursed back to health out of compassion."

        show lilly basic_cheerful_close
        show hanako basic_bashful_clip_close
        with chchange

        li "That last one was always one of my favorites."
        aki "Mom's religion was always pretty low-key, but then I was thrown into middle school and some of those teachers started throwing the S-word around."

        show lilly basic_displeased_close
        show hanako basic_distant_clip_close
        with chchange

        ha "Uh... S-word?"
        aki "{i}Sinful{/i}. Nothing's more off-putting than people telling others they're lower human beings for the slightest infraction."
        li "Some of them were a bit heavy-handed, I'll admit."

        show lilly basic_weaksmile_close
        show hanako basic_bashful_clip_close
        with chchange

        aki "Anyway, I often wondered if a Catholic saying a prayer at a Shinto shrine isn't a sacrilege of some sort."

        show lilly basic_giggle_close
        with chchange

        "Lilly chuckles softly."
        li "I've always told myself that praying for the happiness and good fortune of one's loved ones is never sacrilegious, no matter the circumstances or the location. I'm pretty sure that Mother feels the same."
        "This discussion has made me curious about something. Having just finished a game, I wait until Hanako's finished shuffling and dealing the cards and then give her an inquisitive look."
        aki "How about you, Hanako? Are you a Shintoist yourself?"

        show lilly basic_smile_close
        show hanako basic_distant_clip_close
        with chchange

        "Hanako looks a little awkward, but nevertheless gives it some thought."
        ha "M-my parents were. We always went t-to our local shrine on N-New Year's D-Day too. B-but ever s-since... the accident, I haven't b-been to one."

        show hanako emb_sad_cas_nohat_clip_close
        show lilly basic_reminisce_close
        with chchange

        ha "I d-didn't want to anymore, even though t-the orphanage staff usually visited the n-nearby shrine with t-the other children that day. I'm n-not really sure whether I'd even b-be welcome there anymore."
        "So the situation we just dealt with isn't even something new to Hanako. She's been faced with this kind of thing since she lost her parents."
        aki "Oh..."

        show hanako emb_emb_clip_close
        show lilly basic_displeased_close
        with chchange

        ha "It w-wasn't all bad though. We would usually eat some delicious rice cakes when the other c-children came back, and the staff would play games with us. That was... fun."
        aki "You really like games, huh?"

        show hanako emb_downsmile_clip_close
        show lilly basic_smileclosed_close
        with chchange

        "She smiles gently and nods her head. I give her an encouraging smile back."
        aki "Well, then let's play for two more rounds, and then I'll go back to the shrine, and you two can go back to your books."

        stop music fadeout 2.0

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return


    label .s3:

        $ set_window_tint(TINT_AKIRA)

        scene bg satoujp_stairs
        show lilly basic_weaksmile_close at left
        with Dissolve(2.0)

        play music music_lilly fadein 4.0

        aki "Aaaah..."
        "I stretch my arms as Lilly and I walk out of the bathroom after having taken a nice long soak. Lilly chuckles."

        show lilly basic_smileclosed_close
        with chchange

        li "That felt refreshing, didn't it?"
        aki "Yeah, definitely a change from that cramped tub at my place. Though cramped has its benefits in certain situations too."

        show lilly basic_pout_close
        with chchange

        "Lilly blushes a bit."
        li "Akira. That's kind of..."
        "Before we can continue on the subject, one of the guest room doors opens, and Hanako comes out and walks up to us."

        show hanako basic_bashful_close at right
        with charaenter

        show lilly basic_smile_close
        with chchange

        ha "H-hey. Was it... relaxing?"
        aki "Yeah, it was pretty good. You can go ahead and get in yourself now. The water should be the right temperature for you."

        show hanako basic_smile_close
        with chchange

        ha "T-thanks."
        "I give Hanako a friendly smile."
        aki "You know, you could have taken one together with us, and I would have been more than willing to keep my eyes closed all the time. Soaking on your own is kind of lonely in such a large bath. Or Lilly could have accompanied you instead of me."

        show lilly basic_smileclosed_close
        show hanako emb_smile_close
        with chchange

        "Hanako smiles uneasily and then shakes her head."
        ha "It's... okay. I... already t-took a bath with L-Lilly yesterday. It... m-must have been some time ago when y-you and Lilly last bathed."
        aki "Well, that is kind of true. The home we used to live in had a large bath too, so she and I used to take soaks together all the time. That kind of changed when I started working though. The last time we bathed together must have been..."
        "I rack my brain a bit, but can't come up with an exact answer. I give Hanako a goofy grin."
        aki "...about the time Lilly's chest started getting larger than mine."

        show lilly basic_pout_close
        show hanako emb_blushtimid_close
        with chchange

        li "Oh my..."
        "Lilly is visibly flustered by my joke, but then a playful smile appears on her face."

        show lilly basic_giggle_close
        with chchange

        li "...has it really been that long?"

        show hanako emb_downsmile_close
        with chchange

        "Son of a- OUCH!"
        "Hanako immediately turns her head away, obviously trying to hide her grin. I snicker a bit at Lilly's comeback, but am still determined not to let that little jab go unpunished. I give Lilly a playful poke in the side while at the same time winking at Hanako."
        aki "You know, you'd better not diss my chest. After all, at least I have someone to admire mine. As does Hanako. As does Mom. You're currently the only person in this house who's headed for spinsterhood unless you learn how to accept date requests from people who aren't Hanako."

        show lilly basic_concerned_close
        show hanako emb_smile_close
        with chchange

        li "I b-beg you pardon?"
        "The expression on Lilly's face is so comical that Hanako lets out an amused giggle before she can stop herself. Upon hearing this, Lilly smiles awkwardly."

        show lilly basic_weaksmile_close
        with chchange

        li "I have the impression I'm being made fun of."
        aki "It's a joke, Lils. I hope you're not angry."

        show lilly basic_smile_close
        show hanako basic_smile_close
        with chchange

        li "Don't worry about it."

        show hanako emb_downsmile_close
        with charachangealways
        
        show hanako at offscreenleft
        with charamove

        hide hanako

        "Hanako, probably having determined that the little spectacle before her has come to a conclusion, gently pushes her way past us and gives me a little nod before closing the bathroom door behind us."

        play sound sfx_doorclose

        "After hearing the door's lock snap into place, I turn to Lilly."
        aki "Hope I wasn't out of line just now."

        show lilly basic_cheerful_close
        with chchange

        li "I could very well ask you the same."
        aki "Naw, you can make fun of me as much as you like. Especially if..."

        show lilly basic_smileclosed_close
        with chchange

        li "Especially if?"

        show lilly basic_displeased_close
        with chchange

        aki "Especially if it cheers up Hanako. She looked a little down during our ride to the shrine and during dinner..."
        "Not just down, but also a little lonely if I remember correctly."
        aki "...and she seemed downright depressed while we were driving back, but she was smiling again just now when she entered the bathroom."

        show lilly basic_weaksmile_close
        with chchange

        li "That's a relief to hear."
        aki "You'd better get back to your books for a little while. If you feel up to it, that is."

        show lilly basic_cheerful_close
        with chchange

        li "Hmmm... Have you finally joined the choir, Akira?"
        aki "Heh, you're probably getting tired of all the prodding, but if you want to pursue your dream, you'll have no choice but to do well on the National Center Test the upcoming month. They don't employ English teachers at Satou Medical Technology, so you can't take shortcuts like I did."

        show lilly basic_smileclosed_close
        with chchange

        li "I'll do my best. And Akira?"
        aki "Yeah?"

        show lilly basic_giggle_close
        with chchange

        "A teasing smile appears on her face once more."
        li "For many people being single is only a temporary problem, you know?"

        show lilly basic_cheerful_close
        with chchange

        aki "Meow, Lils."

        scene bg satoujp_guest
        with locationchange

        "Still chuckling, we each go back to our respective rooms. I lie down on the bed, take a manga issue out of my bag and start reading."

        play sound sfx_doorknock2

        "I make it to page 20 before I hear knocking on the door. Too irregular to be Lilly's and too loud to be Hanako's. Not pronounced enough to be Dad's."
        aki "Yes?"

        play sound sfx_dooropen

        show karla basic_troubled_cas
        with charaenter

        "The door opens and, as expected, Mom walks into the room. I give her a look as if to ask what she wants, but she merely stares at me for a moment."
        aki "Uh... Is anything wrong?"

        show karla basic_confused_cas
        with chchange

        kamo "Hey. Did you and Lilly have a pleasant soak?"
        aki "It was alright."
        kamo "No longer feeling tired?"
        aki "Not really, it was pretty refreshing."

        show karla basic_sheepish_cas
        with chchange

        kamo "If that's the case then, would you like to join your father and me downstairs?"
        "Ugh. I was already wondering where this conversation was headed. Now I kind of feel like she set me up."
        aki "I'd... uh... rather stay here if that's okay."

        show karla basic_speak_cas
        with chchange

        kamo "There's not exactly a lot to do here."
        aki "Until I finish this manga, that's probably not going to be a problem."

        show karla cross_displeased_cas
        with chchange

        kamo "That's gotta be one hell of a manga."
        "I manage to resist the temptation to ask her what on earth she meant by that and simply get back to reading."

        stop music fadeout 5.0

        show karla cross_displeased_cas_close
        with chchange

        "But contrary to my expectation, Mom doesn't walk out of the room. Instead, she sits down on the chair near the desk and just keeps looking at me without saying anything."
        "I raise the manga closer to my face in an attempt to block her out, but somehow her gaze manages to unnerve me enough to make further reading impossible."
        "I sigh loudly and put my manga back in my bag before returning the stare that's aimed at me."
        aki "Okay, what's the problem?"

        play music music_moonlight fadein 4.0

        "Mom doesn't immediately answer and merely twirls one of her bangs around her finger."
        kamo "What do you think the problem is?"
        "I'm not in the mood for charades like these."
        aki "Mom, if you have something on your mind, I'd rather get it over with now."

        show karla cross_ponder_cas_close
        with chchange

        "She lets out a tired sigh."
        kamo "When I heard that you were coming over today, I was hoping we'd get the opportunity to... you know... maybe not reconcile, but make a start to mend our differences. I didn't think there'd be a more appropriate day for making a new start than New Year's Day."
        aki "Oh..."

        show karla basic_troubled_cas_close
        with chchange

        kamo "But that's probably not going to happen, is it?"
        aki "Sorry I couldn't meet your expectations."

        show karla basic_troubled_cas_close
        with chchange

        show karla basic_worried_cas_close
        with chchange

        kamo "Couldn't or wouldn't? It's been kind of weird to see you today, you know? Whenever Lilly and Hanako are nearby, you're like all smiles and sunshine. But the moment they're out of earshot, the temperature suddenly drops like 30 degrees."
        aki "What did you want me to do? Put on a fake smile and pretend nothing's wrong?"

        show karla basic_serious_cas_close
        with chchange

        kamo "For the love of God, no. I know a lot has happened between us, and it'll probably take a long time to move past that, but... It felt like you weren't even trying today."
        kamo "Whenever we talk to you, you answer in single syllables. You took literally every single opportunity you could get to avoid us or get away from us."
        aki "At least I haven't started any arguments."

        show karla basic_sad_cas_close
        with chchange

        kamo "Akira, why exactly did you come here today? You've declined Lilly's invitations before, so why not now? You could have spent time with Lilly before or after her stay here."
        kamo "If today wasn't a gesture of reconciliation and you dislike our presence this much, why come here at all? Why let us mar your day?"
        "I never came here to reconcile. If that's what she expected then it's no wonder she's disappointed."
        aki "It's complicated."
        "My gaze briefly wanders towards one of the walls. Mom follows my gaze and then nods."

        show karla basic_distant_cas_close
        with chchange

        kamo "Hanako?"
        "She picked that one up quickly, I have to admit that much."

        aki "I wanted to keep an eye out. Just in case. Make certain she'd be alright. That's why I came."

        show karla cross_displeased_cas_close
        with chchange

        "Mom lets out a bitter chuckle."
        kamo "You came here to protect her against us? I'm not sure whether to be laugh or cry about that. A few weeks ago, you still gave us your blessing. We wouldn't have gone ahead without that. Why the sudden change of heart?"
        aki "No change of heart. Dad asked a very specific question, and I gave a very specific answer. He asked if I objected to having Hanako as my little sister. I said I didn't, and that hasn't changed. She's a sweet kid, and I really do feel a certain bond with her."

        show karla basic_confused_cas_close
        with chchange

        kamo "I agree. And she doesn't seem to have a lot of people in her life right now. Don't you think she deserves a family?"
        aki "I think she deserves a family, alright. I'm just not so sure whether she deserves this one."
        kamo "Any specific objections?"

        aki "Come on, Mom. Don't play dumb. What if Hanako had been a few years younger and you would have had to go through the orphanage staff to make the arrangement? Do you think they would have gone along with it if they knew about your track record?"

        show karla basic_distant_cas_close
        with chchange

        kamo "They just might have. There's one heck of a lot of adoptions taking place each year in this country, but only a miniscule part of those adoptions actually involve children who are in need of a home. Adoptive parents aren't all that common. Nearly all adoptees are succesful adult men."
        aki "So you'd be counting on their desperation? That sure is a big reassurance."

        show karla cross_pissed_cas_close
        with chchange

        kamo "Your cynicism is noted."
        aki "My cynicism, huh? I wonder..."

        show karla basic_serious_cas_close
        with chchange

        kamo "Yes?"
        aki "She hasn't given you an answer yet, has she? Not when you first asked her, not during the week that came after and not today, even though New Year's Day would have been a perfect occasion to make a ‘new start’ as you put it."

        show karla basic_sad_cas_close
        with chchange

        kamo "No. Not yet. But we told her she could take her time. And she really should be focusing on the National Center Test and her entrance exams. Get those out of the way first."
        "I study the expression on Mom's face carefully, and I detect the same slight sense of anxiety that I noticed on Lilly's face when I briefly asked her about this subject during our shared soaking session."
        "It's pretty obvious that both had been expecting Hanako to have jumped at the offer when it was made to her."
        aki "I wonder if you guys also thought of an exit strategy in case Hanako isn't interested."

        show karla basic_confused_cas_close
        with chchange

        kamo "We told her that the decision is hers to make. If she declines, she'll still always be welcome here as an honored guest."
        aki "Surely you don't believe that it's that simple. Hanako probably feels that declining would be an insult. Even if she declined, she'd still be roommates with Lilly."
        aki "She'd still be living in an apartment that you two are paying for and that you might be visiting every now and then too. Do you realize just how awkward that would be for her?"

        show karla cross_displeased_cas_close
        with chchange

        stop music fadeout 2.0

        kamo "You almost make it sound like you're secretly hoping for this whole thing to fall apart."

        queue music music_sadness fadein 4.0

        aki "That's not it. I'm simply hoping for whatever outcome is best for Hanako. That girl's been hurt a lot in the past and is still lugging around one hell of a lot of baggage. The last thing she deserves is to be let down again."
        aki "You couldn't be bothered to take responsibility for your own child six years ago and now you think you have what it takes to take responsibility for someone else's."
        aki "Can you even imagine what that's like?"
        aki "Don't answer that! I know you can't! But I can, thanks to you!"
        "I promised myself not to make a fuss today. I'd just go here, hang out with Lilly and Hanako and bottle up whatever anger I feel towards Mom and Dad. As long as I made sure not to interact with them too much, things'd be fine."
        "But now it looks like I'm about to break my promise. Something about Mom managed to touch a nerve, and now I feel my old wounds are bursting open."

        show karla basic_plead_cas_close
        with chchange

        kamo "Akira, calm down. I'm not justifying what has happened in the past."
        aki "No, now you're downplaying it instead!"
        kamo "I wasn't downplaying anything."
        aki "You come in here and act offended, because I haven't forgotten about you having abandoned Lilly. You're like: ‘What's the problem, we're here now, aren't we? Just shut up and forgive us already.’ Like it was never a big deal!"
        kamo "I'm not..."
        aki "Yes, you are! You're lecturing me about how New Year's Day is such a perfect date for a new start."
        aki "Do you know what would have been an even better date for a new start? Well? The previous six friggin' New Year's Days! That's all Lilly wanted for New Year, you know. For you to come back to her!"

        show karla basic_sad_cas_close
        with chchange

        kamo "I..."
        aki "Just because Lilly isn't going to call you out, doesn't give you the right to scold me for rightfully holding you responsible. Even though you don't want to be reminded that you left your youngest daughter in the care of a girl barely out of high school, that's still exactly what happened."
        aki "Either that or you were planning to rely on a mother-in-law suffering from ulcers, shortness of breath, and high blood pressure to clean up after you... like you've been doing for years anyway."

        show karla basic_displeased_cas_close
        with chchange

        kamo "Akira..."

        show karla basic_pissed_cas
        with charadistant

        "Mom gets up from the chair and takes a few steps towards the door, but before I can reach into my bag to retrieve my manga, she stops, turns towards me, and shoots me a vicious glare."
        kamo "It's nice to see that you're so committed to Lilly's well-being that you're attacking us on her behalf. You've probably convinced yourself that she's secretly thankful for it, too."

        show karla basic_sad_cas
        with chchange

        kamo "What I remember Lilly telling me is that it's her dream to get our family back together again. And she's been trying really hard."

        show karla basic_confused_cas
        with chchange

        kamo "I don't think it'll be easy to move past the last few years, but I still believe it's possible and that we can come out of this closer than we were before, if we give it an honest try."

        show karla basic_speak_cas
        with chchange

        kamo "But you don't really believe that, do you? Neither do you want it. You've already given up on our family, and you're more comfortable with the way things are now!"

        show karla basic_pissed_cas
        with chchange

        kamo "You wouldn't mind if things remain this way forever, but you're afraid of admitting this to Lilly, so you're playing along on days like this while blaming any lack of progress on us."

        show karla cross_angry_cas
        with chchange

        kamo "Shout at us as much as you like if that makes you feel better, but at least stop pretending to have her best interests at heart! Because you don't!"
        aki "Oh, shut up Mom!"
        "I'm shaking with anger at her words, and it takes all my strength to fight off the urge to punch her. I probably would have thrown my book at her if it had been in my hand right now."
        li "Mother... Akira..."

        show lilly cane_cry at twoleft
        show karla basic_sad_cas at tworight
        with charaenter

        "We've both been so occupied with our hostile stand-off that neither of us noticed that the bedroom door softly opened, revealing a very upset-looking Lilly standing in the doorway."
        li "Please... Stop fighting..."
        "The hurt expression on Lilly's face is enough to make me forget about the anger I just felt and replace it with a weary resignation."
        "When I look at Mom, I notice the combatitive look in her eyes has vanished as suddenly as it appeared and has given way to a tired expression."

        show karla at center
        with charachangealways

        "She sighs as she briefly puts her hand on Lilly's shoulder."
        kamo "I'm sorry, dear."
        aki "Sorry, Lils. I'll keep my mouth shut from now on."

        hide lilly
        with charaexit

        "Without responding any further, Lilly turns around and walks out of the room."
        "Crap. I really messed up this time. I wonder how much of that argument she overheard. Probably all of it."

        stop music fadeout 5.0

        show karla basic_troubled_cas
        with chchange

        "Mom turns to me and lets out another weary sigh."
        kamo "I... may have been out of line just now."
        aki "I could really use a beer right about now."

        show karla basic_plead_cas
        with chchange

        kamo "Yeah, me too. Want to go and grab one?"
        aki "...why not?"

        scene black
        with locationchange

        "I follow Mom to the kitchen where she opens the fridge and takes two cans of beer out of it."

        scene bg satoujp_kitchen_ni
        show karla basic_distant_cas_close
        with locationchange

        play music music_night fadein 4.0

        play sound sfx_can

        "I take one of them from Mom, and we open our cans with a loud snap. Neither of us looks at the other or says a word as we drink. I doubt there's much to say to begin with."
        "When I finish my beer and prepare to throw the can away, I suddenly notice a small box on a sidetable that wasn't there when I got a tour of the kitchen."

        aki "What's in there?"

        show karla basic_confused_cas_close
        with chchange

        kamo "Oh, we picked that up today. We got it for Lilly, Hanako and you. We were planning to give it to the three of you later this evening. Now that I think about it, now would be a good time to do so. I doubt Lilly's currently in the mood to do any more studying. Would you mind getting the girls?"
        aki "Well, okay."

        scene black
        with Dissolve(2.0)

        "I go upstairs and visit Lilly and Hanako in their rooms, telling them that Mom and Dad have something they wanted to give to them."

        scene bg satoujp_livingroom
        show hiroyuki thinking at tworight
        show karla basic_sheepish_cas at right

        show lilly basic_displeased at twoleft
        show hanako basic_normal at left
        with charaenter

        "When we get back to the living room, Mom and Dad are already waiting for us with the box I noticed earlier on the table in the middle. The three of us sit down on one of the couches, and Dad scrapes his throat."

        show hiroyuki serious
        with chchange

        hyd "Ahem, I trust the two of you are satisfied with the amount of studying you have managed to get in for today?"

        show hanako basic_worry
        with chchange

        li "I have, Father."
        ha "I... umm... t-think so."

        show lilly basic_smileclosed
        show hanako basic_normal
        show hiroyuki speak
        with chchange

        hyd "Very good. Since the three of you were absent during our visit to the shrine's hall of worship, we made certain to bring you some of these. With the exams so close, we felt it could not hurt."

        show hiroyuki serious
        show karla basic_sheepishclosed_cas
        with chchange

        "He takes the box off the table and opens it. It's filled to the brim with o-mikuji. Mom smiles."

        show lilly basic_smile
        with chchange

        kamo "Hopefully a little good fortune for the exams you're facing this month."
        "I scratch my head."
        aki "You sure bought a lot of those o-mikuji."

        show karla basic_smile_cas
        with chchange

        kamo "The three of you can take one each. I'm going to take the rest of them to my colleagues in Inverness on my next trip there. They love this kind of stuff."

        show hiroyuki thinkraised
        show karla basic_smileclosed_cas
        with chchange

        "Dad makes an inviting gesture towards the box."
        hyd "Go ahead and take one."

        show lilly basic_satisfied
        show hanako basic_distant
        show hiroyuki smile
        show karla basic_smile_cas
        with chchange

        "Lilly, Hanako and I each pick a piece of paper from the box and unfold it. With more than a little hint of excitement, Lilly shows me her piece."
        li "Can you tell me what mine says, Akira?"
        aki "You got 'Good Luck', Lils. I hope that translates into good results later this month."

        show karla basic_sheepish_cas
        show lilly basic_giggle
        with chchange

        li "I really hope so too. What did you get, Akira?"
        with chchange

        aki "I got a 'Bad Luck' one. No biggie."

        show karla basic_sheepishclosed_cas
        show lilly basic_concerned
        with chchange

        li "Oh..."
        "I roll my eyes at Lilly's slightly worried expression."
        aki "You know, I don't really believe in this stuff, so it doesn't faze me."

        show karla basic_smile_cas
        show lilly basic_reminisce
        with chchange

        li "Even so..."

        "My eyes shift from Lilly to Hanako who has just unfolded her piece, but doesn't really react to it."
        aki "What did you get, Hanako?"

        show hanako basic_normal
        with chchange

        "Without saying anything, she gives me her piece of paper."

        show lilly basic_smile
        with chchange

        aki "It says 'Great Luck'. Looks like we have a winner here."

        show hiroyuki thinking
        show karla basic_confident_cas
        show lilly basic_cheerful
        with chchange

        "Mom makes a quick 'not so fast'-gesture with her finger."
        kamo "You know what you have to do to draw out its full potential, don't you?"

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return

    label .s4:

        $ set_window_tint(TINT_AKIRA)

        scene bg shrine_ext_ni
        play music music_dreamy fadein 4.0
        show lilly basic_weaksmile at twoleft
        show hanako basic_normal at tworight
        with charaenter

        aki "You know, I think we may have already used up all our good luck when we made our way up these stairs in the dark without breaking our necks."
        li "I think you may be exaggerating a bit."

        nvl clear
        nvl show dissolve

        n "It was still trickier than I thought though. After we each picked an o-mikuji, Mom suggested I drive back to the shrine together with Lilly and Hanako and tie our pieces of paper to the pine tree on the shrine grounds."
        n "{vspace=30}As custom would have it, bad fortunes can be avoided that way while good fortunes are strengthened."
        n "{vspace=30}Seems a bit silly, but I was kind of aching for some fresh air anyway, and there were some things I wanted to say to Lilly without Mom and Dad being anywhere nearby, so I gave in and drove back with the girls in tow. We very carefully climbed up the stairs to the gate, and now we're standing on the road leading to the various buildings."
        n "{vspace=30}The shrine's been closed for hours, but fortunately there's no need for us to enter any of the buildings. The tree that visitors tie their o-mikuji to has to be somewhere nearby. It's probably near the hall of worship, so that's where we're headed right now."

        nvl clear
        nvl hide dissolve

        show lilly basic_smileclosed
        show hanako basic_bashful
        with chchange

        aki "It might not be easy to find that tree with the shrine grounds being this dark, but a tree containing hundreds of pieces of paper must produce a pretty distinct rustling sound, so keep your ears open."
        li "Hmmm... I think you're right. Are we near the right building already?"
        aki "We're pretty close. Do you hear anything?"

        show lilly basic_smile
        show hanako basic_smile
        with chchange

        li "Somewhere... to our left."

        scene bg shrine_ema_ni
        show lilly basic_smile_close at twoleft
        show hanako basic_distant_close at tworight
        with charaenter

        "I peer through the darkness in the direction Lilly pointed out and vaguely see some light shapes moving in the wind."
        aki "Yup, we've found the spot. I'll hold out a branch and you can do the tying, okay?"

        show lilly basic_satisfied_close
        with chchange

        li "Alright."
        "I approach the tree, grab one of the branches and hold it in front of my sister who starts meticulously tying the pieces of paper to one of its unoccupied parts."
        aki "I'm almost done. Can I have your piece as well, Hanako?"
        "No immediate response. Hanako's merely standing there looking at her o-mikuji as if the thing's calling her names."

        show lilly basic_surprised_close
        with chchange

        aki "Hanako?"

        show lilly basic_listen_close
        show hanako basic_worry_close
        with chchange

        "I hear a tired sigh coming from her and then the piece of paper is pressed into Lilly's hand, who wastes no time attaching it next to our pieces."
        aki "Hey Hanako, is everything alright?"
        ha "Y-Yes. It's just..."
        aki "Hmmm?"

        show lilly basic_displeased_close
        show hanako emb_sad_close
        with chchange

        ha "I... d-don't really believe in t-this either."

        "Earlier today, she told us that she and her parents used to visit a place like this during New Year's Day. I wonder what her last o-mikuji said back then, assuming she picked one. Maybe she picked a 'Great Luck' fortune back then too, only to be orphaned and disfigured later that year."
        "That would turn you off to the practice pretty quickly. On the other hand, maybe the fact that she survived at all is great luck in a really twisted way. I wonder..."

        "Voice" "Good evening. Are you here to... sight-see? I'm afraid we're... only open between 9 and 4."

        show lilly basic_surprised
        show hanako defarms_shock
        with chchange

        "Hanako lets out a cry of surprise when we suddenly hear an unknown voice behind us speaking to us in rather awkward English. We turn around and see a girl who's probably not much older than 16 standing in front of us."

        aki "Uh, hey. Good evening. Sorry for intruding."
        "Shrine maiden" "Oh... ah... excuse me."

        show lilly basic_smileclosed
        show hanako cover_worry
        with chchange

        "She seems a bit surprised when I answer her in Japanese. Due to our blond hair and the weird time of our visit, she must have mistaken us for tourists."
        aki "We weren't really here to see the sights. We just finished hanging up our o-mikuji."
        "Shrine maiden" "Ah... Okay."

        show lilly basic_smile
        with chchange

        "Lilly, sensing the awkwardness in the girl's voice, steps forward and smiles in her general direction."
        li "I realize that we're visiting at a really awkward time, but we've spent most of the day studying at our house, and we need all the good luck we can get for the weeks that lie ahead."
        "A look of realization appears on the girl's face almost immediately."
        "Shrine maiden" "The Center Test?"

        show lilly basic_weaksmile
        show hanako cover_bashful
        with chchange

        li "Indeed."

        "Shrine maiden" "Good luck. I hope you'll do well."
        "We exchange bows and prepare to leave the premise when the girl suddenly calls out to us."

        show lilly basic_surprised
        show hanako cover_worry
        with chchange

        "Shrine maiden" "Excuse me."
        aki "Yes?"
        "Shrine maiden" "Would you... ah... like to use the hall of worship?"
        aki "The hall of worship? But the shrine is closed, isn't it?"
        "Shrine maiden" "The doors aren't locked right now because I just finished cleaning it. If you like, you can make a wish there while I finish my remaining chores at the administrative building."

        show lilly basic_smile
        show hanako cover_smile
        with chchange

        "Lilly gives me an encouraging look."
        aki "Well, okay then. Thanks. We greatly appreciate it."
        "Shrine Maiden" "You're welcome. I have an older sister who worked here as a shrine maiden during the last few New Year's Days, but now she's busy studying as well, which is why I've taken her place this year."

        scene bg shrine_int_ni
        show lilly basic_smileclosed_close at twoleft
        show hanako basic_smile_close at tworight
        with charaenter

        "After thanking the shrine maiden again, we wash our hands at the nearby purification basin and then enter the shrine building."
        "It's still pleasantly warm inside the building, especially compared to the rather chilly night air, and the presence of several lit lanterns in the room gives it a cozy atmosphere. Looking at the row of low seats in the center of the room gives me a sudden urge to take a load off."
        aki "It's kind of cozy in here. Seeing that that shrine maiden sounded like she might still be busy in the other building for a little while, we might be able to take it easy for a few moments without running the risk of wearing out our welcome."

        scene ev shrinesisters_sit
        show lilly basic_smile at left
        show hanako basic_bashful at center
        show akira basic_sweet at right

        "The girls think about it for a moment and then give an almost simultanous nod. We put three of the seats in a circular formation and sit down. This is probably the most relaxed I've felt all day."
        "I guess this would be a good moment to apologize to Lilly. I could do it after today, over the phone, but I'd really prefer to do things like these in person. I don't think either of us minds Hanako being nearby."

        show akira basic_resigned
        with chchange

        aki "So... umm... Lils, what did you think of today?"

        show lilly basic_smileclosed
        show akira basic_resigned
        with chchange

        li "It was good to celebrate New Year's Day together again after being separated for such a long time."
        aki "So you enjoyed it despite me... well... causing trouble?"

        show lilly basic_sad
        show hanako basic_worry
        with chchange

        "Lilly's smile falters a bit. Looks like she picked up what I'm talking about."

        play music music_drama fadein 4.0

        li "You're still troubled by Mother's words, aren't you?"

        show akira basic_distant
        with chchange

        aki "You think she was on to something?"
        "A pained expression appears on Lilly's face. This isn't a comfortable subject for either of us, and the silence that follows merely reinforces that."
        aki "You can tell me what you think, Lils. I won't be upset if you take Mom's side in this case."

        show lilly basic_concerned
        with chchange

        "Lilly's shoulders droop upon hearing my words. I can't help but feel that what was meant to be a reassurance had exactly the opposite effect."

        show akira basic_depressed
        show hanako emb_sad
        with chchange

        li "Akira... I don't want to take sides. I don't want to feel like having to choose between you and our parents anymore. There shouldn't be any sides to begin with. Why can't you understand that? Why won't you understand that?"

        "She's right, of course. There shouldn't be any sides. Yet ever since Mom and Dad left Japan, that's exactly how things have been in my mind. They abandoned us. They abandoned Lilly. So from that moment on, it was us and them."
        "They sent all the financial support we ever needed and then some, but as far as emotional and practical support were concerned, I was the only person Lilly had left. From that point on, it was up to me to be a father and mother figure at the same time."
        "I promised myself back then that I'd be a better parental figure to her than Mom and Dad could ever be. That bar wasn't set particularly high. All I had to do to stay above it was simply vowing to never abandon Lilly. Easiest vow I've made in my life."

        aki "There shouldn't be, but when Mom and Dad left, I really did feel like our family was split into two halves. That was simply the way things were."

        "Deep down, I felt the schism in our family was permanent. Even if they'd return one day, things wouldn't be the same. It would still be us and them. It would always be us and them. Even though I felt angry, even bitter, about it, I accepted this to be reality from then on."
        "Looking back on things, I think I did more than merely accept this new reality. I think I also grew comfortable with it. Like we were better off without them anyway. Maybe I grew too comfortable with the situation."

        show lilly basic_sad
        with chchange

        li "Maybe. But I don't think that's the way things should be."

        show akira basic_distant
        with chchange

        "The same obviously can't be said for Lilly. Deep down she never made peace with the way our family split up and probably always hoped they'd unexpectedly return to Japan and we'd pick up exactly where we left off."
        "Then we took that first trip to Inverness, and we experienced first-hand how much we had grown apart. It didn't really faze me since it merely confirmed what I already knew, but Lilly was very troubled by it."

        show hanako emb_downsad
        with chchange

        aki "I've been thinking about it, and Mom's probably right about me. I have given up on this family. Probably gave up a long time ago. Look, I'm really sorry for kicking up such a fuss."

        "When Mom and Dad asked Lilly to move to Inverness, I didn't really know what to think about it. Part of me felt like she was better off staying in Japan. She had her friends there and a little semi-family of her own. We'd stay in contact regardless."
        "If she'd really move to Inverness, I'd still get to hang out with her, but I didn't think she'd really get that close with our parents."
        "When Dad got hospitalized, the various confrontations between us reached a point where I feared that the two halves that made up our family were in danger of falling apart themselves and I hated the fact that I couldn't reliably support Lilly on this particular issue."
        "So eventually, I turned to Hanako who was the closest thing Lilly had to a sister aside from me. I'm not really sure what Hanako talked to her about - Lilly's never been willing to tell me - but the next time I saw Lilly, she seemed to have found a new sense of determination and purpose."

        "Things really changed after that. When I mentioned to Lilly that people at the office seemed worried about going to the States without Dad and Mom, she suggested for Mom to go and me to accompany her as Dad's representative while she stayed behind in Inverness to look after Dad in Mom's place."
        "We ended up going with that suggestion, and Mom and I spent quite some time in each other's company, although we didn't really do any bonding."
        "Lilly, on the other hand, really managed to make an impression on our old man while we were gone, and after we got back I couldn't help but feel that he developed a genuine soft spot for his youngest daughter."
        "When we learned that Dad was going to be replaced as CEO of the company and Lilly made the proposal for them to come and live in Japan again and Dad seemed to be willing to give it some thought, I did what I felt I had to do - throw my support behind my sister."

        show lilly basic_weaksmile
        show akira basic_resigned
        show hanako basic_bashful
        with chchange

        li "Even if you have given up on us, we haven't given up on you, Akira. Nor will we ever."
        aki "Heh, 'we' meaning 'you', Lils? Are Mom and Dad really this eager to have their black sheep back?"

        show lilly basic_sad
        show hanako emb_sad
        with chchange

        li "I think you're being too hard on yourself."

        show akira basic_distant
        with chchange

        "I dunno about that. As far as I'm concerned, Mom and Dad always considered me a bit of a troublemaker. While other kids in the neighborhood were spoiled by their mothers, I was continuously told what was or wasn't the proper way to act."
        "Them eventually sending me to that horrible middle school was just one more attempt to turn me into something I never was, nor ever could be. Maybe that's why I so quickly became comfortable with the situation of things coming down to me and Lilly."
        "Between the two of us, there was always unconditional acceptance. If the four of us would 'get back together again', there's no question who'd end up eventually falling by the wayside again, like always. Maybe that's why I feel the way I feel."

        aki "It's not myself I'm being hard on. I'm fairly comfortable with who I am even if most others aren't."

        show lilly basic_smileclosed
        show akira basic_resigned
        show hanako basic_normal
        with chchange

        li "They may be hesitant to show it, but your happiness is very important to them."
        li "In fact... While I was selfishly trying to convince you to accompany us back to Japan, Mother and Father felt that maybe it was a good idea to give you the opportunity to find out if you could become happy in Inverness."
        li "They were thinking of your well-being when I wasn't. It was Father who told this to me."

        aki "Heh... Dad?"
        li "He also told me he could never dislike you... because you remind him so much of Mother."

        show akira basic_smug
        with chchange

        aki "A couple of months ago, I would have insisted he'd take a drug test for saying that kind of thing."

        show lilly basic_cheerful
        show hanako emb_downsmile
        with chchange

        "Lilly giggles."

        li "I agree with him. You two really do seem to have a lot in common. I think... it made it easier for me - to reconnect with her."

        show akira basic_annoyed
        with chchange

        aki "Don't remind me, please."

        "It's probably not Lilly's intention, but her words give me an unpleasant feeling in the pit of my stomach, just like seeing Mom's interaction with her tends to do."
        "At first, I believed Mom somehow thought that imitating my way of interacting with Lilly was some quick and easy way to bond with her."
        "I was quite insulted by the idea of such a cheap trick actually working. It wasn't until I spent some more time at head office, where Mom and Dad were frequently brought up, that I started second-guessing my initial impression."

        ha "I... um... t-think it's actually t-true as well."

        show akira basic_smug
        with chchange

        "I smirk slightly as Hanako jumps in for the first time since we sat down here."

        aki "You wannna know something funny? I hear this all the time at work. Just about every time I have a bit of fun with a colleague, I hear stuff like 'That's your Mom talking'. It's actually starting to get on my nerves a bit, being compared to her all the time."

        "Lilly smiles."

        li "I think they're complimenting you. Mother was greatly respected at work, wasn't she?"

        show akira basic_sweet
        show lilly basic_smileclosed
        with chchange

        aki "Mom and Dad both - from what I've been able to tell so far. Dad was considered the brains of the operation. Very sharp business instincts and a knack for playing the long game, but also a bit distant and... heh... a bit repressed."
        aki "Mom was more considered the heart of the business. She had the reputation of being sociable and easy to approach."
        aki "She'd usually be the one to smooth over misunderstandings between the staff and either Dad or people from the Japanese branch, and she also acted as confidant for people on the workfloor."
        aki "Heh, over the last few months people have been randomly walking up to me - probably under the assumption that I am her successor or something..."
        li "This is merely conjecture on my part, but I believe you and Mother will probably get along very well with one another once you manage to work out your... differences."

        show akira basic_annoyed
        show lilly basic_sad
        show hanako emb_sad
        with chchange

        aki "Don't misinterpret my words, Lils. Just because she could earn my respect as a colleague doesn't mean I could respect her as a person, and without personal respect it would be really hard to get along, don't you think?"
        li "That's... pretty harsh..."

        show akira basic_resigned
        show lilly basic_sad
        show hanako basic_normal
        with chchange

        aki "Don't you wonder about it then?"
        li "Wonder about what?"

        aki "Mom used to be so different. She was pretty much the ideal housewife from a traditional male perspective. Quiet, elegant - but also a bit of a doormat."
        aki "I mean... When Dad summoned her to Scotland, I wasn't even that surprised she went along with it without putting up a fight. She almost always deferred to Dad. For some time, I simply saw her as just another victim. But that's kind of hard to believe now."
        aki "If this proper lady thing was really an act, put on to 'set the good example' or whatever lame excuse Dad gave, why didn't she tell him to stick that summoning where the sun don't shine? Unless, of course, she really did want to get away from us."
        li "I don't really have an answer to that. We don't really know what went on between them. Maybe there was a confrontation, and we simply don't know about it. Maybe we'll find out some day. "
        aki "I don't really get it, Lils. Is it really that easy for you to forgive them like that? Are you a saint, or am I simply dead inside?"

        show lilly basic_cheerful
        with chchange

        "Lilly giggles at that."
        li "I think neither. Can I say something that will remain within these walls?"

        show akira basic_sweet
        with chchange

        aki "My lips are sealed."
        ha "M-Mine too."

        show akira basic_distant
        show lilly basic_weaksmile
        show hanako basic_normal
        with chchange

        li "The truth is that... I haven't forgiven them myself yet either. But... I'd still like them to be part of my life in the meantime while I deal with that."
        li "I don't think I can go back to the way things were, because I perceive them in a different light now. Perhaps less as infallible authority figures and more simply as ordinary people, just like you and me - with both qualities and flaws."
        li "This makes it easier to appreciate their qualities and overlook their shortcomings. I'd like to give them a second chance to prove themselves. Deep down I feel that Mother and Father genuinely care about us and about our well-being."
        li "I want to try and have faith in them. I can't really explain it myself. Call it female intuition."

        "Faith, huh?"

        show akira basic_distant
        with chchange

        aki "Hmmph, I wonder why I don't have any of that 'female intuition' of yours..."

        play music music_twinkle fadein 4.0

        show lilly basic_cheerful
        show hanako emb_downsmile
        with chchange

        li "Hmmm..."
        "Lilly raises her hand to her mouth in order to hide a playful grin, and I realize that I just set myself up for the world's easiest punchline."

        show akira basic_kill
        with chchange

        aki "If any of you dare suggest that it's because I'm not feminine enough, you'll either be walking back to our parents' place or sleeping at the shrine. Just sayin..."

        show akira basic_laugh
        show lilly basic_giggle
        with chchange

        "Lilly and I share a hearthy laugh with even Hanako joining in eventually. After this little moment of silliness, Lilly slowly gets up from her seat."

        scene bg shrine_int_ni
        show lilly basic_cheerful_close at twoleft
        show hanako basic_smile_close at tworight

        li "Seeing that we're indeed still at a shrine, perhaps it would be a good idea to do what we came to do here. Our host is probably finishing up as we speak."
        aki "Good point. Let's go ahead and make a wish then."

        "We get up, I put some coins in the nearby offering box, and Hanako walks up to the bell cord on one side of the room, ringing the shrine's bell twice. As she joins Lilly in a silent little New Year's prayer, I find myself trying to put my thoughts in order."
        "For all her polite approach towards our parents, Lilly has a surprisingly down-to-earth attitude towards them that took me off guard a bit. Maybe I really should back off a bit and avoid shouting at Mom and Dad on her behalf."
        "Is it really possible to move on without forgiving them first?"
        "Can I have faith in them?"
        "Do I even want to?"
        "If I want to keep interacting with Lilly, I can't keep avoiding our parents, tempting as it seems."
        "I wonder what kind of future we have as a family, if any."
        "Making a wish for our family to fully reconciliate might be insincere on my part for now."
        "Maybe something more generic. I take a quick look at Lilly and Hanako and then silently nod to myself."
        "I wish..."
        "I wish for everyone I've been with today to have good fortune the upcoming year..."
        "...that includes..."
        "...I suppose..."
        "...Mom and Dad."
        "Yeah, that'll do."

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return

    return
