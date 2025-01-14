label sisterhood_ch16:
label .sh_ch16:

scene black
with None
stop music
scene bg school_roof_rn
with Dissolve(2.0)

play music music_hanako fadein 0.5

nvl clear
nvl show dissolve

n "{i}I'm worthless.{/i}"
n "{vspace=30}As I sit on the ground, knees drawn up to my chin and my hat almost pushed over my eyes, that thought keeps returning to me over and over."
n "{vspace=30}{i}I'm worthless.{/i}"
n "{vspace=30}The period after Hisao made me his girlfriend has been the happiest time of my life. The person I was in love with loved me as well, and we started a relationship. We were both going through a difficult time and made a pledge to support each other in each other's times of need."

nvl clear

n "{i}I'm worthless.{/i}"
n "{vspace=30}Due to my success in winning Hisao's heart, I started reconsidering my previously held belief that I was a useless person to others. I started believing I was only as useless to people as I allowed myself to be. I started making active efforts to become a better girlfriend to Hisao, a better best friend to Lilly and a better club member to Naomi and the others."
n "{vspace=30}{i}I'm worthless.{/i}"
n "{vspace=30}I started enjoying the small things in life. The girl-talk with Lilly, the brainstorming sessions over headlines and captions at the club, the tranquil days in Hokkaido and the occasional lovey-dovey exchanges with Hisao. Each of them brought a smile to my face when I recalled them before falling asleep in the evening."
n "{vspace=30}{i}I'm worthless.{/i}"
n "{vspace=30}My body, despite being scarred and disfigured, was still capable of making Hisao feel good. And despite part of my body being numb, he was able to return the favor as well."

nvl clear

n "{i}I'm worthless.{/i}"
n "{vspace=30}I stopped trying to survive from day to day and started considering my options for the future. If only things could have stayed like this for a little while longer."
n "{vspace=30}{i}I'm worthless.{/i}"
n "{vspace=30}The person I considered my best friend announced she might be leaving the country and it seemed my efforts to sway her had the opposite effect. Then, last Monday, everything came crashing down. Once more, I became an emotional mess hiding away from the world."
n "{vspace=30}{i}I'm worthless.{/i}"

nvl clear

n "Yesterday, a small glimmer of hope appeared. Hisao contacted me and wanted me to be there when he returned. To welcome him back."
n "I took a sleeping pill that evening, the first one since Monday, in the hopes of getting rid of the bags under my eyes that accumulated this week. Maybe we'd be able to reconcile if we could just pretend nothing had happened for just a little while."
n "{vspace=30}But I messed up once more and disappointed him again, and now he was no doubt being welcomed by everyone else. Lilly, Shizune, Misha… maybe even Kenji. Everyone except me."
n "{vspace=60}I wonder how long I can still stay here. There's no school right now, so the building is nearly deserted. Students are hanging out at their dorms, in the gardens or near the track. I don't think anyone will have much reason to hang out on the roof today, seeing that the sky is cloudy just like last Monday."
n "I wonder how long I should stay here."
n "Are people going to discover I'm not in my…"

nvl hide dissolve

play sound sfx_door_creak

"I tense as I hear a sound coming from the stairway. Someone is coming up to the roof."
"I could hide near the far corner that's not visible from the doorway. But that's not much use if someone wants to hang out here. I wonder who it could be."
"A teacher maybe?"
"Emi Ibarazaki? Hisao said she likes to eat on the roof sometimes. That'd be bad. She's on pretty good terms with Hisao since they started doing morning runs together. She'd probably tell him I'm here."
"Emi's artist friend? The one without arms? She likes to stare at the sky here, even when it's cloudy. That'd be okay, I think."
"I move back a little so a person would have to move beyond the doorway to see me."
"The door slowly opens and several seconds pass…"

play sound sfx_doorclose

"Then someone steps forward and closes the door behind him. The moment I catch sight of his sweater vest, I freeze like a deer in the headlights."
"Hisao!"
"It's really him. How did he know I was here?"

stop music fadeout 2.0

"My first reflex is to look at the door. But before I can even seriously consider making a break for it, his gaze follows mine, and he looks back at me with a sad expression."

show hisao basic_worry_swt_rn at twoleft
with charaenter

