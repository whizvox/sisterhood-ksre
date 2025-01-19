label sisterhood_ch3:
label .sh_ch3:

$ set_window_tint(TINT_HISAO)

call sisterhood_timeskip

scene bg school_nurseoffice
show nurse concern_close
with Dissolve(2.0)

play music music_nurse fadein 4.0

"After listening for a moment, the nurse puts away his stethoscope and gives a satisfied nod to indicate I can put my shirt back on."
nk "You sound good to me. No chest pains or dizziness this morning?"
"I shake my head."
"I've been doing these morning jogs for several days now, and so far my heart hasn't acted up a single time despite the exhaustion I feel at the end of each practice session."
nk "And what do you think of the coach I assigned you?"
hi "When I got overconfident and tried to keep up with her yesterday morning, she immediately started yelling at me to stick to my schedule."
hi "She can be pretty intimidating despite her short stature."

show nurse grin_close
with chchange

"The nurse laughs at this."
nk "Is that a compliment?"
hi "I can't really complain about her. She can be harsh, but fair and pretty fun to chat with. Why are you so interested?"
"As I finish putting my shirt back on, the nurse leans in and speaks in a conspiring tone."

show nurse concern_close
with chchange

nk "The reason I asked her to get this involved with your practice sessions is because I want to know how open she is to the idea of using her athletic experience to help others."
nk "Running has always been a solitary thing for her, so it would be good if she took a liking to this whole coaching gig, as informal as it is."
hi "Are you hoping she'll want to turn it into a career?"

show nurse neutral_close
with chchange

nk "Graduation is less than a year away, and Emi doesn't have any clear plans on what to do afterwards."
nk "She kind of likes to live by the day. She's not exactly a bookworm if you know what I mean. But sports are something she's genuinely passionate about."
"You don't have to tell me that."
hi "Are you trying to talk her into becoming a trainer or a coach? Aren't those usually retired athletes?"
nk "More like a P.E. teacher. She might make a lively colleague, don't you think?"

play sound sfx_snap

show nurse grin_close
with Dissolve(0.2)

"The nurse suddenly looks pensive and snaps his fingers with a guilty look on his face."
nk "Speaking of which… that reminds me. A colleague of mine has been asking me about you and wanted to meet you."
nk "Do you have some time to spare later this day?"
hi "I have obligations today, but that's early in the evening. I could manage right after the last class. But what is this about?"
"Today is a special day as Lilly called us from Scotland a few days ago, saying she and Akira would be flying in today, and Hanako and I are planning to welcome them back."
"But I'm pretty curious why someone on Yamaku's staff would call on the nurse to arrange a meeting."
"I don't recall getting particularly bad marks lately, and even if that were the case, a teacher would be more likely to approach Mutou or Shizune in order to get in touch with me."

show nurse neutral_close
with chchange

nk "Just an informal chat, I've been told. If you could drop by after your last class ends, that'd be great."
"That isn't a satisfying answer at all, but I still need to get back to the dorms and take a shower before class, so I leave the office without prying any further."

stop music fadeout 1.0

scene bg school_nursehall
with shorttimeskip

play music music_soothing fadein 2.0

"After class, I reach the corridor leading to the nurse's office."

show nurse neutral
with charaenter

"I can see he's already waiting for me outside. He greets me with his usual fox-like smile."
nk "Good to see you could come so quickly. This way please."

hide nurse
with charaexit

scene bg school_staircase1
with Dissolve(1.0)

"He leads me through a few hallways and up two sets of stairs to a part of the staff building I've never been to before."

play sound sfx_doorknock2

"He stops at a door at the end of one of the hallways and knocks loudly before opening it and making an inviting gesture like a porter beckoning a guest."
nk "After you."

play sound sfx_dooropen

scene bg school_therapist
with Dissolve(2.0)

"I expected to see just another office on the other side of the door. Maybe a variation of the nurse's home turf. But the room I step into fits neither a medical staff building nor a school."
"The best way to describe it would be a rather old-fashioned living room filled with nothing but wooden furniture and curtains in a style similar to ones my grandparents used to own."
"The only piece of technology in plain sight is the phone on a small table in one of the corners."

show nurse neutral_close at left
show takawa smile at tworight
with charaenter

"As much out of place as the room feels in the building we're in, I have to admit it fits its sole occupant like a glove."

"The nurse seems amused by my surprised reaction and puts his hand on my shoulder in an overly personal fashion."
nk "I feel that over the last few days we've grown close enough to each other for me to introduce you to my mother."

show takawa stern
with chchange

