label sisterhood_ch12:
label .sh_ch12:

stop music fadeout 1.0
scene bg school_dormlilly
with Dissolve(2.0)

"As I close the door, I wait a while to hear if Hanako's door is being opened or not. As expected, I hear the sound of footsteps hurrying down the hall instead."
"I laugh quietly. It hasn't been the first time Hanako's snuck off like this lately."
"I really hope she's not going to run into any patrolling staff."

play sound sfx_rustling

nvl clear
nvl show dissolve

n "I take off my clothes, put on my pajamas and sit on the edge of my bed."
n "{vspace=60}Tonight's been only the most recent of several outings Hanako and I have made lately. It's almost as if she's become my girlfriend instead of Hisao's."
n "Just recently we've had two picnics in the park, a visit to a play in a local theater, a shopping trip and yesterday a visit to a local petting zoo."
n "That last one was particularly memorable for both of us, and I'm positive that if they didn't have closing hours there, I'd still be sitting there holding the 2-months old lamb who took a liking to me and Hanako'd still be sitting next to me cuddling with the three members of the local rabbit population."
n "{vspace=30}And then there was this night."
n "We made an agreement that I'd pay the majority of the costs. My parents never left us wanting for money, and I presumed Hanako's budget, as a ward of the state, was quite a bit tighter, but she would organize the various outings."
n "All in all, I've made some wonderful memories."

nvl clear

n "“You have… one… new voicemail.”"
n "{vspace=30}The droning message from my cell phone tugs me back to reality, and I hear a voice that's become slightly more familiar to me since my trip to Europe."
n "“…Lilly, dear. Are you there? If you get this message before morning, could you call us back?…”"
n "{vspace=90}I let out a tired sigh. The problem with wonderful things is that they always end too soon."

scene black
with Dissolve(2.0)

with Pause(2.0)

play ambient sfx_cellphonering loop
with Pause(3.0)

nvl clear
nvl show dissolve

n "{cps=20}Where am I?"
n "{cps=20}What time is it?"
n "{cps=20}That sound is not my alarm clock, is it?"
n "{cps=20}I think I've heard it before…"
n "{cps=20}Somewhere…"
n "{cps=20}Still tired…"
n "{cps=20}My cell phone?"

nvl hide dissolve

scene bg school_dormlilly:
    center
    yalign 0.5 zoom 1.05
with Dissolve(2.0)

stop ambient
play music music_serene fadein 4.0

"I groggily crawl out of bed, but just before I can get to my phone, the ringing stops."
"Now I'm vexed…"
"“You have… one… new voicemail.”"
"Voice… mail?"
"“…Yo, it's me. I expected to get the voicemail. Hehe, still no early riser, eh?”"
"I let out a pained groan."
"“I wanted to talk to you, so maybe you could call me back…”"
"Not now…"
"“…eh, scratch that. I'll just wait a minute and try again…”"
"Minute? What minute?"

play ambient sfx_cellphonering loop

with vpunch

"I can't suppress a cry of surprise when my phone suddenly rings again, barely an inch away from my ear."

stop ambient

li "A-Akira…"

show akira basic_smile_phone at phonebox
with charaenter

aki "Yo. Got some time to spare?"
"I merely let out a loud yawn. Why is she calling this early?"
aki "How was your date yesterday?"
li "It wasn't a date. But it was a lot of fun."
li "We went to a nightclub, or a restaurant, or something similar, and they had a large dance floor and people playing ballroom music."
"As I describe our outing to Akira, my drowsiness slowly starts to disappear."
aki "Yeah, I got a text message from her earlier asking me if you liked that kind of music. The idea itself was hers though."
li "After some convincing, I managed to teach her a few steps. If I had more time, I could probably have made a decent dancer out of her."

show akira basic_laugh_phone
with chchange

aki "She let you drag her onto the dance floor? Man, that girl is just full of surprises."
"A soft sigh escapes my lips."
li "You don't even know half of it."

show akira basic_smile_phone
with chchange

