label sisterhood_ch5:
label .sh_ch5:

$ set_window_tint(TINT_HISAO)

call sisterhood_timeskip

scene bg hok_field_ni
with Dissolve(3.0)

play music music_serene fadein 1.0
play ambient sfx_crickets loop

"I lift my arm, hold my watch in front of my face and press a button on the side, causing the display to light up."
"I hear the soft voice of my girlfriend who's lying on the ground to my left."
ha "Hisao, what time is it?"
hi "It's nearly half past ten."
ha "Do you think we should head back?"
hi "Not yet. Lilly probably hasn't finished her book yet."
"A momentary silence."
"Silences around Hanako are sometimes uncomfortable, but right now they feel alright due to how relaxing our surroundings are."
hi "Hanako?"
ha "Yes?"
hi "How many romance stories do you think have a chapter where a couple is lying in an open field gazing at the stars?"
"I hear an amused giggle from Hanako."
ha "I…I could name at least nine."
"I suppose that would make us number ten."

play sound sfx_whiteout
scene ev wheatfield_smile:
    xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 zoom 1.1
    ease 5.0 zoom 1.0
with whiteout
with Pause(4.0)

show firefly_v1:
    anchor (0.5,0.5) pos (0.15,0.45)
    block:
        ease 18.17 pos (0.15,0.45) knot (0.1,0.3) knot (0.04,0.29) knot (0.22,0.21) knot (0.17,0.29) knot (0.18,0.21) knot (0.21,0.28)
        ease 14.78 pos (0.21,0.28) knot (0.07,0.14) knot (0.12,0.33) knot (0.15,0.26) knot (0.11,0.21) knot (0.22,0.21) knot (0.24,0.08)
        ease 13.54 pos (0.24,0.08) knot (0.25,0.2) knot (0.13,0.06) knot (0.22,0.15) knot (0.36,0.12) knot (0.27,0.12) knot (0.16,0.05)
        ease 14.75 pos (0.16,0.05) knot (0.03,0.04) knot (0.12,0.18) knot (0.1,0.11) knot (0.23,0.16) knot (0.25,0.25) knot (0.14,0.15)
        ease 17.99 pos (0.14,0.15) knot (0.05,0.11) knot (0.12,0.11) knot (0.16,0.23) knot (0.15,0.15) knot (0.0,0.28) knot (0.06,0.1)
        ease 12.38 pos (0.06,0.1) knot (0.09,0.19) knot (0.14,0.23) knot (0.1,0.17) knot (0.28,0.25) knot (0.17,0.33) knot (0.07,0.34)
        ease 15.63 pos (0.07,0.34) knot (0.12,0.47) knot (0.12,0.54) knot (0.14,0.65) knot (0.27,0.59) knot (0.38,0.58) knot (0.37,0.74)
        ease 13.52 pos (0.37,0.74) knot (0.48,0.73) knot (0.47,0.82) knot (0.6,0.82) knot (0.61,0.87) knot (0.69,0.91) knot (0.6,0.8)
        ease 18.83 pos (0.6,0.8) knot (0.64,0.71) knot (0.59,0.61) knot (0.58,0.53) knot (0.63,0.52) knot (0.56,0.45) knot (0.58,0.38)
        ease 19.13 pos (0.58,0.38) knot (0.74,0.39) knot (0.7,0.27) knot (0.75,0.36) knot (0.67,0.39) knot (0.77,0.54) knot (0.68,0.51)
        repeat

