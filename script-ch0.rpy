label sisterhood_ch0:

stop music fadeout 1.0
scene bg school_staircase1
with flashback

ta "Come in, please!"

play sound sfx_dooropen

scene bg therapist_office
with locationchange

"After I hear the reply to my knocking, I hesitantly open the door leading into the 'office' where I have my sessions every other week."
"Office isn't really a good word to describe it. Den or living room seem more appropriate. Miss Yumi has very peculiar tastes when it comes to her work place."

show takawa smile
with charaenter

play music music_another fadein 0.5

ta "Good day, Hanako."
ha "G-good day, Miss Yumi."
"As I enter, Miss Yumi gets up, approaches me and we exchange greetings and polite bows."
ta "May I have the honor of getting you some tea, Miss Hanako?"
ha "I-I humbly accept, Miss Yumi."

hide takawa
with charaexit

"The little ritual we practice at the start of every session is a bit old-fashioned, just like the room and Miss Yumi herself. But it serves its purpose well."
"Since it's exactly the same every time, I can simply repeat the phrases I always use without having to think too hard about how to respond, which usually causes me to start stuttering."
"A small bowl of tea is gently placed in my hands, and after a small bow, we both take a careful drink."

nvl show dissolve

n "When I was admitted to this school, the head nurse explained to me the teachers were not going to make a fuss if I felt anxious and wanted to leave class to catch my bearings. However, he also mentioned he was assigning me one of the therapists at school for sessions outside of school hours."
n "I sensed that they expected me to go along with this in return for the lenience I'd receive in regard to my school attendance, so I reluctantly accepted."

nvl clear

n "My first therapist was a middle-aged man with thick glasses and a scruffy beard."
n "He was polite enough, but also really intimidating. I always felt a bit like a research specimen during our sessions."
n "Eventually I was referred to another person; a rather young man with a stubble, sneakers and an awful sweater."
n "He was nice enough, but I always felt uneasy around him."
n "The third person was Miss Takawa, who was new to Yamaku at the time."
n "She told me I could start calling her Miss Yumi as a sign of trust once I felt we established such a thing. And since a few weeks I've been calling her that."

nvl hide dissolve
nvl clear

show takawa smile_close at center:
    alpha 1.0
with charaenter

ta "Well then, shall we start?"
ha "Y-yes, please."

hide takawa
with charaexit

show bg therapist_office:
    blur 20
with Dissolve(0.5)

show go_board:
    truecenter
    zoom 0.5
    ypos 0.7 alpha 0.0
    easeout 0.5 ypos 0.5 alpha 1.0
with Pause(0.5)

play sound sfx_gostone_soft

"Miss Yumi gives a small nod, and I place the first black stone onto the game board."

play sound sfx_gostone

"Miss Yumi takes one of her white stones and puts it in place with a dull tap."

show go_board:
    easeout 0.5 ypos 0.7 alpha 0.0
with None

show bg therapist_office:
    blur 0
with Dissolve(1.0)

hide go_board
with None

show takawa smile_close
with charaenter

ta "So, Miss Hanako, how have you been sleeping lately?"

play sound sfx_gostone
"{i}*tap*{/i}"

ha "Not t-too badly."
"We usually have an agreement that only the person whose turn it is is allowed to speak. If I want things to slow down, I can simply wait a bit before placing my next stone."

play sound sfx_gostone_soft
"{i}*tap*{/i}"

ta "That's good to hear. May I suggest we try a week without sleeping pills again and see if things remain that way? The worst weeks should be behind us for now."

play sound sfx_gostone
"{i}*tap*{/i}"

ha "If you say so."
"Miss Yumi is an enthusiastic Go player, and ever since our third meeting we've been playing as part of our session."

play sound sfx_gostone_soft
"{i}*tap*{/i}"

ta "If we can get you your daily eight hours of sleep again without any medication, then that's a goal we should not pass up."

show takawa serious_close
with chchange

ta "If you still have bad dreams three weeks after… that day… you could try some herbal tea. I happen to know a recipe that tends to work very well."

play sound sfx_gostone
"{i}*tap*{/i}"

ha "O-okay then."
"I don't think I actually relax while playing games, as Miss Yumi thought at first. It's quite the opposite… I grow more focused than usual."
"But since I get to focus on something other than my anxiety, my head tends to be clearer, and I'm less nervous in my interactions."

play sound sfx_gostone_soft
"{i}*tap*{/i}"

show takawa smile_close
with chchange

ta "If you were a little older, I could recommend a few sips of sake as well, but I don't think that'd be a good idea right now."

show takawa happy_close
with chchange

ta "If the principal were to find out, these old bones would be dragged onto the street in a heartbeat."

play sound sfx_gostone_hard
"{i}*tap*{/i}"

