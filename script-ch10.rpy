label sisterhood_ch10:
label .sh_ch10:

$ set_window_tint(TINT_HISAO)

call sisterhood_timeskip

scene bg school_nurseoffice:
    yalign 0.5 zoom 1.05
show nurse concern_close:
    center
    zoom 1.05 ypos 1.02
with Dissolve(1.0)

play music music_nurse fadein 0.5

nk "So, no lightheadedness, chest pains or tingling feet this morning? No irregularities during the weekend?"
"The nurse casually slurps some coffee while asking me the typical routine questions, to which I respond with the typical routine answers."
hi "None at all. I set a good pace this morning. The coach was pretty pleased."
nk "No problems at all? Are you sure?"
hi "Uh huh. Why would I suddenly get complications? I've been sticking to the schedule, and I haven't had a single flutter since I started training."

show nurse neutral_close
with chchange

nk "Emi said you tried to skip our check-up this morning."
"I roll my eyes."
"I did indeed try to go straight to my dorm room to shower and get dressed, but Emi wouldn't have any of that."
hi "I have some homework I have to look over before class, and I figured I could afford to skip this once."
hi "This whole thing has become such an automated routine for both of us, I sometimes wonder if it's still necessary."

show nurse concern_close
with chchange

nk "I can't blame you for thinking like that, but the moment we start making these sessions optional, we're setting you up for adopting bad habits."
nk "I've had this kind of thing with Emi a little while back, and in the end she came down with an infection and had to get around in a wheelchair for a while."
nk "And in her case, it wasn't even potentially life-threatening. I can't really afford to take those kinds of risks with you."
"I had a feeling my excuse was going to provoke a lecture like that. I learned long ago that the best thing to do is just nod and agree whenever the nurse drops the lame jokes and gets into serious mode."

show nurse neutral_close
with chchange

nk "Now, if you just take your shirt off and let me check your heart beat, you can go back to your homework in a minute."
"I shrug and instead of taking my shirt off, I simply pull it up until my chest scar is completely revealed."

show nurse concern_close
with chchange

"The nurse frowns a bit at this deviation from the usual protocol, but then gives in and presses his stethoscope against my chest without further questions."
nk "Well, I'm not picking up anything out of the ordinary."
nk "Although…"
hi "Yes?"

show nurse fabulous_close
with chchange

nk "You just wanted to go straight back to your dorm because of homework?"
hi "Yes. Is there something wrong with that?"

show nurse grin_close
with chchange

"The nurse's smile turns slightly wicked as he taps the chest piece of the stethoscope."
nk "It's just that your heart rate just said something else. You're not exactly a good liar."
hi "It's nothing related to my heart. Isn't that enough?"
nk "Fine, fine. Let me check your heart beat one last time and then you can go."
"Eager to get it over with, I lift my shirt again, but the nurse shakes his head."

show nurse concern_close
with chchange

nk "I'll go with a different angle this time. Your back."
hi "Huh?"
"I consider protesting, but can't make up a valid excuse in time, so I let him lift up the back of my shirt and press the chest piece just left of my spine."
"He listens for a second, then takes off the stethoscope and gives a satisfied nod."

show nurse grin_close
with chchange

nk "Your heart rate sounds steady enough. Must have been the additional exercise that did it."
"Either this guy is extremely sharp or he simply has a dirty mind."
"If there were still any doubts in his mind about the origin of the thin, red marks on my back, my wincing expression probably blew those right out of the water."
"If his grin were to get any wider, the top of his face would probably fall off."
nk "So, your girlfriend's a scratcher, eh? It's always the ones you least suspect."

play sound sfx_impact2
with vpunch

hi "D-don't you have any shame at all?!"

hide nurse
with charaexit

"I turn around and prepare to leave before he comes up with more ways to fluster me."
"Before I can turn the doorknob, I hear him call out to me."

show nurse grin
with charaenter

nk "Hisao, can I have just one more moment?"
"I turn around and the nurse motions me to sit down again."

show nurse neutral
with chchange

nk "Sorry about the joke. You can't deny that the opportunity was too good to ignore. If I upset you, we can talk tomorrow."
"So he's not gonna drop it. I might as well get it over with now."
"With an emphasized sigh, I sit down in the chair in front of him."

show nurse neutral_close
with characlose

nk "You started sleeping with her?"
hi "If I say no, are you going to take out the stethoscope again?"
"He grins an amused grin, then shakes his head."
nk "You're not very good at keeping a poker face, Hisao. I think I can do without it for now."
hi "I realize there are regulations here, but it didn't take place on the school grounds."
"At least not this time."
nk "I'm not going to give you a hard time over that. Enforcing those regulations isn't my job. Watching over your health is."
hi "You're not gonna demand a check-up after every time we…, are you?"
"He laughs out loud at this, before winking at me."

show nurse fabulous_close
with chchange

nk "I could, if you'd like me to."
hi "Not freaking likely."
nk "Heheh, probably not."

show nurse concern_close
with chchange

