label sisterhood_ch7:
label .sh_ch7:

call sisterhood_timeskip

scene bg school_scienceroom at left
with Dissolve(1.0)

play music music_normal fadein 0.5

nvl clear
nvl show dissolve

n "Ten more minutes until lunch break."
n "We've already completed the assignment we were given, so now I've taken out one of my library books and am trying to finish a chapter before the school bell rings."
n "Truth be told I'm still a little tense, so it's not going as quickly as I had been hoping for. The reason for the tension I feel is the fact I just completed my first group assignment in class - the occasional assignments I do with Hisao notwithstanding."
n "Or rather, my first group assignment that didn't end in disaster, like some time ago in science class, when I was struck with a panic attack. And Hisao wasn't even part of the group I worked with today, or things probably would have been less awkward."

nvl clear

n "Today in Japanese class, we were instructed to work in groups of three people maximum and write a short piece on parliament elections. Hisao immediately got up to join me, only to be pushed back into his seat by Misha and being forced into a heated discussion about having dodged a student council assignment the other day."
n "I don't think it was meant to be a public argument, but Misha is very easy to eavesdrop on. I was familiar enough with Shizune and Misha, as well as Hisao's playfully tense relationship with them, to figure out that they were going to use that group assignment as an excuse to drag a promise out of him to make up for it somehow."
n "All of this meaning the chances of Hisao doing group work with me just dropped to exactly zero; a suspicion confirmed by an apologetic shrug on his part."

nvl clear

n "Just as I got ready to start the assignment on my own, I noticed Hisao was making a gesture with his head towards a point to my right."
n "I followed his gaze and noticed my two neighbors on the right side were the only students not part of a group of three yet."
n "My eyes grew wide as I realized his intention. Was he telling me to join some other group just like that?"
n "I quickly shook my head and gave him a begging look, but he just made a gesture towards Shizune as if to say “matters are out of my hands”."
n "Later on, I started wondering whether he was really unable to ditch the student council duo or whether this was a subtle attempt on his part to help me widen the circle of people I could have social interaction with."

nvl clear

show natsume basic_neutral_close:
    xanchor 1.0 yalign 1.0 xpos 1.15 alpha 0.0
show naomi basic_neutral_close:
    xanchor 1.0 yalign 1.0 xpos 1.4 alpha 0.0
with None

show bg at right
show natsume:
    xpos 0.80
    ease 1.0 alpha 1.0
show naomi:
    xpos 1.05
    ease 1.0 alpha 1.0
with charamove

with Pause(0.5)

show natsume:
    ease 1.0 xpos 1.15 alpha 0.0
show naomi:
    ease 1.0 xpos 1.4 alpha 0.0
with None

show bg at left
with charamove

"I took another look at my neighbors only to quickly look away when they caught my gaze."

hide natsume
hide naomi
with None

show hisao basic_smile_uni at center:
    zoom 0.85 xalign 0.2 yalign 1.1
with charaenter
show hisao basic_grin_uni
with charachangealways

"I looked back at Hisao again, and this time he was smiling at me."
"I knew that expression; I came to know it as his “everything will be alright”-smile."

hide hisao
with charaexit

"It didn't do a lot to inspire confidence in me this time, though."
"In all my time in this class, I could count the words I exchanged with my neighbors on one hand, and I had no clue why they would even want to work with me after I spent the better part of two years trying to avoid even basic interaction with them."

show bg at right
with charamove

ha "Ummm…"
"As usual when faced with an unexpected social situation, my mind completely froze up, and I couldn't come up with even a single way to formulate that simple request that most people could make without even having to think about it."
"The fact that my neighbor is a very outgoing person herself didn't exactly ease my mind."
ha "E-exc…e-excuse me…"

show naomi basic_neutral_close at tworight
show natsume hands_neutral_close at twoleft
with charaenter

"That got their attention."
"The girls looked at me, and when I didn't reply, they looked at Hisao who gave them a quick nod."

show naomi bend_smile_close
show natsume hands_smile_close
with chchange

"My neighbor gave me a cheerful grin."
na "Looking for a group to work with, Ikezawa?"
"I gave them a timid nod."
na "No probs. Feel free to tag along. Three know more than two, right?"
"As I moved my desk over to theirs, my neighbor Naomi wasted no time in making conversation."

show naomi basic_grin_close at tworight
with chchange

na "Bet you were disappointed you couldn't work with Nakai this time, weren't you? You two usually do assignments together these days."
na "Heh, I guess the powers that be decided otherwise, didn't they?"
"Am I really supposed to answer all of that?"
na "You're usually not big on group work, aren't you? Didn't something happen that time before in science class?"

show naomi basic_laugh_close
with chchange

