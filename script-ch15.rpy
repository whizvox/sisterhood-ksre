label sisterhood_ch15:
label .sh_ch15:

$ set_window_tint(TINT_HISAO)

call sisterhood_timeskip

scene bg hosp_room2
with Dissolve(2.0)

play music music_night fadein 4.0

nvl clear
nvl show dissolve

n "Upon finishing the last page of the book I've been reading since morning, I close it with a decisive snap."
n "I'm thankful to Shizune and Misha for bringing along my books. Time passes a lot more quickly while I'm absorbed in one of them. With luck, I'll be allowed to leave the hospital tomorrow around noon."
n "{vspace=60}My heart, after the initial episode four days ago, has decided to abstain from causing me further trouble, though that seems like a small comfort."

nvl clear

n "Yesterday was pretty eventful with my parents dropping by at noon and Lilly, Shizune, Misha and Akira visiting in the evening."
n "{vspace=30}For some time, it seemed like nothing was out of the ordinary, with Akira playfully mentioning how interesting it was to see Lilly and Shizune made peace with one another, to which Shizune replied that “striking a wounded adversary” was simply against her moral code; a provocation which Lilly then used to refute Akira's suggestion. Both eventually got upset at my observation that the two of them were really too proud for their own good sometimes, a remark that amused Misha and Akira to no end."
n "After Lilly and I were left alone again though, it quickly became clear she had simply been doing her best to keep up appearances, a trait of hers that both tends to impress and unnerve me."
n "It turned out that not much had changed. Lilly was still in a very depressed mood although she took my word for it when I assured her that Hanako hadn't been secretly resenting her all along as she had come to believe over the last two days."
n "I also learned that Akira has only been able to postpone their departure to Scotland for one week, and she won't be able to hold things off any longer."

nvl clear

n "In addition to the rift between Hanako and Lilly, I also have my own relation with Hanako to worry about."
n "Can our relationship still be mended? Is it fair to expect her to deal with events like last Monday after all she's been through already?"
n "If that's not possible, can we still be friends? We've been through many highs and lows together. Would ordinary friendship even be possible? I don't want her to be just a friend to me."
n "Is she going to avoid me from now on? It seems an impossible task, seeing that we're in the same class, but Hanako has been keeping up a wall between herself and the rest of the class since she started attending here. She could pull it off if she wanted to."
n "{vspace=30}Lilly, Shizune and Misha are probably going to visit again, but neither Lilly nor I have a clear idea on how to get through to Hanako."

nvl hide dissolve

"As I mull over these things, I notice a familiar figure slowly walking through the hallway."
"She stops near the door and looks to be in deep thought for a moment."
hi "Lilly? Hey, Lilly!"
"Having picked up my voice, Lilly turns in my direction for a moment to acknowledge my greeting and then turns around to talk to someone who was apparently standing behind her."

show lilly cane_oops:
    offscreenright
    ease 2.0 center
with Pause(2.0)

"After a few seconds, she turns back to me and carefully navigates herself to my bed."
hi "Are you here all on your own? Aren't Shizune and Misha with you?"

show lilly cane_weaksmile
with chchange

li "No, not this time."

show lilly at sittingpos
with charamove
show lilly basic_weaksmile
with chchange

"Lilly retracts her cane, sits down in the chair near my bed and puts it into her bag."
"As she does so, I notice something else in there; the plush puppy Hanako gave her. Has she been carrying that thing around with her all week?"
li "I started feeling bad to make them accompany me and then sit most of the time in the cafeteria while we talk here, so I decided to come alone this time."
hi "So the person you were talking to was a nurse you asked for directions?"

show lilly basic_smile
with chchange

li "Not quite. It was a staff member from Yamaku who came up to me and offered me a ride here while I was waiting for the bus."
li "Upon getting here, we made a little bet to see if I could find your room myself without any assistance."
hi "Wow, you made your way here just from memory? Your sense of direction is a lot better than mine, that's for sure."

show lilly basic_giggle
with chchange