nk "The only thing I'd like to know is if your heart ever acted up during one of those times."
nk "I'm sure you are aware of the fact that it's not completely without risks."
hi "I had a brief moment during our first time. That was before I started working out. It was over after a few seconds."
"He briefly nods."
nk "If you're able to handle your current training regimen, you're probably able to handle that kind of stuff as well, though it might be smart to let your girlfriend take the active role if you start feeling tired and avoid actions that place too much strain on your body at all costs."
nk "Just be sure not to ignore the warning signs and stop if you feel something's off, no matter how tempting it may be to continue. Keep the big head in charge at all times."
hi "My girlfriend's very vigilant about that kind of stuff. She noticed it the first time too."
hi "She'd definitely stop me if she suspected something to be wrong. She even thought up a safe word I can use if my chest suddenly starts hurting."

show nurse neutral_close
with chchange

nk "It's a relief to hear she's looking out for you."
hi "You're more laid-back about this than I expected."
"He chuckles. I suspect this is not the first time he's had this kind of discussion with a student."
nk "I prefer the term pragmatic. When kids become adolescents and develop a healthy sex drive, they're not gonna pay much attention to a preachy guy in a white coat telling them to stop having fun. Might as well make sure they at least go about it in a responsible way."

show nurse concern_close
with chchange

nk "But if something does happen, even if it's a minor red flag, I want you to bring it to my attention immediately. That's not a mere request."

show nurse grin_close
with chchange

"His grin returns as he gives me a playful pat on the shoulder."
"It's kinda unsettling how quickly this guy can switch back and forth between being immature and authoritive."
nk "I promise I won't try to embarrass you."
"He tries his best to look trustworthy, though I'm not completely sure how well he'd be able to keep that promise."

show nurse neutral_close
with chchange

nk "Well, that's all. See you tomorrow."

hide nurse
with charaexit

play sound sfx_dooropen

"I nod, get up and head for the door. As I'm about to leave, the nurse gives me one more sly look."

show nurse grin
with charaenter

nk "By the way, Hisao… Applying the chest piece to someone's back is part of monitoring the lungs. For the heart, you always put it on the chest. Always."
nk "Since it was immediately obvious that you were trying to hide your back, I needed to make up a little excuse."
nk "Didn't think you'd fall for it."

hide nurse
with charaexit

"He lets out a maniacal laugh before turning back to his computer, leaving me flabbergasted."

stop music fadeout 0.5

scene bg school_miyagi:
    right
    zoom 1.2
with locationskip

play music music_another fadein 0.5

"As I finish setting up the pawns, a delicious smell teases my nostrils."
hi "Wow, that smells pretty good."

show hanako basic_bashful at twoleft
with charaenter

"Hanako beams at my words and speeds up unpacking the lunch she's made for the two of us."
"Hanako making lunch for us both has become a regularly recurring event, and other than one instance where the food she cooked tasted… not really bad but definitely a little weird, I don't really have anything to complain about."
"I probably should return the favor more often, but I know Hanako enjoys indulging in her domestic side, and I enjoy experiencing this side of her."
hi "Aren't you going to pour the tea?"
"I notice Hanako has finished preparing the tea, but isn't really getting ready to serve it yet."

show hanako basic_normal
with chchange

ha "I'd like to wait for Lilly if that's okay with you."
hi "Why don't you have a seat in the meantime?"

show hanako emb_smile_close at closeright
with charamovechangefaster

"She approaches the table, takes a moment to decide and then sits down next to me, putting her hand on top of mine."
hi "Can I have one little bite, just to sample?"
ha "Just one then. Could you open your mouth, please?"
"I roll my eyes. Does she really enjoy this kind of thing that much?"
hi "I know how to use chopsticks. I've been using them for a large portion of my life."
ha "Please?"
hi "Alright then."
"I open my mouth slightly and Hanako uses her chopsticks to pick up a piece of chicken and put it into my mouth."
"When I close my mouth and she withdraws the chopsticks, she has a childish smile on her face."
hi "It tastes very good. I can't wait to taste the rest."
ha "When Lilly gets here."
"It's nice to have a few moments together."
"After we came back from our date yesterday, we both had to focus on finishing homework, and due to my running sessions each morning, we can't see each other before class either."
"After class, I have club activities to tend to, and Hanako's decided to help out the newspaper club for another week."

show hanako emb_downtimid_close
with charachangealways

"I stroke her hand for a bit before noticing her other hand is fixed on the lower part of her neck. I remember she was in a similar posture for the entire duration of class."
"I give her an amused smile."
hi "How's your hickey, Hanako? Is it still visible?"
"She flushes profoundly at my question before meekly nodding."

show hanako emb_timid_close
with chchange

ha "I-it w-was when I c-checked this m-morning."
"Despite her posture, I'm sure the hickey on Hanako's collarbone wouldn't be visible to anyone unless she removed her blouse in front of them. I made sure not to leave it in a place that her school uniform would leave exposed."
hi "You know, when I suggested giving you one in return for those marks on my back, I was speaking in jest. There was no real need to go through with it."
"When we woke up that morning in our hotel room, we first spent our time lazily cuddling in bed and feeding each other the sandwiches we bought for the occasion at the coffee shop the night before."
"It wasn't until we went to take a bath together in order to wash off the lotion residue that Hanako noticed the red marks on my upper back."
"She didn't remember leaving them and I didn't remember receiving them, so they must have been made while we were too much into the heat of the moment to notice."
"Regardless, Hanako immediately started stammering apologies, causing me to jokingly point out I could leave a little mark of my own so we could call it even and drop the matter."
"I didn't expect her to latch onto that remark as strongly as she did, so in order to settle the matter I gave her a small suction mark on her collarbone."
"I had the impression that at the time, she didn't exactly hate receiving it, embarrassing as it was."
ha "It's o-okay. Nobody n-noticed."
"My thoughts return to my check-up with that demon of a nurse this morning."
hi "I wish I could say the same."

