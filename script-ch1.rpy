label sisterhood_ch1:
label .sh_ch1:

$ set_window_tint(TINT_LILLY)

call sisterhood_timeskip

scene bg satou_patio
with Dissolve(2.0)

play music music_happiness fadein 4.0
play ambient sfx_nature fadein 4.0

"It has been a little over a week since Akira and I arrived at our parents' home."
"Although the official reason for coming over was seeing off Mother's ailing sister, our whole time here has felt more like a vacation. Thankfully, my aunt's situation stabilized shortly before our arrival, so I didn't feel too guilty about that thought."
"I've spent most of our time here sitting in the backyard reading the books I brought along and occasionally chatting with Akira."
"After finishing the remainders of breakfast, I navigate my way to the yard hoping for an opportunity to catch a few rays."

play sound sfx_can

"As I step outside, I'm greeted by the familiar sound of a sharp snap followed by the short hiss of a beer can being opened."
"I turn my head towards the source of the sound and do my best to appear as disapproving as I can."
li "Akira, do you really think it's a wise idea to be drinking this early? How can you think of drinking alcohol before we've even had lunch?"

show akira basic_smile at tworight
with charaenter

aki "Hey, unlike you I've been up and about for four hours already."
aki "Besides, I have a reason to celebrate. Check out what I got this morning."

show akira basic_smile_close at center
with charamovechangefaster

"As I hold out my hand, my sister passes me a rectangular piece of paper that has a familiar size. I remember having held a similar piece not too long ago."
li "A plane ticket! So you have finished making arrangements for our trip back to Japan?"
aki "Not just that. I managed to convince the old man to let us fly business class!"

show akira basic_laugh_close
with chchangefast

aki "We'll be travelling back in STYLE, BABY!!!"
"I wince a little at my sister's overly enthusiastic announcement, but manage to compose myself and smile."
li "Fitting accommodations for your new position in the legal affairs department at head office, are they not?"

show akira basic_lost_close
with chchange

stop music fadeout 2.0

"The playful retort I was expecting doesn't come."
"Uncomfortable silences aren't exactly common around Akira. Did I misjudge her yesterday evening?"

show akira basic_resigned_close
with chchange

aki "Why don't we have a little walk, Sis? A little stroll by the bay shore'll do you good."

stop ambient fadeout 2.0

scene bg inverness_shore:
    yalign 0.5 zoom 1.02
with shorttimeskip

play music music_serene fadein 4.0
play ambient sfx_waves fadein 4.0 volume 0.2

"The area near the bay shore where we're taking a break is pleasant to be sure, but the atmosphere remains somewhat heavy."
"As I am still determining the best way to bring up the obvious subject, my sister turns to me."

show akira basic_smile at center
with charaenter

aki "Be honest, Lils. You think my decision was made a little too hastily, don't ya? It's written all over your face."
"I sigh."
"I didn't really think it was my place to tell Akira what to do with her life, especially not after she sacrificed the latter part of her youth to look after me."
"But when Father told her that a position had opened up at the corporate headquarters here in Inverness, she accepted the job in seconds."
"Within a week, she'll be back in Japan breaking up a relationship that she seemed happy with before."
li "I don't think I can deny you've made your choice extremely quickly. For how long have you been dating…"

show akira:
    ease 1.5 twoleft

aki "I've been making quick decisions since I started working, Sis. I went with my gut instinct there, but I've been sleeping on it and I think I managed to work out why my gut told me to do what I did."

show akira basic_annoyed at twoleft
with chchange

play sound sfx_rockskip

"I hear a whoosh from my sister's direction, followed by several short splashes in the distance."
"Is she skipping rocks?"

show akira basic_resigned
with chchange

aki "You know, there's a part of this whole deal that I don't like… at all."

show akira basic_smile
with chchange

aki "But I've made a clear choice on what to do with my life years ago, and this seems like the best road to take."
"I nod silently."
"She may not seem like it at first impression, but Akira's pretty ambitious. And there are still several rungs of the corporate ladder left that she wants to climb."
aki "This might seem a tad weird to you, but in a way I'm securing my future stability. You can't get any higher than head office."
aki "So if I find someone else and settle down here, future promotions ain't gonna force me to move anymore. I can get where I wanna go and secure my financial future right here."
aki "Heh. Better to get this step behind me before my good looks start fading."
li "Not everybody makes a big deal out of looks."

show akira basic_laugh
with chchange

"We both get a good laugh out of that."

show akira basic_smile_close at center
with charamovechangefaster

"I suddenly feel how she takes my hand and pushes a small flat rock into it before turning me around."
aki "Here, give it a try."

