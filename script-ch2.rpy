label sisterhood_ch2:
label .sh_ch2:

$ set_window_tint(TINT_HISAO)

call sisterhood_timeskip

scene bg school_track
with Dissolve(2.0)

play music music_daily fadein 2.0

"I let out a loud yawn as I approach the running track wearing my gym shorts."
"It's been a while since I wore them as I am still exempted from P.E. classes, and that running session during my first week was also the last time I made an active attempt to improve my health."
"Even then, it was mostly a desire to get the head nurse off my back that drove me to the running track."
"Today will be the first day I am here of my own free will."

scene white
with dissolve

play sound sfx_whiteout
scene ev hanako_goodend:
    matrixcolor SaturationMatrix(0)
with dissolve

nvl show dissolve

n "Two days ago, Hanako and I met in the park in an attempt to salvage our friendship, which had taken a turn for the extremely awkward after we spent the night with each other the evening before."
n "If anything, our mutual confession highlighted just how riddled with misunderstandings and false assumptions our friendship had been up to that point, and clearing those up was a painful process for both of us."
n "But it was also this very process that allowed the two of us to make a fresh start as boyfriend and girlfriend who made a promise of mutual support to each other."

nvl hide dissolve
nvl clear

play sound sfx_whiteout
scene white
with dissolve

scene bg school_track
with dissolve

"My new relationship with Hanako is also the reason I approached the nurse yesterday with a request for a training schedule."
"A week ago, I would have seen a heart flutter as something that was nobody's problem but my own, but now that I have a girlfriend I feel a newfound responsibility to stay in shape."
"The nurse had been quick to draw, in addition to his own conclusions about my motivations, a training regimen for me to follow."

"As I reach the track, I see a familiar girl sitting on the bleachers."

show emi sad_shy_gym:
    zoom 0.85 align (0.7, 1.0)
with charaenter

show emi excited_joy_gym
with charachangealways

"As I approach, she looks up, gives me a wave and a smile and then continues adjusting the prosthetic running blades attached to the stumps just below her knees."

hide emi
with charaexit

"I remember running with her on the track before, during my first week here. But since she's not in my class and I have spent most of my free time in the library, the tea room or my dorm, we haven't really talked much since then."
"I guess if my determination to get in shape holds out, we'll get to know each other better soon enough. According to the nurse, running is pretty much a daily ritual for Emi."

stop music fadeout 1.0
queue music music_emi fadein 1.0

show emi excited_joy_gym
with charaenter

emi "Hey there! It's been forever since I've seen you here."
hi "Yeah, I've been making some early New Year resolutions and decided to make a serious attempt to get into shape."
"Emi gets up from the bleachers and bounces up and down on her leg blades a few times to test their stability."

show emi basic_grin_gym
with chchange

emi "Nurse told me about your visit yesterday. He asked me to keep an eye on you, just in case something happens."

show emi excited_hesitant_gym
with charachangealways

"…"
"She looks at me quizzically."
emi "What exactly was he talking about?"
"I take a moment to consider how to reply."
"When I first started attending here, I felt like my arrhythmia was none of other people's business, but over time I've slowly gotten more comfortable with it, and at this point a few of my classmates know about it."
"It's probably best to give Emi a run-down of the situation, just in case something does happen."
hi "I'm at this school because I have a heart condition, so for me shaping up is more about avoiding sudden death than it is about avoiding weight gain."
hi "Until recently, I just walked some short distances every now and then, but I recently picked up dating, so I have an additional reason to improve my health and stay in shape. I'd hate to leave a grieving girlfriend behind."

show emi excited_happy_gym
with charachangefast

"Emi responds with a smile, but suddenly makes wide eyes and mouths a soundless \"ahah\" as if she just had a revelation of some kind."

show emi excited_joy_gym
with chchange

emi "Ohh, so {cps=10}{i}thaaaaaat's{/i}{/cps} what the nurse was talking about."
"Uh oh…"
hi "What exactly did he tell you?"

show emi basic_closedgrin_gym
with chchange

"Emi strikes a pose, puts her hands in the pockets of an imaginative coat and squeezes her eyes shut while contorting her face in a grin that is as wide as it is artificial."
emi "I have reason to believe young Hisao is being driven by the oldest motivation known to man."
"I don't know whether to be amused by Emi's over-the-top yet somehow frighteningly accurate imitation of the nurse or annoyed by the insinuation she's making."
hi "I don't really see what's wrong with the desire to stay alive."

show emi basic_closedsweat_gym
with chchange

"Emi gives me an impish smile that indicates she really isn't buying my attempt to sidestep her remark."

show emi basic_grin_gym
with chchange

emi "I think he was talking about sex, Hisao."
emi "You know, keeping the species going and all?"
hi "Whatever. Can we save the rest of the small talk for the cool down lap?"

show emi excited_happy_gym
with chchangefast

"That sounded a little bit grumpier than I intended, but Emi doesn't seem to pay it any heed and cheerfully accepts my suggestion to start the morning run."

scene bg school_track_on
with shorttimeskip

play ambient sfx_emipacing fadein 0.3

nvl show dissolve

n "The laps around the track actually turn out better than I expected. The last time I participated in this activity took place a week after I was released from the hospital, and my physical condition was outright pathetic."
n "Nowadays, my condition is sufficient to allow me to walk from town back to school without feeling like an old man afterwards. Though I recently discovered it still wasn't good enough."

nvl clear