na "Don't worry, stuff like that happens to the best of us."
na "But you know that, don't you? You're usually stuck with the front row seat when I short out."
"The last statement was accompanied by a cheerful wink."
"{i}Too many questions!{/i}"
"While I was still reeling from Naomi's verbal machinegun fire, her neighbor Natsume cut in with a question of her own."

show natsume basic_smile_close
with chchange

nt "Japanese is one of your stronger subjects, is it not?"
"I responded with another meek nod."
"It's true, Japanese is probably my best subject. It was one of the benefits of being a bookworm."
"The fact that I was fairly confident I'd be able to pull my weight on this assignment was one of the things that made the whole thing slightly easier."
na "Great, then we'll finish this all the sooner."
"Naomi seemed eager to begin, and I quickly nodded in order to avoid more conversations."
"We divided the workload into three parts and got to work."

show naomi basic_focus_close
show natsume basic_neutral_close
with charachangealways

"While writing my section of the piece, I occasionally observed my new group mates."
"Natsume and Naomi remind me a bit of less extreme versions of Shizune and Misha."
"Natsume wears glasses and has a stern appearance, but isn't as bossy or forceful as Shizune."
"The most striking part of Naomi's appearance is her hair which, while not dyed like Misha's, is bleached to a distinct light blonde color."
"Her personality is a bit like Misha's as well - up-beat, loud and a bit hyper, though Naomi's volume control button doesn't seem to be permanently stuck on the max setting."
"Also, like Shizune and Misha, the two seem together constantly."

hide naomi
hide natsume
with charaexit

"We finished the assignment with a good amount of time to spare and my group mates had started on a piece of homework I already finished the other day."
"If I had been working with Hisao, we'd probably have spent the remaining time talking with one another, but I don't think I'd be able to have small talk with my new group mates."
"Keeping semi-normal interaction going with them had already drained most of my energy, and the tension I felt during our working session isn't fading nearly as quickly as I hoped."

play sound sfx_metalclink

show naomi basic_shock_close at tworight
with Dissolve(0.2)

na "Well, CRAP!"
"I look at Naomi from behind my book, startled by her sudden exclamation, and see her wrestling with a pair of compasses."
"She's been playfully fiddling with them over the course of the entire assignment and now she seems to have jammed them somehow."
na "Natsumeee…!"

show natsume hands_neutral_close at twoleft
with charaenter

nt "They were never meant to be used to grind little pieces of your eraser into powder."
na "I know. I know. Now can I just…"
nt "I left mine in my dorm room. I already finished that question this morning before heading to classes."
"She lets out a disappointed sigh."
"After a few more seconds of trying to get her compasses unstuck, Naomi suddenly turns to me, causing me to instinctively raise my book as if to shield myself."

show naomi bend_smile_close
with chchange

na "Hey Ikezawa, don't you have a pair of compasses I could use?"
na "Just for a sec. I'll be really, really careful with them. Okay? Just to complete this little graph. You'll have them back in the blink of an eye. Pretty please with sugar on top?"
ha "I-I d-don't have any of t-those."

show naomi basic_neutral_close
with chchange

na "You don't? Then how did you take care of that problem where we had to draw up that pie chart as part of the answer?"
ha "I t-t-typed it up."
na "Huh?"
"I sigh inwardly."
"I don't think I'd be able to finish a verbal explanation without it taking another hour, so I reach into my bag and just show her the answer sheet I put together the day before."
"It's all neatly typed out using one of the school's computers, and I used the word processor's graph features to generate the pie chart."

show naomi basic_shock_close
with chchange

na "Oh hey, that first answer is totally different from what I had. I wonder if I missed something or if you were simply over thinking the…"

show naomi basic_smile_close
with chchange

na "Eh, never mind. That's pretty neat you put together your answers like that. Do you often use computers to type up your homework?"
"Why is she so interested?"
ha "S-s-sometimes, b-but not v-very often."
"I mostly use the school computers to put together essays or other homework that requires a lot of writing. The scar tissue on my right wrist sometimes hampers my movement a bit, so I'm not a very quick writer."
"Typing out my homework can be a big time-saver at times. The only downer is the fact the computer lab has no quiet little corners, meaning I only use the place when it's nearly deserted, which isn't very often."
"Naomi seems satisfied with my answer, and I return to my book."

hide naomi
hide natsume
with charaexit

"As I turn another page, I'm starting to notice something is different."
"Naomi and Natsume are no longer working on their homework, but are speaking to each other in whispers too quiet for me to make out, and they occasionally look in my direction."
"I wonder if it's about me."
"I get very uncomfortable."
"Are they gossiping about me?"
"Both are members of the newspaper club which is responsible for writing and printing the school newspaper, and Naomi in particular loves to keep on top of the local rumors floating around."
"Is acute indiscretion an officially recognized condition? If so, she'd probably be diagnosed with it."

