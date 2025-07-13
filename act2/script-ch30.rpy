label sh_ch30:
    label .s1:

        $ set_window_tint(TINT_LILLY)

        call sisterhood_timeskip

        scene bg satou_livingroom
        with nextchapter

        play music music_tranquil fadein 4.0

        show hanako basic_smile at tworight
        show hisao basic_frown_polo at twoleft
        with chchange

        ha "Check!"
        hi "Hrmg..."
        "I smile as I hear these two conflicting reactions from my friends."
        "I haven't been following the game between them very closely, but Hanako's exclamation, voiced in a slightly sing-song tone, as well as Hisao's frustrated grunt, leave little doubt as to who is currently winning."
        li "Is Hanako giving you trouble, Hisao?"

        show hisao basic_speak_polo
        with chchange

        hi "It's okay, Lilly. Nothing I can't handle."

        show hisao basic_pout_polo
        with { "master": chchangefast }

        extend " {size=*0.5}Who needs a queen anyway?{/size}"
        "That last part is spoken in a soft mumble, but I can hear it anyway."

        nvl clear
        nvl show dissolve

        n "It's been one and a half weeks since we first arrived in Inverness, and so far I can say that the vacation has been very enjoyable. Hanako and Hisao have even taken a few trips together without Mother and me around."
        n "They're still a little bit reluctant to travel around the area together due to their English being less fluent than mine, but this does happen to be the ideal way for them to improve it."
        n "I also think they enjoy spending some time together now and then. It must be wonderfully romantic spending your vacation in a part of the world that's completely new together with someone you love. I think I even envy Hanako a bit."
        
        nvl clear

        n "Today has been a rather uneventful day. Hanako and Hisao slept in, or at least didn't come out of their room until it was nearly noon, and since we had some rain early in the afternoon, we decided to spend the day here at my parents' home, reading and talking."
        n "Right now it's just Hanako, Hisao, and me here, hanging out in the living room. The cleaning staff have already left, Mother's currently visiting her older sister and won't be back until tomorrow, and Father's still at work."

        nvl clear

        n "I feel a bit bad for Father. Apparently the final negotiations for the acquisition of another company by Father's company are only a few weeks away, and things are extremely hectic at work. I have a feeling my visit here has been rather ill-timed."
        n "Mother and Father have both promised to spend at least a few days with me while I'm here, and so far Mother has already come through."
        n "{vspace=30}Father is set to spend three days with us the day after tomorrow. Akira mentioned a few days ago that she wouldn't be surprised if he ended up calling our time together off, since he can't really afford to take these days off at this point, but so far I haven't heard him confirm that."
        n "Apparently he's been trying to finish as much of his work that was originally planned for the upcoming week as possible, but as a result, I've barely interacted at all with him. He tends to leave the house early and works until very late."
        n "Since he's apparently partially doing this for my sake, I don't really feel in a position to complain."
        
        nvl clear

        n "To be honest, Father has always worked very long hours for as long as I can remember. I suppose as the son of the company head he felt he had to set the good example. But Akira said that over the last few weeks he's been looking like a ‘burnout sufferer in denial’."
        n "I'm not sure what to make of that, but even Hisao and Hanako said that he didn't look like he was sleeping very well. I hope that when he takes a few days off, he'll be able to relax a little bit."
        n "{vspace=60}It's probably too much to hope for, but surely he realizes that having a breakdown at this point in time might sink his whole deal."
        
        nvl hide dissolve

        hide hanako
        hide hisao
        with charaexit

        play ambient sfx_phonering2

        "My thoughts are interrupted by the phone on one of the sidetables suddenly springing to life. After some hesitation, I pick it up."

        stop ambient

        li "Good evening, Satou residence. Lilly Satou speaking."

        show karla basic_smile_cas_phone at phonebox
        with charaenter

        kam "Hi Lilly."
        li "Oh, hello Mother. Have you already arrived at Aunt Stella's place?"
        kam "Yeah, I arrived here half an hour ago."
        li "Aren't you tired? Driving all the way over there after work..."

        show karla basic_sheepish_cas_phone
        with chchange

        kam "Only a little. It's been a long day, but I promised her I'd come see her before your father and I leave for the US, and I think the upcoming weeks are only going to get busier."
        kam "And I won't have time the upcoming days either when your father takes a few days off and I get back to work."
        kam "Speaking of which, is he already home?"
        li "No, not yet..."
        "I think those two work way too hard."
        li "Mother..."
        "I'm a little worried about them, but I don't really think it's a daughter's place to admonish her parents about the way they live their lives."

        show karla basic_smile_cas_phone
        with chchange

        kam "Yes?"
        li "Ah... I don't mean to speak out of line, but..."
        kam "Heh, don't worry about that. Just say what's on your mind."
        li "Are you and Father still... holding up? Things have been stressful for you, haven't they?"

        show karla basic_ponder_cas_phone
        with chchange

        kam "I'm still doing okay. It's been hectic, and will continue to be for a few weeks, but I still feel fine. I'll be glad when it's over, but I still feel like I'm able to handle things."
        li "How about Father? Akira, Hisao, and Hanako said he looked... not well."
        "Mother lets out a weary sigh."

        show karla basic_distant_cas_phone
        with chchange

        kam "Well, I won't deny he's been a little under the weather lately."
        kam "He's been having trouble sleeping, he mentioned having bouts of indigestion, and earlier today, he even mentioned repetitive strain injury in his shoulder and arm. It's just one thing after another."
        li "Shouldn't he take it easier then?"

        show karla basic_lost_cas_phone
        with chchange

        kam "I suggested that too, but it's not that simple. To me, this whole thing is just crunch time for the company I work for. It'd be great if we could pull it off, and I'll be sure to do my part, but in the end, it's still just work."

        show karla basic_resigned_cas_phone
        with chchange

        kam "To him, this is his legacy. His grandfather expanded the company, as did his father. Now it's his turn. It's what he's studied and worked for. Wouldn't you feel enormous pressure? Would you take it slowly just a few inches before the finish line?"
        li "Probably not, but it doesn't sound like a very healthy situation to be in."

        show karla basic_ponder_cas_phone
        with chchange

        kam "I know, but it's only a few more weeks, and he said he was still fine, so I'll take his word for that."

        show karla basic_wistful_cas_phone
        with chchange

        kam "After we travel to the US and finish the deal there, I intend to stay there for a bit and take him on a little trip. See some of the national parks, maybe the Niagara Falls, too. Take it easy, see stuff, just relax. That'll fix him right up, you'll see."
        li "...I hope so."
        kam "When he's taking time off to spend with you, just try to do whatever you can to take his mind off the business, okay? I'd appreciate that even though it may be a losing battle."
        li "I will try."

        show karla basic_smile_cas_phone
        with chchange

        kam "Great. By the way, the reason I'm calling is to ask if either Hanako or Hisao happens to have an allergy to nuts or almonds."
        li "Not as far as I know. We had both as a snack during our flight."

        show karla basic_cheerful_cas_phone
        with chchange

        kam "That's good to hear. Stella was thinking of baking you a dundee cake. That's a traditional Scottish fruitcake covered with almonds. I find it kind of filling, but really tasty, too."
        li "That sounds delicious. I can't wait for us to get there so I can have a taste. How is she doing these days?"

        show karla basic_sweet_cas_phone
        with chchange

        kam "She doesn't really get out of the house much yet, and she has the occasional spells of sudden tiredness, which is probably partially due to her medication, but all in all, she's doing a lot better than two months ago."
        li "Please give her my regards."
        kam "Will do. I'm going to hang up now. Be sure to let your father know that I've arrived safely when he gets home, okay?"
        li "I will. Until tomorrow, Mother."
        kam "Bye."

        hide karla
        with charaexit

        nvl clear
        nvl show dissolve

        n "I put down the phone with some mixed feelings."
        n "{vspace=30}I still feel a little awkward talking to Mother. What's more, what she said about Father didn't exactly reassure me. Even though Father's been a hard worker his entire life and wasn't home very often except on Sundays, this is the first time I've heard of his work taking a physical toll on him."
        n "I don't like the idea of him overworking himself even more merely because I wanted to spend a few days with him. If I had known things were this hectic for him already, I wouldn't have asked to begin with."
        
        nvl hide dissolve

        "I put away the phone and refocus my attention on my friends' game of chess."
        "I can't hear any direct reactions, but I notice from the pauses between the taps that one side is taking a lot less time to plan the next move than the other."
        "Eventually, the verdict is called."

        # TODO PICK UP FROM HERE

        show hanako basic_smile at tworight
        show hisao cross_pout_polo at twoleft
        with charaenter

        ha "Checkmate!"
        hi "Congratulations."
        li "Congratulations, Hanako."
        ha "Thanks. Ummm, do you want to go again, Hisao?"

        show hisao cross_smile_polo
        with chchange

        hi "Well, okay. This time I might try to stick more to the tried and true stuff."

        show hanako basic_bashful
        with chchange

        ha "Your opening was a bit unusual this time."
        hi "Yeah, I tried to do one of those exotic openings I read about in a chess book before we went on vacation, but either I remembered it wrong or I bungled it up somewhere along the way. I don't usually lose this quickly."
        ha "Unpredictability is usually a good thing in chess."

        show hisao cross_grin_polo
        with chchange

        hi "Yeah, but only if you know what you're doing."
        "I hear the sound of chess pieces being placed in their starting position, and moments later, the first piece is moved."

        show hanako basic_smile
        show hisao basic_speak_polo
        with chchange

        hi "Lilly?"
        li "Yes, Hisao?"
        hi "Where exactly was your mother staying again?"
        li "Edinburgh, Hisao. Her older sister lives there."
        hi "Is this the same sister you and Akira visited in July?"
        li "It is. Mother promised her that she'd stop by before she and Father left on their business trip to the US."
        li "Since it's about a 3 hour drive from Inverness to Edinburgh, she decided to spend the night at her sister's place and drive back very early tomorrow morning."

        show hanako basic_bashful
        show hisao basic_neutral_polo
        with chchange

        ha "Are she and your mother close? Like you and Akira?"
        li "I don't think they've ever been extremely close. Mother had very little contact with her family while she was living in Japan."
        li "She was a bit of a late arrival in the family and didn't form an extremely close bond with her siblings. There are 10 years between her and Aunt Stella."
        ha "There are also 7 years between you and Akira."
        li "That's true. I suppose it's different for everyone. I was lucky my sister paid so much attention to me when we were younger."

        show hanako basic_smile
        show hisao basic_smile_polo
        with chchange

        hi "Did you say that we were going to go there ourselves?"
        li "Yes. When Father takes a few days off, he'll be taking us to Edinburgh. We'll visit my aunt when we're there, but for the most part, we'll be sightseeing—so to speak."
        hi "Were you there last time as well? What's the city like?"
        li "I was there only briefly during my last stay, but the city feels different from Inverness. Bigger and more crowded. Mother said it's literally ten times as populated as Inverness."
        li "Of course, Edinburgh is the capital of Scotland and the most populated city in the country after Glasgow, so it's quite unlike Inverness. I'm rather curious about your impressions of it."
        hi "You mentioned sightseeing. Any further information on where we'll be going, or is it going to be a surprise?"
        "I open the drawer of one of the sidetables and pull out what I know is a tiny folder on Edinburgh's main tourist attractions, which I give to Hisao."
        li "You could take a little look in here and see if there's anything you like."
        hi "Thanks... "

        show hisao basic_frown_polo
        with { "master": charachangealways }

        extend "ugh, it's all in English."
        "I grin."
        li "Of course. But if you don't understand the meaning of certain words, just read the corresponding sentence to me and I'll tell you what it means."
        hi "If I do that, are you going to correct my mispronunciations again? The last time we did something like this, you turned it into a miniature English lesson."
        "I give a disappointed pout. Why is he so resistant towards improving his language skills?"
        li "But... it's a pretty important skill to have in order to make yourself understood around here and surely an upcoming scientist must have some adequately honed skill in the language, especially since many scientific documents and websites are in English."
        li "Isn't it better for me to give you a few pointers now instead of having you picking up the wrong habits?"

        show hisao cross_grin_polo
        with charachangealways

        show hanako emb_downsmile
        with charachangealways

        "The only immediate response I get is a muffled giggle from Hanako. Hisao must have rolled his eyes or made a face in response to my words. I'm probably fighting a losing battle here, so I decide to drop it."

        show hisao cross_smile_polo
        with chchange

        li "Anyway, Edinburgh has quite a few museums that make for an interesting experience. There are also other places of note that Father said would be worth our while, such as the Edinburgh Zoo and the National Library of Scotland."

        show hanako emb_smile
        with chchangefast

        ha "Library?"

        show hisao cross_grin_polo
        with chchange

        "Hisao and I both chuckle at Hanako's immediate reaction."
        li "Yes, Edinburgh has quite a few libraries, and the National Library of Scotland is the most prominent among them, because it's this country's legal deposit for books. They have quite a few old documents and maps there as well."
        li "I think a visit there would be most educational and, given the fact that Father has quite a fondness for books himself, I'd be extremely surprised if a visit to the National Library wasn't on the program."

        show hisao basic_smile_polo
        with chchange

        hi "It sounds like an interesting place to visit. I've never visited a national library before. Have you, Hanako?"
        ha "No. I'd like to go there, even if it's not the national library of Japan. It sounds interesting."
        li "Well then, one destination is already set."

        show hanako emb_downsmile
        with chchange

        ha "Hmmm, those koalas in that picture look really cute."
        "I smile at Hanako's words."
        li "It sounds like we have another addition to our to-do list."

        show hisao basic_speak_polo
        with chchange

        hi "But Lilly, aren't these things kind of boring for you? This doesn't look like the petting zoo you and Hanako went to before."
        li "I think I can still enjoy myself there, Hisao. You and Hanako can describe the animals to me and I can still hear and smell them."

        show hisao basic_grin_polo
        with chchange

        hi "Smell? I've always felt that all zoos smell alike. Is there a big difference between the smell of elephant droppings and the smell of gorilla turds?"
        li "Well, ah..."

        show hanako emb_smile
        with chchangefast

        ha "Pfffff!"
        "While I'm still wondering whether that question deserved a serious answer, I hear Hanako trying desperately to hold her laughter, and I realize Hisao was having a little fun at my expense."
        "I sigh and give Hisao an admonishing pout before turning to Hanako."
        li "Hanako, it's probably not necessary to go easy on Hisao this match. I don't think he deserves it."
        "Hanako lets out a conspiring giggle."

        show hisao basic_neutral_polo
        show hanako emb_downsmile
        with chchange

        ha "Okay."
        hi "Hey! That's not very nice."
        "I smile sweetly at Hisao."
        li "Any more suggestions, Hisao?"

        show hisao basic_smile_polo
        show hanako basic_smile
        with chchange

        hi "I don't know. There seem to be a lot of museums in Edinburgh, but I'm not sure which ones would be most interesting to visit. I'd rather not go to ones that require a lot of knowledge about the local history."
        li "How about the Museum of Childhood then?"
        hi "The Museum of Childhood?"
        li "I've heard there's a museum in Edinburgh that's dedicated to children's toys throughout the last two centuries. Apparently it has an exhibition containing many dolls from several generations."

        show hanako basic_bashful
        show hisao cross_grin_polo
        with chchange

        ha "Hmmm, Hisao?"
        hi "She caught your interest, didn't she?"
        ha "It sounds like a fun place to visit."
        "I can't help but smile at Hanako's elated tone. Yes, this place definitely sounds worth visiting, if for no other reason than to witness Hanako's reaction."
        li "I'll bring it up with Father. Are there any other museums worth visiting in the folder, Hisao?"

        show hisao basic_smile_polo
        show hanako basic_smile
        with chchange

        hi "Hmm, City Art Center, Museum of Edinburgh... I don't know if visiting art displays is really something you'd enjoy."
        li "Any museums about specific subjects?"
        hi "This one may interest you. The Writers' Museum. It's dedicated to three well-known Scottish writers."
        li "Hmmm, which ones?"

        show hisao basic_speak_polo
        with chchange

        hi "Robert Burns, Sir Walter Scott, and Robert Louis Stevenson."
        li "Burns is probably not very familiar to you, seeing as he was a poet, considered by many as {i}the{/i} Scottish poet. You may not know about Scott either, unless Ivanhoe sounds familiar to you."

        show hisao basic_neutral_polo
        with chchange

        hi "I'm afraid it doesn't."
        li "Surely you must know Stevenson though. Have you read ‘Treasure Island’ or ‘The Strange Case of Dr Jekyll and Mr Hyde’?"

        show hisao basic_smile_polo
        with chchange

        hi "I haven't, but I know the general plot of both."
        ha "Me too."
        li "Then this will be my request for the day. It's not a location an aspiring English teacher can afford to pass up."

        show hisao basic_speak_polo
        with chchange

        hi "They might not have much information printed in Braille."
        li "Then surely I'll be able to rely on the two of you to read it to me, and..."

        play sound sfx_car_driveup

        show hisao basic_neutral_polo
        show hanako basic_normal
        with chchange

        "As I reply to Hisao, I suddenly pick up a sound coming from outside the house."
        ha "Lilly, did you hear something?"
        "I think I hear a car outside. Is that Father coming home already? Seems that way."
        li "I think Father's home. What time is it right now?"
        hi "Half past 8. I don't recall him coming back this early since we arrived here."
        li "That's true, he's unusually early, though I certainly won't complain about that."
        "A few minutes later, I hear footsteps slowly approaching followed by the voice of my father greeting us."

        show hisao at left
        show hanako basic_distant:
            xalign 0.35
        show hiroyuki basic_neutral_suit at right
        with charaenter

        hyf "Lilly, Miss Ikezawa, Mister Nakai... Good evening."
        hi "Good evening, sir."
        ha "G-good evening."
        li "Welcome back, Father. I'm happy to see you could make it back here sooner than usual."

        show hiroyuki basic_strain_suit
        with chchange

        stop music fadeout 4.0

        hyf "I... am afraid I still have a few things to do. I will be retiring to my study. Please do not disturb me while I am working..."

        play ambient sfx_ticktock fadein 4.0

        show hisao basic_neutral_polo
        show hanako basic_worry
        with chchange

        ha "..."
        hi "..."
        li "Ah... Of course, Father."
        hyf "Good evening, then."

        hide hiroyuki
        with charaexit

        "I'm taken off guard by the abrupt tone of Father's voice. He usually takes the time to properly greet us when he comes home. Is he in that much of a hurry?"
        "As Father's footsteps head into the direction of the study and I hear a door being closed in the distance, I turn to Hanako and Hisao."
        li "I... apologize. He's usually not that curt with others."
        hi "It's okay, Lilly. To be honest, he didn't really look like he was up for a chat anyway."
        li "Hmmm?"
        hi "I don't know, he looked a bit pale. Maybe he came home because he was getting sick."
        li "Mother already said he had trouble sleeping and had been complaining earlier about bouts of indigestion and repetitive strain injuries."
        li "I wonder if it's a good idea to force him to take a few days off while he obviously can't afford it. Would you be very disappointed if I suggested canceling the trip to Edinburgh, so Father would have a bit more breathing room?"

        show hisao basic_smile_polo
        show hanako basic_bashful
        with chchange

        hi "Of course not, Lilly. Heck, this trip could end right here and now, and I'd still call it a grand success."
        ha "I agree."
        li "That is good to hear. I'll go and talk to him about it."

        hide hanako
        hide hisao
        with charaexit

        "I take my cane and slowly make my way to the study."

        if _in_replay:
            return

    label .s2:

        $ set_window_tint(TINT_LILLY)

        scene bg satou_stairs
        with locationchange

        "I open the door just a little bit and hear the sound of someone typing on a keyboard."

        play sound sfx_doorknock2 volume 0.9

        "I knock a few times to announce my presence."

        stop ambient fadeout 1.0

        play sound sfx_doorclose

        scene bg satou_study
        show hiroyuki basic_strain_suit
        with locationchange

        play music music_happiness fadein 4.0

        "I'm greeted by a tired sigh as I enter."
        hyf "Yes?"
        li "Ah...Father?"

        show hiroyuki basic_stern_suit
        with chchange

        hyf "Lilly, did you not hear what I said earlier?"
        li "I know, Father. This won't take long."
        hyf "Go ahead."
        "I walk further into the room until I'm standing near the table where Father is working."
        li "Father, is it... wise to keep working right now despite the fact that you were plagued by RSI earlier?"

        show hiroyuki basic_raisesternbrow_suit
        with chchange

        hyf "Hmmm? Ah, my shoulder? Did your mother tell you about that?"
        li "She did. Are you... feeling alright?"
        hyf "I am fine. Why are you suddenly so concerned about me?"
        li "Hanako and Hisao said that you looked a little pale when you came in."

        show hiroyuki basic_strain_suit
        with chchange

        "Another weary sigh. He's obviously not pleased with my insistence."
        hyf "I felt a bit unwell at the office, so I decided to return home earlier than planned. The sensation disappeared when I left the building. It has not returned since. I am fine right now."
        li "I've been thinking, Father. Perhaps we should call off our trip to Edinburgh. Or at least postpone it until a more convenient time."
        hyf "A more convenient time?"
        li "When you're... no longer under so much pressure."

        show hiroyuki basic_stern_suit
        with chchange

        hyf "I have already made you a promise, have I not?"
        li "There will be other times."
        hyf "I do not like to go back on my word. It is a matter of honor."
        li "B-but..."
        hyf "Lilly, a proper lady... respects the will... of her elders."
        li "Father, is anything wrong?"

        show hiroyuki basic_strain_suit
        with chchange

        hyf "Perhaps... you could get me a glass... of water."
        li "Right away, Father."

        play sound sfx_dooropen

        scene bg satou_livingroom
        show hisao basic_neutral_polo at twoleft
        show hanako basic_worry at tworight
        with locationchange

        "I make my way out of the study and back to the living room and let out a tired sigh."
        li "It seems you were right, Hisao. Father did feel unwell earlier and decided to go home earlier because of that. Whatever he felt disappeared before he could get behind the wheel. Fortunately."
        li "But I still think he's falling ill. There was just... something off about his breathing."
        ha "..."

        show hisao basic_speak_polo
        with chchange

        hi "Wow, you actually notice these things?"
        li "Only because I was paying close attention to it. But despite everything, he still won't take my offer of calling off our trip to Edinburgh. It is a little disheartening."

        scene bg satou_kitchen
        with locationchange

        "I navigate over to the kitchen and probe the shelves of the cupboard with my hand until I feel an empty glass against my fingers."
        "I take it, feel my way over to the tap and fill it with fresh and cool water."

        show hanako emb_timid at right
        with charaenter

        ha "L-Lilly?"
        "Just as I finish filling up the glass, I hear a soft voice coming from the doorway."
        li "Hanako. Are you already finished with your chess match?"

        show hanako emb_sad at tworight
        with charachangealways

        ha "Ummm... If your father is feeling ill, w-wouldn't it be good to... call a doctor?"
        li "A doctor?"
        ha "Y-yes."
        "I'm about to brush aside Hanako's suggestion, seeing that Father would probably not go along with that, but then I realize that Hanako following me here and telling me this are kind of unusual for her."
        "She's not exactly the most proactive person in the world. She probably wouldn't bother approaching me like this without good reason. But what reason is that?"
        li "Do you really think so, Hanako?"

        show hanako emb_timid
        with chchange

        ha "It's... p-probably nothing, but... better safe than sorry, right?"
        "It's probably nothing, but better safe than sorry..."
        "What's probably nothing?"
        "Does Father really look that bad?"
        "I really wish I'd be able to look at him with my own eyes."
        li "I'll talk to him about it, Hanako."
        ha "Okay."

        scene bg satou_study
        with locationchange

        "I carefully make my way back to the study, wondering how on earth I'd be able to convince Father to go see a doctor."
        "A proper lady respects the will of her elders..."
        "The hint was clear. He wants me to stop worrying about him."
        "But still..."

        show hiroyuki basic_strain_suit
        with charaenter

        li "Father, I brought you your drink."
        hyf "Thank you."
        "He takes it from my hands and takes a few careful sips."
        "This should be the moment where I take my leave, but I manage to stop myself from walking away."

        show hiroyuki basic_raisesternbrow_suit
        with chchange

        hyf "Lilly, is there something else?"
        "He must have spotted my fidgeting."
        li "Father... are you really feeling fine?"
        hyf "This again?"
        li "It's just... m-maybe it would be a good idea to call a doctor if you're feeling unwell."
        hyf "A doctor?"
        li "You say you're fine, but... I noticed... t-that your breathing is a bit more shallow than usual."

        play sound sfx_impact2

        $ renpy.music.set_volume(0.0, delay=0.2)
        $ renpy.music.set_pause(True)

        show hiroyuki basic_stern_suit
        with chchangefast

        hyf "Lillian, that is quite enough!"
        "I cringe at his stern tone. I overstepped my boundaries, that's obvious."
        li "I... apologize. I'll be on my way. But..."

        $ renpy.music.set_pause(False)
        $ renpy.music.set_volume(1.0, delay=4.0)

        show hiroyuki basic_neutral_suit
        with chchange

        hyf "Yes?"
        li "You told Mother you were fine, and she said she took your word for it. Would you... also give me your word that you'll be fine?"

        show hiroyuki basic_raisesternbrow_suit
        with chchange

        hyf "My word...?"
        li "Yes, please promise me that you'll be okay. Since keeping your word is a matter of honor, I will trust it."

        show hiroyuki basic_thinking_suit
        with chchange

        hyf "..."
        "There's a long silence. I wonder if he's going to scold me, but to my surprise, he eventually lets out a resigned sigh."

        show hiroyuki basic_strain_suit
        with chchange

        hyf "If I talk to a doctor... on the phone... will that be enough to reassure you?"
        li "It will."
        hyf "The phone in the living room should contain our general practitioner's phone number. His name is Thompson."
        li "Thank you, Father."

        show hiroyuki basic_stern_suit
        with chchange

        hyf "Hrmmm..."

        scene bg satou_livingroom
        show hisao basic_neutral_polo at twoleft
        show hanako basic_worry at tworight
        with locationchange

        "I walk back to the living room as quickly as I can and hand Hanako the phone."
        ha "Thompson?"
        li "Yes, Father said the number should be in the phone's memory. I suppose it's listed as either doctor or Thompson."

        show hanako basic_distant
        with chchange

        play sound sfx_phonedial

        "I hear a long series of beeps as Hanako starts browsing through the phone's contact list."
        ha "Here it is. Shall I call it?"
        li "Yes please."

        hide hisao
        hide hanako
        with charaexit

        "I hear one more beep and then the phone is handed back to me."
        
        play sound sfx_phonepickup

        "Moments later, I hear someone on the other end of the line picking up."
        "Doctor" "Thompson speaking."
        li "Doctor Thompson, good evening. This is Lilly Satou speaking. I hope I'm not intruding on you. I'm terribly sorry for calling you this late."
        "Doctor" "Not a problem, Miss... Satou?"
        li "Yes, you are my father's general practitioner, are you not?"
        "Doctor" "Why yes, I am. Is there something wrong?"
        li "Father's been extremely busy with work lately. There's a very important event in his business coming up, and he's under a large amount of pressure right now. It seems to be... taking a toll on him."
        "Doctor" "Are there any specifics you can give me, Miss Satou?"
        li "Just... several things. He's been having trouble sleeping as of late. My mother said he complained about RSI in his shoulder earlier today. There's been talk of... hmmm... indigestion."
        li "He actually came home earlier today because he felt a little unwell and my friends said he looked rather pale. I noticed his breathing was a bit shallower than usual."
        li "I'm... probably worrying about nothing, but I was wondering if you would..."
        "Doctor" "Just a moment, Miss Satou. Did you say he felt unwell earlier?"
        li "Yes, but the sensation disappeared eventually."
        "Doctor" "What kind of sensation? Localized somewhere?"
        li "He didn't say."
        "Doctor" "..."
        "A long silence."
        li "Doctor?"
        "Doctor" "Miss Satou, is there someone present with a driver's license aside from your father?"
        li "Ah... there isn't. Mother is out of town this evening. I could perhaps call the housekeeper. She might be willing to take him to your place."
        li "But is there a reason why it'd be irresponsible for him to drive himself?"
        "Doctor" "There is no need for him to come by my place, Miss Satou. But I think it would not be a bad idea to quickly stop by at Raigmore and have someone there take a look at him. It's not very far from where you live, is it?"
        "I let out a surprised gasp."
        li "The hospital?"
        "First Hanako and now the doctor..."

        stop music fadeout 10.0

        play ambient sfx_ticktock fadein 10.0

        "Doctor" "Yes. I'm going to make a quick phone call there and tell them to expect you. Have you been to Raigmore before? Do you know where the cardiology ward is located?"
        "Doctor" "Ah, then again, your father probably knows where it is, given his profession."
        "I feel my blood freeze in my veins and a heavy sensation in the pit of my stomach."
        li "C-cardiology?"
        "Doctor" "Yes. The person on duty there will either be Doctor Morrison or Doctor McElroy."
        li "Doctor... What's going on?"
        "Doctor" "...could I speak briefly with your father, Miss Satou?"
        li "Of course..."

        stop ambient fadeout 1.0

        scene bg satou_study
        with locationchange

        "A bit unsteadily, I head back to the study again."
        li "Father?"
        "There's no response. That's strange. I thought I heard a sound coming from the study while I was on my way there."
        li "Father, are you there?"
        "Nothing."
        "Not an acknowledgement, nor a typing sound. Not even a breath."
        "Did he leave?"
        li "Father, where are you?"

        play sound sfx_impact

        "I walk further into the room and almost immediately my foot hits something."
        "Something on the floor that wasn't here before."
        "I kneel and reach out to examine it."
        "As my hand makes contact with it, I feel a shiver running down my spine."
        "It's a person, lying on the floor near the door."
        li "Father?"
        "Not an acknowledgement, nor a typing sound. Not even a breath."
        "{i}NOT EVEN A BREATH!{/i}"

        scene ev withoutthinking_lilly
        with mediumflash

        play music music_tragic

        li "{i}FATHER!{/i}"
        "Doctor" "Miss Satou!"
        "The sound of the doctor's voice on the phone reminds me that I was on my way to hand over the phone."
        "Doctor" "Miss Satou, I'm going to hang up and call an ambulance to pick up your father this instant. Do not leave his side until they arrive."
        "What's happening? What's going on? Is he...?"
        hi "Lilly? Is something wrong?"
        "I hear Hisao's and Hanako's footsteps hurriedly approaching, probably drawn here by my shout."

        show ev withoutthinking_crowd
        with charachangeev

        "As they come in, I hear two gasps."
        hi "Mister Satou! Lilly, what's happened here?"
        li "I... I d-don't know. I c-can't hear him breathing."
        "{i}Somebody do something! Please!{/i}"
        "Hanako's breathing, on the other hand, is becoming more pronounced by the second. I'd probably start worrying about her if I wasn't on the verge of panic myself."
        hi "Damn, should we give him artificial respiration? Does he even have a pulse?"
        li "I... I don't know. J-just d-do something, please."
        "I'm not sure what's more unsettling—Hisao's panicked tone or Hanako's ragged breathing."
        hi "I can't feel any pulse in his wrist. Is there a better way to do this?"
        "She's almost hyperventilating."
        li "I don't know!"

        window hide None

        show ev withoutthinking_cpr
        with { "master": charachangeev }

        call screen sh_doublespeak(li, _("Aah!"), hi, _("Hey!")) with dissolve

        window auto True

        "Hisao and I let out a surprised cry as we're suddenly violently being pushed aside, and I nearly hit my head on the table in the process."
        "When I catch my bearings, I become once again aware of Hanako's breathing, but it's different this time. Instead of the hyperventilating gasps she was letting out earlier, she's now letting out a steady stream of short, sharp breaths."
        ha "{i}*huff* *huff* *huff*{/i}"
        li "H-Hanako?"
        ha "{i}*huff* *huff* *huff*{/i}"
        li "What are you doing?"
        hi "She's pressing down on his chest. I think she's doing CPR, Lilly. Hanako, is there anything I can do?"
        ha "{i}*huff* *huff* *huff*{/i}"
        hi "Hanako, can you hear me?"
        ha "{i}*huff* *huff* *huff*{/i}"
        "No answer. Hanako's breathing is so steady it's almost robotic."
        "I wonder if she knows what she's doing. But what choice do we have?"
        "{i}What's taking that accursed ambulance so long?!{/i}"
        li "Doctor Thompson said he'd call an ambulance. They... they should be on their way."
        hi "Then I'll go and open the gates and the front door, so they'll be able to get here as quickly as possible when they arrive."
        li "Y-yes, thank you Hisao."
        ha "{i}*huff* *huff* *huff*{/i}"

        show ev withoutthinking_cpr_nohisao
        with charachangeev

        "I hear Hisao running off, leaving me alone in the room with Hanako... and Father."
        "It doesn't happen often, but right now I'm cursing my blindness. My friends are both doing their part, and here I am, unable to do anything."
        li "Please d-do your best, Hanako. Let me know if you need anything..."
        "{i}Father...{/i}"
        "Seeing how close to the door he was, I think he was trying to get out of the room before he collapsed."
        "Did he call out for help, and did I fail to hear it?"
        ha "{i}*huff* *huff* *huff*{/i}"
        "{i}What's taking that ambulance so long?{/i}"
        "Am I going to lose him, just like Hanako lost her parents?"
        "Is that exasperated sigh he let out when I walked out of here going to be the last thing I'll ever hear from him?"
        "That's too cruel."
        ha "{i}*huff* *huff* *huff*{/i}"
        "{i}Please hang in there, Father.{/i}"
        li "Hanako, please hang in there."
        "Is that the best I can come up with?"
        "I used to have no trouble finding the right words to encourage Hanako. And now, now that it matters more than ever, I find myself lost for words."
        ha "{i}*huff* *huff* *huff*{/i}"
        "Hanako's breathing is getting less steady. Is she getting worn out? What she's doing must be pretty tiring."
        "What if she gets too tired to continue and the ambulance hasn't arrived yet?"
        "How will she feel?"
        "{i}What's keeping that ambulance?{/i}"
        ha "{i}*huff* *huff* *huff*{/i}"

        play sound sfx_brokenbone

        show ev withoutthinking_cpr_cover
        with charachangeev

        "A wave of nausea washes over me as I hear a soft crunch coming from the place where Father's lying."
        "It's barely audible yet it chills me to the bone. Is this the sound of someone's ribs being fractured? That sounded really painful."
        li "Hanako, be careful!"
        "I manage to get a hold of myself just in time to refrain from making the terrible mistake of grabbing Hanako and yanking her away from Father. At this point, it seems stupid to worry about broken ribs."
        ha "{i}*huff* *huff* *huff*{/i}"
        "Hanako didn't even seem to have heard my scream. She just keeps going as if there's nobody else in existence."

        play sound sfx_brokenbone volume 0.8

        "I squeeze my eyes shut in order to hold back the tears and let out a tortured whimper as I hear a second crunch."
        "What if one of those ribs punctures his lung? What if they manage to revive him only for him to drown in his own blood moments later?"
        "No, don't think that way. Don't even start thinking that way."
        "{i}Damnit, where's that ambulance?{/i}"
        ha "{i}*huff* *huff* *huff*{/i}"
        "I wonder if there isn't a defibrillator somewhere in the house. Father's company sells them after all. He might have taken one home at some point."
        "But where would he keep it? And would any of us be in a condition to operate it?"

        play ambient sfx_ambulance_distant fadein 10.0

        "Before I can ponder my thought further, my attention is drawn by a distinctive sound coming from outside."
        "Is that a siren?"

        show ev withoutthinking_cpr_nohisao
        with charachangeev

        li "Hanako, I think I hear a siren!"
        ha "{i}*huff* *huff* *huff*{/i}"
        "Trying to keep focus through the sound of my own rapidly beating heart, I try to concentrate on what I heard earlier. Somewhere from outside I can clearly hear the distinct wail of a siren."
        li "Hanako, the ambulance is arriving!"
        ha "{i}*huff* *huff* *huff*{/i}"
        li "Hold on for just a little while longer, Hanako. Please... Hang in there..."

        stop ambient fadeout 4.0

        play sound sfx_ambulance_arrive fadein 1.0

        "The sound of the siren is now joined by the sound of a car screeching to a halt."
        "Then footsteps. Many footsteps. And voices."
        "Paramedic" "Lead the way, lad."
        "Paramedic" "The doctor who called said it was probably a heart attack. Bruce, you do the compressions!"
        "Paramedic" "Will do!"
        ha "{i}*huff* *huff* *huff*{/i}"

        stop sound fadeout 0.5

        play ambient sfx_crowdmale fadein 1.0

        scene bg satou_study_blur
        show crowd
        with locationchange

        "I hear several people bursting into the room. I just sit there in a daze as everything plays out in front of me, unable to figure out how to act or what to say."
        "Paramedic" "Alright, lass, you can stop now. We'll take over from here."
        ha "{i}*huff* *huff* *huff*{/i}"
        "Paramedic" "Hey, didn't you hear me? You need to give us room to work!"
        ha "{i}*huff* *huff* *huff*{/i}"
        "Paramedic" "Damn, we don't have time for this. Ian, get her away from him so I can get started!"
        "Paramedic" "Sure."

        show hanako defarms_shock at center behind crowd
        with Dissolve(0.2)

        ha "AAAAAAAAHHH!"
        "Paramedic" "Whoa! Hey, no need to freak out. We're here to help!!"

        show hisao basic_annoy_polo at left
        with charaenter

        hi "Hey! Get your hands off of her!"
        "Paramedic" "What's he saying?"

        show hisao basic_worry_polo at twoleft
        show hanako emb_downtimid
        show crowd behind hanako 
        with charachangealways

        hi "Hanako! Come on, Hanako. I'll get you to our room. Just... there... just come along with me, okay?"

        hide hisao
        hide hanako
        with charaexit

        "Paramedic" "Bruce!"
        "Paramedic" "I'm on it! Neil, get that adrenaline injection ready."
        "Paramedic" "Hey lass, maybe it's better if you go and check up on your... uh... friends."
        "Paramedic" "Lass, you with us?"
        li "Ah, I apologize. I'd... like to stay here if possible."
        "Paramedic" "Just don't get in our way, okay?"
        "Paramedic" "Okay, I'm giving him an adrenaline shot."
        "Paramedic" "Ian, get that defibrillator ready. Hopefully we get lucky and get a shockable rhythm."
        "Paramedic" "Man, what was with that girl? Why did she go nuts like that?"
        "Paramedic" "This is probably her dad. Can't blame her. I've seen worse reactions."
        "Paramedic" "Whadda you think that guy who let us in was saying?"
        "Paramedic" "Dunno, it sounded like Chinese or Japanese. Heck, look at this room. It's completely Asian style."
        "Paramedic" "Neil, one more injection."
        "Paramedic" "Gotcha."
        "Paramedic" "Keep going, people."
        "Paramedic" "Come on, come on!"
        "Paramedic" "Did you guys see that girl? That was one nasty burn on her face. Wonder how she got it."
        "Paramedic" "Hey, keep it down Neil!"
        "Paramedic" "Sorry."
        "Paramedic" "I think I'm getting something."
        "Paramedic" "Keep going, Bruce."
        "Paramedic" "Give him another shot?"
        "Paramedic" "Might not be necessary. Get those electrodes in place!"
        "Paramedic" "Right away!"
        "Paramedic" "That's a beat alright. Ian!"

        play sound sfx_defibrillator_charge

        "Paramedic" "Okay, get back Bruce."
        "Paramedic" "He's all yours."
        "Paramedic" "Clear!"

        play sound sfx_defibrillator_discharge

        pause 2.0

        "Paramedic" "And...?"
        "Paramedic" "One more time."
        "Paramedic" "Clear!"

        play sound sfx_defibrillator_discharge

        pause 2.0

        "Paramedic" "I think we got a pulse. Get the respiratory device and ready the stretcher."
        "Paramedic" "Got it!"
        "Paramedic" "Hey lass. We're about to move out."
        li "W-will my father make it, sir?"
        "Paramedic" "We've done all we can here. It's up to the doctors at Raigmore to make it stick."
        "Paramedic" "Keith! Radio the Emergency Department that we'll be there in 8 minutes."
        "Paramedic" "Right!"
        li "Sir, would it be okay with you if I... came along?"
        "Paramedic" "Only if you come along with us right here and now. We can't wait for you."
        li "I understand."

        stop music fadeout 2.0

        scene bg satou_stairs_blur
        with locationchange

        pause 1

        scene bg satou_entrance_blur_ss
        with locationchange

        pause 1

        stop ambient fadeout 1.0

        scene bg raigmore_ambulance:
            yalign 0.5 zoom 1.02
        with locationchange

        play music music_sadness fadein 4.0

        "I get up and feel out the shoulder of the ambulance worker who addressed me. We hurry outside and he quickly helps me into a seat."
        "I didn't get the opportunity to explain this to Hanako and Hisao, but I'm sure they'll understand."

        show bg raigmore_ambulance_blur:
            yalign 0.5 zoom 1.02
            block:
                ease 0.2 yalign 0.0
                ease 0.2 yalign 1.0
                repeat
        with locationchange

        play ambient sfx_ambulance_close

        "I hurriedly fasten my seat belt as both the engine and the siren spring to life, and the driver sends the ambulance down the driveway and onto the road with a speed that would make Akira's driving seem subdued."

        nvl clear
        nvl show dissolve

        n "During the short ride, I pick up a remark from the amulance driver mentioning we're lucky that our house is so close to the hospital."
        n "A little bit later I hear the voice of someone on the radio giving us the number of the operating room Father will be taken to, but I'm barely able to process all of these things as my brain is still trying to digest what's happening."
        n "{vspace=90}Just a little while ago I was still sitting in the living room, relaxing, talking with my friends and planning our trip to Edinburgh without a care in the world."
        n "How could this suddenly turn into such a nightmare?"

        nvl hide dissolve

        scene bg raigmore_ambulance:
            yalign 0.5 zoom 1.02
        with locationchange

        "My thoughts are interrupted by the ambulance making a sharp turn and coming to a standstill. The ambulance workers quickly get out, and I hear the sound of many voices and many footsteps followed by the sound of a stretcher being pushed down a nearby corridor."
        "The driver then gets out as well, I hear him walk off and then return with someone else in tow."

        stop ambient fadeout 1.0

        scene bg raigmore_entrance_ss
        with locationchange

        "He helps me get out of the car before giving an awkward cough."
        "Paramedic" "I have to get back on the road, but... uh... right in front of you is a nurse who'll be happy to look after you for a bit. Her name's Sally."
        "Nurse" "Hello, Miss. What's your name?"
        li "Ah, L-Lilly. About my father..."
        "Nurse" "They're taking him to the operating room as we speak. We're going to do everything we can to help him, so try not to worry, alright?"
        li "I'll... try."
        "Nurse" "I'm going to take you to the waiting area. We're going to inform you the moment we know more."
        li "Yes, t-thank you."

        play ambient sfx_crowd_indoors fadein 1.0

        scene bg raigmore_waitroom
        show crowd
        with locationchange

        "I place my hand on her arm and let her guide me through several hallways."
        "We finally reach an area where I hear several other people around me."
        "Nurse" "You can wait here. There's a seat right in front of you."
        "Nurse" "Is there anything I can do? Perhaps get you something to drink?"
        "They probably don't have a white cane lying around here. There wasn't time to retrieve my own, and I feel really disorientated and vulnerable in the middle of an unknown environment without even my cane to navigate."
        "No, there's probably no point in asking. But maybe..."
        li "Would it be possible... to make a quick phone call? My sister and my mother don't even know what has happened yet, and I left my own cell phone behind when I came here."
        "Nurse" "If it's just a very quick call, you can make one in our office. Let me take you there."
        li "Thank you."

        stop ambient fadeout 0.5

        scene bg raigmore_office
        with locationchange

        "I'm taken to an office room nearby, and the nurse asks me for the number. I realize that I don't even know Mother's phone number by heart yet, but I fortunately have Akira's cell phone number memorized."
        
        play sound sfx_phonedial

        "The nurse dials the number and then hands me the receiver."

        play sound sfx_phonepickup

        show akira basic_smile_phone at phonebox
        with charaenter

        aki "Good evening, this is Akira Satou speaking."
        "I'm taken back by Akira's formal tone before realizing that she doesn't recognize the number I'm calling from."
        li "A-Akira, it's me."

        show akira basic_cheerful_phone
        with chchange

        aki "Hey Sis, I didn't recognize the number. This isn't the landline at our folks' place, is it?"
        li "I'm at Raigmore right now. The emergency ward."
        li "You... I need you to come over immediately!"

        show akira basic_lost_phone
        with chchange

        aki "The hospital? Sheesh, Lils, what's happened? It's not Hisao, is it? Are you...?"
        li "It's F-Father. I... I don't know what happened. He just... collapsed. The doctor called an ambulance. They're... operating on him right now."
        li "Please Akira..."

        show akira basic_angry_phone
        with chchange

        aki "I'm on my way. I'll be there in 15 minutes."
        li "Please hurry... and call Mother. Let her know to come back here, too."

        hide akira
        with charaexit

        "Akira hangs up, and I hand the phone back to the nurse."
        li "Thank you. Could you... take me back to the waiting area, please?"
        "Nurse" "I will."
    
        if _in_replay:
            return

    label .s3:

        $ set_window_tint(TINT_LILLY)

        play ambient sfx_crowd_indoors fadein 1.0

        scene bg raigmore_waitroom
        show crowd
        with locationchange

        "The nurse takes me back to the seating area and then leaves me alone with my thoughts."

        $ renpy.music.set_volume(0.5, delay=2.0)

        "The voices of other people in the room join the thoughts that whirl around my head."

        show darkness:
            alpha 0.1
        with { "master": Dissolve(1.0) }

        "How could this have happened?"
        mystery "Daddy, it hurts! When can the doctor see us?"

        show darkness:
            alpha 0.2
        with { "master": Dissolve(1.0) }

        "And why?"
        mystery "Just a little while longer, Mary. There are other people here who also need help. Let me get you a glass of water."

        show darkness:
            alpha 0.3
        with { "master": Dissolve(1.0) }

        "Just when I finally had an opportunity to spend time with him."
        mystery "I don't want a glass of water! Why can't we see the doctor now?!"

        show darkness:
            alpha 0.4
        with { "master": Dissolve(1.0) }

        "To get to know him."
        mystery "Hey mommy, that girl sitting over there is staring really strangely."

        show darkness:
            alpha 0.5
        with { "master": Dissolve(1.0) }

        "There were so many things I still wanted to tell him. And ask him."
        mystery "Shush Kevin, don't be rude!"

        show darkness:
            alpha 0.6
        with { "master": Dissolve(1.0) }

        "Will I ever get the opportunity now?"
        mystery "Mister McAdams, the doctor will see you now."

        show darkness:
            alpha 0.7
        with { "master": Dissolve(1.0) }

        "I've never felt so alone and miserable as I'm feeling right now."
        mystery "Thank God. Come on, dear."
        "Father..."
        "Please make it through this."
        "Please."
        "Please..."

        $ renpy.music.set_volume(0.0, delay=5.0, channel="ambient")

        "..."
        "I lower my voice to a whisper."

        show darkness:
            alpha 0.9
        with { "master": Dissolve(5.0) }

        li "{size=*0.8}Our Father in heaven,{/size}"
        li "{size=*0.8}hallowed be your name.{/size}"
        li "{size=*0.8}Your kingdom come, your will be done, on earth, as it is in {i}*sniff*{/i} heaven.{/size}"
        mystery "Doctor, is there any news about my wife?"
        li "{size=*0.8}Give us this day our daily bread,{/size}"
        li "{size=*0.8}and forgive us our debts,{/size}"
        mystery "Please have a bit more patience, sir. My colleagues are doing the best they can."
        li "{size=*0.8}as we also have forgiven our debtors.{/size}"
        li "{size=*0.8}And {i}*sniff*{/i} lead us not into temptation,{/size}"
        li "{size=*0.8}but deliver us from evil.{/size}"

        stop music fadeout 2.0

        mystery "Lilly? Lilly!"

        $ renpy.music.set_volume(1.0, delay=1.0)
        $ renpy.music.set_volume(1.0, delay=1.0, channel="ambient")

        play music music_friendship fadein 4.0

        hide darkness
        show akira basic_lost
        with charaenter

        "A familiar voice suddenly calls out to me and I quickly rise to my feet."
        li "Akira? Akira! Thank God you're here..."

        show akira basic_wistful_close
        with characlose

        "My older sister walks up to me and tenderly wraps her arms around me and, despite me feeling a bit embarrassed about being hugged in public, I feel a sense of relief."
        "How long has it been since Akira last comforted me this way? It must have been quite some time ago, but it still feels as soothing as ever."
        "My loving and reliable big sister who always knew what to do. It feels so good to know she's here now."

        show akira basic_wistful
        with charadistant

        aki "Jeez, you look about ready to faint, Sis."
        "I nod weakly."
        li "I... I'll manage, I hope. I really don't do very well under pressure."
        aki "Let's find ourselves a quiet place to sit down. I noticed a vending machine on my way in here that dispenses drinks. I'll go and get you some."
        li "Yes..."

        stop ambient fadeout 1.0

        scene bg raigmore_entrance_ss
        show akira basic_sweet_ss
        with locationchange

        "Akira takes my arm and guides me down one of the hallways and through a few automatic doors until I feel fresh air on my face. She helps me get to a nearby bench and walks off, only to return later with a paper cup she hands to me."
        aki "I got you some tea. Take care not to burn your tongue."
        "I meekly nod and take a careful sip as Akira sits down next to me and puts an arm around me."

        show akira basic_wistful_close_ss
        with characlose

        aki "Now... Just take a bit of time to get your bearings back, and then tell me what happened."
        li "..."
        "What happened...? That's a good question."
        "Things went so quickly all of a sudden. Two hours ago, I was still planning our upcoming trip with my friends. And now I'm here, wondering if my life will ever be the same again."
        li "He left the office earlier than usual today because he wasn't feeling well..."
        li "By the time he made it home he was already feeling better, so he resumed his work in his study."
        li "I spoke to Mother earlier this evening, and she already said he wasn't feeling well, but apparently Father blamed indigestion and repetitive strain injury in his shoulder."
        li "When he came home, both Hisao and Hanako noted he looked pale, and Hanako even suggested calling a doctor."
        li "Father wouldn't hear of it at first, but then he gave in and allowed me to call his general practitioner."
        li "When I told the doctor about Father, he immediately suggested we take him to see a cardiologist at the hospital. But when I returned to the study..."
        "I sniffle as I recall what happened next."
        li "I found that Father had collapsed while I was away."
        li "Before... he hung up, the doctor said he was going to call an ambulance. And eventually, one arrived."

        show akira basic_sad_close_ss
        with chchange

        aki "Heart attack, huh? You described some of the warning signs just now."
        li "...it seems like it. I suppose the writing has been on the wall all along, and we just didn't pay attention to it until it was too late."

        show akira basic_resigned_close_ss
        with chchange

        aki "It won't be too late if he makes it through, Sis."
        li "I... completely froze up when I found Father lying there. If it hadn't been for Hanako..."

        show akira basic_lost_close_ss
        with chchangefast

        aki "Hanako?"
        li "I believe she performed CPR on him until the ambulance arrived."

        show akira basic_wistful_close_ss
        with chchange

        aki "So that first aid training paid off, huh? Bet she didn't expect someone other than her boyfriend to be the beneficiary."
        li "...I wonder how she and Hisao are doing right now. When the ambulance staff took off with Father, I had no choice but to come along immediately."

        show akira basic_sweet_close_ss
        with chchange

        aki "You can use my cell phone to get in touch with them after I've dropped Mom a little call. It might help to take your mind off things."
        li "Y-you haven't called her yet? W-why not? I...I asked you..."

        show akira basic_lost_close_ss
        with chchange

        aki "Relax, Sis. If you're gonna ask someone to drive all the way back to Inverness from Edinburgh late in the evening, they're gonna demand a reason, and your phone call didn't exactly shed a lot of light on things."
        aki "I figured it was better to come over here first, calm you down a bit and then find out exactly what happened."
        li "You're right. I'm sorry for reacting this way, Akira."

        show akira basic_wistful_close_ss
        with chchange

        "She gives me a pat on the shoulder."
        aki "Don't worry about it, Sis. You've had an extremely frightening experience this evening, so it's understandable that you're still rattled. I don't blame you in the slightest."
        li "Thank you, Akira."

        show akira basic_sweet_ss
        with charadistant

        aki "I'll go and call Mom now. I'll be right back."

        hide akira
        with charaexit

        "Akira walks off again, and I'm left to ponder the situation."

        nvl clear
        nvl show dissolve

        n "Akira's explanation made logical sense, and yet, I still feel I would have acted differently in her place."
        n "I'm really thankful that my older sister's here for me right now, but something has felt a little off."
        # TODO Not sure about this line
        # n "{i}...that my older sister's here for me...{/i}"
        n "{vspace=30}Ever since she arrived, Akira's been the kind, strong and reliable big sister that she's always been for me. The strong person who's lending me her shoulder to lean on. But... how does she feel? She's barely mentioned Father at all. It almost seems like..."
        n "...like she's more worried about me than about him..."
        n "{vspace=30}No, I don't want to think of Akira that way. She's simply keeping a brave face for my benefit right now."
        n "Still, our parents are a very touchy subject for her. I don't think she's completely adapted to the fact that they're suddenly a big part of her life again yet."

        nvl hide dissolve

        show akira basic_resigned_ss
        with charaenter

        aki "Well, Mom's on her way. I told her not to drive like crazy and that I'd call her when we know more."
        li "How did she react?"

        show akira basic_lost_ss
        with chchange

        aki "It's probably still sinking in."

        show akira basic_lost_close_ss
        with characlose

        "She sits down next to me, and we stay like this for a very long time, neither of us saying a word."
        "Eventually, she pushes her cell phone into my hand."

        show akira basic_smile_close_ss
        with chchange

        aki "You know how to operate this thing, don't you?"
        "I think I do. I've used my sister's phone before, and I have Hanako's number memorized."
        li "I do."
        aki "Good. I'll go back inside to see if they already know more. I'll be back soon."

        hide akira
        with charaexit

        "I listen to Akira walking off into the building and prepare to dial Hanako's number when I realize she might already be asleep."
        "This must have been very stressful for her too. I don't want to intrude on her."
        "What if I call my own number first? I left my cell phone in the living room, so they certainly won't be resting if they pick that one up."

        play sound sfx_phonedial

        "I quickly dial the number of my cell phone and cross my fingers that someone'll pick up."

        play sound sfx_phonepickup

        "Eventually, I hear Hisao's voice on the other end of the line."

        show hisao basic_worry_polo_phone at phonebox
        with charaenter

        hi "Ah... Akira... This is Hisao. Lilly isn't here right now, and she left her phone behind. Umm..."
        "I quickly speak up in order to save Hisao from having to come up with a proper explanation."
        li "Hisao, it's me. I'm using Akira's phone."

        show hisao basic_speak_polo_phone
        with chchange

        hi "Lilly... How... is your father?"
        "I let out a depressed sigh."
        li "They're still operating on him as we speak. I'm praying that he's going to make it through."

        show hisao basic_worry_polo_phone
        with chchange

        hi "So are we, Lilly..."
        "Hisao's voice is barely audible, and he sounds extremely tired. I'm obviously not the only one rattled by what happened."
        li "Hisao, how are you and Hanako? Is she there as well?"
        hi "No, she's resting right now. I only got downstairs a few minutes ago. I spent the rest of the time keeping her company and trying to comfort her."
        hi "It took a long time before she was finally able to relax a little. I don't think any of us will be getting much sleep tonight."
        li "Are you doing okay?"

        show hisao basic_speak_polo_phone
        with chchange

        hi "I've been better. This... hit really close to home."
        hi "I was kinda glad I got the opportunity to help Hanako get to our bedroom, because if I had stuck around and watched that emergency team get to work on your father, my own heart might have started acting up as well. I'm still shaking a little even now."
        li "I can imagine how you must feel. How about Hanako?"

        show hisao basic_worry_polo_phone
        with chchange

        hi "Hanako got hit even harder. I mean... Her own parents died in front of her 10 years ago. Heck, I nearly died in front of her as well."
        hi "Whatever memories she's been forced to relive this evening were probably extremely traumatic ones. I haven't been able to get a single word out of her."
        li "And yet... Hanako came through. While I was unable to think of what to do, Hanako did what she could to keep my father alive."
        li "She acted where I couldn't, and I'm extremely proud of her, Hisao."

        show hisao basic_neutral_polo_phone
        with chchange

        hi "Yeah, she acted. But... You didn't see her."
        li "What do you mean?"

        show hisao basic_speak_polo_phone
        with chchange

        hi "On the day that you and Hanako reconciled, I spoke to Hanako's therapist, and she proposed sending Hanako to that training to help her deal with the situation in case my heart gave out again with her nearby."
        hi "I asked her if that was really going to prevent another panic attack, and Miss Takawa said that a panic attack was probably unavoidable."
        li "Then why the training?"
        hi "To delay the anxiety. She believed that as long as Hanako could keep her mind occupied during an emergency and distract herself by performing first aid rather than sitting there and feeling helpless, she'd be able to delay her panic attack."
        hi "I heard that during that training she repeated the CPR procedure until it was almost a reflex to her."
        hi "That's... I think that’s what happened. She was holding off her own panic, in the only way she could."
        hi "She just kept going, maybe even without being aware of what was happening around her. Even when those ambulance workers arrived and told her to let them take over, she just kept going and going."
        li "What happened then?"
        hi "One of those people grabbed her and tried to drag her away from your dad. She reacted very badly to that."

        show hisao basic_worry_polo_phone
        with chchange

        hi "I was able to take her to our room... I'm still not sure how. There, I just held her in my arms—probably for nearly an hour—until she finally stopped trembling."
        "Poor Hanako."
        li "Even if it was just a reflex on her part, I'm still really grateful for what she did, Hisao."

        show hisao basic_neutral_polo_phone
        with chchange

        hi "Yeah."
        "We let out a mutual sigh and remain silent for a long time."
        "I've been so overwhelmed by what happened that I didn't even stop to think how personal this experience must have been for both Hanako and Hisao. My heart goes out to both of them."
        "Suddenly, I hear footsteps approaching, and I feel a hand on my shoulder."

        show akira basic_sweet_ss at twoleft
        with charaenter

        aki "Lilly?"
        li "Akira, do you... have any news?"
        aki "Are you still on the phone?"

        show hisao basic_speak_polo_phone
        with chchange

        hi "Hisao here. I'm still listening, Akira."

        stop music fadeout 2.0

        show akira basic_wistful_close_ss
        with chchange

        aki "I just got word from the doctor."
        aki "They finished the operation. He said it was still too early for a damage report, but they've managed to stabilize him."

        play music music_comfort fadein 4.0

        aki "He'll live, Lilly. And I'm sure he'll be okay, eventually."

        show hisao basic_sweet_polo_phone
        with chchange

        "My last bit of restraint broken, I return the phone to Akira and hold my face in my hands, sobbing uncontrollably—both in order to get rid of the fear, tension, and stress, as well as to express my relief."
        "Akira gives me a gentle squeeze in the shoulder, but doesn't respond."
        "Finally, the silence is broken by Hisao's voice over the phone."
        hi "Thanks Akira. I'm really relieved to hear that."
        hi "I'll... be sure to tell Hanako. Maybe... just maybe... we'll be able to get some sleep tonight after all."

        stop music fadeout 3.0

        scene black
        with endchapter

        if _in_replay:
            return

    return