show firefly_v2:
    anchor (0.5,0.5) pos (0.63,0.63)
    block:
        ease 13.09 pos (0.63,0.63) knot (0.51,0.56) knot (0.58,0.62) knot (0.67,0.52) knot (0.69,0.63) knot (0.54,0.67) knot (0.58,0.62)
        ease 12.37 pos (0.58,0.62) knot (0.53,0.64) knot (0.56,0.69) knot (0.69,0.77) knot (0.8,0.85) knot (0.87,0.83) knot (0.88,0.69)
        ease 13.36 pos (0.88,0.69) knot (0.74,0.82) knot (0.88,0.93) knot (0.92,0.87) knot (1.0,0.82) knot (0.99,0.66) knot (0.95,0.7)
        ease 12.11 pos (0.95,0.7) knot (0.82,0.7) knot (0.92,0.8) knot (0.84,0.79) knot (0.93,0.68) knot (0.91,0.63) knot (0.83,0.59)
        ease 19.89 pos (0.83,0.59) knot (0.91,0.6) knot (0.96,0.55) knot (0.93,0.64) knot (0.95,0.5) knot (0.97,0.58) knot (0.92,0.48)
        ease 18.05 pos (0.92,0.48) knot (1.0,0.62) knot (0.81,0.57) knot (0.93,0.57) knot (0.84,0.62) knot (0.87,0.7) knot (0.86,0.78)
        ease 14.35 pos (0.86,0.78) knot (0.85,0.83) knot (0.92,0.97) knot (0.81,0.95) knot (0.99,0.98) knot (0.84,0.9) knot (0.84,0.8)
        ease 18.19 pos (0.84,0.8) knot (0.77,0.75) knot (0.71,0.75) knot (0.72,0.81) knot (0.85,0.87) knot (0.93,0.72) knot (0.97,0.91)
        ease 14.68 pos (0.97,0.91) knot (0.92,0.78) knot (0.77,0.8) knot (0.89,0.7) knot (0.71,0.69) knot (0.7,0.59) knot (0.81,0.57)
        ease 12.32 pos (0.81,0.57) knot (0.66,0.54) knot (0.63,0.48) knot (0.67,0.34) knot (0.79,0.31) knot (0.76,0.48) knot (0.59,0.42)
        repeat

show firefly_v3:
    anchor (0.5,0.5) pos (0.04,0.68)
    block:
        ease 19.28 pos (0.04,0.68) knot (0.07,0.74) knot (0.19,0.73) knot (0.04,0.85) knot (0.1,0.97) knot (0.19,0.83) knot (0.19,0.68)
        ease 15.6 pos (0.19,0.68) knot (0.24,0.67) knot (0.13,0.72) knot (0.11,0.63) knot (0.15,0.74) knot (0.07,0.64) knot (0.15,0.56)
        ease 13.64 pos (0.15,0.56) knot (0.08,0.47) knot (0.19,0.49) knot (0.3,0.58) knot (0.44,0.49) knot (0.5,0.47) knot (0.59,0.33)
        ease 13.92 pos (0.59,0.33) knot (0.51,0.35) knot (0.47,0.47) knot (0.38,0.54) knot (0.35,0.39) knot (0.45,0.48) knot (0.46,0.42)
        ease 17.98 pos (0.46,0.42) knot (0.57,0.44) knot (0.53,0.48) knot (0.67,0.54) knot (0.65,0.67) knot (0.73,0.79) knot (0.88,0.73)
        ease 14.93 pos (0.88,0.73) knot (0.98,0.7) knot (0.96,0.81) knot (0.92,0.94) knot (0.81,0.81) knot (0.78,0.67) knot (0.68,0.73)
        ease 19.85 pos (0.68,0.73) knot (0.51,0.74) knot (0.48,0.78) knot (0.38,0.86) knot (0.32,0.9) knot (0.35,0.95) knot (0.31,0.83)
        ease 18.53 pos (0.31,0.83) knot (0.42,0.71) knot (0.47,0.53) knot (0.62,0.44) knot (0.7,0.38) knot (0.88,0.37) knot (0.95,0.21)
        ease 17.97 pos (0.95,0.21) knot (0.84,0.15) knot (0.92,0.11) knot (0.91,0.19) knot (0.87,0.29) knot (0.79,0.29) knot (0.79,0.36)
        ease 15.77 pos (0.79,0.36) knot (0.85,0.44) knot (0.92,0.57) knot (0.86,0.51) knot (0.95,0.51) knot (0.82,0.46) knot (0.74,0.41)
        repeat