li "The last hallway threw me off a bit. I might have lost if you hadn't called out to me."
li "Thanks to you, I was able to earn us both a free drink. Apparently they sell some good tea down here."
hi "I don't think the doctors will be thrilled with me drinking caffeine right now."
"???" "I feared that as well, Mister Nakai, so I bought you some fresh orange juice instead. It's the healthiest drink they had."

stop music fadeout 0.5

"When I look up to greet Lilly's mysterious benefactor, I notice a familiar face."

show lilly at twoleft:
    yanchor 1.0 ypos 1.1
show takawa smile at tworight
with charaenter

play music music_another fadein 0.5

"It's been a while since I've last seen her, but the old lady walking into the room carrying a tray with three drinks on it is wearing the same violet shawl and black skirt as she was when the nurse took me to see her on that day Lilly and Akira arrived back in Japan."
hi "Miss Takawa!"

show lilly basic_smile
with chchange

ta "Good evening, Mister Nakai. It grieves me that we meet again under such trying circumstances, but I'm nevertheless most pleased to see you again."

show takawa at center
with charamove

"Ever the polite one, she makes a bow and places the tray on my nightstand before putting one of the tea cups into Lilly's outstretched hands and making another bow. She then does the same with my cup of juice."
ta "Please enjoy."

show takawa:
    ease 1.0 tworight
    ease 1.0 tworight_sittingpos
with None
show lilly basic_smileclosed
with chchange

"Lilly, recognizing the old lady's gesture as a make-shift tea party, makes a bow of her own with an appreciative smile on her face."
li "Thank you for the trouble."
"I'm still trying to wrap my head around the old lady's sudden appearance. Is she here with news from Hanako?"
hi "I suppose your visit here is not a coincidence?"

show takawa calculating
with chchange

"The old lady takes another careful sip before responding."
ta "Yes and no. It was a coincidence I saw Miss Satou on my way home sitting there at the bus stop and deciding she was looking so troubled that the least thing I could do was give her a ride."

show takawa smile
with chchange

ta "But then I decided that since I was here anyway, I might as well drop by and see how you are faring."

show lilly basic_surprised
with chchange

li "I take it you have met this person before?"
hi "Only once. Miss Takawa is Hanako's therapist."

show lilly:
    linear 0.1 yanchor 1.0 ypos 1.07
    linear 0.1 sittingpos

"That news certainly surprises Lilly, for her hands shake for a moment, and she nearly drops her cup."
"Looks like Miss Takawa doesn't have the habit of mentioning her patients in her introductions to others."
li "Ah… Excuse me. I had no idea. I'm afraid Hanako never mentioned a name to me."

show takawa happy
with chchange

ta "That's alright. I usually tell my clients that therapy sessions are among the least interesting things to talk about with their friends."
"In other words, she discourages the practice."
hi "I take it that you are aware of what has happened to Hanako and me this Monday?"

hide lilly
show takawa calculating at sittingpos:
    xanchor 0.5 xpos 0.5
with charaenter

ta "That's correct. The head nurse notified me as soon as he received the news."
hi "Would you also happen to be the person who picked her up after the ambulance brought her here?"
ta "Yes, that was me."
ta "Miss Ikezawa was still in shock when she arrived here, and I decided that a hospital bed was not an ideal place for her to calm down, so I took her to my office and let her rest there."
ta "When we heard the news that your condition had stabilized, I took her back to her dorm room."
hi "Have you spoken to her since then?"
ta "I'm afraid I haven't. I informed her that I could supply her with a sleeping pill or anti-depressant for the night if she wanted one and that I'd be available if she wanted to talk, but she hasn't made use of those offers so far."
hi "Didn't you place her… you know… under supervision?"
"The old lady sighs."

show takawa serious
with chchange

ta "Yamaku is not a mental hospital, Mister Nakai. We can do very little without a client's explicit consent. I can only make exceptions if I have determined that a client is prone to suicidal tendencies."
hi "So at least Hanako does not have those. Thank goodness."
ta "Indeed, or I highly doubt any of us would have even had the opportunity to make her acquaintance in the first place."
"That's a pretty morbid thing to say. Both Lilly and I shudder at the same time."
hi "Miss Takawa, we're not really sure what happened to Hanako."
hi "Can you tell me what a panic attack is like? Hanako had one last Monday, didn't she?"