play sound sfx_rockskip_fail
"{i}*splash*{/i}"

show akira basic_annoyed_close
with chchange

aki "Anyway, if I ever have any kids of my own, this will at least mean I can work my way to the top without having to leave them behind in another country."
aki "And they definitely seem more open to part-time employment than the management in Japan. Must be a cultural thing."
"Akira suddenly sounds very bitter. I cringe a bit at her sudden change of tone."
"I've never really felt comfortable when she vented about our parents, but I've never denied her a chance to do so, even though my own feelings are more nuanced."

show akira basic_annoyed at twoleft
with charamovechangefaster

aki "Of course, the old man didn't exactly hide the fact he pulled some strings to help me get this job, so I think we both know what'll be expected of me in return for taking it."
li "Wh-what would that be?"

play sound sfx_rockskip
"{i}*splash* *splash* *splash*{/i}"

show akira basic_resigned
with chchange

aki "I'll be expected to stop giving him a hard time about leaving us to fend for ourselves. He'll have paid me back, so all's fine and dandy again. Like every person has his price."
"I want to deny it, but I too have the impression Mother and Father are trying to make up for their sudden migration six years ago. A migration that Akira always interpreted as an escape."
"An escape from us… from me."

play sound sfx_rockskip
"{i}*splash* *splash* *splash*{/i}"

li "W-wouldn't it be good to have them try and make amends, even if it's a little late? We're still a family after all."

play sound sfx_rockskip
"{i}*splash* *splash* *splash*{/i}"

aki "It might have been good if I had been in a position to accept or decline."
li "Aren't you?"

show akira basic_annoyed
with chchange

aki "Whaddayathink? Word of my recommendation already spread around."
aki "You really think my job won't hit a dead end if I decline?"
aki "You think anyone at home would give a promotion opportunity to someone who declined a recommendation from head office?"
aki "I was extremely lucky to get as far as I already got, but I only have to push things once and it'll be over. Me declining the offer I got would be just the excuse they'd need."

play sound sfx_rocksplash
show akira:
    linear 0.1 xpos 0.26
    linear 0.1 xpos 0.3
"{i}*SPLOOSH*{/i}"

"That was probably more than just a pebble she just threw."
aki "I could start at the bottom rung of the ladder at another company, but chances are pretty high I'd get stuck there permanently. Assuming they'd want to hire me."

show akira basic_resigned
with chchange

aki "All things considered, this new position is something I probably wouldn't have turned down anyway, but it would have been nice if the choice would have felt more like my own."
aki "Now it has a bitter aftertaste I'm still trying to get out of my mouth."
"I didn't see it like that before. I want to say it is just paranoia on her part, but I know I'm not going to win that discussion."
"Akira has been in the business long enough to get a feel for the unwritten rules of the place. I don't really have any reason to doubt her assessment of her own situation."
li "This is why I dislike the notion of office politics. I cannot even begin to imagine how I would feel in that kind of situation."

show akira basic_laugh_close at center:
    ypos 1.02
with charamovechangefastest

play sound sfx_impact
with vpunch

"I stifle a cry as Akira gives me a cheerful slap on the back."
aki "Probably like a goldfish in a shark tank."
aki "Stick with your own dream, Lils. You'll thank yourself later."

show akira basic_smile at twoleft
with charamovechangefaster

play sound sfx_rockskip
"{i}*splash* *splash* *splash*{/i}"

li "Is this what you'll be telling your boyfriend as well?"

show akira basic_resigned
with chchange

aki "Something like that. He knows I want to work my way up."
aki "If I give it all up for his sake, I'll probably end up resenting him over it, even if the decision was completely my own."
aki "No relationship can survive with that kinda baggage."

show akira basic_lost
with chchange

aki "I think he'll understand."
aki "I hope he'll understand."

show akira basic_smile
with chchange

aki "Anyway, let's start walking back."
li "D-did you really consider all these things during the few seconds between when Father asked you and you accepted?"
aki "Like I said, it was a gut feeling. It took me a whole night of mulling to figure out the specifics."
"I am impressed. Akira wasn't the only one who was asked to move from Japan to Scotland."
"I too have been asked to move back in with our parents. But where she accepted almost immediately, I have been trying to avoid even thinking about the choice that has been offered to me."
"Akira trusts her instincts blindly. I'm not quite as confident in my gut feelings and tend to mull over things longer than I should."

show akira basic_resigned
with chchange

aki "You know, there's one thing that kinda bothers me about my decision. And that concerns you."

play sound sfx_rockskip
"{i}*splash* *splash* *splash*{/i}"