show firefly_v4:
    anchor (0.5,0.5) pos (0.79,0.62)
    block:
        ease 16.49 pos (0.79,0.62) knot (0.7,0.63) knot (0.56,0.72) knot (0.52,0.53) knot (0.49,0.33) knot (0.44,0.41) knot (0.56,0.41)
        ease 16.64 pos (0.56,0.41) knot (0.6,0.36) knot (0.69,0.44) knot (0.71,0.5) knot (0.68,0.37) knot (0.54,0.41) knot (0.5,0.51)
        ease 14.68 pos (0.5,0.51) knot (0.43,0.42) knot (0.31,0.36) knot (0.26,0.33) knot (0.3,0.15) knot (0.44,0.22) knot (0.3,0.15)
        ease 12.13 pos (0.3,0.15) knot (0.43,0.18) knot (0.36,0.16) knot (0.37,0.09) knot (0.34,0.23) knot (0.5,0.25) knot (0.52,0.3)
        ease 18.08 pos (0.52,0.3) knot (0.66,0.36) knot (0.79,0.33) knot (0.63,0.28) knot (0.62,0.15) knot (0.81,0.21) knot (0.79,0.09)
        ease 17.34 pos (0.79,0.09) knot (0.79,0.18) knot (0.9,0.21) knot (0.84,0.18) knot (0.88,0.28) knot (0.98,0.44) knot (0.89,0.4)
        ease 12.57 pos (0.89,0.4) knot (0.85,0.35) knot (0.75,0.53) knot (0.83,0.39) knot (0.7,0.32) knot (0.7,0.13) knot (0.85,0.24)
        ease 19.81 pos (0.85,0.24) knot (0.76,0.19) knot (0.86,0.22) knot (0.73,0.14) knot (0.79,0.06) knot (0.74,0.04) knot (0.56,0.08)
        ease 12.93 pos (0.56,0.08) knot (0.71,0.11) knot (0.56,0.05) knot (0.64,0.2) knot (0.71,0.22) knot (0.62,0.18) knot (0.69,0.12)
        ease 15.93 pos (0.69,0.12) knot (0.76,0.28) knot (0.66,0.4) knot (0.65,0.28) knot (0.79,0.41) knot (0.96,0.45) knot (0.85,0.49)
        repeat

show firefly_v5:
    anchor (0.5,0.5) pos (0.59,0.68)
    block:
        ease 17.42 pos (0.59,0.68) knot (0.69,0.72) knot (0.76,0.9) knot (0.57,0.85) knot (0.6,1.0) knot (0.5,0.99) knot (0.6,0.91)
        ease 16.14 pos (0.6,0.91) knot (0.68,0.88) knot (0.73,0.9) knot (0.67,0.8) knot (0.78,0.72) knot (0.76,0.87) knot (0.62,0.92)
        ease 13.58 pos (0.62,0.92) knot (0.79,0.99) knot (0.83,0.93) knot (0.8,0.82) knot (0.9,0.68) knot (0.99,0.51) knot (0.94,0.46)
        ease 19.16 pos (0.94,0.46) knot (0.8,0.52) knot (0.76,0.67) knot (0.81,0.65) knot (0.68,0.76) knot (0.72,0.86) knot (0.78,0.73)
        ease 14.1 pos (0.78,0.73) knot (0.7,0.79) knot (0.5,0.78) knot (0.5,0.88) knot (0.59,0.8) knot (0.48,0.66) knot (0.55,0.7)
        ease 13.14 pos (0.55,0.7) knot (0.57,0.76) knot (0.59,0.94) knot (0.71,0.85) knot (0.55,0.84) knot (0.64,0.81) knot (0.63,0.74)
        ease 15.05 pos (0.63,0.74) knot (0.49,0.72) knot (0.52,0.83) knot (0.57,0.92) knot (0.6,0.84) knot (0.53,0.96) knot (0.43,0.99)
        ease 15.32 pos (0.43,0.99) knot (0.54,0.86) knot (0.54,0.74) knot (0.61,0.73) knot (0.78,0.78) knot (0.66,0.75) knot (0.5,0.73)
        ease 17.3 pos (0.5,0.73) knot (0.49,0.61) knot (0.53,0.46) knot (0.61,0.32) knot (0.69,0.4) knot (0.62,0.26) knot (0.49,0.31)
        ease 19.08 pos (0.49,0.31) knot (0.5,0.4) knot (0.48,0.47) knot (0.37,0.39) knot (0.5,0.38) knot (0.5,0.44) knot (0.44,0.4)
        repeat