show hanako defarms_shock_close
with chchangefast

ha "W-w-what!?"
"I roll my eyes."
hi "It might be a good idea to avoid the nurse for a week or so."
ha "H-he n-noticed?"
"I relate my experience in the nurse office to Hanako."
"When I finish my story, the result is a muffled giggle. Except the sound isn't coming from Hanako but from beyond the doorway."

show lilly:
    xpos -0.5 xanchor 0.0
with None

show bg:
    xanchor 0.0 xpos 0.0 yanchor 1.0
show lilly basic_ara:
    xpos 0.0 xanchor 0.0
show hanako:
    xpos 1.4 xanchor 1.0
with charamove

"We turn towards it and are mortified to see Lilly standing there."
"Her hand is raised in front of her mouth, but her shaking shoulders make it obvious she's bursting with laughter on the inside."
"Hanako lets out a soft, desperate whimper and promptly shuts down, covering her face with her cupped hands in embarrassment. I let out a gasp myself but manage to collect myself enough to greet Lilly."
"Something tells me I won't be able to count on Hanako for the time being."

hi "You kinda picked an awkward moment to join us, Lilly."
"Lilly makes an apologetic gesture while still trying not to laugh out loud."
li "It appears that I did. I won't be here for very long however, so perhaps things won't be uncomfortable for too long."
hi "You're not joining us? Class rep duties again? It's happened pretty often lately."

show lilly basic_smile
with chchange

"Lilly simply nods."
li "Perhaps I'll be able to make up for it tonight. I came here to invite you to join me in my room this evening. Akira will be coming over and it would be nice to hang out together."
hi "That sounds like a good idea. We'll be there."

show lilly basic_cheerful
with chchange

li "Wonderful. Until tonight then."
"With a polite wave, Lilly walks out of the room."

show lilly:
    xpos -0.5
show bg:
    xanchor 1.0 xpos 1.0
show hanako at closeright
with charamove

"I turn to Hanako, who's still in the same position as she was when we first noticed Lilly, as if time had stopped around her."
hi "Ummm… Hanako. She's gone."
hi "Let's… just… have our tea now and play a little match."

show hanako emb_downtimid_close
with charachangealways

show hanako at offscreenright
with charamove

stop music fadeout 2.0

"Hanako, still covering her face, manages to give a nod and stiffly gets up to get the teapot."
"Fifteen minutes later I score my first easy victory on her in two months."

scene bg school_gate_ss
show hanako basic_worry_close_ss
with locationskip

queue music music_pearly fadein 4.0

hi "We could just ask her directly."
ha "I-I know. But I'm… afraid she'll just smile and dismiss it."
hi "So now the plan is to ask her sister behind her back?"
ha "I-I don't really like it either. B-but I'm a bit worried."
"After I finished my homework for the day and headed over to Lilly's dorm room, I ran into Hanako who was waiting outside the girl's dorm building and who wanted to take a little walk with me first."
"And now we're standing near the school gate, waiting for Akira to arrive."
hi "I realize Lilly's been absent from lunch more often than usual, and we didn't have many get-togethers until last week, but does that really suggest that there's something wrong? She could simply have more than usual class rep duties to tend to."
ha "I don't think that's the case. I-I asked one of her classmates today, and he said things weren't any busier than usual in class. Nothing out of the ordinary happened recently that could result in more work for her."
hi "You asked one of her classmates?"
"That's an interesting development."
"Despite the fact that Hanako has become quite a bit less passive than she used to be while being around me, she still has a tendency to try and avoid interaction with most other people and is still uncomfortable around the people with whom interaction is unavoidable."

show hanako basic_normal_close_ss
with chchange

ha "H-he's a member of the newspaper club and c-came over to submit some material to me, s-so I asked him if he thought things were busier than usual in class."
hi "Were you nervous?"
ha "I w-was, but him being blind made it a bit easier to talk to him."
"If what Hanako's saying is true then Lilly is either using her class representative duties as an excuse to be on her own or something's on her mind that acts as a distraction."
"Either way, Hanako's hunch might be worth looking into."

hide hanako
with charaexit

"And after a few minutes of waiting…"

show akira basic_laugh_ss
with charaenter

aki "Yo!"
"Upon noticing us, Akira greets us with a friendly wave."
hi "Nice to see you again. It's been a while since we last saw you. Have you been busy?"

show akira basic_annoyed_ss
with chchange

aki "Extremely. And that's probably not gonna change much in the upcoming weeks."
hi "I hope you at least enjoyed your time off in Scotland then."
aki "Meh, best thing about it was our folks' beachside home."

