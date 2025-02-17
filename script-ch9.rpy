label sisterhood_ch9:
label .sh_ch9:

$ set_window_tint(TINT_HANAKO)

stop music fadeout 2.0
play sound sfx_shower fadein 2.0

scene bg hotel_bathroom
show steam2
with Fade(1, 0, 1)
with Pause(5)

hide steam2
with Dissolve(2.0)

nvl clear
nvl show dissolve

n "As I step out of the bath, I can't help but think that this is like one of those romance novels where a guy and a girl go out, have dinner and a date, and then spend the night at a hotel consummating the relationship."
n "After taking a break at a coffee shop near the arcade we visited, I expected us to return to Yamaku. Then Hisao proposed spending the night at a hotel nearby. And that's exactly what we ended up doing."

nvl clear

n "We ended up splitting the costs—Hisao didn't object this time—and got a nice room on the eighth floor with a soft carpet, a double bed, and a clean bathroom. Hisao took a rather quick bath, but told me I could take my time, and I was happy to take some time in order to get myself cleaned up."
n "As fun as the arcade had been, the smell there wasn't exactly heavenly, and I felt like the odor of perspiration rubbed off on me. Well, maybe some of it is my own. The cabinet in the bathroom contained a few small flasks of fragrant shampoo that I gratefully made use of."

nvl clear

n "Consummating the relationship."
n "{vspace=60}Hisao never said anything specific, but I'm not so naïve as to believe we're merely here to sleep in a bigger bed. Nor do I think we got ourselves a room far from the noisy dorm rooms in order to just give each other a “helping hand” in the dark, like we've done a few times before now."
n "{vspace=30}If we go all the way tonight and I can manage to enjoy it, we'll be closer than before."
n "If not, we'll probably spend the next few days apologizing to each other."

nvl hide dissolve

"I put on the soft bathrobe that Hisao left here for my perusal. It feels very nice to the touch."
"Where are all the other towels? I saw Hisao carrying some of them."
"What exactly is he planning?"
"I walk over to the place where our clothes are piled up, and fish my hair clip out of the pockets of my pants."
"I apply the clip, say a little prayer for good luck and leave the bathroom."

stop sound fadeout 0.5

scene bg hotel_room
with Dissolve(2.0)

play music music_one fadein 4.0

"The first thing I notice is that the room isn't quite like I expected it to be."
"I thought it'd either be completely dark or the lights near the bed being lit, but neither is the case. None of the lights are on, yet I can still make out the interior somewhat, particularly near the window, due to the curtains still being drawn back."
"I also notice the room's pretty warm. Did he turn the radiator up?"
"The second thing that stands out is the fact that nobody is sitting or lying on the bed."
"Hisao, who's wearing a bathrobe similar to mine, is sitting on the floor near the window, in the spot illuminated by the moonlight and lights from the city."
"Does he want to do it on the floor? Isn't that uncomfortable?"
ha "Hisao?"

show hisao basic_smile_bath_ni
with charaenter

"Hisao looks in my direction and beckons."
"As I approach him, I notice he's spread one of the blankets on the floor and put the towels he took from the bathroom on top of it, creating what almost looks like a make-shift picnic blanket."
ha "A…a moonlight picnic?"

show hisao basic_grin_bath_ni
with chchange

hi "It kinda resembles it, doesn't it?"
"A little bit, though it'd be a pretty shoddy picnic. No glasses, no napkins, just a bottle of…"
"…What's in there anyway? And what's in that large flat bowl nearby?"
"I walk over to Hisao and sit next to him, still trying to make sense of things."

show hisao basic_smile_bath_close_ni
with characlose

ha "What do you have there? Where did that bowl come from? And what's in the bottle?"
"He gives me a sheepish grin."

show hisao basic_grin_bath_close_ni
with chchange

hi "The stuff from the bottle needed to be mixed with some hot water, so I got this bowl. It's actually a fruit bowl."
hi "As for the bottle…"
"Are we going to be intimate or practice science together?"

show hisao basic_blush_bath_close_ni
with chchange

hi "…in a way, you could call it lubricant and in a way…"
"{i}LUBRICANT?!{/i}"
"Does he plan to skip foreplay? Or is he planning something else…?"

show hisao basic_smile_bath_close_ni
with chchange

"My expression must have given me away as Hisao puts his hand on my shoulder as if to reassure me."
hi "Relax, we're not going to do anything weird."
"Are you sure about that?"
ha "S-sorry."