show firefly_v6:
    anchor (0.5,0.5) pos (0.13,0.46)
    block:
        ease 18.49 pos (0.13,0.46) knot (0.11,0.55) knot (0.29,0.61) knot (0.33,0.49) knot (0.5,0.58) knot (0.38,0.48) knot (0.31,0.37)
        ease 15.28 pos (0.31,0.37) knot (0.32,0.3) knot (0.3,0.44) knot (0.18,0.47) knot (0.12,0.44) knot (0.14,0.49) knot (0.07,0.36)
        ease 12.16 pos (0.07,0.36) knot (0.1,0.45) knot (0.15,0.3) knot (0.2,0.41) knot (0.05,0.33) knot (0.08,0.4) knot (0.1,0.25)
        ease 14.44 pos (0.1,0.25) knot (0.1,0.36) knot (0.24,0.39) knot (0.26,0.31) knot (0.39,0.19) knot (0.54,0.25) knot (0.57,0.11)
        ease 13.81 pos (0.57,0.11) knot (0.38,0.14) knot (0.23,0.02) knot (0.31,0.12) knot (0.34,0.21) knot (0.45,0.28) knot (0.48,0.08)
        ease 18.06 pos (0.48,0.08) knot (0.49,0.22) knot (0.62,0.14) knot (0.5,0.25) knot (0.58,0.17) knot (0.6,0.27) knot (0.59,0.19)
        ease 13.69 pos (0.59,0.19) knot (0.64,0.18) knot (0.78,0.28) knot (0.68,0.13) knot (0.75,0.09) knot (0.74,0.0) knot (0.84,0.02)
        ease 14.04 pos (0.84,0.02) knot (0.9,0.02) knot (0.82,0.15) knot (0.77,0.13) knot (0.75,0.23) knot (0.67,0.13) knot (0.62,0.14)
        ease 15.52 pos (0.62,0.14) knot (0.55,0.16) knot (0.49,0.13) knot (0.44,0.18) knot (0.4,0.22) knot (0.27,0.17) knot (0.36,0.13)
        ease 12.92 pos (0.36,0.13) knot (0.22,0.23) knot (0.24,0.42) knot (0.23,0.56) knot (0.34,0.65) knot (0.36,0.53) knot (0.33,0.66)
        repeat

"After getting up early—too early—yesterday morning we took the train to Hokkaido and arrived at the Satou summer home late in the afternoon."
"I failed to get a great deal of sleep the night before, so I spent a large part of the evening napping while Lilly and Hanako cleaned up the house and made supper. I felt a bit guilty about it, but neither seemed to mind it very much."
"The day afterwards, we walked to the nearby town which was more exhausting than I thought due to the heat. We had ice-cream to cool down once we reached our destination, and Hanako spent most of the time afterwards browsing clothes for Lilly, herself and me."
"After a filling lunch in town and more shopping, we walked back to the summer home, had a delicious dinner and then went out for an evening walk while Lilly remained behind in order to finish the book she started on the train a day ago."
"After lazily strolling through the surrounding area, we decided to take a break, and now we're lying side by side in the wheat field behind the summer home just staring at the sky."

show ev wheatfield_talk
with charachangeev

ha "Umm… Hisao?"
hi "What is it?"
ha "What do you think of our trip so far?"
"I take a moment to think."
"We haven't really been doing anything spectacular ever since we got here. Lilly's blindness, my heart condition and Hanako's difficulty with crowds rule out a lot of activities, but somehow it hasn't detracted from the experience."
"Something about our little outing feels… just right."
hi "I like it. A lot. I'm happy we got the opportunity to go here. It's nice to relax a bit after all the studying."
"Not to mention the stress related to other recent events."

show ev wheatfield_smile
with charachangeev

ha "I really like it too. I'm thinking of why I like it so much."
hi "Well?"
ha "Promise you won't laugh at me."
hi "I won't."
"Hanako hesitates for a bit and then takes a deep breath."
ha "It… feels… like…"
hi "It feels like what?"
ha "It… feels like…"
ha "I… have a family again…"
hi "A family huh?"
ha "Y-yes. A small, disabled family, but a family all the same."
"I think about Hanako's words for a bit. The atmosphere between us really has felt like that over the last two days."
"The way Hanako and Lilly looked while preparing our meals together. The way we had breakfast and dinner together."
"The way we huddled on the couch while watching television together. The way we relaxed in the back yard, reading books or playing games."
"It all felt so strangely comfortable."
hi "I think I know what you mean."
ha "You feel the same?"
hi "I think I do. I keep trying to imagine what this kind of trip would have been like with the friends I used to hang out with before I came to Yamaku, and I don't think things would have felt this… natural. This… homey."
ha "Maybe we both needed to be away from Yamaku for a while. To… you know… maybe… remember what it's like to be n-normal."