show akira basic_smile_ss
with charachangealways

"As Akira and I are exchanging small talk, I start noticing she's sneaking the occasional glance at Hanako, which is strange since Akira knows Hanako dislikes being stared at."
"And it wasn't just me who picked it up."

show akira at twoleft
show hanako emb_downtimid_ss at tworight
with charaenter

ha "Ummm… I-is there s-something o-on m-my…"

show hanako defarms_shock_ss
with chchangefast 

"Hanako gasps before she can finish her sentence, and we have a mutual moment of clarity as we both realize what it is Akira is looking at. Or rather, looking for."
"Hanako's eyes grow wide in an expression that's a mixture of desperation and horror. I myself am mostly just annoyed."
hi "Look, her blouse is covering it up, so could you stop looking for it already?"

show akira basic_laugh_ss
show hanako emb_downtimid_ss
with chchange

"Akira laughs heartily at my reaction."
aki "Looks like I got busted. Sorry. I wasn't sure of its exact location. Lilly obviously couldn't tell me."
hi "Lilly told you about this, huh? I hope she didn't merely invite you for a chance to poke fun at us."

show akira basic_smile_ss
with chchange

aki "She didn't invite me, I invited myself. And no, it wasn't to poke fun at you."
aki "Though if it makes you feel better, I've had a few crummy weeks behind me, and that silly little story cheered me up for the day."
aki "Besides, it's not a big deal. Take this from someone with experience in attending meetings with one of those things peeking out from under her collar."
"While part of me is eager to satisfy my morbid curiosity regarding the “experience” Akira is talking about, I haven't forgotten the reason we came here in the first place, and I eagerly take advantage of the opening she just gave me."
hi "Crummy weeks, huh? Is it about something that also involves Lilly?"

show akira basic_resigned_ss
show hanako emb_timid_ss
with chchange

aki "Huh? What makes you think that?"
hi "We both feel like Lilly's been a bit more distant lately. Like something's on her mind that she doesn't like to talk about."
hi "Seeing that you two share so much, we thought maybe you had a clue."
aki "Really?"
"Akira looks pensive for a second."

show akira basic_smile_ss
with chchange

aki "Why don't you join us? You can ask her yourself."
hi "We were already invited, so let's go to her place together then."

stop music fadeout 1.0

scene bg school_dormlilly
show akira basic_laugh:
    xpos 0.1 xanchor 0.0 yanchor 1.0 ypos 1.1
show lilly basic_ara at sittingpos
show hanako emb_emb:
    xpos 0.9 xanchor 1.0 yanchor 1.0 ypos 1.1
with locationskip

queue music music_lilly fadein 2.0

aki "An arcade center, huh? That's a pretty unusual destination for a date."
"Since lunch today got so uncomfortable, we decided to use this opportunity to tell Lilly and Akira about our date last weekend. At least the first part. They already knew more about the second half than they needed to know."
hi "We had a pretty good time. She may not seem like it at first, but Hanako has quite the competitive streak."
ha "W-we didn't just play competitive games though. We also teamed up in a lot of games. Both are great fun in their own way."

show akira basic_smile
with chchange

aki "Did you win that little fellow over there as well?"
"Akira has noticed the plush dog sitting in Hanako's lap. Hanako nods enthusiastically."
ha "Yes, he was lying in one of the crane games. I thought he was adorable, so we made an effort to retrieve him."
aki "A dog who's half blind. Talk about ironic."
hi "Hey Lilly, do you like animals? Have you ever had a guide dog in the past?"

show lilly basic_smile
with chchange

li "That issue came up a few years ago, but ultimately, we decided against having one."
aki "Yeah, keeping the place in order was already enough work for the two of us without having to tend to an animal as well."

show hanako basic_bashful
with chchange

ha "Ummm… Well, this one is not a guide dog, but he's very sweet regardless. Would you like to adopt him, Lilly?"

show lilly basic_oops
with chchange

"Lilly is visibly surprised by Hanako's offer."
li "Really?"
ha "Sure."

show lilly basic_cheerful
with chchange

"Lilly takes the little dog from Hanako and briefly examines it with her hands in order to determine its appearance."
li "My, how cute he is. Thank you very much, Hanako. Does he have a name already?"
ha "Niji."
li "That's a very nice name. I'll be sure to take good care of Niji for you."

show akira basic_laugh
with chchange

aki "Why are you giving her gifts? It ain't even her birthday yet."

show hanako basic_worry
with chchange

ha "Hmmm… She has been… seeming… a bit blue lately. I thought she could use some extra company."
aki "Awww… Isn't that sweet? What do we say now, Sis?"
hi "Somehow you lecturing Lilly on etiquette, even in jest, feels extremely wrong."

show akira basic_boo
show lilly basic_giggle
show hanako basic_bashful
with chchange

"Judging by Lilly's and Hanako's chuckling, I'm not the only one who feels that way."
aki "Oi, I can speak formally if I have to. I just choose not to in my free time."
"A nod from Lilly affirms this."
"I'm not exactly sure what Akira's profession is, but her suit indicates a job where her usual overly casual language probably wouldn't be deemed as very appropriate."