show hisao basic_speak_bath_close_ni
with chchange

hi "Anyway… You enjoyed the shoulder rubs and massages we've shared, didn't you?"
ha "Y-yes, I did."

show hisao basic_neutral_bath_close_ni
with chchange

hi "I was thinking we could do a more… intimate… massage. That stuff in the bottle is a special type of massage gel."
ha "D-didn't you just say it was lubricant?"

show hisao basic_smile_bath_close_ni
with chchange

hi "It's both actually. Its main purpose is to act as a massage lotion, but since it's so smooth and slippery, it can double as a lubricant."
"I try to digest what Hisao's saying. He has put more thought into this whole thing than I expected."
"A massage… So we'll be rubbing that stuff on each other?"
"That explains why we're sitting on the floor and why he has covered the area with towels."
ha "Where did you get this?"
hi "A little shop in the city last weekend."

show hisao basic_grin_bath_close_ni
with chchange

hi "I was actually going for some ordinary massage lotion, but the guy behind the counter said this was the ultimate experience for a couple."
hi "I didn't tell him we were fairly new at this though."
"“Couple”."
"I really like the sound of that word."

show hisao basic_blush_bath_close_ni
with chchange

hi "I tried to get some more information about this kind of thing, but… heh… Most sites that came up wouldn't make it through the computer lab's content filter."
"That's not exactly reassuring."
ha "So… ummm… H-how does this w-work?"

show hisao basic_smile_bath_close_ni
with chchange

hi "Do you want to try it?"
ha "Y-you went through a lot of effort to arrange all this."
hi "We can stop at any time you want."
"I meekly nod."

show hisao basic_smile_bath_close_ni:
    zoom 1.3 ypos 1.2
with characlose

"Hisao pulls me closer in a gentle hug and carefully puts his lips on mine."
hi "We can start with this."
ha "O-okay."

scene black
with shuteye

"As his right hand starts stroking my head and his tongue starts playing around with mine, I close my eyes and try to push my insecurities to the back of my mind."
"I'm not completely sure how well I'll be able to relax in the spot we're in."
"The curtains are drawn back, but we're on the eight floor. People couldn't possibly peek inside from the other buildings and even if they were watching, the room itself is dark, so all they'd see was the reflection of the lights on the window, right?"
"This is the first time since that one night in my room we'll be able to see each other pretty clearly. Obviously if the room were pitch black, we'd end up toppling the bowl with lotion sooner or later."

scene bg hotel_room
show hisao basic_smile_bath_close_ni
with openeye

"Parting his lips from mine, Hisao breaks his hug, gives me a quick kiss on my left cheek and holds out the bowl to me."
hi "Do you want to sample a bit, Hanako?"
"I dip my finger into the bowl in an attempt to get an impression of Hisao's concoction."
"The substance is more a liquid than a gel, clear and not all that much thicker than water."
"I stir the mixture a bit and don't meet much resistance."
"I hold my finger under my nose and sniff shortly, but don't smell anything. What surprises me most is its temperature."
ha "It's… really warm."

show hisao basic_speak_bath_close_ni
with chchange

hi "Yeah, I mixed the gel from the bottle with hot water, and I've been covering the bowl until you came out of the bathroom."
hi "You don't think it's too hot, do you?"
ha "N-no."

show hisao basic_smile_bath_close_ni
with chchange

hi "So… shall we?"
ha "…W-what would you l-like me to do?"

show hisao basic_speak_bath_ni
with charadistant

"Hisao puts the bowl away, moves off the blanket and points at a small bump beneath the towels."
hi "I've put the small cushion from one of the chairs there for you to rest your head on."
hi "Could you undo the belt of your bathrobe and then lie down on your stomach?"
"Nervously, I remove the belt of my bathrobe and lie down, putting my head on the pillow beneath the towels and laying my arms at my side."
ha "Like this?"

show hisao basic_smile_bath_ni
with chchange

hi "Yes. Now just take a deep breath and relax."
"I inhale deeply and then slowly exhale, trying to slow the nervous beating of my heart a bit."

hide hisao
with charaexit

scene ev hotel_onhanako_large:
    crop (302, 700, 1920, 1080)
show black behind ev
with mediumflash

