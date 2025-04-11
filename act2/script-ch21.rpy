label sh_ch21:
    label .s1:

        $ set_window_tint(TINT_HISAO)

        call sisterhood_timeskip

        play ambient sfx_airport_ambience fadein 2.0 volume 0.5

        scene bg airport_coffeeshop
        show lilly basic_listen_cas at twoleft
        show hanako emb_downsad_cas at tworight
        with Dissolve(2.0)

        play music music_night fadein 4.0

        li "Hisao, did you remember to bring a written statement from the nurse along regarding your medication?"
        hi "It's kinda late to bring that up, isn't it Lilly? If I hadn't, it'd be too late to get one seeing that we're already past the security gate. Anyway, I did remember to pick one up yesterday and the lady at the baggage check-in said she'd make sure everything would be fine."

        show lilly basic_weaksmile_cas
        with chchange

        li "That's a relief. Three weeks worth of medication must be quite a quantity."
        hi "Seriously. Good thing Yamaku has its own apothecary."
        "This morning, our final preparations went off without a hitch, and neither our bus to the train station nor our train to the airport had any delays."
        "We made sure to arrive at the airport three and a half hours before the departure of our flight, since getting around the airport wasn't going to be a quick process."
        "Baggage check-in went well. That was pretty much where things went south though."

        show lilly basic_smileclosed_cas
        with chchange

        li "Do you know what time it is, Hisao?"
        "Getting around the place proved to be a slow process and our odd formation must have turned several heads. Lilly had to be guided, of course, and I was placed in the role of navigator."
        "With Lilly's hand on one arm and her carry-on luggage in the other, I've been leading our little group through the halls of the airport."
        "Clinging to Lilly's other arm was Hanako, head down and hat lowered to obscure her face as much as possible, doing her best to block out the crowd all around us. The crowd didn't even turn out to be her biggest concern this day."
        hi "We still have about 45 minutes until our plane departs, Lilly."
        "Having made it through airport security, we're now sitting in the corner of a small coffee shop near the gate, enjoying a drink and a light meal."
        "The small talk between Lilly and myself is partially to kill time and partially to try and ease Hanako's tense mood."
        "That Hanako would have a tough time navigating the airport was something to be expected—the terminal halls are quite a bit more crowded than the average street in the city, especially during this time of year."

        show lilly basic_displeased_cas
        with chchange

        li "I wonder if we should already head for our gate."
        "During our trek through the main hall, we were suddenly approached by one of the security officials walking around the place who seemed drawn to Hanako in particular."
        "A very uncomfortable pause took place when he walked up to us and then suddenly backed away for a moment upon noticing Hanako's facial scarring, though Lilly was quick to take control of the situation."
        "When asked by Lilly if there was a problem, the guard explained to us that part of his job was to look out for people who were showing signs of unusually nervous behavior, and Hanako's body language caught his attention."
        "We got a profuse apology afterwards, but the damage had already been done."
        "Whenever I cast a sidelong glance at Hanako, I could see her eyes darting left and right as if watching out for other security officers who might see a potential smuggler or someone with some other form of guilty conscience in her."
        hi "Isn't that way too early?"
        "Neither Lilly nor I bothered suggesting to Hanako to try and act more casually. She'd be as likely to do that as she'd be to don a bikini in the middle of the terminal."
        "Both of us are aware she's emotionally in a bad place right now, but we also realize that openly worrying about her will only make her feel worse."
        "We've come this far. The only way out is through and we're counting on the assumption that if we can get Hanako to her plane seat without her suffering a breakdown, she'll have plenty of opportunity to catch her bearings during the flight itself."

        show lilly basic_weaksmile_cas
        with chchange

        li "International flights often start the boarding process about 20 minutes prior to departure. I'd like to be one of the first in the boarding area."
        li "Last time Akira and I got on a plane, we were among the very first people allowed to board. It's a courtesy policy of our airline towards disabled passengers. I see no reason not to take advantage of it."
        li "I would also…"

        show lilly basic_concerned_cas
        with chchangefast

        "Lilly hesitates for a moment."
        hi "Yes?"

        show lilly basic_displeased_cas
        with chchange

        li "I would also like to get past the security gate before a big line forms there."

        show hanako emb_timid_cas
        with chchange

        "This immediately manages to catch, perhaps unsurprisingly, Hanako's attention. She's been quiet the whole time we've been sitting here, but now she looks at Lilly with a look of dread on her face."
        ha "But Lilly, d-didn't w-we already p-pass security?"

        show hanako emb_downsad_cas
        with chchange

        li "I'm sorry, Hanako. But there will be another security check just before we enter the jet bridge."
        "Hanako sighs loudly."

        nvl clear
        nvl show dissolve

        n "When we accepted Lilly's offer to join her on her trip, we were asked if either of us had ever been abroad before. When this didn't turn out to be the case, Akira was quick to point out we'd need to get ourselves a passport in order to accompany her sister."
        n "The process of getting a passport in itself wasn't that big of a problem. The whole thing had to be finished on a very short notice, but thankfully getting a passport doesn't take too long a time in this country and Akira gave us plenty of pointers on how to complete the application process as quickly as possible. Hanako, Lilly and I skipped school the day afterwards in an attempt to get all the necessary steps on our part done before the end of the day."
        n "{vspace=60}Everything went pretty well until it was time to submit the forms and the photos. There was a photo booth nearby, so getting mug shots wasn't a big deal, but we found out that there were some pretty strict guidelines regarding the pictures."

        nvl clear

        n "When Hanako realized that she was expected to have a picture taken that showed a full frontal, unobscured closeup of her face, we could tell that she was seriously considering backing out of the whole trip."
        n "With a lot of effort, Lilly and I managed to convince her to grit her teeth and go through with the whole thing, though it still took over 10 tries before we managed to take a picture where Hanako was able to force herself into keeping a relatively neutral expression on her face. The expression on her face when she submitted her passport photos to the clerk behind the counter was beyond troubled."
        n "{vspace=60}The whole experience made me realize that for Hanako, willingly showing her face to someone was something she considered extremely intimate and she later confided in me that the whole thing very much felt to her like having a nude photo stuck on her passport."
        n "Needless to say, the prospect of having to show her passport to yet one more security guard and getting the almost guaranteed shocked look in return is something that makes her more than a little bit anxious."

        nvl hide dissolve

        "I get up."
        hi "Best thing we can probably do is get it over with quickly."
        "Hanako nods quietly though it's apparent she's not exactly eager about it."
        "As Lilly also rises to her feet, she puts her hand on Hanako's shoulder."

        show lilly basic_weaksmile_cas
        with chchange

        li "Hanako, I realize today has been difficult and confrontational for you, but I'm still really happy that you decided to come along."

        show hanako emb_downsmile_cas
        with chchange

        "For a moment, Hanako allows herself to smile softly."

        stop music fadeout 2.0

        ha "T-Thank you, Lilly."

        stop ambient fadeout 1.0

        if _in_replay:
            return
    
    label .s2:

        $ set_window_tint(TINT_HISAO)

        scene bg plane_cabin
        show lilly cane_smile_cas at twoleft
        show hanako cover_worry_cas at tworight
        with locationskip

        "Flight Attendant" "Your seats are on the left all the way in the back. May I help you with the luggage?"
        "Lilly smiles sweetly at the flight attendant welcoming us aboard."
        li "Thank you, but my friends and I will manage."

        play music music_pearly fadein 4.0

        "As Lilly predicted, the airline allowed us to board the plane before anyone else in economy class and we were all relieved we had the opportunity to get to our seats before the plane started filling with people."
        "It looks like Akira put some thought into picking our seats. A place in the back meant there'd be fewer people around us and Hanako's scarred side would be facing the wall of the cabin."
        "We walk down the aisle with me in the lead, Lilly behind me with one hand on my shoulder, and Hanako following very close behind us."
        "As we get to our seats, three chairs next to each other in one corner in the back of the plane, I turn around."
        hi "Ladies first."

        show lilly cane_smileclosed_cas
        show hanako basic_worry_cas
        with chchange

        "Lilly smiles, but shows no sign of getting ready to sit down."
        li "Akira told me once that one's first plane flight is a very special moment, particularly the first takeoff when you see the land below slowly get smaller."
        li "I think a place near the window would be wasted on me. I believe the window seat should go to the only person who hasn't flown before. I certainly think she has deserved it."
        "That's a good point. Not to mention the fact that having both me and Lilly as a buffer between herself and the rest of the people on the plane will probably allow Hanako to relax a little more."
        "I open the storage compartment above the seats and take Hanako's backpack from her."
        hi "That's you, Hanako. Go ahead and take the seat in the back. I'll put your and Lilly's luggage away."

        show hanako basic_normal_cas
        with chchange

        "Hanako nods and quickly moves to her assigned seat while I put everyone's bag in the storage bin."
        hi "So I guess the second seat will be mine?"

        show lilly cane_smile_cas
        with chchange

        li "Yes. You might still have the opportunity to enjoy the view a bit, assuming Hanako doesn't end up hogging all of it for herself."

        show lilly cane_cheerful_cas
        show hanako basic_bashful_cas
        with chchange

        li "And better still, you'll get to spend the upcoming 12 hours with one lovely lady on each side. I'm sure many men would envy you."
        hi "How can I say no to such a tempting offer?"

        scene bg plane_seat
        with locationchange

        "I take my seat next to Hanako as Lilly folds up her cane, puts it in her bag and sits down in the seat to my left."
        "During this moment, I take a look at my girlfriend."

        show hanako emb_downtimid_cas_close at tworight
        with charaenter

        "As expected, just before we could board the plane, she received another proverbial gut punch in the form of another security gate we had to pass. I can tell the whole thing has taken its toll on her as she's looking gloomy, exhausted, and physically ill."
        "I don't like the fact that we'll have to repeat this hassle again when we arrive in London, but I'm thankful that that moment is still about half a day away. Hopefully Hanako will be able to rest a bit during the flight and be less tense when we arrive at London Heathrow."
        hi "Hanako?"

        show hanako emb_timid_cas_close
        with chchange

        ha "Yes?"
        hi "Can I have a book?"
        "This week, Hanako and I paid a visit to the library and made sure to borrow a few books that neither of us has read before, so we could swap them after we're finished with them."
        "Seeing that we'll be spending several weeks in a foreign country, getting new books in Japanese will be all but impossible."

        show hanako basic_smile_cas_close
        with chchange

        ha "Sure."
        "Hanako picks up her handbag and hands me one of our books."
        
        show hanako_camera at displayitemshow
        with Pause(1.0)

        show hanako_camera at displayitem
        with None

        "I expect her to get one for herself as well, but instead, she takes out a neat-looking photo camera."
        hi "Hey, that's a nice camera."
        ha "It is."

        show hanako_camera at displayitemhide
        with Pause(1.0)

        hide hanako_camera
        with None

        show lilly basic_satisfied_cas_close at twoleft
        with charaenter

        "Lilly turns her head in our direction."
        li "I didn't know you owned one, Hanako. We should remember to register it at customs so you don't have to pay duty on it."

        show hanako emb_smile_cas_close
        with chchange

        ha "It's… not really mine. It belongs to the n-newspaper club. Naomi let me borrow it."
        li "Really? That's really nice of her. Do you get along well with her, Hanako?"

        show hanako basic_normal_cas_close
        with chchange

        "Hanako seems to think a bit on that."

        show lilly basic_smileclosed_cas_close
        with chchange

        ha "She… often comes up to talk to me these days, although she… does that with all members of the c-club."
        ha "Most of the time, she just talks… and I just try to k-keep up with her. But I don't exactly hate spending time with her. I think she means well."
        "Until Hanako joined the newspaper club, I never really interacted with Naomi even though we're both in the same class."
        "I wouldn't exactly call them a natural combination, seeing how talkative and forward Naomi often is and how quiet and reserved Hanako usually is."
        "On the other hand, the fact that moments with Naomi hardly contain any silences probably does a lot to hide Hanako's social handicap, and shared interests can go a long way in bridging gaps between people."
        hi "Well, let's give her gift meaning by making sure to take lots of photos to remember this trip by. Perhaps we could start right now."
        ha "Now?"
        hi "Could I have your camera for a moment?"
        "With a puzzled expression on her face, Hanako hands over the camera. I take it from her, get up and beckon a stewardess who's walking down our aisle."
        hi "Excuse me. Would you mind taking a picture of the three of us?"
        "Flight Attendant" "Of course not."
        "As the stewardess readies the camera, I quickly wrap one arm around Hanako's waist, pulling her a little closer, and put my other hand on Lilly's shoulder. I give the stewardess a affirmative nod."

        show lilly basic_cheerful_cas_close
        show hanako cover_bashful_cas_close
        with chchange

        "Flight Attendant" "Smile please!"

        play sound sfx_camerashutter

        "The stewardess presses the button, we hear a sharp click, and then she hands the camera back to me. I thank her and return the camera to Hanako."
        hi "Let's take a look."

        show hanako basic_bashful_cas_close
        with chchange

        "Hanako presses a button on the side, and I can see a picture of the three of us on the display."
        "It's not perfect… Neither Lilly nor Hanako are completely facing the camera. Lilly was probably still in the process of determining the exact location of the camera, and Hanako was trying to look into the camera while at the same time trying to keep her scars out of view."
        "Still, aside from those small snags, it's a nice picture and probably the first one ever taken that features all three of us."
        hi "I like it. The first picture of the three of us."

        show lilly basic_smile_cas_close
        with chchange

        li "The first of many, I hope."
        ha "Y-yes."

        play ambient sfx_plane_waiting fadein 4.0

        "I open my book and start reading, trying to ignore the steady flow of fellow-travelers filling up the plane."

        show hanako basic_distant_cas_close
        with chchange

        "I shoot a sideway glance at Hanako, but she's too occupied with examining the various options on the camera's display screen to pay much attention to the ever-growing crowd."
        "That's probably a good thing. As I turn to page 12 and the flow of people starts slowly drying up, Hanako turns to Lilly."
        ha "Ummm… Lilly."

        show lilly basic_smileclosed_cas_close
        with chchange

        li "Yes, Hanako?"
        ha "They have these… special clothes in Scotland, don't they? Like skirts?"

        show lilly basic_planned_cas_close
        with chchange

        li "Not many Scottish would appreciate you referring to them as skirts. They're called kilts over there."
        ha "Do a lot of p-people wear them over there?"

        show lilly basic_smile_cas_close
        with chchange

        "Lilly shakes her head."
        li "Think of them as traditional garments, like kimonos, that are worn during special events but are uncommon in everyday life."
        "I scratch my head."
        hi "Why the sudden interest in traditional local garments? Are you planning on getting one yourself?"

        show hanako basic_bashful_cas_close
        with chchange

        "Hanako shyly shakes her head."
        ha "Naomi wanted me to t-take a picture of a Scotsman. She m-meant a person in traditional clothes, I think."

        show lilly basic_smileclosed_cas_close
        with chchange

        "Lilly thinks for a moment."
        li "The ideal occasion to get pictures would have been the Inverness Highland Games—a traditional sports event held once a year. But unfortunately, that event has been held in July already."
        li "I'm positive, however, that there are several tourist attractions in the area where you should be able to get a few shots of Scots in traditional garb."
        li "They are part of Scotland's national image after all, and we're in the middle of the tourist season."
        "I turn to Hanako."
        hi "It's a small price for the opportunity to get a free camera, but it's still an odd request."
        ha "She asked f-for a picture of the Loch Ness monster first, b-but then said a picture of a true Scotsman was fine too. She's a l-little strange sometimes."

        show lilly basic_giggle_cas_close
        with chchange

        li "A true Scotsman? Oh my!"
        "Lilly raises her hand and covers her mouth, but it's not enough to hide a giggle and the broad grin on her face."
        "I must have missed something, but Lilly seems to find Hanako's last remark extremely funny. Looking at Hanako, I can tell she's as confused by Lilly's reaction as I am."
        hi "I'm afraid I don't quite follow. Care to enlighten us on what's so amusing?"
        "Lilly giggles once more, then scrapes her throat and composes herself."

        show lilly basic_cheerful_cas_close
        with chchange

        li "By tradition, kilts are worn without any underwear underneath. Asking a Scotsman whether he's a true Scotsman or not is the same as asking him if he's naked underneath his kilt."

        show hanako emb_blushtimid_cas_close
        with chchange

        "Upon hearing Lilly's explanation, Hanako lets out a shocked gasp before turning bright red."
        "Looks like Lilly just helped us dodge a bullet here."

        show lilly basic_smileclosed_cas_close
        with chchange

        hi "Thanks for saving us a really awkward situation. Hanako, do you think Naomi was serious or do you think she was playing with you?"
        ha "It's d-difficult to t-tell with her sometimes. I t-think she was serious."
        hi "Eh, we'll just take a picture of a Scotsman and tell Naomi it's a true one. Let her prove otherwise."

        show hanako emb_smile_cas_close
        with chchange

        ha "Okay."

        stop ambient fadeout 2.0
        queue ambient sfx_plane_beforetakeoff fadein 2.0
        play sound sfx_plane_dingdong

        show hanako emb_timid_cas_close
        with chchange

        "Before we can continue the discussion, the announcement system above our heads springs to life and we hear a chime followed by a male voice."
        "Captain" "Good afternoon ladies and gentlemen and welcome to flight OCN007 to London. Thank you for flying with Oceanic Airlines."
        "Captain" "In a few minutes, we'll receive permission from the control tower to access the runway."
        "Captain" "In the meantime, please make certain that your seat is in the upright position, and keep your seat belt fastened for as long as the sign above your seat is lit."
        "Captain" "We're about to show you a short video with safety instructions detailing how to act in an emergency situation."
        "The displays on the back of the seats in front of us suddenly turn on, and a flight attendant is seen going through the safety regulations like the smoking prohibition and the request to turn off cell phones."
        "Captain" "...please take note of the nearest emergency exit indicated by the signs that are currently lit up. In case of limited visibility, follow the trail of emergency lights on the floor..."
        "Judging from the seat chart the nearest emergency exit is right behind us although I seriously wonder if I'd be in a condition to even make it there in case of an emergency landing."

        show hanako emb_downsad_cas_close
        with chchange

        "Captain" "...in the case of the loss of cabin pressure, compartments above your head will open automatically to reveal oxygen masks. Always make sure to put on your own breathing masks before helping others with theirs..."
        "I wonder if I'm the only one who's a bit put off by how annoyingly cheerful the attendant in the video seems to be while describing a grave emergency situation."

        ha "That d-doesn't h-happen often, d-does it?"

        show lilly basic_listen_cas_close
        with chchange

        "I'm surprised by Hanako unexpectedly chipping in and even grow a little concerned when I notice she's become pale and visibly shivering a bit."
        hi "Hey, are you alright?"
        "Hanako nods weakly, but looks more than a little bit uncomfortable."
        "While I'm still trying to figure out why Hanako, who hasn't shown any indications of flight anxiety before, is suddenly getting jittery, Lilly calmly answers her question."

        show lilly basic_weaksmile_cas_close
        with chchange

        li "I wouldn't worry, Hanako. These worst-case scenarios are very rare, and air travel on the whole is a lot safer than travelling by car."

        show hanako emb_sad_cas_close
        with chchange

        "Hanako seems to relax a bit. The information video ends, and a few minutes later I can hear the plane's engines starting, and we slowly start moving."
        "We keep moving for about a minute and then suddenly stop again, causing Hanako to give us a puzzled look. Lilly seems to guess her thoughts."

        show lilly basic_smile_cas_close
        with chchange

        li "This is perfectly normal. We'll probably start moving again soon."

        show hanako basic_normal_cas_close
        with chchange

        "Sure enough, after a short while we start moving again, and the plane makes a slow turn. As we stop momentarily, Lilly smiles."

        stop music fadeout 3.0

        li "Here we go. You might experience some light ear pain during the takeoff or landing due to the changing pressure in the cabin. What I did last time was try to yawn a few times or chew some chewing gum. I have some in my handbag if you want it."
        
        stop music fadeout 2.0
        stop ambient fadeout 2.0
        queue ambient sfx_plane_takeoff2 fadein 2.0

        window hide

        scene bg plane_window_runway:
            yalign 0.5 zoom 1.02
            2.0
            block:
                linear 0.1 yalign 0.53
                linear 0.1 yalign 0.47
                repeat 50
            block:
                linear 0.1 yalign 0.58
                linear 0.1 yalign 0.42
                repeat 60
            block:
                ease 0.5 yalign 0.58
                ease 0.5 yalign 0.42
                repeat 2
            block:
                ease 1.0 yalign 0.58
                ease 1.0 yalign 0.42
                repeat
        with locationchange

        centered "Just as she finishes, the engines start roaring louder, and we're pressed into our seats as the plane starts accelerating.{fast}{w=12.0}{nw}"
        centered "Faster and faster we go...{fast}{w=6.0}{nw}"
        centered "...and then I get a strange feeling in my stomach as our plane leaves the ground.{fast}{w=10.0}{nw}"
        centered "I put my hands on Hanako's shoulders and softly move her aside just a little bit so I can look past her out the window as well.{fast}{w=10.0}{nw}"

        play music music_romance fadein 4.0

        scene bg plane_window_city:
            zoom 1.02
            ease 1.0 yalign 0.58
            ease 1.0 yalign 0.42
            repeat
        with Dissolve(1.0)

        "I move my right hand up to her face and use my index finger to gently brush her bangs aside so she can absorb the view with both eyes."
        "And an amazing view it is, just like Lilly said."
        "Tall buildings are turning small like playthings. The countryside turns into a big green blanket."
        
        show bg plane_window_clouds:
            zoom 1.02
            ease 1.0 yalign 0.58
            ease 1.0 yalign 0.42
            repeat
        with Dissolve(1.0)

        "And then, just before the pilot informs us we've reached cruising altitude, Hanako and I are faced with a vast ocean of clouds as far as the eye can see."
        "As we sit here, my arm around Hanako and her cheek pressed against mine, I occasionally look at the expression on her face which has turned from silent awe to a beautiful excited smile."
        "Over the course of this day, I've had my doubts from time to time whether this whole trip was a good idea, but that doubt is completely gone now."
        "This experience, this moment we're sharing together, was totally worth it."

        stop music fadeout 3.0
        stop ambient fadeout 3.0
        scene black
        with Dissolve(3.0)

        if _in_replay:
            return
    
    label .s3:

        $ set_window_tint(TINT_HISAO)

        scene bg black
        with Dissolve(2.0)

        play ambient sfx_plane_inflight fadein 2.0

        play music music_lilly
        scene bg airplane_cabin
        show lilly basic_smileclosed_cas at twoleft

        hi "Lilly?"

        show lilly basic_smile_cas

        li "What is it, Hisao?"
        hi "I didn't wake you up, did I?"

        show lilly basic_smileclosed_cas

        li "You didn't. I wasn't even sleeping. I already found out last time that I'm unable to sleep on airplanes."
        hi "I guess that makes two of us. It seems like only Hanako will be getting any sleep for the rest of the day."

        show lilly basic_weaksmile_cas

        li "So she's asleep right now? I already suspected as much by the sound of her breathing."
        hi "She is. And what's more, she's currently using my shoulder as a pillow."
        li "It's not uncomfortable for you, is it?"
        hi "No, far from it. However, I need to take a restroom break and take my medication, but I don't want to wake her up."

        show lilly basic_smileclosed_cas

        li "What do you want me to do?"
        hi "I've moved the armrests up. I'd like you to trade places with me for a little while if you don't mind."
        li "I don't mind. Do you simply want me to move to my right?"
        hi "Just a second... Now."

        show lilly basic_smileclosed_cas at tworight

        "I gently nudge Hanako upright a bit, then quickly get up as Lilly moves onto my seat before Hanako can slump back. I move away, and Lilly stays still for several seconds without even breathing."
        "Eventually Hanako mumbles something in her sleep before settling down on Lilly's shoulder."
        hi "Looks like we got away with it. I'll be back soon."
        li "Please don't rush yourself on my account."

        hide lilly

        nvl show dissolve

        n "{vspace=60}I shake my legs, which have started tingling from the long bout of inactivity, back to life and wobble unsteadily towards the lavatory in the back."
        n "{vspace=60}Opening the door, I'm taken aback for a moment at how cramped the thing is, but then take a deep breath and step inside. I'm pretty glad I'm not a claustrophobe right now. First taking the time to empty my bladder, I then open my backpack and get the usual dosage of pills out."
        n "{vspace=60}A few hours earlier we had a modest meal (it was okay, though not exactly up to the standards of Lilly's cooking or Hanako's more succesful school lunches), and I made sure to order an additional flask of bottled mineral water for this occasion."

        nvl clear
        nvl show dissolve

        n "{vspace=60}I use the water to flush the pills down my throat and yawn a bit. It should probably be night already, but if you look through the windows it's still broad daylight. Since we're flying west, we're essentially keeping up with the sun, making this possibly the longest day of my life."
        n "{vspace=60}When we get to London, it'll be late in the afternoon. I hope I'm not going to experience jet lag while we're in Scotland."

        nvl clear

        show lilly basic_smileclosed_cas at tworight

        "When I get back to our seats, I see that Lilly made herself a bit more comfortable. She has her right arm wrapped around Hanako and holds Hanako's hand in her left hand. They look very cute together."

        show lilly basic_pout_cas

        "I reach for Hanako's handbag near her feet, take out the camera and snap a quick picture. As Lilly recognizes the click from the camera she pouts with mock indignation."
        li "You should ask before taking pictures, Hisao. I probably looked a bit silly in this one."
        hi "Nonsense, some of the best pictures are the ones taken spontanously. Ready to switch places again?"

        show lilly basic_weaksmile_cas

        "Lilly considers for a moment."
        li "Actually, would you mind if I stayed like this a little longer?"
        hi "Not at all."

        play music music_twinkle
        scene ev planeride_normal

        "I take a seat and look at the girls again. Lilly has a peaceful smile on her face. I don't think her request was merely about not wanting to risk waking up Hanako."

        hi "There are blankets in the pockets of the seats in front of us. Would you…?"

        li "Yes please."

        "I take the folded blankets and remove the plastic wrapping around them. I softly wrap one of them around Hanako's sleeping form and pass the second one to Lilly, who merely folds it out and covers her lap with it."
        "I sit down in Lilly's original seat and get my own blanket. I doubt I'll get any sleep, but I try to relax nevertheless."

        li "Hisao, how long is it until we reach our destination?"

        "I take a look at one of the monitors hanging from the ceiling. The screen shows various bits of information, like the temperature outside, the altitude of the plane and the estimated time of arrival."

        hi "Four and a half more hours. I hope Hanako will have recovered her energy a bit by the time we land."

        li "I'm relieved she was able to relax. She seemed anxious when we were about to take off. I was afraid she'd turn out to have a fear of flying."

        hi "I've been thinking that over and… I don't think it was the flight itself that got her nervous. In fact, she seemed to love the view. It's the first time I've really seen her smile today. It was probably…"

        li "Hmmm?"

        hi "Ever since my first heart attack, I've hated hospitals. I dislike the sterile appearance and the overly clean smell."
        hi "I've really come to dislike heart monitors as well as anything that sounds like them. It's those beeps that really grate on me. Probably stir up some unpleasant memories."
        hi "The same is true for Hanako, I think. She's been through a long stay in the hospital herself ten years ago. I was thinking that maybe…"

        "Lilly seems to get where I'm going."

        li "The oxygen masks?"

        hi "Exactly."

        "She sighs."

        li "Today was certainly confrontational for her."

        hi "Yeah and yesterday wasn't really all that much better, with her being forced to sit through a lecture about burn injuries and her trainer scaring the living daylights out of her by faking a heart attack."
        hi "I really can't wait for this day to end."

        li "Hisao, do you know if Hanako has gone on any trips before she came to Yamaku?"

        hi "I asked her that myself a few days ago. You probably know the answer already. She hasn't been on vacation since she lost her family."
        hi "The orphanage occasionally organized day trips for the children there, but Hanako skipped most of those. The closest thing she's had to a vacation in a decade was that trip to Hokkaido."

        "Lilly softly squeezes Hanako's hand and strokes her long, dark hair."

        li "Hisao… Let's both do our best to make this vacation the most memorable and wonderful experience of her life."

        nvl show dissolve

        n "{vspace=60}I take another look at Lilly and Hanako. Many of the people I know at school hang out in pairs."
        n "{vspace=60}I know Emi often hangs out with her friend Rin, Naomi from the newspaper club is often seen together with Natsume, her neighbor in class, and I've hardly ever seen Shizune and Misha apart from one another."
        n "{vspace=60}But none of them seem to have that intimate emotional connection that Lilly and Hanako seem to share, especially now that they've settled their differences."

        nvl clear

        hi "You really love Hanako, don't you?"

        "She gives a deep nod, smiling warmly."

        li "I feel very fortunate to have her as my best friend."

        hi "I think she's very lucky to have you too. I don't think she could have wished for a better friend."

        "Lilly gives a self-deprecating sigh."

        li "I think I merely provided her with company and comfort."
        li "It was you who first broke through the barrier she erected around herself and convinced her to start opening up to others, including me."
        li "And it's been the people at the newspaper club who made her start thinking about what to do after graduation. In the end, I wasn't really able to help her grow as others have."

        "Something about what Lilly just said has a very familiar ring. I attempt to hold back a chuckle, but it's still loud enough for Lilly to catch it."

        li "Did I say something amusing?"

        hi "You're starting to sound a little bit like Hanako."

        li "I beg your pardon?"

        hi "The whole thing of 'How useful am I to my friends?' and 'Do my friends get as much out of me as I get out of them?' is how Hanako used to think all the time. Probably it's how she still thinks now and then."
        hi "But I don't think it matters. Maybe it's true that I helped Hanako grow more than you did, and maybe it isn't. Maybe it's true that the newspaper club helped Hanako grow more than you did, and maybe it isn't."
        hi "But I think that's completely irrelevant. I'd like to think that Hanako goes to the newspaper club because she enjoys the activities."
        hi "I'd like to think that the reason she hangs out with me is because she cares about me and feels appreciated and validated by me. That's probably also why she spends time with you."
        hi "Everything else is just a bonus. I don't think it matters to her. It probably shouldn't matter to us either."

        "Lilly breaks out into an amused smile."

        li "You sound so wise, Hisao."

        "I get the feeling she's poking fun at me, but she still sounds appreciative of my words."

        hi "What I'm trying to say is that you shouldn't sell yourself short. You're the first real friend Hanako's ever made in her life. That's got to count for something."

        li "The first real friend…"

        "Lilly seems lost in thought for a moment, then shakes her head as if dismissing some unspoken thought."

        li "I suppose I'd better do my best to prove myself worthy of that honor."

        hi "Just being yourself should be more than enough to pull that off."

        "Lilly smiles, but there's a sad quality to her expression."

        li "I'm not completely sure about that. The dilemma I faced concerning my parents' summoning weighed quite heavily on me, and the fact that Akira was involved in the whole situation as well meant that I couldn't go to her for objective advice."
        li "By facing that decision all on my own and by opting to keep everyone else out of it, I could argue that I was very much being myself. And it didn't bode particularly well for me."

        hi "I think that trying to address your own problems yourself is only human. We all like to be as independent as possible."

        "There's also the possibility that, given the way she acts, Lilly was probably raised and educated to behave as traditionally as possible and was taught that burdening others with one's problems is one of the biggest sins one can commit."

        li "True, but if it had been Hanako who had been in my predicament, I would have encouraged her to let others share the burden. I suppose... I don't always practice what I preach."
        li "If I had confided in Hanako sooner, I probably could have saved her a breakdown. And you a heart attack."

        hi "You're forgiven. This time."

        "Lilly chuckles and then carefully caresses Hanako's hair once more."

        li "I'd like to return the trust that Hanako has placed in me, Hisao. The next time she extends me a helping hand or a shoulder to lean on, I'll make sure not to turn it down."

        "I smile at Lilly and softly take her hand which is still holding Hanako's."

        hi "I'm sure she'd be very happy to hear that, Lilly."

        scene black
        with Dissolve(2.0)

        play music music_dreamy
        scene bg airport_baggagecarousel

        show hanako def_worry_cas at tworight

        hi "Hey Hanako, I think this one is ours. Can you take a look at the other side of the carousel? I'm aching to get out of here."

        ha "O-Okay."

        nvl show dissolve

        n "{vspace=60}Hanako walks over to the far side of the conveyor belt that has long strings of suitcases going in an endless circle, and we start looking for our baggage."
        n "{vspace=60}When our plane landed here at Inverness Airport, we made sure to wait until all the other people on the plane got out."
        n "{vspace=60}When we reached the baggage claim, I expected our suitcases to be the only ones left, but it seemed another flight had already finished unloading as well, and now we're rummaging through a large pile of bags and suitcases in search of our own."

        nvl clear

        "Lilly's suitcase is easy to recognize, containing both a sticker with the Japanese and a sticker with the Scottish flag on it, no doubt put there by Akira during their previous journey here."
        "Hanako's suitcase, however, is as average as they come, and the only way it stands out is that it appears less used than most suitcases on the conveyor."

        nvl show dissolve

        n "{vspace=60}As I rummage through the contents of the baggage carousel, I let out a loud yawn. It's nearly seven o' clock in the evening right now meaning it'd be about six o' clock in the morning in Japan. All three of us are about ready to faint from exhaustion."
        n "{vspace=60}Neither Lilly nor I have slept for the last 22 hours or so, and while Hanako did get some sleep in during our flight to London, the sheer amount of stress she's had to deal with, both before and after our international flight, has pretty much negated the advantage she had."
        n "{vspace=60}London Heathrow was even bigger and busier than the airport we departed from, and both the crowdedness and the process of having to go through customs and security took a harsh toll on her."

        nvl clear

        show hanako defarms_worry_cas

        "From the corner of my eye, I can see Hanako throw me a quick wave. As I look at her, I can see her dragging my suitcase off the conveyor belt. I get over to her side and notice there are two other suitcases at her feet."
        "Either she got lucky or she's still sharper than I am right now."

        show hanako basic_worry_cas

        hi "You just take your suitcase, and I'll carry mine and Lilly's."

        ha "Are you g-going to be okay?"

        hi "I'll be fine. You just guide Lilly for me."

        ha "Okay."

        show lilly basic_sleepy_cas at twoleft
        show hanako cover_worry_cas at tworight

        "We head back to Lilly who's sitting on the floor leaning against one of the walls and talking into her cell phone. As we reach her, I clear my throat to get her attention."
        hi "We retrieved all our luggage, Lilly."

        show lilly cane_weaksmile_cas

        "Sporting a weary smile, Lilly closes her cell phone and gets up."

        li "Very good, Hisao. Akira says she's almost at the airport. I asked her to wait for us at the parking space in front of the terminal."
        hi "I can't wait to get out of here. Is there anything we need to do before we leave, Lilly?"
        li "No, Hisao. We've already dealt with customs in London, so all we need to do now is leave the secure zone and get through the main hall of the terminal building."
        "I take a quick look around and see a sign on the wall indicating the direction of the exit. I point it out to Hanako, and she takes Lilly's hand and puts it on her shoulder for guidance."
        hi "Then let's get going. The sooner we get out of here, the better."
        "Lilly smiles wearily and nods."
        li "Yes, let's go."

        show hanako emb_downsad_cas at tworight

        "As we leave the baggage claim area through some automatic one-way doors, Hanako presses her hat down in preparation of another slow slog through the crowd. It looks like I'm not the only one who can't wait for this long day to end."
        "Thankfully, Inverness airport isn't nearly as large as London's is, so it only takes us a few minutes to get to the main entrance."

        scene bg inverness_airport

        show lilly cane_smile_cas at twoleft
        show hanako basic_distant_cas at tworight

        "We leave the building, and Hanako and I start looking around for Lilly's sister."

        show lilly cane_satisfied_cas

        li "Do you see her anywhere?"

        "Despite her weariness, I can tell by the tone of Lilly's voice she's extremely eager to meet up with her older sister again, despite the fact it's been less than two weeks since she left Japan."
        hi "I don't see her. Hanako?"
        ha "Maybe she got h-held up in traffic."
        "Lilly takes out her cell phone again and presses the recall button."

        show lilly cane_listen_cas

        li "Akira? We're at the main entrance right now. Did you already make it here?"

        show lilly cane_surprised_cas

        li "You did? Hisao and Hanako haven't seen you."
        li "What? You can see us?"

        play music music_comedy

        show hanako basic_smile_cas

        "Hanako and I immediately start looking around, and, sure enough, less than 50 meters away from where we're standing we can see a person with blond hair holding a cell phone to her ear with one hand and waving enthusiastically in our direction with the other."
        hi "Nevermind, we spotted her. I guess neither of us thought of the possibility she'd be wearing plain clothes today."

        show lilly cane_cheerful_cas
        show akira basic_ending at center

        "Lilly puts away her phone, and we hurry over to our welcoming committee. Hanako and I politely wait while Lilly steps forward and gives Akira a long and loving hug. Chuckling, Akira breaks off her sister's embrace."

        show akira basic_smug

        aki "Damn, you missed me that much? It hasn't even been two weeks."
        "I have the impression Akira's merely playing cool. She looks quite happy to see her sister again as well."

        show akira basic_smile
        show lilly cane_smileclosed_cas

        li "I must admit it felt strange knowing that you were all the way on the other end of the world and I couldn't meet up with you whenever I wanted to anymore."

        show hanako emb_downsmile_cas

        "Turning to us, Akira gives me a friendly nod while playfully ruffling Hanako's hair - a slightly odd gesture that nevertheless makes Hanako smile."

        aki "Yo. Guess you were looking for someone in a business suit, huh?"

        show hanako emb_smile_cas

        "We both look Akira over. She does look different from the way she usually does. Instead of her striped black suit, she's wearing jeans and a loose-fitting shirt. She also has a pair of sunglasses on her head."
        ha "You look… c-cool, Akira."
        "I smirk at our welcoming committee."
        hi "No fair coming here in disguise."

        show akira basic_laugh

        "Akira laughs heartily at my comment as she opens the trunk of her car and takes Lilly's suitcase from my hands."

        show akira basic_boo

        aki "Unlike some people in this family, I can still occasionally get away from my job. And today's weather was too nice for the suit."

        show lilly cane_reminisce_cas
        show hanako basic_worry_cas

        "She finishes putting Lilly's suitcase away and reaches for Hanako's. Lilly looks disappointed."
        li "So they really couldn't make it? Even though it's Saturday today?"
        "Akira shrugs."
        aki "A foreign business delegation came over two days ago, and Dad wants to impress them, so he's showing them the sights this weekend. He and Mom are essentially playing tour guide right now."

        show lilly cane_sad_cas

        li "Couldn't he have delegated it to someone else?"

        show akira basic_annoyed

        aki "It's Dad we're talking about, remember? He really, really likes to keep on top of his business."
        aki "Though I wonder if those people would still have been so impressed if they had known he put off an opportunity to greet his daughter who's been living on the other side of the world."
        "I put my own suitcase in the trunk, and Akira slams the lid shut slightly louder than necessary."

        show akira basic_cheerful
        show lilly cane_weaksmile_cas
        show hanako basic_bashful_cas

        aki "Are you guys hungry? I'll treat you."
        hi "I'm not. We've already had dinner on the plane and had another meal at the London airport. Hanako?"
        ha "Me neither."
        li "I think all three of us are merely very tired right now."
        aki "Fair enough. I'll treat you guys tomorrow then. A good night of sleep will do you a world of good."
        "Hanako and I get in the back while Lilly gets into the passenger's seat next to Akira."
        aki "Our folks' home lies slightly to the northeast of Inverness. We keep following the shoreline, and we'll reach it in no time. All buckled up?"
        "Our last ride during that outing to a jazz club in the city near Yamaku showed us Akira's not particularly concerned with the speed limits, so we make sure to strap ourselves in firmly."

        show akira basic_laugh

        aki "Good. Let's go, guys!"
        "As we leave the airport behind us, I breathe a sigh of relief. Looks like the hard part of our vacation is over. Now the fun part can begin."

        stop music fadeout 2.0
        scene black
        with Dissolve(2.0)

        if _in_replay:
            return

    return