stop music fadeout 2.0

show takawa calculating
with charachangealways

"Miss Takawa looks lost in thought for a second."

queue music music_drama fadein 4.0

ta "Yes, the most severe one since she enrolled here. And it lasted for quite some time too. I can only assume your accident stirred some extremely ugly memories inside her."
ta "I cannot speak from personal experience regarding what it's like. The people who've had one themselves described it to me as the most frightening experience of their life."
ta "Some compared it to a heart attack of some kind."
ta "Chest pain, difficulty breathing, flashing vision and sometimes the sensation of dying."
ta "I think, Mister Nakai, you may be one of the few people in school who can somewhat relate to what Miss Ikezawa must have been going through. Try to recall your own experience, except more prolonged and without passing out."
"I let out a dejected sigh."
hi "That bad? No wonder she broke up with me."

show takawa serious
with chchange

"The old woman raises a curious eyebrow at that news, but doesn't seem overly shocked."
ta "Did she break up with you?"
hi "…I phoned her last Tuesday and she said she couldn't be my girlfriend anymore. Then she hung up. But she seems to be serious about it."
ta "I see. And how about you, Mister Nakai? Are you planning to break up with her?"
hi "Huh?"

show takawa smile
with chchange

ta "Because if you're not, you could perhaps try to change her mind."
hi "What am I supposed to say? Ask someone who lost her parents in such a tragic manner to put up with someone who might die on her at any moment?"
ta "Why not? She has known about your condition all along, hasn't she? And it hasn't stopped her from pursuing a relationship with you before."
ta "You could remind her that you're still here. Nothing permanent was lost."
hi "Nothing except all the progress she has made since we met."
hi "Before that heart attack ruined things, she was organizing stuff, joining a club, going on dates, trying new things… and now she seems to be back to hiding away in her room and avoiding everyone and everything."
hi "If she had been with someone who wasn't suffering from this condition, maybe she could have…"

play sound sfx_teacup_loudclink

show takawa stern
with chchangefast

ta "AHEM!"
"For a moment I'm startled by the sound of Miss Takawa loudly scraping her throat and setting down her tea cup with a loud cling."
"As I look upon her face, I can tell she's glaring knives at me, though I'm not sure why."
ta "Maybe she could have a chance to recover fully is what you were going to say, Mister Nakai?"
hi "Ummm… Well…"
ta "Did you really believe that a few months of dating you was all it would take for Miss Ikezawa's trauma to disappear just like that? Or a few months of dating anybody for that matter?"
ta "Were you counting on that when you started going out with her? Do you even know why I'm treating her?"
"Her voice is barely raised, yet I feel as if the sudden authoritive tone in her voice and her stern gaze are pinning me against a wall."

show takawa serious
with charachangealways

"She keeps up her gaze for a few more seconds, then softens her expression, takes another sip and reverts back to her grandmotherly tone."

show takawa calculating
with chchange

ta "Perhaps I should explain a few things."
ta "What I'd like you to understand is that what happened last Monday had nothing to do with her self-confidence, which has indeed improved a bit lately."
ta "I've worked with war veterans who were usually strong and confident men, yet they too had breakdowns in situations where their post traumatic stress was triggered."
"She pauses for a second, puts her cup on the tray and absentmindedly fiddles with her shawl for a bit."

show takawa smile
with chchange

ta "If you can manage to convince her to pick things up where you left off, you may find that much of the recent progress she has made has remained intact."
ta "It might take her a little while to sort things out, but she'll get back on her feet eventually."
ta "That's because I have found that Miss Ikezawa has a resilience that even many seemingly stronger people do not have."
"I can attest to that. She's been through hell after the fire that scarred her, but she still managed to keep going. It's one of the things I admire about her."

show takawa calculating
with chchange