"I feel my hips being pressed down as Hisao straddles me."
"He takes the shoulders of my bathrobe, slowly pulls them aside and slides it down until just beneath my waist."
"His hands gently run through my hair before moving it to one side, exposing my back."
"He then slowly strokes my neck and shoulders."
hi "I'm going to apply some gel. Don't get startled."
"I hear a few soft splashes, and feel a trail of liquid running down my left side."
"I let out a soft gasp as something warm and wet hits my back and his hands start rubbing the wet substance on my neck, all the way up to my jaw line, before going down and proceeding on my shoulders."

show ev:
    crop (1685, 0, 1920, 1080)
with Dissolve(1.0)

"The sensation is different from the shoulder rubs I'm accustomed to. His touch is a lot softer and more gentle than the usual kneading."
ha "H-Hisao?"
hi "Yes?"
ha "Is… Is it okay to… you know… rub that… stuff… in my burn scars?"
hi "It shouldn't be harmful. The bottle says it's made out of seaweed leaves and is completely water-based."
hi "The shampoo you used to wash your hair earlier is probably more aggressive than this stuff."
ha "If you say so…"
hi "Hanako, could you put your arms by your side so your palms are facing up?"
"I do as he says, and he takes my right arm gently in his hand, rubbing it in top to bottom."

scene ev hotel_onhanako:
    zoom 1.2 align (0.5, 0.5)
    ease 10.0 zoom 1.0
with mediumflash

"For the most part, I don't feel much of it, but I shudder a bit when he reaches my hand and starts caressing my palm with his fingers."
hi "That's not unpleasant, is it?"
"I bite my lip to keep myself from laughing when he rubs in and then strokes each of my fingers."
ha "I-it tickles a bit."
"He moves to my left arm next, carefully working his way down."
"He chuckles when I let out a surprised gasp."
hi "Do you like having your elbow stroked?"
"Does he expect me to answer that?"
"He ends his caresses with my left palm and fingers, obviously enjoying the reactions his touches get out of me."
hi "Can you place your arms in front of you now?"
ha "Okay."
"He moves back to my shoulders before spreading his hands to stroke my armpits…"
"I giggle. That really tickles."
"…and my sides."
"I let out a content sigh to let him know how nice this feels."
"As he spreads and rubs the gel all over my back, it leaves a warm and comfortable sensation behind."
"My entire upper body is now covered in lotion and Hisao's now firmer strokes slide across my skin without much resistance, even in the scarred areas."
"Hisao seems content at just stroking my shoulders, neck and back for now."
"Is he waiting for a cue from me?"
ha "Hisao… Should I… turn around?"
hi "Just a little while longer, Hanako. There's one spot left to go."
"I feel him move back just a little bit and the next moment I feel my bathrobe being pulled down further, exposing my bottom."
"I swallow hard, but don't resist as he starts rubbing, stroking and fondling my buttocks."
"…"
"…I don't exactly hate it."
"In fact, I kind of like it, but what makes me feel awkward is the fact I just {i}know{/i} he's staring."
"It makes me nervous. Not only is my right buttock pretty heavily scarred, but I also have rather small hips for my size."
ha "A-are you s-staring?"
hi "Sorry. I can't exactly say it's a bad view."
"Having finished applying the gel, Hisao raises his hips in order to allow me room to turn around, but before I can get up, he kneads my buttocks one last time and then gets off me."
"I pull my bathrobe up a bit, turn around and lie back."
"Hisao straddles me again, holding a handful of gel in his cupped hands that's gently trickling upon my stomach."
hi "Ready?"
ha "Y-yes."
"I can feel Hisao's hands spreading the warm gel across my neck and my collarbone before they move down to my breasts, stroking them gently, then more and more firmly."
"My breathing gets heavier as his hands pet and fondle my breasts, running my erect nipples between his fingers."
"It would have hurt if they hadn't been this slippery, but right now this feels really good."
"After covering my belly, he gets off me, gently takes my ankles and lays my feet onto his lap."
"I can't help but giggle again."
"The soles of my feet are so ticklish that I have to use all my willpower to prevent myself from accidentally kicking Hisao, but the way he lovingly fondles each separate toe feels wonderful."
"He carefully raises my legs, letting my ankles rest on his shoulders, and starts stroking my shins and the back of my knees, causing me to make a sound that's part giggle and part moan."
"As he slowly, teasingly, moves down to my thighs I cannot help but remember how I was depressed not too long ago because part of my body is numb to sensations."
"Hisao told me that evening that I still had plenty of sensitive spots left and this night I realize more than ever how right he was about that."
"Even in the last few minutes we've found several sweet spots I never knew I had."
hi "Is it okay?"
"I respond with a reassuring nod and brush aside the parts of my bathrobe still covering my body."
"He takes another handful of gel, I close my eyes and moments later I can feel his hands moving from my thighs down to the place between them."
"But instead of merely the rubbing he usually does, he starts stroking and massaging it with both hands."
"My breath catches due to the sensation."
"This feels… different from the other times I've allowed him to stroke me down there."
"He notices my reaction and starts trying different strokes while keeping a close eye on my face."
"…long, swift ones…"
hi "What way do you like best?"
"…short, swift ones…"
ha "Hhhh—"
"Too much direct stimulation."
"…slow firm ones…"
ha "B-better already."
"…swift circular ones…"
ha "S-slower…"
"…slow circular ones…"
ha "Nnnngg…"
hi "Seems like you like this one in particular."
"I nod my head, too embarrassed to admit it with words."
hi "Do you want me to keep going?"
ha "S-stop for a moment…"
"I take a second to catch my breath."
"This has felt wonderful, but I feel a bit bad that right now I'm the only one having a good time. Usually, I try to do the final part together with him, his arousal often acting as a catalyst for my own."
ha "Can I r-rub you in first?"
"He nods and lets go of me, letting me move aside before taking up the spot I was occupying before."
"He loosens his belt and lies down on his stomach in front of me."

