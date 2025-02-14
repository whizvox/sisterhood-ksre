label sisterhood_ch4:
label .sh_ch4:

$ set_window_tint(TINT_HISAO)

scene bg school_gate_ss
show hanako emb_smile
with delayblinds

play music music_pearly fadein 4.0

"The sun is already setting by the time Hanako and I make our way to the parking lot."
"Hanako received a text message from Akira confirming they landed safely, and Akira is going to drop Lilly off at the school gates."
hi "Are you sure they'll be here soon?"
ha "Y…yes. It should take them less than an hour to get here."
"I was already aching to see Lilly back after two very eventful weeks, but I'm particularly excited to break the news of Hanako and me going out. I'm very curious about how she'll react."
hi "I wonder how we should tell them about us. Maybe we could hold hands when they arrive."

show hanako def_worry
with chchangefast

ha "H-hold hands?"
"Hanako seems a bit absentminded ever since we left the school grounds."
"I wonder if something's wrong. She seemed excited to see Lilly again earlier today."
hi "Yeah. And then leave it to Akira to point that out."
hi "Then again, she might just keep it to herself just to mess with Lilly a bit. I wouldn't put it past her."

show hanako emb_blushing
with chchange

"Hanako doesn't respond. I notice she's playing with something she's holding in her hand."
hi "Are you considering wearing that when they arrive?"
ha "I don't really know yet."
hi "It's your choice."
ha "Y…yes."

show hanako emb_downtimid
with charachangealways

"Neither of us really knows how to continue the discussion."
"While the silences between us are no longer as frequent or awkward as they once were, they still rear their head every now and again. This is one of those times."
"We went to town the other day to do some shopping for this evening. Neither of us thought Lilly would have much energy for a party, but we wanted to make the evening a bit special nevertheless and bought a batch of fragrant tea as well as a box of sweets for her."

play sound sfx_car_driveup

"Hanako is still toying around with her little trinket as I spot a car heading up the parking lot and approaching us."

show hanako emb_downsmile
with charachangealways

"As it gets closer, I see the distinctive hair color of the Satou sisters behind the windshield. The car stops in front of us, and Hanako lets out a small sigh, putting the trinket back in her pocket."
"Looks like she isn't ready yet to let Akira see her new look."

stop sound fadeout 0.5

"The car door opens, and Akira steps out, giving an enthusiastic wave."

show hanako basic_bashful
with chchange

"I have no idea how much energy this woman has, but an intercontinental flight and a ride from the airport to Yamaku seem insufficient to diminish it."
"Lilly, on the other hand, looks a little worse for wear."

stop music fadeout 1.0
queue music music_ease fadein 4.0

ha "Lilly!"

show hanako at offscreenleft:
    easeout 0.5 alpha 0.0
with charamovefastest

hide hanako

"Hanako's fidgety mood seems to vanish the moment Lilly gets out of the car as she rushes forward and grabs Lilly in a tight hug with a huge smile on her face."
"Lilly is visibly surprised but then recollects herself and returns Hanako's hug with a gentle embrace of her own."
"I can't help but smile myself as I see this display of unrestricted affection between them."

show lilly basic_cheerful_cas at twoleft
show hanako basic_smile:
    xalign 0.4
with charaenter

li "It's so good to meet you again, Hanako."
ha "I'm so happy to see you again, Lilly."

show hanako at center
with charamovefaster

"Lilly carefully signals Hanako to break her embrace and then places both hands on her shoulders."
li "Hanako, I'm very happy for you. Happy and proud."
"She then turns to my general direction."

show lilly basic_satisfied_cas
with chchange

li "Very happy for both of you."

show hanako emb_blushing
with chchange

"I shoot Hanako a suspicious look and notice she's started fidgeting again."
hi "Both of us? Wait, did you…?"

show akira basic_laugh at tworight
show lilly basic_cheerful_cas
with charaenter

"Lilly doesn't reply and merely maintains a cheeky grin on her face."
"Akira is noticeably less subtle."
aki "Congratulations, lover boy! Looks like ya caught yourself a nice fish while we were gone."

show akira basic_ending
with chchange

"I'm starting to understand why Hanako seemed nervous while I was considering how to announce our relationship."
"Lilly probably sweet talked the news out of her days ago."
hi "Hanako, didn't we agree to tell them the news in person?"
"Hanako gives me such a guilty look I'm starting to feel heartless for scolding her."
ha "I…I'm sorry, Hisao. I meant to keep it a secret, but…"

show lilly basic_smile_cas
with chchange

li "Don't be upset, Hisao. It took me a great deal of effort to convince Hanako that keeping such happy news bottled up is an unhealthy and frustrating thing to do to herself."
li "She seemed genuinely relieved when she finally decided to break the news to us ahead of time."
"Now she's pretending this was all for Hanako's benefit instead of satisfying her own curiosity."
"Lilly's playful expression shows she is all too eager to take full responsibility for this premature leaking of information, and she doesn't look even a little bit guilty about it."
"Akira merely looks at me with a mischievous grin."