ta "Finally, take note that emotional trauma takes a long time to recover from."
ta "It takes time, therapy and support. One cannot always judge this recovery process by short-term results as you've been doing. What's important is that progress is made in the long run."
ta "Many people who are recovering from trauma have relapses every now and again. It's not necessarily a problem as long as they eventually take more steps forward than backwards."
ta "It's important that you understand that about her, but it's equally important that Miss Ikezawa understands that about herself."
ta "I could help her with that, but it might good if you can remind her of that as well."
hi "Long-term thinking, huh?"

show takawa smile
with chchange

ta "That's right. Do not believe you have failed her and give up if something happens that causes her to temporarily regress."
ta "Some people can do well for years and then suddenly relapse unexpectedly. Just support her to the best of your ability until she can get back on her feet again."
ta "I do not wish to deny the good influence you've had on her. Just don't look upon yourself as a miracle worker, or even as someone whose responsibility it is to assure her recovery."
hi "I haven't really been doing a great job supporting her this week."

show takawa calculating
with chchange

ta "To the best of your ability may not be as much as you like, just like she may not always be able to support you as much as she likes."
ta "It's up to you two to decide whether you're willing to settle for the support you still {i}can{/i} give each other."
ta "Does the fact she couldn't be by your side throughout this ordeal mean she cannot do anything for you anymore?"
hi "Of course not."
ta "She might feel the same. You could ask her."
hi "You think she didn't mean it when she said she didn't want to be my girlfriend anymore?"

show takawa smile
with chchange

ta "I recall you saying she said something different."
hi "It comes down to the same thing, doesn't it?"
ta "I don't believe it does, but that's up to you to find out for sure."

show lilly basic_oops at twoleft_sittingpos
show takawa calculating at tworight_sittingpos
with charaenter

"My gaze wanders between Lilly and Miss Takawa who both have an expectant expression on their face."
"Are they expecting me to take action right here and now?"
"I take a deep breath."
hi "I guess I could reach out to her like you're suggesting."

show takawa smile
with chchange

"I turn to the old lady who's doing her best to give me the most encouraging look she can muster."
hi "I don't suppose you have any helpful tips? You're the expert here."

hide lilly
show takawa at sittingpos
with charaenter

ta "I'm afraid I have to disappoint you there. Relationship therapy isn't my field. The real expert in the room would be you, Mister Nakai."
hi "Me?"

show takawa happy
with chchange

ta "Certainly. When it comes to winning Miss Ikezawa's heart, you're the world's leading expert."
ta "You are aware of the fact that you are her first boyfriend, aren't you? I think you'll do fine."

show takawa smile
with chchange

ta "Just be as sincere to her as you were to me when you told me why you liked her so much."
hi "You still remember that?"
ta "I was hoping that you'd be able to remember it as well during the times when your relationship with her is being tested."
"I remember it alright. And between then and now I've found several additional reasons to be attached to Hanako."
"The problem isn't the fact I wouldn't like her anymore. The issue is the fact that I hurt her and scared her off even though it wasn't something I did on purpose."
"But Miss Takawa has a point as well. Hanako knew of my heart condition all along and yet she allowed herself to get close to me."
"I have to talk to her."

show takawa at center
with charamove

"As I reach for the phone and pick up the receiver, Miss Takawa gets up from her chair."
ta "Would you like Miss Satou and me to excuse ourselves?"
hi "It's fine. I'm not really expecting her to pick up."

hide takawa
with charaexit

play sound sfx_phonedial volume 0.7

"I dial Hanako's number and wait, my heart racing."
"One look at Lilly tells me she's probably as tense as I am."
"After hearing the tone several times, the short beep of her voicemail sounds."
"Looks like Hanako has her phone turned on, but simply won't pick up."
"That's fine though. I think I know what I want to say."
hi "…Hanako? It's me."
hi "I don't think that this is a situation either of us wants."
hi "I'm not angry with you. I… just want to pick up where we left off, if possible."
hi "I'll be back at Yamaku around noon tomorrow. If you could… wait for me at the gate to… welcome me back… that'd make me really happy."
hi "I hope to see you tomorrow. Bye…"
"I hang up, still feeling apprehensive."
"No turning back now. The rest is up to Hanako. I can only hope she'll bother to listen to her voicemail."