show naomi bend_smile_close
with charaenter

"As if to confirm my suspicions, Naomi suddenly addresses me with a conspiring smile."
na "Hey, Nakai is still your boyfriend, isn't he? I mean, you guys haven't broken up yet or anything, right?"
"I visibly reel back from the impact of this blunt question and barely manage to shake my head."
ha "W-we're s-still d-dating."

show naomi bend_laugh_close
with chchange

na "You know, as of last week you're officially dating a geek. You're not put off by nerdy traits in your guys, are you?"
"Your guys? She's talking as if I've been dating boys ever since I enrolled here."
"I know what this is about though. A new club was formed last week and our homeroom teacher Mutou is in charge of it."
"It's a science club, of course… The only kind of club he'd have interest in setting up. And I'm currently dating its sole member."
"It's a bit weird, but Hisao said the club's main activity, reading and discussing scientific literature, has been pretty fun so far."
ha "Er…"

show naomi bend_smile_close
with chchange

na "It's kinda sad there's still only one member though. I suppose you're not joining to flesh out membership?"
"I did actually offer to join, but Hisao shot that suggestion down almost immediately."
"“Science isn't really your thing, Hanako,” he told me. “It'd just feel like class to you. If you want to join a club, you'd be better off finding something that actually captures your interest.”"
"I couldn't really argue with that. Unlike Hisao, who seems to have a knack for deciphering Mutou's convoluted lectures, I'm not exactly a star pupil in science class, and it's hardly my favorite subject."
ha "N-no, I'm n-not."
na "But you won't be able to hang out with your boyfriend after school hours, because he's in a club and you're not, right?"
"What is she trying to get at?"

show naomi at tworight
show natsume basic_neutral_close at twoleft
with charaenter

"Natsume, who had remained silent during the whole interrogation put her hand on Naomi's arm to indicate she wanted to say something."

show natsume hands_smile_close
with chchange

nt "What Naomi is trying to ask you is if you'd be willing to help out the newspaper club with an emergency situation for a few days."

show naomi basic_shock_close
with chchangefast

na "Hey, I was still getting to that point!"
ha "H-help out?"
"Is this a veiled recruiting attempt?"
ha "And why me? There's probably dozens of other students more suitable."

show naomi basic_smile_close
with chchange

na "Yeah, you probably know we're both members there."
na "Most of the members write or collect stories for the school newspaper, but we also have someone to put them together on the computer before we send the whole thing to the copy shop."

show naomi basic_neutral_close
with chchange

na "At least, we usually do."

show natsume hands_neutral_close
with chchange

nt "Unfortunately, the girl who usually does the job is out of commission for a little while. She injured herself a few days ago and certainly won't be able to help before the deadline."
na "Yeah, she broke her hand after tripping outside her dorm room. She has this thing called os{cps=5}…{/cps}osto-{w=0.7}something."
na "Anyway she breaks easily. And now we need someone who can do the data entry and some minor editing jobs in her place for a few days."
ha "B-but w-w-why me?"
nt "There aren't that many students here who aren't already part of another club or don't have other tasks like class representative duties to tend to and who are also capable with computers."
nt "When we saw the way you made a digital print of your homework, we thought you might be able to help us out."

show naomi basic_smile_close
with chchange

na "Yeah, I mean, it's not a really complex task. And there's not a lot of distractions there either. The place the club uses has a small side room where we keep the computers and archives."
"I really don't know about this. The idea of getting involved in a club with nothing but people I'm unfamiliar with sounds terrifying."

show naomi bend_smile_close
with chchange

na "You don't have to decide right now, you know? But it'd be good if we got a yay or nay before the end of tomorrow."
ha "Well… I…"

play sound sfx_normalbell
play ambient sfx_crowd_indoors fadein 2.0

hide naomi
hide natsume
with charaexit

"While I'm still fumbling with my words, the school bell sounds, and most people immediately start getting up."
"Hisao collects his things, quickly gets away from Shizune and Misha and approaches my desk."

show hisao basic_smile_uni_close:
    xanchor 1.0 xpos 0.0 yalign 1.0 alpha 0.0
    ease 1.0 xalign 0.1 alpha 1.0
with None

show bg at left
with charamove

hi "Hey Hanako. Sorry about not being able to team up. Did you complete the assignment?"
ha "Y-yes, we even managed to finish ahead of time."

show hisao cross_smile_uni_close:
    xalign 0.1 alpha 1.0
with chchange

hi "Great. Let's head to the tea room, then."
"Phew. Saved by the cavalry."
ha "S-sure, I'll be with you in a second."

hide hisao
with charaexit

"As Hisao starts heading towards the exit, Naomi suddenly addresses me again."

