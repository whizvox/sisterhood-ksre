label sisterhood_ch14:
label .sh_ch14:

scene black
stop music

"Where am I?"
"My dorm? My bedroom at home?"
"My eyelids are unusually heavy and random thoughts zoom by like a passing train."

play ambient sfx_hospital fadein 2.0
scene bg hosp_ceil:
    blur 20
    matrixcolor BrightnessMatrix(0.7)
with openeye

show black
with shuteyefast

$ renpy.music.set_volume(0.0, 0.5, "ambient")

"When I manage to open my eyes for a moment, all I can see is a white blur."
"I try to focus my thoughts, but for some reason they keep whirling around in my head."
"Did I hit my head or something? What's wrong with me?"

$ renpy.music.set_volume(1.0, 2.0, "ambient")
show bg hosp_room2:
    blur 20
    matrixcolor BrightnessMatrix(0.5)
with None
hide black
with openeye

"I try to force my eyelids open again."
"This time I see a few silhouettes against the white background."
"I hear voices, but I can't focus enough to make out the conversation beyond a few loose words."
"???" "…stable…narcosis…worn off yet…rest…tomorrow…"
"What's going on?"

stop ambient fadeout 0.5
show black
with shuteye

"Despite my best efforts, I can feel myself sinking back into a black hole, the voices dying down to an incomprehensible murmur."

scene black
with Dissolve(2.0)

scene bg hosp_ceiling:
    blur 10
with openeye

"When I open my eyes again, my vision is still blurry, but my mind is clearer than it was before."

show bg:
    blur 0
with Dissolve(2.0)

play music music_rain fadein 0.5

"I rub my eyes, and as my vision starts to focus I notice I'm staring at a white ceiling, one I haven't seen before yet is still disturbingly familiar."
"As I try to rise, a painful sensation wells up in my chest."
"I bring my hand to my chest only to find something stuck to it."
dc "Please don't touch the bandage, Mister Nakai. It'll still take some time for the wound to heal. Let me help you sit upright."

scene bg hosp_room2
with Dissolve(2.0)

"I hear a click and the head of the bed I'm lying in slowly tilts upwards, allowing me to see more of the room I'm in."
"The room is clean and rather empty, almost artificially so. An EKG monitor next to me emits a steady stream of beeping sounds, and I see an IV-tube leading from a bag containing clear liquid to my arm."
"The owner of the voice is a middle-aged man in a white coat standing in front of me."
"A hospital. Probably the hospital near Yamaku as the landscape outside the window has a familiar look."
"I'm in a hospital room."

# show doctor bigsmile at center
# with charaenter

dc "I see you're awake, Mister Nakai. How are you feeling?"
"I open my mouth to reply, but my mouth is too dry to speak clearly and a feeling of nausea boils up, forcing me to close my eyes until it passes."
"I swallow a few times, open my eyes and make attempt number two."
hi "What happened to me?"
dc "You had another episode, Mister Nakai."
dc "You had an accident yesterday afternoon. A collision with a cyclist triggered your condition. You were brought here and taken to the operating room soon after."
hi "I… had another surgery?"
dc "We performed a keyhole surgery to get an accurate assessment of your condition, but we want to wait a bit and see if you remain stable without any drastic procedures."
dc "We're keeping you under close observation and under increased medication for the next few days. If we run into complications while you're here, we'll operate later this week."
dc "If no further irregularities take place, we can probably let you go this weekend. So let's hope your luck holds out."
"Is this guy joking?"
hi "I can't say I'm feeling particularly lucky right now. I've been working out nearly every morning to avoid something like this."
hi "I haven't forgotten my medication for a single day. And despite everything, one moment of bad luck makes me end up here again."
hi "If that isn't depressing, I don't know what is."
dc "I wouldn't call those efforts a waste of time, Mister Nakai. All circumstances concerned, things could have ended a lot worse. If you remain stable, you'll be able to pick up your life again before the week is over."
"As the doctor speaks, I try to recollect what happened."
"He said the accident took place yesterday, so it's Tuesday right now, seemingly afternoon from the look of the sky outside."