show takawa happy at tworight_sittingpos
show lilly basic_smileclosed at twoleft_sittingpos
with charaenter

stop music fadeout 2.0

"As my attention shifts back to my two visitors, I am greeted by two smiling faces."

play music music_comfort fadein 4.0

ta "My, my… That certainly would have won me over if I were forty years younger."

show lilly basic_smile
with chchange

li "Hisao… I'm sure she'll be there tomorrow."
li "I know she still loves you. Please try not to worry too much about this."
"Looks like Lilly's maternal instincts are resurfacing. Somehow this is the most reassuring thing I've seen all week."

show takawa smile
with chchange

ta "If it is alright with you, I'll be taking my leave, Mister Nakai. I'm sure you'll need all the rest you can get."
ta "After that message you really can't afford the doctors to keep you here, now can you?"
hi "Thanks for the advice, Miss Takawa. I'm sure you'll find out soon whether things worked out or not."
ta "I'd appreciate it if you could keep me informed, Mister Nakai."
ta "If you manage to reconcile with Miss Ikezawa, I may have a small gift for her that I'd like to present to you. Nothing serious, just something I just thought of."
hi "You're making me curious."
ta "All the more reason to try and sort things out as soon as you can, isn't it?"

show takawa at tworight
with charamove

"Miss Takawa takes the tray, puts our empty cups on top of it and then turns to Lilly."
ta "Miss Satou, I can drop you off at school if you wish. It's only a small detour for me and visiting hours are probably about to end."

show lilly at twoleft
with charamove
show lilly cane_smileclosed
with chchange

"Lilly gets up, makes a polite bow at the old woman and smiles."
li "May I have the pleasure of treating you to a cup of tea first, Miss Takawa?"

show takawa happy
with chchange

ta "I humbly accept. Please lead the way, Miss Satou."

hide takawa
hide lilly
with charaexit

"As Lilly and Miss Takawa say their goodbyes and leave the room, I can't help but think that these two would probably get along pretty well."

stop music fadeout 2.0

scene bg school_nursehall
with Fade(1.0, 1.0, 1.0)

"Only thirty more minutes."

nvl clear
nvl show dissolve

n "I pace around the hallway restlessly."
n "{vspace=60}After finishing breakfast this morning, the doctor came by, performed a few minor check-ups and informed me that we'd be having a short meeting in his office at twelve o' clock and that I was free to go back to Yamaku afterwards."
n "At least I don't need to stay here any longer."

nvl clear

n "I wonder if Hanako has even listened to my message."
n "Is she going to come out of her room today?"
n "What the hell am I supposed to tell her?"
n "I've packed my things, brushed my teeth, took a shower and checked the bus schedule at least five times."
n "Isn't this talk just a formality?"
n "Why couldn't he just tell me what he needed to this morning and let me go back?"

nvl hide dissolve

play sound sfx_dooropen
with Pause(0.5)

dc "Nakai."
"I turn around as I hear my name and rush over to the doctor as he emerges from his office."
dc "Come in, please."

play sound sfx_doorclose

scene bg school_nurseoffice
with locationchange

play music music_pearly fadein 4.0

"I follow him into his office and sit down, but instead of giving me the expected “be careful in the future”-talk, the doctor merely stands there and checks his watch."
"What is he waiting for?"
hi "Excuse me, aren't we ready to begin yet?"
dc "You sound like you are in a hurry."
hi "I am. Very much."
dc "I'm afraid that you'll have to hold back for a while. If you exhaust yourself at this point, you may be in for another stay here."
hi "I understand."

play sound sfx_dooropen