show naomi bend_smile_close:
    offscreenright alpha 0.0
    ease 1.0 xalign 0.9 alpha 1.0
with None

show bg at right
with charamove

na "Hey Ikezawa, just to reassure you; this isn't a recruiting attempt, though we always welcome new members of course."
na "But if you'd be willing to help out the newspaper club, we'd be really thankful."
na "Think about it, okay?"

hide naomi
with charaexit

"Without waiting for a reply, Naomi and Natsume gather their belongings and walk off past Hisao who has turned around and is looking at me with a curious expression on his face."
"Wait… Did he overhear?"

show hisao cross_grin_uni_close
with charaenter

hi "That sounded pretty interesting, Hanako."
"I can only sit there with my mouth agape as I realize that my cavalry has just been turned into Naomi's cavalry instead."

stop music fadeout 0.5
stop ambient fadeout 0.5

scene bg school_miyagi
show lilly basic_surprised_close at twoleft:
    zoom 0.9
show hisao basic_neutral_uni_close at tworight
with locationskip

play music music_lilly fadein 0.5

li "Were you really asked to join a club?"
"As expected, the main talk of our lunch break was Naomi's proposal. Lilly was understandably surprised to hear of this sudden development."
ha "I-it's not really about joining. They have a deadline for the end of the week and need some help."
li "Have you already decided what to do?"
"I haven't. On the one hand, I must admit I'm a bit curious."
"On the other hand, Naomi and Natsume, with whom I've never even really interacted before, are the most familiar people in there, and I can't really say their presence is a calming factor for me."
"While I don't think Naomi is the kind of person to hold a grudge, the fact remains that if I mess up or disappoint somehow, classes will become much more uncomfortable. Naomi and Natsume will still be my neighbors until the end of the school year."
ha "N-no, I haven't."

show hisao basic_grin_uni_close
with chchange

hi "Someone told me not too long ago that it's important to seize opportunities if they're handed to you on a platter like this."
"Hisao has decided to jump into the fray too."
"I roll my eyes at his remark. Those are the exact same words I used last week to convince him to give Mutou's science club idea a chance."
"At first he was reluctant, afraid he'd have less time to spend with me. The last thing I wanted to do was hold him back, so I did my best to convince him to give the whole thing a try."
"I knew the subject interested him, and I hoped this would also encourage him to make more definite plans for his future. He consistently scores the highest marks in class in Mutou's subject, and I genuinely believe that he'd do very well if he went for a career in that direction."
ha "I-I know I said that last week. I'm not ruling the opportunity out r-right away."

show hisao basic_smile_uni_close
with chchange

hi "You could choose to see it as a sign that fate is extending you a helping hand."
"By breaking somebody else's? That's kind of a cruel way to motivate someone. Fate must know how easily I can be guilt tripped."
"I merely nod. I don't believe the work itself will give me much trouble."
"What scares me is the idea of being thrown into a group of unfamiliar people who might stare at my scars, who might be put off by my stammering -- which always gets worse whenever I'm feeling nervous -- my shyness and inability to make conversation."
"A few weeks ago, I was still the “shy kid who kissed her first boyfriend in public” to people, but tomorrow I might be the “shy kid who panics at the most mundane things” once again."

show hisao cross_speak_uni_close
with chchange

hi "Anyway, if you're considering it, it might be best to go this afternoon. I could pick you up afterwards when I'm done with my club meeting."
hi "If you're nervous and wait until tomorrow, you might lose sleep over it."
"That's a pretty good point. Knowing myself, I'd probably mull over it all night long, and I'd only become more prone to messing up."
ha "O-okay, I'll give it a t-try after classes t-today."

show lilly basic_satisfied_close
show hisao cross_grin_uni_close
with chchange

"Lilly claps her hands excitedly upon hearing my words."
li "Wonderful!"

show lilly basic_cheerful_close
show hisao cross_smile_uni_close
with chchange

li "I hope you two will be willing to join me for some tea tonight. I'd really like to hear how things played out."
"I smile."
"It's been a while since we last sat together in Lilly's room to talk and relax. Having something to look forward to will make things easier."
ha "T-that would be nice."
hi "We'll be there, Lilly."

stop music fadeout 0.5

scene bg school_newspaperclub
show naomi basic_smile at tworight
with locationskip

play music music_comedy fadein 0.5

na "So while the classroom is the place we use as an editorial office, most of the editing takes place here."

show naomi at twoleft
with charamove

na "We have two computers here, though only one is regularly used. The other's more like a digital archive. You can take a look at it later for examples of how we've been doing things."

show naomi at center
with charamove

na "And here's the cabinet where we store most of our equipment. It isn't very large as you can see."

show naomi basic_neutral
with chchange