show rainmemory:
    alpha 0.1
with Dissolve(1.0)

"It was pouring really hard."
dc "Of course, you'll have to take it a little easier than usual for a while after you get back."

show rainmemory:
    alpha 0.2
with locationchange

"We were running as fast as we could, keeping our head down against the rain."
dc "We've been keeping in close contact with Yamaku's head nurse. He'll take over when you leave here."

show rainmemory:
    alpha 0.3
with locationchange

"I was looking over my shoulder."
dc "Your parents were here earlier, though you were probably still too much under the influence of the anesthetics to have heard them."

show rainmemory:
    alpha 0.4
with locationchange

"Then something hit me and knocked me over."
dc "They said they'd visit again later this week."

show rainmemory:
    alpha 0.5
with locationchange

"I was lying on the asphalt, my chest hurting, my heartbeat out of control."
dc "We want you to get plenty of rest for now. You might be ready to receive visitors tomorrow if all goes well."

show rainmemory:
    alpha 0.6
with locationchange

"I must have lost consciousness at some point. The last thing I remember seeing before blacking out…"
dc "You might experience some side-effects from the medication we're giving you."

$ renpy.music.set_volume(0.0, 0.5)
show rainmemory:
    alpha 0.7
with locationchange
$ renpy.music.set_pause(True)

# TODO maybe show a VFX of hanako's terrified face

"…was Hanako's terrified face."
dc "Any further questions, Mister Nakai?"

hide rainmemory
with Dissolve(1.0)

$ renpy.music.set_pause(False)
$ renpy.music.set_volume(1.0, 0.5)

"Hanako?"
dc "Ahem… Mister Nakai."
"Hanako!"
"The sudden change in signal from the EKG monitor catches the attention from the doctor."
dc "Is something the matter, Mister Nakai?"
"Today's Tuesday. Lilly's leaving Yamaku in a matter of hours. Hanako and I were out to buy things for her farewell party we scheduled for last night."
"What happened to Hanako? Is she alright? Where is she?"
hi "This heart attack came at a very inopportune moment."
"The doctor chuckles."
dc "I hear that more often around here."
hi "Doctor, can you tell me if someone was brought in together with me? A girl with long dark hair?"
dc "I'm afraid I don't know. I wasn't present when the ambulance brought you in."
hi "Has someone been here for me other than my parents?"
dc "No, I can say that much with certainty. I could check with the ambulance staff for you."
hi "Thanks…"
"As the doctor walks out, my thoughts dwell on Hanako again."
"I'm a little taken aback by the fact that nobody has heard from her.{w} Ever since we started dating, she's been completely devoted to me, and I would have half-expected her to be sitting at my bed when I woke up."
"And what about Lilly? Does she even know I'm here?"
dc "It turns out you were correct."
"The doctor returns, only a few minutes after he left."
dc "I'm afraid I don't know the details, but there was indeed another person who was taken here together with you.{w} She wasn't injured in any way, though the ambulance staff noted she was acting rather oddly. Eventually someone from Yamaku arrived to pick her up."
"I appreciate the fact he took the time to check, but I wish he could be more specific about Hanako.{w} 'Oddly' is a very vague term, and to some people even Hanako's usual behavior would probably qualify as odd."
"It doesn't really do much to relieve my anxiety. I take a look at the chair near the bed that holds my school uniform."
hi "Doctor, could you please hand me my cell phone? It should be in one of the pockets of my pants."
dc "I'm afraid the use of cell phones is prohibited in the building. They can interfere with some of the equipment we use. You can use the phone on your nightstand if you wish to make a call."
hi "I'll use that one then. Thank you doctor."
"It's a good thing I know Hanako's and Lilly's number by heart. Hopefully, talking to Hanako will put me at ease. And if I can't get back to Yamaku before the weekend, I'll just have to say goodbye to Lilly this way."
"It's hardly ideal, but at least I can get a hold of her before her plane takes off."
"I hope she'll pick up if she's called by a number she doesn't recognize."
"I dial Hanako's number and anxiously wait for her to pick up."
"As far as I know, my condition is stable right now.{w} While we both know from personal experience that that's hardly a guarantee, it at least gives me something to tell her, assuming she doesn't already know."
"And who was it who picked her up? The nurse?"