nvl clear
nvl show dissolve

n "That's a pretty good point Hanako is bringing up."
n "When passing by students from other classes, I still tend to revert to thinking of them as “that girl with the crutch” or “that guy who's missing several fingers” from time to time, and every time I catch myself, I'm reminded of my own condition."
n "On the other hand, I'm now so familiar with both Lilly and Hanako that I find it harder and harder to see their condition as something out of the ordinary. It simply has become part of who they are in my mind."

nvl clear

n "Life here has been very relaxed. Lilly's familiarity with the building has allowed her to get around without needing her cane. Having no other people in a one-mile radius has allowed Hanako to relax to the point where she's been wearing her hairclip almost constantly, and although she's still not as chatty as Emi or Misha usually is, she's calm enough to hold conversations with us without her usual stammering."
n "The only time I was reminded of my own condition was when I was forced to admit to Hanako yesterday evening that I hadn't thought about taking my medication for the day yet after she asked me about it."
n "While taking my pills has become an automatism for me at Yamaku, I was confronted by the fact I become prone to forgetting about them when suddenly taken out of my usual daily routine."
n "While I'm thankful that Hanako takes her promise of mutual support so seriously, I'm not thrilled by the prospect of her watching me like a hawk for the remainder of the trip."
n "{vspace=60}Still, her scolding was only a minor inconvenience."

nvl hide dissolve
nvl clear

hi "You're right. It's been months since I've felt this… normal."

show ev wheatfield_talk
with charachangeev

ha "F-for me it's probably been years."
"A silence."
"While she didn't sound sad while saying it, the reminder of how stagnant Hanako's life has been until recently depresses me a bit."
"Eager to steer the discussion away from that topic, I return to what we were talking about previously."
hi "So, if we're like a family, what would that make Akira? The loud and feisty aunt?"

show ev wheatfield_smile
with charachangeev

"Hanako giggles at that mental image."
ha "Probably."
hi "And I guess Lilly would be the mother of the bunch?"
ha "N-no mother or father. Just Lilly, you and me."
"My question was merely in jest, so I raise an eyebrow at how seriously Hanako answers it."
"Does Hanako object to the suggestion of her and Lilly's relationship being like a mother-daughter relationship or does she think the idea of other people being like a mother or father figure is inappropriate since her own parents died?"
"If it's anything related to the latter, there's no way I'm going to explore that right now, lest I ruin her mood for the rest of our time here."
hi "Is Lilly like a sister to you then?"

show ev wheatfield_talk
with charachangeev

ha "I… I can't really tell for sure. I was an only child, so I don't really know."
hi "Same here. We could have asked Lilly if she were here right now."
"Hanako lets out an audible sigh. I wouldn't be surprised if her thoughts are the same as mine right now."

ha "About Lilly… Have you noticed as well?"
hi "It'd be really hard to miss it. She's kind of acting like she accidentally joined us on our honeymoon."
"The lengths Lilly's going to in order to give Hanako and me private time together seems a bit much."
"It's been mostly small things, like deciding to finish a book when we asked her to take a walk with us or suddenly wanting to take a break and catch a tan for an hour while we were in town, leaving Hanako and I to do the shopping without her."
"Although small, they have started adding up."
ha "Is she avoiding us?"
hi "Naw, she's just trying to give us some space. Wouldn't you do the same for her if it was her who just got a new boyfriend?"
ha "P-probably… Maybe. It's just that it feels like she's trying to get us to hook up even though we're already together. So I don't really understand."
"Good point. It's like she's trying to play match maker, which seemed strange since we have all the time in the world to do this at our own pace, and unlike her cousin, Lilly isn't really the type to try and hurry people along."
"Then again, she did do something similar back when she had Akira take her and us to that pool club in town in an attempt to get Hanako and me closer to each other."
hi "It's her motherly streak. She can get carried away with it at times. Just give it time. It'll probably blow over in a week or two."
ha "You're probably right."

show ev wheatfield_dreamy
with charachangeev