"I suppress a small giggle."
"While Miss Yumi is always a bit formal, she's not always serious and is quick to fill the silences with some small talk whenever I don't have much to say myself."

play sound sfx_gostone_soft
"{i}*tap*{/i}"

show takawa smile_close
with chchange

ta "So, how is life in the dorms these days?"

play sound sfx_gostone
"{i}*tap*{/i}"

ha "S-same as always. Except the girl in the room next to mine has moved out recently."

play sound sfx_gostone_soft
"{i}*tap*{/i}"

ta "I see. Have you ever spoken to her?"

play sound sfx_gostone
"{i}*tap*{/i}"

"Not that I can remember. {i}She{/i} tried to speak to {i}me{/i} though, around the time I moved in here. Or rather, barged into my room and pretended living next to each other was enough to make us instant buddies."
"I've kept my door locked ever since."
ha "N-no. I haven't."

play sound sfx_gostone_soft
"{i}*tap*{/i}"

ta "So I suppose you can expect to get a new neighbor soon. I doubt the housing department will leave that room empty for long."

play sound sfx_gostone
"{i}*tap*{/i}"

"That would be too much to hope for."
ha "Maybe."

play sound sfx_gostone_soft
"{i}*tap*{/i}"

ta "Maybe even someone nice."

play sound sfx_gostone
"{i}*tap*{/i}"

"Hopefully nice enough to ignore me instead of staring at me."
ha "Maybe."

play sound sfx_gostone_soft
"{i}*tap*{/i}"

show takawa calculating_close
with chchange

ta "That's not a bad move, Miss Hanako. You're getting much better at this."

play sound sfx_gostone
"{i}*tap*{/i}"

"She's just flattering me. While it's nice to play against her, I haven't beaten her a single time."
"She's a formidable player and doesn't feel the need to hold back for her opponent's sake."
ha "N-not really."

play sound sfx_gostone_soft
"{i}*tap*{/i}"

ta "I have the not-very-scientific belief that it's possible to deduce certain personality aspects of a person through their playing style while they're still learning the ropes of a game."

play sound sfx_gostone
"{i}*tap*{/i}"

"What does that say about me? Has she been analyzing me through this? Like a creative variation of a typical question form?"
ha "R-really?"

play sound sfx_gostone_soft
"{i}*tap*{/i}"

ta "Your defensive playing style fits your personality, Miss Hanako. Am I right to assume your favorite chess strategies also focus on defense?"

play sound sfx_gostone
"{i}*tap*{/i}"

"That's a pretty good deduction. Am I really that predictable?"
ha "That's… right."

play sound sfx_gostone_soft
"{i}*tap*{/i}"

show takawa serious_close
with chchange

ta "But pure defense will never win you anything. At best, it results in a stalemate."

play sound sfx_gostone
"{i}*tap*{/i}"

"Isn't that still better than losing? Is she saying I should go on the offensive instead? That'd just get me beaten sooner."
ha "S-should I play aggressively then?"

play sound sfx_gostone
"{i}*tap*{/i}"

show takawa smile_close
with chchange

ta "Playing aggressively doesn't suit you. It would be better for you to stick to what comes naturally to you and improve upon it."

show takawa calculating_close
with chchange

ta "A good offensive player forces opportunities. A good defensive player takes advantage of opportunities as they arise."

play sound sfx_gostone
"{i}*tap*{/i}"

"Are we still talking about Go here?"
ha "Ah…"

play sound sfx_gostone_soft
"{i}*tap*{/i}"

ta "We could practice it if you'd like. I'm going to leave you a few openings now and then and it's up to you to spot them and exploit them as quickly as you can."

show takawa smile_close
with chchange

"She smiles as her eyes scan the board."
ta "You might find that games like these and life in general have quite a few parallels."

play sound sfx_gostone_hard
"{i}*tap*{/i}"

"I just nod and try to focus on the result of Miss Yumi's latest move."
"Am I already supposed to look for openings?"

play sound sfx_gostone
"{i}*tap*{/i}"

show takawa serious_close
with chchange

ta "By the way, Miss Hanako, I almost forgot to tell you that I will be on leave for the next two weeks. So our next session will be in twenty-one days."
ta "If anything happens, you can always contact the head nurse here. I have no plans to take any trips, so he should have no problems getting in touch with me in the unlikely case of an emergency."

play sound sfx_gostone
"{i}*tap*{/i}"

stop music fadeout 0.5

with Pause(1.0)

#queue music music_friendship fadein 0.5

"That news makes me feel sad."
"I didn't think about it at first, but I've come to enjoy these sessions."
"I can be on my own just fine most of the time without feeling miserable, but now that I'm being told I'll have to wait for three weeks before we'll get to talk and play games again, I suddenly start to feel lonely."