stop music fadeout 0.5

ha "…H-h-hello?…"
"Just when I'm about to give up and speak a message into Hanako's voicemail, I hear a small voice on the other end of the line… soft, hesitant and nervous."
"I've heard her talk like this only once or twice and that was when she was in a very bad place emotionally. This doesn't sound good."
hi "Hanako, it's me."

show hanagown worry_phone at phonebox
with charaenter

play music music_hanako fadein 0.5

ha "H-H-Hisao…"
"This is odd. I expected her to be relieved, but her voice actually sounds frightened.{w} What's going on?"
hi "I… just woke up. I'm at the hospital and had a keyhole surgery so they could check me up, but they don't want to operate if they don't have to."
hi "I'm stable right now. With luck I'll be able to leave here soon. I'm alright. Well, maybe not right now, but I'm gonna be. Promise."

show hanagown distant_phone
with chchange

ha "…"
"Again, no relieved answer."
hi "Hanako?"

show hanagown worry_phone
with chchange

ha "…T-that's g-good… I'm h-happy f-for you, H-Hisao…"
"Huh?"
hi "Hanako, can you tell me what happened yesterday? The whole thing's still a bit of a blur to me."
hi "I heard you came along with me in the ambulance. Were you alright? And who picked you up there?"
"A lot of questions, I know. She probably had one hell of a scare yesterday. I just hope I can get her to talk about it. Get it out of her system."

show hanagown distant_phone
with chchange

ha "…"
"Is it my imagination or is her breathing speeding up?"
"She's not… crying, is she?"
"Are things still too recent for her? Should I try to get her mind off things instead?"
hi "Hanako?"

show hanagown worry_phone
with chchange

ha "…Yes?"
hi "I'm allowed to have visitors from tomorrow on if everything goes well."
hi "You know, I wouldn't mind having one of your home-made dishes. Beats the hospital food by a mile."

show hanagown irritated_phone
with chchange

"I hear a gasp on the other end of the line."
"Hanako?"
ha "{cps=20}…I…can't…{/cps}"
hi "You can't do what?"

show hanagown distant_phone
with chchange

stop music fadeout 0.5
with Pause(0.5)

ha "{cps=10}…I… can't… be… your… girlfriend… anymore…{/cps}"

play music music_rain

hi "{i}Hanako?!{/i}"
ha "…I'm… sorry, Hisao…"

hide hanagown
with charaexit

"I physically reel in shock upon hearing Hanako's announcement."
"When I lift the receiver to my ear again, the only thing I hear is the tone indicating the connection was broken off."
"I immediately press the recall button, but this time, I merely hear the beep of the voicemail. She must have turned off the phone."

nvl clear
nvl show dissolve

n "This can't be real."
n "Did Hanako really just break up with me?"
n "But why?"
n "This is crazy."
n "Or is it?"
n "Hanako lost both of her parents at young age. They died right in front of her. I wouldn't be surprised if she still has nightmares about that every now and then."
n "Yesterday, I also nearly died in front of her. I wouldn't be surprised if this thing had a greater impact on her than it had on most other people."
n "And if yesterday taught me anything, it's that no matter how hard I try, I can't make any guarantees it won't happen again."
n "Can I expect Hanako to stay with someone who might rip her old wounds open again and again?"

nvl hide dissolve

"As my mind is still making somersaults in an attempt to digest this unexpected turn of events, my fingers are already pressing the buttons in order to call another number."
"I don't expect Lilly to be able to help, seeing that she's set to leave Yamaku in a matter of hours, but maybe she has some advice for me."

show lilly basic_smile_phone at phonebox
with charaenter

li "Good afternoon. Lilly Satou speaking."
hi "Lilly, it's me."

show lilly basic_concerned_phone
with chchange

