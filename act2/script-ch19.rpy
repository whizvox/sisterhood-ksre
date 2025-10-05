label sh_ch19:
    label .s1:

        $ set_window_tint(TINT_HANAKO)

        call sisterhood_timeskip

        scene bg school_hallway2
        with nextchapter

        play music music_normal fadein 4.0

        "I look from the form in my hand to the room number on the small metal sign next to the door several times to make certain I have the right classroom."
        "I'm nervous enough as it is, and accidentally walking into the wrong room and getting caught in a crossfire of glances would probably kill my resolve to make it through the day outright."
        "Today is the first day of my first aid training, and although Miss Yumi gave me some general information, I have absolutely no idea what to expect."
        "Telling myself that vacation has started and if I got the wrong classroom, it'll probably just be empty, I open the door a bit and carefully peek inside."

        play sound sfx_dooropen

        scene bg school_firstaidclass:
            yalign 0.5 zoom 1.02
        with locationchange

        "The first thing that draws my attention is the fact most of the desks and chairs have been moved to one corner of the room except for a handful of chairs that are positioned in a row near a flip chart, a beamer and several large bags that look remarkably like body bags."
        "The second thing is that there are four people here already. I can see two men I don't recognize talking to each other near the window and two teachers, a fit-looking man whom I recall being a PE teacher and a woman with short hair, sitting on the chairs near the beamer."
        "I tiptoe into the room, trying hard not to attract attention, and approach the chair at the far right end of the row."
        "Before I can sit down, the short-haired woman—whom I recognize as Lilly's homeroom teacher and our English teacher—notices me, frowns, and walks up to me."
        "Miyagi" "Good morning Ikezawa. Do you have business with someone here?"
        "I softly shake my head at her."
        ha "Is t-there a f-f-first aid t-training here t-today?"
        "Miyagi" "As a matter of fact there is. Why?"
        ha "I'm p-participating t-too."
        "The teacher looks puzzled."
        "Miyagi" "Are you certain about that? These courses are for staff members only."
        "I meekly nod."
        ha "M-Miss Takawa s-said she arranged it."
        "The woman frowns again, then concludes this probably isn't her business to worry about, sits down again, and resumes her conversation with her colleague."
        "I sit down, take a library book out of my bag, and try to read a few pages in order to calm my nerves."
        "Two more people enter. One is another person I don't recognize, but who is enthusiastically greeted by the two men who were talking near the window."
        "The other is somewhat overweight, has silver-gray hair, and wears a colorful tie. He sits down on the chair next to me and greets me with a grin that makes me flinch."

        show nakamura neutral
        with charaenter

        "Just as I prepare to open my book again and use it to hide behind, a man in his mid thirties comes walking in with what appears to be another bodybag in his arms and a big backpack over his shoulder."
        "He gets to our corner of the classroom, puts the bag and backpack on the floor, checks his watch and then walks up to the door and closes it. He walks over to us again, clears his throat and then makes a polite bow which we return."

        show nakamura smile
        with chchange

        nak_ "Good morning everyone. I see it's nine o' clock right now, so I suggest we simply start now even though we're still one person short."
        nak_ "Allow me to introduce myself: my name is Kensuke Nakamura, and I am a first aid trainer employed at the nearby hospital. This is the fourth year I've been giving these courses here."

        show nakamura speak
        with chchange

        nak "The course planned for this week has been scheduled to take up five days, mostly because I intend to try and give all of you plenty of opportunity for additional practice, which is what we'll be concentrating on in the last two days."
        nak "Those of you who have participated in my training before and are merely brushing up can get by with only attending here until Wednesday."
        "I wonder how many of this group will remain after the first three days. I suppose private lessons on Thursday and Friday would be too much to hope for."
        nak "Let me start by checking who's in attendance right now. Fujimoto."
        "Fujimoto" "Yes."
        nak "Hamasaki."
        "Hamasaki" "In attendance."
        "Those names don't ring a bell. They're probably administrative staff."
        nak "Ikezawa, filling in for Takawa."
        "I quietly raise my left hand to indicate my presence. As I do so, I can see Lilly's homeroom teacher giving me a nod and a smile from the corner of my eye."
        nak "Inaba."
        "Inaba" "Yes."
        "Somebody else working at the administration? He seemed to be friends with the other two I didn't recognize."
        nak "Miyagi."
        "Miyagi" "Attending."
        nak "Nishihama."
        "Nishihama" "Yes."
        nak "Nomiya."
        no "Good to see you again."

        show nakamura instruct
        with chchange

        nak "Well, that seems to be everyone for now. Before I start with the first subject, let me lay out the topics we'll be covering in the upcoming days as well as the day-to-day schedule."

        hide nakamura
        with charaexit

        "Nakamura opens his backpack and takes several ring binders out of it, giving one to each of us. Thumbing through my own, I see a myriad of illustrations, photos and accompanying text."
        "I get a bit queasy when my eye catches a photo of a particularly nasty open wound. Not everything here is material suitable for reading during lunch."

        show nakamura smile
        with charaenter

        nak "I'll start by introducing you to my associates and your practice partners for the upcoming days."

        show nakamura:
            xalign 0.9
        with charamove

        "The trainer gives a wink and then walks over to the large bags he lugged in here not too long ago. He opens them, and I can see I wasn't really far off the mark when I likened the bags to body bags."
        "Inside each bag is a large practice dummy, about the size of a regular person, each of them fully clothed."
        nak "Unfortunately, I don't have enough of them for each of you to have your own dummy, so we're going to be working in pairs. Or rather, one group of three and two pairs."

        hide nakamura
        with charaexit

        "We're getting to a part that I really hate: making groups. Ever since elementary school, this has meant that other people make groups, and I'm the leftover that people reluctantly take if it suits them."
        "I see the three people who greeted each other at the beginning of class bunching together, meaning the trio's already a done deal. Next, I see the PE teacher who was talking to Miss Miyagi earlier give her a playful nudge that she responds to with a quick nod."

        show nomiya talk at twoleft
        with chchange

        "In less than five seconds, the groups seem to have been determined already. And my practice partner, the flamboyant art teacher, approaches me with a smile that feels part jolly and part predatory to me."

        show nomiya at center
        with charamove

        no "It seems you're stuck with me for the upcoming days. If you have any questions, just ask. I've followed this training several times in the past, so none of these things are new to me. I'm sure we'll work well with one another."
        "I'm not quite so sure. He's friendly and enthusiastic alright, but something about him makes me extremely uncomfortable. If this wasn't for Hisao's sake, this might have been the moment where I'd have bolted from the room."

        show nomiya veryhappy
        with chchange

        no "So, you're one of Takawa's wards, aren't you? Is this some sort of alternative therapy she's experimenting with?"
        "He laughs just a little bit too loudly at his own remark, but I find myself cringing."
        "Of course, everyone in the room who knows Miss Yumi's occupation probably figured out my relationship with her in an instant, but I'm not particularly proud of the fact that I need therapy sessions, and I don't like it when other people bring them up."

        hide nomiya
        show nakamura speak
        with chchange

        "Mister Nakamura scrapes his throat and everyone sits down again."
        nak "Very well. Now that we've made pairings, I'd like to give a quick summary of what we'll be doing the upcoming days."

        show nakamura instruct
        with chchange

        nak "We're going to start with some general instructions on how to act in an emergency situation and what actions to avoid. We'll also get into the practice of checking for vital signs."
        "My mind wanders briefly, revisiting that moment when Hisao was lying on the street in front of me and I couldn't move a muscle."
        "Will this whole training make a difference? Will I even remember what's being taught here when faced with the pressure of a real life emergency?"
        nak "Next up is one of the most prominent parts: how to perform CPR on someone and how to handle the artificial respiration that's part of it. We'll make sure to get plenty of practice in with the dummies I have here."
        "I wasn't exactly thinking clearly that time. What if something happens again, and I fail to recall what I'm being taught here? Won't that make me feel like an even bigger failure?"
        nak "Tomorrow we'll start with instructions on emergency treatment of wounds. I will talk about how to stop extensive bleeding and how to limit the risk of infections."

        show nakamura smile
        with chchange

        "He chuckles for a moment."
        nak "I hope nobody's prone to fainting spells when they see blood."
        "I think I'll be okay."

        show nakamura neutral
        with chchange

        nak "After that, we'll move on to emergency treatment of… erm…"
        "Strangely enough, Nakamura doesn't finish his sentence and seems unsure on how to proceed."
        "As I look at the others I can tell that I'm not the only one who's puzzled as to why he's suddenly stumbling at what should be an easy summary for anyone who's ever given a training before."
        ha "(…the emergency treatment of…?)"
        "The trainer seems lost in thought for a moment, then gives a short shrug and proceeds."

        stop music fadeout 2.0

        nak "Ahem. After ordinary wound treatment, we'll cover the emergency treatment of burn injuries."

        play music music_tension fadein 2.0

        hide nakamura
        show black:
            yalign 0.5 zoom 1.02 alpha 0.5
        show n_vignette:
            yalign 0.5 zoom 1.02 alpha 0.8
        with dissolve

        "I feel a sharp shock slam through my body as if someone just walked up to me and pounded me in the chest with a sledgehammer, and I spring to my feet as if someone just hammered a nail through the bottom of my seat, my eyes widening in shock."
        "No wonder he was lost on how to continue. He was trying to figure out how he's going to spend an hour detailing the various degrees of burn wounds all the while a miserable exhibit A is sitting right in front of him."
        "Of course, my reaction draws the attention of the rest, merely contributing to the sense of panic that starts welling up inside me."
        "As my hands start shaking uncontrollably, I am gripped by one all-consuming thought."
        "{i}I have to get out of here!{/i}"
        "Struggling to stay on my feet, I manage to stammer the only thing that pops into my head as I head for the exit…"
        ha "I… I… have… to go do something!"

        play sound sfx_impact
        with vpunch

        stop music fadeout 2.0

        "…only to nearly collide with someone who seems to be in as much of a hurry to get into the room as I am to get out of it."

        hide black
        hide n_vignette
        show yuuko cry_down
        with dissolve

        yu "I'M SORRY!"

        play music music_running fadein 2.0

        "Taken aback by this person's sudden entrance, I stare in bewilderment as she makes an apologetic bow that's almost deep enough for her nose to touch her toes."
        yu "I found out this morning that I put the keys to the library in the wrong person's pigeon hole,{w=0.5}{nw}"
        yu "so my replacement for this week couldn't get the library doors open until we tracked down the person who had my keys,{w=0.5}{nw}"
        yu "and when we found him he told us he just dropped the keys back in my own pigeon hole, and…{w=0.5}{nw}"
        "For a few seconds the entire room is silent as everyone is trying to digest what just happened, and for a moment, I'm too confused to remember I was in the middle of an attempt to flee the room in terror."
        "As the woman in front of me lifts her head, I'm surprised to see a familiar face."
        ha "Y-Yuuko?"

        show yuuko panic_up
        with chchange

        yu "Hanako? What are you doing here? Isn't there supposed to be a first aid training for Yamaku staff here?"
        "Suddenly, a panicked expression appears on her face."

        show yuuko neurotic_up
        with chchange

        yu "I didn't just barge into the wrong room again, did I? It's happened to me before."
        ha "Ummm… N-no."
        "A soft chuckle from one of the others breaks the awkward silence in the room and a moment later, I can hear our trainer walk up behind me."

        show nakamura smile at tworight
        with charaenter

        nak "Welcome Shirakawa. Good of you to join us. Please take a seat. I was just giving a brief summary of the topics we'll be covering this week."

        hide yuuko
        with charaexit

        "Making another apologizing bow to Mister Nakamura, Yuuko nervously walks past me and takes a seat on one of the empty chairs."

        show nakamura neutral
        with chchange

        "Instead of walking back to his spot, Mister Nakamura softly addresses me."

        stop music fadeout 2.0

        nak "Can I have a moment, Ikezawa?"

        hide nakamura
        with charaexit

        play sound sfx_dooropen

        "Without waiting for an answer, he walks out the door and beckons me to follow him."

        scene bg school_hallway2
        show nakamura bow
        with locationchange

        play music music_nurse fadein 4.0

        "After we're both outside earshot range of the others, he makes an apologizing bow very much like Yuuko's."
        nak "I'm sorry for what just happened before Miss Shirakawa showed up. I suppose this is what people would call an oversight. I wasn't quite sure how to handle it. Miss Takawa explained your situation to me, but didn't share a lot of information about you."
        "I merely nod my head, not sure how to react to his statement. Apparently, Miss Yumi didn't mention to him that I'm a burn victim."

        show nakamura neutral
        with chchange

        nak "I can understand why an information session about the subject I just spoke of would be extremely awkward for you to attend."
        nak "Unfortunately, if I want the certificates we hand out at the end of the training to have any value whatsoever, I will have no choice but to cover the entire program. I cannot ignore that fact."
        ha "I… understand."
        "I certainly wouldn't want him to pander to my problems by skipping a major portion of his training. Besides, if he were to end up skipping that part, it'd be immediately obvious to everyone but Yuuko why he did it."

        show nakamura speak
        with chchange

        nak "So here's what I'd like to propose: I'm going to shift the order of the lessons so the course about burns is the last thing I'll be covering tomorrow. Before we get there, we'll be taking a short break and that's where you can call it a day."
        nak "On Thursday or Friday, when only the first-timers remain, I'll take the opportunity to give you a short private lesson about the part that you missed while the rest practices the material we've been covering."
        ha "Is t-that… okay?"
        nak "I think it's a bit early to throw in the towel. Walking away might seem tempting right now, but you might feel bad about it if you ever get involved in a situation where the knowledge I'm looking to impart this week can make a difference."
        "That's a good point. If I opt out now and Hisao has another episode in my presence in the future, I don't think I'd ever be able to forgive myself."
        ha "O-okay then."

        show nakamura smile
        with chchange

        stop music fadeout 2.0

        nak "Good. Let's head back inside and get things back on track."

        play sound sfx_doorclose

        scene bg school_firstaidclass
        show nakamura neutral
        with locationchange

        queue music music_daily fadein 4.0

        "I follow him back into the classroom and return to my seat. Mister Nakamura doesn't waste any time picking up where he left off."

        show nakamura instruct
        with chchange

        nak "Getting back to this week's material, the next part we'll be covering will be what to do in cases of exposure to toxic substances. On Wednesday, we'll spend some time on cases involving bone and joint injuries as well as how to act in case someone's choking."
        nak "Finally, I'll go over a variety of situations involving specific medical conditions such as epileptic seizures, diabetic emergencies, and allergic reactions."
        "That last part sounds rather interesting, seeing that I currently have an epileptic as editor-in-chief."
        nak "Seeing that all eight of you are currently here, we can split into four pairs and we'll have just enough dummies for each group to use one."
        "I can see one of the people who formed a group of three head towards Yuuko, who turns to Mister Nakamura and raises her hand."

        show yuuko smile_down:
            xalign 0.9
        with charaenter

        yu "Teacher, would it be okay with you if I paired up with Ikezawa? We know each other fairly well."
        nak "If she's okay with that, I am too."

        hide nakamura
        with charaexit

        "I breathe a quiet sigh of relief and quickly nod my head. The art teacher gives an indifferent shrug and then walks over to Yuuko's initial partner."
        "Nakamura takes the practice dummies out of their bags and carries three of them to a different corner of the room and then puts one in the center."

        show yuuko neutral_up at center
        with charachangealways

        "As Yuuko and I walk to one corner, I give her a grateful look."
        ha "Umm… thanks."

        show yuuko smile_up
        with chchange

        yu "When I came in, that person who was going to pair up with me was chuckling at me. Since I'm a bit accident prone, I'd like a partner who isn't going to laugh at me when I screw up."
        "She gives me a wink."

        show yuuko happy_up
        with chchange

        yu "Also, Nomiya's nice enough, but he creeps me out a bit, so…"
        "I give her a small smile. Truth be told, I'm often at a loss on how to handle Yuuko's erratic mood swings, but currently there's no other person in the room I'd rather be paired up with."
        "It feels comforting to know I'll be working with someone who won't judge me for my skittish behavior. I suppose it feels good for her as well to pair up with someone who won't judge her."

        hide yuuko
        with charaexit

        "As we sit down on the floor next to the dummy, Nakamura walks to the center of the classroom."

        show nakamura speak
        with charaenter

        nak "Before we start the first part, I'd like to hold a short introduction."
        
        show nakamura instruct
        with chchange

        nak "What we teach here won't make you a perfect substitute for a doctor or a trained nurse. The goal of first aid in case of an emergency is to stabilize the victim until professional help arrives."
        nak "Therefore, have your cell phone with you and call the ambulance before tending to the victim, or let someone else on the scene make the call."
        nak "Well-meaning attempts by non-trained civilians to help an injured person—for example, by moving the injured person after a traffic accident or removing a puncturing object from a wound—have been known to make matters worse."
        nak "If you ever see someone trying to help in such a way, make sure to stop them quickly and tell them that you've received first-responders training."
        "He looks around the classroom."
        nak "So, in short, in case of an accident or if anybody collapses in front of you, there are three simple steps. One, always call an ambulance. Two, check for vital signs, and do a quick checkup to see what can be done to stabilize a person's condition."
        nak "Three, perform the appropriate actions while waiting for the ambulance to arrive, and don't leave an injured person alone."

        show nakamura neutral:
            ypos 1.1
        with charamovechangefaster

        "Beckoning us to watch his actions, he kneels down next to the dummy in the center of the room and places his fingers on its left wrist."
        nak "First thing to do in case of an emergency is to see if the person is still responding and check for vital signs if that's not the case. Specifically, the victim's pulse and whether or not he's still breathing."
        nak "We can check a person's pulse by putting two fingers on this spot right here just beneath the victim's wrist joint. Or we can go for the spot here at the throat."
        "Pausing for a bit to make sure we all got the point, he then carefully moves the dummy's arm and leg a bit before rolling it on its side."
        nak "If the person has a pulse and is breathing, you'll want to put them in the recovery position like this. This'll make certain the victim can't suffocate on his own tongue or whatever it is he recently ate that might get vomitted back out."
        nak "Always watch the head. And be sure to remove or loosen any pieces of clothing that might hamper breathing."

        show nakamura smile:
            ypos 1.0
        with charamovechangefaster

        "He gets up and cracks his knuckles."
        nak "Let's practice these actions for a few minutes. I'll walk around and give feedback where necessary. Once everybody's got it right, we'll move on to CPR, which is the interesting part and…"
        "He takes out a green bag with the picture of a thunderbolt on top of a heart in the middle and the letters SMT in one corner."
        nak "…we'll break up the practice with a demonstration on how to use a defibrillator."

        hide nakamura
        with charaexit

        "Yuuko and I exchange a glance."

        show yuuko neutral_down
        with charaenter

        yu "Do you want to go first?"
        "I give a quick nod back."

        stop music fadeout 2.0

        ha "O-okay."

        scene bg school_firstaidclass
        show yuuko neurotic_down at tworight
        show nakamura neutral at twoleft
        with shorttimeskip

        queue music music_tranquil fadein 4.0

        yu "{i}*huff*{/i} {i}*huff*{/i} {i}*huff*{/i}"
        nak "Two minutes this time, Shirakawa."

        show yuuko worried_up
        with chchange

        "Yuuko looks up at the trainer while rubbing her arms."
        yu "I-is that good or bad?"

        show nakamura
        with chchange

        nak "It depends on whether the paramedics have already arrived on the scene or not. Movies like to pretend CPR involves pushing a victim's chest a few times and then they cough and get up good as new. But spontanous revivals are rare occurrances."
        nak "In reality, you're supposed to keep going until the ambulance arrives or you're too exhausted to continue."
        "It's that last part that actually has me terrified. I already know what it felt like to just sit there and be unable to do anything while Hisao was slipping away from me."
        "I don't ever, ever want to find out what it feels like to have some paramedic tell me they could have saved Hisao's life if I would have only lasted one more minute."
        nak "You were doing well, Ikezawa. Though you were probably a little bit too gentle. I don't think those were compressions of 5 centimeters. Try pressing deeper the next time."
        nak "Remember: if a victim complains about his ribs hurting afterwards, it means you've done something right."
        ha "I-I'll try."

        hide yuuko
        show nakamura smile at center
        with charachangealways

        play sound sfx_clap

        "Nakamura gives a friendly nod and then claps his hands in order to get everyone's attention."

        show nakamura speak
        with chchange

        nak "I think that's enough for now, people. You can review the material we've covered today by reading page 4 until page 32 of the binder I gave you."
        nak "For those of you interested in testing your aptitude on the various subjects, I'll have a few small optional written tests you can take on Thursday and Friday."
        nak "Let's call it a day for now. No need to worry about the dummies, I'll put them away myself later."

        hide nakamura
        with charaexit

        "As I get up, I rub my sore arms. Those CPR practice sessions really made me wish I was more atlethic."
        "Still, aside from the rough start this morning, I think I learned a lot of valuable things. And Yuuko proved to be a pleasant, although panic-prone, partner."

        scene bg school_hallway2
        show yuuko happy_down
        with locationchange

        "As we leave the classroom, she gives me a comforting smile."
        yu "Will you be here tomorrow too?"
        ha "Y-yes."

        hide yuuko
        with charaexit

        "Checking the time, I conclude that Hisao's probably still at the science club. I consider going to the library to kill some time, but then decide to drop by the newspaper club first."

        stop music fadeout 2.0

        "Seeing that summer break has already started, I don't expect there to be much activity, but I still need to know if I missed anything important."

        if _in_replay:
            return

    label .s2:

        $ set_window_tint(TINT_HANAKO)

        scene bg school_newspaper
        show natsume hands_smile
        show naomi basic_smile at tworight
        show jun cast_smile at twoleft
        with locationskip

        play music music_another fadein 4.0
        
        # TODO Simplify description of Jun
        "As I slowly open the door to the classroom that's home to our club and peek inside, I can see Naomi and Natsume relaxing and sharing some drinks with a tall, frail-looking girl with long, brown hair."
        
        nvl clear
        nvl show dissolve
        
        n "The girl, whose name is Jun Yamazaki, is the club member whom I was initially drafted to replace for a little while as assistent editor."

        show natsume hands_cheerful
        show naomi bend_smile
        show jun cast_happy
        with { "master": charachangealways }

        n "{vspace=60}As I enter, I'm greeted by three friendly waves, Jun's being emphasized by the white orthopedic cast around her hand."
        n "{vspace=30}Jun, a second year student here, is one of the reasons the computer lab is almost never completely deserted. She's a bit of a whiz kid whose knack for computers far exceeds my own, and she joined the newspaper club for the specific purpose of getting to do the editing jobs. Last week, we ended up working together a few times to put the latest issue of the school newspaper together. I'm not completely comfortable around her yet, but due to her skinny build and her usually quiet demeanor, her presence is not exactly threatening, either."
        n "When I was first invited into the club, I learned that Jun suffers from osteoporosis and is very prone to breaking bones as a result of minor falls that other people would simply shrug off."

        nvl hide dissolve

        show naomi bend_laugh
        with chchange

        na "Hey there, Hanako. All done for today? How was the training? What did you learn?"
        "As usual, Naomi's quick to fire off a verbal torrent of questions."
        ha "It was pretty useful. We learned about… ummm… checking someone's pulse and doing CPR."

        show naomi basic_smile
        show natsume hands_smile
        show jun cast_smile
        with chchange

        na "Any familiar faces there?"
        ha "Yuuko was there. And ummm… Miyagi. And Fujimoto. And erm… N-Nomiya as well."

        show naomi bend_grin
        with chchange

        "Naomi throws me a mischievious wink."
        na "Soooo… Did you guys have to practice mouth-to-mouth breathing? On each other? Did you see any teachers doing it?"

        show naomi bend_laugh
        show natsume basic_neutral
        show jun cast_annoyed
        with chchange

        "My eyes grow wide in disturbed shock at the mental image that Naomi's remark conjures up, but it's apparently highly amusing to her, for she bursts into giggles after a short moment of silence."
        ha "N-no… ummm…"
        "As I struggle to figure out how to respond to Naomi's inane suggestion, I notice how Natsume and Jun both shoot her a dirty glare."
        nt "Will you… please stop… polluting my brain with that kind of stuff?"
        "Natsume's scolding doesn't really seem to impress Naomi as she giggles at her own joke."
        na "Oh, come on. I thought it was funny."

        show jun cast_smile
        with chchange

        "Jun turns to me."
        jun "They have big dolls for that kind of thing, don't they?"
        "I sigh in relief at Jun's attempt to steer the subject in a different direction."
        ha "Y-yes. Practice dummies. We… used them t-to practice CPR, too."

        show naomi basic_neutral
        with chchange

        "Naomi, apparently deciding to drop the previous subject, gives a quick nod."
        na "Sounds like your day was more interesting than ours. We ended up sharing the distribution duties with the student council."
        na "When we finished printing the last issue and dropped everything off at the council room, we caught Hakamichi in the middle of packing for summer break. She insisted we help out in order to guarantee everyone got a copy in time."
        ha "W-wasn't the printing supposed to take place later this week?"

        show jun cast_serious
        with chchange

        na "According to the official schedule, yeah. Practically speaking, waiting that long would have been really stupid."
        ha "How so?"
        "Naomi shrugs casually."
        na "Well, summer break started this week."
        na "Right now, lots of students are still busy tying up loose ends and packing their bags, but I'm betting that within a smatter of days, nearly half of the student body will have gone home for the summer, and this school will be one hell of a lot emptier."
        na "Meaning that half our batch would just end up gathering dust. But now, we got people a copy just before they're leaving here…"
        ha "…they're likely to take it along, so they h-have something to read during the trip back home."

        show naomi basic_laugh
        with chchange

        "Naomi smiles, pleased that I picked up on her train of thought."
        na "Bingo."

        show natsume hands_smile
        with chchange

        "Natsume fiddles with her glasses for a moment."
        nt "I'll be here until Wednesday. Naomi said she and Jun will be heading home the upcoming weekend."
        na "Yup, so if you need to unwind from the whole changing-bandages-and-compressing-chests thing, you know where to find us."
        ha "Ummm… Thanks."

        hide naomi
        hide jun
        show natsume hands_smile_close at center
        with charachangealways

        "As I turn to leave the room, Natsume gets up and hands me four copies of the latest edition—three ordinary ones and one with larger font for visually impaired students."
        nt "While we were out there handing out newspapers, Naomi deliberately skipped the science club. She thought you'd want to be the one to hand them the latest issue."

        scene bg school_scienceroom
        show muto smile
        with locationskip

        "I haven't seen Mutou smile very often; I think he looks a bit strange when he does."
        "And as I hand him one of the newspapers I've brought along, which he very eagerly takes, his expression almost becomes a grin."

        hide muto
        show hisao basic_neutral_uni at twoleft
        show kenji happy
        with charachangealways

        "Feeling a bit unnerved by it, I quickly turn to Hisao who was working on a sophisticated-looking circuit diagram together with Kenji until I came into the room."

        show hisao cross_neutral_uni
        with chchange

        hi "What's got him so excited?"
        "Hisao, unlike Kenji, has noticed Mutou's expression who's now gleefully thumbing through the paper, and he seems genuinely puzzled by it. In response, I simply hand him his copy."
        ha "It's on p-page 5."

        show hisao basic_neutral_uni
        show kenji neutral
        with chchange

        "As Hisao starts flipping the pages of his copy, I give Kenji his visually-impaired edition. He takes it with a suspicious look in his eyes that puts me slightly on edge."
        "Hisao, having reached the page that contains my column, looks surprised."

        show hisao basic_speak_uni
        with chchange

        hi "‘Club in the spotlight?’ Hey, this is about the science club! But what…?"
        "I smile bashfully."
        ha "M-my first article."
        hi "Huh? I thought you were merely helping out with the editing."

        show muto normal behind hisao at tworight
        with charaenter

        mu "Ikezawa approached me a little while back for some information about this club for a small article in the next issue of the school newspaper."
        
        show muto smile
        with chchange

        mu "But it's a lot larger than I thought. You never said it was going to be a column."
        ha "Naomi… liked the g-general idea, so we turned it into a c-column that will cover a new club each issue."
        "Mutou gives me an approving look."
        mu "This will certainly give our club some much-needed exposure. With luck, we'll get a few new members out of it."

        show hisao basic_grin_uni
        show kenji tsun
        with chchange

        "Hisao looks delighted by Mutou's prediction, but I notice that Kenji suddenly looks terrified, and he taps Hisao on the shoulder."
        ke "We gotta talk, man. We can't be taken off guard by this thing. We gotta prepare."

        show hisao basic_neutral_uni
        with chchange

        hi "Not now, Kenji. We'll have plenty of time to talk later. I doubt we'll get any reactions before the end of summer break."

        hide kenji
        with charaexit

        "Kenji shrugs and walks out of the room. Though I don't get involved with Kenji a lot, I really can't wrap my head around his behavior. I've asked Hisao about it several times, but he usually just rolls his eyes and urges me not to think too much of it."
        "As the sound of Kenji's footsteps fades away, my attention shifts back to the other people in the room who seem significantly more appreciative of my actions."
        mu "I believe this club is indebted to you, Ikezawa. I obviously can't give you a straight 100%% for your next test as a sign of appreciation as that'd be against the regulations, but… hmmm…"

        show muto normal
        with chchange

        "He thinks for a moment, "

        show muto smile
        with chchange

        play sound sfx_snap

        extend "then snaps his fingers."
        mu "I will be going for some coffee. Nakai?"

        show hisao basic_speak_uni
        with chchange

        hi "Sir?"
        mu "Please kiss Ikezawa on my behalf."

        show hisao basic_grin_uni
        with chchange

        stop music fadeout 2.0

        "Wait, what?"
        "Hisao chuckles."
        hi "With pleasure, sir."

        play music music_comfort fadein 4.0

        hide muto
        show hisao cross_smile_uni_close at center
        with charachangealways

        "Mutou walks out of the room and before I can react, Hisao has wrapped one of his arms around me and uses his other hand to gently push my chin up before giving me a tender kiss on the lips."

        show black
        with shuteye

        "I freeze up for a moment, more than a little bit embarassed by the fact that we're in a classroom, but I then close my eyes and accept the kiss."
        "Not letting go of me just yet, Hisao pulls me even closer and softly whispers in my ear."
        hi "Hanako?"
        ha "Y-yes?"
        hi "You'll get my own kisses later today."
        ha "O-okay."

        hide black
        with openeye

        hi "And Hanako?"
        ha "Yes?"

        show hisao cross_grin_uni_close
        with chchange

        hi "I love you."
        "A happy smile appears on my face as I return Hisao's hug."
        "I hope Mutou is going to stay away for a little while, because I want to enjoy this moment for as long as I can."

        stop music fadeout 3.0

        scene black
        with Dissolve(3.0)

        if _in_replay:
            return

    return