"We fall silent, neither of us really knowing how to continue the conversation."

nvl clear
nvl show dissolve

n "One thing remains on my mind. Even though most of Lilly's actions to give Hanako and me some time alone were rather small, one of them was decidedly less so."
n "When we arrived at the summer home and made preparations to unpack, Lilly gave us a small tour of the house ending up in the house's only bedroom: a fairly large room with a double bed near the window and a smaller single bed near the corner."
n "She then dropped a bombshell by announcing that she herself would be using the convertible futon in the living room to spend the night on before casually walking out of the room, leaving Hanako beet red and me baffled at this uncharacteristically unsubtle move on her part."
n "{vspace=60}I later questioned her about it, but she replied by saying she wasn't forcing us to sleep in the same bed, and the sight of Hanako in her nightgown wasn't anything new to me. When I realized that in order to continue the discussion I'd have to get into how far along Hanako and I were in that area, I decided not to paint myself into corner and dropped the subject while I was still ahead."
n "{vspace=60}I was, of course, a gentleman, so Hanako was given the double bed while I spent the first night in the smaller one. All in all, it was still a pretty comfortable place to sleep."

nvl clear

n "Still, the question how far Hanako and I were in “that” area lingers on my mind."
n "We have kissed each other of course and sometimes shared a tight hug, but I'm not really sure if that was any indicator on the rest. We slept together once, but Hanako merely initiated that because she thought it was the only way to prevent me from drifting away from her, and she was so uncomfortable during the whole experience that it is clear to me in hindsight that she certainly wasn't ready for the act itself."
n "{vspace=90}Is having that kind of intimacy something Hanako will ever be doing for her own enjoyment to begin with?"
n "We have never mentioned that night we spent together again after we started dating, and I don't really know how Hanako sees sex."

nvl clear

n "She isn't exactly a flirty person or someone who I'd expect to come onto me of her own. How open to sex is Hanako when the threat of losing our friendship isn't looming over her?"
n "Would she reluctantly offer herself to me again if I took the initiative out of fear that I might lose interest in her otherwise rather than because she wants me?"
n "The only way to avoid that would be to leave the initiative up to her, but that could again cause the risk of her making a move on me because she feels she has to."
n "If anything, our night together made things more complicated."
n "{vspace=60}I wonder if there's an opportunity to talk to her about it without her freezing up in embarrassment. I've learned over the last few weeks that making assumptions about Hanako isn't always the smartest thing to do."

nvl hide dissolve
nvl clear

"I gently sit upright to look at Hanako."
"It's too dark to see her face clearly, but the fact she doesn't react to me staring at her suggests she has her eyes closed."
hi "Hanako."
ha "Yes?"
hi "You weren't sleeping, were you?"
ha "No, just relaxing a bit."
"Feeling a little playful, I pick up one of the straws that broke off when we sat down here and use it to gently tickle the side of Hanako's face."
"She doesn't react."
"I carefully move the straw closer to the center of her face."
"When there's still no reaction and I start tickling her nose, she lets out a gasp, opens her eyes, puffs out her cheeks and blows the straw upwards."
"I bring it closer to her face again and for a second time she blows it away."
"We repeat this little charade a few times until she gets tired of it, sits up and playfully snatches the straw away."
ha "You're m-mean, suddenly tickling my nose like that."
hi "It wasn't exactly sudden. You just didn't react before."

show ev wheatfield_awkward
with charachangeev

stop music fadeout 2.0

"Hanako thinks for a moment, then suddenly slumps her shoulders."
ha "Oh…"
"Why does she suddenly sound depressed? Did I do something wrong?"
hi "H-hey, what's the matter?"
ha "You t-touched the right side of my face, d-didn't you?"
hi "Y-yes."
ha "I… I… don't r-really feel anything there. Not anymore…"
"I feel the urge to punch myself."
"I really should have spotted that landmine from a mile away, and yet I happily pranced right onto it."
hi "I-I'm sorry, Hanako."
ha "It's t-the s-same for my right shoulder and arm and… {i}*sigh*{/i} …well, y-you've seen it for yourself."
"I have. But I hadn't really thought much about the fact that a not insignificant part of her body was devoid of the sense of touch."
hi "You can't feel anything in any of those areas?"
ha "A-around some areas, I can f-feel it when you press hard enough. B-but nothing s-softer. N-not any pleasant sensations anymore."
"I wrap my arms around her."
"I start realizing why Hanako often hugged me so tightly when we exchanged kisses. Since the sensation on her back and shoulders was partially numbed, she had the tendency to press herself against me to maximize the sensations she was feeling from the front."
ha "I-It's p-probably for the better though. It c-could have been w-worse. I-It's better to feel n-nothing at all than to be in c-constant pain, i-isn't it?"
"That's true, but that can't feel like much of a consolation right now. I don't think it's going to do much good offering her sympathy. What she needs me to do right now is cheer her up."
"I think for a moment."
"I have an idea that might work, even if it's a bit of a gamble. It might also end up backfiring on me, but I decide to take the risk."
"I sit a little bit closer to her."
hi "You know, maybe it's not as bad as you think it is."