"Please don't look at me like that."
hi "You're not going to run away from me, are you Hanako?"
"I don't respond, but after a moment I slowly shake my head."
hi "You weren't in the library or the tea room and Lilly didn't hear you in your own room either, so I started checking the spots most suitable to avoid people."
"Am I really that predictable?"

show hisao:
    ease 2.0 center
with None

"He slowly walks up to me, but stops several meters away from me as if suspecting that getting any closer might trigger an involuntary fleeing response."
"For a minute or so, we just look at one another, unsure on what to say or do. Then he takes the plastic bag he's carrying in one hand and pulls something out of it."

show hisao basic_speak_swt_rn at center
with charachangealways

hi "A little something I picked up at the gift shop near the hospital's cafeteria."

show bouquet:
    center
    ypos 1.3 alpha 0.0
    ease 1.0 ypos 1.0 alpha 1.0
with None

show hisao_roof_blur behind bouquet
with Dissolve(1.0)

play music music_innocence fadein 4.0

"My eyes grow wide as I see what it is. It's a small bouquet of flowers."
"You're so kind, Hisao."
"Why are you so kind?"
"He doesn't approach me any further. Instead, he just holds out the bouquet the way you'd hold out a dandelion leaf to a skittish rabbit."

show bouquet:
    ease 1.0 ypos 1.3 alpha 0.0
with None

hide hisao_roof_blur
show hisao basic_neutral_swt_rn
with Dissolve(1.0)

hide bouquet
with None

"After a moment of hesitation, I get up and slowly take a step forward. And then another one."
"{i}They look beautiful. I don't deserve these.{/i}"
"And another one."
"{i}I should have been the one giving you these.{/i}"
"And another one."

show hisao basic_smile_swt_close_rn
with characlose

"An expectant smile appears on his face."
"I slowly stretch out my hand, grab the bouquet and gently take it from him when he loosens his own grip on it."
"I hold the flowers to my chest, smelling the really nice odor coming from them."
"I'm not really sure how to proceed. I'd really like to thank him, but I think I'm too uneasy right now to speak."
"Part of me is happy for such a sweet gesture, but another part of me reminds me how much this emphasizes my own inadequacy and makes me feel even worse."
"Again, we're just standing there, looking at each other. After another minute, Hisao slowly starts to speak."

show hisao basic_speak_swt_close_rn
with charachangealways

hi "Hanako, you don't really need to say anything. But will you listen to what I have to say?"
"I slowly nod my head."
"It's the least thing I can do for him, even if I can't do anything else."

show hisao basic_neutral_swt_close_rn
with charachangealways

"He takes a deep breath."

show hisao basic_speak_swt_close_rn
with charachangealways

hi "This week has been very hard for both of us. I had a painful reminder this week that I'm still at this school for a reason, no matter how normal I've started feeling over the last period of time."
"That's true for me as well. For a while, I was convinced I was able to climb out of that rut I've been in for years and live an ordinary life, before I was dragged back in with a vengeance. It really is depressing."
hi "The last time I had a heart attack, it redefined me. It changed my outlook on life, on myself and on others. And not at all for the better."
hi "I forgot about all the small things in life I used to derive happiness from. I didn't rediscover them until I met someone with whom I could share those things with."
"That's… probably true for me, too."
hi "I have no intention of letting this event become a similar turning point in my life, Hanako. I want to pick up where I left off."

show hisao basic_smile_swt_close_rn
with chchange

hi "I still want to graduate here and study science. I still want to improve my physical condition in order to stretch the limits my arrhythmia imposes on my life."
hi "I still want to get a few more members for my club. I still want to make more memories with the people I have here. And preferably, with the girlfriend I have here as well…"
"Hisao…"

show hisao basic_speak_swt_close_rn
with chchange

hi "For all the misery this week has brought, we have plenty of good memories to compensate, Hanako. I know I can't force you of all people, who has lost so much already, to stay with a person who could theoretically die at any moment…"
"Wait! What…?"
hi "…I just want you to know how terribly sorry I am to have put you through all of this…"
"Wait! No, Hisao, that's not what… Did you think I…?"
hi "…I know I'm being selfish for asking you this, but…"
ha "You're wrong!"

show hisao basic_worry_swt_close_rn
with chchange

"I blurt out my thoughts. For a second, he seems shocked, not expecting me to interrupt his carefully rehearsed speech like this."