show akira basic_smile
with chchange

aki "My sis can be pushy in her own polite and passive way, you know?"

hide hanako
hide lilly
hide akira
with charaexit

"Akira walks back to the car, fishes Lilly's luggage out of the trunk, and beckons me to take on the role of porter."

show akira basic_smile at tworight
with charaenter

aki "I'd like to stick around, but I still have a big distance to drive and a boyfriend to catch up with."
hi "Aren't you at least a little bit tired after travelling for so long?"
aki "Nope. When I was born, I hogged all the genetic jet-lag immunity I could get."
aki "As you'll find out soon, there wasn't anything left for Lilly afterwards."

show lilly basic_displeased_cas:
    xalign 0.4
with charaenter

show lilly basic_weaksmile_cas:
    xalign 0.6
with Dissolvemove(1.0)

"Lilly lets out a light groan before carefully walking over to Akira and giving her a polite hug."
li "Stay in touch."

show akira basic_ending
with chchange

aki "Will do. And think about the upcoming weekend, will ya?"
li "I will."

hide akira
with charaexit

"With that, Lilly and Akira part ways, and a minute later we're watching the car drive off into the distance."

show lilly basic_weaksmile_cas_close at center
with characlose

"I walk over to Lilly and give her a quick hug."

show lilly basic_smile_cas_close
with chchange

hi "Welcome back, Lilly. You're probably tired, but Hanako and I planned a little private party for you to celebrate your return."
hi "If you wish to go to bed right now, we'd understand, but if you can bear with us for another hour or so, we can take the opportunity to catch up."
"Lilly smiles gratefully at us."

show lilly basic_weaksmile_cas_close
with chchange

li "I accept the offer as long as you don't mind me being a little less talkative than usual."
hi "Hanako, I'll help Lilly carry her luggage back to the dorms. Would you go ahead and prepare the tea?"
ha "Sure!"
"As Hanako dashes off to the girl's dorm, I turn to Lilly."
hi "What was with Akira's remark about the upcoming weekend?"

show lilly basic_smile_cas_close
with chchange

"Lilly smiles mysteriously."
li "Later."

stop music fadeout 2.0

scene bg school_dormlilly
show lilly basic_weaksmile_cas at twoleft
show hanako basic_bashful at tworight
with shorttimeskip

queue music music_lilly fadein 4.0

li "I needed that."
"As Lilly puts her second cup of tea down, she lets out a satisfied sigh. She still looks a bit tired, but the caffeine seems to have taken the edge off."
"None of us have said a lot since we reached Lilly's room and Hanako brought in a pot of fragrant tea, though it doesn't really matter much. Lilly's presence always seems to turn otherwise uncomfortable silences comfortable."
hi "I suppose what I originally planned to talk about was the news that the two of us are dating now, but with that cat already out of the bag, maybe we could hear some tales from Scotland instead."
"Lilly reaches down, takes a piece of candy from the box we bought, and brings it to her lips as if to further justify leaving the talking to us."

show lilly basic_cheerful_cas
with chchange

li "You could tell me about your first official date, if you'd like."

show hanako emb_downsmile
with chchange

"Hanako really must have spilled her guts to Lilly."
hi "So you know about that too?"
li "Only that it was meant to take place a few days ago."

show hanako emb_blushing
with chchange

"I look at Hanako who's sitting next to me, still looking a little guilty."
hi "Go ahead."

show hanako at center
with charamovefast

"Hanako bashfully nods and gently takes Lilly's hand. She reaches into her pocket, fishes something out of it and puts it into Lilly's hand."
ha "This is a gift Hisao gave me."

$ renpy.music.set_volume(0.7, 1.0, channel="music")

show hanako_hairclip:
    truecenter
    ypos 0.7 alpha 0.0
    easein 1.0 truecenter alpha 1.0
with Pause(1.0)

show hanako_hairclip:
    truecenter
    alpha 1.0
with None

show lilly basic_listen_cas
with chchange

"Lilly takes the object and softly runs her sensitive fingertips alongside it."

show lilly basic_satisfied_cas
with chchange

"After careful examination, she smiles."
li "A little hair clip. With a small flower on top. What a nice gift. Were you wearing it when we arrived?"
ha "N-no. Not yet. I could wear it now if you like."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show hanako_hairclip:
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause(1.0)

hide hanako_hairclip
with None

"I look at Hanako as she takes back the clip from Lilly, pauses for a moment, carefully brushes aside the lock of hair that's usually covering the right side of her face, and applies the clip to pin it in place."

show hanako basic_bashful_clip
with charachangealways