scene ev hotel_onhisao_large:
    crop (1046, 0, 1920, 1080)
show black behind ev
with mediumflash

"For a moment I consider putting my bathrobe back on but then decide that doing so would feel really uncomfortable with my entire body covered in lotion."
"The room temperature itself is high enough for me to comfortably continue without my bathrobe, though I'm a bit squeamish about the part where he'll be able to see me rubbing him in."
"Did he decide to let me go first so he could be massaged by a naked girl?"
"Pushing these thoughts aside, I straddle him, pull his bathrobe down to his waist and use my cupped hands to gather some gel which I drop on his back with a soft splash."
"Then I realize I'm not really sure on how to proceed. Hisao probably secretly read up on this stuff beforehand."
"Maybe I should just to try and copy him as closely as I can."
"Hmmm… The neck and shoulders first, right?"
"…Then the arms…"
hi "H-hey!"
"I giggle at this surprisingly cute reaction and make a mental note that he likes having his upper arms fondled. I have to keep that in mind."
"The back next…"

show ev:
    crop (0, 716, 1920, 1080)
with Dissolve(1.0)

hi "That feels really nice, Hanako."
"He actually has a pretty nice back."
"I move to pull down his bathrobe, then change my mind and carefully take it off altogether and start kneading his buttocks."
hi "You're not staring, are you?"
ha "I-I'm not."
"I am, of course."
"I swallow nervously as I finish with his butt and raise my hips so he can turn around."
"This is going to be the most awkward part."
"As he turns around and I gently sit down on top of him, I notice he's staring."
"Not a quick, sneaky peek, but a thorough almost analyzing look."
"Uncomfortably, I cross my arms in front of my breasts, even though he's not looking at them specifically."
ha "P-please don't stare at me like that."
hi "You're looking really beautiful, Hanako."
ha "D-don't say that."
"There's something about his tone though."
"It doesn't sound like he's making some random compliment. He sounds somewhat serious."
hi "Could you stand up for a moment and take a look in the mirror on the far wall from here?"
ha "D-do I have to?"
hi "Just really quick."

scene bg hotel_room
with locationchange

"I reluctantly get up."
"I hate looking at myself in mirrors, even when not wearing my badly damaged birthday suit. At least the mirror is rather far away and it's fairly dark."

scene ev hotel_mirror:
    zoom 1.2 align (0.5, 0.0)
    ease 10.0 zoom 1.0
with Dissolve(2.0)

"I look and then it strikes me that I can still see my body fairly well."
"Or at least, part of my body. Specifically the part of my body that isn't scarred."
"Of course the scar tissue is still there, but due to the rough texture, it doesn't reflect the nearby light very well despite being covered in lotion and merely appears as a dark area covering part of me."
"The other parts of my body and my freshly washed hair, on the other hand, are accentuated like never before, sparkling in the moonlight coming through the window due to the gel turning my smoothened skin into a semi-reflective surface."
"A little befuddled, I slowly turn around once."
"A chuckle comes from my boyfriend who's still in the same spot as I left him."
hi "I don't mind if you want to keep admiring yourself in the mirror a little while longer, Hanako."
"My mood lifted, I get back on top of him again, taking a handful of lotion to apply to his chest."