show bg hok_field_ni behind ev:
    yalign 0.5 zoom 1.02
show hanako emb_sad_cas_nohat_clip_close_ni behind ev
with None
hide ev
hide firefly_v1
hide firefly_v2
hide firefly_v3
hide firefly_v4
hide firefly_v5
hide firefly_v6
with charachangeev

play music music_comedy fadein 0.5

"Hanako looks at me with a puzzled expression, clearly having expected a different response."
"Keeping my left arm around her, I gently move my right hand downward to a point just above her hip and start tickling her side."

show hanako emb_blushtimid_cas_nohat_clip_close_ni at onebounce
with None

"Hanako's puzzled expression gets uncomfortable and she suddenly lets out a forced giggle."
"I smile inwardly. This was the reaction I was hoping for."

ha "H-hey, t-that tickles."
"I give her a mischievous grin and keep going. Hanako's body begins to squirm, and she starts trying to push herself away from me."

show hanako emb_downsmile_cas_nohat_clip_close_ni:
    linear 0.15 align (0.4, 1.0)
    linear 0.15 center
with Dissolvemove(0.3)

ha "D-don't do that."

show hanako:
    transform_anchor True
    parallel:
        easeout 0.7 rotate 90
    parallel:
        linear 0.5 yalign 1.5
with Pause(0.7)
with vpunch

"I let her try to get away for a moment, then unexpectedly let go of her, causing Hanako to fall backwards."
"Before she can sit upright again, I move over to her and quickly straddle her."

show hanako:
    rotate 0 ypos 2.4
with None
show hanako emb_blushtimid_cas_nohat_clip_close_ni at center
with charamovefaster

ha "H-Hisao!?"
hi "Hanako, I bet you still have plenty of sensitive spots left."
"I quickly reach down and start tickling her left side again, drawing out another giggle."

show hanako emb_smile_cas_nohat_clip_close_ni:
    ease 0.15 xalign 0.6
    ease 0.15 xalign 0.5
with Dissolvemove(0.3)

ha "D-don't."
hi "And I won't stop until you admit that."
"She moves her arm down to shield herself, so I quickly move my hand and start tickling her neck instead. One more involuntary giggle is the result."
ha "S-stop."
hi "I don't even have to look very hard, Hanako."
"When she moves her arms up to ward off my hand, I swiftly go for her armpit instead."

show hanako emb_downsmile_cas_nohat_clip_close_ni:
    function partial(bounce_general, 0.3, 0.04, 1)
with Pause(0.3)

ha "Hi-hee hee-sao, c-cut it out hee hee hee."
hi "Admit it and I'll stop."
"She tries to buck her hips in an attempt to knock me off, but I barely even feel it."
"As she lowers her arm, I grab it and start tickling the lower part of her arm…"
ha "Hee hee hee…"

show hanako emb_smile_cas_nohat_clip_close_ni:
    xalign 0.4
with Dissolvemove(0.3)

"A gasp."

show hanako emb_blushtimid_cas_nohat_clip_close_ni:
    xalign 0.6
with Dissolvemove(0.4)

"…then her collarbone when she yanks her arm away…"

ha "P-please *snort* st-stop."
"She's now giggling uncontrollably."
"…Then her tummy…"

show hanako emb_downsmile_cas_nohat_clip_close_ni:
    xalign 0.5
with Dissolvemove(0.3)

ha "Hahahahaha!"
"…then her ribs just beneath her breasts."