show hisao basic_neutral_swt_close_rn
with chchange

"Then he gets a puzzled expression on his face."

show hisao basic_speak_swt_close_rn
with chchange

hi "Wrong about what?"
ha "I… I would never think that way about you."
hi "What way?"

show hisao basic_neutral_swt_close_rn
with chchange

"I swallow."
ha "M-maybe there are p-people in this world who would not allow themselves to get close to you, because they're afraid to l-lose you p-prematurely."
ha "But if everybody thought that way, you'd always remain alone. That'd b-be too cruel. You d-don't deserve that. N-not you…"
hi "You can't deny it's quite a burden."
ha "I-I know. And I w-was often reminded of it."
ha "Each t-time I s-saw you come back from the running track… each t-time I saw you take… or not take… your medication… each t-time… each t-time I got into bed with you, I remembered."
ha "B-but… when you b-became my boyfriend, I m-made a choice to accept that burden. Because you accepted mine."

show hisao basic_speak_swt_close_rn
with chchange

hi "Then why…?"
ha "B-because…"
"I feel the lump in my throat returning."
"I struggle to get the words I need to say out of my mouth before I get too scared to say them."
ha "B-because I couldn't do anything for you."
hi "What do you mean?"

show bg:
    yalign 0.9
    ease 1.0 zoom 1.2
with None

hide hisao
with dissolve

pause 0.5

with vpunch

"I feel my legs getting weak. I cover my face with my hand and drop to my knees, unable to keep my emotions in check any longer."
ha "When we started dating, we promised to support each other in times of need."
ha "But while you were l-lying there on the street, I couldn't do a thing for you. I saw you looking at m-me… but I couldn't m-move. I couldn't p-phone for an ambulance, I couldn't call for h-help… I couldn't even hold your h-hand to reassure you."
ha "I'm… worthless."
"Despite my best efforts to contain them, tears are flowing down my cheeks, and my shoulders shake as all the guilt and shame that have been eating me up all week long come flowing out of me."
ha "I t-thought, maybe it was better if I broke up with you, so you could be with someone who could make you happy and also wouldn't f-fail you like I did."
ha "What g-good are all the small things like homemade m-meals and games and caresses when I can't even be there for you… the very moment you need me most?"

show hisao basic_smile_swt_superclose_rn
with charaenter

"I can feel his arms wrap around me and pull me close."
hi "Hanako, it's… It's okay."
ha "It's n-not okay. *sniff* W-what do you think would have h-happened *sniff* if we had been alone? You c-could have *sniff* died right in f-front of me while I just s-sat there doing n-nothing."

show hisao basic_worry_swt_superclose_rn
with chchange

hi "Hanako, I…"
ha "Hisao, I-I'm so sorry."
"For a long while he just holds me without saying anything as I sob against his shoulder."
"I wonder if he's going to try and tell me not to worry about it. Is he going to comfort me by telling me it'll all even out nicely with a couple of lunches and a night between the sheets?"

show hisao basic_speak_swt_superclose_rn
with chchange

hi "Hanako?"
ha "Y-yes?"
hi "Was that an apology?"
ha "W-what?"
hi "Were you apologizing?"
ha "Y-yes."

show hisao basic_smile_swt_superclose_rn
with chchange

hi "Okay. I'll accept your apology, if you accept mine."
ha "Yours?"

show hisao basic_neutral_swt_superclose_rn
with chchange

hi "I couldn't help you either while you were having a panic attack, Hanako. Even though I promised myself that if what happened that day in science class would ever happen again, I'd be there to calm you down and reassure you."
hi "I wasn't able to keep that promise."
ha "B-but you were having a heart attack at the time. There's no way I could expect…"
hi "There no way I could expect you to keep your cool in the middle of a panic attack either."
ha "P-please stop comparing the two."

show hisao basic_speak_swt_superclose_rn
with chchange

hi "Why? Because it's devastating to your argument? We could ask your own therapist for her opinion, but I think if you're really honest we can agree that neither of us was in a position to help the other and that expecting otherwise would have been very unreasonable."
ha "It's… not that easy."
hi "Of course not. I'd probably feel awful about it too if I had been in your place, even though it's unreasonable."
hi "But I'm not blaming you. If there's blame to be passed around, I feel it's justified that I take my part, which happens to be slightly larger than yours."
ha "T-that's not true."
hi "But it is. Your panic attack took place because I got into an accident. That accident took place because I disregarded your advice and acted rashly."
hi "If someone is to be blamed, I should be that one."
ha "It… wasn't really your fault. M-most people wouldn't walk slowly in the middle of a rainstorm."