na "Oh hey, you're not claustrophobic, are you?"
ha "N-n-no, I'm n-not."
"Naomi was visibly surprised when I showed up at their club's classroom after school, but wasted no time giving me a brief tour."
"Good thing only she and Natsume were around when I arrived."
na "I think Jun, the girl who is usually doing this, has some templates saved which she uses for the various pages of each issue."
na "But that's not really the number one priority we have at this point. The most important thing to do now is to get all the stuff we have digital."

show naomi bend_smile
with chchange

na "By the way, do you have any questions so far?"
ha "Ummm… s-so I j-just t-type up the a-articles you wrote?"

show naomi bend_laugh
with chchange

na "Eager to get started, huh? Neat."
"More like eager to end this one-sided conversation."

hide naomi
with charaexit

"Naomi opens the nearby cabinet and fishes out several small digital recording devices and a flash drive."

show naomi basic_smile at center
with charaenter

"Putting them and a small pile of hand-written notes on the nearby desk, she makes a sweeping gesture over it."
na "Here's what we have so far! Jun has already made a folder for the upcoming issue and a shortcut on the desktop."
na "This memory stick is from Kaoru. He likes to type up all his articles himself, so all you have to do is copy them to the right folder and then print me a copy to look it over."
"She takes out one of the recorders and picks up a small USB cable from the desk."

show naomi basic_neutral
with chchange

na "Several of our members use these to compose their contributions."
na "Hideki's completely blind and not too tech-savvy, so he just dictates his articles. Natsume uses these too whenever her joints are hurting."
na "Like… the last few days. Anyway, just plug one of these in with this cable here, and the application for playing the contents should start automatically. It'll be easier than rewinding and replaying manually."
na "Always check the sections at the very end first. They often contain comments on whether to omit or alter certain portions. And the written notes here just contain articles and interviews by the rest."
ha "I-I'll s-start p-putting these in then."

show naomi basic_laugh
with chchange

na "Cool. I'd do this myself, but I can't sit in front of monitors for very long for a while."
na "Nurse's latest orders. I can be a bit sensitive to them. They sometimes cause, you know, short-circuiting."
"I know alright. Naomi's reason for attending Yamaku is a pretty heavy case of epilepsy, and over the years, she's had several harsh episodes right next to me in class."
"The first time she fell out of her chair and started thrashing around on the floor got me so riled up I couldn't sleep for days. I'm still not completely used to it."

show naomi basic_smile
with chchange

na "Anyway, be sure to let the computer do a spelling and grammar check on everything to save ourselves some trouble later."
na "You have any questions, Natsume and I'll be in the other room."
ha "A-alright."

stop music fadeout 0.5

scene bg school_girlsdormhall
show hisao basic_smile_uni_close
with locationskip

play music music_dreamy fadein 0.5

"Having left Lilly's room, I unlock the door to my own bedroom and prepare to kiss Hisao goodnight and retire for the day when he stops me."

hi "Can I come in for a little while?"
ha "S-sure."

play sound sfx_dooropen

scene bg school_dormhanako
with locationchange

"We go in, and he sits next to me on the bed."

show hisao basic_speak_uni_close at sittingpos
with charaenter

hi "You're going back to the newspaper club tomorrow, aren't you? Even though you said you didn't know yet."
ha "I… I think I want to at least finish what I started today."
"That isn't the only reason. I also want to start feeling more reliable."
"For a long time, I've felt like a useless person, unable to be there for others."
"Today, I had an opportunity to deconstruct that belief, but my social anxiety nearly ruined it for me. Even though Naomi and Natsume were friendly, I felt on edge all the time."
"By the time we went back to the dorms, I felt exhausted. Even though we just had tea with Lilly, I'm still tense all over."

show hisao basic_worry_uni_close
with chchange

hi "You look tired. And tensed up."
ha "D-do you think I s-should skip tomorrow?"
hi "I don't think I can make that decision for you."

show hisao basic_smile_uni_close
with chchange

hi "But if it helps, I might be able to help you relax a little bit. Do you want to?"
"He sits back a bit, spreads his legs and gestures me to sit in front of him."
"I smile."
ha "Y-yes, please."

hide hisao
with charaexit