aki "Eh?"
li "When I first met her, she was barely functioning at all. Instead of living, it seemed like she was just existing."
li "And now, she shows initiatives, has club activities, a love life, even plans for the future. She's opened herself up to new experiences."
li "It all happened… so quickly."

show akira basic_annoyed_phone
with chchange

"I can hear Akira click her tongue."
aki "You sound a bit down. Surely you're not longing to go back to the time when she was clinging to you as if you were a life preserver?"
aki "I mean, she's not your child. She never was."
li "I think you misunderstand…"

show akira basic_resigned_phone
with chchange

aki "Eh, whatever. Anyway, I didn't really call you to ask about your evening, though I wanted to be sure you were fully awake before getting to the main topic."
"I'm pretty sure I know what that main topic is about."
aki "I got a call from Scotland last night. They said they spoke to you."
li "That they did."
aki "And that you made a decision."
li "Y-yes."
aki "So… Are you sure you're going to accompany me to Scotland next week?"
li "…Probably as sure as I'm ever going to get on this…"
aki "When did you decide? Last night?"
li "More or less. Although it wasn't decided on a whim, if that is what you're asking."
aki "Well… As long as it's your decision and your decision alone, I won't argue it."
li "…Akira…?"
aki "Yeah?"
li "How did you… break the news to your boyfriend?"

show akira basic_lost_phone
with chchange

aki "I don't think you want to handle things my way. I doubt you even could."
li "You're not being very helpful."

show akira basic_resigned_phone
with chchange

aki "I don't have any advice for you, Sis, but I'm confident you'll pull it off."
aki "Between the two of us, you were always the diplomatic one."
li "I'm not exactly that confident about it myself."
aki "Let me know how it goes. And remind me to call the school administration to take care of the paperwork regarding the transfer."

$ _window = False

hide akira
with charaexit

stop music fadeout 2.0

scene bg school_dormlilly
with Fade(1.0, 1.0, 1.0)

nvl clear
nvl show dissolve

n "Part of me probably would have liked to keep this to myself for a little while longer, but I don't think that'd be a good idea."
n "Hanako and Hisao already sensed something was afoot last time, and I don't feel it's fair to keep them in the dark unnecessarily."
n "Even so, I'll be glad when this evening is over. I invited them over to my room during lunch break. They'll probably arrive together."

nvl clear

n "They'll probably be disappointed in me. Especially Hanako."
n "{vspace=30}Should I try to lift their spirits? Or will that seem hypocritical?"
n "{vspace=30}I hate situations like these. But I can't just sneak away in silence and never return."
n "{vspace=90}I'm going to miss you two."
n "Especially you, Hanako."

nvl hide dissolve

play sound sfx_doorknock2

"My thoughts are interrupted by a quiet knock on the door."

play sound sfx_dooropen

"My invitation to come in is followed by the sounds of the door opening and two people walking in."

show hisao basic_neutral_uni:
    xanchor 1.0 xpos 1.3
show hanako basic_worry:
    xanchor 1.0 xpos 1.7
with None
show hisao at twoleft
show hanako at tworight
with MoveTransition(3.0, time_warp=_ease_time_warp)
with Pause(1.0)
show hisao:
    ypos 1.1
show hanako:
    ypos 1.1
with charamove

"I notice they're unusually quiet while I pour the tea."
"I ask them both how things are going at their respective clubs, but from the short answers I get, it appears neither is eager for a lot of small talk."
"As I search for an opportune way to bring up the obvious subject, Hisao suddenly speaks up."

play music music_drama fadein 2.0

hi "Lilly, from the hesitant way you invited us here during lunch, we got the impression you wanted to tell us something important."
hi "We all know what it is about, so maybe we should just get it out of the way without further ado."
li "You're correct, Hisao. It is about the matter of my parents' summons."
hi "You've made a definite decision then?"
li "Yes. I wanted the two of you to know about it before I tell anyone else."
"In a way, I've already broken the news to them. Why would I need to tell anyone else I'd be staying here?"
hi "You've decided to answer it."
"Not a question, but an observation."
"I merely nod quietly."
li "My family dearly wants me to join them, and Akira will be going there as well. I can still fulfill my dream of becoming a teacher there."