dc "I was merely waiting for… Ah… Good morning."
"I turn around and watch two more people enter the room."
hi "Mom? Dad?"
"I just sit there with my mouth open. I don't recall them saying they'd be here to pick me up when they visited two days ago."
dad "Hello, son. We're not late, are we?"
dc "No, you're just in time. I've only called in your son a minute ago."
dad "I apologize. We live rather far away from here."
"My parents sit down next to me, and the doctor starts off with the predictable talk."
"That collision could have ended a lot worse than it did. I was lucky an ambulance was nearby. Of course I am warned to be more careful in the future."
"It turns out this hospital has a special arrangement with Yamaku. The ambulance personnel got instant access to my medical history by scanning in my student ID. Good thing I was carrying it and I was still wearing my school uniform."
"At least I get praised by the doctor for keeping up with my medication and improving my physical condition. It's probably the reason I didn't need heavier surgery."
"I'll have to take it easy for a little while, but I'll be allowed to start engaging in light exercise in a few days."
"I'll be put on some additional medication for a while. The nurse has been informed and will take it from here on out."
"My parents visited me shortly after my surgery, but I was still recovering from the narcosis at that time and wasn't even aware of their presence."
"They came by again two days ago. Apparently they talked to the doctor afterwards, and he timed this meeting so they could make it here."
"I wish they had let me in on this."
dc "Take care, Mister Nakai. And good luck with school."
hi "Ah? Oh, thank you."

play sound sfx_dooropen

scene bg school_nursehall
with locationchange

"As we leave the doctor's office, my father addresses me."
dad "We were expecting you to be a little bit more pleasantly surprised. We had to get up pretty early to make it here in time."
hi "Sorry, I really do appreciate you coming here."
dad "You were so tired two days ago we haven't really been able to talk much."
"I was partially pretending to be more tired than I really was. That may have been rude, but I was too distracted by the matter with Hanako to be very sociable with them, and I didn't want them to worry even more about me."
dad "Hopefully we can catch up a bit in the upcoming days. We barely know what's going on in your life anymore."
hi "Huh? I don't understand."
dad "We were planning to take you with us and let you rest at home for a few days."

stop music fadeout 1.0

"WHAT? NO!"

scene bg school_dormext_full
with locationskip

play music music_pearly fadein 2.0

mom "I'm sorry, Hisao. We had no idea one of your friends was going to move away in the upcoming days. You should have let us know."
hi "It's… okay, Mom."
"We've arrived at the grounds of Yamaku and are now wandering along the path to the boys' dormitories."
dad "I was already surprised. At first you hated the idea of going here, and now you just couldn't wait to get back."
hi "I guess I found my place here, Dad."
dad "You sure did. What's in that plastic bag you're carrying with you?"
hi "Ah, nothing important."
"As we reach the dorm entrance, we're greeted by an ear-shattering “HICCHAN! WELCOME BACK!” that could only originate from one person in Japan."

show misha hips_grin:
    xalign 0.5 xpos 0.75
show shizu basic_happy at center
show lilly basic_cheerful:
    xalign 0.5 xpos 0.25
with charaenter

"In front of the dorm are Shizune, Misha and Lilly. Shizune cheerfully makes a small saluting gesture, Misha excitedly jumps up and down and Lilly calmly stands next to them."
mom "Are these your friends, Hicchan?"
mi "Are these your parents, Hicchan?"
hi "Erm… Mom, Dad. These are indeed my friends."
hi "The person in the middle is Shizune Hakamichi, our class representative and student council president."
hi "The one on the right is Shiina Mikado, my neighbor in class. We usually just call her Misha."
hi "The girl on the left is Lilly Satou who attends the class next to ours and often shares lunch with me."

show misha perky_smile
show shizu behind_smile
show lilly basic_smileclosed
with charachangealways

"Shizune, Misha and Lilly make polite bows towards my parents, Lilly's slightly more graceful and Misha's slightly more energetic than the rest."

show lilly basic_smile
with chchange

li "I'm sorry, Hisao. I tried to get your neighbor Kenji to join us as well, but he seemed preoccupied and wouldn't come out of his room."
hi "That's okay, Lilly."

show misha sign_confused
with chchange

mi "Hey Hicchan. Maybe I missed something here, but… why isn't Hanako with you?"

stop music fadeout 1.0

"The fake smile I have been wearing since we reached Yamaku is wiped off my face in an instant."
hi "I… haven't seen Hanako anywhere, Misha."

show misha cross_frown
show shizu basic_angry
show lilly basic_reminisce
with chchange

mi "WHAT???"

scene black
with Dissolve(2.0)

return