show hanako basic_worry
with chchange

"I could ask her, but right now Hanako's gaze towards me tells me she's expecting me to help her capitalize on the opening she just created."
hi "Lilly, about what Hanako said earlier… I noticed it as well. If something's bugging you, you could tell the plush dog, but remember we're also here for you."

show lilly basic_weaksmile
with chchange

li "Thank you, Hisao. I appreciate it."
"Looks like she's not gonna take the bait."

show akira basic_resigned
with chchange

aki "Hey Sis…"
"Akira's tone has changed from the light-hearted one she usually uses, and for a moment we can see her carefully contemplating and measuring her words—a trait that until now we thought belonged exclusively to the younger of the Satou siblings."
aki "…don't you think now would probably be a good time to tell them? I certainly think so myself."
"So not only is there something, but Akira has known about it too."

show lilly basic_displeased
with chchange

li "Before we left Scotland, you told me I had to determine my choice and the right moment to tell others myself."
"I can tell that Lilly's not happy with her sister butting in."
"Her tone is polite as usual, but also a little irritated. Akira is unfazed, however."
aki "Yeah, but your friends are worried about you, and keeping 'em in the dark doesn't seem like the right thing to do."
li "Even so…"
aki "What's more, I went over to uncle's place yesterday and told Hideaki, who may have told his sister about it."
aki "I realize the odds of it happening are slim, but you wouldn't want your friends to learn the news from Shizune, do ya?"

show lilly basic_concerned
with chchange

"That remark makes Lilly visibly cringe."
"I was quite surprised when Hanako revealed to me that Lilly and Shizune are first cousins. Seeing how Akira herself doesn't seem to be bothered by their hostility, she probably doesn't pay the feud between her sister and her cousin much heed."
"Still, she mercilessly used it to her own advantage just now."

show lilly basic_displeased
with chchange

stop music fadeout 2.0

li "…very well then…"

play music music_night fadein 4.0

"Lilly takes some time to determine what she wants to say, occasionally fidgeting with Hanako's puppy as she does."
li "As you know, our parents live in the city of Inverness in Scotland. It's the town where the head office of our family's company is located."
li "Father decided to move there six years ago in order to fill the executive position that opened up there, which resulted in Mother moving there as well. Akira and I stayed behind for the sake of her job at the Japanese branch of the company and my education."
hi "Is education really that much better here in Japan than in Scotland?"
li "I'm not really sure, though our family has good ties with Yamaku here. The family's company is among its donors."
li "Anyway, Akira and I were summoned there to visit an aunt of ours who had fallen ill. It was the first time in six years we met with our parents again."
li "While we were there, our father gave Akira a job offer at head office. He talked to some people at the legal department there and recommended her for a position. A position she has decided to accept."
"So Akira is migrating."
"Despite not having siblings myself, I can see how this would affect Lilly's mood. Since her parents moved to Europe years ago already, Akira must have been the closest thing she's had to a parental figure."

show hanako emb_sad
with chchange

ha "So… You're… leaving? Permanently?"
"I can tell Hanako's trying to sound casual, but she doesn't really do a good job at hiding the sadness in her voice."
"Akira is one of the few people Hanako gets along well with, despite their contrasting personalities, so this news doesn't just mean Lilly loses a sister in a way, but also Hanako losing one of her few friends."

show akira basic_lost
with chchange

aki "That's the gist of it. I've already broken up with my boyfriend. There's no way a long-distance relationship between us would work out."

show akira basic_resigned
show hanako emb_downsad
with chchange

aki "If the choice had been completely mine, I would have picked a better time, but sometimes things just happen outside your control, and the best thing you can do is roll with the punches."
hi "You're kinda making it sound like you didn't have a choice in this at all."
aki "Don't get me wrong, it's still my own decision. But a side effect of the old man's recommendation was that my current career was pretty likely to hit a dead end if I declined."
aki "There were still plenty of steps on the corporate ladder I wanted to take, but in the end my promotion could have taken place under far better circumstances."
hi "So when exactly are you leaving?"
aki "Around the time your summer break starts. I've been working hard to try and tie up all the loose ends here over the last few weeks. I'd be lying if I pretended it hasn't been stressful."
"Loose ends? Are we a loose end as well? What about Lilly?"
"Hanako, who has been quiet for some time now, suddenly speaks up again."

show hanako emb_sad
with chchange

ha "I-I'm going to m-miss you, Akira."

show akira basic_smile
with chchange

aki "Same here. It was fun hanging out with you guys. It's nice to see my sister has such good friends here."
"One thing still is still troubling me."
"Lilly spoke of a decision earlier. And I can see I'm not the only one who wonders about that."
ha "L-Lilly, w-what was t-that decision you mentioned b-before about?"

show lilly basic_sad
show akira basic_resigned
with chchange

stop music fadeout 2.0

"Lilly pauses for a few seconds before speaking, clearly not completely comfortable."
li "The truth is, Hanako, that my parents also summoned me back."
li "They want me to move back in with them when Akira transfers."

play music music_rain fadein 4.0

show hanako emb_downtimid
with charachangealways

