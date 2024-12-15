label sh_ch17alt:
label .sh17alt:

call sisterhood_timeskip

scene bg school_track_on
with Dissolve(1.0)

"I wonder how Hanako is doing right now."
"That thought keeps returning to me as I casually stroll along the running track with my hallmate Kenji in tow."
"The official excuse is to catch up on what transpired at the science club during my week of absence and fill Kenji in on the reason I was out of commission."
"But more importantly, my dorm room is being used by Lilly right now to try and patch up her damaged friendship with Hanako."
"While I'm not completely sure how much of it can be salvaged in the 24 hours that remain until Lilly's departure to Scotland, I don't want to risk things being ruined by my eccentric neighbor bursting into my room unannounced."
hi "I'm sorry. What did you say?"

show kenji neutral_gym
with charaenter

play music music_kenji fadein 0.5

ke "How can you be so sure that the person who assaulted you wasn't a woman? A feminist or perhaps a lackey hired to take you out."
"I wonder how Hanako and Lilly are doing right now."
hi "It was a guy. A slightly older man on a bicycle."
hi "Hana…{w=0.5} I mean, people at the scene confirmed it to me later. I don't think he was a feminist."

show kenji tsun_gym
with chchange

ke "The whole thing still smells extremely fishy to me. I mean... Getting body checked in the middle of the street and carried off to who-knows-where... Does that sound normal to you?"
"Hanako at least seems relieved that she and I have managed to reconcile after last week's events. I think she's going to need my support after Lilly leaves tomorrow."
"Despite having pushed Lilly away last week, I have no doubt that Hanako's going to miss her terribly."
hi "We were in the middle of a downpour, and neither one of us was paying attention. The rainstorm made it kinda hard to see far ahead. It was just a stupid little accident with big consequences."
"I sigh inwardly."
"The idea was to just get an update on what Mutou and Kenji discussed at the science club meetings last week, but it turns out that after my accident, Kenji came to his own conclusions about my absence and shut himself in for the rest of the week."
"It's still a mystery to me how Kenji can act so ordinary during club meetings and so irrational when we're alone."
# TODO maybe show rage version?
ke "Accident my ass! You were on somebody's hit list, man. It was a coordinated operation."

show kenji neutral_gym
with chchange

ke "The feminist movement is onto you. I bet that wasn't even a real ambulance that picked you up."
"I can't really judge that since I was out like a light at that time, and what I know about that moment is from Hanako's recollection."
"Since she's still very reluctant to talk about what happened that afternoon, I can't really get into the details."
hi "It was a pretty real hospital I woke up in though."

show kenji happy_gym
with chchange

ke "They sent some goons the day after to ransack your room. Or maybe to bug the hell out of it. They're watching you now, man."
"That would be Shizune and Misha who asked the dormkeeper for a spare key and got me my possessions and some books to make my stay in the hospital more comfortable."
"So it turns out that Kenji spotted them. I wonder what he would say if he knew there are two other girls in my dorm room right now."
"I feel once again that getting Kenji away from the dorm building today has been a very wise move."
hi "Those were just some girls from my class, picking some stuff up for me."

show kenji tsun_gym
with chchange

ke "You really think I can't tell the difference between students and trained spies? They were dressed like female students for sure, but their mannerisms gave them away."
hi "How so?"

show kenji happy_gym
with chchange

ke "They didn't say a single word during the whole operation. They were only communicating in coded gestures, like commandos on a mission."
hi "Could it be that one of them was a deaf-mute and they were communicating in sign?"
ke "Maybe. It makes sense to pick a mute person for an infiltration job. When they're captured and interrogated they at least can't blab. Unless you untie their hands first. That's what they're counting on. They're trained for those kinds of situations."
"You're completely missing the point."

hide kenji
with charaexit

"I fiddle with my cell phone for a bit. I asked Hanako to send me a little text message when they're done."
"In less than half an hour, I have a talk coming up with Hanako's therapist who asked me to come and see her, if Hanako and I managed to reconcile."
"She was seeing a client earlier this day though and made it clear she didn't want me to wait outside her office, presumably for the sake of her client's privacy."
"So until her last appointment is over, at four o' clock apparently, I'm stuck playing along with Kenji's conspiracy theories."