"Before I can fully digest his extremely out-of-place joke, the old lady behind the table rises to her feet and approaches us while shooting the nurse a stern glare."
ta_ "If I was truly your mother, dear colleague, I would have taught you how impolite it is to make these kinds of remarks before even introducing us properly."

show nurse grin_close
with chchange

"The nurse acknowledges her words with a cheerful nod and a slightly apologetic gesture."
nk "This young man next to me is Hisao Nakai, whom I'm certain you've heard plenty about by now. My colleague here who wanted to meet you is called Miss Takawa."

show takawa smile
with chchange

ta "Yumi Takawa. I'm very pleased to make your acquaintance, Mister Nakai."
"The old woman in front of us makes a graceful bow as the nurse continues."

show nurse neutral_close
with chchange

nk "Here at Yamaku, our primary focus is to help students deal with the physical implications of their conditions."
nk "But in certain cases where a student's condition is the result of an accident of some sort, some additional support can be desired, and if I feel their circumstances warrant it, I usually refer them to Miss Takawa here or one of her co-workers."
nk "Eventually the final decision lies with the students, but most of them accept the additional help we offer them here."
"I notice how his smile shortly fades for a moment during the last part of his statement, but before I can ponder on whether he had some specific people in mind, his jovial expression returns, and he reaches for the door handle."

show nurse grin_close
with chchange

nk "I'm sure the two of you will do fine without me. I'll be going now. See you after your next practice run."

hide nurse
with charaexit

play sound sfx_doorclose

show takawa calculating
with charachangealways

ta "You'll have to excuse my colleague. He is a fine young man, but I believe he enjoys his own jokes a little bit too much sometimes."

stop music fadeout 2.0

"She makes an inviting gesture over to the table in the middle of the room."

hide takawa
show takawa smile_close at sittingpos
with charaenter

queue music music_another fadein 4.0

ta "May I have the honor of getting you some green tea, Mister Nakai?"
hi "Uh… sure. I mean… please."
"I take a seat at the low table in the middle of the room as my host walks over to a corner and fills two ornate tea bowls with the contents of a kettle boiling on a small brazier there."
"After returning to the table and putting one of the bowls in my hands, she sits down across from me and gives a small bow to indicate it's okay to drink."
"As I drink, I am reminded of the many lunch breaks I've spent in the tea room with Hanako and Lilly."
"This room seems to have the same relaxing atmosphere, maybe even more so, and the grandmotherly feeling that the old woman in front of me is giving off reminds me slightly of Lilly's composed demeanor."
"But unlike Lilly's unfocused and cloudy gaze, Miss Takawa's gaze is sharp and analytical."

show takawa calculating_close
with charachangealways

ta "If I may ask, Mister Nakai… Did my colleague tell you why I wanted to meet you?"
hi "No, not really. All he said was that it was informal."
ta "Correct. I have no reason to believe you yourself are in need of my services."
"Services? The nurse said that this Miss Takawa gives \"additional support\" after accidents. Did he mean psychiatric help? Is this old lady a shrink?"
"Suddenly, a realization dawns on me."
hi "You're a counselor, aren't you? Are you by any chance Hanako's therapist?"

show takawa happy_close
with chchange

#"The old lady gives an appreciative smile at my deduction."
ta "Well reasoned, Mister Nakai. My specialty is cognitive behavioral therapy, and Miss Ikezawa does indeed happen to be one of my clients."
"I have to admit I have wondered about the person Hanako was seeing ever since Lilly first brought up the subject, but this old lady was not what I was expecting a therapist to look like at all."
hi "Sorry for the reaction. I've always thought of therapists as bearded guys with thick glasses."

show takawa smile_close
with chchange

"Miss Takawa covers her mouth with her hand and chuckles briefly. I doubt this was the first time she heard about that stereotype."
ta "Plenty of those exist around here as well."
hi "So I guess this is about my relationship with Hanako?"

show takawa serious_close
with chchange

ta "You've come up with increasing frequency in recent sessions. When Miss Ikezawa started referring to you as her boyfriend, I felt it might be a good idea to meet you myself and create my own impression of you."

show takawa smile_close
with chchange

#"She smiles playfully."
ta "Miss Ikezawa is presumably expecting me to say something positive about you during the next session, so it would probably pay off for you to be on your best behavior here."
hi "Does Hanako know you're having this talk with me?"

show takawa serious_close
with chchange

ta "If she hadn't consented to this, you would not be sitting here right now."
hi "So what exactly are you expecting of me?"

show takawa calculating_close
with charachangealways