scene ev hotel_onhisao:
    zoom 1.2 align (0.5, 0.5)
    ease 10.0 zoom 1.0
with mediumflash

"He's still looking me over like before, but for the time being, I actually feel a little bit beautiful."
"I lovingly fondle his chest and nipples, tickling his scar while applying the gel and watching with playful amusement whenever I reach a spot that forces a reaction out of him."
"My caresses have already made him pretty aroused and while stroking his feet and legs, I try my hardest to look at my hands instead of at his crotch in order to avoid embarrassment."
"With only one more spot of his body to cover, I straddle his upper legs, take a handful of gel and start stroking his member."
"First slowly and carefully, then faster and firmer."
"I'm having very mixed feelings right now."
"On the one hand, this is great fun. Previously, I only had aural feedback to rely on while getting him off."
"Seeing the subtle changes in his expression as I change the pace and firmness of my touches and watching the pleasure on his face as a result of my caresses is wonderful."
"On the other hand, seeing his… thing… right in front of me makes me more than a little nervous."
"Is that really going to go inside of me?"
"Well, I know it's possible since I didn't tear the last time, but it certainly hurt back then and not just when he put it in."
"Part of the reason he purchased that lotion is probably to make it go smoother."
hi "Hanako, could you stop for a moment?"
ha "Hmmm?"
"He looks at me with an inviting look in his eyes."
hi "I think we're more than ready for the next part."
"How can you tell?"
ha "Just… give me a moment."
"Maybe it'll feel better if I do it myself."
"Lower myself onto it and move back up if it hurts."
hi "Hey, don't look so scared. You're probably going to love this."
ha "Huh?"
hi "Just lie down on top of me."
ha "Like this?"
"I carefully lie down on top of him, my chin now hovering closely above his chest."

scene ev hotel_layontop
with Dissolve(1.0)

hi "Could you move up a little bit so we're at the same eye level?"
"I brace my feet and push myself up his body a bit…"
ha "EEK!"
"…only to find out that the lotion covering us reduced friction between our bodies to such an extent that I completely overshoot my mark and his nose ends up between my breasts."
hi "My eyes are down here, Hanako."
"I giggle at that remark."
ha "Sorry."
"I hastily push myself down, again sliding slightly too far, causing me to end up back where I started."
hi "Looks like you're picking it up pretty quickly."
"I push myself up again, more gently this time, and now we level out well."
ha "P-picking what up?"
hi "Applying the lotion was just preparation."
"Preparation? I'm a bit puzzled."
"What am I picking up? Sliding up and down?"
"Suddenly, I have a bright moment. I smile bashfully."
ha "You w-want me to g-give you a f-full b-body massage?"
hi "This gel is made specifically for that purpose. That's why it's so extremely slippery."
hi "Do you want to give it a try?"
"I nod shyly."
"The prospect of an extended massage sounds infinitely better than the prospect of intercourse right now."
"I push myself down a bit until just beneath his chest scar, then slide upwards again until I look him in the eyes once more where I am rewarded with an approving nod."
"For a third time I slide down and up on top of him, this time a passionate kiss being my greeting."
"For nearly half an hour, we go on like this; kissing, rubbing our bodies against each other, me softly pushing myself off to drift back and forth on top of him and he occasionally raising his upper body or hips to let me slide on my own."
"I'm enjoying the extensive body contact immensely and am surprised at how smoothly I'm able to move despite my scar tissue."
"Neither of us says a word the whole time, the only sounds our excited breathing, the occasional soft moan and our awkward laughter throughout."
"As we get more and more passionate in our movements, I can feel him pressing his loins up against mine."
"Our slip-and-slide fest, while certainly enjoyable, isn't the most efficient way to stimulate our most sensitive areas and I'm considering getting off of him and finishing the job by hand."
"I already found out that I can probably afford to be a bit rougher this time without the risk of hurting him."
"Just as I prepare to follow up on that plan, another idea flashes through my mind that might excite him more than the usual way we tend to end our intimate moments."
ha "…H-Hisao…?"
hi "…H-Hanako…?"
ha "…could you…do something…?"
hi "…what…?"
ha "…s-spread…your…legs…?"
hi "Huh?"
ha "…p-please?"
"He looks at me with a puzzled expression for a moment but then complies while doing his best not to look too uncomfortable."
"I move myself up a bit, take hold of his erect member, point it at the ceiling and then move down until it's resting against my crotch."

