label sh_ch29:
    label .s1:

        $ set_window_tint(TINT_HANAKO)

        scene bg satou_guestroom
        with nextchapter

        play music music_another fadein 4.0

        nvl clear
        nvl show dissolve

        n "I guess these belong to Lilly's parents."
        n "{vspace=60}After we got back from the beach, Hisao went down to the kitchen to get something to drink while I went to our room to put away my diary and brush my hair to get any tangles out. Now I'm holding two bathrobes that I retrieved from the bathroom's small changing area on my way here."
        n "The changing area contained shelves and baskets for clothing, but I doubt we'll be slipping back into our clothes again after we're done bathing, so I might as well leave my clothing here. I just hope Lilly or her parents aren't going to miss the bathrobes this evening."
        
        play sound sfx_rustling

        n "{vspace=30}I walk up to the window, close the curtains, take off my clothes and put one of the bathrobes on. Both are a little bit too large for me, though, since I'm used to wearing a rather oversized nightgown, it doesn't feel too awkward."
        n "I fold my clothes over one of the chairs, leave the bedroom and make my way over to the bathroom."

        nvl hide dissolve

        scene bg satou_changingroom
        with locationchange

        nvl clear
        nvl show dissolve

        n "Two of the changing area's walls look suspiciously like reinforced room dividers, suggesting that the bathroom and this tiny changing area used to be part of the same room before the Satous moved in."
        n "I conclude with a sense of relief that the outer door can be locked from the inside, meaning that even if Lilly or her parents were to come home early there'd still be no risk of them accidentally walking in on us."
        n "In addition to a shelf with baskets for clothing and a space for shoes along one wall there are two cabinets near the exit; one containing bottles of liquid soap and several types of shampoo and the other containing washcloths and towels. I take two of each, making sure to get a bottle of shampoo for myself that contains conditioner and suits my hair and then slide away the inner door and enter the main bathroom."
        
        nvl hide dissolve

        scene bg satou_bathroom
        with locationchange

        nvl clear
        nvl show dissolve

        n "While it's certainly not as large as the public baths I've visited in my childhood, it's definitely larger than any bathroom I've ever been to before. The floor is covered with slightly rough tiles to avoid slipping."
        # n "On the far wall is a fairly large window with sun blinds in front of it. The wall near the bath consists of a large tile mural depicting a few large waves in front of a mountain. The bath itself seems large enough to hold about seven or eight people."
        n "On the far wall is a fairly large window with sun blinds in front of it. The bath itself seems large enough to hold about seven or eight people. The opposite corner of the room consists of facilities to clean oneself before bathing. Two pairs of faucets are attached to the wall in that part of the room, and each pair also has a detachable shower head connected to it. There's a small mirror on the wall above each pair of faucets and a pair of wooden buckets and low stools nearby. The floor near the faucets and shower heads seems to be slightly sloped so the water can flow into the drain near the corner."
        n "{vspace=60}After putting the soap and shampoo near the stools and leaving the towels on the edge of the bath, I examine the bath a little closer and notice a few small buttons and a display embedded into part of the edge showing a number."
        
        nvl hide dissolve

        "45 degrees. That's much hotter than I can probably handle. I wonder whether this is the default temperature or if Hisao set it to that level."
        "I hope my preferred temperature doesn't feel too cold for him..."
        "I press the button with a minus sign on it a few times until the display shows 37. That's probably a more responsible level for me."
        hi "Pretty impressive, isn't it?"

        show hisao basic_smile_bath:
            center
            xanchor 0.5 xpos 0.7 alpha 0.0
            ease 0.5 center alpha 1.0
        with Pause(0.5)

        show hisao at center:
            alpha 1.0
        with None

        "I turn around and see Hisao entering the room wearing the bathrobe I left in our bedroom."
        "He gives me an expectant smile and walks back into the changing area. I meekly follow him."

        scene bg satou_changingroom
        with locationchange

        ha "Ummm... D-did you lock the door?"
        hi "When I came in. How's the temperature? There's a panel near the door we can use to turn the room's heating up."
        "Hisao probably used that already since it's pleasantly warm in here. When we take off our bathrobes, it probably won't be the temperature that'll make me feel uncomfortable."
        ha "It's... probably w-warm enough."
        hi "How about the light? I noticed that the light switch has a dimmer."
        ha "Hmmm..."

        scene black

        "That might make things easier. I play around with the slider a bit until ultimately simply turning off the lights, leaving the changing area in near pitch blackness."
        hi "Err... Hanako... I think we're going to need some light, or we'll be setting ourselves up for some very painful pratfalls."

        nvl show dissolve
        n "{vspace=60}I feel my way over to the inner door and slide it open. While the changing area is pitch black, the bathroom itself is only moderately darkened due to it still being light outside and the sun blinds in front of the window letting more than enough light through to make out the room's interior."
        nvl clear

        hi "I guess we'll be okay after all, at least until the sun sets completely."

        "He puts a hand on my shoulder."

        play music music_dreamy

        hi "So... Shall we?"

        ha "G-Go ahead."

        nvl show dissolve
        n "{vspace=60}I hear some rustling next to me, and a few seconds later Hisao, now completely naked, strolls past me, heads over to the washing area, sits down on one of the stools next to the faucets, reaches forward and starts filling up the wooden buckets, occasionally testing the temperature of the water inside them with his finger."
        n "{vspace=60}I find myself staring at him for a moment, then let out a soft sigh. I guess it's too late to start having second thoughts."
        n "{vspace=60}I remove my bathrobe, slowly approach Hisao and sit down on the stool next to him. I appreciate the fact that he's been considerate enough to let me sit on his right so my scarred side is facing away from him."
        nvl clear

        scene bg satou_bathroom
        show hisao basic_smile_nak_close

        hi "Is this close to the right temperature?"
        "Without looking at me, Hisao moves one of the buckets to his right and I dip my finger in to check the temperature. It could be a little hotter; I don't want to start feeling chilly when we're in here for a little while."
        "I add hot water until the temperature is acceptable, pour the contents of the bucket all over myself and then start refilling it while quietly watching Hisao do the same."
        "We repeat this process a few more times, and when we're both completely drenched, Hisao turns in my direction."
        hi "Can you hand me a bottle of soap and shampoo?"
        ha "O-Okay."
        "I take a bottle of each from the small shelf nearby where I put them earlier, pass them to Hisao and then take of bottle of both myself."
        "I guess I'd better get started quickly, because something like this usually takes a long time."
        ha "Hisao?"
        hi "Yes?"
        ha "When you're f-finished, you can go ahead and enter the bath."
        hi "Even when you're not finished yet?"
        ha "Washing my hair usually takes a long time."
        hi "Yeah, I bet it does."

        "A slightly uncomfortable silence follows. What do you talk about in situations such as this?"
        hi "Hey, Hanako?"
        ha "Yes?"

        show hisao basic_grin_nak_close

        hi "Can I help you... you know... wash your hair? I can wash your back too if you don't mind. I'll let you wash mine in return."
        ha "Ah..."
        "I blush a bit. I didn't expect him to offer that. It might not be a bad idea, provided we can limit ourselves to just washing. It might actually be enjoyable."
        ha "Ah... O-okay then. But c-can I... w-wash you first?"
        hi "Be my guest."

        scene ev soapopera_hisao_backwash

        "I put down my stool behind Hisao, sit down and ready my washcloth before deciding it might be more fun to proceed without it."
        "I unhook the shower head from the nearby wall, turn it on and briefly spray his back and his hair. I then put some liquid soap into my hands, rub them together for a moment and start soaping his back."
        "I tenderly stroke his shoulders and upper back, occasionally pausing for a second to apply some more soap to my hands."
        "He exhales sharply as I move my hands down and playfully stroke his sides and armpits with my fingers."
        hi "H-Hey! No tickling."
        "I giggle at the cuteness of his response."
        hi "Just remember I'll be in a position to return the favor later."
        ha "Okay then."
        ha "Hisao... could you... l-lean back a bit?"
        hi "Huh?"

        scene ev soapopera_hisao_hairwash

        "He seems puzzled for a moment, but then complies and carefully starts leaning backwards."
        "I use my hands to guide him until he's leaning against me with the back of his head resting against my chest. We both let out a slightly nervous laugh."
        hi "Is this really okay?"
        ha "J-Just relax."
        "It's a bit of an odd feeling to be in this position, but it's also rather intimate."
        "I carefully get some shampoo from the bottle nearby, apply it to my hands and then start running my hands through his hair, gently massaging his scalp in the process."
        "We stay like this for several minutes, neither of us saying a word the whole time, but the silence doesn't feel uncomfortable. I'm just happy carressing him like this, and he seems content to let me."
        "Eventually, after deciding I'm done, I get a shower head and wash the shampoo out of his hair. Afterwards he sits up and looks at me from over his shoulder to indicate it's my turn."
        "Suddenly feeling a little self-concious, I cover my genitals with one hand and use my other arm to cover my breasts as much as I can, drawing a small amused smile from him."
        hi "Hanako, could you turn around and face the other way?"

        scene ev soapopera_hanako_backwash

        "I do as he asks, separate my long hair into two halves and drape it over both shoulders, exposing my back."
        "With my hair no longer partially covering the scars on my back I feel even more exposed than before, but my anxiety slowly starts ebbing away when Hisao sits down behind me and starts rubbing soap on my back and shoulders."
        "My upper back hasn't been very sensitive since my accident, but his touch nevertheless feels good in the places where I can feel the sensation."

        scene ev soapopera_hisao_hairwash

        "After finishing my back and shoulders he gently pulls me backwards until I'm leaning against his chest. I turn my head a bit so I can listen to his heartbeat - something that always manages to put me at ease."
        "I close my eyes and try to relax as his hands start rubbing and stroking the top of my head."
        hi "Uh... Hanako?"
        ha "Yes?"
        hi "I... uh... don't really have much experience washing hair as long as yours."
        "I giggle at his uneasiness."
        ha "Shall we... s-split the workload?"
        hi "Split?"
        "I take the half of my hair that's draped over my left shoulder and swing it back. He carefully takes the ends of it in his hand."
        hi "I guess I'll do this part then. Wow, it's kind of heavy when it's wet. Doesn't that strain your neck?"
        ha "I'm used to it."
        "I can't help but smile. I have to admit that his sudden curiosity about my hair is more than a little endearing."
        hi "I'll just watch and do what you do then."

        "I take the ends of my hair in my hands and start massaging the shampoo into them, carefully working my way up from the bottom."
        "I've done this often enough to be able to do it in my sleep, but this time I deliberately slow down a bit so Hisao can see how it's done."
        "If he messes this up, I'll have two distinct halves of hair tomorrow. That'd be a real problem."
        hi "Man, long hair can be a real chore to maintain."
        ha "You get b-better at it after a while."
        hi "Hanako?"
        ha "Yes?"
        hi "I was wondering... Have you always had your hair this long even before your... accident?"
        ha "It... used to be just a little bit shorter when I was little, but I had my hair longer than shoulder-length even as a child. My..."
        "I hesitate for a moment, not sure whether to smile or feel sad at the resurfacing memory."
        ha "My m-mother r-really liked my hair. She h-had hair j-just like mine. We'd always bathe together and she'd take her time washing it and telling me how b-beautiful she t-thought it w-was."
        hi "I think it's very beautiful as well. It's pretty eye-catching too."
        ha "R-Really?"
        hi "Yeah. That day when Mutou introduced me to the class, you were the first student in class I took notice of. Your hair was probably the reason why."

        nvl show dissolve
        n "{vspace=60}I'm not sure how to feel about that. I don't really like any part of me to be considered eye-catching, because trying to avoid standing out has always been part of my survival strategy, but to hear Hisao say that I was the first person he took notice of in class and to hear him say that he considers my hair beautiful nevertheless makes me very happy."
        nvl clear

        ha "Umm... T-thanks."
        "Truth be told, I really like my hair as well. Covering myself up with it makes me feel safe, as if I have my own personal protective cloak. Well... hardly completely safe but just a little bit safer."
        hi "Hanako?"
        ha "Yes?"
        hi "This may be a weird question, but... About your hair, do you... err...?"
        "I suppress an amused giggle at his awkwardness. I think I have a pretty clear idea of what he wants to ask."
        ha "In the o-orphanage, one of the staff would cut my hair, so I w-wouldn't need to go to a barber. Eventually, I l-learned how to cut it myself."
        hi "Wow, really?"
        ha "Yes."
        "What I don't say is that it was out of necessity. Going to the barber and exposing my facial scarring would be one of those things I could lose sleep over for days in advance."
        hi "You're a girl of many talents, Hanako."

        "He drapes the hair he was tending to back over my left shoulder, embraces me from behind and kisses me on the cheek. Then he just holds me for a little while."
        "Eventually, after determining that the conditioner must have had enough time to do its thing, I take the shower head and use it to rinse the shampoo away."
        "I guess this is the point where we'll soap up the rest of our bodies. Or maybe..."

        hi "...Hanako?"
        "Just when I'm about to dismiss the thought I just had, Hisao puts his hand on my shoulder. I'm willing to bet he had the exact same thought I just had and unlike me he didn't think it was too inappropriate to suggest."
        ha "Y-Yes?"

        play music music_heart

        hi "Can I... soap your front as well?"
        ha "M-My f-front?"
        hi "I... liked washing your back."
        ha "...If... If I can w-wash y-your f-front as well."
        hi "Sure."

        scene ev soapopera_hisao_bodywash

        "I think I can see the traces of an awkward smile on his face as sits in front of me, using his hands to cover himself in order to prevent things from being too awkward."
        "I retrieve the soap, put some of it in my hands and start running my hands up and down his legs and feet, then move behind him and continue on his arms."
        "While I'm busy soaping his shoulders, I suddenly become aware of his gaze towards the nearby wall-mounted mirror, making me a little uncomfortable."
        "Despite the room being dimly lit, our reflections are still clearly visible and I can tell he's watching me."
        "Since I can't cover myself up and wash him at the same time, I gently nudge his chin away with my finger and kiss him from behind."
        "Keeping him occupied this way, I reach down, pour some more liquid soap into my cupped hand and then start on his chest, paying special attention to the scar in the middle."
        "I feel his breathing speed up as my hands go lower and lower, rubbing his thighs and abdomen before stopping at the place his own hands are covering."
        "I break off our kiss and exchange an awkward look with him. I wonder if this is one spot he wants to do himself."
        ha "Uh, Hisao... D-do you... uh...?"

        "My boyfriend lets out a nervous laugh and then moves his hands away. My eyes grow large, and I barely manage to suppress an uncomfortable giggle."
        "The sights and sensations of our act have left his manhood completely erect and my mere glance is enough to make it quiver a bit."
        hi "I guess this was kind of inevitable..."
        ha "Uh..."
        hi "Hanako, could you... uh... help me with this before we get into the bath?"

        scene ev soapopera_hisao_handjob

        "I blush heavily, but nevertheless find myself nodding. I apply some extra liquid soap to my hands and then I take hold of him, wrapping my other arm around him from behind."
        "I start kissing him once more, moving my hand as I do so. I consider slowly building things up, but by the way he's thrusting his hips I don't think he's in need of a warm-up at this point."
        "I tighten my grip a bit and move my hand up and down his length in tandem with his thrusts. I think I'm getting pretty excited myself from the reactions my caresses are drawing out of him."

        "Hisao probably had a point just now. When a girl and a boy who haven't been together for all that long get together in a bathroom, stuff like this is probably bound to happen."
        "I'm actually a little bit surprised that he didn't suggest doing it with me right here and now."
        "Maybe he was thinking the same thing I was: the only options we'd have here would be doing it on the bathroom floor or in the bath itself."
        "The first option probably would have been rather uncomfortable and the second option would have been a really bad idea."

        scene ev soapopera_hisao_climax

        "I keep going, kissing his neck and cheek, using one hand to pleasure him and letting the other one roam across his chest and tummy until I can tell that he's nearing his limit."
        "Deciding to end things with a bang, I press myself against him even more tightly and start using both hands while rubbing myself against his back."
        "Since he's still covered with soap, it goes really smoothly, and I have to admit it feels pretty good to me too."
        "Both his breath and his movements grow faster and faster, and I enthusiastically adjust the speed of my own movement, pushing my hips forward in order to add a little bit more force to his own thrusts."
        "Suddenly, he exhales sharply and makes several jerking motions with his hips."

        scene ev soapopera_hisao_cleaned

        "I wait until his climax has subsided and then hold him in a tender embrace until I can feel him relax."
        "After letting go of him, I take one of the nearby showerheads and use it to wash my hands."
        "Then I place my hand on his chest until his nod tells me that he's alright and use the showerhead to get the soap off, wash the evidence of our activity down the nearby floor drain and clean him from head to toe."
        "As I turn off the water, my boyfriend smiles at me."
        hi "Thanks, Hanako. That was really good."
        "I fidget a bit upon hearing his praise and then simply nod my head. This is not a subject I want to get into a back-and-forth with him over."
        "I guess it's my turn next."

        scene ev soapopera_hanako_bodywash

        "I'm not really sure what to do now, so I simply remain seated and wait until Hisao comes over to me, sits down behind me and wraps his arms around me."
        hi "You can lean into me a bit, Hanako."
        "I do so and try to relax as much as possible as he takes the bottle of soap, pours some into his hands and starts rubbing it onto my arms and shoulders."
        "I barely manage to hold back a giggle when he playfully tickles my left armpit. I don't think a simple washing is all Hisao wants to give me."
        hi "Can you move your right leg just a little bit, Hanako?"
        "Feeling a little bit flustered, I open my legs a bit and let him wash them though I quickly cover up my intimate area with one of my hands when he approaches my inner thighs."
        "He moves on to my tummy and sides without breaking stride, but pauses for a moment when he gets near my chest. Then he gently tucks my chin up with his finger."
        ha "Hisao..."
        "My voice is cut off when a shower of kisses descends on my left cheek and neckline. I'm so distracted by this that I barely notice how his hands are massaging my breasts, covering them with soap."
        "Not content with just that, his hands proceed to carress my chest."
        "First he merely traces my breasts with his fingertips, but then he holds them in the palm of his hands before fondling them and kneading them, his fingers feverishly stroking my nipples."
        ha "Mmmmmmmm!"
        "Encouraged by my restrained moan, he slowly, but steadily moves his hand downwards. He has almost reached my private area when I suddenly think of something and quickly grab his hand."
        ha "W-Wait!"
        hi "You... eh... don't want me to...?"
        ha "There's... uh... s-soap on your hands..."
        "Soap I'd rather not accidentally have forced inside me."
        hi "Oh... right."
        "He moves away, takes the showerhead that I used to clean him, turns on the faucet and washes the soap off his hands. Then he kneels behind me again and hugs me once more, softly kneading my breasts for a second time."
        "Now his hands are covered in soap again."
        ha "Uh... Hisao?"
        "I hear him chuckle."
        hi "Yeah, I know. Maybe I should simply do it without using my hands."
        "Huh?"

        scene ev soapopera_hanako_showerhead

        "Still fondling one of my breasts with one hand, he picks up the showerhead and aims the water spray at my chest."
        "I gasp for a moment when one of the jets of warm water hits my nipple for a moment. Looks like I'm still pretty sensitive from his touch earlier."
        "His hand slides downward and gently spreads my legs."
        ha "H-Hisao?"
        "His only response is another quick peck on my cheek."
        "Just when I'm about to ask him what he meant with that earlier comment, his other hand moves downward as well and the warm sensation that was focussed on my chest earlier is now emanating from between my legs."
        "My body jumps a bit as my most intimate place is suddenly stimulated by several narrow streams of water at the same time."
        ha "H-Hey!"
        "This is... a pretty new sensation. It's different from when he uses his fingers. The fact that the stimulation is continuous is... not bad at all."
        "Hisao's other hand moves up again and goes back to fondling my stomach, chest and collarbone. As I endure this strange new experience, I try to focus on the feeling in my chest since it's the more familiar one..."
        ha "Mmmm..."
        "...which becomes harder and harder as the sensation from the water continues and starts feeling better and better, and I start getting more and more aroused because of it."
        "And then he turns the switch on the side, disabling the smaller jets and turning on the stronger stream from the holes in the center, which intensifies the sensation even more."
        "I start panting, my body reacting strongly to the stimulation."
        "The place between my legs starts feeling extremely warm, hot even, but it's not due to the temperature of the water."
        "I can't believe this is happening."
        "He moves the showerhead even closer to my sensitive spot, making the sensation even more overwhelming than it already was. A moan of pleasure escapes from my lips."
        "I don't think I'll ever be able to look at a showerhead again without blushing."

        "My legs and thighs have now started trembling from the pleasure."
        "My breathing comes out in sharp gasps as the non-stop sensation rapidly drags me towards my limit. My moaning is starting to get audible above the sound of running water."
        ha "Mmmmmmm!"

        scene ev soapopera_hanako_climax

        "I squeeze my eyes shut and grit my teeth in an attempt to brace myself."
        "And then the climax hits me; several jolts of intense pleasure that cause my body to shudder uncontrollably. It's like a white light flashes brightly in the back of my head."
        "I let out a whimper of ecstasy before I can control myself."

        scene ev soapopera_hanako_cleaned

        "After the last shock has passed through me, I instinctively push the showerhead away and let out a long, deep sigh."
        "Hisao turns off the faucet and just sits there holding me for several minutes until my heartbeat and breathing have returned to normal."
        "Then he turns the showerhead back on and washes me all over. When the last traces of soap have been rinsed off, he turns off the water, gets up and looks at me."
        hi "Hanako, can you stand?"
        ha "Y-Yes."

        scene bg satou_bathroom
        play music music_serene
        show hisao basic_smile_nak_close

        "He extends his hand towards me, I take it, and he pulls me up. My legs are still a bit shaky, but the small distance to the bath shouldn't be a problem."
        "Hisao gets in the bath ahead of me and takes my hand. He helps me in, and then we sit down and huddle together in one of the bath's corners."

        scene ev sharedsoak_hisao_lean

        "We let out a long mutual sigh as the warm water envelops us."
        "This feels so good."
        "I lean against Hisao and let my head rest on his shoulder. I'm suddenly starting to feel really sleepy. Today was a long and eventful day."
        "I got up early in the morning, we took a trip that lasted for most of the day, and then there's the overload my senses experienced minutes earlier."
        "All in all, I'm pretty tuckered out right now and slipping into a warm bath feels like the epitome of relaxation."

        scene black
        with shuteye

        "I close my eyes and try to empty my mind, focussing only on the comfort of every single muscle in my body relaxing in the warm water. I feel Hisao's head tilting and leaning against mine."
        "I guess he's pretty worn out as well. That's fine though. We can stay in here as long as we like. There's nobody else around, and we have all the time in the world right now. What more could I possibly want?"
        "For a long time, my mind keeps floating in the place between slumber and awareness, content to just relax and enjoy the warmth all around me and I find myself losing track of time."

        scene bg satou_bathroom

        "When I feel Hisao shifting a bit, I open my eyes and the first thing I notice is that it's slightly darker than before. I wonder how long we've been in here already."

        show hisao basic_grin_nak_close

        "When I take my head off Hisao's shoulder, I feel him turning towards me."

        hi "Good morning, sleepyhead."
        ha "I... wasn't asleep. Just... relaxing a bit."

        show hisao basic_smile_nak_close

        hi "I might have dozed off myself a little as well."
        ha "I think it's a little darker outside than it was before. Do you know what time it is?"
        hi "I don't know... or care. I don't have any further plans for the evening, so we can stay in here as long as we like."
        ha "I'd like to stay here for a bit longer. The water's really comfortable."
        hi "Glad to hear that."
        ha "Ummm... Hisao?"
        hi "Yes?"
        ha "Is it... comfortable for you too?"
        hi "Sure."
        ha "But... y-you like your baths hotter, don't you?"
        hi "Only a little. That doesn't mean the current water temperature is uncomfortable. Far from it."
        ha "S-Sorry."

        show hisao basic_speak_nak_close

        hi "Hey, don't be like that. Like I said, it's still a very nice temperature. And the last thing I want is for you to get unwell again."
        ha "I'm... s-sorry about last week."
        hi "I'm sorry too."
        ha "Huh? W-Why?"
        hi "When we came back from that picnic last week and you went to get some rest after dinner, Lilly's mom approached me and asked me if you were prone to heat illnesses."
        hi "She said... uh... burn victims are sometimes more vulnerable to them than most people. I... ah... didn't really know how to answer that."
        hi "She then told me that I should keep an eye on you during warm days so you wouldn't get unwell again."
        "I already thought it suspicious that nobody ever brought the subject up again after that day. I shouldn't have been surprised that it was discussed without me present."
        ha "I'm sorry. I d-didn't mean to cause trouble."
        hi "It's fine. I felt a bit stupid though. I always overlooked the fact that maybe your... injuries came with some catches of their own."
        hi "I kind of feel I should have made an effort to learn about them. Either by reading up on the subject or by simply asking you."
        ha "W-Why?"
        hi "Well, you're keeping an eye on me too. You even followed a first aid course to be better suited to watch over me. I feel I can't do anything less."
        "That's not a bad point. We're supposed to look out for each other. I never really talked to him about my burn injuries because I don't like talking about them in general. But after hearing what he said just now, I feel that it's not him who ought to apologize for dropping the ball, but me."
        ha "You d-don't need to apologize. I... probably should have told you."
        hi "I'm willing to listen at anytime you're willing to talk."
        ha "N-Now?"
        hi "Only if you're comfortable with it."
        "I don't think I'm very comfortable with it, but I would like to get it out of the way, and I'm feeling fairly comfortable right now."

        scene ev sharedsoak_hisao_talk

        ha "There's... n-not really that much to tell. There are a few minor things like... ummm..."
        "I think for a moment."
        ha "My scars are usually r-really dry and stiff in the morning. I often have to do a few... stretching excercises after I get out of bed."
        hi "Because scarred skin can't produce sebum?"
        ha "Is... that's what it's called?"
        hi "Uh, yeah."
        ha "I... often use m-moisturizing cream to make them a bit more supple."
        hi "Yeah, I noticed the bottle in our room. But you usually don't put it on until you're ready to get dressed, do you? I mean, we've slept in several times this week..."
        ha "S-Sometimes it's more noticable than other times. I only put it on immediately if it itches too m-much when I wake up."
        hi "Speaking of your scars being dry... That's kind of what that incident last week was about, wasn't it?"
        "I nod."
        ha "Scars... c-can't sweat either, so when the weather's warm or I... exhaust myself, it takes me longer to cool down again."
        "Though my physical condition really could have been better that day as well. Lilly's mother was probably right and part of the problem was the fact I wasn't even properly rehydrated to begin with."
        hi "What happened that afternoon, has that happened to you before?"
        ha "A... few times... in the past. But it hasn't happened in a long time, not counting last week."
        hi "Hmmm..."
        ha "Y-Yes?"
        hi "Hanako... maybe this is a silly question, but is there any risk of you... uh... 'getting overheated' when we sleep together?"
        "I giggle. Is this how it's going to be from now on? Two people exchanging an 'are you alright' after each time they sleep together?"
        ha "I've b-been fine so far. I think... if you can handle what we do, I can handle it as well. So please don't worry about me."
        ha "Besides... c-cooling down just takes me a little longer. It's n-not like I can't s-sweat at all anymore..."
        hi "Yeah, good point."

        nvl show dissolve
        n "{vspace=60}There's a brief silence that's slightly uncomfortable. At least Hisao was diplomatic enough to stick with a generic answer."
        n "{vspace=60}I suppose I should be grateful that I still have enough functioning sweat glands to engage in modest physical activity without fainting or killing myself, but the annoying thing about having less sweat glands than usual is that the ones I do have have to work overtime in order to compensate, which can lead to some extremely unladylike results."
        n "{vspace=60}Hisao surely must have noticed already that during our activities in bed, part of me always remains almost completely dry while the other part is sweating like a pig. Thank goodness we always do it without any clothes on."
        nvl clear

        ha "Umm... you know... I used to like my baths a little hotter than this too, but ever since... my accident... I've been a room-temperature person."
        ha "Hot and cold temperatures just quickly feel... uncomfortable to me now. Umm... S-scar tissue doesn't isolate as well as normal skin."
        hi "Yeah, I thought so."
        ha "That's m-most of it. If... it wasn't for my appearance, the s-scars would probably only be a minor inconvenience in everday life."
        hi "Okay. Thanks for telling me."
        ha "P-Please don't go worrying about me."
        hi "I won't if you promise not to worry about me too much."
        ha "O-Okay."

        scene ev sharedsoak_hisao_lean

        "The conversation having reached its end, we fall silent again, though the silence is comfortable this time. I feel Hisao's hand sneaking up my arm and shoulder, and he starts running his fingers through my hair."
        "I sigh contently and snuggle up to him a little more."
        hi "It's still really nice in here, isn't it?"
        ha "Yes."
        "My boyfriend chuckles."
        hi "Maybe we simply ought to spend the night here."
        "I giggle."
        ha "W-We shouldn't. Lilly and her parents would think we're strange."

        scene ev sharedsoak_hisao_talk

        hi "If they'd even notice. Lilly's mom's usually away from the home the whole day unless she's taken a day off, and I've barely seen Lilly's dad at all."
        ha "I... spoke with him this morning. In his study."
        hi "You had a conversation with him?"
        ha "Not for very long. But... he did tell me that if we wanted to read any of his books, we could borrow them."
        hi "You mean the contents of that bookcase in the study? I figured they were books on business or heart equipment and stuff."
        ha "No, almost all of it is fiction. And it's all in Japanese too. He has a very impressive collection. You should have a look at it tomorrow."
        "Hisao grins at my failure at hiding the excited tone in my voice."
        hi "So he's your hero now?"
        ha "N-No, but it's a very generous offer."
        hi "Yeah, it is. I might check it out when I have the opportunity. Did he say anything else?"
        ha "He told me I should make use of the bathroom if I liked an opportunity for a traditional soak. I was actually already c-considering giving it a try before you came and invited me to have one together."
        hi "Well, that was some good advice then."
        "My thoughts return to the last words he said."
        ha "H-Hisao...?"
        hi "Yes?"
        ha "He also... t-thanked me... f-for looking after Lilly."
        hi "Huh?"
        ha "Y-Yes."
        hi "Well, that's kind of ironic, seeing that she's really been looking after us, in a manner of speaking."
        ha "That's what I thought too."
        hi "I suppose you didn't... correct him?"
        "Are you crazy?"
        ha "N-No."
        hi "You didn't tell Lilly about what he said, did you?"
        ha "No. I think she'd be upset, and I d-don't want to complicate things between them."

        hi "There was a similar thing during that picnic last week, wasn't there?"
        ha "You noticed that too?"
        hi "Uhuh. Well, Akira did say that Lilly wasn't very independent when their parents left Japan. Still, seeing them be this out of touch with Lilly kinda suggests some estrangement with a capital E, don't you think?"
        ha "I... d-don't know. I think the situation is... just r-really complicated."
        ha "Lilly's parents seem... v-very busy all the time, Akira is... rather hostile towards them and is k-keeping them away and Lilly's... floating somewhere in between them."
        hi "Sounds like she has her work cut out for her, huh?"
        ha "Yes. I wonder if there's anything we can do to help."
        hi "I don't think we should meddle in this. Obviously a lot of stuff happened in the past, and we don't know anything about that, so getting involved would just mean getting in over our heads."
        ha "I know..."

        hi "I don't think Lilly came here expecting to undo six years worth of estrangement in only a few weeks."
        hi "I think she simply meant this to be a beginning of something. Something she wants to maintain with weekly phonecalls while she's in Japan."
        hi "This is probably a long-term thing to her. At least, if she's realistically-minded, it should be a long-term thing to her."
        ha "Yes, you're probably right."
        hi "Her mom's already taken quite a bit of time off to spend with her, and her dad said he'd try to get some time off at the end of the week. It's a modest start, but it's still a start."
        hi "I don't think we need to do anything. Well, except maybe hang out and have fun with Lilly whenever she feels like it. But we're already doing that. And we'll just keep doing that, right?"
        ha "Yes! We will."
        hi "In the meantime, seeing that Lilly's not here right now, there's no point in worrying about her. Let's focus our attention on something else, shall we?"

        scene ev sharedsoak_hisao_cuddle

        "I smile as he wraps his arms around me waist and pulls me onto his lap."
        ha "Umm... l-like what?"
        "He snickers and gives me a kiss on the cheek."
        hi "We could... I don't know... go out onto the beach and count how many pebbles there are..."
        "I turn around and smilingly shake my head."
        hi "...or we could... like... go to the yard, draw some squares on the ground and play a game of hopscotch..."
        "I giggle, shake my head again, and we share a kiss. Ever since he embraced me, my desire's been steadily rising."
        hi "...or we could simply return to our room and... well... you know..."
        "I smile, eagerly nod my head, and we share another kiss. Then I let my forehead rest briefly against his. A quick peck on my lips seals the deal and I get off his lap."

        scene bg satou_bathroom

        "I feel a bit dizzy upon getting up, so I quickly sit down on the edge of the bath until the feeling passes."
        "We get out of the bath, dry ourselves off with the towels I left nearby and then carefully, walking hand in hand, make our way back to the changing area."

        scene black

        "The bathroom itself was already pretty dark, but the changing area is pitch-black. Nevertheless, we manage to find the bathrobes we left here with relative ease, and after putting them on, we quickly walk back to our bedroom."

        scene bg satou_guestroom

        "We enter, and I waste no time in locking our bedroom door. Not that I expect anyone to come in here unannounced, but better to be safe than sorry."
        "When I turn around, I notice Hisao has already turned on a small lamp on one of the nightstands, bathing the area in a light that's just bright enough to see clearly, but still dim enough not to make me feel too uncomfortable."

        show hisao basic_smile_bath_close

        "I notice there's a bit of a nervous expression on his face as he sits down on the edge of the bed. Feeling a little awkward myself, I sit down next to him on his right side and wait for him to initiate the next step."
        ha "..."
        hi "..."
        ha "H-Hisao?"
        hi "Uh... Want to cuddle a bit first?"

        "That's a bit odd. When we were getting ready to get out of the bath, the atmosphere was such that I expected him to jump on top of me the moment we set foot in this room, and yet he seems hesitant right now."
        "Nevertheless, I've never said no to a cuddling session before, and I have no intention of breaking that habit. I get a little farther onto the bed and wait for him to make the next move."
        ha "Okay."

        hide hisao

        nvl show dissolve
        n "{vspace=60}He gets closer to me, pulls me into a hug and then lets himself fall backwards, causing me to end up on top of him. The feeling of his hands stroking my scalp and shoulders and the sensation of his ankles rubbing against mine are very pleasant indeed, but every time we make eye contact and I give him an expectant look, he merely gives me a sheepish look back. He's definitely stalling for some reason."
        nvl clear

        "Come to think of it, this situation actually feels familiar."
        ha "Hisao?"
        hi "Yes?"
        ha "Ummm... it's not like this doesn't feel good, but... this... feels a little like last week, d-doesn't it?"
        "'Last week' in this case referring to the evening he convinced me not to go with the usual way of him lying on top of me and give spooning a try, which I actually ended up enjoying quite a lot."

        show hisao basic_smile_bath_close

        "The half-guilty look on his face all but tells me I was right on the mark."
        hi "Heh, perceptive as ever, I see."
        ha "What... were you thinking about?"

        show hisao basic_speak_bath_close
        hi "Just a passing thought."
        ha "..."
        hi "Promise me you won't laugh."
        ha "Okay."
        "He leans in, kisses my ear and then whispers something to me."
        "I don't laugh, just like I promised. That was hardly going to be my first reaction anyway. I merely fall prey to one of the most luminescent blushes I've ever experienced. He wants to do... that?"

        show hisao basic_bashful_bath_close

        "Hisao's awkward look shows that he's already sorry he said anything."
        hi "Eh... On the other hand, never mind."
        ha "Ummm..."
        hi "..."
        ha "..."
        ha "W-Why?"
        hi "Uh... curiosity, I guess. And we just got out of the bath. And... uh..."
        ha "Y-Yes?"

        hi "It's also supposed to feel really good."
        "That's as good a reason as any, I suppose."
        "In fact, it's probably a better reason than any other."
        "It's still extremely embarrassing though."
        "But if it feels really good to him..."
        "It might be worth it."
        "If it feels really good..."
        "As long as I don't mess up, of course."
        ha "Uh... W-what if... What if I m-mess up?"
        "There's a surprised silence on his end. He probably didn't expect me to even consider it."
        "But if it feels good to him..."

        hi "If you mess up, we'll just go back to sticking to what works, and I'll do my best to make it feel extra good to you. And we'll just deny that it ever happened."
        "Denial? Yeah, I guess denial works for me."

        play music music_one

        ha "O-Okay..."

        "Another awkward smile. Let's hope this isn't going to result in mutual regret."
        hi "So... uh... it's probably going to be easiest to take turns, right?"
        ha "Y-Yes. Uh...w-would you l-like to g-go first?"
        hi "...okay."

        show hisao basic_bashful_nak_close

        "I get off him, and we both sit up. I start fumbling with the belt of his bathrobe, taking several seconds to get it loose. He allows the bathrobe to slide off his shoulders and then starts loosening mine as well."
        ha "M-Me too?"
        hi "If it's okay with you."
        "I'm not completely comfortable, but I nod nevertheless."
        "As I let my bathrobe slide down as well and then drop both robes over the edge of the bed, I only hope that the atmosphere isn't going to remain this awkward the whole time."

        "When I turn back towards Hisao, I see an expectant expression on his face. I'm not really that confident myself."
        ha "Ummm..."
        hi "Yes?"
        ha "I... d-don't really know h-how to do this."
        "He lets out an uneasy chuckle."

        hi "I don't either, but... I think it's simply... using your hands... without using your hands. I'm not sure if that makes sense."
        ha "I... I think it does."
        hi "That's probably a good way to go about it."
        ha "Okay."

        scene ev eveningsnack_hisao_look

        "At least I have a general idea now. I give a hesitant nod to Hisao who lies down on his back and then beckons me to lie on top of him."
        "I do so and we share a few kisses and cuddles until my nervousness starts to die down a bit."
        "I suppose it's up to me now."
        "Use my hands without using my hands."
        "Okay then."

        scene ev eveningsnack_hisao_neck

        "I give him one more peck on the lips and then move sideways until I reach his ear. He shudders lightly as I take his earlobe between my lips and start kissing it."
        "His hands wrap around me and stroke my back as I move from his earlobe to his neck and let my tongue do what my fingertips have done several times before."
        "Before moving further down, I suckle gently on the most sensitive part of his neck, making sure not to leave a suction mark. I quietly smile to myself when I think of what comes next."

        scene ev eveningsnack_hisao_chest

        "His chest has been a source of fascination for me ever since he revealed his chest scar."
        "There might be other heart patients at Yamaku, I neither know nor care about that. But as far as I'm concerned, that light horizontal line there is a sight that is truly unique to him."
        "His chest may easily be my favorite part of his body. I love stroking it with my hand or laying my head on it and listening to his heartbeat. Perhaps these acts are my way of reminding him of my acceptance."

        "And now my head is hovering a few centimeters above his chest, the scar in the middle nearly touching the tip of my nose."
        "I give his chest a loving stare and then start planting kisses on it, first slowly, but then faster and faster. Every so often, I briefly pause to listen to his heartbeat before resuming my pampering."
        "Eventually, I look up and see an encouraging smile on his face. He seems to like it so far."
        "Emboldened a bit by this, I move my attention back to his chest and stick out my tongue, letting it travel from his chest scar to his right nipple."
        "I teasingly circle it a few times before flicking it with the tip of my tongue and am pleased by the gasp that follows. I let my tongue wander from his right nipple to his left and start caressing it in the same way."
        "Rewarded with another sharp breath, I decide to step up the pace a bit, I lick one nipple, then move to the other, then back again, sneaking in little kisses near his armpit, side and collarbone on the side."
        "By this time his entire body has started moving underneath me, shuddering at each contact with my tongue and his breathing has grown quick and shallow."

        "I don't think I'd mind going on like this for a long time, but when he gently puts his hands on my shoulders and gives them a few short taps with his fingers, I realize that he's ready for the main event."
        "I giggle a bit as I playfully rub his erect nipples with the tip of my nose and give him one last kiss on the scar located in between them."
        "Then I move downward a bit and kiss him again, lower myself even more and kiss him once more. Laying a trail of kisses in the process, I work my way from his chest, past his tummy and finally down to his abdomen."

        scene ev eveningsnack_hisao_stare

        "When I finally come face to face with his member, I can't help but swallow a little lump in my throat. I've seen it plenty of times before, but never from up close like this."
        "I'm not supposed to... put that in all the way, am I? I'll choke for sure."
        "It's also supposed to feel really good."
        "I shoot an uncertain glance at Hisao's, who's watching me with a mixture of embarrassment and anticipation on his face."
        hi "Just... take it slowly, Hanako. And just stop if you don't like it."

        "I think back on what he said earlier. Use my hands without using my hands. Most of the time, I'd start by simply running a finger or two along. I could do something like that now as well."
        "Leaning on my elbows, I lower myself to his base, my face hovering mere centimeters over his length."
        "I giggle briefly when I see his length twitching ever so slightly whenever I breathe on it. That actually looks kind of cute."

        scene ev eveningsnack_hisao_blowjob

        "I finally take a deep breath, take his member between my fingers, stick out my tongue and touch it against his base. Then I run it along its length, stopping just as I reach the head."
        "I hear a pleased sigh coming from Hisao. It sounds like he likes this and doing this isn't so bad, so I run my tongue along the length of his member again."
        "And again."
        "And again."
        "His breathing has started running in tandem with the caressing of my tongue. Having gained some courage from his reactions so far, I take his member in my hand and gently pull it upright."
        "I notice that the tip is glistening ever so slightly. Forcing my hesitation aside, I lower my head, place a gentle kiss on it and then give it a quick flick with my tongue."
        "As I do so, a faint, foreign smell enters my nostrils. Trying to avoid thinking too hard on this, I start licking the tip some more, each flick of my tongue slightly more forceful than the previous one."

        "While I'm busy tending to him, I suddenly feel a strange sensation in the back of my head, and when my gaze shifts up for a moment, I realize why."
        "Hisao is looking straight at me. He's looking at what I'm doing and how I'm doing it. My head instantly goes into tomato-mode, and my gaze starts jumping between random points in the room in an attempt to evade his."
        hi "Uh... You were doing really well just now, Hanako. It's been great so far."
        ha "H-Hisao... P-please don't look at me."
        hi "Huh?"
        ha "It's... r-really embarrassing."
        "He briefly opens his mouth to say something, but then seems to reconsider and merely nods his head."
        hi "Okay, Hanako. I'll keep my eyes closed."

        "As he says this, he indeed lies back and closes his eyes, leaving me to pick things up again."
        "Feeling a little more at ease now that he's no longer watching me, I lower my head again, part my lips and carefully wrap them around his tip."
        "Not sure how to proceed, I tilt my head a bit and let it rub against the inside of my cheek. I carefully start moving my head a little and get a soft sigh in response."
        "I move my head a little faster in response until I suddenly hear a loud yelp which causes me to quickly pull back."

        scene ev eveningsnack_hisao_grimace

        hi "Ah... B-be careful with the teeth!"
        ha "S-Sorry!"
        "It sounds like his tip accidentally brushed against my teeth. I didn't even notice it myself, but he must have gotten extremely sensitive and just that little touch was painful for him."
        ha "S-Should I...?"
        hi "If you like..."

        scene ev eveningsnack_hisao_blowjob

        "I lower my head again and take him in my mouth once more. This time I try to keep it in the middle of my mouth and away from my teeth."
        "I attempt to keep my jaw as relaxed as possible as I slowly slide up and down."
        "This is hardly the most comfortable act in the world as I have to brace myself at the end of every downward motion in order to prevent myself from letting it slide in too far. I wonder if I'm even doing this right."
        "Hesitantly, I start moving my tongue around a bit."
        "It seems to get him even more aroused than he already was, but my initiative quickly comes to bite me when he suddenly bucks his hips ever so slightly and his member goes in just a little bit past my comfort zone."

        scene ev eveningsnack_hisao_grimace

        "The sensation causes me to immediately pull back again just before I have a sharp coughing fit. He immediately sits up and opens his eyes, a worried expression visible in them."
        hi "Hanako! Are you alright? I'm really sorry."
        ha "I'm... o-okay..."
        hi "Sorry, I didn't mean to do that. It just... happened automatically."
        ha "It's... okay. I'm p-probably just not any g-good at this."
        hi "...Hanako, I... realize this is kind of selfish, but could you try one more time and just focus on the tip this time? Maybe you could get a little more comfortable too."
        ha "How?"
        hi "Maybe you could lie down on your side?"
        "I was about ready to throw in the towel, but the look in his eyes convinces me to give it one last shot. It's not like actual intercourse was something I immediately got right."

        scene ev eveningsnack_hisao_tummypillow

        "I nod, and he lies down again. I lie down on my right side and lay my head on his belly as if it's a pillow. I gently take hold of him again with my left hand and wrap my lips around the head once more."
        "This position is a lot more pleasant than the previous one and I soon become comfortable enough to make little nodding motions with my head while suckling on his tip as if it's an ice cream cone. He lets out a pleased sigh."
        hi "That's... really... good, Hanako."
        "Suddenly, I feel his hands on me, and for a moment I'm afraid he's going to grab hold of my head, but then a warm sensation spreads across the left side of my face."
        "I realize he's stroking my cheek with his fingers while his other hand is gently running through my hair. I'm amazed at how tender and loving his caresses are and how good they make me feel."
        "If we can keep doing things this way, I can probably keep this up until the end."

        "With newfound enthusiasm, I start nodding my head a little faster, using my left hand to rub and stroke his base and my tongue to dance and slide around him."
        "Ever since I first started using my tongue on his tip, a slightly odd taste has been spreading through my mouth, but to my surprise it hasn't even been unpleasant."
        "His taste is slightly salty with just a little hint of sweetness, and while I'm not really sure whether it's pleasant or unpleasant, it's much too mild to really bother me."

        "He keeps caressing my cheek, and it makes me feel so content that I snuggle up against him. I notice that his breathing has become labored, with more and more gasps and sighs in between breaths."
        "I eagerly keep going, the tenderness of his touch and the arousal in his voice filling me with happiness and lust at the same time."
        "I close my eyes to better concentrate on both and for a little while time seems to stop as the motions of my lips and tongue match up with the rhythm of his breathing."
        hi "H-Hanako..."
        "I love the way he's cooing my name. It makes me want to pleasure him even more."
        hi "H-Hanako... aah... I..."
        "He's nearing his limit. The way he breathes, the way he moves, the strain in his voice. He's almost there."
        hi "...almost..."
        "But what am I supposed to do now? Should I keep going? Should I stop? Should I pull away at the last moment? Is he telling me to pull away or to brace myself?"

        "If I pull away at the last moment, that stuff will inevitably be in my hair for the rest of the night. It'll be a nightmare to get it out tomorrow, and I don't want to shower again this evening."
        "If I stop to ask him with him being this close, I'll kill the moment and might ruin his finish. I'm not even sure if I'd be able to get the question out of my mouth."
        "If I keep going until the end and he doesn't want me to, I might gross him out."
        "But if I stop prematurely, I'll have disappointed him, and that's much, much worse than grossing him out."
        "Boys like it when a girl keeps going, don't they?"
        hi "Hanako... I..."

        "Anything but disappointment. I already have his taste in my mouth anyway. Judging from his voice, he's extremely close to the edge."
        "My mind made up, I speed up the pace and go all out on him. My lips and tongue dart across his tip again and again, my left hand moves furiously up and down, and I stretch out my pinky finger for the finishing touch."

        scene ev eveningsnack_hisao_climax

        "Just when my pinky lightly tickles the area underneath his base, several things happen at once."
        "Hisao lets out a loud and prolonged groan, his member starts throbbing violently, his entire lower body starts jerking uncontrollably and his upper body rises slightly despite my head still resting on his belly."
        "My eyes fly open in surprise when the mild taste that was in my mouth before is suddenly replaced by a much different, much stronger taste."

        "My initial plan had been to just swallow it, but I quickly decide against that now. What's overpowering is not so much the taste."
        "It's a lot saltier than what I tasted earlier with just a touch of bitterness, but it's nothing I can't handle. What makes me a little queasy is the texture."
        "It's surprisingly thick and a bit slimy, and I can't shake the feeling that if I swallow it, it'd either get stuck in my throat or crawl its way back up."

        scene bg satou_guestroom

        "As soon as the spasms in Hisao's lower region have died down, I get up and quickly spit the contents of my mouth onto his stomach. Hisao's still too engaged in his subsiding climax to even notice."
        "Staying true to tradition, I lie next to him and place my hand on his chest, feeling his frantic heartbeat slowly return to normal and keeping an eye out for palpitations."
        "Eventually, Hisao's dazed eyes start regaining some focus, and after recognizing the look on my face he gives a careful deliberate nod. I give a reassured smile and a quick peck on the cheek back."
        ha "I'll... go and get something to clean you, Hisao."
        "Without waiting for a response, I walk over to the bathroom area and get some tissues from a box on one of the shelves."
        "We have some tissues in our nightstand drawer too, but I also wanted an excuse to clean myself a bit. I don't think Hisao's going to kiss me like this."
        "I get myself a glass of water and drink it, slowly weakening the odd taste in my mouth until it's gone altogether. I return to the bed and kneel at Hisao's side, using the tissue to wipe his stomach clean."
        "After having cleaned up the little puddle, which was barely large enough to fill a teaspoon, I turn to him and notice he's gotten his bearings back and is now looking at me."

        show hisao basic_neutral_nak_close

        hi "Hanako?"
        ha "Hisao... Did you... like it?"
        hi "Yeah. It's just..."
        "He looks lost for words for a few seconds."

        show hisao basic_speak_nak_close

        hi "Why did you keep going?"
        ha "Huh?"
        hi "I kind of assumed you were going to pull away at the last second when I was about to... I was kind of surprised that you kept going."
        ha "I... t-thought that's what you w-wanted. D-Don't b-boys... like it that way?"

        show hisao basic_grin_nak_close

        hi "Did you read that somewhere?"
        "My shoulders droop, and my smile instantly drops. So it turns out that I guessed wrong after all, and now he's weirded out or even grossed out by me."
        ha "S-Sorry. I thought... I'm r-really sorry."

        show hisao basic_smile_nak_close

        hi "Hey, don't get all apologetic on me. If anything, I should probably apologize to you for not having been clearer. I... uh... don't know if this is a consolation to you, but..."
        "He takes my hand and holds it tenderly."

        show hisao basic_bashful_nak_close

        hi "...as embarrassing as it is to say this, what you just did probably felt better than anything I've ever felt before. It was really, really good."

        "He does look a little awkward upon saying this, but my mood instantly jumps from gloomy to elated and, wearing a huge smile on my face, I lean forward and grab him into a tight, almost savage, hug."
        "He merely chuckles a little at my reaction and then looks into my eyes."
        hi "The least thing I can do is return the favor. If you're up for it."
        "I'm not completed sure if I'm ready to be on the receiving end or not, but I don't want to keep Hisao waiting any longer."
        "I'm also admittedly a little curious after having witnessed how much he got into it, so I ignore the feeling of my heart beating in my throat and lie down in the place where Hisao was lying earlier."

        scene ev eveningsnack_hanako_look

        "I feel a warm sensation all over when Hisao lies down on top of me and mouth a silent 'okay' in response to the expectant look in his eyes."
        hi "Don't be afraid, Hanako. Just... lie back, relax and let it happen."
        "He kisses me and lets his forehead rest against mine for a moment."

        scene ev eveningsnack_hanako_neck

        "I giggle as he playfully rubs his nose against mine before letting his lips wander towards the right side of my face. I can't feel him kissing my cheek, my neck and my shoulder, but I can hear it."
        "Even though my body no longer picks up those kinds of sensations there, him kissing or touching me there still makes me feel warm inside. It's the gesture that matters. The gesture that he's not repelled by my scarred skin."

        "I reflexively close my eyes when he brings up his hands, strokes the side of my face and kisses the spots above my eyebrows. It tickles a bit, and I squeeze my mouth shut in order to suppress a laugh."
        "Then he moves to the left side of my face, and I gasp as I feel his lips and tongue proceed to caress my earlobe."
        "What starts out as a few cautious pecks soon becomes a barrage of kisses with a few playful nibbles thrown in."
        "When he moves his head slightly down and starts relentlessly kissing and licking my favorite spots on my neck, I let out an excited cry and wrap both my arms and my legs around him."
        "My body has started moving on its own, driven into a higher state of arousal with each flick of his tongue."
        "This is so good."

        scene ev eveningsnack_hanako_chest

        "He whispers in my ear to let go of him for a moment, and as I do so, his tongue starts working its way down again, creating a wet trail from the back of my ear across my neck all the way to my chest."
        "He places a wet smooch on my collarbone and then pulls his head back. His gaze wanders from my eyes to my bared breasts, and the look in his eyes is a mixture of excitement and something that almost resembles hunger."
        "He lowers his head again, and I shiver as I feel his breath tickling my nipple. Unable to resist the anticipation any longer, I gently hold his head to my chest."
        "I let out a sigh as his tongue comes into contact with my right breast and starts drawing ever-shrinking circles around its center."
        "He licks my rapidly hardening nipple for a moment and then repeats the process with my other breast. Then he starts using his hand, kneading and groping one breast while licking and suckling the other with his mouth."
        "The sensation feels so good that I arch my back and sway my upper body in ecstasy."
        ha "Ah... Hmmm..."
        "The experience is such a turn-on that I actually feel a pang of disappointment when he pulls away. I feel his tongue on my collarbone again before he draws a thin trail of saliva between that point and my tummy."
        "He places several playful kisses on my belly button and then lowers himself more."

        scene ev eveningsnack_hanako_stare

        "He puts his hands on my upper legs and gives me a look as if asking for permission. I feel the sudden sting of self-consciousness, but manage to keep it at bay for long enough to stiffly nod my head."
        "I cringe visibly as he takes hold of my legs, lifts them slightly and spreads them wide before lying down on his stomach with his face merely centimeters away from my entrance."
        "I squeeze my eyes shut in sheer embarrassment, but I can nevertheless feel his gaze sweeping across my secret place, getting a closer look at it than he's ever gotten before."
        "I've never felt so extremely vulnerable in my entire life, and I struggle against the temptation to close my legs or cover that place up with my hands."
        "I wonder how I smell or taste to him. Will he find it unpleasant? The moment seems to take forever with no sound except for our shallow breathing and no sensation except the maddening feel of his breath against that place."

        scene ev eveningsnack_hanako_forceful

        "Then, finally, his arms wrap around my upper legs, and I feel something warm and wet press hard against my most sensitive spot."
        ha "Hhhhggg..."
        "I grit my teeth as an intense sensation shoots through my lower body."
        "I thought this was going to feel like the attention he gave my chest earlier, but it's much, much stronger than that. Even to the point of being overpowering."
        hi "Just relax, Hanako."
        "A reassuring whisper from Hisao and then his tongue proceeds to jab against the tiny button above my entrance. I try to relax my muscles, but the sensation is much too strong for that."
        "Is this how it's supposed to feel?"
        "I hold still, doing my best to get used to it, but the sensation is so strong it's bordering on pain."

        scene ev eveningsnack_hanako_grimace

        "My hands edge downward until they reach his head, and I let out a sigh of relief when I softly, but firmly push his head away. Hisao looks at me with a worried expression."
        hi "It didn't feel good?"
        ha "I'm... n-not sure... It... s-started getting unpleasant."
        hi "Maybe I was too forceful?"
        ha "M-Maybe."
        hi "Could you... tell me... how you think you'd like it?"
        ha "..."
        "I blush and merely shake my head. I'm already at my limit as far as awkwardness is concerned."
        hi "Can I try something else?"
        "I give a silent nod. I didn't get it right from the start either, so it's fair that I give him a second chance too."

        scene ev eveningsnack_hanako_gentleunsure

        "My body jumps a little when I feel the wetness of his mouth again, but this time it's merely a kiss on the inside of my right thigh, followed by one on my left."
        "He gently works his way to the center again, and I hold my breath when he reaches my lady parts once more, but this time, the intense pressure stays away and what comes in its place is a gentle lapping."

        "As his tongue gently keeps caressing the area around my entrance, my tension slowly starts ebbing away. The sensation feels a little like his hand, except softer, more fluid and... slightly better too."
        "I close my eyes again and try to focus on the sensation once more. This act is still extremely embarrassing, but the feeling is really nice."
        "I feel my pelvic muscles tense up and relax every time his tongue runs up the length of my entrance and a wonderful shudder each time it gently flicks the little place at the top."
        ha "Mgh..."
        "Just lie back..."

        scene ev eveningsnack_hanako_gentle

        "I shift a bit to get more comfortable and try to relax my body as much as possible."
        ha "Mmmm..."
        "...relax..."
        "I block the rest of the world from my mind. All that exists right now are me, him and that sensation."
        ha "Mmmm... hee hee... Mmmmm..."
        "...and let it happen."
        "A blissful smile has appeared on my face as I surrender myself to that feeling, allowing myself to drift along on it."
        ha "Mmmmmm..."
        "My hands take hold of his head once again but without the intent of pushing him away this time."
        "Instead, I start running my fingers through his hair, tenderly caressing his scalp and gently pulling him close now and again in order to make it feel better. My breaths get heavier and heavier."
        ha "Mmg...mmmg..."

        "A moan escapes my lips as one of his hands wanders up my body and playfully strokes one of my breasts. My arousal is rising by the second and my breathing can barely keep up with the tempo of his lapping."
        "An intense heat has started building up between my legs and is now spreading through my entire body. My thought process is getting fuzzier and fuzzier. The embarrassment of our act barely seems relevant anymore."
        ha "H-Hisao..."

        "Encouraged by the way my body is reacting to the stimulation, he moves in closer and wraps his mouth around the upper part of my entrance, massaging it with his lips while his tongue is dancing around my pleasure center."
        "The sensation alone nearly drives me crazy. Almost my entire body is flushed red at this point."
        ha "Ah...."
        "I can feel my limit approaching as his tongue takes me past the point of no return. I grab the bed sheets tightly and arch my back in pleasure as I lose control."
        ha "Ah...ah..."

        scene ev eveningsnack_hanako_climax

        "I reach the edge, but instead of going over it immediately, I keep dangling for several seconds."
        "His arms grab hold of my hips tighter and continue holding me in place as I start squirming uncontrollably and start letting out squeals of delight."
        ha "Ah...ah...ah..."
        "I instinctively grab his head and press it against me. Then all muscles in my lower body forcefully tense up at once, my legs involuntary squeeze themselves together and my upper body lunges forward."
        "The intense pleasure causes me to squeeze my eyes shut and open my mouth to scream, but a quiet, prolonged whimper is all that leaves my throat."
        "And still he keeps going."
        "My body relaxes for a moment and then immediately tenses up again."
        "And again."
        "And once more."
        "Finally, the spasms are replaced by small aftershocks of ever diminishing intensity, and then my body relaxes completely."

        scene black

        ha "Ow! Ow!"
        "Without warning, the sensation of his licking, which he kept up while I was experiencing my climax, becomes painful again and I reflexively push his head away."
        "I faintly hear him apologize, but I'm beyond the capacity to reply. I close my legs completely, roll on my right side, draw my knees up to my chest and let out a long sigh as a profound feeling of bliss descends upon me."
        "My mind wanders in random directions as I recover from the experience I just had."
        "I hear him getting off the bed and heading somewhere. I briefly hear the sound of running water, but it seems to come from very far away."

        scene ev pillowtalk_placeholder_normal

        "I become vaguely aware of the lights being turned off and then I feel him get back in bed, cover me with the bed sheet and hug me. I slowly start becoming more aware again as I feel his breath against my neck."
        "Eventually, I manage to recollect myself enough to open my eyes and turn my head towards him."
        hi "Hanako?"
        ha "Hmmmm?"
        hi "...how was it?"
        ha "...very good."
        "It's pretty dark in the room now, but I think I can see him smile. He tenderly starts running his fingers through my hair."
        hi "No bad taste in your mouth anymore?"
        ha "N-No. You?"
        hi "Naw. It didn't taste bad to begin with. My tongue's kind of tired now, though. Kind of like that time last week when we were trying to find out how long we could keep a kiss going."
        "I giggle at the memory of that little game we played back then. The comparison is surprisingly accurate."
        ha "M-Mine too."
        "My jaw's a little tired as well. Still, for a first time, I don't think we did that badly. We're lacking experience right now, but I wouldn't mind doing this again in the future."
        hi "So we should probably take it easy with the kisses?"
        "I don't say anything back. Instead, I slowly rub myself against him, use my feet to play footsie with his and reach back to lovingly stroke his hair."
        "Hisao's all too eager to respond in kind, letting his hands run across my cheek and tummy."

        "Even though my experience left me tired, I still love cuddling like this. I'm feeling content, satisfied and very happy right now."
        "As our caresses slow down and we start drifting into a peaceful slumber together, my thoughts return on the events of the day and the days that came before it."
        "I'm having a great time right now, and we still have nearly two weeks to go before we have to go back. I don't think this vacation can get any better, but I'm nevertheless hoping that it will."
        "As I drift off to sleep in Hisao's arms, one last thought remains in my mind."
        "I'm really looking forward to tomorrow."

        stop music
        scene black
        with shuteye

        return