li "Hisao! Thank God. You and Hanako never showed up yesterday. I got worried and called the nurse's office, who said you had an accident. I've been worried sick. What has happened?"
"Lilly's familiar worrying tone is strangely reassuring right now. Although it also suggests she hasn't spoken to Hanako yet."
hi "The short version is: we went shopping for last night, got surprised by the rainstorm and collided with someone in our rush to reach the store. That shock triggered my arrhythmia, and I had to be taken to the hospital."
hi "I only woke up an hour ago. Hopefully I'll be allowed to leave before the weekend's over. Right now, I'm stable."

show lilly basic_sad_phone
with chchange

li "You were shopping for my farewell party…"
hi "Don't be like that. It was just a stupid accident that could have taken place at any time. It's nobody's fault."

show lilly basic_displeased_phone
with chchange

li "I understand."
hi "Could you let Shizune and Misha know about this in case they don't already know? I get that you two don't get along, but I doubt Shizune will pick a fight with you under these circumstances."
li "I will. Are you already allowed to have visitors at the hospital?"
hi "Not yet. Hopefully tomorrow. But that won't do you much good, will it?"
li "I called Akira yesterday, and she's currently trying to postpone our departure."

show lilly basic_concerned_phone
with chchange

li "I… I really don't feel comfortable leaving with things as they are now. I hope to hear soon if she has succeeded."
hi "That's good. I could really use your advice right now."

show lilly cane_oops_phone
with chchange

li "Of course."
hi "Have you spoken with Hanako since yesterday afternoon?"
li "I have not. It's possible I heard her bedroom door last night, but it was already very late."
li "Her door has been locked ever since. If she's in there, she's not responding to knocks."
hi "So you have no idea what's wrong with her either?"
li "Wrong?"
hi "I just got off the phone with her."
hi "She acted… shell-shocked. She… She said she couldn't be with me anymore."

show lilly basic_concerned_phone
with chchange

li "W-what? What does that mean?"
hi "Lilly… I think Hanako just broke up with me."

show lilly basic_reminisce_phone
with chchange

li "N-no…"
"Lilly's exclamation of disbelief barely reaches above the level of a whisper.{w} I don't think I've ever heard the usually calm Lilly so thoroughly unsettled before."
li "H-Hisao, why would she do that?"
hi "Only she would know for sure, but I suspect that me having a heart attack right in front of her hit her very hard."
hi "She already lost both of her parents. Being faced with the loss of yet another person who was important to her…"

show lilly basic_sad_phone
with chchange

li "But… she loved you dearly. I can't believe she would just give that up."
li "Maybe… Maybe I can get her to talk to you. "
hi "I doubt it's gonna be that easy."

show lilly basic_reminisce_phone
with chchange

li "Maybe she merely said this in the spur of the moment. Perhaps I'll be able to get through to her. I have to try."

hide lilly
with charaexit

"Neither of us feeling really up to the usual ritual of small talk, we hang up and my thoughts once again dwell on Hanako."

nvl clear
nvl show dissolve

n "\"I can't be your girlfriend anymore.\""
n "What does that mean?"
n "Not: 'I don't want to', but 'I can't'."
n "It really feels like she feels compelled by the circumstances. It might not be a spur of the moment as Lilly suggested."
n "This had quite an impact on Lilly as well. She didn't sound as calm and in control as she usually does."
n "I can't blame her though. She's scheduled to leave Yamaku this evening. If Akira is unable to cancel the trip, Lily will be leaving Japan in the middle of a big mess. Knowing her motherly nature, that'll seriously burden her."

nvl clear

n "I feel so powerless."
n "I should be there at Yamaku confronting Hanako. Comforting her.{w} Instead, I'm being trapped in here for at least several more days."
n "I slam my fist hard onto the side of the bed. The increased frequency of beeps from my heart monitor draws my attention."
n "I'm getting too worked up right now. I'm stuck here, and nothing I can do will change that."
n "The best thing I can do is focus on my recovery right now. If I stay on edge all the time, the doctors may decide to keep me here longer."
n "If the upcoming weekend is the earliest time I can leave here then that's what I should aim for."
n "I'll just ask for some sleeping pills or something to get more rest."

nvl hide dissolve

stop music fadeout 0.5