show hisao basic_neutral_swt_superclose_rn
with chchange

hi "That's my point. It was a really small screw-up that happened to have big consequences, but there's no valid reason for either of us to beat ourselves up over this."
ha "E-even so… I didn't even visit you. I should have been by your bedside…"
hi "I wasn't able to help you either while you were in your room fighting off a depression."
ha "Please s-stop doing that!"
hi "Look, the point is that we both had our own problems to deal with first."
"That's kind of depressing."
ha "So… We're not really t-that good at supporting each other in times of need, are we?"

show hisao basic_smile_swt_superclose_rn
with chchange

hi "We both want to support each other to the best of our ability, and sometimes that's a little bit less than we'd like it to be. But it might still be enough for the other person."
hi "I couldn't be there for you while I was in the hospital, but I can be here for you now if you'll still have me."
"Without thinking, I give him a quick kiss on the cheek."
ha "You're… doing a great job. I just wish I could return the favor."
hi "You already have."
ha "How?"
hi "By waiting for me like I asked you yesterday."
ha "B-but I wasn't at the gate when you arrived. I couldn't even…"
hi "But you were waiting for me. Misha said she saw you waiting out there for pretty much the entire morning."
ha "I… w-was. B-but…"

show hisao basic_neutral_swt_superclose_rn
with chchange

hi "Something happened?"
ha "I saw you… in the distance. Together with… two other people. I thought those were probably your p-parents."
ha "I… was a-afraid to face them after n-neglecting you the entire w-week and I… got scared and ran off."
"I hang my head in shame, but he doesn't seem bothered by it."

show hisao basic_speak_swt_superclose_rn
with chchange

hi "They were my parents alright. But what you did was probably for the best. This talk would have been really awkward with other people present. The important thing is that you were there and waited for me."
ha "Hisao, why was m-me waiting there so important to you?"
hi "One of the disheartening things about my first stay in the hospital, Hanako, was that by the time I was finally released, everyone except my parents had already moved on. And I was already aware of that while I was still lying there."
hi "I was thinking… If there was just one other person who was out there waiting for me… anticipating my return… I could have easily made it through the whole thing, even without visitors."
"I know what you mean, Hisao. I know exactly what you mean. That really would have helped me too when I was in the hospital for so long."
"I think I know what to do now."

show hisao basic_neutral_swt_close_rn
with charadistant

"I gently break his embrace and take his hands in mine."
ha "Hisao… then… then I will be that person for you."
ha "If you… were to get into the hospital again, even if I can't visit you, I'll be waiting for you no matter how long you have to stay there. I promise."

show hisao basic_smile_swt_close_rn
with charachangealways

"Despite the fact my face is all red from crying, I do my best to smile at him."
"Hisao doesn't say anything, but I can tell by his smile how much my words mean to him."
"I let go of him, gently take his face in my hands and give him a short, sweet kiss on the lips."
ha "Welcome back, Hisao. I've missed you."
"Again, he doesn't respond, but I see a small tear from one of his eyes. He then brings one hand up to my face, softly brushes my hair lock aside and then presses his other hand to the side of my head until I hear a familiar click."
"My hairclip. He's kept it with him."
"He doesn't ask me to be his girlfriend again. I don't bring it up either. We don't need words for this moment."

show black
with shuteye

"Instead, he simply presses his lips on mine, and we kiss again, longingly, passionately this time, throwing off the weights that have been on our shoulders the whole week."

stop music fadeout 2.0

scene bg school_roof_rn
with Fade(1.0, 0.0, 1.0)

play music music_comfort fadein 4.0

"I'm not sure how long we've been sitting here. An hour? An hour and a half? We've barely spoken a word the entire time."
"He's just been sitting here on the ground, leaning against the wall and I'm sitting on his lap, my head against his chest while he's stroking my hair."
ha "Hisao?"

show hisao basic_smile_swt_close_rn
with charaenter

hi "Yes?"
ha "Your parents, are they still here?"
hi "I asked Lilly, Shizune and Misha to keep them occupied while I searched for you. I think if they wanted to leave, they would have called me on my cell phone."
ha "They live pretty far away from here, don't they?"