"I sit in front of him, drape my hair over my shoulders and gently pull the shoulders of my nightgown away, causing it to slide down to just above my breasts."
"I let my chin rest on my chest and try to relax."
"I hear him rub his hands together for a bit and then feel one touch my exposed left shoulder."
hi "Wow, your shoulders and your neck are really stiff this time."
ha "I'm… not very good with people, so situations like these will probably always cause me stress."
hi "Even though people were friendly today?"
ha "I-It's not something rational. I really wish it was. It'd be a lot easier to control."
"He starts carefully rubbing and kneading my neck and shoulders."
"We've been giving each other these little massages for a while now, and I've really come to enjoy them."
"While I can't feel the sensation of his hand touching and rubbing the skin of my right shoulder, I still feel the result in my muscles there afterwards. It almost feels like I'm challenging my condition this way."
hi "But it'll get less as you get used to it, right? You used to be awkward in my presence too, remember?"
ha "Y-yes. It will get less as long as I can manage to keep going. At least, I hope it will."
hi "Then we'll keep helping you relax afterwards."
hi "Lilly and me. We'll just repeat this evening tomorrow. And the day after tomorrow. Until it's no longer necessary."
ha "T-thank you, Hisao."
"We remain silent for a few minutes as Hisao finishes massaging my shoulders, neck and upper back."
"He moves back, gives a quiet nod to me, and I lie down and let my head rest in his lap."

scene black
with shuteye

"I close my eyes as his hands start massaging my scalp and temples."
hi "Does it feel good?"
ha "Yes."
"…"
hi "Hanako?"
ha "Hmmm?"
hi "Do you have any plans for the upcoming weekend?"
ha "Not really."
hi "Would you like to go on a date the upcoming Saturday?"
ha "Sure."
hi "Great. We'll have a bite to eat at the Shanghai around six and then be on our way."
ha "Do you already have something planned?"
hi "Yep. I was already planning it before this whole newspaper club business came up."
ha "What is it?"
hi "A surprise."
ha "Awww…"

scene bg school_dormhanako
with openeye

"Hisao finishes his massage with a ruffle of my hair. I get up and fix the shoulders of my nightgown."
hi "Loosened up a bit?"
ha "Yes, it really helped."

show hisao basic_grin_uni_close at sittingpos
with charaenter

"As I turn around to face him, Hisao gives me a playful wink."
hi "If you want me to give you a more extensive massage…"
"As I grasp the meaning behind his remark, I reflexively turn my head away although I doubt my attempt at hiding my extensive blush is successful."
"Lately there have been a few times we started with a mutual backrub and ended up… doing… what we did that night in Hokkaido."
ha "N-n-not t-this t-time."

show hisao basic_smile_uni_close
with chchange

hi "Okay."
ha "Ummm…"
hi "Yes?"
ha "C-can I return the favor, Hisao?"

show hisao basic_speak_uni_close
with chchange

hi "You don't really need to. I'm not feeling tense right now."

show hisao at center
with charamove
show hisao basic_neutral_uni_close
with chchange

"As he gets up from the bed, I grab hold of his hand."
ha "Umm… P-please?"
"Hisao gives me an extended analytical stare that makes me nervous, but then gives a quick nod, sits down in front of me and starts unbuttoning his shirt."

show hisao basic_smile_uni_close
with chchange

hi "Alright then, Hanako."

stop music fadeout 0.5

scene bg school_newspaperclub
show naomi bend_laugh
with locationskip

play music music_comedy fadein 0.5

na "Nice! You got all content digital now?"
ha "Y-yes. Everything."
na "Great, that was pretty quick overall."
"It was more work than I expected. Especially the audio recordings took a while to type up. But now all articles and interviews are saved as documents."
ha "T-thanks."

show naomi bend_smile
with chchange

na "Could you print them all out? The pictures and templates for all the pages too. And then come and sit here next to me."
ha "I-I'm not done yet?"
na "I can't force you to do more than you want, but there's still something else to do and we're getting to the part that I think you'll like."
"I simply nod and return to the computer room."

stop music fadeout 0.5

scene bg school_newspaperclub
show naomi basic_focus
with shorttimeskip

play music music_comedy fadein 0.5

"A few minutes later I return to Naomi with a stack of paper containing everything I digitized over the last two days."
"Naomi is usually loud and somewhat chaotic, but in her role of editor-in-chief she becomes a bit more serious and structured than usual and I have an easier time keeping up (and putting up) with her."

show naomi basic_focus_close
with characlose

na "So here's the templates we have for each page of the newspaper. Now we're gonna have to see what articles go where."
na "We have the front page for the main article, five pages for internal news, three pages for external news, one page for advertisements, one page for columns and one page for sponsor-related stuff."
ha "So n-now what?"

show naomi basic_neutral_close
with chchange

na "Each article has a number. So now we take a few empty sheets of paper and each try to come up with a layout that'll get us the articles in the places we want."
ha "T-two layout proposals?"

show naomi basic_smile_close
with chchange

na "It's nice to have a second opinion. Just try to estimate how much space each article will take up and how much redundant content each article has that can be cut or shortened."

hide naomi
with charaexit

"We spend the next hour trying to come up with our own layout."
"I do my best not to look in Naomi's direction in order to avoid copying her idea."
"After I hand in my proposal, she puts the two sheets of paper side by side."