aki "You wanna be an English teacher and I think you'd be a mighty good one. The nice thing about a teaching gig is that you don't have to worry about promotions as long as you can get the job to begin with."
li "I am not certain what you are getting at."
aki "So I'm guessing the decision you're gonna make is eventually gonna come down to the people who'll be affected by your choice."
aki "But since I made my own decision right in front of you, I probably influenced your choice already and that felt kinda wrong."

show akira basic_annoyed
with chchange

aki "I probably could've shut up and let you figure out what to do for yourself."
li "I do have my family over here. And your decision would have mattered to me."

show akira basic_smile
with chchange

aki "True, you got our little family over here, but you got your little family over there too, right?"
aki "Heh. And I'm not referring to that competitive cousin of ours with whom you get along so well."
"I sigh."
"Akira is correct, unfortunately. When Mother and Father told me they liked me to move to Scotland and live with them again, Hanako and Hisao were the first thought that came to my mind."
"We were almost our own little family, the three of us—at least that is how I feel. And right now I am very worried about how they are doing."
li "Hisao called last week to tell me Hanako had withdrawn within herself, just like last year."
li "He's been showing interest in her lately, but I'm not certain if it's the kind of interest she would appreciate. All in all, I've been worried."
aki "Hey, how badly could they screw up in the short time we've been here? You're probably worrying about nothing."
li "You're probably right."

show akira basic_smile_close at center
with charamovechangefaster

"Suddenly, something smooth is pushed into my hand. I recognize the feeling of a cell phone."
aki "If you wanna ease your mind, why not contact them? I've got the tickets, which means you've got an official excuse."

hide akira
with charaexit

play sound sfx_phonedial

"I smile appreciatively at Akira as I dial Hanako's number. Just hearing her voice would probably ease my worries."
"I feel a bit guilty for not having called earlier, but I know from before that Hanako would have been unlikely to respond during her birthday depression."

play sound sfx_phonepickup

show hanako basic_worry_phone at phonebox
with charaenter

ha "A-Akira?"
"Hanako's voice sounds very far away, but the reception isn't all that bad."
li "Hello, Hanako."

show hanako emb_smile_phone
with chchange

ha "Lilly!"
"Hanako sounds delighted to hear from me. That's good. It means she must have bounced back from last week sooner than expected."
li "It is good to hear from you, Hanako. How are you doing right now? And how is Hisao?"
ha "W-we're doing very well. And how are you doing, Lilly? D-Do you have any idea when you'll be heading back?"
"It takes me a moment to place Hanako's tone."
"While I've known Hanako for about a year and have been around during her good moods, this is the first time in a long while she's sounding outright cheerful."
li "We'll be returning to Japan near the end of the week. Akira will be dropping me off, so I'm hoping the two of you will be welcoming us at the gate."
ha "S-sure, we'll be there."
"…I wonder…"
li "Hanako, you sound like you're in an unusually good mood right now."

show hanako emb_timid_phone
with chchange

ha "Ummm… Lilly, there's something I have to tell you when you get back."
"I have no doubt that whatever she wants to tell me is responsible for the good mood she's currently in, and I'm not looking forward to spending several more days wondering what it might be."
"I decide to press the issue a bit."
li "Hanako, did something good happen to you?"

show hanako emb_blushing_phone
with chchange

ha "I… I can't tell you yet. I promised to keep it a secret until we could tell you in person."
li "Hmmm… would you be willing to elaborate on who ‘we’ might be?"

show hanako def_worry_phone
with chchangefast

ha "Ah… no, I mean… I meant to say ‘I could tell you in person’."
li "Hanako, do you mind if I make a few guesses?"

$ _window = False
hide hanako
with charaexit

stop ambient fadeout 1.0

scene bg satou_grounds
show akira basic_laugh:
    tworight
    ease 4.0 center
with shorttimeskip

"By the time Akira and I arrive at the driveway of our parents' mansion, we're both wearing a huge smile on our face."

show akira at center

aki "Hah, I still can't believe she got herself a boyfriend."
aki "Who would have known? Didn't think she had it in her."
li "I think it's very sweet. They have so much in common. I am sure they'll be a very nice couple."

play sound sfx_dooropen

scene bg satou_stairs
show akira basic_smile_close
with locationchange

"As we enter the mansion through the patio doors, Akira turns around and gives me a playful poke in the ribs."
aki "How about I go down to the cellar and fetch us something to celebrate?"
aki "Wanna open up a little bottle of champagne and perform a toast?"
"I smile at my sibling and nod playfully."
li "Yes, please."

stop music fadeout 3.0
scene black
with Dissolve(3.0)

return