play sound sfx_gostone_soft
"{i}*tap*{/i}"

"She said she's not going to be away from home."

play sound sfx_gostone
"{i}*tap*{/i}"

"Should I ask if I can visit her sometime? Just to play a few more games?"

show bg therapist_office_blur1
show takawa serious_close_blur1
with Dissolve(1.0)

play sound sfx_gostone_soft_stress1
"{i}*tap*{/i}"

"What if she rejects me?"

play sound sfx_gostone_stress1
"{i}*tap*{/i}"

"She's an adult. She has been for a long time. She's different from my old schoolmates. We get along well. She doesn't mind my scars."

play sound sfx_gostone_soft_stress2
"{i}*tap*{/i}"

ta "{size=-3}{alpha=0.8}Is something bothering you, Miss Hanako?{/alpha}{/size}"

play sound sfx_gostone_stress2
"{i}*tap*{/i}"

ha "Umm… I…"

show bg therapist_office_blur2
show takawa serious_close_blur2
with Dissolve(1.0)

"My social anxiety, which usually remains subdued during these sessions, has just returned in full force and is threatening to choke me."

play sound sfx_heartslow

with Pause(1.0)

hide takawa
with charaexit

"As my breathing starts speeding up, Miss Yumi places her bowl in front of me and then gets up to get the kettle from the brazier in the corner."

show takawa smile_close_blur1
with charaenter

ta "{size=-2}{alpha=0.9}Don't force yourself, dear. Take a sip, a few deep breaths, close your eyes and think of a clear sky or flowing water.{/alpha}{/size}"

"Just a few sentences. I can do this."

play sound sfx_heartslow

with Pause(1.0)

show takawa smile_close
with chchange

ha "{cps=20}M-Miss Yumi…c-c-can I…c-c-come o-over n-next…w-week and p-p-play a…a g-game w-with y-y-you?{/cps}"

with Pause(1.0)

show takawa serious_close
with chchange

play sound sfx_heartslow

"Miss Yumi merely looks at me with an unreadable expression on her face."
"Or rather, stares at me."
ta "Come over next week, you say?"

play sound sfx_heartslow

"Don't tell me she didn't understand. Did I really cut such a pathetic figure?"

play sound sfx_heartfast
queue sound sfx_heartfast
queue sound sfx_heartfast

"I gather all of what's left of my rapidly vaporizing determination and force myself to smile at her."
ha "{cps=20}M-m-Miss Yumi…c-c-can I b-be…b-b-be f-f-friends w-with you?{/cps}"
"I exhale deeply."
"I said it."
"I didn't think I could do it, but I said it."
"But strangely enough, Miss Yumi doesn't react."
"As I look at her, I still see that same neutral expression on her face."
"Just when I'm about to ask her if she's heard me, she slowly starts speaking."

show takawa smile_close
with chchange

ta "Miss Hanako, your friendship is the second most valuable gift in the world you can offer another person… and a priceless gift it is."

show takawa serious_close
with chchange

"Her gaze suddenly lowers and shifts to one of the corners of the table."
"A feeling of dread starts to well up inside me."
"Miss Yumi shuts her eyes for a few seconds and then forces herself to look right at me."
ta "I am very sorry that I cannot possibly accept it."

play music music_sadness

ha "Of… of course not."

show takawa serious_close_blur2
with chchange

"I try to think of something more to say. Some way to change the subject."
"But I can't."
"Of course she wouldn't want me around."
"Who would want to spend time with a useless person like me?"
"She's only tolerating me because she's being paid for it."

play sound sfx_heartslow
show black:
    alpha 0.2
with Dissolve(1.0)

"I have to get out of here."

play sound sfx_heartslow
show black:
    alpha 0.3
with Dissolve(1.0)

"I feel a lump in my throat. I desperately try to swallow it."

play sound sfx_heartslow
show black:
    alpha 0.4
with Dissolve(1.0)

"I have to get out of here."

play sound sfx_heartslow
show black:
    alpha 0.5
with Dissolve(1.0)

"I squeeze my eyes shut, but I can't prevent tears from rolling down my cheeks."

play sound sfx_heartslow
show black:
    alpha 0.6
with Dissolve(1.0)

"I have to get out of here now."
ta "{size=-6}{alpha=0.6}Miss Hanako…{/alpha}{/size}"

play sound sfx_heartslow
show black:
    alpha 0.7
with Dissolve(1.0)

"Go somewhere. Anywhere. Away from here."
ta "{size=-8}{alpha=0.4}Miss Hanako…{/alpha}{/size}"

play sound sfx_heartslow
show black:
    alpha 0.8
with Dissolve(1.0)

