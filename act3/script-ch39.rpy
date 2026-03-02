label sh_ch39:
    label .s1:

        $ set_window_tint(TINT_HANAKO)

        call sisterhood_timeskip

        scene bg school_dormlilly
        show karla basic_smile_cas_close at tworight
        show lilly basic_smile_cas_close at twoleft
        with Dissolve(2.0)

        play music music_happiness fadein 4.0

        ka "A writing club, huh?"
        "Lilly, her mother, and I are currently sitting in Lilly's room and having a cup of tea. We all have plans for this evening that don't involve hanging around here, but it feels nice to take a few minutes to sit back and relax."
        ha "Not really an official c-club. Just a few of us trying s-something new."

        show karla basic_smileclosed_cas_close
        with chchange

        ka "As a result of my advice?"
        ha "Yes."

        play sound sfx_whiteout

        scene bg school_newspaper:
            matrixcolor SepiaMatrix(tint="#ffeee0")
        with locationchange

        "Karla's visit to the newspaper club a few days ago had been an unexpected success. Neither Naomi nor Mister Hoshino had objections to letting a former journalist pay a visit, and so the afternoon at the club turned out to be quite different from the usual fare."

        show karla basic_smile_cas at center:
            matrixcolor SepiaMatrix(tint="#ffeee0")
        with charaenter

        "Lilly's mother was first introduced to everyone and given a little explanation on how we usually go about putting a newspaper issue together. Afterwards, all usual activities for the day were put on hold, and we spent several hours listening to Karla's stories about her own time as a journalist."

        show karla basic_cheerful_cas
        show naomi bend_laugh at right:
            matrixcolor SepiaMatrix(tint="#ffeee0")
        with charaenter

        "It turned out that Karla and Naomi took pretty much an instant liking to one another, feeding off each other's enthusiasm rather than being put off by it."

        play sound sfx_whiteout

        scene bg school_dormlilly
        show karla basic_smile_cas_close at tworight
        show lilly basic_smile_cas_close at twoleft
        with locationchange

        nvl clear
        nvl show dissolve

        n "At first I was a little worried when Lilly's mother mentioned that she had been out of the profession for quite some time, but that concern was quickly alleviated when it became clear how knowledgable Karla still was about many aspects of the job."
        n "{vspace=30}She started with a recount of how she went to study journalism in order to broaden her horizons and meet new people and how she got to travel around the country as a business reporter."
        n "She continued with an account of how she switched jobs and relocated to Japan and concluded with an analysis on how she experienced the news business in Europe, Japan and the United States."

        nvl hide dissolve

        show lilly basic_smileclosed_cas_close
        with chchange

        li "I spoke with one of the club's members in class two days ago. It seems you've made quite an impression on the club, Mother."

        show karla basic_cheerful_cas_close
        with chchange

        ka "Hahaha, that's good to know. It'd have been bad if it turned out that I was the only one who had fun that day."

        show lilly basic_weaksmile_cas_close
        with chchange

        li "I heard you brought me up, by the way."

        show karla basic_smile_cas_close
        show lilly basic_smileclosed_cas_close
        with chchange

        ka "Only to make a point, dear. You should be honored that I brought you up as a source of inspiration."

        nvl clear
        nvl show dissolve

        n "I remember that. Naomi asked Karla about the possibilities of getting a job in the news business if you couldn't drive and were encouraged by the doctor to keep your day-night rhythm as regular as possible."
        n "{vspace=30}Karla responded that the image of the reporter who's out and about 24/7 in search of the next big scoop hardly covered all journalists and that many articles could take weeks or even months to gather interviews and information for, so planning the project properly could go a long way in avoiding having to pull all-nighters."
        n "She also mentioned that it wasn't uncommon for reporters to team up to work on articles, and joining up with the right partner was all it would take to work around your individual limits. She then mentioned how Lilly wanted to teach English as a career and listed some of the workarounds her daughter came up with to circumvent the limits of her blindness."
        n "{vspace=60}That was a pretty motivating moment for everyone. Even I found it inspiring, even though Karla didn't really say anything about Lilly that I didn't already know."

        nvl hide dissolve

        li "Speaking of inspiration, what advice did you give that inspired the formation of this club?"
        ka "Probably the stuff I said about writing practice, wasn't it?"
        "I nod. Near the end of her visit, Lilly's mother said that the best way to start a journalism-related career would be to apply to a good university and get plenty of writing practice in the meantime."

        nvl clear
        nvl show dissolve

        n "Mister Hoshino promised to drop off a collection of brochures at the club for universities that offered suitable studies, and Naomi came up with a proposal to cover the writing practice a day after Karla's visit. Her proposal was to start checking out online writing competitions and take part in them."
        n "Unfortunately for her, Mister Hoshino immediately shot that idea down, as he argued that the club was centered around the creation of the school newspaper and received a club budget specifically for that purpose."
        n "He did encourage Naomi to pursue the venture after club hours though, and said he was happy to look up a few contests held by magazines, websites, and other third parties that high schoolers would be able to partake in. Encouraged by our teacher's support, Naomi promptly announced the founding of an unofficial writing club and invited everyone in the room to join."

        nvl clear

        n "I wasn't very sure how serious she was at first. Naomi has the tendency to be a bit impulsive from time to time, but when she approached me the day afterwards and repeated her invitation, I realized she was actually planning to go through with this."
        n "{vspace=60}Long story short, she ended up convincing me to give it a try."
        n "{vspace=60}I wasn't sure if this was going to go anywhere, but I had been thinking of getting some writing practice myself, and since our teacher said he was willing to provide feedback on everything we submitted, this appeared to be a pretty good opportunity."

        nvl hide dissolve

        ha "Y-yes. Mister Hoshino said he'd look into a few competitions for us to submit our w-work in. Even if we d-don't win anything, it'll still be good practice."

        show lilly basic_cheerful_cas_close
        with chchange

        li "And even if you don't win anything, you're still spending your time with friends doing something you enjoy. That's never a waste of time."
        "Friends? I'm slowly starting to get used to my clubmates' presence, but I'm not sure if we're truly friends. Certainly not in the way I'm friends with Lilly."
        ha "I... suppose."

        show lilly basic_smile_cas_close
        with chchange

        li "When will you be starting?"
        ha "We... meet up for the f-first time this evening. It's just... three of us right now."

        show lilly basic_satisfied_cas_close
        with chchange

        li "How exciting. And where will you be meeting up?"
        "I sigh. That issue came up earlier today, and I'm not too fond of the outcome."
        ha "We d-drew straws. They're c-coming t-to my room tonight."

        show lilly basic_displeased_cas_close
        show karla basic_confused_cas_close
        with chchange

        "Lilly nods understandingly, but her mother looks a bit confused."
        ka "You look a bit apprehensive about it."
        ha "Ummm... L-Lilly and Hisao are the only two people I've ever let into my room before."
        "I'm quite aware of the possibility that they'll find my room empty, dull and devoid of personality—especially Naomi who tends to speak her mind from time to time—and that might be enough to instantly kill my motivation and what little self-esteem I've been trying to gather for this."

        show lilly basic_weaksmile_cas_close
        show karla basic_sheepish_cas_close
        with chchange

        li "Would you like to use my room, Hanako? Mother and I will be away for most of the evening, so nobody will bother you here."
        "Karla will apparently be travelling the country the upcoming week in order to look for attractive neighborhoods to settle down in if they want to go through with the plan of migrating back to Japan."
        "That means she won't be in the area for several days, so she and Lilly are going out tonight and probably won't be back until rather late."
        ha "Ummm..."
        "I strongly consider taking Lilly's offer, but there are a few problems with it. First of all, if this meeting turns out well, it won't be the last time we get together, and I might end up playing host at some point in the future again. I can't keep relying on Lilly for that."
        "Also, the others will be able to immediately tell that this isn't my room and might start speculating why I'm so reluctant to invite them over to my place. That speculation, especially with Naomi, might be worse that the real thing."

        ha "Thanks, but... they'll probably s-start thinking bad things about me if I won't even l-let them into my room."

        show lilly basic_smileclosed_cas_close
        show karla basic_speak_cas_close
        with chchange

        "Lilly's mother toys around with her hair a bit and looks at me with a serious look in her eyes."
        ka "I guess this must be kind of intimidating, but sometimes the only way to move forward is to take a bold step and have faith that it'll turn out alright."
        ha "Faith?"

        show karla basic_smileclosed_cas_close
        with chchange

        ka "Yep. It can help from time to time, you know."

        show lilly basic_smile_cas_close
        with chchange

        show teaset:
            truecenter
            ypos 0.6 alpha 0.0
            easein 1.0 truecenter alpha 1.0
        with Pause(1.0)

        "Lilly takes the teapot and holds it out for me."
        li "If you're not going to use my room, please at least use my tea set. Seeing that you were the one who picked it, I feel it is also partially yours anyway."
        "That might not be such a bad idea."

        show teaset:
            parallel:
                easeout 1.0 ypos 0.6
            parallel:
                ease 1.0 alpha 0.0
        with Pause(1.0)

        hide teaset

        ha "Okay then. I'd better go and make new tea."

        scene bg school_dormkitchen
        show karla basic_smile_cas at tworight
        show lilly basic_smileclosed_cas at center
        with chchange

        "We leave Lilly's room, head down to the kitchen area, and I start boiling water for a new batch of tea. Judging by the fact that Lilly and her mother are carrying their handbags, the two are just about ready to leave. As I start filling up the teapot, Lilly turns to me."

        show lilly basic_smile_cas
        with chchange

        li "Hanako, I know that Naomi is part of this little club too, but you said there were three of you right now. Who is the third member?"
        mystery "I am."

        # TODO replace Jun sprites with her in a wrist brace
        show jun basic_smile at left
        with charaenter

        "We turn around to find my fellow editor standing in the kitchen doorway wearing her favorite red-and-white cap, carrying a flat, black bag with one hand while wearing a wrist brace on the other. Lilly's mother smiles and returns Jun's bow with a polite one of her own."

        show karla basic_cheerful_cas
        show lilly basic_smileclosed_cas
        with chchange

        ka "Yamazaki, wasn't it?"

        show jun basic_smileclosed
        with chchange

        jun "Good evening."
        "Karla shifts her gaze to the bag Jun is carrying."

        show karla basic_smile_cas
        with chchange

        ka "You brought a laptop along?"

        show jun basic_happy
        with chchange

        jun "It's my own. We can use it to type up what we come up with and look things up if necessary."

        show karla basic_confused_cas
        with chchange

        ka "Do you have Internet here? I didn't notice any network sockets in the wall of Lilly's room."
        ha "There aren't any. But I've seen people checking their mail on l-laptops in the common room before, so the building probably has Wi-fi."

        show karla basic_sheepish_cas
        show lilly basic_displeased_cas
        with chchange

        ka "That makes sense."

        show jun basic_laugh
        with chchange

        "Jun nods enthusiastically."
        jun "There's a Wi-fi router in the common room's TV cabinet. The network isn't password-protected, so anyone with a laptop who wishes to access the internet can log onto it."

        show karla basic_smile_cas
        show lilly basic_weaksmile_cas
        show jun basic_smile
        with chchange

        li "Mother, now that one of Hanako's guests has already arrived, perhaps it would be a good moment for us to be on our way."
        "I use my hand to hide a small amused smile. Lilly has a point of course, but I noticed she visibly cringed for a moment when the discussion turned technical. Lilly's never been very comfortable with her computer illiteracy."

        show karla basic_laugh_cas
        show lilly basic_smileclosed_cas
        with chchange

        ka "I guess so. You'll say hello to Inoue for me, won't you?"
        ha "Sure."
        ka "Well, have fun you two. Bye."

        show lilly:
            xpos 1.1
        show karla:
            xpos 1.3
        with charamove

        hide lilly
        hide karla

        "Lilly and her mother wave goodbye and walk out of the room while I'm left with Jun who seems eager to leave."

        show jun basic_eyeroll_close
        with chchange

        jun "Shall we go, Hanako? This laptop is getting a bit heavy, so..."
        ha "Oh... ah... Sure."

        if _in_replay:
            return
        else:
            stop music fadeout 2.0

    label .s2:

        $ set_window_tint(TINT_HANAKO)

        scene bg school_girlsdormhall
        show jun basic_serious_close at twoleft
        with locationchange

        "We leave the kitchen and make our way to the door of my room."
        "Once again my anxiety flares up a bit. Jun isn't someone whom I expect will immediately criticize me for the way my room looks, but she'll definitely think something when I let her in."
        jun "Hanako?"
        ha "J-just a moment."

        play sound sfx_dooropen

        scene bg school_dormhanako
        with locationchange

        "I unlock the door to my room, and we go in. I walk right up to my desk and put the tea set down so I don't have to see the look on Jun's face. There's no immediate reaction either."
        "When she finally says something, it isn't even a reaction to her surroundings. I'm not sure whether to feel relieved or worried."

        show jun basic_speak_close
        with charaenter

        jun "...can I put my laptop on your desk? It'll be easier that way."
        ha "Ah, sure."

        play music music_normal fadein 4.0

        hide jun
        with charaexit

        "She walks up to my desk, plugs her laptop into the nearby power socket and starts it up. The room is quiet except for the subdued humming of the computer. The silence starts feeling really heavy to me, but it doesn't seem to bother Jun."

        show jun basic_serious_close
        with charaenter

        "I haven't really known her for very long, but one thing I've learned about her is that she isn't very talkative most of the time unless a subject she's specifically interested in pops up, at which point she can get quite verbose."

        show jun basic_pout_close
        with chchange

        "I don't think it's shyness in her case... I've seen her put Naomi in her place when the latter said something that Jun thought was ridiculous and that's a pretty big thing seeing that Naomi is her senior."
        "It's just that she doesn't like to use twenty words to say something that can also be said with ten."

        show jun basic_serious_close
        with chchange

        jun "..."
        ha "..."
        "While I'm still struggling to think of a way to make conversation, Jun has finished booting up her system and is now running her internet browser to test the network connection. That suddenly makes me wonder about something."
        ha "Ah... Jun?"

        show jun basic_smile_close
        with chchange

        jun "Hmmm?"
        ha "Ah... You... often visit the computer lab, don't you?"

        show jun basic_happy_close
        with chchange

        jun "Yes. I think that's where we first saw one another. It was some time before you joined."
        ha "Why... do you go there if you h-have your own laptop?"

        show jun basic_sheepish_close
        with chchange

        jun "This is a really old model, and it isn't always stable. That's why it took so long to start up. It can't handle graphically intensive websites well. Or message boards where a lot of pictures are posted."
        ha "Oh."

        show jun basic_speak_close
        with chchange

        jun "Hanako, what do you like most? Writing or editing?"
        ha "I like the idea of writing. I just... don't have much experience yet."

        show jun basic_happy_close
        with chchange

        jun "Maybe now that I'm back at the club you can do more writing. I'm sure Naomi can find plenty of things for you to do."
        ha "Maybe... I'd still like to do a bit of editing if that's okay. It's... umm..."
        "Safer. People are less likely to criticize me, because I didn't actually create anything for them to criticize."
        ha "...fun too. Do you like editing?"

        show jun basic_eyeroll_close
        with chchange

        jun "It's a fun job to do. I've been told that I'm very particular about spelling and grammar, so it's nice to put that to good use."
        ha "Told by whom?"

        show jun basic_smug_close
        with chchange

        jun "Some people online. I don't think much of it. I usually make an attempt to type correctly on message boards even if one of my arms is in a cast or brace, so it's not too much to ask others to do the same, is it?"
        "For some reason she rolls her eyes while she says that. I wonder why."
        ha "No. But... if you prefer editing then why did you join a writing club?"

        show jun basic_smileclosed_close
        with chchange

        jun "Editors and researchers are useful for writing clubs, too. When Naomi invited me, I told her I wasn't really up to writing stuff myself, but I'd be happy to assist you with yours."

        show jun raise_smug_close
        with chchange

        jun "And hey, I'm the fastest typist in the club whenever my hands aren't encased in plaster."

        show jun basic_smile_close
        with chchange

        show jun basic_confused_close
        with charachangealways

        "The conversation falls silent again until I'm startled by a sudden movement from the door handle. Someone just tried opening the door. Jun throws me a puzzled look."
        jun "Did you lock the door after we got in here?"
        ha "F-force of habit."

        play sound sfx_dooropen

        scene bg school_girlsdormhall
        show naomi basic_neutral:
            twoleft
            ease 1.0 offscreenleft
        with locationchange

        pause 0.5

        "I quickly unlock the door and notice someone with bleached hair and a file folder under her arm walking down the hall and away from the door."
        ha "N-Naomi."

        show naomi basic_laugh at twoleft
        with charamovefastest

        "She turns around and waves."
        na "Hey! I was already heading for the kitchen to check for you there. Is Jun already inside?"
        ha "Y-yes. C-come in."

        scene bg school_dormhanako
        show jun basic_smile_close at twoleft
        show naomi basic_smile_close at left
        with locationchange

        play sound sfx_doorclose

        show naomi basic_smile_close at tworight
        with charamove

        "I let Naomi into my room and my heart skips a beat when I see her take a long, long look around the room. Surprisingly, the expected “What the hell?” doesn't come."

        show naomi basic_focus_close
        with chchange

        "Instead, she merely keeps sweeping my room with an analyzing gaze that feels strange coming from her. Eventually, her eyes fall on my cabinet containing my two dolls. A smile suddenly appears on her face."

        scene ev hanako_dolls
        with locationchange

        na "Hey! This one looks a lot like Satou. That's probably not a coincidence, is it?"
        "I'm taken a bit off guard by her sudden switch from analytical observer to her usual self, but manage to stammer out a response."
        ha "It... was a g-gift from Lilly. Hisao p-picked it out for her."
        na "It looks really cute."

        scene bg school_dormhanako:
            zoom 1.1 yalign 1.0
        show jun basic_happy_close at twoleft
        show naomi basic_smile_close at tworight
        with locationchange

        "Jun taps her fingers on the teapot next to her laptop to get Naomi's attention."
        jun "Do you want to have some tea? It's still warm and pretty good."

        show naomi basic_laugh_close
        with chchange

        na "Yeah, I'd like some."

        show jun basic_smile_close at twoleft
        show naomi bend_smile_close at tworight
        with chchange

        "A bit relieved by Jun's attempt to divert Naomi's attention away from my room's interior, I pour some tea for her and myself, and we take a seat on my bed while Jun remains seated on my chair."

        nvl clear
        nvl show dissolve

        n "The atmosphere is fairly relaxed as we drink our tea and just sit there, but I still feel a bit on edge. I wonder if that's because there are two people whom I haven't known for that long sitting in my room right now."
        n "{vspace=60}Ever since I came to Yamaku, this room has been the only place where I could always go to feel safe and secure."
        n "The knowledge that I'll have nowhere to run off to if something happens that sets my anxieties off makes me feel uneasy and a little bit cornered."

        nvl hide dissolve

        show jun basic_eyeroll_close
        show naomi basic_confused_close
        with chchange

        na "...Hanako?"
        ha "Ah... Y-yes?"

        show naomi bend_smile_close
        with chchange

        na "I was asking whether it's okay to get started."
        "I really need to stop spacing out over this. I'm not going to be able to pull my weight here if I can't put my mind at ease."
        ha "S-sure."

        show bg:
            yalign 0.0
        show jun:
            ypos 1.25
        with charamove

        stop music fadeout 2.0

        show jun basic_smile_close
        show naomi basic_laugh_close
        with chchange

        "Naomi gets up, scrapes her throat, pauses for a bit of effect and then throws her fist up in the air."

        queue music music_comedy fadein 4.0

        na "Welcome to the first meeting of our new club, people. It would be grand if we could start cranking up pieces tonight already, but let's start with the most important thing first."

        show jun basic_speak_close
        with chchange

        "Jun looks at the folder Naomi took along with her."
        jun "You spoke to Mister Hoshino about recommendations, didn't you?"

        show jun basic_serious_close
        show naomi basic_smile_close
        with chchange

        na "We'll get to that later. The most important thing for now is deciding on a name for ourselves."
        ha "Ummm... D-do we really need a name? This isn't an... official club, is it?"
        na "Of course we need a name. I already felt cheesy saying ‘our new club’ the first time and having an official name makes things easier. We need to know what to say when referring to the club. It's also a matter of principle."

        show jun basic_confused_close
        with chchange

        "Jun looks puzzled at that."
        jun "Why is it a matter of principle?"

        show naomi bend_grin_close
        with chchange

        na "If we don't even have the creativity to think up a name for ourselves, what does that say about our ability to come up with stuff to write about?"

        show jun basic_smileclosed_close
        with chchange

        jun "I can't really argue that point."

        show bg:
            yalign 1.0
        show jun:
            ypos 1.0
        with charamove

        show jun basic_smile_close
        show naomi basic_grinclosed_close
        with chchange

        na "Okay! Brainstorm time, girls! How are team names made up?"

        show jun basic_smileclosed_close at left
        with Dissolvemove(1.0)

        pause 0.3

        show jun basic_smile_close
        with chchange

        "Jun thinks for a moment and then starts typing on her laptop. A few seconds later she moves aside to reveal a website containing information about the Japanese baseball league."

        show jun basic_happy_close
        with chchange

        jun "Yomiuri Giants. Hanshin Tigers. Tokyo Yakult Swallows. Chiba Lotte Marines. Fukuoka SoftBank Hawks."

        show naomi basic_focus_close
        with chchange

        na "Okay, so those teams often use animal names or some other impressive-sounding noun and combine it with the area they're from or the company that owns them. That's not a bad way to come up with a name."

        show jun basic_smile_close at twoleft
        with Dissolvemove(1.0)

        show naomi basic_smile_close
        with chchange

        na "For us that would probably be Yamaku then. We just need a noun to go with it. Maybe animals. How does ‘The Yamaku Kittens’ sound?"

        pause 0.6

        show naomi bend_laugh_close
        show jun raise_laugh_close
        with charachangealways

        "There's a short silence followed by a giggle from all three of us. I think that name sounds way too cute for a writing club. Jun smilingly shakes her head."

        show jun basic_smileclosed_close
        show naomi basic_grinclosed_close
        with chchange

        jun "That may be a better name for a cheerleaders' squad. Maybe we need to go with something that refers to writing or writing implements. ‘The Yamaku Pens’ or ‘The Yamaku Pencils’ perhaps?"

        show jun basic_smile_close
        show naomi basic_focus_close
        with chchange

        "Those might be better suited for a writing club. Naomi doesn't look completely convinced though."
        na "Doesn't sound bad, but I think it lacks a little punch."
        jun "There aren't that many writing implements. I hope you're not planning to go with typewriters or word processors."

        show naomi basic_grinclosed_close
        with chchange

        na "Hehehe, that sounds horrible. I don't know, maybe we ought to look at it from more than one angle. Hanako, what do you think?"

        show naomi basic_smile_close
        with chchange

        ha "Ah... I'm... n-not sure. I don't r-really have any better ideas."
        na "What's the last team name you've heard lately? Baseball teams don't count."
        ha "Ummm... Oriental Express?"

        show jun basic_confused_close
        show naomi basic_neutral_close
        with chchange

        na "Huh?"
        ha "In Scotland... Lilly and her sister won a p-pub quiz under that name."

        show jun basic_smile_close
        show naomi basic_grin_close
        with chchange

        na "Heh, that sounds kinda cool. Do you remember any more names?"
        "Akira listed a whole bunch of them when we left the pub, but I don't remember them all."
        ha "Ummm... A lot of them w-were related to beer or drinking like ummm...‘Beer today, Gone tomorrow’. And some were some self-mocking names like... ‘Beauty School Dropouts’."

        show naomi basic_focus_close
        with chchange

        na "Hmmm, a slightly playful name may be cool too."

        show jun basic_speak_close at left
        with Dissolvemove(1.0)

        "Jun turns back to her laptop and types a few more words."

        show jun raise_laugh_close
        with charachangealways

        show naomi at center
        with charamove

        show naomi bend_grin_close
        with charachangealways

        show jun basic_eyeroll_close
        show naomi bend_smile_close
        with charachangealways

        "The page she's looking at must be pretty funny, because she lets out a soft giggle but when Naomi comes over she quickly clicks the page away."

        show jun basic_sheepish_close
        with chchange

        jun "Hmmm... Well, some of those pub quiz team names are pretty creative, but I don't know how I'd feel about referring to us as ‘Oh no, my pen's running ou...’ or ‘One wheel short of a unicycle’. It'd probably get old after the second time."

        show jun at twoleft
        show naomi at tworight
        with charamove

        show naomi basic_smile_close
        with chchange

        na "Yeah, so playful is okay, but over-the-top is bad..."

        show jun basic_speak_close
        with chchange

        jun "Maybe we should go with the pen or pencil angle after all."

        play sound sfx_snap

        show naomi basic_grin_close
        with chchangefast

        "Suddenly Naomi snaps her fingers."
        na "How about... The Broken Quills?"

        show jun basic_confused_close
        with chchange

        "Jun and I instinctively exchange a baffled look."
        jun "What?"
        ha "Ummm... W-what?"

        show naomi bend_grin_close
        with chchange

        na "You girls know what a quill is, don't you?"

        show jun basic_annoyed_close
        with chchange

        jun "Yes, but what about the broken part?"

        show naomi bend_wink_close
        with chchange

        na "It's not meant to be insulting, but simply a little playful. I mean, if you use Yamaku in the name and people wonder what the heck the word means and look it up, they'll know what kind of school this is anyway."
        jun "Just because we attend this school doesn't mean we're... like... damaged beyond all use, right?"

        show naomi basic_grinclosed_close
        show jun basic_serious_close
        with chchange

        "Naomi pumps a fist into the air as if Jun just proved her point."

        show naomi bend_laugh_close
        with chchange

        na "Just like a quill you break in half. It may not be exactly like an ordinary quill, but you can still use it and you can even write masterpieces with it if you have the inspiration and the drive."
        na "We may be attending this school and have reason to do so, but with inspiration and drive we too can create some great things!"

        show jun basic_confused_close
        with chchange

        "I exchange another baffled look with Jun. Naomi's reasoning, as twisted as it is, kind of makes sense, but only in a very morbid way."
        jun "I'm still not completely sold, to be honest."
        na "Hanako?"
        ha "I'm... not really sure... either."

        show naomi bend_smile_close
        show jun basic_serious_close
        with chchange

        na "Consider it, okay? And take some time to think up some alternatives. We'll get back to this next time. Let's get to the other topic of tonight."

        show jun at left
        show naomi at right
        with charamove

        show naomi basic_smile_close
        show jun basic_smile_close
        with chchange

        "Naomi takes the file folder she brought along and fishes several sheets of paper out of it."
        na "Aaaaand... here are our challenges. Look them over and let me know what you think."

        show naomi basic_neutral_close
        show jun basic_serious_close
        with chchange

        "She passes a few pages to each of us, and I start looking through mine. I'm impressed by how many our Japanese teacher managed to find in only a few days."
        "There are a few contests organized by online writing communities, but most of them are hosted by various literary clubs associated with high schools and universities in the region."
        ha "Wow... A p-poetry contest."
        na "I have one about essays here."
        "Jun scratches her cheek."

        show jun basic_speak_close
        with chchange

        jun "Did you girls notice that most forms mention a word or page limit?"

        show naomi basic_smile_close
        with chchange

        na "I think Hoshino picked those out on purpose. He probably wants us to start small and not spend months writing a single piece. Hanako and I have exams in January after all."

        show jun basic_serious_close
        show naomi basic_grin_close
        with chchange

        na "If we're going with the essay assignment, I suggest we make them about those exams. Plenty of stuff to write about."
        ha "Such as?"

        show naomi basic_annoyed_close
        with chchange

        na "How stupid they are. You spend three years working your butt off trying to get good grades and yet all those grades end up not meaning crap as far as your admission goes. Just a handful of days in three whole years that have any significance whatsoever."
        na "You sleep through high school and have a lucky break at the end and you pass. You work hard and have a bad day or two and you flunk. Does that sound fair to you?"
        "Looks like we've hit a personal pet peeve of Naomi's."

        show jun basic_sheepish_close
        with chchange

        jun "If you don't like exams then how would you do it?"

        show naomi basic_neutral_close
        with chchange

        na "I dunno. Instead of stuffing the whole national exam into one weekend, maybe spread it out throughout the year so you only have to memorize a little bit at a time and get a chance to make up on the next run if you miss one or do badly? Or maybe hold the exams four times a year."
        na "Now you lose a whole year of your life if Murphy screws you over on the wrong day. It's complete bullshit."
        "Wow, she's really passionate about this. Jun looks at Naomi, then at me, then back at Naomi again."

        show jun basic_smileclosed_close
        with chchange

        jun "I don't think an essay needs to be completely objective, but I doubt the word ‘bullshit’ will look good in there."

        show naomi basic_grin_close
        with chchange

        na "Duh. I can reword it a bit."

        show jun basic_eyeroll_close
        with chchange

        "Jun looks at one of the forms again and smirks."

        show naomi basic_neutral_close
        with chchange

        jun "We probably won't win a prize with that subject."
        na "Why not?"

        show jun raise_smug_close
        with chchange

        jun "Because the essay contest is hosted by a university. They might not take well to us criticizing their method of accepting students."

        show naomi basic_annoyed_close
        with chchange

        na "It's a conspiracy."

        show jun raise_laugh_close
        with chchange

        jun "I may know of a few internet forums that are suitable for venting about that if you're interested..."

        show jun basic_sheepish_close
        show naomi bend_smile_close
        with chchange

        na "Okay, okay. Next."

        show jun basic_happy_close
        with chchange

        jun "The rest seem to be about short stories."
        ha "Mine too."

        show jun basic_smile_close
        show naomi basic_focus_close
        with chchange

        na "That's probably the best place to start. So what options do we have in terms of subjects? Jun?"
        jun "I have science fiction and slice-of-life here. The rest allows the participants to pick their own genre."
        na "Hanako?"
        ha "Hmmm... Slice-of-life, fantasy, and drama. The rest leaves it up to us."
        na "Mine are fantasy and romance. Looks like we have plenty of options. What do you say we write down our two favorite options and compare them all?"
        "Jun and I both nod in agreement. As I take a piece of paper to jot down my preferences, I notice that Jun has finished her cup of tea. I take the teapot to refill her cup only to find out that it's nearly empty."
        ha "I'll... ummm... go and make some more tea."

        show jun basic_smileclosed_close
        show naomi basic_grinclosed_close
        with chchange

        jun "Great. Thanks."

        stop music fadeout 4.0

        scene bg school_dormkitchen
        with locationchange

        nvl clear
        nvl show dissolve

        n "I leave my room, teapot in hand, and make my way to the kitchen."
        n "{vspace=60}So far everything's been going rather well. I'd still like to get back though. What would happen if Naomi started snooping around and found my birth control pills or the diary I kept until Lilly's father got hospitalized?"
        n "I don't think there'd be a second meeting if that were to happen. At least not with me present."

        nvl hide dissolve

        "After boiling some more water and refilling my teapot, I start walking back to my room."

        scene bg school_girlsdormhall
        with locationchange

        "As I do so, my thoughts return to Naomi's rant about the exams. It came as a surprise to hear her get so worked up over something like that. I guess there's still plenty about her that I don't know."

        $ renpy.music.set_audio_filter(channel="sound", audio_filter=renpy.audio.filter.Lowpass())

        play sound sfx_impact2 volume 0.8

        "I make it to the door of my room and reach out to push it open when I'm suddenly startled by a loud crashing noise followed by a shriek."
        "I freeze. That sound came from behind my own door. What's happening?"
        "I uneasily open the door and look inside."

        $ renpy.music.set_audio_filter(channel="sound", audio_filter=None)

        scene bg school_dormhanako
        show jun basic_disturbed_close at left
        with charaenter

        "Jun's no longer sitting at my desk. She's standing up, her back pressed against the nearby wall, and there's a terrified look on her face. There are several things lying at her feet. A box of tissues, a desk lamp and an alarm clock. My things."
        "They're usually on the shelf just above my bed. Did Naomi accidentally knock them off?"
        jun "She... She suddenly got like this..."

        play music music_rain fadein 4.0

        show naomi basic_seizure_close at center:
            anchor (1.0, 1.0) pos (1.15, 1.2) rotate 10
        with charaenter

        "My gaze shifts to Naomi who hasn't moved since I opened the door. She's still sitting on my bed, but there's something strange about her posture. It looks like she's leaning, no, slumping against the now empty shelf."

        show naomi:
            linear 0.1 rotate -20
            linear 0.1 rotate 10
        
        pause 0.2

        "Just when I'm about to walk up to the bed and ask if she's alright, her head snaps back as if an invisible person just walked up to her and punched her in the face."

        show naomi:
            linear 0.1 xpos 1.25 rotate -10
            linear 0.1 xpos 1.15 rotate 10

        play sound sfx_impact2

        pause 0.2

        "At the same time, she violently swings her left arm as if trying to slap someone. I cringe as I hear her hand crash into the shelf. That sounded like it hurt, though Naomi doesn't even acknowledge it. That certainly explains how all my items suddenly ended up on the floor."
        "I look at Jun again. Judging by the freaked-out look on her face, this is probably the first time she's seeing Naomi having an epileptic seizure."
        "And truth be told, the sight of Naomi, eyes rolled back, lips slightly blue and movements spastic and unnatural is an extremely disturbing sight even though I've witnessed this spectacle plenty of times myself over the years."

        show jun basic_sad_close
        with chchange

        jun "What should we do?"
        "I really don't know. If we were in class, Natsume or the teacher would jump in and take care of this. But right now it's just Jun and me, and neither of us really seems sure what to do."

        show naomi:
            linear 0.1 xpos 1.25 rotate -10
            linear 0.1 xpos 1.15 rotate 10

        play sound sfx_impact2

        pause 0.2

        "Again, Naomi's hand violently hits the shelf. I know enough about epilepsy to remember that epileptics sometimes suffer concussions from banging their head against a wall or floor during a seizure. The least thing I can probably do is making certain that won't happen this time."

        show naomi:
            xanchor 0.5 xpos 0.6
        with charachangealways

        show naomi:
            linear 0.1 rotate -20
            linear 0.1 rotate 10

        play sound sfx_impact

        pause 0.2

        "I walk over to the bed, grab hold of Naomi and try to get her to lie down to the best of my ability. I'm promptly rewarded for my efforts as one of Naomi's flailing arms hits me hard in the side."
        ha "Ow!"

        show jun basic_sad_close at twoleft
        with charamove

        show naomi:
            linear 0.1 rotate -20
            linear 0.1 rotate 10
        
        pause 0.2

        show jun basic_disturbed_close at left
        with charamovefastest

        "I quickly back off, grimacing and rubbing my side. That was unexpected. Jun worriedly gets a little closer, but quickly steps back when one of Naomi's legs kicks the air."
        "I don't think it's a good idea for someone as physically fragile as Jun to try and get anywhere near Naomi. Some time ago she accidentally tripped and broke her hand while trying to catch herself."
        "I don't want to imagine what would happen if Jun took a hit from one of Naomi's thrashing limbs. I doubt the results would be pretty."
        jun "Are you alright?"
        "I quickly nod. I don't think I'm the one we should be worrying about right now."

        show jun basic_sad_close
        with chchange

        jun "Is... is it always like this?"
        "I nod again. Well, it's like this most of the time. There are times when she simply appears to black out, but my mind isn't really clear enough to give Jun a detailed account on Naomi's condition as far as I've experienced it."
        jun "Hanako, we should... probably get help. Don't you think?"
        "My first thought is ironically that I don't want some random nurse barging into my room. Then I realize how selfish and unfeeling that is, and I feel guilty for even thinking it."
        ha "Y-yes, we probably should. But w-we can't leave her alone like this."
        "Jun is obviously looking to me for advice on how to deal with this, but unlike someone like Natsume, I really don't have any experience handling this sort of thing."
        jun "Hanako?"
        ha "...N-Natsume. You s-should go and fetch Natsume. I'll stay with Naomi."

        show jun basic_annoyed_close
        with chchange

        jun "Right."

        show jun basic_annoyed_close at offscreenleft
        with charamovefaster

        hide jun

        scene ev seizure_bedroom_fit
        with locationchange

        "As Jun walks out of the room I focus my attention back on Naomi. She's still flopping around like a fish out of the water, and she's threatening to fall off my bed because of it."
        "I take a deep breath and push her as far back onto the bed as possible, making sure she keeps lying on her side."
        "I'm currently racking my brain to remember what my first aid training said about seizures again, but one thing I remember is that it's best to lay victims on their side so they don't risk choking on their own saliva."
        "Judging by the large dark stains that have already formed on my pillow, that's certainly something to keep in mind with Naomi."
        jun "Hanako?"

        scene bg school_dormhanako
        show jun basic_annoyed_close at left
        with locationchange

        "The door opens and I see Jun in the doorway. Did she find Natsume already? It's probably been less than a minute."
        ha "Did you already find...?"

        show jun basic_serious_close
        with chchange

        "Jun points at something near my feet."
        jun "I just thought of a better way to get a hold of her. Could you toss me Naomi's handbag?"
        "I take the handbag Naomi left near the nightstand and give it to Jun."

        play sound sfx_phonedial

        "She opens it, takes a cell phone out of it, quickly presses a few buttons and then puts it to her ear."
        "That's a pretty smart move. I don't have Natsume's number saved on my phone and apparently Jun doesn't either, but Naomi unsurprisingly does."

        scene ev seizure_bedroom_fit
        with locationchange

        jun "Natsume? This... ah... is Jun speaking. Something's happened to Naomi."
        jun "It's... ah... actually still happening as we speak."
        jun "No, we're in Hanako's room right now."
        jun "I'll tell her. Thank you."
        "Jun puts down the phone and turns back to me."
        jun "Natsume's on her way. She says that the best thing to do is to let the seizure run its course and not to put anything in her mouth or restrain her in any way."
        ha "Ummm... O-okay."
        jun "She also said that if the fit lasts longer than five minutes, you'll have to use this and then warn a nurse."
        "She reaches into Naomi's handbag and takes something out of it that looks a bit like a marker."
        jun "It's an injection pen that's applied to the thigh. It contains a rather strong anticonvulsant for emergencies."
        "I instinctively look at my alarm clock on the ground only to notice it's not displaying anything right now."
        ha "Ummm... W-when did this start?"
        jun "I'm... not really sure. I think 3 minutes ago."

        show ev seizure_bedroomfit_injector
        with charachangeev

        nvl clear
        nvl show dissolve

        n "I really hope Natsume gets here before it comes to that."
        n "Naomi isn't thrashing around as badly anymore, but she's definitely not lying nice and still, either."
        n "{vspace=60}I wonder if, nervous as I'm feeling right now, I'd be able to keep my hand steady enough to jab that thing in just the right place without messing up, especially with “the right place” twitching every second or so."

        nvl clear

        n "Without really thinking about it I put one hand on Naomi's thigh and make a few stabbing gestures with the other hand in an attempt to practice the motion. It is then that I suddenly notice something."
        n "{vspace=30}Naomi's inner thigh feels a bit moist and when I look down, my eyes fall on a dark stain on the blanket. My eyes widen in shock as I realize what happened and I can only barely suppress a gasp."

        nvl hide dissolve

        "Jun looks at me with a worried expression."
        jun "Is something the matter?"
        ha "N-no."
        "This is getting worse and worse. First my clubmate has an epileptic fit right in front of us. Then it turns out I might have to apply an injection in order to stop the seizure, and now I find out that Naomi has voided her bladder in the process. What's taking Natsume so long?"
        jun "Just one more minute. Is it... just my imagination or is she quieting down a bit?"
        "The twitches seem to start getting more infrequent. But there's still a trinkle of drool coming down her lips, and a small puddle has already formed on the pillow her head is resting on. I take a tissue from the box on the floor and start wiping Naomi's cheek."

        play sound sfx_doorknock

        "Just when I get started on the pillow, a knock on my door draws our attention."

        scene bg school_dormhanako
        show natsume basic_neutral_close at left
        show jun basic_disturbed_close at center
        with locationchange
        
        "A moment later, Natsume enters the room."
        nt "How is she?"
        "Jun makes a helpless gesture."
        jun "It might be better for you to have a look yourself. I'm afraid I'm not very familiar with this."

        show natsume basic_neutral_close at center
        show jun basic_disturbed_close at left
        with charamovefast

        "Natsume approaches the bed, and I consider moving over, but then I remember the stain on my blanket, and I decide that I can at least try to make sure Jun doesn't notice, so I remain in place trying to block the spot."
        nt "Was it like this the whole time?"
        "I shake my head."
        ha "N-no, it was... like it usually is in c-class."

        stop music fadeout 2.0

        "We remain silent for some time and watch as Naomi's convulsions become more and more infrequent until eventually they stop entirely."        
        "Just when I'm about to ask what to do now, we can see Naomi's eyes open just a little bit, and she lets out a soft moan."

        scene ev seizure_bedroom_groggy
        with locationchange

        play music music_moonlight fadein 4.0

        na "{cps=15}Ooh...."
        ha "Are y-you alright?"
        "Natsume positions herself close to Naomi's face and speaks to her in a soft voice."
        nt "It's okay. I'm here. So are the others."
        na "{cps=15}What... is... g-going... on..?"
        "There's more than a hint of fear in her voice and it pains me to hear the usually confident and up-beat Naomi talk like this."
        nt "You had a seizure. But it's over now. It was just a seizure."
        na "{cps=15}W-what... who...?"
        nt "It's over now. Do you remember where you are?"

        show ev seizure_bedroom_scared
        with charachangeev

        na "{cps=15}...n-no..."
        nt "Do you know who I am? Or who these girls are?"
        "She tries to open her eyes a little bit more and look in our direction, but when she does so there's no immediate sign of recognition."
        na "{cps=15}...no..."
        nt "Do you remember your name?"
        na "{cps=15}...n-no..."
        "The fear in her voice starts becoming more pronounced, and I can even sense a hint of panic. She sniffles before the next words leave her mouth."
        na "{cps=15}W-what... is going... on...?"
        nt "Just close your eyes and relax. Let it come back to you. It will. It always does."
        na "{cps=15}...but..."
        "I softly place a hand on her shoulder."
        ha "Just r-relax, Naomi. It'll be okay."

        show ev seizure_bedroom_sleep
        with charachangeev

        "As Naomi closes her eyes again while letting out a pathetic whimper, I whisper Natsume's name to try and get her attention. When she looks at me, I make a little gesture with my head towards Naomi's groin."
        "The fact that she closes her eyes and groans softly suggests that Natsume has gotten my meaning."

        scene bg school_dormhanako
        show jun basic_sad_close at left
        # TODO replace with serious expression
        show natsume hands_neutral_close at center
        with chchange

        "After some deliberation, she gets up and looks at Jun."
        nt "Jun, will you do me a favor? There's usually a nurse on duty in the dormkeeper's office, and otherwise there'll be one doing rounds outside. Could you go and give her a summary of what just happened?"

        show jun basic_confused_close
        with chchange

        "Jun looks a little puzzled."
        jun "Is it necessary to bring a nurse in here?"
        nt "No, but if we report this right now, Mutou won't be expecting Naomi to show up in class tomorrow morning, and it'll save me an explanation later. Just stress that the seizure is over and that the situation is under control."
        jun "Well... okay."

        hide jun
        with charaexit

        "Jun shrugs her shoulders and leaves the room."
        
        play sound sfx_doorclose

        "As the door closes, Natsume silently sighs."

        # show natsume hands_sad_close
        # with chchange

        nt "What a mess."
        "It is, in every sense of the word."
        ha "N-now what?"

        # show natsume hands_neutral_close
        # with chchange

        "Natsume thinks for a moment."
        nt "Do you happen to have a spare blanket?"
        ha "In my closet."
        nt "I'd like to use it. Also..."

        show natsume hands_neutral_close
        with chchange

        "She takes Naomi's handbag, takes a room key out of it and gives it to me."
        nt "I'd like you to go to her room real quick and get a few things from there. You're probably faster on your feet than I am. I need you to retrieve her pajamas from under her pillow and some clean undies..."

        show natsume basic_neutral_close
        with chchange

        "I blush a bit as Natsume casually peeks under Naomi's skirt."
        nt "...white ones if there are any. She keeps them in her dresser. There should be a washing bowl and a wash cloth in the bathroom next to her room."
        ha "Ummm... O-okay."

        scene black
        with locationchange

        "Trying not to think too hard about this, I leave my room and hurry over to where I believe Naomi's room is. Good thing we swapped room locations before drawing straws to determine where to hold our meeting."
        "A few minutes later, I return to my room with the items Natsume requested."

        scene bg school_dormhanako
        show natsume basic_neutral_close at center
        with charaenter

        "Natsume's still at Naomi's side, and Naomi's still lying completely still. She's obviously still very much out of it."
        "As I put the items I retrieved on my desk, Natsume gives an appreciative nod."

        play sound sfx_dooropen

        show jun basic_sad_close at left
        with charaenter

        "Before she can say anything though, the door opens and Jun comes back in. I instinctively move in front of the bed in order to prevent Jun from spotting the stain on my blanket."
        "Natsume coughes softly in order to get our attention."

        show natsume basic_serious_close
        with chchange

        nt "It'd be rude of me to ask you to leave your own room, but would it be a problem if you gave Naomi a bit of privacy? You can wait in her room if you like."
        "Jun and I both nod our heads in unison. I personally don't think this is something I'd even want to see anyway."

        show jun basic_serious_close
        with chchange

        # TODO add original dialogue here
        jun "Hey, would you mind carrying my laptop?"
        "When I walk out of my room with her laptop, I notice she's carrying my lamp and alarm clock along with her."

        scene black
        with Dissolve(1.0)

        if _in_replay:
            return
        else:
            stop music fadeout 2.0


    label .s3:

        $ set_window_tint(TINT_HANAKO)

        scene bg school_dormnaomi
        play music music_dreamy fadein 4.0

        show jun basic_sheepish_close at twoleft
        with charaenter

        ha "Wow."
        "After we got to Naomi's room, Jun plugged in the lamp only to conclude it didn't work anymore, even after swapping its bulb with the one from Naomi's desk lamp."

        show jun basic_pout_close
        with chchange

        "So she removed the fixture, started tinkering with the wires, and after putting the fixture and the bulb back in, my lamp was working again."

        show jun basic_happy_close
        with chchange

        jun "Your lamp is rather sturdy. The impact merely caused one of the wires to get loose."

        show jun basic_eyeroll_close at center
        with charamove

        show jun basic_eyeroll_close at twoleft
        with charamove

        "She takes my alarm clock and starts using a screwdriver from her laptop bag to get it open. I look at her in awe."
        ha "I... never realized you knew how to fix things like that."

        show jun basic_sheepish_close
        with chchange

        "Jun smiles humbly."
        jun "I'm not some sort of gadgeteer genius. I've just spent a lot of time around electronic devices."
        ha "A lot of time?"

        show jun basic_happy_close
        with chchange

        jun "My father runs a small store that sells consumer electronics, and he tended to take damaged devices with him to tinker with them before disposing of them."
        jun "I couldn't have any physically intensive hobbies, so he gave me my own devices to experiment with to pass the time. Flashlights, digital clocks, portable CD players, hairdryers...even an old Gameboy with a cracked screen."

        show jun basic_eyeroll_close
        with chchange

        "She points at her laptop bag."
        jun "I asked a laptop for my birthday a few years ago, but instead of buying one for me, Father started bringing discarded laptop systems home with him that I ended up salvaging for parts that still worked."
        jun "The system in the bag is a bit like Frankenstein's monster. There's stuff from at least four different systems in there."
        "Something tells me that Jun would have been a great fit for the science club, and if it had existed at the start of her first school year she may very well have ended up joining it instead of the newspaper club."
        ha "I'm impressed. Did you f-fix many of the things you were given?"

        show jun basic_smileclosed_close
        with chchange

        "Jun smilingly shakes her head."
        jun "I learned a lot from taking apart those devices, but especially in the beginning I often merely ended up putting those things out of their misery."

        show jun raise_laugh_close
        with chchange

        jun "I guess breaking stuff really is a second nature to me."

        nvl clear
        nvl show dissolve

        n "I smile awkwardly. Hearing Jun poking fun at her own condition sounds a bit off-putting to me, but she's hardly the only person around here with that habit. Naomi occasionally jokes about her epilepsy, and Lilly makes light of her own blindness all the time. Even Hisao has occasionally started making little jokes about his condition."
        n "I've never been able to poke fun at my own scarring. Do I simply lack a sense of humor, or is it the fact that others have made fun of my appearance so often that makes it seem inappropriate to joke about it? Lilly said that a little self-mockery can help you put things into perspective."

        nvl clear
        nvl hide dissolve

        show jun basic_weaksmile_close
        with chchange

        "While I'm pondering all of this and more, Jun has been examining the insides of my alarm clock, and she softly shakes her head."

        jun "I don't think there's much hope left for this alarm clock. The impact from Naomi's haymaker damaged several capacitors, so even if I got it running again, it would remain unreliable and lose power ever so often."
        jun "There's not much use for an unreliable alarm clock that resets itself every few days. You're better off setting your phone's volume to maximum and using its alarm function. At least until you can get another alarm clock."

        ha "Thanks f-for having a look. At least you got my lamp working again."

        show jun basic_confused_close
        with chchange

        jun "It's okay. I needed to do something to get my mind off what just happened anyway. That was really disturbing."
        jun "I wonder if we set it off in some way. Like... Maybe my computer screen triggered it?"

        ha "I... don't really think so. I think they just h-happen from time to time without needing to be triggered. Look at her room."

        show jun basic_serious_close
        with chchange

        "Naomi's room is pretty distinct. Unlike mine, it's very colorful with posters on several walls and tons of little touches to make it feel more personal. What's immediately noticable is the extremely thick carpet that covers pretty much the entire room."
        "Also, instead of a bed there's merely a futon on the floor and nearly half of that futon is covered with all sorts of plush toys including the toy Nessie I brought from Scotland for her."

        show jun basic_speak_close
        with chchange

        jun "I noticed. Maybe those plush toys aren't merely there to cushion her in case of a seizure, and she simply likes them, but this room seems geared at preventing injury in case she has an episode here. With a carpet this thick, she might not even need a futon."
        ha "It has to be difficult to keep it clean though."

        show jun basic_weaksmile_close
        with chchange

        jun "Yes. I wonder how they clean it after a seizure. It has to be a real chore to get the spots out."
        "Spots? I freeze and stare at Jun. Did she see after all?"

        show jun basic_confused_close
        with chchange

        jun "I... ummm... meant saliva spots."

        show jun basic_sad_close
        with chchange

        "The brief look we exchange has pretty much given it away though. I know that she knows, and she knows that I know. What follows is a short but uncomfortable silence that Jun eventually ends up breaking."

        show jun basic_sadclosed_close
        with chchange

        jun "So... ah... it seems like we both saw what happened."
        "I don't really know what to say, so I simply nod."
        jun "I wasn't completely sure myself until you carried in that washing bowl..."

        show jun basic_disturbed_close
        with chchange

        "She grimaces uncomfortably."
        jun "...that Natsume is using right now to... I suppose it's going to take a while before she's back to normal, and you don't let someone sleep a whole night in soiled undies, but it's still a bit..."

        show jun basic_sheepish_close
        with chchange

        "Those were my thoughts as well, though Natsume probably has her reasons. Jun grins awkwardly."
        jun "I heard a rumor about Natsume and Naomi once. That they're... together? This thing kind of plays into that, don't you think? Do you suppose it's true?"

        show natsume hands_annoy_close at center
        show jun basic_serious_close at left
        with charamove

        nt "Of course it's true!"
        ha "Ah!"
        "We both jump in surprise as Natsume comes walking into the room carrying a folded blanket and a plastic bag with what look like clothes inside. She has a scolding expression on her face, obviously having heard Jun's words."
        nt "And what I did just now was totally because I'm turned on by that sort of thing."

        show jun basic_smug_close
        with chchange

        "Jun blushes a bit, but also giggles at Natsume's obvious sarcasm."
        jun "It does sound rather silly when you put it that way. I hope I didn't offend you."
        nt "You didn't. I know the rumor. I just thought that only a certain part of the male student body attending here actually took it seriously. You know - the innocent manga-educated kind? "

        show jun raise_laugh_close
        with chchange

        "Jun laughs out loud."
        jun "Well, I often pretend to be an innocent manga-educated male whenever I go online. I suppose part of the mindset sticks around at times whether you like it or not."

        show natsume hands_neutral_close
        show jun basic_sheepish_close
        with chchange

        nt "There have been times when Naomi has helped me get dressed whenever my arthritis got so bad that I had trouble doing it myself, so she and I are fairly comfortable in each other's presence."
        nt "She's my best friend, but we're not in a relationship any more than Hanako and Satou are in a relationship. I think our friendships are actually very similar."

        show natsume basic_smile_close
        show jun basic_eyeroll_close
        with chchange

        nt "Heh... and maybe viewed in the very same light by the male student body until recently."

        "My heart promptly skips a few beats when I hear Natsume make that comparison. How have other students been looking at Lilly and me anyway?"
        ha "Ah... ummm... There w-weren't r-rumors about me, were there?"

        nt "A few, after you and Satou started hanging out together. I mean, you never really interacted with other people before around here, and then suddenly you started having lunch with Satou nearly every day in addition to visiting her room in the evening."

        show natsume basic_cheerful_close
        show jun basic_smile_close
        with chchange

        nt "Since neither of you had a boyfriend, how could you have been anything but lesbians? You had to have been, seeing that girls having tea and cookies together is not exactly tantalizing."
        ha "B-B-B-B-But...!"
        "THAT MAKES NO SENSE AT ALL!"

        show jun basic_smileclosed_close
        with chchange

        "Jun gives me an overly cheerful smile, obviously finding this conversation extremely funny."
        jun "At least you hooking up with Nakai must have quelled those rumors just a little bit, though I bet people are now wondering whether Satou is secretly part of the relationship or not."
        "Please be joking. Please be joking. Please be joking."
        ha "We're... j-just f-friends."


        show natsume basic_annoy_close
        show jun basic_sheepish_close
        with chchange

        "Natsume scrapes her throat."
        nt "Point is: if I were a lesbian, I probably wouldn't have done what I just did. I would have felt like a creep. This was simply a little nursing chore..."

        "I have to admit that in contrast to the way she was speaking to Naomi while calming her down, what I saw of Natsume's actual handling of things looked rather clinical and detached."
        "The few times I allowed Hisao to apply my moisturizer lotion for me, there was no way I would have mistaken his touch for that of a hospital nurse."

        show natsume hands_neutral_close
        show jun basic_serious_close
        with chchange

        nt "And can we maybe lay off that subject now and switch back to the reason we're here right now?"
        "That's more than acceptable to me. I quickly nod."

        ha "H-How is she right now?"
        nt "Sleeping like a baby. I managed to get her her jammies on, changed the blanket, and then I stuck around until her mind was clear enough to recognize me and comprehend the fact that she just had a seizure."

        show natsume basic_neutral_close
        with chchange

        "She looks at me."
        nt "I'm sorry to ask this of you, but would it be okay if Naomi spends the night in your room? It usually takes her brain some time to recover from a seizure, and she could use the rest right now."
        nt "You can spend the night here if you like. I retrieved your nightgown for you. You don't have to worry about Naomi going through your stuff."
        nt "She'd never betray your hospitality like that, and besides, she'll probably be too sore to even make it out of bed tomorrow morning though I'll try to help her make it to her own room after she's had a night's sleep."

        "I reluctantly nod. I guess I can stay here. Or I could simply ask Hisao if I can stay over."
        ha "O-Okay then."

        show jun basic_sad_close
        with chchange

        "Jun gives Natsume a worried look."
        jun "Is she always like that when she comes out of a seizure?"

        nvl clear
        nvl show dissolve

        n "I'm a bit curious about that as well. I learned at the first aid training that people who just had a seizure are often in a disorientated and confused state for some time afterwards, but since Naomi's usually carried to the nurse's office on a stretcher after a seizure in class has died down, I've never really seen the aftermath until today."
        n "It was kind of disturbing to see Naomi act like a lost and frightened little child rather than the bundle of energy she usually is."

        nvl clear
        nvl hide dissolve

        play music music_moonlight fadein 4.0

        show natsume basic_annoy_close
        with chchange

        nt "Most of the time. She usually suffers from brief memory loss after the seizure ends and waking up not knowing what happened, where you are or even who you are can be really terrifying to a person."
        nt "That's why I asked you not to get a nurse. I figured leaving her in an unfamiliar room with a person she doesn't know would discomfort her even more."

        show jun basic_confused_close
        with chchange

        jun "Speaking of discomfort, has that... ah... thing with the bedsheets happened before?"

        "Natsume stares at the floor for several seconds before replying."
        nt "Never in class, and I thank my lucky stars for that. It's happened twice or thrice in my presence over the years, and if there have been other occasions, I doubt that Naomi would have told me about them."

        show natsume basic_sad_close
        with chchange

        "Natsume's expression takes on a tinge of sadness."
        nt "Those epileptic fits are demeaning enough as they are, but I think that for the most part Naomi's resigned herself to the fact that they happen to her from time to time. But this is... different."
        nt "After the first time this happened with me present, Naomi spent a good deal of the week avoiding me, and even afterwards she was really awkward with me for some time."
        nt "I had been hoping to save you two the trouble of having to deal with that by cleaning things up before she became aware enough to notice what happened."
        nt "This night's events will probably remain a big blur in her mind, so if you two don't slip up, she won't ever know what happened other than the fact that she had an episode. Ignorance can be bliss sometimes."

        show jun basic_sad_close
        with chchange

        "Jun and I nod understandingly."
        ha "I w-won't tell anyone."
        jun "Me neither. I guess some things are bad enough to even embarrass Naomi."

        show natsume hands_smile_close
        with chchange

        "Natsume gives Jun an amused smirk."
        nt "This may surprise you, but Naomi's actually quite self-concious about how others perceive her."

        show jun basic_serious_close
        with chchange

        "Judging from her expression, that does indeed surprise Jun."

        show jun basic_speak_close
        with chchange

        jun "She doesn't come across as someone who ever keeps a low profile."

        show natsume basic_neutral_close
        with chchange

        nt "You have to remember that it's impossible for someone like Naomi to be completely inconspicuous, whether she likes it or not."
        nt "Even if she goes out of her way to avoid attracting anyone's attention, it's usually only a matter of time before her condition kicks in and forces her to create a public spectacle."
        nt "So it's not so much the question whether Naomi ends up sticking in people's minds or not, but merely for what reason."

        show jun basic_confused_close
        with chchange

        "Jun raises an eyebrow."
        jun "Are you saying that Naomi goes out of her way to define herself to people before her condition has the chance to do it for her? Even if it means acting a bit like a goofball at times?"

        show natsume hands_smile_close
        with chchange

        "Natsume nods."
        nt "Naomi's worst fear is probably that people end up remembering her merely as that one girl who has fits in class."

        show natsume basic_neutral_close
        show jun basic_serious_close
        with chchange

        jun "I see."

        nvl clear
        nvl show dissolve

        n "There's a momentary silence as Natsume's words sink in. I don't know about Jun, but what Natsume said about Naomi resonated deeply with me. I wonder for a moment how the people from my former schools remember me."
        n "There's no doubt in my mind that I'll live on in their memories as just that one panicky recluse with the hidious scars on her face. They might remember the nicknames they made up for me, but I don't think anyone remembers my actual name anymore by now."
        n "For a long time, I was probably headed for a similar fate here. With luck, I'll be able to avoid that this time."

        nvl clear
        nvl hide dissolve

        "Jun absentmindedly fiddles with her screwdriver a bit before turning to Natsume."

        show jun basic_speak_close
        with chchange

        jun "Doesn't Naomi take medication to prevent those episodes?"

        show jun basic_serious_close
        show natsume basic_sad_close
        with chchange

        nt "She does, but most of the medication she's tried so far has only been able to decrease the frequency of her episodes. If she was able to suppress her seizures completely, I don't think she'd be attending here."
        nt "She's tried a lot of different meds over time, but most either didn't work or forced her to deal with very unpleasant side effects. One of the few treatment drugs that seemed to work for a while nearly ruined her social life in the past."
        ha "Her social life?"
        "Natsume nods."

        nt "One of the drugs she tried seemed to work at first, without immediately noticable side effects like skin rash or drowsiness, but it later turned out that the dose she needed to keep her episodes at bay had an effect on her mood."
        ha "You mean it made her depressed?"

        show natsume basic_annoy_close
        show jun basic_sad_close
        with chchange

        nt "No, more like agitated... irritable. Kind of like a permanent case of PMS. It started to take an ever increasing strain on her relationships."
        nt "After a falling out with one of her best friends, she decided that having fits in public was still better than not being herself anymore and other people believing her to be someone she isn't."
        "I'm not really sure what to think about that. Naomi always made the impression on me of being someone who didn't care what others thought of her. But judging from what Natsume just said, it seems like deep inside she cares very much about that."
        "Before this meeting I remember being very anxious about making a bad impression and straining my relationship with Naomi and Jun. Now I start wondering whether Naomi was perhaps just as worried as I was and just didn't show it."
        "We sit there in silence for a few minutes, and then Natsume slowly gets up."

        show natsume hands_neutral_close
        show jun basic_sheepish_close
        with chchange

        play music music_twinkle fadein 4.0

        nt "Perhaps it would be a good idea to call it a night. Thank you again for letting Naomi use your room, Hanako. I'll wash your blanket for you together with Naomi's clothes, so don't worry about that."
        nt "I'll also go over there tomorrow morning and make sure she gets back to her own room. I might be a little bit late in class, but when Mutou reads the nurses' night report I don't think he'll make a big deal out of it."

        show natsume hands_smile_close
        show jun basic_smile_close
        with chchange

        ha "T-Thanks. What about Naomi?"
        nt "Well, it's Saturday tomorrow, and we'll only have classes until noon. Naomi often says that after a hefty seizure, her muscles feel like she jogged up Mount Fuji in one go."
        nt "I suspect the trip from your bedroom to hers will be all the physical effort we can expect out of her tomorrow."

        show jun basic_eyeroll_close
        with chchange

        "I exchange a glance with Jun. She nods as if she just read my thoughts."
        ha "Ummm... M-maybe we c-can v-visit her tomorrow after classes and... keep her company?"

        show natsume basic_cheerful_close
        show jun basic_smileclosed_close
        with chchange

        nt "You should. I think she'd really like that. Just be prepared to hear her complain every ten seconds or so about how sore her muscles are."
        ha "O-Okay."

        show natsume basic_smile_close at offscreenleft
        with charamove
        hide natsume

        "Natsume says her goodbye, promising me I'll be able to get back into my own room before classes start tomorrow. After she leaves, Jun also starts getting up."

        show jun basic_sheepish_close
        with chchange

        jun "I'd best be going as well. We both had a rough evening."
        ha "Are you... okay now?"

        show jun basic_happy_close
        with chchange

        jun "Yes. I was just a little freaked out when it happened, but I'm fine now."

        show jun basic_annoyed_close
        with chchange

        "She sighs."
        jun "When you think about it, that epilepsy of hers is a pretty messed up condition. It's not just the seizures and the memory loss and the medication and that incident with your blanket."
        jun "If you look at this room, you can tell that it's geared towards someone who could go into convulsions almost completely at random. That's gotta be so creepy. You take a bath, you risk drowning. You walk up a staircase, you risk breaking your neck. How does she put up with it?"
        "By joking about it and living her life to the fullest without worrying too much, it seems."
        ha "With... a s-smile, I think. Knowing her..."

        show jun basic_pout_close
        with chchange

        jun "I wouldn't want to trade places with her. My condition isn't exactly a blessing, but I'd still take mine over hers, thank you very much."
        ha "..."

        show jun basic_sheepish_close
        with chchange

        "Jun opens the door, but before she walks out, she turns around and smiles awkwardly at me."
        jun "This sure was an unusual first meeting, was it not? I wonder if this is going to be a regular occurrance."
        "I giggle."
        ha "I hope not."

        show jun basic_eyeroll_close
        with chchange

        jun "I've been thinking..."
        ha "Yes?"

        show jun basic_smileclosed_close
        with chchange

        jun "Maybe 'The Broken Quills' isn't such an inappropriate name for us after all."

        show jun basic_laugh_close
        with chchange

        "We both let out a laugh, mostly as a relief from the insanity of this evening."
        ha "M-Maybe not... Shall we tell Naomi tomorrow that we accepted her suggestion?"

        show jun basic_smileclosed_close
        with chchange

        jun "Let's do that."

        scene black
        with Dissolve(2.0)

        pause 1.0

        scene ev pillowtalk_39_1

        ha "Hisao?"
        "I softly whisper the name of my boyfriend, but receive no reply. He's probably asleep already."
        "After Jun left, I realized I didn't really feel completely comfortable spending the night in an unfamiliar room, so I snuck into the boys' dorm and asked Hisao if I could stay over, which he had no problems with."
        "Now that we're lying in bed, I'm absentmindedly fiddling with my hair as I'm thinking about the events that took place this evening. Especially Jun's words after Natsume left have been nagging me almost non-stop."
        "(My condition isn't exactly a blessing, but I'd still take mine over hers, thank you very much.)"
        "I didn't tell her that, but my first reaction to her statement was to agree with it. It took me a while to let that sink in and realize how shocking that was."

        "I'm not particularly happy with the way my life has turned out. There's nearly a decade of my life that I'd like to erase from my memories if such a thing was possible, and I'm not even 20 yet."
        "Unlike Lilly, Hisao, Jun and Naomi, people only need a single glance at me to be able to tell that something's seriously wrong with me. I'll have these scars for the rest of my life."
        "Even though it's no longer as bad as it used to be, I'm also still a nervous wreck at times who gets panicky about stuff that other people wouldn't even think twice about."
        "I have very few people in my life, and I tend to anxiously avoid those I'm not familiar with. My scars come with their own set of physical limitations. All in all, my life's hardly enviable."
        "And yet..."

        scene ev pillowtalk_39_2

        "Would I want to trade my life with any of them? Would I want to walk on eggshells all the time like Jun, knowing a casual misstep could severely injure me and spend a large part of my life dealing with one bone fracture after another?"
        "Or Natsume, who has to deal with chronic pain and stiffness of her joints on a regular basis even though she's in the prime of her life?"
        "How about Naomi, who has to deal with the combination of sudden dramatic seizures that make her the center of unwanted attention whenever they happen and medication that she doesn't always react well to?"
        "Would I want to trade places with Lilly, who can only navigate places unsupervised if she's memorized the layout? Who is dependant on others for several basic things and who can never read normal books or watch movies?"
        "Do I envy Hisao his life, who is regularly confronted with his own mortality, has to take a truckload of medication every day and who knows that a sharp shock, excertion or simple scare could kill him?"

        scene ev pillowtalk_39_3

        "I'm not really sure anymore. I probably have more trouble functioning in everyday life than any of my friends, and yet my life may very well be a lot more normal than theirs in a decade or so."
        "That notion keeps whirling around in my head for quite some time. Before sleepiness finally gets the better of me, one thought sticks in my mind, and to my surprise it is accompanied by a sense of curiosity rather than anxiety."

        scene ev pillowtalk_39_4

        "I wonder what my life will be like a few years from now on."

        scene black
        with Dissolve(2.0)

        if _in_replay:
            return
        else:
            pause 2.0

    return