"I'm still a bit unused to the sight of Hanako's face being completely exposed, but that's more because I've been staring at that lock for so long I've gotten used to it."

nvl clear
nvl show dissolve

n "The clip, its flower decoration a miniature version of the one on Hanako's phone strap, was something I gave to her just before our first date with the request to wear it on occasion when we were alone."
n "I told her that the sight of her face wasn't going to be a big deal to me, and I wanted to be able to look my own girlfriend in both eyes."
n "It also served a more practical purpose as I found it awkward to kiss her with that lock of hair constantly getting in the way."
n "As far as I know, this is the first time she's worn it in the presence of someone other than me. Though with Lilly, it obviously doesn't make much of a difference."

nvl clear

show lilly basic_cheerful_cas
show hanako emb_downsmile_clip
with { "master": charachangealways }

n "{w=0.5}I sit back and nibble on a piece of candy myself as Hanako gives Lilly a brief summary of our date."
n "I can't help but be a bit amused as her retelling actually makes it sound much more spectacular than it really was. In fact, it was probably as tried-and-true a date as we could have managed."
n "This was a bit intentional on my part as I wanted our first date to be as comfortable as possible."

nvl clear

n "We started with a quiet little dinner at the Shanghai, a familiar place without a lot of people around. It was here that I gave Hanako the hair clip that she's now carrying with her all the time."
n "After finishing our meal, I took her to a small movie theatre in the city. The movie we went to was actually a film adaption of a book we both read before, so neither of us was very surprised by most of the twists in the plot, but we had the benefit of having additional discussion material on our way home, and being able to avoid awkward silences with Hanako is always a good thing."
n "I was even entertained at how passionate she got for a moment while we were debating the way the director changed a few things about the ending before slipping back into her usual meek demeanor."
n "{vspace=60}One thing about our date that stood out was Hanako's uneasiness with the idea of me paying for everything, so we ended up paying for each other's meal and movie ticket."

nvl hide dissolve
nvl clear

show lilly basic_satisfied_cas
with chchange

li "It sounds like you both had a wonderful time."
"Lilly seems pleased with Hanako's story."

show lilly basic_weaksmile_cas
with chchange

"She pauses for a moment before addressing us with a sheepish expression on her face."
li "Are there any more dates planned for the upcoming weekend? Or am I not privy to such information?"
hi "Not at the moment. We both wanted to catch up on things with you. Why?"
li "I was thinking that with us having the upcoming three days off, we could spend our time away from Yamaku. Our family owns a summerhouse in Hokkaido we can stay in."
hi "Is that what Akira was talking about before she left?"
li "Correct. She is planning to stay there next weekend with her boyfriend."

show lilly basic_displeased_cas
with chchange

"Her expression clouds for a moment."
li "Which means that if we go there… we will probably end up cleaning the place up for them."

show hanako emb_emb_clip
with chchange

"I share a brief look with Hanako. Having to do some cleaning seems a small price to pay for a cheap vacation, and spending that vacation with Hanako and Lilly only makes the prospect even more attractive."
hi "I'd love to go. I've never been to Hokkaido before. How about you, Hanako?"
"Hanako beams."
ha "Me neither. I'd really like to go, too."

play sound sfx_clap

show lilly basic_satisfied_cas
with chchangefast

"Lilly claps her hands together."
li "I suppose it's settled then. We'll have to leave early in the morning in order to catch the train there."
li "Maybe it'd be best if we retire for the evening for now. We won't be able to sleep in tomorrow."
"Hanako gets up and gathers the tea cups and tea pot from the table."
ha "I'll go and clean the tea service downstairs. And I think I'll go to bed afterwards."

hide hanako
with charaexit

play sound sfx_doorclose

"As I get up myself to leave as well, Hanako gives me a quick kiss on the lips before removing her hair clip and walking out of Lilly's room."
"Before I can follow her, Lilly softly calls my name."

show lilly basic_smile_cas
with chchange

li "Hisao, would you mind helping me unpack a few things? I'd like to get some sleep myself, and I will still have to pack a few things tomorrow morning as well."
"For a second I want to ask if it wouldn't have been more appropriate to ask Hanako to help her with that."
"But then I realize that this may very well be Lilly's roundabout way of asking me to stick around for a small talk, which is fine because there's something I've been meaning to ask her as well."

show lilly basic_weaksmile_cas at center
with charamove
show lilly at sittingpos
with charamove

"As I start messing with the lock of the suitcase, Lilly sits down on her bed with a tired but cheerful expression on her face."
li "So… you and Hanako…"
hi "Yes, life can take some interesting turns. Thankfully this one was far more positive than most of the other big changes in my life this year."

show lilly basic_cheerful_cas
with chchange