scene ev hotel_thigh_large:
    crop (1618, 0, 1920, 1080)
show black behind ev
with Dissolve(1.0)

"I carefully close my legs, then cross my feet and squeeze my thighs together as tightly as I can."
"Hisao tenses up and lets out a loud groan in response."
"Did that feel good or did I just really hurt him?"
hi "…Hanako…"
ha "Y-yes?"
hi "…can you…try moving…?"
"Whew…"

scene ev hotel_thigh:
    zoom 1.2 align (0.5, 0.5)
    ease 10.0 zoom 1.0
with mediumflash

"I lean on my arms, pressing myself against his base and with a bit of trial and error find an angle that allows me to enjoy the friction as well."
"As I start swaying my hips, Hisao wraps his legs around mine and starts caressing my neck and chest with his hands."
"This is… pretty good."
"This almost feels like we're having intercourse. Except I'm the one doing the thrusting."
"Hmmmm… really good…"
"Because I have my back arched I can't see Hisao's face very well, but I can tell by the sounds he's making that he's getting close."
"Good thing my inner thighs are still slippery or he'd be groaning in pain right now."
hi "Ahh… Hanako…"
ha "Nnnng… Hisao…?"
hi "{cps=20}S-slow down… hah… slow down a bit…{/cps}"
"I can tell his heart's doing fine right now. From the look of ecstasy on his face, I can tell he's feeling really good and trying his hardest to hold back."
"I consider slowing down, but then speed up the movement of my hips and try to get as much stimulation for myself out of it as I can."
hi "Ugh… H-H-Hanako… W-what…"
"For a second, it seems like he's going to protest, but then he gives in and starts thrusting until he reaches his climax in a frenzy of frantic grinding."

scene ev hotel_thigh_climax
with Fade(1.0, 0, 0.3, color="#FFF")
with Pause(2.0)

stop music fadeout 4.0

scene bg hotel_room
with Dissolve(2.0)

"After Hisao catches his breath, I let go of him, and we sit upright, still in a bit of a daze from our unusual experience together."
"Now we're sitting on the floor next to the bed, Hisao leaning back against it and me sitting in front of him and gently leaning back against his chest."
"Hisao has one arm wrapped around me and is softly caressing me with the other."

show hisao basic_speak_nak_close_ni
with charaenter

hi "Hanako… Why did you just…?"
"Is he bothered by the fact I just pushed him over the edge?"
ha "You w-were looking like you were f-feeling really good, so I thought it wouldn't be a problem to go on."
ha "If your heart was acting up, you wouldn't have asked me to just s-slow down."

show hisao basic_neutral_nak_close_ni
with chchange

hi "It's not that, it's just…"
"I follow his gaze as it rests on the towel I just used to wipe my thighs clean after his ejaculation."
hi "…what we did just now wasn't exactly safe."
hi "Even if the odds are very low of you getting… you know… pregnant from this."
"Pregnant…"
ha "Ummm… Hisao?"
hi "Yeah?"
ha "It's okay. You've been… exercising in order for us to be… intimate, so I w-wanted to do something too."
ha "I've been using… p-protection so you wouldn't h-have to and this would feel b-better for you."

show hisao basic_speak_nak_close_ni
with chchange

hi "Huh? You mean to say that you're on the pill? Since when?"
ha "S-since Hokkaido."

show hisao basic_grin_nak_close_ni
with chchange

hi "Wow… I didn't imagine you making the effort to get them."
ha "I h-had… help."
"That is to say, Lilly obtained them for me."
"I realize I'm probably not allowed to get a hold of them that way, but Lilly was the only person I dared to approach."
"Thankfully, she was a really good sport and willfully bought my blatantly transparent excuse about troubles with my menstruation without asking any further questions."

show hisao basic_speak_nak_close_ni
with chchange

hi "But why didn't you tell me?"
ha "I w-wanted to tell you when I was… r-ready for it."

show hisao basic_smile_nak_close_ni
with chchange

hi "I understand. That probably wasn't today, was it? I saw your frightened face earlier."
ha "I d-don't… really know."
hi "It's okay. This night has been really wonderful so far. I'd hate to see it ruined because we end up doing something that causes me to hurt you."
"Maybe that's part of the problem."
"I had a really good time just now, and tonight's been very good on the whole. How am I supposed to relax in the first place if he's implying the evening will be ruined if I can't enjoy it enough?"
"And if I can't relax, it'll only become more likely that I won't be able to enjoy it. It's like a vicious circle."
ha "Ummm… That's… a problem…"