show naomi basic_neutral_close
with charaenter

na "Looks like we have similar ideas on a lot of stuff."

show naomi bend_smile_close
with chchange

na "But I didn't think of putting that article about the exposition into external news instead of internal."
ha "I-I thought i-it could fit b-both. I-it's being organized b-by a teacher from here, b-but t-together with an ex-external p-party and n-not on the school grounds."

show naomi basic_focus_close
with chchange

na "Maybe. Maybe. It'd save us from having to severely truncate that story about the baseball tournament."

show naomi basic_smile_close
with chchange

na "Okay, we'll go with my layout with the exposition story moved from page five to page eight instead."
na "Could you paste the contents into the template pages? You'll run outside the borders in several places, but we need to know what articles to trim or reword a bit."
na "You can fiddle a bit with the pictures on page two, five and six as long as the faces remain recognizable."

show naomi basic_laugh_close
with chchange

na "Let's get started."
ha "Y-yes."
"I quickly get to work. We only have one and a half days to get everything done."
"I'll have time to relax this evening, but until then, I feel pressed to work as swiftly as possible."

stop music fadeout 0.5

scene bg school_dormlilly
show lilly basic_listen_close at twoleft:
    zoom 0.9
show hisao basic_neutral_uni_close at tworight
with locationskip

"Barely breathing, I wait as Lilly runs her slender fingers across the last page of the newspaper's Braille edition."
"Since she appears to be getting close to the end, her fingers must be near the staff section right now."

show lilly basic_smileclosed_close
with chchange

"Suddenly, her fingers stop and skim over a section a second time. It looks like she read the part that bears my name."

show lilly basic_smile_close
with chchange

li "Assistant Editor: Hanako Ikezawa."

play music music_dreamy fadein 0.5

show lilly basic_cheerful_close
show hisao basic_grin_uni_close
with chchange

"Lilly breaks into a dazzling smile as she reads the line I knew would catch her attention. A smile that proves very infectious."
li "Hanako, this is great."
"I nod humbly, but in truth I'm very proud of the result."
"It took a lot of effort, but we managed to meet the deadline and get the newspaper printed today. Everyone at the newspaper club was very satisfied with this latest issue."
"Tomorrow, the student council will be distributing it among the rest of the student body, but I couldn't wait that long and took three copies in advance: one for Hisao, one for myself and a Braille edition for Lilly."

show hisao basic_smile_uni_close
with chchange

hi "Hey Hanako, is it difficult to create a newspaper in Braille?"
"I nod my head."
ha "The newspaper club has software that can convert normal documents into a file type that a Braille printer can work with. I've used it myself yesterday."
ha "It's a lot of work, but there's a member at the club who can read Braille and helps us with this. I just operate the s-software according to his instructions."
"Hisao laughs and playfully ruffles my hair."

show hisao cross_grin_uni_close
with chchange

hi "I didn't know my girlfriend had this nerdy side to her."
"Before I can think up a reaction of my own, Lilly is already eagerly pouncing on his remark."

show lilly basic_ara_close
with chchange

li "Wouldn't that make her a perfect match for the current president of the science club, Hisao?"

show hisao basic_pout_uni_close
with chchange

"Hisao's only reply is a mock-offended huff that makes both of us burst out in giggles."
hi "I'm not going to argue that point."
ha "A wise decision, Hisao."

show lilly basic_smile_close
with chchange

li "So Hanako, do you have any plans to continue this?"
ha "T-this was only a temporary solution to meet this week's deadline. But they said they'd welcome any help I could offer them."

show hisao basic_smile_uni_close
with chchange

hi "It sounds like they want you to stick around."
ha "I-I might give it another try next week. Maybe."
hi "Sounds like a great plan."

show hisao basic_neutral_uni_close
with chchange

hi "Where were they this afternoon anyway? The club's classroom was deserted when I dropped by."

show lilly basic_oops_close
with chchange

"I smile a bit sadly at that."
ha "After a new issue is printed and handed over to the student council for distribution, the club always goes into town to relax and celebrate the release in one of the coffee shops there."

show lilly basic_concerned_close
with chchange

li "And they did not invite you to come along as well?"
ha "They did. It's just…"
ha "If I went along, I don't think I'd be able to relax enough to have fun. All I'd be doing would be watching the others have fun."
"That was pretty much the gist of it."
"This week, I've been forced to communicate with the club members in order to get things done, and I found that as long as the conversation remained strictly about the tasks at hand, I could manage with a bit of effort."
"But in the face of any small talk, I'd quickly freeze up."
"I didn't think I'd add much to the social event the club was planning, and it'd be better if I didn't go and attend."
"I can be on my own just fine, but being at a celebration and being the only one not having fun never fails to make me feel terribly lonely."
"I felt pretty good about the release and didn't want to do anything that might ruin my mood."