"Despite the fact I'm not really that surprised by Lilly's revelation after she brought up Akira's departure, this news still hits us like a bombshell."
"Not too long ago Hanako and I were still talking about how it felt like the three of us were like a small family. And now, one member of that family is about to leave for good."
"Or is she?" # vsauce, michael here

show hanako emb_timid
with chchange

"Taking a sidelong glance at Hanako, I notice she's looking at me with a desperate look in her eyes."
"She wants to know whether this is final or not, but obviously isn't sure whether she's prepared for the answer."
"I decide to ask the question for her."
hi "So, Lilly, will you be leaving too?"

show lilly basic_reminisce
with chchange

li "…I… haven't made my decision yet, Hisao. In fact, I wasn't really planning on breaking this news to you two until I made up my mind."
li "I didn't want this matter to ruin the joy of your newly-found relationship. Especially since I'm still in the process of trying to decide."
aki "I'd be the last one who'd want to rush you Sis, but that process has been going on for quite some time, and I'm not getting the impression much progress has been made."
aki "It'd be nice if I knew whether to cancel your ticket or not."
hi "You have a ticket already?"
aki "Yeah, proof that the folks are eager to help her make a decision."

show lilly basic_sad
with chchange

li "Akira, please…"
aki "Sorry."

show akira basic_smile
with chchange

"Akira looks at us with a weary smile."
aki "Well, now you know the gist of it."
hi "Are you here to help her make a decision as well?"
aki "Naw, just to catch up on things. It's been a while since we've met face to face."
aki "I feel I've already influenced her decision too much as it is."

show hanako emb_sad:
    ypos 1.0
with charamovechangefaster

"Upon hearing that, Hanako slowly rises to her feet. I notice she's looking very tired."
ha "W-we'll give you two some time alone then."
"I get up as well, but before we leave there's one more thing I want to address."
hi "Lilly, speaking of which… We initially thought you were being distant in order to give Hanako and me some space…"

show lilly basic_weaksmile
with chchange

li "That was still part of the reason, Hisao."
li "I genuinely wanted you two to spend more time together in order to deepen your relationship and grow closer. And it seems that's exactly what you and Hanako have done."
li "In that regard, I have no regrets."
li "But it is also true that this matter has been on my mind a lot and I've been needing time alone in order to sort things out for myself."
hi "Just take care not to get stuck in permanent worry-mode."
hi "Seeing that we know now, you can count on Hanako and me if you want a listening ear or a shoulder to support you. Both of us would happily sacrifice our ‘time together’ for your sake at this point."

show hanako basic_worry
with chchange

"I take a side-look at Hanako who's nodding fervently, before remembering Lilly can't see that."
ha "Y-yes. W-we'll support you, Lilly."

show lilly basic_smile
with chchange

li "Thank you, Hanako, Hisao."
li "I will make sure to spend more time with you from now on out. Maybe it will indeed help to take my mind off matters."

show lilly basic_weaksmile
with chchange

li "I hope you can forgive me if I don't discuss this subject a lot in front of you."
"Come to think of it, I bet it's been the main subject of conversation between herself and Akira as well as her parents ever since she returned to Japan. She's probably really sick and tired of it already."
ha "T-that's okay, Lilly."
"Without much more to discuss, we say our goodbyes to Lilly and Akira."

scene bg school_girlsdormhall
show hanako emb_timid_close at closeright
with locationchange
with Pause(1.0)
show hanako emb_downtimid_close at offscreenright
with charamove
play sound sfx_doorclose

"As we leave the room, Hanako gives me a quiet goodnight kiss and enters her room without saying anything."
"I would have liked to accompany her, but I guess she wants to be alone for a while."
"I just hope she's not going to bottle up whatever she's feeling right now."

stop music fadeout 2.0

scene bg school_dormhisao_blurred_ni:
    right
    zoom 1.2
with locationskip

nvl clear
nvl show dissolve

n "As I put on my pajamas and take my dose of pills for the night, my mind continues wandering on Lilly's revelation and what it means for us and especially for Hanako."
n "Until I came to Yamaku, Lilly was the only friend Hanako had here, possibly the only person Hanako had here or pretty much anywhere else."
n "What kind of effect would the loss of such a person have on Hanako?"

nvl hide dissolve
nvl clear

play sound sfx_rustling

"After getting into bed, I spend some time staring at the ceiling and trying to digest this evening's events."
"Maybe it's still too early to jump to conclusions."

play sound sfx_taps1

centered "*tap* *tap*"
"Lilly said she was still deciding, and I doubt she'd just say that to ease our minds while she's already certain what she's going to do."

play sound sfx_taps2

centered "*tap* *tap* *tap*"
"Especially not with Akira sitting nearby."

play sound sfx_taps3

centered "*tap* *tap* *tap* *tap* *tap*"

show bg school_dormhisao_ni:
    right
    zoom 1.2
with dissolve

"It takes another moment before I realize the strange sound is coming from my door. It's as if a dog is scratching it on the other side."
"Is that Kenji? It's kinda late for him to try and bug me about something."

play sound sfx_taps4

centered "*tap* *tap* *tap*"
"At least he's being more considerate than usual. Usually he bangs on the door with enough force to wake up everyone in the building."

show bg at left
with charamove