show hisao basic_worry_uni
show hanako emb_downsad
with charachangealways
with Pause(1.0)

"Silence follows. Probably the most painful silence I've ever endured."
"When Hisao speaks again, his voice is a lot softer than before."
hi "If that's the choice you've made and that choice makes you happy, then we'll support it. Although, the both of us will miss you terribly."
li "I won't be gone forever, Hisao. I can still call you two, and with Akira's help I could exchange things over the internet."

show hanako emb_sad
with chchange

ha "{cps=20}I'll… miss you, Lilly.{/cps}"
"It hurts me to hear the tone in Hanako's voice."
"The budding confidence that was still very evident in her voice last night seems to have vanished and is once more replaced with the scared, insecure tone that was there when she started speaking to me for the first time."
"I feel I owe it to Hanako to help her get her confidence back and remind her of how far she's already come."
li "Hanako, remember when we first met? When you entered my room for the first time after overhearing my consoling of a friend, you didn't say a single word for the entire night."
li "Even as I poured you tea and talked, you sat silently and simply listened to what I said."
li "It took many quiet meetings like that before you began to open up to me, but as you began to, I felt some of the happiest moments I've ever felt."
"I take a sip of my drink, before continuing."
li "I didn't become your friend because I pitied you, Hanako. I became your friend because I knew you were hiding not just from me, but from everyone."
li "Your ambitions, personality, interests, tastes… I didn't know any of them and neither did anybody else."
li "As you showed yourself to me, though I began to realize the person that you were and became sure that our meeting was a very special moment."

show hanako emb_downsad
with chchange

"I feel a small lump in my throat, but go on anyway."
li "I believe you are a very beautiful person, Hanako, and I am certain that you will become a strong and confident woman…"
"I have more to say, but cut myself off as I realize that what I'm saying isn't accurate. What I'm saying will happen eventually has actually already come to pass."
li "No, that's not correct. You already have become a strong and confident woman, Hanako."
li "You have shown you have obtained your own friends and hobbies, your own hopes for after graduation and your own love live from which to draw strength."
li "I want you to devote yourself to them, even after I'm not around anymore, for others will draw strength from you as well."
li "Especially in the last weeks, you have shown how much you have to offer to those around you."
li "That's why I think you will be okay, Hanako. Because you are your own self with your own life. You yourself have proven that to me."
li "I've learned many new things about you since I came back to Japan, but the most significant thing I've come to witness is how strong and independent you truly have become."
"We remain silent for a long time, but eventually Hanako speaks softly."

show hanako emb_timid
with charachangealways

ha "{cps=20}I… I… understand.{/cps}"
li "Will you be okay?"
ha "I will."
"I truly believe she will."
"We spend some time quietly drinking tea, small talk seeming inappropriate after the moments we just had."
"Eventually, Hisao addresses me."

show hisao basic_speak_uni
with chchange

hi "So when exactly will you be leaving? And how?"
li "On Tuesday the week after this one. Akira will be picking me up here, and we will spend the night at the Hakamichi home where Akira will have the rest of our luggage stored. Our flight will depart on Wednesday."
hi "So I guess we won't be coming along to the airport to see you off."
li "I do not think that will be practical. However, I'd like to save the Monday evening for a little get-together in my room if that's okay. A small seeing-off party as it were."

show hisao basic_smile_uni
with chchange

hi "That seems like a good idea, Lilly. We'll be there."
li "I'm looking forward to it, Hisao."
li "The upcoming week will be very busy for me. I have very limited time to tie up all loose ends and transfer my class representative duties to others."
"A busy time indeed. The fact that summer break is approaching makes the upcoming workload even larger."
"It doesn't seem like I'll be able to relax for a while."

stop music fadeout 2.0

scene bg school_council
show mishashort perky_sad at twoleft
show shizu behind_blank at tworight
with locationskip