show kenji tsun_gym
with chchange

ke "After they left your room, I knew they'd be coming for me next. I knew they were gonna kidnap me, imprison me somewhere and then send a squad to my room to steal my blueprints and plans for resistance activities."
ke "So I locked my door, moved my bed in front of it and got to work on developing a defense mechanism. It's not finished yet, so maybe you can take a look at the designs at the next club meeting."
hi "Really?"

show kenji happy_gym
with chchange

ke "It's a very clever contraption. I've hidden my papers in a secret compartment in my desk drawer."

show kenji neutral_gym
with chchange

ke "To open it, you gotta lift the compartment lid through a hole in the bottom of the drawer using a pen or pencil."
ke "If you open the compartment any other way, an electronic circuit is closed that causes the flammable substance inside the contraption to ignite which in turn causes all the incriminating evidence to go up in smoke."
ke "I saw it on TV once and thought it was a stroke of genius."
"I make a mental note to sabotage that insidious thing (if it even exists) the first chance I get and keep any and all flammable substances far away from Kenji before he accidentally sets the guys' dorm building on fire."
hi "Sure, I'll help."

show kenji happy_gym
with chchange

ke "Hey, thanks!"

show kenji tsun_gym
with chchange

"Kenji seems delighted at my quick offer of assistence, but then suddenly narrows his eyes and takes a step back."
hi "Something's wrong?"
ke "You're way too eager to agree all of a sudden. You're usually far more reserved about my plans. This doesn't sound right. Didn't you say they operated on you?"
hi "Yeah."
ke "How can I be sure that they didn't install a mind control device while you were out? Maybe you were merely being ordered to agree to help me just now and they'll make you sabotage my device the moment I turn my back."
"I'm not quite sure whether to be impressed by Kenji's justified suspicion of me or baffled by the leap of logic he took to explain it."
hi "They operated on my chest. Doesn't a mind control device usually go in the brain?"
"Why am I even arguing with him as if this is a serious conversation topic?"

show kenji neutral_gym
with chchange

ke "Hmmm… Maybe not a mind control device then. Probably a tracking device. Definitely a tracking device."
hi "Why definitely a tracking device?"
ke "Last Saturday that tall blonde from my class came knocking and told me that you'd be arriving at noon and that they were going to 'welcome you back'. They knew exactly where you were going to be and when."
ke "If they were confident enough of the success of their ambush to go and taunt me with it, they had to have placed a device on you somehow that allowed them to pinpoint your location."
"It's kinda scary how seamlessly he manages to fit all of last weeks events into one big narrative and still get things completely wrong."
hi "I'm not sure I want to know but… Since you knew they were setting up an ambush for me, did you do anything to try and thwart them?"

show kenji tsun_gym
with chchange

ke "Sorry man, but I had to set up my own defenses first. In this harsh world, it's every man for himself."
hi "That's okay. I managed to survive."
ke "Maybe you were worth more to them alive. With that tracking device inside you, they may be monitoring us right now."
ke "Maybe we shouldn't be seen together."
"I do my best to supress a groan and check my watch."
"It's almost time for my meeting with Miss Takawa. It'll take some time for me to reach the building where the medical staff resides, especially since I'm still forced to take it slowly for a little while, and I think I've heard enough crazy for one day."
hi "Maybe you should do a perimeter check if that's what worries you. I have an appointment at the nurse's building. I'll have them check me for tracking devices."
hi "Why don't you stay behind and make sure I'm not followed? Then you can check your theories for yourself."

show kenji happy_gym
with chchange

ke "Hey man, that's a great idea. Go ahead and leave. I'll watch your back and then check this place for spies or bugs."
hi "Sure thing."

hide kenji
with charaexit

"As I start making my way to the staff building and see Kenji sneak off into the nearby bushes, I feel a bit guilty about sending him off on a wild goose chase, but after what I've just heard, I can't have him return to the dorms just yet."
"I can't help but roll my eyes at the irony of it all."
"There's a guy out there who believes in mind control devices searching the bushes for spies and cameras right now, and yet I'm the one about to see a therapist."

stop music fadeout 3.0
scene black
with Dissolve(3.0)

return