play sound sfx_lightswitch_on
with Pause(0.1)
show bg school_dormhisao_ss
with None

"I get out of bed, turn on the lights, and unlock the door, but before I can prepare a lecture about the importance of someone's daily eight hours of rest…"

show hanako def_worry at offscreenleft:
    matrixcolor BrightnessMatrix(-1.0)
    xzoom -1.0
with None
show hanako at offscreenright
with charamovefastest

"…the door flies open and someone zips past me before I can even react."
hi "Dammit, Kenji, what the fu-{w=0.2} Hanako?"

show hanako emb_timid_close_ss at offscreenright:
    matrixcolor BrightnessMatrix(0.0)
    xzoom 1.0
with None

show bg:
    xpos 1.0 xanchor 1.0
show hanako at closeright
with charamove

"Sure enough, the unexpected visitor who forced herself into my room in such a blunt manner is none other than my girlfriend who's standing in front of me with a nervous expression on her face."
ha "Ummm… D-did I w-wake you up?"
hi "The noise you made was hardly enough to qualify as knocking. If I had already been asleep there's no way that would have woken me up."
ha "I-I didn't want to r-risk waking up anyone else."
"Good point. Sneaking across campus and into the guys' dorm at night was already a risky move, especially on her part, but causing a ruckus in the middle of the dorm hallway would be a scandal in its own right."
"Kenji would probably flip if he found a girl knocking on doors here at night."
"He's already convinced Hanako's burns are the results of a bra-burning gone horribly wrong. He'd probably take her presence here as a sign that the feminist movement was getting ready for nocturnal deportations or something equally outlandish."
hi "It's okay."
"I'd ask her what she came to do here, but I already have a pretty good idea."
hi "Do you want to stay here for the night? I'm okay with it if you do."

show hanako emb_smile_close_ss
with charachangealways

"She gives me a faint smile and nods softly."
ha "T-thanks. I could use some… comfort."

hide hanako
with charaexit
play sound sfx_rustling

"She sits on my bed and starts removing her shoes and stockings."
"I swallow a lump in my throat. Does she mean {i}that{/i} kind of comfort? She's not even asking me to turn around."
hi "H-Hanako, by ‘comfort’, do you mean {w=0.5}{i}comfort{/i}?"
"She unbuttons her blouse and pulls it off in a single move, revealing her…{w=0.5} nightgown?"

show hanagown worry_close_ss
with charaenter

ha "J-just c-comfort."
"Looks like I just dodged a bullet there."
"I try to recall what I've been reading lately. Whatever it was, I'd better avoid it in the future."
hi "Of course."

hide hanagown
with charaexit

with Pause(0.5)
play sound sfx_lightswitch_off
with Pause(0.1)
show bg school_dormhisao_ni
with Pause(1.0)

play music music_night fadein 4.0

"After Hanako has finished taking off her blouse and skirt and putting them in a neat pile beside my clothes, I turn off the lights and get back into bed."
"Moments later, I can feel her lying down next to me and snuggling up to me."
"For several minutes, we just lie there, holding each other, lazily playing footsie and me softly stroking her hair and scalp; something I've lately learned she really likes."
"On my first impression I didn't really have Hanako pegged for a very physical person. She already tended to get nervous when people came near her, and I expected being touched would probably cause her to flee the scene in a heartbeat."
"I started having second thoughts about that impression when she got drunk and really clingy with me during her birthday party. And after I started dating her, I discovered that beneath her skittish nature, Hanako's actually quite the snuggle bunny in private."
"I continue running my hand through her hair until I can feel her relax and lay her head on my chest so she can listen to my heartbeat; another thing she likes to do."
"I'm not sure if she wants to talk to me about this or simply wants physical comfort. In a way, it's already a good thing she came here instead of pretending nothing's wrong and bottling up things inside."
hi "Do you want to talk for a bit?"

show hanagown smile_close_ni
with charaenter

ha "Y-yes."
hi "How do you feel about Lilly's announcement."

show hanagown distant_close_ni
with chchange

ha "I f-feel sad. My first thought was ‘why now?’"
hi "Huh?"
ha "L-lately I've started to become more motivated to turn my life around. L-like you have. That i-includes my friendship with Lilly."
ha "B-but now I wonder if I'll even get the chance for that."
hi "Maybe you should tell her that. Your word might just tip the scales. I wouldn't be surprised if you were one of the main reasons she's still not sure what to do."

show hanagown worry_close_ni
with chchangefast

ha "{i}M-m-me?{/i} What do you mean?"
"I take a moment to put my thoughts in order."
"I don't think I'm wrong about this, but how do I best explain this to Hanako?"
hi "Akira made her choice with her career in mind, but Lilly doesn't seem to have any ambitions of getting a big-shot corporate job."
hi "The last time we spoke about figuring out what to do after Yamaku, you mentioned Lilly wanted to study English, didn't you?"

show hanagown normal_close_ni
with chchange