ta "I merely wish to get a general impression of you. Would you be willing to tell me a few things about how your relationship with Miss Ikezawa came to be from your perspective?"
"There are plenty of things and events that took place regarding our relationship that I don't care to talk about with this person, especially since I don't know what Hanako has told her."
"So I just end up describing a few moments I've had with Hanako to her: like our first meeting in the library, our first game of chess during the festival and our various outings in the city."
"As I relay these events, Miss Takawa listens to me without saying a single word."

show takawa smile_close
with chchange

ta "Thank you for your account of these events, Mister Nakai. I very much appreciate your time."
hi "I suppose you aren't willing to tell me a few things in return? Or is that all covered under patient confidentiality?"
"I don't have high hopes for any attempts to learn more about Hanako from a therapist, especially since the nurse was already so tight-lipped about it. But for some reason, it seems unfair for me to be the only one giving out information."

show takawa calculating_close
with chchange

ta "Client confidentiality, Mister Nakai. And I'm afraid that I'm indeed not at liberty to tell you anything that was confided in me during closed sessions."
ta "All I can tell you is that I'm content with Miss Ikezawa's progress so far."
"I can't resist a frown at that statement."
"If the nurse was correct, Hanako must have been in therapy at Yamaku since she came here two and a half years ago. But when I first met her, she was still too skittish to even hold a conversation with me."
"Was Hanako even worse when she first came here, or is this therapist exaggerating the progress that was made?"
"Of course, there was also a third possibility."
hi "May I ask for how long you've been treating Hanako? Are you the only person who's been treating her?"
ta "I'm very sorry, but I'm afraid I cannot disclose information of that kind to you."
hi "Can I ask you something that won't force you to violate your client confidentiality?"
ta "By all means."
hi "For how long have you worked here at Yamaku?"

show takawa serious_close
with charachangealways
with Pause(0.5)
show takawa smile_close
with charachangealways

"Miss Takawa raises her eyebrows for a second and then smiles."
ta "Very well played, Mister Nakai. I have only worked here for a little over a year."
"That means Hanako must have been meeting with at least one previous therapist in the past to whom she presumably didn't open up."
"Somehow I'm not really that surprised. I am still a bit skeptical about Miss Takawa's claim of the therapy's effectiveness, though."
"Was it just a coincidence Hanako started opening up more when I befriended her? I don't think so."

show takawa calculating_close
with chchange

"Miss Takawa seems to read my thoughts."
ta "Am I correct in my assumption that you don't seem to believe me?"
hi "I haven't known Hanako for as long as you have, but considering how she's grown over the last period, I feel that instead of therapy, maybe all Hanako really needed were friends."
"I prepare myself for an offended reaction, but Miss Takawa doesn't seem fazed."
ta "I don't believe that the two are mutually exclusive. In fact, I believe Miss Ikezawa benefits most from having both."
"I don't really think there's a point in arguing that sort of thing with her."
"After taking another sip of her tea, she gives me another one of those analytical stares."
ta "Mister Nakai, I won't take up much more of your time. I already appreciate you coming here. Would you be adverse to one more question?"
hi "Go ahead."

show takawa serious_close
with chchange

ta "What is it that drew you to Miss Ikezawa? Why is it that you are attracted to her?"
"That's kind of a personal question. Fortunately, it's something I've often thought over myself, so I don't have difficulty coming up with an answer."
hi "Multiple things, I guess. We both enjoy reading and playing games. We both like spending time away from the bustle of the rest of the world."
hi "She's also a really sweet girl and once you get used to the scars, she's actually pretty attractive, too."
hi "Also… I can't really describe it very well but I feel some kind of kinship with her. Like she's a kindred spirit. It's hard to explain."
hi "We figured we could both use support from someone and we made a promise to be that someone for each other during tough times."

show takawa happy_close
with chchange

"My answer seems to satisfy her as she nods appreciatively."
ta "You didn't even need to think before answering. Very good."

show takawa smile_close
with chchange

ta "I have no further questions for you, Mister Nakai. You can take your leave if you wish."
hi "Then I'll be going now. Hanako and I are planning to welcome Lilly back this evening."

show takawa at center
with charamove
show takawa at left
with charamove

"She rises as well and walks me to the door before giving a polite bow as a farewell."
ta "I hope Miss Satou has had a pleasant trip abroad. Take care of yourself, Mister Nakai."

hide takawa
with charaexit

"After a polite greeting, I leave the secluded “office” and hurry back to the exit of the staff building."
"There are still plenty of things to do before tonight."

stop music fadeout 2.0
scene black
with Dissolve(2.0)

return