"Far away from here…"

stop music
hide black
show bg therapist_office
show takawa stern_close
play sound sfx_impact2

ta "Miss Hanako!"
"Miss Yumi's stern voice snaps me out of it."
"When I look at her, I notice she has a tissue in her hand which she offers me while her eyes look sadly, but compassionately at me."

show takawa serious_close
with chchange

ta "Before you draw your own conclusions, please let me explain."
"Explain? Is this where she's going to make up excuses? Tell me she's not worthy or something?"
ta "I'm not refusing your gift because I don't enjoy spending time with you or because you're not a sweet and caring girl. I do and you are."
ta "I cannot accept your gift because… a friendship between us would be inappropriate."

show bg therapist_office_blur2
show takawa serious_close_blur2
with Dissolve(1.0)

play music music_hanako fadein 0.5

"Inappropriate? You know what's inappropriate? Your friendliness!"
"Playing games with me and acting all interested in me!"
"Pretending that you care!"
"It's just a facade. Another tool to pry me open so you can take a look inside and determine just how broken things are!"
"I'm trying to restrain myself, but suddenly I feel furious."
"Before I can stop myself, I hiss a reply to her."
ha "{cps=20}I-I'm j-just another br-broken human being f-for you to f-fix.{/cps}"
"I regret those vitriolic words the instant they leave my mouth."

show takawa serious_close_blur1
with chchange

"But… Miss Yumi doesn't flinch."
"Instead, she refills the tea bowl and calmly looks back at me."

show takawa serious_close
with chchange

ta "Supporting your recovery, or 'fixing you' to use your own words, is what I'm here for."
ta "It'd be disingenuous of me to pretend otherwise. I am a therapist after all."
"I freeze. That's not the reaction I expected at all."
ta "Miss Hanako, the desire for friendship you expressed just now is undeniably a good thing, and I'd greatly encourage you to hold onto it, but not all friendships are undeniably good."
ta "Some friendships can be downright unhealthy. And friendships with therapists are the unhealthiest of them all."

show bg therapist_office_blur1
with Dissolve(1.0)

ha "I… I don't understand."
ta "Friendship is a bond of mutually accepted equality, Miss Hanako."
ta "True friends are equals. Two people cannot be equals if one of them is being paid to spend time with the other."
ta "Two people cannot be equals if one has learned the history of the other through a case file."
ta "True friends are willing to share both each other's joy and each other's grief."
ha "And you… can't?"

show takawa smile_close
with chchange

ta "As your therapist, I will be here as long as you need my help."

show takawa serious_close
with chchange

ta "But when you stop requiring that assistance… when you start getting better, people like me will start backing out of your life in order to shift their attention to those more in need of their presence."
ta "It's what a therapist does. It's not something a friend would ever do."
ha "So… are you saying we cannot be friends? Ever?"
ta "I believe that a good therapist will never try to become your friend, and a good friend will never try to become your therapist."
ta "No person should try to fulfill both roles for you."

show takawa calculating_close
with chchange

ta "I believe I can serve you best as a therapist because we work well together… unless you can no longer believe in me after today."
ha "I…I'm not sure."

show takawa serious_close
with chchange

ta "Please let me assure you right now, Miss Hanako, that still I believe in you."
ta "Just because I cannot be your friend doesn't mean I'm going to give up on you. I believe that you'll get the friendships you desire in time."
ha "W-why?"
ta "Because I learned one more thing from watching you play."
ha "What's that?"

show bg therapist_office
show takawa smile_close
with Dissolve(1.0)

ta "That you're not a quitter."
ta "Even though life, like me, hasn't been going easy on you, you do not quit."
ta "And because quitting is not in your character, you'll eventually come across the right opportunities."
"Now I believe she's merely trying to cheer me up."
"I really need some time alone at the moment."
"I get up to leave and Miss Yumi lets me go without protesting."

hide takawa
with charaexit

play sound sfx_dooropen

"As I open the door and turn around to bid her farewell, Miss Yumi performs what has to be the deepest and most prolonged bow I've ever seen from her."

show takawa worried
with charaenter

"When she rises I'm shocked to see an expression of genuine sadness on her face."
ta "Truth be told… I've been forced to have this talk with several people over the years, and it still breaks my heart every time I have to repeat it."
ta "I'm truly sorry, Hanako."
"For a moment I forget my own sadness and disappointment."

show takawa smile
with chchange

"Then, her smile is back and the moment is lost as her words echo in the hallway."
ta "I hope to see you here again in three weeks."
ta "Please take care."

play sound sfx_doorclose
scene bg school_staircase1
with locationchange

"My head understands her words, but my heart is still feeling miserable."

stop music fadeout 3.0
scene black
with Dissolve(3.0)

return