scene bg hosp_room2
with Fade(1.0, 1.0, 1.0)

play music music_night fadein 0.5

"The evening and the rest of the next day are completely uneventful, so I just try to get as much rest as I can.{w} Having just finished my evening meal, I lie back and close my eyes."
"It's been a day since I've called Hanako and Lilly, and I haven't heard a reply from either."
"Is Lilly still in Japan, or is she flying to Scotland right now?"

show black
with shuteye

"Dozing off a bit, I can vaguely hear a sound approaching me."
"I'm not sure if it's my imagination or not. A doctor wouldn't walk with such loud pronounced steps."
"Suddenly I feel something on my face. I open my eyes, but there's still nothing but darkness."

mi "Guess who, Hicchan!"
hi "Misha, what are you doing in my dream?"
mi "Wahaha~, it isn't a dream! I'm right here!"

show mishashort hips_grin_cas behind black
with None
hide black
with openeyefast

mi "Hey there, Hicchan! How are you feeling?"
hi "Slightly better than yesterday. Are you here on your own?"

show mishashort hips_smile_cas
with chchange

mi "No. I brought company."

show shizu basic_frown:
    xanchor 0.0 xpos 1.0
show lilly cane_displeased:
    xanchor 0.0 xpos 1.3
with None

show mishashort at twoleft
show shizu at tworight
show lilly at right
with charamovefast

"She moves to the side a bit, and I'm surprised to see not just Shizune entering the doorway, but Lilly as well, her hand resting on Shizune's shoulder for navigation."
"So it seems Akira managed to extend their stay in Japan after all."
"Shizune has an irritated expression on her face, Lilly's pace obviously far too slow for her liking, but she doesn't pull away.{w} It's an interesting sight, seeing that Shizune and Lilly usually can't stand each other."

show lilly at offscreenright:
    alpha 0.0
with charamovechangefaster

# TODO original dialogue, check
"As Shizune heads further into the room, Lilly hangs back in the doorframe."

hi "Misha, did you walk on ahead?"

show mishashort hips_grin_cas at twoleft
show shizu at tworight
with chchange

mi "Ahahaha. How did you know?"

show shizu behind_smile
with chchange

"I merely roll my eyes and focus on Shizune who has reached my bed as well and gives me curt nod as a greeting, the modest smile on her face indicating she's happy to see me."

show mishashort sign_smile_cas
with chchange

mi "Good to see you, Hicchan. You certainly gave us a scare."
hi "Nice to see you too, Shizune. And thanks for dropping by."
mi "Not a problem. We made sure to bring you a few things you may appreciate during your stay here."

show shizu basic_normal2
show mishashort perky_smile_cas
with chchange

"Shizune gestures to Misha who grabs the bag lying at her feet and drops it on the bed. Inside are my own pajamas, toothbrush and several books I got from the library last week."
"I guess it would appear ungrateful to ask Shizune how the heck they managed to get into my room."
hi "Thanks guys. This'll make the rest of my time a lot easier to sit out."

show mishashort hips_smile_cas
show shizu adjust_happy
with chchange

"I then notice a small envelope near the bottom of the bag.{w} There's no post mark or stamp on it; only my own name written with what appeared to be shoddy or shaky handwriting."
"Curiously, I look at Shizune."
hi "What's in the envelope?"

show mishashort sign_confused_cas
show shizu basic_normal
with chchange

mi "I don't know. We found it in the student council's mailbox. We don't know who left it there."
"Intrigued, I open the envelope."

stop music fadeout 0.5

"But when I feel what's inside I feel my blood curdle, and both Misha and Lilly cringe when the beeping of my EKG monitor suddenly spikes."

show mishashort perky_confused_cas
show shizu behind_blank
with chchange

mi "H-Hicchan, what's in there?"
"I take the object from the envelope and carefully hold it in the palm of my hand."

play music music_sadness fadein 0.5

hi "I-it's Hanako's hairclip.{w} I… I gave it to her when we started dating."

show mishashort perky_sad_cas
show shizu behind_sad
with chchange

"That revelation is enough to kill the atmosphere in the room on the spot."
"For a moment, everyone merely stares at the floor, unsure of what to say."