show hisao basic_neutral_nak_close_ni
with chchange

hi "Huh?"
ha "You'll f-feel bad when I can't relax and e-enjoy it… S-so I can't relax b-because I don't want you to feel bad."
hi "I see. That makes sense."
hi "So I can't relax if you can't relax, and you can't relax because I can't relax. It's like a feedback loop."
ha "Y-yes…"
hi "What do you suggest?"
ha "I… d-don't think a little discomfort is enough to ruin this wonderful night. I'm… not going to break."

show hisao basic_smile_nak_close_ni
with chchange

hi "Then let's give it a try."

play music music_one fadein 4.0

scene ev hotel_masturbate:
    align (0.5, 0.5) zoom 1.2
    ease 10.0 zoom 1.0
with mediumflash

"He places his legs in front of mine, preventing me from closing them. Then he takes a bit of lotion and starts fondling me with both hands while kissing the left side of my neck and earlobe."
"I gasp and giggle at his attentions."
ha "H-hey…"
hi "…let's get you warmed up a little."
"Our earlier actions already got me “warmed up” quite a bit, but I'm not going to refuse a chance to be pampered by him a bit more."
"I sit back and let out a little cry as his left hand sneaks down and starts fingering me."
"For a while he keeps quiet, content to just listen to my heavy breathing. Then he moves his lips to my ear and softly whispers to me."
hi "Hanako, I want you to try and relax as much as you can."
ha "…s-sure… ahhhh…"
"I can feel how his right hand slowly moves down as well."
ha "W-what are you… hmmm… g-going to do—{i}WHAAaa!{/i}"
"Before I realize what's happening, his right hand has reached my lady bits and he's slowly pushing one of his fingers inside me."
"I let out a yelp and reflexively grab his arm though because we're both still pretty slippery, I can't get enough grip to pull it away. He keeps his finger in place for a second and then slowly pulls out again, causing me to exhale in relief."
hi "Sorry, did that hurt?"
"I don't think it did. It felt really weird and awkward, but it wasn't exactly painful."
ha "N-no."
"Upon hearing my reply he pushes back in…"
"I try to suppress a gasp, but fail."
hi "Try to relax your muscles, Hanako."
"…and back out. Then back in again…"
hi "Don't hold your breath. Just keep breathing in and out normally."
"…and out."
"I nod weakly and try to focus on the sensation his other hand instills in me."
"At first, my body jumps each time he pushes forth his finger, but as he continues with what he called my “warming up”, I slowly manage to relax and enjoy his touch again, even as he slightly speeds up the movement of both hands."
"… Upon seeing that my signals of discomfort are disappearing, he whispers in my ear."
hi "You're doing well, Hanako. Now… let's try with two…"
# custom start
"I really like how soothing his voice is when he does that."
"True to his word, the number of digits inside me doubles. It doesn't take me by surprise as much this time, though I'm not entirely used to the sensation quite yet. Still, I'll take unfamiliarity over pain."
"In and out, and in again…"
"Unfamiliarity makes way for growing pleasure as time passes. Small coos of satisfaction escape my lips, which Hisao takes as an indication to go faster. This, combined with his other hand on my breast and his kisses on my neck, are nothing short of pure euphoria."

show ev hotel_masturbate_climax
with charachangeev

"After a few minutes, my body begins to squirm, an indication of what's to come. My hands find their way to Hisao's hips in order to help steady myself, my previously quiet moans growing louder and more frequent."
ha "H-ha… Hi…"
"For his part, Hisao increases the speed of his fingers, bringing me ever closer to the edge. I can feel that familiar buildup between my legs, and my breathing is increasing in both speed and raggedness."
"After a couple of seconds, I can't hold it any longer."
ha "Hi… Hisao!"
"I feel a surge of pleasure from my lower regions that quickly spreads all over my body. Hisao hasn't stopped, even as my lower lips contract rhythmically around his fingers."

stop music fadeout 4.0

scene bg hotel_room
with Fade(3, 0, 1, color="#FFF")

"It begins to subside all too quickly, and as much as I'd like to continue, my body is demanding respite."
# custom end
ha "S-s-stop..."
"As the sensations of the last contraction die down and Hisao ceases providing the intense stimulation I just endured, I breathe a long sigh of relief."
"Hisao moves his legs away, wraps his arms around my waist and lets me catch my bearings while kissing my heavily flushed cheek and softly chuckling a bit to himself."
ha "P-please d-don't laugh at me…"
"It wasn't as obvious when we were still keeping the lights off, but being pleasured can draw some pretty entertaining reactions out of people. It's really best not to think too hard about how you must have looked to someone else afterwards."