show lilly basic_weaksmile_close
with chchange

li "Maybe if you spend enough time there, they'll grow on you."
ha "M-maybe."

hide hisao
hide lilly
with charaexit

"We spend the rest of the time making small talk with me occasionally answering questions about last week's activities."
"Lilly then lets out a small yawn from behind her hand and we take as a cue to retire for the night."
"As Hisao and I rise to return to our dorm rooms, Lilly navigates her way around the table and approaches us."

show lilly basic_displeased_close at center:
    zoom 0.9
with charaenter

li "Hanako, it seems unfair that the rest of the club got to have a celebration, and the person who helped them out of a difficult spot did not."

show lilly basic_weaksmile_close
with chchange

li "Maybe you can see this little tea party as your own private celebration."
ha "I-I think I'll do that."
li "Hanako…"

hide lilly
with charaexit

stop music fadeout 0.5

"Suddenly, Lilly gets close to me and wraps her arms around me in a warm embrace."
"I let out a startled gasp."

show lilly basic_smileclosed_close at center:
    zoom 1.1 yanchor 0.9
with charaenter

play music music_friendship fadein 0.5

li "…I think you did a terrific job this week."
hi "Lilly's right. You really did."

show lilly:
    xanchor 0.5 xpos 0.35
show hisao basic_grin_uni_close:
    xanchor 0.5 xpos 0.65 yanchor 1.0 ypos 1.1 zoom 1.2
with charaenter

"Without warning, Hisao also hugs me."
"For a second, this weird three-way hug takes me off-guard."
"Then I return the embrace, wrapping one arm around each of them and gently pulling them closer."
"It really feels nice."
"It feels like the way things felt in Hokkaido while we were staying there."
"A small disabled family."
"My family."
"I suddenly feel a lump in my throat. I want to laugh and cry at the same time."
"Are Lilly and Hisao feeling the way I'm feeling right now?"
"I sniffle briefly."
ha "L-Lilly… H-Hisao…"
li "Yes, Hanako?"
"I love you."
"I love you both so much."
"Please let me be here for you the way you're here for me."
ha "…t-thank you."

hide lilly
hide hisao
with charaexit

"We break the embrace and I quickly wipe my eye."
"As Lilly sees us off, she smiles at me."

show lilly basic_smile at center
with charaenter

li "Enjoy your date tomorrow."
ha "Thanks. I'm sure we will."
ha "And um… Lilly… I… um…"
ha "I… really enjoyed our time together this week. W-we should hold these tea ceremonies more often again."

show lilly basic_sad
with Dissolve(0.2)

scene bg school_girlsdormhall
with locationchange

play sound sfx_doorclose

"For a split-second Lilly's expression seems sad, but before I can react the door closes, and the moment is gone."

show hisao basic_smile_uni_close
with charaenter

hi "Can I come in for a little while?"
ha "S-sure."

play sound sfx_dooropen

scene bg school_dormhanako
with locationchange

"We go in and he places his hands on my shoulders."

show hisao basic_smile_uni_close
with charaenter

hi "I thought I felt it earlier. You're not nearly as tense as you were during the last few days."
ha "Today I didn't have much stress, just the printing process and delivery of the papers - and then the tea ceremony with you and Lilly."

show hisao cross_grin_uni_close
with chchange

hi "So I guess you won't be needing a shoulder massage today."
ha "I-I'm not sure yet."
"I doubt I need my shoulders or neck loosened up, but I don't want him to leave yet."
"This week was tough."
"But we're going on a date tomorrow, and I'm looking forward to it."
"A fitting conclusion to a stressful week."
"I kinda made another important step this week."
"Maybe I've earned a little something extra."
"Maybe we've both earned something."
"…Should I…?"
ha "H-H-Hisao…?"

show hisao cross_smile_uni_close
with chchange

hi "Yeah?"
"I blush."
ha "Ummm… T-that e-e-extensive m-massage you o-offered earlier t-this w-week…?"

show hisao basic_grin_uni_close
with chchange

hi "That offer is still valid, Hanako."
ha "…s-share o-one t-together?"

show hisao basic_smile_uni_close
with chchange

hi "I'd love to."

hide hisao
with charaexit

play sound sfx_rustling

"He removes his socks and shoes and sits on my bed."
"I open one of my drawers, take a few tissues to avoid us messing up my blanket too much…"

with Pause(0.5)
show black
with None

play sound sfx_lightswitch_off

"…and then turn off the lights."
"I feel my way over to the bed, position myself in front of him and lean forward for a kiss."
ha "R-ready, Hisao?"
hi "I'm all yours, Hanako."

stop music fadeout 3.0
scene black
with Dissolve(3.0)

return