show shizu basic_angry
with chchange

"Shizune is the first one to recollect herself, and she starts signing, giving Misha a gentle shove in order to shake her out of the dazed state she was just in before repeating herself."

show mishashort sign_sad_cas
with chchange

mi "R-right. Umm…Hicchan. We went to the nurse's office today to see if we could find out some more for you, and um…"
mi "Do you remember that incident in science class some time ago?"
"I do.{w} Hanako, Shizune, Misha and I were working on an assignment together when Shizune and Misha started grilling me for information about my activities during the weekend and made me reveal Lilly and I were buying something for Hanako's upcoming birthday."
"That triggered a panic attack with Hanako, and although we were able to get her out of the class with a minimum of attention from the rest, the whole experience was very unsettling."
hi "How could I forget about that?"

show mishashort perky_sad_cas
with chchange

mi "It seems something similar happened on Monday."
mi "It was… pretty bad, apparently. That's all the nurse would tell us, and he only told us because we said it was for your sake."
"So things are even worse than I thought.{w} My accident two days ago didn't just give Hanako a scare, it gave her a panic attack."
"Was that what the doctor was talking about when he said she was behaving 'oddly'?"
"This at least explains why she sounded the way she did when I phoned her. It was very much like the last time Lilly and I visited her shortly after that occurrence in class."

show lilly:
    alpha 1.0
with None
show lilly at right
show shizu at center
with charamove

"I turn to Lilly, who has been standing some distance away from the bed the whole time and who has been strangely quiet during my interaction with the student council duo."
hi "So, Lilly, I suppose this means you weren't able to talk to Hanako after all."
"Lilly doesn't immediately respond, and I notice how Shizune and Misha both give her an uncomfortable look."

show lilly cane_oops
with chchange

"Lilly, in turn, turns her head in Misha and Shizune's direction and shoots them a pleading look back."

show lilly basic_sad
with chchange
show shizu adjust_frown
with charachangealways
show mishashort sign_sad_cas
with charachangealways

"After fiddling with her glasses for a second, Shizune nods and makes a flurry of gestures in Misha's direction."
mi "Ummm… Hicchan, I think we'll leave the two of you alone for a while. We'll be in the cafeteria downstairs."
mi "When you're done, you can give them a call and ask them to notify us."

show shizu at offscreenright:
    xanchor 0.0 xpos 1.2 alpha 0.0
show mishashort at offscreenright:
    xanchor 0.0 xpos 1.0 alpha 0.0
with charamovechange

"Without waiting for a reply, Shizune and Misha get up, give me a quick nod and then walk out of my room with quick determined steps, leaving me alone in the room with Lilly."
"This looks rather ominous. Do they know something I don't?"
hi "Err…you'd better sit down. There's a chair a few steps away from my bed on the right side."

show lilly cane_reminisce
with chchange

li "Thank you."

show lilly at center
with charamovefast

"Lilly takes out her cane and carefully approaches while waving it in front of her until she finds the chair I mentioned."
"As she walks towards me, I take a moment to look her over."
hi "You're… not looking so good."
"I'm actually being polite. She's looking far worse than I've ever seen her before, and the only reason I didn't notice it sooner was because she was standing some distance away from the bed and Shizune and Misha were hogging my attention."
"Her posture is different than usual. I don't think I've seen her slump her shoulders before, but she certainly does now."
"When I look closer, I also notice bags under her eyes as if she's completely skipped sleep last night."
hi "Lilly, what's going on?"

show lilly cane_concerned
with chchange

li "Hisao, I… did speak with Hanako yesterday."
"Her voice sounds softer than usual, almost a whisper."
hi "Judging by the envelope she left, I don't get the impression it was a spur-of-the-moment thing."
"Lilly sadly shakes her head."
hi "Why don't you start at the beginning?"

show lilly cane_displeased
with chchange

