label sh_ch42:
    label .s1:

        $ set_window_tint(TINT_HANAKO)

        call sisterhood_timeskip_broken
        scene bg school_dormhanako

        play music music_normal fadein 4.0

        ha "Hmmm... Notepad and pen... check."
        "I'll probably end up taking some notes."
        ha "Study books... check."
        "To study in the car. Fortunately I can read just about anywhere without getting motion sickness."
        ha "Lunchbox with extra large lunch... check."
        "They probably have a cafeteria there, but I bet it'll be really crowded, and we'd be standing in line for half an hour. Better to bring my own lunch."
        ha "Pocket change for vending machines... check."
        ha "Sweets for consumption during the trip... check."
        ha "Cell phone... check. Battery's fully charged too."
        "I look at the cell phone lying on my nightstand. I've been using it as an alarm clock ever since Naomi accidentally wrecked my actual one, and I keep putting off buying a new one."
        "It might be a good idea to use both my phone and an actual alarm clock on the day of the exams. Can't be too careful."
        "Did I forget anything? I have my wallet with me. Hmmm, can't think of anything."

        play sound sfx_doorknock

        "A knock on the door interrupts my thoughts."
        ha "It's open!"
        "The door opens behind me, I hear someone walk into the room, and the next moment someone kisses me on my left cheek."

        show hisao cross_sweet_swt_superclose at left
        with charaenter

        hi "Hey there. Good morning."
        "I turn around, kiss my boyfriend back and smile at him."
        ha "Good morning. Did you sleep well?"

        show hisao cross_smile_swt_superclose
        with chchange

        hi "Yeah. And you? Did you stay up late yesterday?"
        "I nod."
        ha "I studied until eleven, but I think I've caught up now."
        "Since Naomi, Jun, and I were busy with our outing the whole Friday evening, I spent most of the Saturday afternoon and evening holed up in my room in an attempt to compensate for the time lost."
        "It practically melted my brains, but I feel I caught up with Hisao and Lilly now."

        show hisao cross_speak_swt_superclose
        with chchange

        hi "You did remember to eat yesterday, right?"
        "I'm not a kid, Hisao."

        show hisao cross_smile_swt_superclose
        with chchange

        ha "Just a quick bite, but enough to keep going."

        show hisao basic_neutral_swt_superclose
        with chchange

        "Hisao looks at my bed and notices something that wasn't there before."

        show hisao cross_sweet_swt_superclose
        with chchange

        hi "Hey, aren't you going to introduce me to your new roommate?"

        show teddybear at displayitemshow

        "I show him the teddy bear that is lying near my pillow."

        show teddybear at displayitem

        ha "I... haven't thought up a name for him yet. But Naomi got it for me from a crane game at the arcade."

        show hisao cross_grin_swt_superclose
        with chchange

        hi "He certainly looks cute. I just hope he'll have the decency to sleep somewhere else when I stay over."
        "I chuckle and nod my head."
        ha "Sure."

        show teddybear at displayitemhide
        with None

        show hisao cross_speak_swt_superclose
        with chchange

        hi "So, have you packed everything for the trip?"

        hide teddybear

        ha "I think so. Is Lilly ready?"

        show hisao cross_smile_swt_superclose
        with chchange

        hi "I saw her outside the dorm just a while ago. I think she's ready to go."
        ha "Let's go outside, then."

        scene bg school_gate
        show lilly back_smileclosed_cas at left
        # TODO replace Hiroyuki sprites with casual outfit
        show hiroyuki serious at twoleft
        with locationchange

        nvl clear
        nvl show dissolve

        n "We leave the dorm building and make our way to the parking lot."
        n "As we approach the gate, we see two tall figures standing nearby. I easily recognize Lilly, but I have to look twice before I recognize the man next to her as her father."
        n "{vspace=30}Of course he's not wearing his business suit today. Instead, he's wearing dark pants and an inconspicuous light-grey vest under his long coat. His glasses are different, too. These ones soften his appearance a bit."
        n "But the biggest difference is his body language. He still looks formal, but I notice his shoulders are a bit more slumped than before, and there's a slightly tired look in his eyes. He also appears to be a bit thinner than before. He looks like he's aged a decade in those few months. I wonder if Lilly is aware of that."

        nvl hide dissolve

        show lilly cane_cheerful_cas
        show hiroyuki bow
        with chchange

        hy "Miss Ikezawa, Mister Nakai. Good morning."
        "He politely bows as we approach, and I notice that his bow towards me is particularly deep."
        ha "Good m-morning, Mister Satou."

        show hisao basic_speak_swt at center
        with charaenter

        hi "Good morning, sir. It's been a while. How are you feeling?"

        show lilly cane_smileclosed_cas
        show hiroyuki thinking
        show hisao basic_neutral_swt
        with chchange

        hy "A lot better, thank you."
        "I'm not sure if I quite believe him. From the few things Lilly has told me, I know that her father's physical recovery has been going fairly well, but he's had a lot of trouble adjusting to life at home and he's quite at a loss what to do with his life now that he no longer has a daily job."
        "Hisao turns to Lilly."

        show hiroyuki serious
        show hisao cross_speak_swt
        with chchange

        hi "Now that we're all here, it might be a good idea to get going. It's still a pretty long ride."

        show hiroyuki eyebrow
        show hisao basic_neutral_swt
        with chchange

        "Lilly's father raises an eyebrow."
        hy "Are we still not one person short?"

        show lilly cane_weaksmile_cas
        show hiroyuki serious
        show hisao cross_speak_swt
        with chchange

        hi "Huh?"

        show naomi bend_laugh at offscreenright
        with None

        show naomi at tworight
        with charamovefastest

        na "Hey guys! I didn't keep you waiting, did I?"
        "Greeting us with a cheerful wave, Naomi comes running up to us."
        hi "Huh? Are you coming along as well?"

        show lilly cane_smile_cas
        show naomi basic_smile
        show hisao cross_neutral_swt
        with chchange

        li "Hanako asked me yesterday if it was okay if she accompanied us. Since we still had room in the car, I saw no reason to refuse."
        "I smile sheepishly at my boyfriend. I did plan to tell him that, but I've barely been out of my room yesterday, and we didn't see each other for very long."
        ha "Sorry I didn't tell you."

        show lilly cane_smileclosed_cas
        show hisao cross_smile_swt
        with chchange

        hi "Eh, it's okay."

        show naomi bend_smile
        with chchange

        "Naomi looks past me at Lilly's father."

        show hisao cross_neutral_swt
        show naomi bend_laugh
        with chchange

        na "You must be Mister Satou. Pleased to meet you. I'm Naomi Inoue."

        show hiroyuki bow
        with chchange

        "Lilly's father answers Naomi's bow with one of his own and introduces himself in return."

        show hiroyuki serious
        show naomi bend_smile
        with chchange

        "Naomi smiles at Lilly's father."
        na "Um... is your wife here too? I'd really like to talk to her again. She's been this really strong motivator for our club. Hehe... both clubs actually."

        show hiroyuki thinking
        with chchange

        "Lilly's father shakes his head."

        show hiroyuki smileclosed
        with chchange

        hy "My wife has been in Scotland this week and is currently on the plane back home. I am afraid that my company will have to suffice for today. I will be sure to give her your regards."

        show lilly cane_weaksmile_cas
        show hisao cross_smile_swt
        show naomi basic_neutral
        show hiroyuki thinking
        with chchange

        na "Awww."
        "Naomi is visibly disappointed, but then gives a resigned nod."
        na "Yeah, that'd be great."

        show lilly cane_smile_cas
        with chchange

        "Lilly tries to give Naomi an encouraging smile."
        li "I'm certain you'll be able to talk to her again. She'll be present for our graduation after all."

        hide lilly
        hide hisao
        hide hiroyuki
        hide naomi
        with charaexit

        "And with that consolation, we head for the car and hit the road."

        if _in_replay:
            return
        else:
            stop music fadeout 2.0

    label .s2:

        $ set_window_tint(TINT_HANAKO)

        scene bg satou_hiroyukicar at top
        with shorttimeskip

        queue music music_another fadein 4.0

        ha "Ummm... Anybody want another piece of chocolate?"

        show lilly basic_smile_cas at twoleft
        show hiroyuki neutral at tworight
        with charaenter

        li "That sounds good. Thank you Hanako."
        "This is probably the third round of chocolates we've gone through already, but it's been quite a long ride, and we've got to keep our brains in top gear so we can keep studying."
        "Well, at least that's true for Lilly, Naomi, and me. Hisao's just looking out the window."
        li "Hisao, do you often get car sick if you read on the road?"

        hide lilly
        hide hiroyuki
        with charaexit

        show carseats at center:
            ypos 1.2 alpha 0.0
        with None

        show bg at bottom


        hi "Sometimes I do, sometimes I don't. I remember when my father drove me to Yamaku, I was reading pretty much the entire way there, and that was the same route as we're driving right now."
        "Lilly's father raises an eyebrow and looks at Hisao through his rearview mirror."
        hy "I take it then that you are originally from Chiba? Are you planning to move back into your parental home?"
        hi "That's the idea. Living five minutes away from school is a luxury I'm going to miss, but I have my own room at home, and my parents work long hours, so I'd at least have some extra privacy."
        "Naomi grins."
        na "Eh, you shouldn't see it as a lack of privacy. You ought to see life at the dorms as a good way to meet lots of interesting new people with whom you might not interact as much if you weren't living on campus."
        na "Heck, they say that university years are the party years of your life. Not that I can go overboard with parties myself of course, but I bet it'll still be awesome."
        "Sounds like somebody is looking forward to her time as a university student. I am not so eager to move accommodations myself."
        ha "I'm... not really a party p-person myself, but..."
        "There was Lilly's proposal, but I wonder just how much chance she has of changing her father's mind."
        li "Father, do you remember that conversation we had previously about... accommodations?"
        hy "I do. But is now really the proper time to bring that up again?"
        li "Would you be willing to reconsider if a person like Hanako moved in as a roommate to keep an eye out?"
        hy "A person like Miss Ikezawa or Miss Ikezawa herself?"
        li "Hanako herself. I... ah... have reason to believe she'd be interested in the opportunity if it was presented to her."
        "I can see his eyes giving me a long analyzing look that sincerely unnerves me."
        hy "Miss Ikezawa, is that so?"
        ha "Y-Yes... ummm... sir."
        hy "You are not merely saying that because it would convenience my daughter, are you?"
        ha "N-No. I'm... not very good with people, so... having a bit m-more space and only having to s-share the facilities with my best friend would be very convenient for me too."
        "Lilly's father furrows his brow as if weighing every word I just said."
        hy "Hmmm..."
        hi "Sir?"
        "I look at my boyfriend who's remained quiet during this discussion and now suddenly speaks up."
        hy "Yes, Mister Nakai?"
        hi "Would you mind if I shared something with you that caught my attention about this?"
        hy "By all means."
        hi "I don't think sharing a place with a blind person is something that works out well for everyone. If you're sloppy by nature and leave stuff lying about or don't put things back in exactly the place where you found them, you'll usually make things harder rather than easier for your roommate."
        hy "That makes sense."
        hi "But I've seen Lilly and Hanako prepare a meal together a few times in the past and they seem to have a system in place between the two of them that allows them to work almost in perfect unison."
        hi "Hanako seems to know exactly how to arrange things so that Lilly can easily find them, and she's always very meticulous about putting things back in exactly the right place when she borrows stuff from Lilly's cupboard."
        hi "I don't think it's an exaggeration when I say that Hanako is easily the best roommate Lilly could ever wish for."
        "I blush from this unexpected avalanche of praise. It's true that I'm somewhat used to Lilly's preferences related to chores and cooking, but I don't consider that trait to be nearly as impressive as Hisao is making it out to be."
        "Lilly, on the other hand, smiles and gives an appreciative nod."
        li "I could not agree more with that assessment, Hisao."
        "I kind of wonder if this is going to make any difference whatsoever. I'm not really sure how useful I would be to Lilly in everyday life once she's memorized the layout of the apartment and the neighborhood."
        "I don't think of myself as an extremely reliable safety net, and if Mister Satou's not willing to rent an apartment for his daughter, what are the odds of him wanting to do the same for a relative stranger. Unless..."
        "A realization suddenly dawns on me."
        "Unless he felt he owed that person something. Didn't he say before that if I ever needed anything, I only needed to ask? If he's serious about that and he knows that I'd like having a small place of my own together with Lilly, would he refuse? Could he?"
        "Wait a second... Is Lilly counting on that? Is that why...?"
        "No, Lilly seemed genuinely happy when I said I'd like to be her roommate. I believe she sincerely desires my company. I also don't think she'd like it if an obligation to me was the only reason her father would allow her to live on her own."
        "But even so, Lilly's employing a pretty devious strategy, and when I look at Mister Satou, I notice that he opens his mouth to say something, but then merely sighs, shakes his head and gives his daughter a long, hard look."
        hy "It appears that you inherited your negotiation tactics from your mother. Well, if you want me to take all of this into account and reevaluate my opinion, I am willing to do so, but I cannot make any promises."
        li "Thank you Father. I greatly appreciate it."

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return

    label .s3:

        $ set_window_tint(TINT_HANAKO)

        play music music_pearly fadein 4.0
        scene bg kasshoku_campusentrance
        show crowd
        show lilly cane_smileclosed_cas at left
        show hiroyuki serious at twoleft
        show naomi basic_smile at tworight
        show hisao basic_speak_swt at right

        hi "Wow, it's really big. I hope I won't get lost here."

        show lilly cane_smile_cas
        show hisao basic_neutral_swt
        with chchange

        li "Could you describe it to me, Hisao?"

        show lilly cane_displeased_cas
        show hisao basic_speak_swt
        with chchange

        hi "If the map we're looking at is any indication, this place is the size of a city block."

        show hisao basic_neutral_swt
        with chchange

        li "Have you already located the places we're supposed to be heading for?"

        show lilly cane_displeased_cas
        show hisao cross_speak_swt
        with chchange

        hi "Let's see. You and your father have to be in the building on the northwest side of the campus. The faculty building I'm heading for is located on the east side and Hanako and Naomi are set for the building just to the north of here. Geez, we're spread all over the place."

        show lilly cane_weaksmile_cas
        show hisao cross_neutral_swt
        with chchange

        li "Seeing that we're all applying for different studies, it's no surprise we're set to visit different faculties."

        show hiroyuki thinking
        show lilly cane_smileclosed_cas
        show hisao basic_neutral_swt
        show naomi basic_neutral
        with chchange

        hy "I propose that we meet up back here at the entrance after we are finished for the day."

        show hisao cross_speak_swt
        with chchange

        hi "At what time should we be back here?"

        show hiroyuki speak
        show lilly cane_smile_cas
        show hisao basic_smile_swt
        show naomi basic_smile
        with chchange

        hy "I have looked up the day's program online and I believe it ends at half past 3. So I suggest we meet back here at four o' clock."
        "At least somebody came prepared. Since I spent most of yesterday cramming for the upcoming mock exams, I didn't even think of looking up today's schedule. And it seems like the same is true for the rest of us."
        hi "Fine by me."
        na "Sure."
        ha "O-Okay."

        show hiroyuki serious
        show lilly back_smile_cas
        with chchange

        "Lilly gently takes her father's arm."
        li "We'll return here at four o' clock then. Shall we be off then? Have fun everyone."

        show hiroyuki bow
        pause 0.7
        show hiroyuki thinking
        with chchange
        hide lilly
        hide hiroyuki

        "Lilly's father bows to us and then walks off into the crowd together with his daughter. Hisao looks me over before picking up his backpack."

        show hisao basic_worry_swt
        show naomi basic_neutral at center
        with charamove

        hi "Are you going to be okay?"

        "Looks like he picked up on my nervous mood. Over the course of last week, I've kept telling myself that I'd be okay today, since I've lately been able to walk Yamaku's hallways with only some mild discomfort every now and then."
        "Looks like I've been fooling myself into thinking it'd be that easy. Ever since we've passed the gate, I've been feeling an unusually oppressive atmosphere."

        ha "Y-Yes, I'm okay."

        show hisao cross_speak_swt
        show naomi basic_smile
        with chchange

        hi "Keep an eye on her, okay?"

        show hisao cross_neutral_swt
        show naomi basic_grinclosed
        with chchange

        "Naomi rolls her eyes at Hisao."
        na "Geez, have a little faith. We'll be just fine."

        show hisao basic_sweet_swt
        show naomi basic_grinclosed
        with chchange

        hi "Well, good luck today."
        ha "Y-You too."

        hide hisao

        "I sigh softly as I watch my boyfriend disappear into the mass of people. Naomi picks up her backpack from the floor and gestures towards the buildings ahead of us."

        show naomi bend_wink_close
        with chchange

        na "Shall we go too?"
        ha "N-Not too fast, please."

        scene bg kasshoku_campusgrounds
        show crowd
        show naomi basic_smile_close at center

        "I take a deep breath and then we start making our way through the crowd. I make sure to keep to Naomi's left side and stick as close to her as possible while keeping my head down."

        scene bg kasshoku_journalismentryhall
        show crowd
        show naomi basic_smile_close at center

        "When we finally reach the entrance to our building, Naomi grabs two pamphlets from a desk near the door and hands one of them to me. I fold it open and look at its contents."

        nvl clear
        nvl show dissolve

        n "Information sessions and presentations: (start every 45 minutes. 9:15 - 15:15)"
        n "{vspace=30}- History of journalism (classroom 1-1)"
        n "- Journalistic writing (classroom 1-2)"
        n "- Research and analysis (classroom 1-3)"
        n "- Researching media and culture (classroom 2-1)"
        n "- Advanced reporting (classroom 2-2)"
        n "- Political reporting (classroom 2-3)"
        n "- The media and popular culture (classroom 2-5)"

        n "{vspace=30}Closing session: (15:30 - 16:00)"
        n "- The internet, social media and the future of journalism (lecture hall 1)"

        nvl clear
        nvl hide dissolve

        show naomi basic_focus_close
        with chchange

        na "Information sessions, huh? They're probably kinda like ordinary class sessions we can attend if there's still room."
        ha "P-Probably."

        show naomi bend_wink_close
        with chchange

        na "So, any special requests?"
        ha "No. You?"

        show naomi bend_laugh
        with chchange

        na "Let's check out 'Research and analysis' first."

        "I nod and we go off to find classroom 1-3 where the lecture about that particular subject is being given using the map on the back of the pamphlet as a guide."

        scene bg kasshoku_journalismhallway
        show crowd
        show naomi basic_smile at left
        pause 1.0
        show naomi bend_smile
        with chchange

        "As we reach the classroom, Naomi looks inside."

        na "Swell, there's like 4 seats left. Shall we?"

        show naomi bend_smile_close
        with chchange

        "I cautiously peek into the room from behind Naomi. There are indeed a few seats left, but they're all on the left side of the room. If I sit there, everyone will probably be able to see my scars."
        ha "Ummm... What about t-the classroom next t-to this one?"

        show naomi basic_neutral_close
        with chchange

        na "Huh?"
        ha "We c-could do this one later."

        show naomi basic_confused_close
        with chchange

        "Naomi looks puzzled for a second and then shrugs her shoulders."

        show naomi basic_neutral_close
        with chchange

        na "Well, okay."

        scene bg kasshoku_journalismclassroom1
        show crowd
        show naomi basic_smile_close at right
        with charaenter

        "Classroom 1-2 fortunately has several more vacant seats, and I make my way to the back of the classroom as quickly as I can. Naomi hurriedly moves to the seat next to mine."
        "I feel guilty about forcing Naomi to put up with this. The last thing I wanted was to throw her into the babysitter's role."
        "The next 45 minutes are mostly spent listening to a long story about what makes a well-written article, but I'm having trouble taking notes due to the thoughts whirling around in my head."

        nvl clear
        nvl show dissolve

        n "I've been a bit antsy over the course of the week, but for the most part I've been able to keep myself from getting too worked up about it. I actually felt fine this morning, but the moment we reached the campus entrance my agoraphobia almost immediately kicked in."
        n "{vspace=30}Despite Yamaku's campus being far from small, the school itself is definitely not very large and houses only around 250 students or so, so things are usually rather peaceful aside from the hallways and cafeteria during lunch break."
        n "{vspace=30}It's such a contrast to this place which is both massive and crowded. Especially the classrooms are a lot larger and more crowded here. It reminds me a bit of my middle school, and I'm not so sure whether that's a good thing."

        nvl clear
        nvl hide dissolve

        "Finally, the teacher in front of the class looks like he's finishing up his story."

        show naomi basic_neutral_close at tworight
        with charamove

        "I instinctively start gathering my stuff and prepare to quickly slip out of the room, but before I can get up I see Naomi subtly shaking her head at me, and I realize that I just stopped short of making a huge mistake."
        "While the teachers at Yamaku were informed of some of my circumstances and tolerated my tendency to leave class early in order to avoid the crowds, I don't think there'll be such leniency here."

        show naomi basic_sheepish_close
        with chchange

        "I merely would have made a spectacle out of myself. That would have been disasterous. I quickly give a nod of understanding and put my backpack back down before I attract anyone's attention."

        scene bg kasshoku_journalismhallway
        show crowd
        show naomi basic_smile_close at twoleft
        with charaenter

        "We wait until other people rise from their seats, and then I quickly get out of the classroom with Naomi in tow. After we get a safe distance away from the classroom entrance, Naomi turns to me and points down the hallway."

        show naomi basic_smileclosed_close
        with chchange

        na "Want to try 'Research and analysis' again? We might have more seats to choose from this time."
        ha "O-Okay."

        show naomi bend_smile_close at center
        with charamove

        "We quickly head over to classroom 1-3, which is still in the process of emptying. As the stream of people moves past us, I hurriedly hide behind Naomi, which is only partially effective since I'm a bit taller than her."

        scene black
        with Dissolve(2.0)

        "Eventually people stop coming out of the classroom, and Naomi and I both carefully walk inside. Naomi gives a little nod with her head."
        na "Are we going for a spot on the right in the back again?"
        ha "Y-Yes please."

        if _in_replay:
            return

    label .s4:

        $ set_window_tint(TINT_HANAKO)

        play music music_soothing fadein 4.0
        scene bg kasshoku_trackbleachers
        show naomi basic_neutral_close at tworight

        na "Are you sure that this is okay?"
        "Naomi looks a bit uncertain upon taking her half of my lunch from my hands."
        ha "Sure. I p-packed a very large lunch anyway. It's too much for me to eat all by myself."

        show naomi basic_smileclosed_close
        with chchange

        na "Well, okay then. Thanks a lot."
        ha "N-Not a problem."

        show naomi basic_smile_close
        with chchange

        nvl clear
        nvl show dissolve

        n "So far we've been to three of the presentations that were offered, and the faculty's program for the day has a window of 45 minutes reserved for lunch break, meaning we still have about half an hour before we have to return to the faculty building."
        n "{vspace=30}I, for one, really welcome this opportunity to get a little break. Naomi wanted to drop by the cafeteria at first, but I managed to convince her to go and find a quiet and secluded spot for us to eat our lunch."
        n "{vspace=30}Naomi didn't bring any lunch herself, probably counting on getting to buy her lunch around here, but I got her to abandon that idea by promising her half of my lunch. Fortunately I already anticipated the possibility of Naomi not bringing a lunch of her own, and I prepared a particularly large lunch myself this morning, so neither of us is in danger of going hungry."

        nvl clear
        nvl hide dissolve

        show naomi basic_neutral_close
        with chchange

        na "The sky's kinda cloudy though. If it starts raining, we'll have to run back or we'll get soaked."
        ha "Do you... want to go b-back already?"

        show naomi basic_smileclosed_close
        with chchange

        "Naomi shakes her head."
        na "I take it that you had a reason for coming here, and I don't mind either way, so we're better off staying here for a while longer."
        "'Here' being the spot I picked after we left the faculty. It's a bench near the sports field a few minutes walk away from the journalism faculty. Since there are barely any other people around here, this spot feels nice and safe."
        ha "T-Thanks."

        show naomi basic_sad_close
        with chchange

        "Naomi gives me a worried glance."
        na "I... uh... know that this whole trip was to gain inspiration and motivation for the upcoming exams, but you're looking neither inspired nor motivated right now."

        nvl clear
        nvl show dissolve

        n "I answer Naomi's words with a sad nod. Looks like even she picked up on it. I'm so disappointed in myself right now. I should be motivated and inspired."
        n "{vspace=30}This is the school I've applied for. The school that Hisao, Lilly and probably even Naomi will be attending. The first choice I've put on my application form at Yamaku. The one chance I have to easily stay in contact with my best friends and keep my relationship with Hisao going."
        n "{vspace=30}Despite the fact that I can't afford to let my anxieties take control of me, the massiveness, crowdedness and unfamiliarity of this place started getting to me the moment I set foot in here. Naomi gives me a sheepish look."

        nvl clear
        nvl hide dissolve


        show naomi basic_sheepish_close
        with chchange

        na "You really don't like crowds, do you?"
        ha "I don't like it... when p-people look at me. Or ask me about... you know. So I t-try not to be in p-places with lots of people."

        show naomi basic_neutral_close
        with chchange

        "Naomi nods understandingly."
        na "Yeah, that makes sense. If it's a consolation to you, I'm not fond of large crowds either. I prefer smaller groups of people to big masses."
        ha "You?"

        show naomi basic_sheepish_close
        with chchange

        na "Surprised?"
        "A bit. Naomi's a pretty social girl who has an easy time interacting with others, and her bleached hair draws way less attention than my facial scarring. Of course, her epileptic seizures make even my scars seem inconspicious."
        ha "Because of y-your... ah...?"

        show naomi bend_grin_close
        with chchange

        na "...fits."

        "I awkwardly nod as Naomi bluntly finishes my sentence. Naomi acts about as easygoing about her epilepsy as Lilly does about her blindness, at least most of the time, but I'm not completely comfortable discussing the subject with her yet."

        show naomi basic_serious_close
        with chchange

        na "Hmmm. Have you ever heard of the 'bystander effect'?"
        "I shake my head."
        na "Put simply it means that the more people are nearby when something bad happens to you, the less likely they are to do something."
        na "If you have a seizure while there are like one or two people nearby, they're very likely to do whatever they can to help. If the same thing happens, and there are 40 people nearby, all they usually do is stand there and stare."
        na "Nobody likes to risk screwing up in front of others, so nobody lifts a finger even while you're banging your head against the pavement and suffer a concussion as a result."

        show naomi basic_annoy_close
        with chchange

        "The brief bitter glint in Naomi's eyes suggests that she might not have made that example up just now."

        show naomi basic_neutral_close
        with chchange

        na "Anyway, I mostly go into town with others for that reason. This isn't a problem when I'm with Natsume or you and Jun since you know how to act when I short out, which is a real load off my mind."
        ha "Uhhh... You... really feel better while we're around?"

        "It seems Naomi has more faith in me than I have. If she has a seizure in a public spot, and there are 40 people looking at her, that would also mean there'd be 40 people looking at me."
        "And 40 people looking in my direction may just be enough to shut me down too. That'd leave Jun, and I'd rather not let her near Naomi while the latter is thrashing around on the floor."

        show naomi basic_sheepish_close
        with chchange

        na "Yeah, I do. By the way... I didn't remember you being so high-strung two days ago, and the part of town we were in was kind of busy too."
        "There's a pretty big difference between the streets of the city and the hallways of the building we've spent the last few hours in."
        "While I'm not completely comfortable walking through the city either, it helps when I remind myself that I never have to be on the streets for very long and that I can relax once I reach my destination."
        "This place, however, will be where I will be spending the next years of my life from morning until afternoon. If I'm going to feel on edge all day long, how will I even function?"
        ha "It... probably helped that it was rather d-dark while we were there, and I... know my way around that part of the c-city a bit."

        show naomi basic_sad_close
        with chchange

        "Naomi looks at me with a worried frown as she reads my expression."
        na "Were you hiding your anxiety and merely pretending to have fun? You weren't, were you?"
        ha "N-No, not at all. I... really liked the day before yesterday."
        "That's not a white lie. After our get-together in town, Naomi, Jun and I took the bus to the city where we first had a great meal in a quiet little sushi restaurant."
        "Then we went for a 2-hour long karaoke session until all three of us became a bit hoarse. And finally, after hearing that the arcade was a favored spot for Hisao and me to spend our dates, Jun dragged me there to engage in some competitive gaming sessions."
        "Our little outing felt different from the dates I went on with Hisao or the girl-dates I undertook with Lilly. But despite the different group dynamic, I can honestly say I had a lot of fun that evening and went to bed with a smile that night."

        show naomi bend_smile_close
        with chchange

        na "Really?"
        ha "Yes, really."

        show naomi basic_smileclosed_close
        with chchange

        na "I also had fun. It was pretty enlightening too. I never would have guessed you to have such a nice singing voice. Or Jun to be that crazy about video games."
        "I blush at Naomi's praise."
        ha "Jun... didn't really surprise me that much. She likes computers, after all."

        show naomi basic_grin_close
        with chchange

        na "Heh, yeah, but I don't think every girl who merely 'likes computers' acts like a kid in a candystore when you take her to the arcade."
        "I giggle. I don't think I could have described Jun's disposition more perfectly than Naomi just did."
        na "I think... she simply doesn't have many other f-friends who like to play games... particularly video games."

        show naomi basic_sheepish_close
        with chchange

        ha "Makes me wish I could have been there all the time."
        "Naomi reasoned that a darkened arcade hall filled with flashing displays was a very bad place for an epileptic to be, so she waited for Jun and me in the entrance hall."
        "At first we were worried that she was going to be bored out of her mind, but after we finished our gaming binge, we actually found her in the company of no less than three large plush animals she procurred from the nearby crane games."
        ha "But then... we wouldn't have those nice plush toys you won for us."

        show naomi basic_grinclosed_close
        with chchange

        "Naomi grins proudly."
        na "And don't you forget it."

        nvl clear
        nvl show dissolve

        n "On the way back I asked Naomi if she was interested in coming along today."
        n "{vspace=30}I felt a bit bad that a not unimportant reason for bringing her along was the fact that I expected my anxieties to get the better of me if I had to attend this event completely on my own, and there's no way I could have asked Lilly or Hisao to skip their events and come along with me just so I could hide behind them."

        nvl clear
        nvl hide dissolve

        ha "I won't. And ah... Thanks again for c-coming along today."

        show naomi bend_wink_close
        with chchange

        na "I'm enjoying myself here, so don't sweat it. Besides, it's the least I can do back for someone who lets me stay over every once in a while."

        "Two weeks ago, Naomi had another seizure during a session of our writing club although she thankfully didn't mess up my blanket this time, and we let her spend the night in my bed again. Natsume joked the day after that maybe Naomi ought to start paying me rent."
        ha "That's... okay."

        show naomi basic_sheepish_close
        with chchange

        "Conversation dries up, and we finish our lunch without making further small talk. I feel my nerves slowly easing although I'm not sure how long that is going to last. As Naomi suggests going back, I quickly check my watch. It's nearly one o' clock. Only three more hours to go. I can do this."

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return

    label .s5:

        $ set_window_tint(TINT_HANAKO)

        play music music_dreamy fadein 4.0
        scene bg kasshoku_journalismclassroom2
        show crowd
        show naomi basic_neutral_close at right

        "Teacher" "...and many of the people now covering our politicians are alumni from this school."
        "I try to take a casual glance at my watch without making it too obvious that I'm checking the time. It's 15:10 right now. Only five more minutes."
        "We arrived fairly late, and most seats were already taken, but since this was the only presentation we hadn't attended yet we couldn't just skip it and visit another one."

        show black:
            alpha 0.2
        with Dissolve(1.0)

        "We're sitting right in the middle of class right now, and I'm having the impression that the person on my right, a slightly thin-looking girl with a silver-colored hairpin is staring past my bangs."

        show black:
            alpha 0.3
        with Dissolve(1.0)

        "In fact, I can almost swear half the class is watching me, but I'm afraid to turn my head. I consider covering the right side of my face with my hand, but that will only make the scarring on the back of my hand more noticable."
        "Teacher" "There's also the matter of several political leaders in the Liberal Democratic Party as well as some in the Democratic Party of Japan and the Japan Restoration Party being graduates of this university."
        "Teacher" "This creates a bond that can be used to your advantage to improve your working relationship with the politician you're assigned to cover..."
        "I've been on my guard ever since we returned here from our lunch break, and I'm feeling drained right now."
        "Teacher" "Since Kasshoku has good ties with the five largest newspapers in the country, graduates of this school will have a good chance to get into the various kisha clubs you need to be part of in order to have direct access to the members of our legislature."
        "I've only been able to pick up fragments of this last presentation, so I really hope Naomi's been taking notes."
        "Teacher" "...and there's information about Japanese kisha clubs obtainable online for those of you who wish to learn more. That is all for today. In 15 minutes, the faculty head will close off today's events with one last presentation in the hall one floor down. We are hoping to see all of you there."

        hide crowd
        hide black
        show naomi basic_annoy_close at center
        with charamove

        "As the teacher finishes and people start getting up, I breathe a sigh of relief. Eventually the teacher follows his audience out the door, leaving just Naomi and me in the classroom. Naomi walks up to me with an annoyed expression on her face."
        na "Man, I thought political reporting was gonna be awesome, but from what that guy just said, I get the impression that it pretty much involves working your butt off to get put in a club, get assigned to one politician and then repeating the exact same press releases that everyone else in your group is getting."
        na "That's kind of boring, not to mention a pain."

        show naomi basic_grin_close
        with chchange

        na "Heh, what if I actually made it into the exclusive group of journalists assigned to covering one of the bigwigs and then shorted out? Can you see the headlines? 'Female reporter chews up prime minister's sofa during epileptic fit?' That'd be kind of awesome."

        show naomi basic_grinclosed_close
        with chchange

        "If that actually happened, I don't think she'd be laughing anymore. I merely shrug my shoulders at Naomi's remark."

        show naomi basic_smile_close
        with chchange

        ha "We'd b-better get going."

        show naomi bend_wink_close
        with chchange

        na "Right. I doubt that hall is going to run out of seats anytime soon, but we'd better not press our luck."
        ha "Eh... hall?"

        show naomi basic_confused_close
        with chchange

        na "Yeah, they're gonna tie the whole thing up in that lecture hall in 15 minutes, aren't they? That's what that guy said. It's on the program too."

        show naomi basic_neutral_close
        with chchange

        ha "B-But... We were g-going to meet at the entrance at four o' clock. If we attend that last p-presentation, won't we be late?"
        "I didn't think about it before, but it seems our program finishes later than Lilly's. Looks like every faculty here has made its own schedule for today without worrying about the others."
        na "Only a bit. The campus entrance isn't that far from here. If we return there now, we'll be sitting there twirling our thumbs for like 40 minutes."
        "I personally wouldn't mind that much. We have our study books with us, and there are some benches there."
        ha "But... They might g-get worried."

        show naomi basic_sheepish_close
        with chchange

        na "Only if they make it there before we do. The other faculty buildings are farther away from the entrance than ours is, and from what I saw earlier today, Lilly and her dad have a very slow walking pace."
        na "If we set a brisk pace for ourselves after we finish the program here, I bet we could still get to the meeting point before they do."

        nvl clear
        nvl show dissolve

        n "Naomi does have a point. While Lilly and her father are the punctual type, they do have a rather slow pace, and knowing them, both will probably try to take it easy for the sake of the other."
        n "{vspace=30}While I'm not fond of the idea of attending yet another presentation in a probably crowded room, Naomi seems eager to attend it, so the best I can do is probably to go along with her suggestion as a way to thank her for coming along with me today and putting up with my nervousness without complaining even once."

        nvl clear
        nvl hide dissolve

        ha "Well... O-okay then."

        show naomi basic_smileclosed_close
        with chchange

        na "Great. We'd better get a move on before they run out of seats."
        scene bg kasshoku_journalismentryhall
        show naomi basic_smile at center
        with charaenter

        "We quickly leave the empty classroom, and I'm relieved to find out that the hallways are a lot emptier right now than they've been the whole day. As we reach the bottom of the stairway, Naomi points to a stream of people trinkling into a room through a set of double doors."

        show naomi bend_smile_close
        with chchange

        na "That's where we need to be."
        "We hurriedly join the small crowd and make our way into the hall beyond the doorway."

        scene bg kasshoku_journalismlecturehall
        show crowd
        show naomi basic_neutral_close at center
        with charaenter

        "Upon passing through the doors though, I let out a horrified gasp and instinctively move behind Naomi as I find out why the hallways were so empty just now."
        "The hall we've just entered is huge and filled almost completely with people already, leaving only the occasional empty seat here and there."
        "The first thought that enters my mind is how much of a mistake it was to come here. No matter how interesting this lecture is going to be, I don't think any of it will end up sticking in my mind."
        ha "Uhh..."

        show naomi basic_sad_close
        with chchange

        "Naomi turns around and looks at me with an uncertain expression."
        na "Erm..."
        ha "I'll... be... okay."

        show naomi basic_neutral_close
        with chchange

        "I doubt Naomi believes me, but she nevertheless nods, and we walk up to the rows of seats that still have vacant spots. Naomi suddenly stops and points at one of the empty seats."

        show naomi basic_sheepish_close
        with chchange

        na "I think this is a good spot for you."
        "It's a seat at the very end of one of the rows. Merely being surrounded by people on three rather than four sides might make the experience just a little less harrowing for me, but since it's only a single seat that means Naomi will be sitting somewhere else."

        show naomi basic_sheepish
        with chchange

        "I give Naomi an uncertain glance, but then nod and sit down after shoving my backpack under my seat."

        show naomi basic_sheepish at offscreenright
        with charamove
        hide naomi

        "The person sitting next to me still appears to be in a conversation with his neighbor and didn't pay attention to me when I sat down next to him, so I pull up my collar a bit and pray he doesn't take a closer look at me."

        nvl clear
        nvl show dissolve

        n "Ugh, I hate crowds. Is this the place where I'll be getting the majority of my courses if I end up enrolling here?"
        n "{vspace=30}I take a careful look over my shoulder to see where Naomi is sitting. It takes a bit of effort, but I eventually manage to spot her thanks to her bleached hairdo standing out among the mostly dark-haired crowd."
        n "{vspace=30}She's sitting in the middle of one of the rows near the back of the hall, quite a distance away from me. It makes me feel even more isolated here."

        nvl clear
        nvl hide dissolve

        "I notice that the stream of people flowing into the hall has dried up, and one of the people standing near the doorway, a slightly older gentleman, closes the doors and activates the large screen on the back wall before walking up to the microphone."

        play music music_night fadein 4.0

        "Lecturer" "I would like to welcome you all for taking time out of your busy schedule to visit us today. We hope you have been finding your visit educational and enjoyable so far..."
        "I check my watch again. 25 more minutes to go. Just 25 more minutes. I catch the person sitting next to me taking a peek at my right hand and quickly cover it with my left."

        scene black
        with Dissolve(2.0)
        scene bg kasshoku_journalismlecturehall
        show crowd

        "Lecturer" "...and there are some who say that the rise of the internet will spell an end to newspapers and possibly even journalism."
        "Lecturer" "Let me say that one of these claims is an exaggeration and the other one is untrue. Newspaper readership is still extremely high in our country, newspapers will always continue to exist in some form or another and journalism maintains its role in society as it always has..."

        "20 more minutes to go. I notice that the person next to me is whispering to his neighbor. I wonder if they're talking about me."

        scene black
        with Dissolve(2.0)
        scene bg kasshoku_journalismlecturehall
        show crowd
        show black:
            alpha 0.2
        with Dissolve(1.0)

        "Lecturer" "...news organisations will have to get used to no longer being the ones to have the scoop on images of unexpected events as random passersby will often use their cell phone to take a picture of these events as they witness them and upload it to their weblog."
        "Lecturer" "But there is more to news than a picture of an event as it takes place..."

        show black:
            alpha 0.3
        with Dissolve(1.0)

        "15 more minutes. I wonder what Lilly and Hisao are doing right now. Are they already waiting for us? No, it's still too soon. I hope we can quickly get out of here when this lecture is over. Being in the room with so many other people is slowly getting to me."
        "I don't recall feeling this way when Hisao and I went to see movies, but then again we'd usually try for the smaller theaters, and we'd always go and see movies that had been out for some time so we'd know in advance the theater wouldn't be filled to the brim."
        "It helped that it was usually dark too. And that Hisao was nearby. I wish Naomi was sitting closer."

        scene black
        with Dissolve(2.0)
        scene bg kasshoku_journalismlecturehall
        show crowd
        show black:
            alpha 0.3
        with Dissolve(1.0)

        "Lecturer" "...it is up to the reporter to provide the big picture of events through investigative journalism."
        "Lecturer" "A random witness may help the world see the where and when of an event, but the public will always turn to the true journalist for answers on questions that eyewitnesses cannot answer such as why and how..."

        show black:
            alpha 0.4
        with Dissolve(1.0)

        "10 more minutes. I wonder if closing my eyes will make a difference. If I can't see the crowd all around me... No, the idea that someone could be staring at me without me being aware of it is even more maddening."

        scene black
        with Dissolve(2.0)
        scene bg kasshoku_journalismlecturehall
        show crowd
        show black:
            alpha 0.4
        with Dissolve(1.0)

        "Lecturer" "...of course, there is no need to take my word for it. If you take a look at the statistics of the last decade, you can see that they follow the trend that was just discussed."
        "The man in front of the microphone stops speaking and uses his remote control to show a series of slides containing graphs and numbers. He slowly and quietly runs through the slides, pausing after each one to give the information time to sink in."

        "7 more minutes. I hope Hisao and Lilly had a good time. Maybe they have been inspired by today and their enthusiasm will find its way back to me."
        "I think when we get back I'll just let Naomi recount today's events for us. She's been having a good time today, aside from having to put up with my nervousness."
        "Yes, that's a good idea. I smile a bit to myself. If Naomi, Lilly and Hisao all had a good time and are enthusiastic about today, I'll surely feel a lot better as well by the time we're back at Yamaku."
        stop music

        play sound sfx_phonering
        queue sound sfx_phonering
        queue sound sfx_phonering
        "I could even..."

        "My thoughts are suddenly interrupted by the loud noise of a cell phone piercing the silence in the hall, and I can see the speaker turning his head towards his audience."
        "A sense of foreboding sneaks into the pit of my stomach as I realize that that sound came from somewhere awfully close and that sensation is replaced by a feeling of pure dread when it dawns on me why."

        play music music_tension

        scene ev fatefulcall_realisationzoomedinmax

        "THAT'S MY CELL PHONE THAT'S RINGING!"

        queue sound sfx_phonering
        queue sound sfx_phonering
        queue sound sfx_phonering

        "My phone! I've been so focussed on keeping my anxiety under control today that I completely forgot to turn it off. I can see the speaker sweeping the rows of seats with his gaze, annoyed that someone interrupted his lecture."

        queue sound sfx_phonering
        queue sound sfx_phonering
        queue sound sfx_phonering

        scene ev fatefulcall_coverfacerightzoomedinmax

        "I hastily reach down to open my backpack, but as I do so I suddenly become aware that my neighbor is looking at me. Not merely a quick glance, but he's LOOKING STRAIGHT AT ME. My hand instinctively flies up again to cover the scarring on my face."

        play ambient sfx_heartslow loop
        queue sound sfx_phonering
        queue sound sfx_phonering
        queue sound sfx_phonering

        "I can see one of the people sitting in front of me slowly turning around, and when the full realisation of what's happening right now hits me, I feel a sudden and painfully tight sensation in my chest as if my rib cage is rapidly shrinking and squeezing my heart and lungs until they're ready to pop."

        queue sound sfx_phonering
        queue sound sfx_phonering
        queue sound sfx_phonering

        "I need to turn it off. I need to turn it off right now!"

        scene ev fatefulcall_openbackpackleftzoomedinmax
        show black:
            alpha 0.3

        "I frantically reach down with my free hand to open the backpack under my seat and get my phone out, but my hand movements have suddenly become jerky and shaky from the stress and I'm struggling to even get hold of the zipper."

        queue sound sfx_phonering
        queue sound sfx_phonering
        queue sound sfx_phonering

        scene ev fatefulcall_openbackpackleftzoomedoutfar

        "One by one, more heads are starting to turn in my general direction as the ringing sound mercilessly continues."

        queue sound sfx_phonering
        queue sound sfx_phonering
        queue sound sfx_phonering

        "Whoever you are, stop it! Stop it already! What did I do to you? Stop it, stop it, PLEASE!"
        "The pain in my chest is becoming nearly unbearable, and despite my frantic breathing, it's like the oxygen in the room is slowly disappearing."

        scene ev fatefulcall_coverfaceleft
        show black:
            alpha 0.5

        "I realize that people may be noticing the scar tissue on my hand and I quickly switch hands, using my left hand to hide as much of my face as I can while desperately trying to open my backpack with my right hand."

        queue sound sfx_phonering
        queue sound sfx_phonering
        queue sound sfx_phonering

        "More and more people are starting to turn around, and I feel as if their gazes are piercing right through my hand, mercilessly taking in and appraising my damaged features."

        scene ev fatefulcall_paniczoomedinmax
        show black:
            alpha 0.1

        "Don't look at me please don't look at me quit looking at me STOP LOOKING AT ME!"

        "I'm feverishly tugging at the zipper of my backpack in an attempt to get it open, but my shaking hands and the sudden stiffness in my fingers make that almost impossible. I might be able to open it if I use two hands, but I'm too frightened to move my other hand away from my scarred face."

        play sound sfx_impact
        with vpunch
        queue sound sfx_phonering
        queue sound sfx_phonering
        queue sound sfx_phonering

        "In a sudden act of despair I suddenly kick my backpack with the heel of my foot, aiming for where I believe my cell phone is located."
        "A little voice in the back of my head, presumably the voice of my quickly dwindling rationality, asks me what the hell I'm doing to something that I usually consider valuable."
        "It's true that I normally consider my phone, itself a present from Lilly and the attached phone strap a gift from Hisao, a valuable possession. But in the current situation that dreadful object is my worst enemy in the world. Just when I prepare for another frantic kick..."

        scene ev fatefulcall_coverfaceleft
        stop ambient
        stop music
        stop sound
        show black:
            alpha 0.2

        "...the ringing suddenly stops. An almost unnatural silence follows as I realize that despite the fact that that cursed contraption is no longer ringing, I'm still at the center of attention right now."

        play ambient sfx_heartslow loop
        show black:
            alpha 0.4

        "Despite the pain in my chest and my head, despite the feeling of terror that's nearly overwhelming me and despite the fact that I'm having real difficulty breathing, I sit completely still without moving a muscle, without blinking, without breathing, my hand still covering the right side of my face."
        "I feel like a cornered rabbit being eyed by a predator who's been pursuing me and who is now considering whether I'm tasty enough to be ripped to pieces."
        "Continue the lecture continue the lecture please I'll never ask for anything else in my life just don't put me through this again."
        "I see the man holding the presentation looking down at his notes and extending his hand to the microphone and I prepare to say a silent prayer of relief, but before he can resume his lecture..."

        stop ambient
        play ambient sfx_heartfast loop
        play music music_tragic
        queue sound sfx_phonering
        queue sound sfx_phonering
        queue sound sfx_phonering
        show black:
            alpha 0.6

        "...the infernal sound resumes, destroying what little hope I had left to get out of this in one piece. The tight, squeezing sensation in my chest immediately returns, worse than before."

        scene ev fatefulcall_cryzoomedoutfar

        "More and more gazes are trained upon me and hear a few soft chuckles in the distance that set the hair of my neck on end. I squeeze my eyes shut, but can't prevent tears of fear from flowing down my cheeks."

        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow

        "Ever since that house fire permanently disfigured me, I've been uncomfortable around crowds of people. Every time I had to get near one, I expected someone to call out 'Look at her face!' and then everyone would turn towards me and gasp in horror."
        "Hisao, Lilly and Miss Yumi always said that that was never going to happen, yet it's exactly what's happening right now and it's a million times worse than it ever was in my imagination."

        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow

        scene ev fatefulcall_coverbothhandszoomedoutfar
        show black:
            alpha 0.4

        "And the most frightening part of all is that I can feel that this is going to get even worse. I can barely breathe, my heartbeat is both frantic and unsteady, and it's getting harder to think straight with every passing second."
        "First fear about dying or passing out, followed by fear about not dying or passing out. I can feel a pressure building up from within, and the prospect of that pressure eventually getting released in one way or another in front of everyone here terrifies me more than anything else."
        "And I know I won't be able to stop it when I reach that point."

        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow

        show black:
            alpha 0.1

        "I manage to suppress a crazed giggle with supreme effort. My mind is growing increasingly irrational and the sense of panic has driven it to a point where I feel that it's about ready to snap."

        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow

        "I don't know what's going to happen, but something will happen if this keeps up. Maybe I'll faint and everyone here will gather around me to take a close look at me. Or maybe I'll go crazy and start screaming or laughing like a lunatic."

        show black:
            alpha 0.2

        "Or maybe it'll be something even worse. That thought makes me even more frightened than I already am."

        scene ev fatefulcall_approachingzoomedinmax
        show black:
            alpha 0.7

        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow

        "I have to get out of here I have to get out of here now."

        show black:
            alpha 0.2

        "I can faintly sense someone walking down the aisle and approaching me from behind. They've spotted me. Someone's getting closer, and he'll point me out to the rest and it'll all be over for me."

        show black:
            alpha 0.6

        "Stay away from me don't look at me get away from me!"

        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        show black:
            alpha 0.1

        "The footsteps are getting even closer."

        show black:
            alpha 0.8

        "I have to get out of here I have to get out of here!"

        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        show black:
            alpha 0.2

        "I struggle to regain control of my body and maintain what little grip on my sanity I still have."

        show black:
            alpha 0.5

        "I have to get out of here I have to get out of here!"

        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_heartslow
        queue sound sfx_phonering
        queue sound sfx_heartslow

        show black:
            alpha 0.1

        "LET ME OUT OF HERE!"

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return

    return