show hisao basic_neutral_swt_close_rn
with chchange

hi "Yeah, I've seen them more often this week than I have in the last few months."
ha "Do you get along with them?"
hi "We're not extremely close since they work long days, so I was often home alone until late in the evening."
ha "But they still took time to visit you this week."
hi "Yeah, they even wanted to take me home to get some rest after picking me up from the hospital. You should have seen me freak out when they told me that."
"I giggle at that mental image."

show hisao basic_smile_swt_close_rn
with chchange

hi "But they meant well."
ha "I guess I should spend some time with them before they leave, shouldn't I?"
hi "Yes. I won't be going anywhere."

play sound sfx_phonedial

"Hisao takes out his cell phone, and I see him call Lilly's number. He waits a few seconds, and then I vaguely hear a voice on the other side."

show hisao basic_neutral_swt_close_rn
with chchange

hi "Hey Lilly, it's me."
hi "Yeah, I found her. And we reconciled."
hi "Yeah, me too. Me too."
hi "Where are you now? Are you guys still giving my parents a tour of the school?"

show hisao basic_speak_swt_close_rn
with chchange

hi "The Shanghai? Why'd you go there?"
hi "Shizune was bored, and she convinced them to take you there? I see."
hi "Actually, could you ask them to stay there? I want to spend some private time with them, and the Shanghai is more comfortable than my dorm room. I'll come down there in a minute."

show hisao basic_neutral_swt_close_rn
with chchange

hi "No, I'll be okay. You can probably stay for twenty more minutes or so. I could…"
hi "You still have some shopping to do? That's fine too. Say, Lilly, could you… Hello?"

show hisao basic_smile_swt_close_rn
with chchange

hi "Well, certainly not Misha."
hi "Misha, could you give Lilly her phone back?"
hi "Sure, sure, I'll treat you guys for your trouble. No need to try and guilt trip me into it."

show hisao basic_speak_swt_close_rn
with chchange

hi "No, I'm not gonna foot your entire bill."

show hisao basic_frown_swt_close_rn
with chchange

hi "Okay, three things. One: that has nothing to do with the matter at hand, two: I was only six at the time and three: why the hell is she telling you about that?"
hi "Misha, put Lilly on the damn phone already! Hello?"
"With an annoyed face, Hisao snaps the phone back shut. I chuckle at the scene that just unfolded in front of me."
ha "Trouble?"
hi "Just Shizune and Lilly extracting every embarrassing piece of information there is to know about my childhood from my mom."

show hisao cross_smile_swt_close_rn
with chchange

hi "I'd better get down there before Shizune procures enough blackmail material to put me on the student council's volunteer list for the rest of the year."

hide hisao
with charaexit

"I get off his lap, and we both head down the stairs to the entrance of the school building."

show hisao basic_smile_swt_rn
with charaenter

hi "I'd better be off now."
ha "You're going to walk all the way to the Shanghai? Is that okay?"
hi "I've been lying in bed for nearly a week. I really need to stretch my legs a bit."
hi "I'll be fine. I'm going to take my time, the whole way's downhill, and I'll be sure to take a short rest half-way through. Promise."
ha "How about your way back?"
hi "Mom and Dad went there by car. They'll drive me back to school afterwards."
ha "Ummm… Can I walk along with you a bit?"
hi "Fine with me. Be sure to drop those flowers off in your room first."
ha "Y-yes. Meet at the gates?"
hi "See you there."

stop music fadeout 2.0

scene bg school_gate_rn
show hisao cross_grin_swt_rn
with locationskip

play music music_soothing fadein 4.0

"Hisao laughs as I walk past the school gate."
hi "Nice umbrella you've got there."
ha "T-thanks."
hi "Did you want to come along just in case those clouds above us decide to drop a rainstorm down on me?"
ha "N-not really. I mean… Not just that."

scene bg suburb_roadcenter_rn
with locationchange

"We head down the road and true to his word, Hisao adopts a pace that's barely distinguishable from Lilly's."
"After ten minutes, we sit down on a rock near the side of the road."
ha "Ummm… H-Hisao?"

show hisao basic_smile_swt_rn
with charaenter

hi "Yes, Hanako?"
ha "There's… probably something you should know. About… me and Lilly."