ha "Yes. She wants to be an English teacher."
hi "She can study English in Scotland as well. It doesn't matter what she does concerning her education."
hi "Heck, her parents might just hire private tutors, seeing that they seem well-off. And she can find a job as a teacher either here or there. Over there, she could also teach Japanese if she liked."
ha "Uh huh…"
hi "So what else could determine her choice? There's relatives, I guess. Lilly said it's been six years since she last met her parents before that last trip."
hi "I had the impression this evening that Lilly and Akira are estranged from their family. Did Lilly ever mention them to you?"

show hanagown distant_close_ni
with chchange

ha "N-no. She talks about Akira all the time, but never brings up her parents."
ha "I don't think she talks to them very often. She phones her sister every few days, but I've never seen or heard her talk to her parents either."
hi "How do you think she feels about them?"
hi "Akira doesn't like them, that's impossible to miss. But Lilly wasn't that blatant with her opinion."
ha "I'm really not sure. I think she's neutral about them."
hi "Neutral? Is that even possible?"

show hanagown worry_close_ni
with chchange

ha "She seemed uncomfortable by Akira's outbursts about their parents, but didn't defend them in any way."
hi "She's definitely not neutral towards Akira though. And Akira will be migrating. The only other family she has contact with around here seems to be Shizune and that's hardly positive contact."
hi "So if she doesn't dislike her parents and the sister she loves is leaving for a country where Lilly herself will have no problems finishing her education, why exactly {i}is{/i} she still trying to make up her mind? Shouldn't the decision be easy?"
ha "S-she has many friends here too."
hi "True, but the two of us seem to be the only ones she regularly invites to her room, and we're the ones she took along to her family's summerhouse in Hokkaido."
hi "And while I'm sure Lilly considers me a good friend, I think the title of best friend goes unavoidably to you."
hi "If there's one person she could be considering staying here for, it has to be you."

show hanagown distant_close_ni
with charachangealways

"Hanako falls silent for a long while, the gentle rubbing of her feet against mine the only indication she hasn't spontaneously fallen asleep."
"I don't think she disagrees with the logic behind my argument. It's probably her own unsteady sense of self-worth that's denying the possibility someone else could consider her important enough to decline an emigration opportunity for."
"Still, after a long deliberation, she silently nods."
hi "So I think if you don't want her to go, you should consider asking her to stay. Or if that prospect makes you uneasy, perhaps I could…"

show hanagown worry_close_ni
with chchangefast

ha "NO!"
"Her sudden exclamation startles me a bit which in turn startles her."

show hanagown normal_close_ni
with chchange

ha "Ummm… I mean, p-please don't."
hi "Why not? I realize it's not a competition and Lilly's not a prize to be won, but her parents don't seem to mind doing their part to help her reach a decision if Akira is to be believed."
hi "You don't have to nag her about it, but making your position clear can't hurt in my opinion."

show hanagown distant_close_ni
with chchange

ha "B-because… ummm… Because…"
"She hesitates for a bit, then mumbles something."
hi "I can't hear you very well."

show hanagown worry_close_ni
with chchange

ha "B-because that would r-ruin what our f-friendship is about. Or rather… what I'd l-like our friendship to b-be about."
hi "Could you explain that to me?"

show hanagown distant_close_ni
with chchange

ha "S-sometimes I wonder if Lilly thinks of me as a true f-friend or simply as someone who needs looking after."
ha "Because despite her always being there for m-me, I haven't been able to do anything for her."
ha "Even now, while she was struggling with this s-summons, I couldn't help her."
hi "But you can now."
hi "She wasn't planning to tell us, but we found out and now we can be there for her, right? You can be there for her just like you're here for me."

show hanagown worry_close_ni
with chchange

ha "M-maybe. But I don't want to ask her to stay for my sake."
ha "W-what if she would rather live with her f-family and m-me asking her to stay would make her stay here out of a s-sense of duty towards me?"
ha "W-what kind of friendship would we have then?"
hi "In the end, the decision remains with her, Hanako."
hi "If we're not going to ask her to consider staying here, the only other thing we can do is cross our fingers and support her choice, no matter what it is."

show hanagown smile_close_ni
with chchange

ha "A-and provide some distraction when she needs it."
hi "According to Akira, the departure will be soon. Maybe we should postpone our dates for the time being and focus on hanging out with Lilly."

show hanagown worry_close_ni
with chchange

ha "H-Hisao…?"
hi "Yeah?"

show hanagown distant_close_ni
with chchange

ha "If… the two of us… hang out with Lilly all the time… she'll feel like… the third wheel and might b-back away from us."
hi "Then maybe it should be just you spending some additional time with her for a while."

show hanagown worry_close_ni
with chchange

ha "B-but you're my boyfriend."
hi "I'm not going anywhere."
hi "You just hang out with Lilly, and maybe you'll get around to convincing her to stay here, even if you don't end up asking her directly."

show hanagown smile_close_ni
with chchange

ha "Okay."
hi "Hanako?"
ha "Yes?"
hi "If I don't go to sleep soon I'll miss my morning jog tomorrow. And Emi cursing like a sailor is a very ugly sight."
ha "G-goodnight then, Hisao."
hi "Goodnight, Hanako."
ha "And Hisao?"
hi "Yes?"
"She gives me a quick kiss."
ha "…thank you."

stop music fadeout 3.0
scene black
with Dissolve(3.0)

return