mi "Awww… That's a shame, Lilly. I bet Hanako and Hisao are really sad, aren't they?"
"I smile at Misha's reaction to my announced departure. It's easy for many people to forget that Misha is more than merely Shizune's mouthpiece, and this reaction is obviously her own."
li "Saying goodbye is never easy, Misha."
li "But I draw relief from the fact that they still have each other. They'll be fine, you'll see."

show mishashort hips_smile
with chchange

play music music_shizune fadein 4.0

mi "Yeah, I'm sure they will."

show shizu adjust_frown
show mishashort sign_smile
with chchange

mi "I will not pass judgment on your decision to migrate, that is your own choice."
mi "But it is my responsibility to see to it that your sudden stepping down does not come at the cost of the functioning of 3-2 as a class."
li "That is why I'm here. I have already managed to find a classmate willing to act as my replacement."
li "After my departure, my classmate Aki Sujishi will function as representative of class 3-2. Please give her your full cooperation in the carrying out of her duties."
"And please try to treat her with what other people would call common decency."

show shizu adjust_smug
show mishashort sign_smile
with chchange

mi "I'm pleased to see you've managed to transfer your duties to one of your classmates this quickly. Then again, seeing that you've had quite a bit of practice with that over the years, I shouldn't be too surprised."
"She just can't help herself, can she?"
li "She took the task willingly and with enthusiasm. I wonder how many students in the dictatorship you've got running would take these tasks without you forcing them to."

show shizu behind_frown
with chchange

mi "Dictatorships are effective. Running a tight ship produces timely results."
mi "Do you really think our classmates' future employers will coddle them and tack on a ‘pretty please’ each time something needs to be done?"
li "Your classmates are not paid employees, and your class is not a commercial company nor a police state. People acting out of a sense of duty will always work more efficiently than people ordered to do something."

show shizu adjust_smug
with chchange

mi "I'm afraid you do not have the data to back that up, class rep. If you want a summary of what classes ended up running up against the deadlines most often, I'll be more than happy to procure one for you."
li "It's good to hear that you've managed your schedule so well that you can afford to take part in these kinds of petty games."

show shizu adjust_angry
show mishashort sign_confused
with chchange

mi "My schedule is not the problem right now. Yours is. There are still absence summaries, score charts and rosters to cover."
mi "I presume you'll be responsible and fill them all in a few hours before leaving instead of delegating them to your successor?"
li "I have reserved the last two days of my stay here for those tasks, so I am sure to have all the latest data. The time I'll be taking is about twice as much as I predict will be needed, so I will be able to take care of the paperwork even if distractions are to be present."

show mishashort perky_confused
with chchange

mi "I need to go take a bathroom break, I'll be back in a few minutes."

hide mishashort
show shizu adjust_frown
with charaexit

"It seems Misha has finally had enough of being a vessel to our argument, and I hear her walk briskly towards the exit of the room."
"I slump my shoulders dejectedly. It's silly, I'm about to leave this school permanently, and Shizune and I are still going at it as if nothing has changed."

show shizu basic_angry at center
with charachangealways

shi "…"
"Misha walking out on us has now left Shizune and me simply standing there, our argument cut off, unable to get through to the other to either continue the fight or simply get back to business."
"I'm not sure about Shizune, but I'm feeling rather embarrassed right now."
"We probably had this coming."
"I don't think there's much left to discuss anyway. I've already said what needed to be said and the rest was just both of us trying to gain the advantage over the other."
"I don't like the idea of simply turning my back on Shizune and walking away, but our communicative means are severally limited right now, so I simply bow in her direction, wait a few seconds to give her an opportunity to return the favor and then turn to leave."

show shizu behind_blank
with charachangealways
show shizu at left
with charamove

play sound sfx_dooropen

"As I take out my cane, I hear her footsteps walking towards the door, followed by the sound of the door opening."
"I think that's her way of acknowledging my gesture, so I give a quick nod in her direction and leave the council room."
"This is one thing I won't miss about this place."

stop music fadeout 3.0
scene black
with Dissolve(3.0)

return