li "After your phone call, I went over to her room."
li "The door was locked of course and she didn't react to my knocking at first, but I kept trying and eventually she opened the door for me."
li "She told me I shouldn't have visited her.{w} She said she wanted to see me off with a smile and she didn't want our last moments together to be like this."
li "I told her that I asked Akira to postpone our departure, and with luck I could be here for her for a little while longer.{w} I expected her to be happy or at least relieved, but she didn't react at all to this news."
hi "Go on."
li "I asked if she wanted to go and visit you here together with me, just in case Akira would fail to move the departure date. I was pretty sure the doctors would have made an exception for us."

show lilly cane_reminisce
with chchange

li "But she wouldn't.{w} She told me that she wasn't your girlfriend any longer. That she couldn't be your girlfriend any longer."
li "I asked her why, but she wouldn't tell me. Then I asked her what happened the day before, but she wouldn't tell me that either."
li "Instead, she asked me to leave."

show lilly cane_displeased
with chchange

"Lilly sighs deeply."

show lilly cane_reminisce
with chchange

li "I…I should have left.{w} But at that time I didn't. I couldn't."
li "I kept reminding her of all the wonderful times you two had together. I kept trying to find out what caused her to act the way she did. I kept trying to convince her to go and see you."
li "I thought… I thought if she would just go and see you, she'd change her mind."
li "She kept telling me to leave her alone. I-I must have pressured her too much, because suddenly she… she…"

show lilly cane_sad
with chchange

"Lilly swallows, and for a moment I think she's going to break down."
"Then she continues, her pain evident in every word she says."

show lilly cane_concerned
with chchange

li "She…{w=1.0} lashed out at me."
li "She screamed at me to leave her alone. She said I was only here to make myself feel better. I said I was here because I wanted to support her. Because she is my best friend."
li "Then she snapped that I had never been interested in her as a friend. That I had only been interested in fixing her. That she was nothing but a project to me."
li "And then she told me to go away… and to never come back."

show lilly cane_reminisce
with chchange

li "I… I was terrified of her at that moment."
li "I turned around and fled the room. I haven't been back since. I don't think I could even if the door wasn't locked."

show lilly cane_sad
with chchange

"Unable to keep her emotions in check any longer Lilly stands up and holds her face in her hands before bursting into tears."
li "I'm sorry, Hisao…I-I've messed up everything."
"I can barely believe what I'm hearing."
"Hanako screaming at someone else, at Lilly of all people, is almost impossible for me to imagine."
"She's such a meek and subdued girl she usually has trouble even raising her voice. But the sight of the sobbing Lilly in front of me leaves me very little doubt that this is what has happened."
hi "Lilly…"

show lilly cane_sad_close
with chchange

"I sit upright, gently wrap my arms around her and hold her as she cries, her carefully crafted lady exterior completely shattered."

show lilly cane_reminisce_close
with chchange

li "I-I could hear her last night, Hisao."
li "I… I could hear her cry on the other side of the wall."
li "And I couldn't do anything to help her."
hi "We'll find a way, Lilly."
"At least, I hope so. I'm not so sure myself."
"Are there any other ways to approach Hanako now that she's pushed both me and Lilly away? Is this really how our little family was meant to end? Is this how our relationship was meant to end?"
"Was the whole thing doomed from the start? Were things never meant to last beyond my first episode?"
"Lilly sniffles, obviously not convinced."

show lilly cane_sad_close
with chchange

li "I…I disappointed you, didn't I Hisao?"
hi "Don't be so hard on yourself."
"Truth be told, I wouldn't have expected Lilly's attempt to talk Hanako out of her depression to backfire like this."
"For as long as I've known her, Lilly has always been a steady pillar of support for both Hanako and me.{w} Whenever I was lost at what to do, Lilly would always nudge me in the right direction in that calm, confident and motherly manner of hers."
"But that was before this whole Scotland business reared its head. I had no doubt this thing has been on her mind constantly."
"Did her own worries throw off her judgment? That seems to be the case."

show lilly cane_reminisce_close
with chchange

li "I-I feel I failed both of you."
hi "You've always been there to support us, Lilly. And you've been doing a great job. But you're only human."

show lilly cane_sad
with chchange