n "I wonder how Emi and the nurse would react if they knew their teasing had an element of truth in it."
n "Getting healthy enough to have sex wasn't the only reason behind my resolve to start working out, but the brief hiccup my heart experienced during the night Hanako and I slept together was enough to scare us both for a moment, and my condition hanging over our newly formed relationship like a dark cloud was something I wanted to avoid at all costs."

nvl hide dissolve

stop ambient fadeout 1.0
queue ambient sfx_emijogging fadein 1.0

"Emi politely waited for me at the finish line, and now we are casually doing our cool down lap. She doesn't waste any time bringing up a subject to talk about."

show emi excited_proud_gym
with charaenter

emi "So, Hisao… are the rumors I've heard true?"
hi "What rumors would that be?"
emi "Don't tell me you don't know. I don't keep up with gossip much, and even I have heard about it."
"I sigh. Of course I knew."
"After Hanako and I bared our souls to one another in the park and we were walking through town to get something to drink, Hanako gave me what she called her first gift to me: a sweet kiss on the lips that marked the official start of our relationship."
"But it turned out that our little public display of affection had been spotted by some fellow students, and a day later the rumor mill was working overtime spreading the news throughout the hallways of Yamaku."
hi "What have you heard?"

show emi basic_grin_gym
with chchange

emi "About Hanako Ikezawa… kissing someone in the middle of the street…"

show emi excited_proud_gym
with charachangealways

emi "…a transfer student."
hi "Guilty as charged. Is that enough for you?"

show emi excited_laugh_gym
with chchange

"She giggled and gave me a wink."
emi "I bet I'm not the first one to bother you about this, am I?"
hi "More like the sixth. Which isn't too bad. Given the fact the entire school seems to know about it, I was prepared for more interrogations than I've received so far."

stop ambient fadeout 2.0
scene bg school_track
with locationchange

"As we finish our lap, we walk to the bleachers and take a few sips from the water bottles we brought along."
"We sit down for a moment, and Emi gently starts rubbing the spots where her legs meet her prosthetics."

show emi basic_grin_gym
with charaenter

emi "The rumor's not really about you, you know. I mean, you're just a new transfer student."

show emi basic_confused_gym
with chchange

emi "But Hanako… she's been the shyest girl in school for the better part of three years. It's no wonder people talk about something like this."
hi "It's surprising so many people seem to know her, given the effort she usually makes to avoid drawing attention to herself."

show emi basic_grin_gym
with chchange

emi "I don't think anyone except you and Lilly Satou really know her. But I bet most students know who she is. Sometimes, when you try hard enough to avoid being noticed, you end up standing out all the more."
"We get up and take another sip. Emi lets out a cute little burp that most people would only associate with infants and we start walking towards the staff building."

show emi basic_happy_gym
with chchange

emi "How did she react to the attention?"
hi "She hates it. What did you expect?"
hi "Before, she merely thought people were staring at her all the time."
hi "Now, she {i}knows{/i} people are staring. She's been ditching the last few minutes of every class so far in an attempt to avoid the crowds."

show emi sad_grin_gym
with chchange

"Emi looks down for a moment as she hears this and gives me a sad smile."
emi "That's too bad. I mean, I get that she hates people staring, but I don't think this kind of attention is a bad thing. It's a shame she can't enjoy it."
hi "What do you mean?"
emi "Every student here has baggage of some kind. Some have gotten accustomed to things, but others are still working on it."
emi "But we all have… you know… milestones we have reached or still want to reach."

show emi basic_closedgrin_gym
with chchange

"She lightly taps her right leg blade in order to accentuate her point."

show emi basic_grin_gym
with chchange

emi "When I first heard the rumor, I was reminded of the time I took my first few steps with these. Or the first time I successfully navigated a staircase."
emi "For people like me, it brings back a pleasant memory. For people who are still coping, it's a little glimmer of hope, I think."
emi "Anyway, maybe I'm too optimistic, but I think right now most students, even though they don't know her, are genuinely happy for her."
emi "If she doesn't realize that and can't enjoy that, she's missing out."
"Emi's words sound oddly logical to me. Without exception, all students here must have dealt with hardships in their life, some more than others."
"Hanako's act was an undeniable sign of recovery, and no doubt something that would resonate with a lot of people here."
"I smile at Emi appreciatively."

show emi basic_closedgrin_gym
with chchange

hi "That actually makes a lot of sense. I don't think it'll change the way she feels about this, but I bet it'll make her feel a little bit better when I tell her."
hi "You know, you're a lot deeper than I expected."

show emi basic_annoyed_gym
with chchange

"Emi looks annoyed at this."
emi "You think I'm shallow or an airhead or something?"

show emi excited_amused_gym
with chchangefast

"Her frown quickly makes way for a mischievous grin."

show emi excited_proud_gym
with chchange

emi "You'd better watch what you say to me. I bet I could convince the nurse to tack on a few extra laps to that daily training schedule of yours."
hi "Bring it on. It'll only make me healthy sooner."

show emi excited_laugh_gym
with chchange

"Emi laughs at me calling her bluff."
"As she opens the door of the nurse's office, she playfully pokes me in the ribs with her finger."

show emi excited_proud_gym
with chchange

emi "Let's hope you still have that drive tomorrow morning. The second days are always the worst ones."

hide emi
with charaexit

"After delivering that ominous premonition, she closes the door behind her."

stop music fadeout 2.0
scene black
with Dissolve(2.0)

return