show hisao basic_neutral_swt_rn
with chchange

hi "Lilly said you two had a fight."
ha "…it wasn't really a fight…"
"That's not a lie. It was far too one-sided to be a fight."
"Lilly was uncharacteristically persistent that day. Eventually I completely lost it and just tore into her."
"I'll never forget the hurt and frightened look on her face that moment. All I wanted was for her to leave me be. I never wanted to hurt her."
"I immediately regretted lashing out at her, but I couldn't find the words to stop her from leaving the room, and she couldn't see the pained expression on my face."
hi "Are you planning to talk to her?"
ha "I don't think she ever wants to talk to me again."
"I told her never to come back after all. How horrible can a person be?"

show hisao cross_speak_swt_rn
with chchange

hi "Don't say that. Lilly feels horrible about what happened. She blames herself much more than she blames you."
ha "She does?"
hi "Yeah. This week's been hell for all three of us."
ha "…"

hide hisao
with charaexit

"Hisao gets up, and we prepare to walk the rest of the way down, but after a few minutes he suddenly turns around and looks me straight in the eye."

show hisao basic_neutral_swt_rn
with charaenter

hi "Hanako?"
ha "Y-yes?"
hi "You don't hate Lilly, do you? I mean, she can be a little bit overbearing at times, but she means well. I remember you telling me she was a very special person to you and that you loved her a lot."
ha "I-I don't h-hate her. I just… wish things were different between us."
hi "Different?"
ha "…it's complicated…"
hi "I see."
ha "D-do we have to talk about this now? I'm still feeling a bit drained."

show hisao cross_smile_swt_rn
with chchange

hi "We can talk about it later."

stop music fadeout 2.0

scene bg suburb_shanghaiext_rn
with locationchange

"Ten minutes later we stand in front of the Shanghai."
"Hisao dropped Lilly another quick phone call. Officially to ask her to get him some things from the store, although I'm pretty sure the real reason was to find out about her location so she and I don't accidentally run into each other."
"For a few moments I think back on the day."
"The best I was hoping for this morning was an awkward greeting with Hisao followed up by an involuntary game of hide and seek. Instead, we managed to put this week's events behind us, and we've successfully averted the first crisis in our relationship."
"It was a very rough ride, but I also feel a bit proud. Maybe our relationship is more resilient than I thought at first."
"One thing that stands out in my recollection of today are my words to Hisao."
"Now I think back about it, my promise to wait for him if he gets hospitalized again sounded a lot like a long-term commitment. And now he's about to enter the Shanghai, there's another decision for me to make."
"He's not saying anything, but I bet the same matter is on his mind as well."
"Can I do this?"
ha "Hisao?"

show hisao cross_speak_swt_rn
with charaenter

hi "Yeah?"

play music music_friendship fadein 4.0

ha "What do you t-think of me?"

show hisao cross_smile_swt_rn
with chchange

hi "I love you, Hanako."
ha "I l-love you too, Hisao."

show hisao basic_smile_swt_close_rn
with characlose

"I extend my left hand, and he takes it with a smile."
ha "I… I won't be staying l-long."
hi "That's okay, Hanako. This means a lot to me."

scene bg suburb_shanghaiint
with locationchange

play sound sfx_storebell

"He gently leads me inside, and we walk towards the spot where we usually sit."
"Ahead, I can see a middle-aged couple; the same people who got out of the car with Hisao at noon. The man has a few facial features that look familiar to me."
"They wave at Hisao as we approach, and then their eyes fall on me."
"I can tell that they're staring, and I also know what they're staring at."
"My knees start shaking a bit, so I squeeze Hisao's hand a little harder and try to focus all my attention on him in an attempt to block their gaze and my growing anxiety from my mind."

show hisao basic_smile_swt_close
with charaenter

"As we reach the table, I try to read Hisao's expression. He's a bit nervous as well, but also wears a proud smile as he opens his mouth to speak."
hi "Mom, Dad… There's one more person here at Yamaku I'd like you to meet."
"Taking off my hat, I bow as deeply as I can and then take a deep breath."
ha "G-good afternoon. My n-n-name is H-Hanako Ikezawa."
ha "I'm Hisao's g-g-girlfriend."

stop music fadeout 3.0
scene black
with Dissolve(3.0)

return