"Her flood of tears slowly subsiding, Lilly lets go of me and sits down again next to my bed, taking out a fancy embroidered handkerchief to dry her tears."
li "I probably shouldn't have pressured her the way I did."
hi "The last time Hanako locked herself away, I was the one who was dying to drag her out and you were the one who told me it was probably best to back down and let Hanako sort things out on her own."
hi "That advice might very well have prevented our relationship from failing before it even started. So I can't help but feel there's some irony in the way things played out."
hi "It seems… a little unlike you."

show lilly cane_weaksmile
with chchange

"Lilly gives me a tired smile, obviously aware of what I just pointed out."
li "I'm used to pacing my life in such a way that I can always carefully consider the situation before acting. It's how I've always done things."

show lilly cane_displeased
with chchange

li "I'm afraid I function very badly under pressure."
li "I admit I have acted rashly. It's just that I… At the time I didn't even know if Akira would succeed in extending our stay here."
li "I thought that maybe I only had a few hours left here before I'd be forced to leave, and I couldn't bear the thought of leaving the two of you in the middle of a situation I share some responsibility for myself. I would have felt like abandoning you."
hi "Just because we were on our way to buy stuff for your seeing-off party doesn't mean you are responsible for what happened."

show lilly cane_concerned
with chchange

li "That's not what troubled me. Hisao, what do you think triggered Hanako's panic attack this Monday?"
hi "The most realistic assumption I can come up with is probably the prospect of losing one more person dear to her."

show lilly cane_reminisce
with chchange

li "One more person? Or perhaps two more?"
"I take a moment to consider Lilly's suggestion."
"When I had my heart attack in front of Hanako, she was already busy grappling with the fact she was about to lose Lilly.{w} I have to admit the theory of Lilly's rapidly approaching departure playing at least a role in this sounds very plausible."
li "And unlike your heart attack, me going away has been a conscious choice on my part."

show lilly cane_sad
with chchange

li "But I've never meant to hurt her, Hisao. I've never meant to hurt anyone."
hi "Hey, nobody could have predicted this."
"She sadly shakes her head."
li "In the end, I felt responsible for this situation and felt it as my duty to help sort it out."
li "There may be some truth in Hanako's point about my actions merely serving to ease my own conscience."
hi "That may be so, but I think I would have acted exactly the same in your situation. And I'm willing to bet all my limbs on it that the same is true for Hanako."

stop music fadeout 0.5

scene bg hosp_room2
show lilly cane_listen
with shorttimeskipsilent

play music music_comfort fadein 0.5

"We stay quiet for a long time, neither of us really knowing what more to say."
"Eventually, I see a doctor passing by in the hallway, looking into my room and checking his watch."
hi "Apparently the staff here thinks you're wearing out your welcome. Hopefully you can come back some time tomorrow."

show lilly cane_displeased
with chchange

li "I will."

hide lilly
with charaexit

"I take the receiver from the phone on my nightstand, call the cafeteria's number and ask them to call a girl with crazy pink drill hair and a girl with glasses using sign language and direct them to my room."
"As I finish, I notice Lilly has sought out the sink near one corner of the room and is busy washing the tears off her face and tidying herself up as best as she can."
"I cannot help but chuckle."
"Even under these circumstances, Lilly still won't be caught dead facing Shizune looking anything less than a hundred percent presentable.{w} Some things will probably never change."
hi "Lilly, you should probably try to get a good night's rest."

show lilly cane_listen
with charaenter

li "You too, Hisao. I will make an effort on my part, although I cannot guarantee anything."
hi "You can use my dorm room for tonight if you like. The keys are still in the pockets of my uniform."
"Lilly considers it for a moment, but then adamantly shakes her head."

show lilly cane_weaksmile
with chchange

li "Refused."
hi "It'd at least eliminate the temptation of listening in on Hanako."

show lilly cane_smile
with chchange

li "I appreciate the gesture Hisao, but only one girl in the world has any business sneaking into that dorm room of yours and sleeping in your bed."
"She firmly taps the floor ahead of her with her cane as if to further emphasize her point."
li "And that girl is Hanako."

stop music fadeout 3.0
scene black
with Dissolve(3.0)

return