show hisao basic_grin_nak_close_ni
with charaenter

hi "I recall you laughing to yourself while I was making faces."
"I guess I'm not in a position to say anything."
"…"
"I give him a quick kiss back as a quiet admission and then look at him expectantly."
"Now what?"

show hisao basic_speak_nak_close_ni
with chchange

hi "Can you get onto the bed?"

hide hisao
with charaexit

"I unsteadily get to my feet and lie down upon the bed."
"Hisao takes the pillow we used as a head rest earlier and carefully places it under my hips."
"We're still completely covered in seaweed gel. This bed's gonna be a major mess afterwards."
"Good thing we won't be the ones who'll have to change the sheets."
"For a moment we just look each other in the eyes."
"A mutual look of uncertainty, then one of mutual reassurance."

show hisao basic_neutral_nak_close_ni
with charaenter

hi "Don't be afraid."
ha "I won't be if you aren't."

hide hisao
with charaexit

play music music_romance fadein 4.0

scene ev hotel_bed:
    zoom 1.2 align (0.5, 0.5)
    ease 10.0 zoom 1.0
with mediumflash

"I close my eyes and he gently spreads my legs, stroking the inside just a little and then I feel the sensation of something just a little larger than his two fingers smoothly sliding into me."
"For a moment we both take a surprised look at the place where we're joined now, and Hisao makes a few reluctant movements to check for signs of discomfort on my part."
"When those signs fail to occur, we share a little laugh of relief, and Hisao lowers himself and lies down flatly on top of me."
"He grabs hold of my shoulders and slides up my body as far as he can until we can look each other in the eyes."
hi "I'm not too heavy, am I?"
ha "N-no."
"The weight of his body on top of mine makes me pretty much unable to move anything other than my arms and legs, but it's a small price to pay for the extensive body contact we can have this way."
"I raise my legs, letting them rest on his calves and wrap my arms around him."
"He slowly starts grinding his pelvis against mine, and I do my best to adapt my movements to his, tilting my hips until the friction starts feeling good."
"It takes us a bit of effort to find a workable rhythm, my scar tissue occasionally hampering us a bit. Fortunately, since we're still really slippery from before, it's a lot easier than last time."

show ev hotel_bed_climax:
    zoom 1.05 align (0.5, 0.5)
    ease 0.3 zoom 1.0
    ease 0.2 zoom 1.05
with dissolve

"I lie back and close my eyes, basking in the amazing sensation we're experiencing, wiggling my upper body as much as Hisao's weight allows me to in order to increase the stimulation."
"This couldn't be more different from the last time our bodies became one."
"The last time, we were distant, neither of us really knowing what we were feeling, whether we really wanted this and whether the other really wanted this. Our bodies had minimal contact, and we experienced more than a little bit of discomfort, physically and emotionally."
"Now we're entangled in each other, closer to each other than we ever have been before, and I feel this union is as both an emotional and a physical one."
"With each moment, our movements become more instinctual than before, more desperate than before."
"As I feel my orgasm approaching inevitably, I tighten my arms around him as strongly as I can as if to draw him into myself."
"I lose control and the first convulsion hits my body, letting out an involuntary cry that contains both physical pleasure and emotional joy at the same time."

stop music fadeout 6.0

scene black
with Fade(3, 0, 1, color="#FFF")

"After our climax, Hisao uses the last of his strength to slide off of me and roll on his back."

play music music_twinkle fadein 4.0
play sound sfx_rustling volume 0.8

"With some effort, I manage to pull up the covers and press myself close to him before every muscle in my body relaxes and a feeling of bliss washes over me that makes me want to laugh and cry at the same time."
"Despite already knowing that he came through our act of passion in one piece, I place my hand on his chest as if to acknowledge his heart remained steady."
"Hisao's already slipping away into slumber, and I find myself getting sleepier by the second as well."
"But I still want to say something; something to thank him for the moments we just shared."
"I softly kiss his cheek in order to get his attention and whisper in his ear."
ha "Thank you, Hisao. That was a very memorable first time."
hi "…first …time …Hanako?"
ha "Yes…"
ha "First time making love."

stop music fadeout 3.0
scene black
with Dissolve(3.0)

return