show hanako:
    ease 0.3 xalign 0.6 yalign 1.3 rotate -10
with Pause(0.3)

ha "S-stop, h-h-hee-hee-hee!"
"At this point I'm using both hands to tickle several areas at once. Hanako is literally crying with laughter."
"I realize I'm taking a bit of a risk right now. If one of her flailing arms accidentally hits me in the chest, I'll probably go out like a light and I doubt an ambulance could get here very quickly."
"Still, seeing the usually subdued Hanako like this is an interesting experience."
ha "Hahaha st-stop, I hee hee a-admit hee hee it! I admit it!"

show hanako emb_downtimid_cas_nohat_clip_close_ni at center:
    rotate 0
with charachangealways

stop music fadeout 1.0

"I immediately stop tickling her, get off of her and sit across from her as she tries her hardest to catch her breath."

play music music_pearly fadein 0.5

hi "I never knew you were this ticklish."
"Hanako's now panting as if she just sprinted a kilometer uphill."
"As her breathing slowly returns to normal, she sits up and wipes the tears from her eyes."
"I half expect her to angrily walk away, but instead she just sits there."
hi "I think this kind of proves my point, don't you agree?"

show hanako emb_blushtimid_cas_nohat_clip_close_ni
with chchange

ha "Ummm…"
"Not willing to let her back down, I reach out and make a tickling motion in the air with my fingers."

show hanako emb_emb_cas_nohat_clip_close_ni:
    xalign 0.6
with Dissolvemove(0.3)

"Hanako immediately shivers, crosses her arms in front of her chest and lets out an involuntary giggle."
ha "Th-that tickles. D-don't get near me."
hi "I didn't even touch you just now. Anyway, don't you agree?"

show hanako emb_smile_cas_nohat_clip_close_ni at center
with chchange

"She doesn't say anything, but she carefully leans forward and gives me a kiss on the lips."
"As unorthodox as it may have been, I think my method of cheering her up worked."
"I've never heard Hanako laugh like that before. I hope that someday she'll be able to laugh like that without being forced into it."
ha "Hisao?"
hi "Yes?"
ha "I'm okay now. Just d-don't do that again, promise?"
hi "It's a big temptation, but okay. I promise."

show hanako emb_blushtimid_cas_nohat_clip_close_ni
with charachangealways

ha "Shall we go back now? I'm a bit tired after all this."
hi "Lead the way."

scene bg hok_houseext_ni:
    yalign 0.5 zoom 1.02
with locationskip

"We slowly walk back to the summer home at the far end of the wheat field."
"As we approach the patio, which is pitch-black due to being in the shadow of the building, we hear Lilly's familiar voice from somewhere."
li "Welcome back, Hanako, Hisao. Have you enjoyed your walk?"

play sound sfx_impact
with vpunch

"I am about to ask Lilly where she is when I hear a soft thud followed by a startled yelp."
"Seems like Hanako, who was walking slightly ahead, has already found her."

show lilly basic_oops_cas_ni at twoleft
show hanako cover_worry_cas_ni at tworight
with charaenter

ha "I-I'm sorry, Lilly. I didn't see you."

show lilly basic_cheerful_cas_ni
with chchange

li "My, is it that late already? Please wait here for a moment."

play sound sfx_dooropen volume 0.4

hide lilly
with charaexit

"We hear measured steps head towards the house followed by the sound of an opening door."

show lilly basic_smile_cas_ni at twoleft
with charaenter

"A few seconds later, a light near the patio door flicks on as Lilly emerges and heads back towards the chair she was sitting in before Hanako nearly tripped over her."
hi "We'll be going inside, Lilly. Care to join us?"

show lilly basic_satisfied_cas_ni
with chchange

"Lilly picks up a discarded book lying near the chair and holds it up for a moment."
li "I only have a few pages left. I will be with you in a few minutes. Please make yourselves comfortable."
li "And ah… Hanako?"

show hanako cover_bashful_cas_ni
with chchange

ha "Yes, Lilly?"

show lilly basic_cheerful_cas_ni
with chchange

"She sends us a playful grin."
li "Can you retrieve the bottle we opened this morning? I believe a glass before bedtime will help us sleep all the better."

stop music fadeout 3.0
stop ambient fadeout 3.0
scene black
with Dissolve(3.0)

return