li "I'm happy you two found each other. Hanako's mood seems to have improved so much compared to how she used to be."
hi "Things could have worked out very differently."
hi "By the way, thanks for the advice the other day. I needed that wake-up call pretty badly."
"That's an understatement. Not too long ago, I was thinking of nothing but protecting Hanako from the world around her."
"I was obsessing with her emotional condition and thought of nothing except on how to prevent her from getting hurt more than she had already been."
"I didn't realize how patronizing my disposition must have been until Lilly called me out on it that evening. Not only was Lilly's judgment of my behavior spot on, but Hanako was aware of it too and instead of protecting her, my attitude was actively hurting her."
"If anything, I want to forget about this stage of our relationship as soon as possible."

show lilly basic_smile_cas
with chchange

li "I'm glad I could help. Though you two probably would have been able to sort things out yourselves."
hi "I don't think so. Hanako turned out to be aware of my obsessive worrying, and it only served to make her feel worse."
hi "I'm not sure how things would have turned out if you hadn't told me to back off a bit, but I doubt we'd be where we are now."
hi "But there's one thing you said during that phone call that I'd like to ask you about."

show lilly basic_oops_cas
with chchange

li "What is it that you would like to know?"
hi "You told me not to doubt my bond with Hanako, because of some reason or another, but you cut yourself off before elaborating."
li "I promised Hanako not to tell you about how she felt about you. I caught myself in time to avoid breaking that promise."
hi "I'm a bit surprised she told you about that. I would have expected her to keep something like that to herself."

show lilly basic_listen_cas
with charachangealways

"Lilly remains silent for a few seconds, carefully choosing her words before answering."

show lilly basic_weaksmile_cas
with chchange

li "She didn't. At least not at first. We frequently spoke about you while spending time together."
li "Shortly after the festival, Hanako suddenly started asking me what I thought of you."
li "She wanted to know whether I… liked you. She was uncharacteristically persistent in her questioning."
hi "And you in return wanted to know why she was so interested?"

show lilly basic_oops_cas
with chchange

li "Yes. After some digging on my part, I got her to admit to me that she was in love with you herself."
hi "So it was like she was asking you if it was safe for her to pursue me without becoming a rival to you?"
li "I do not think she had any plans to pursue you. But in the case I liked you as well, she would have tried to push her own feelings away for my benefit…"

show lilly basic_reminisce_cas
with chchange

li "…regardless of how you felt about her. That's the kind of person she is."
"That does sound like something Hanako would do."

show lilly basic_oops_cas_close
with characlose

"I put a hand on Lilly's shoulder."
hi "Well, things worked out in the end. We got together, and I'm happy that I'm able to call her my girlfriend."

show lilly basic_weaksmile_cas_close
with chchange

"Lilly nods silently before smiling inquisitively at me."

show lilly basic_smile_cas
with charadistant

li "Hisao… if I may ask. How did you two get together? How did things… fall into place between you two?"
li "I asked Hanako, but she wouldn't tell me much about it."
"That's a tricky question. Things falling into place was probably the worst description of how our relationship came to be."
"It was a whole lot more accurate to say things were blown to very tiny bits that we ended up using to piece together something more stable."
"We ended up playing emotional hide and seek, we ended up hurting each other and pushing each other away and to top it off, we had sexual intercourse for misguided reasons that neither of us was emotionally ready for."
"It wasn't exactly romance novel material we took part in. I have my sincere doubts Lilly would really want to know even half of these things."
hi "The right word would be… messily."

show lilly basic_reminisce_cas
with chchange

hi "It's probably better to leave this to your imagination. Please take my word for that."
li "Oh."
"Thank goodness she doesn't pry."

show lilly basic_listen_cas
with chchange

"One more thing bothered me, though. There were many things Hanako told me during our confession in the park that day—many things that I didn't think Lilly was aware of—and some of them applied to her as well."
"The difficulty with trusting friends Hanako admitted to having was one thing that came to mind, and part of me wants to let Lilly in on this. But I'm not certain yet if the risk would be worth it."
"The things Hanako told me in the park were things she confided in me, because she trusted me. Earning her trust has been a ride through hell, and something tells me it won't be easily regained if she feels I betrayed it."
"With luck and Hanako's slowly growing confidence, she'll be able to improve her friendship with Lilly on her own without me having to meddle in it."
"While enveloping myself in my thoughts, I finish emptying Lilly's suitcase, stand up and get ready to return to my own dorm room."
hi "Don't worry too much about it. The important thing is we're fine now."

show lilly basic_smile_cas
with chchange

hi "Let's focus on what's ahead of us. Starting with a few days in Hokkaido."

show lilly at center
with charamove

"Lilly gets up from the bed and gives a polite bow."
li "Thank you for tonight, Hisao. I'm looking forward to tomorrow."
hi "Me too. Goodnight, Lilly."
li "Goodnight, Hisao."

stop music fadeout 3.0

scene black
with Dissolve(3.0)

return