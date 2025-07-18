label sh_ch28:
    label .s1:

        $ set_window_tint(TINT_HANAKO)

        call sisterhood_timeskip

        scene bg inverness_shore
        with nextchapter

        play music music_dreamy fadein 4.0
        play ambient sfx_waves fadein 2.0 volume 0.6

        ha "I guess they're not here."
        "I put the binoculars down and giggle softly to myself. The idea that the “friends” I’ve made today would follow me all the way back to the shore near the Satou home is really childish, but a girl can dream."
        "I take a look at my watch and notice it's half past eight. Hisao will still be busy for more than half an hour. Lilly and her mother will be gone for the rest of the evening and if last week was any indication, the same will be true for Lilly's father."
        "I could go back to the mansion and read some more, but I kind of like it here."

        nvl clear
        nvl show dissolve

        n "This quiet place at the shore of the bay has become my private retreat spot."
        n "{vspace=60}Karla's suggestion of keeping a journal turned out to be a pretty good idea and each day, some time after dinner, when Hisao goes up to the attic to use Karla's home trainer in order to keep his practice regimen going, I use that time to take a little private walk along the shoreline of Moray Firth, sit down here, collect my thoughts and write them down."
        n "The soft sound of the waves, the gentle breeze and the sight of the sun setting in the distance all serve to put my mind at ease."

        nvl hide dissolve

        play sound sfx_paper

        "I thumb through the pages of my notebook. I decided to reject Karla's idea of turning it into a private newspaper and go with a more personal angle. That also meant this diary's for my eyes only."
        "Not immediately knowing anything else to write, I decide to re-read what I've already written and see if anything comes up that's worth writing down."

        call screen sh_diary(
            _("Day 1\n\nThis day was almost entirely spent getting from Yamaku to the Satou residence in Inverness, Scotland. We assembled in Lilly's room in the morning, took the bus directly to the train station and then the train to the airport. We made sure to plan ahead for unexpected delays, but in the end it all ran smoothly. We made sure to do our baggage checkin as soon as we arrived and wasted no time getting through security. We went for something to eat and then hurried along to the gate. It turned out they let us board the flight before anyone else in economy class.\n\nThe flight itself took a long time, nearly 13 hours. London airport was even busier than Narita and it was quite the trip to the gate of our next plane. Fortunately, the second flight only took about an hour and Inverness Airport was really small compared to the other ones. When we left the building, Akira was already waiting for us. She drove us to the Satou residence."),
            _("\n\nSince we had already eaten something in London, we didn't waste any time getting to bed. After a trip that took nearly a day, we'd certainly earned it.\n\nMusings:\nI wasn't looking forward to this day to begin with, but my first experience with the hassles of air travel was worse than I thought. If we take a walk into the city, I can at least tell myself that those crowds aren't going to bother me if I just keep my head down and stay on the move. Not so much here. The idea that there are people at every airport who are being paid to keep a look out for travellers showing ‘unusual’ behavior creeps me out like nothing else. Then there's the security gates. It's a bit depressing to have pretty much the whole world make it clear to you for nearly a decade that the sight of your face is an affront to their sensibilities, and then they still insist on you showing it completely unobscured.")
        ) with dissolve

        call screen sh_diary(
            _("\n\nAll in all, this was not a good day for me. I can't comment on much of the flight as I've been asleep for the biggest part of it.\n\nAddendum:\nNow that I've been here a few days longer, I feel that I should mention that although I still dislike airports, I do think this vacation has been worth the stress of navigating them so far. Also, what Lilly said about how special an experience your first takeoff is couldn't be more on the mark. In fact, the second one wasn't any less exciting. It's hard to describe the feeling I got when the plane left the ground, and I could see the world slowly shrink beneath us until the only thing visible through the window was that ocean of clouds all around us. It felt... liberating in some way. As if I was leaving an old part of my life behind me and was on the edge of something new and exciting. I guess I'm doing just that—if only temporary."),
            _("\n\nSo I suppose it wasn't all bad, though I still dread going through customs and security again when we return to Japan.")
        )

        call screen sh_diary(
            _("Day 2\n\nI learned something new about myself this morning. I'm pretty much immune to jet lag. I woke up around ten o' clock feeling fit as a fiddle. It seemed I was the only one. I took a long shower, applied my moisturizer, and decided to try and finish “The Temple of the Golden Pavilion” that I started on while on the plane to London. I could have gone exploring the house, but I preferred Lilly to be there when we'd introduce ourselves to her parents. I can't afford to make a poor first impression. I finished almost the entire book AND got several ideas for my article before Hisao finally woke up. It turns out he and Lilly had been awake for most of the night. The dinner we had at the start of the evening was delicious and much, much better than the food on the plane. Akira then came to pick us up to spend the evening inside a real Scottish pub."),
            _("\n\nThe atmosphere there reminded me of that visit to the jazz club before Hisao and I started dating. Lilly and Akira took part in and won a pub quiz, while Hisao and I took part in and both won a billiards game. Also, we met Lilly's mother! We just didn't know it was her at first. Back at the Satou residence we tried out the wine that Lilly won, hung out together and then went to bed.\n\nMusings:\nWow, the Satou residence is really large. I wonder if it doesn't feel extremely empty with just two people living there. Maybe that's secretly part of the reason they have housekeepers. Lilly's been trying to warm us up to the idea of exploring Inverness on our own. I don't think I'm confident enough yet to try a stilted conversation with some locals in order to ask for directions, but Hisao's English isn't going to get us out of a jam either.")
        )

        call screen sh_diary(
            _("\n\nI think Lilly's enjoying the idea of us having to practice our English skills the hard way far more than she should. The town of Inverness is really impressive. The older buildings look so different from the ones in Japan. It's really starting to feel like we're on vacation.\n\nLilly performed a toast. I really envy her bond with Akira. They seem so close. Also, Akira suggests their parents are both workaholics. It explains why they couldn't pick us up from the airport the other day. Interesting tidbit: Lilly learned most of her homemaking skills from their old housekeeper. I wonder if she'd be comfortable with Akira telling us that. Billiards is great fun, but much more difficult than pool. Fortunately, this was a first time for both of us playing it."),
            _("\n\nI told Hisao about what I'd like to do. Hisao has already figured out where he's going to go after graduation. I wonder if there's a university in his hometown of Chiba that I could attend. If we end up studying in different towns, maintaining our relationship is going to be really difficult. Also, meeting Lilly's mother was unexpected. Looks like she was toying with us a bit. I feel a bit embarrassed for not having made the connection myself because the family resemblance is quite striking. I wonder if this is what Lilly will eventually end up looking like when she's older. If so, she's a lucky person. There'll be a picnic tomorrow, and Lilly wants me to help her prepare the food. Hurray!")
        )

        call screen sh_diary(
            _("Day 3\n\nI woke up feeling extremely sick this morning. Shower didn't help much. Fresh air didn't help much. Swearing to my ancestors to never ever drink again didn't help much. I guess I really deserved this. At least I'm not the only one. Lilly and Hisao were apparently in bad shape too. Lilly got in trouble for passing out on the couch—AFTER her parents already escorted her upstairs. Hisao and I had sandwiches for breakfast, filled with meat, lettuce and tomato. It was really hard eating them while resisting the urge to throw them back up, but Hisao said they'd make us feel better. In the end we decided to sleep for a few more hours. Fortunately, I felt seriously better around noon. Lilly and I spent nearly an hour preparing picnic food which was fun and a good way to distract myself from the painful sensation in my head. Lilly's mother brought tandem bikes along. Riding them was a bit like playing that motorcycle arcade game with Hisao. It was tricky but fun. At first."),
            _("\n\nWe ended up visiting some old battlefield, but I didn't quite catch most of what Lilly's mother told us about it. I got unwell during our bike ride, but it was kind of my own fault, so thankfully the picnic didn't end up cancelled over me. We learned that the company of Lilly's family makes medical equipment. And that Lilly's mother was told to come to Scotland just like Lilly was, though unlike her daughter she didn't end up staying at the last moment. I wonder how things would have played out if that had been the case. Also, Lilly's mother used to be a journalist. I got some nasty cramps near the end of the picnic, so Lilly's mother ended up calling the housekeeper to pick us up. I was given A LOT to drink during the picnic and over dinner that evening. I ended up going to bed early that night to recover from today.")
        )

        call screen sh_diary(
            _("\n\nMusings:\nI really should have remembered last night how terrible I felt that morning after I had wine for the first time, because apparently that first hangover didn't make enough of an impression to prevent me from making the same mistake again. I was worried things'd be awkward between Hisao and myself for the rest of the week, but fortunately we managed to settle things before we went on that picnic today. If I learned any lesson today it's that I should maybe worry less about Hisao and more about myself. Hisao may not take well to hot weather, but I don't either, and I was reminded of that today. Lilly's mother said it was heat exhaustion and she was probably right, but I think my body temperature was also just a little bit too high. It's been years since I've last experienced any real heat-related afflictions, so I guess I was becoming forgetful about the fact that I'm prone to them."),
            _("\n\nI suppose this is what happens when you suddenly start getting out more after years of being a shut-in. I'd better be more careful in the future, lest it's me who ends up in the hospital here.\n\nWe also got to know Lilly's mother a little bit better today. She's apparently head of PR at the family company. She was relaxed enough while talking about the business, but I noticed she got tense when she talked about following her husband to Scotland. That's obviously still a sore point that she seemed eager to skip over. When my activities in the newspaper club came up, Lilly suddenly fished our latest newspaper out of her bag. What on earth? Hisao likes to say Shizune is the scheming type, but I'd say it runs in the family. If Lilly's intentions hadn’t been so good, these kinds of stunts would have scared me.")
        )

        call screen sh_diary(
            _("\n\nAnd Lilly's mother used to be a journalist. How neat is that? And she likes to talk about it. A lot. Her enthusiasm on the subject is a bit overwhelming, but it's also pretty contagious. She suggested me to start keeping a journal and even gave me an old notebook to use. I decided to follow her advice, so from now on I'll be writing a little bit about each day I'm here, and I'm going to write a bit for the first two days as well."),
            _("Day 4\n\nBefore heading to bed last night, I was told that we'd be taking it easy for today, and I could sleep in to my heart's delight. I'm not someone who sleeps in a lot, but I did end up staying in bed until nearly noon. Not so much because I had trouble waking up, but because I decided to wake up my sleeping boyfriend in the only way that's appropriate when you're in a large bed, it's a beautiful sunny morning and you have plenty of time to spare: lazy morning cuddling. I didn't mind the fact at all that one thing lead to another. All in all, I had a great morning.\n\nI was given my own tour of the house this afternoon. It's a really nice place. I asked if I could take some photos of its interior. Lilly and her mother said that was okay, and I could go anywhere I wanted. Maybe I'll do that tomorrow morning. Or some other time when it's still daytime but there aren't many people around.")
        )

        call screen sh_diary(
            _("\n\nIt'll be interesting to view my photos side by side. If I show pictures of the Japanese rooms to people, they might not believe they were made in the same house as the other ones. I also found out today that Lilly's mother has a home trainer that Hisao will be using for his daily practice.\n\nAround four o' clock in the afternoon, we took a trip into the city to walk along the river Ness and visit St Andrews Cathedral. It was a beautiful church, though we didn't really get a lot of information on its history. I suppose it's still a church first and a tourist attraction second. The warmest part of the day was already over by the time we went into the city, but Lilly's mother nevertheless gave me her sun hat and said I could keep it for the remainder of my stay."),
            _("\n\nMusings:\nFirst of all, I really love the sun hat. It has a pretty wide brim, so it does an excellent job at hiding my facial scars and during the warm months it's more fitting than my own hat. It's also really elegant, and Hisao says that I look cute while wearing it. What more could I possibly wish for?\n\nLilly's mother really got going when the subject of her former job came up yesterday, and I was a little overwhelmed at first, but now that I've had a night to sleep on it, I think there was a lot of useful advice in what she said. I should ask the teacher in charge of the newspaper club, Mister Hoshino, if there's a study like the one Lilly's mother mentioned yesterday. I just hope I can work up the nerve to approach him about this. Then there's the career paths. My head was spinning when Lilly's mother was rattling off job options.")
        )

        call screen sh_diary(
            _("\n\nI think fiction writer would be a dream come true to me. I've taken in so many books—how wonderful would it be to be able to return some of that. But Lilly's mother had a point in that it might not be the most stable career, and I think I really benefit from having some stability in my life. Maybe at some point when/if I share a home with someone who has a monthly income himself. (is it too early to be hoping for something like that?)\n\nTechnical writer seems like a solid and stable career, but I wonder if that kind of writing isn't too cold and lifeless for me. There's no personality in good technical writing. Biographer or ghost writer would be exciting. Imagine working closely with some celebrity who tells you all kinds of intimate things about his life that the rest of the world doesn't know about yet. But then you'd probably need a network and contacts in order to even get someone to approach you for such a job."),
            _("\n\nI wonder what it would be like to be a speech writer. Imagine seeing hundreds of people listening to someone giving a rousing speech and knowing those people are really listening to and applauding your words. In the end though, copywriter or content writer may be the jobs that are easiest to get.\n\nI can't really shake what Lilly's mother said about working with other people in order to work around your own shortcomings. Would I be able to practice journalism if I had someone like Naomi to do the interviews with me or for me and let her do the talking while I do the writing? That might just work. Lilly uses all sorts of tricks to work around her limits. Maybe I should take a page from her book and do the same. I wonder if Naomi would be up for a duo interview some time. I could always go into editing if things don't work out.")
        )

        call screen sh_diary(
            _("\n\nI can't believe I'm thinking about all these things. Not too long ago I had no clue on what to do with my life after Yamaku, and now I'm trying to eliminate options that all look attractive. I guess it's about time though. Lilly and Hisao already have their career path largely figured out. I can't lag behind too much. In the end, it probably doesn't matter if I don't have one particular job in mind at this point. If I know what study to go for, I'll probably have plenty of opportunities to see where my interests lie. Like Hisao. Still, I wonder if I should have another talk with Lilly's mother about all of this. Will it look weird if I approach her? Will I even be able to pull that off without turning into a stammering mess? Maybe it's better to ask Lilly to break the ice for me. I don’t think she’d mind."),
            _("Day 5\n\nToday is the first day Hisao and I have gone out without being accompanied by Lilly. We spent last evening preparing for today. We packed our lunches, the tourist guide and a map of the city and surrounding Highlands area. Lilly's mother gave each of us a bus card that we can use to take any of the bus lines in the area without having to pay the driver. I was a bit nervous to go out there without Lilly or her mother accompanying us, but the fact that Hisao was also a bit uneasy was a small comfort. Lilly's mom told us we could always call if we weren't sure how to get back. Good thing it didn't come to that. I'm not even sure how much reception we'd have in the middle of nowhere.\n\nHaving focussed on the cultural sights over the last two days, Hisao and I decided to get away from the city and take a nature-viewing trip for a change."),
        )

        call screen sh_diary(
            _("\n\nWe took the bus from the area near the Satou residence to the bus station in the center of Inverness and then took another bus to our destination. That bus ride took quite long - almost an hour. Fortunately, the bus drivers have been really helpful so far. When we show them our bus cards and then point out our destination on the map we brought along, they usually give us a little notice when we reach the bus stop where we need to get off.\n\nOur destination for today was the hamlet of Tomich far to the south-west of Inverness. The village was built in a very charming style. It's called the Victorian style; named after one of the queens who ruled in that era. It seems most of the village's buildings used to be part of the local nobleman's estate, though the manor itself is now a ruin."),
            _("\n\nFun fact: the first golden retriever was bred in this village. The nobleman who lived here needed a dog who could retrieve game from almost anywhere during the hunt, be it the ground or a lake. (of which there are plenty in the area) So he ended up breeding a dog breed that loves both water and playing fetch.\n\nThe main attraction around here was the awe-inspiring waterfall slightly south of the village called Plodda Falls. We spent a lot of time just staring at it and taking pictures, and then we had a little picnic (nothing big this time, just the lunch we packed) near the falls. We spent the rest of the afternoon taking strolls through the nearby woods. It was really beautiful around there and so peaceful as well. Eventually we took the bus back to Inverness. We made our way back to the Satou residence without messing up, so kudos to us.")
        )

        call screen sh_diary(
            _("\n\nHere's hoping we can keep this going. Also, before we went to bed this night, we met Lilly's father.\n\nMusings:\nLilly's father and mother are really different. I don't think the saying “opposites attract” applies to Hisao and me, but it certainly seems true for them. I’ve always pictured Lilly's father as an intimidating figure who ruled his household with an iron fist, but he's actually not that bad; just a little bit stiff and stern. Okay, maybe more than a little stiff in his manners. He's also extremely polite and formal—much, much more so than Lilly. I don't think we'll be calling him by his first name anytime soon. It just doesn't seem appropriate.\n\nHe welcomed us to Scotland when we were introduced and told us to consider his home our own for the duration of our stay."),
            _("\n\nThen, he excused himself and retired to his study. From what I've heard, he's going to take a few days off within a week or two to spend some time with Lilly just like his wife has been doing, but in order to be able to afford that time off during this busy period at the office, he's been working massive overtime on an almost daily basis to compensate. He made a rather tired and restless impression on me when we met him. I hope he isn't going to burn himself out for our sake. I don't think Lilly would want that.")
        )

        call screen sh_diary(
            _("Day 6\n\nHisao and I went to visit a castle today. There are several of them around the area near Inverness but the closest one, called Castle Stuart, has been turned into a hotel, so we couldn't really go there. Fortunately there was another one nearby; to the north-east of where the Satous live. It's called Cawdor Castle. The required bus trip was fortunately a lot shorter than the one to Tomich yesterday.\n\nCawdor Castle is really impressive. It feels like a place right out of a storybook. Speaking of which, this castle was apparently the home of the protagonist in one of Shakespeare's most famous plays. I haven't really read any of Shakespeare's works, though Lilly's mother gave us a brief summary of the story this morning. It turns out that the real Macbeth never lived at this castle because it wasn't built yet when he was alive, though lots of tourists who visit this place don't seem to be aware of this."),
            _("\n\nWe spent about an hour touring the castle and spent the rest of our time there walking the nature trail nearby and the castle's various beautiful gardens. I think our little walk through the flower garden was one of the most romantic moments of our vacation so far. Despite having brought our own lunch, we actually ended up buying a meal at the snackbar near the bus stop since I gave most of my sandwiches to the ducklings swimming in the nearby pond. I managed to lure a few of them close enough for a photo. They looked so extremely cute I still smile whenever I picture them in my mind. I can't wait to have that photo printed out.")
        )

        call screen sh_diary(
            _("\n\nMusings:\nWhile browsing through the camera's memory, I found out something embarrassing. Apparently Hisao took a picture of me while I was asleep in our bed. Perhaps he thought I looked cute while sleeping. That wasn't really the issue though. The problem was the fact that I wasn't wearing anything when he took that picture. The bedsheet covered most of me, but I could still see my face, my shoulders and the top of my back. Has he forgotten that this camera belongs to the newspaper club? What if Naomi had found that picture? I don't think she's the type to use this kind of thing as blackmail material against me, but I'd still have to deal with a spell of excruciating embarrassment."),
            _("\n\nOn that note, as of this week our “love life” seems to be back on track. I think I'm going to miss our bedroom here when we return to Japan and have to get back to sleeping in a cramped single bed, sneaking around the dorm in order to stay over at each other's place and worrying about bumping into each other's neighbors the morning after. Best to enjoy the time we have here.\n\nNote to self: don't leave my birth control pills anywhere near Hisao's collection of medication. He nearly took some by mistake. Hahaha, that'd have been awkward.")
        )

        call screen sh_diary(
            _("Day 7\n\nNaomi will be pleased. A true Scotsman has been spotted and photographed. Not just that but we also got to see how these traditional Scottish garments are made. We visited the Scottish Kiltmaker Visitor Center as well as a shop specializing in Highland clothes today. In addition to the the exhibition there was also a viewing area where we could see craftsmen at work creating these pieces of clothing. It turns out there is no such thing as THE Scottish kilt; each clan used to have its own pattern as well as an accompanying belt with the clan sigil on the buckle and a decorated pouch (it has a name but I forgot what it was) to make up for the fact that kilts have no pockets. While we were at the Highland dress shop, Lilly and I also took the opportunity to try on a few Scottish dresses. I don't think anyone would ever mistake me for a local, but I the dresses looked very natural on Lilly. Hisao snapped some nice pictures of this event."),
            _("\n\nThere were a few nice affordable dresses there, but I don't think there'd be a point in me buying one. They stand out so much that I'd never be able to get myself to wear one in public.\n\nMusings:\nI almost filled up my first memory card today and I'm thinking of having a few photos printed out when we visit the shopping center here. Of course, lots of the photos are about the same things shot from a slightly different angle, but I've nevertheless managed to capture most of my vacation on camera so far.\n\nMy vacation...\n\nAside from that long weekend in Hokkaido, I haven't had a real vacation in a decade. There were dates with Hisao or outings with Lilly that I enjoyed, but this feels different somehow.")
        )

        call screen sh_diary(
            _("\n\nOr maybe I simply feel different. I'm not sure when it started; perhaps when Lilly's mother started talking about writing and journalism? Or maybe when I started keeping a journal and actively using my camera? It hit me today while I was browsing through the pictures stored on the camera already. I'm in quite a few of the pictures myself. To most people that would be logical, but that's not the case for me. I don't think there are many photos of me in existence at all. Most of the ones that existed before the fire were destroyed when our house burned down. I never liked the idea of people staring at a picture of me any more than people staring at me directly, so I’ve always tried to avoid being caught on camera whenever possible, even if that involved skipping class. I don't appear in the class photo of class 3-3 nor in any of the pictures from earlier years."),
            _("\n\nYet during this week I've allowed myself to be photographed more often than in the preceding 10 years combined. And I'm writing about everything that's happened too. Photos used to be nothing more to me than a painful reminder of my disfigurement, but the ones recently taken are different. They're reminders of things I enjoyed. I realize now that that's probably also why I'm keeping a diary. I'm busy making memories. That's kind of new to me as well. When I still lived at the orphanage, I survived by focussing completely on the present. I tried to forget the events of yesterday and tried not to think about what would happen tomorrow. (both were often painful) And yet what I'm doing right now is doing what I can to make sure I won't forget what's happened here in Scotland so far, and I find myself dwelling on what the future will bring even at times when I'm trying to just enjoy the moment.")
        )

        call screen sh_diary(
            _("\n\nI realize I'm rambling. A lot is going on inside my head right now, and it's overwhelming and confusing me at times, but I don't think I completely hate it. I hope that by writing all of this down I can give it a place and then try to make sense of it later.\n\nOn a final note, when re-reading my recollection of the first day, I realize I maybe wasn't being completely fair. I did like the flight itself and our stay here so far has definitely been worth the stress of the trip so I'm going to try and write something positive about it after I finish this page. Maybe that's the key to sorting out my life. Writing down the precious memories and taking pictures of them in order to to keep them alive that way while letting the bad memories fade with time.\n\nHmmm..."),
            _("Day 8\n\nToday was another day off. We decided to go shopping in Inverness. There's an indoor market built in Victorian style located near the Ness. It's a really nice looking place filled with all kinds of small owner-operated shops, and the archways and colorful shop facades give the place an atmospheric old-fashioned charm. It was a little more crowded there than I would have liked, but my sun hat did a good job at obscuring the right side of my face. Among the shops we visited were candy stores, a bagpipe store (those things are really expensive!), several tailor and clothing stores and a few gift shops. (I got Naomi a toy Nessie from one of them as a thanks for letting me borrow her camera. She did want to see the Loch Ness monster after all.) We also bought ingredients for tonight's dinner. Lilly and I will be making fruit cocktail tonight.")
        )

        call screen sh_diary(
            _("\n\nFinally, we met up with Akira in a cafe located in the marketplace. It was nice catching up with her. Also, we (secretly) had a glass of wine there. Akira treated us to one after she heard that Lilly had been sentenced to a soda diet for the remainder of her stay. We made sure not to have more than one though, lest we'd be found out.\n\nMusings:\nIt sure was nice to meet up with Akira again, although I'm a bit surprised that it's been nearly a week since we last saw her. She and Lilly still have almost daily contact over the phone, but you'd say that this would be an ideal opportunity for them to spend lots of time together while they still can. Who knows how long it'll take before they can meet in person again after we return to Japan."),
            _("\n\nAkira says she's busy with work, and I'm sure that's true, but I also have the impression that she'd rather not visit the Satou residence or even be in the presence of her parents. I heard that she's living in a small apartment she's renting on the other side of Inverness. I feel bad that Hisao and I are staying in such luxury right now while Akira is living in such modest conditions, even though I'm pretty sure it's completely by her own choice. From what I've been able to tell, Akira doesn't like her parents and is still upset with them about the way they left her and Lilly in Japan to fend for themselves. She doesn't act openly hostile towards them most of the time, but she's definitely keeping them at arm's length. While she's been willing to let us drink alcohol before, I got the impression the main reason she treated us to a glass of wine was to spite her father.")
        )

        call screen sh_diary(
            _("\n\nI don't think Lilly's happy with this, but she seems hesitant to try and force things. Well, that's Lilly for you. Still, it's a pity she can't spend time with both her parents and her sister at the same time. They're all really nice people on their own."),
            _("Day 9\n\nWe went to visit the famed Loch Ness today. It's not the lake in Scotland that covers the largest area, but it's definitely the lake that contains the largest amount of water (it's much deeper than any other lake around here) so you could still argue that it's the largest lake in the country. The road to our destination ran parallel to the lake for nearly 10 kilometers, so we got plenty of opportunity to take pictures. Now about that destination...\n\nThe name of our destination is Grmblwarwmx. Actually the village's real name is Drumnadrochit, but as far as pronunciation goes that's the same thing in my mind. Infuriatingly enough, Lilly managed to get it right after a few tries. Karla promised Hisao and me that we'd be flying business class back to Japan if we could learn to say the name out loud three times without mispronouncing it before the end of our stay.")
        )

        call screen sh_diary(
            _("\n\nLilly promised to make us lunch for the rest of the school year if we could pull it off. That told us all we needed to know about our chances. We still tried for several kilometers though. Yes, the atmosphere in the car got quite silly.\n\nWe first made a stop by the Loch Ness Exhibition Center. It was a very impressive display showing some insight into the legend of the dinosaur-like creature that was reputedly living in the lake and also contained an overview of the various scientific expeditions that made attempts to verify Nessie's existence. Ultimately none of them ever found evidence, but like the ghosts that are said to inhabit the various castles in the region, it adds a nice touch of mystery to the place. After the exhibition center we took a nice hour-long boat trip on the lake. Afterwards, we drove to one of the sights we saw during the boat ride: the ruins of Urquhart Castle."),
            _("\n\nIt's a very impressive castle ruin that overlooks the lake. The view from up there was magnificent, especially from the top of its remaining tower. Lilly’s mother said this place held some very special memories for her, but wouldn’t elaborate further on it.\n\nMusings:\nToday was another day we spent with Lilly's mother coming along. Watching her is kind of interesting. Physically she resembles Lilly quite a bit, but if I had to pick one daughter to compare her to, I'd still say she's more like Akira. (just a little bit more refined) I had always pictured Lilly's mother as an extremely refined noblewoman of some sort, but Karla is surprisingly down-to-earth and laid-back. She's also rather informal, and her casual attitude makes her pretty easy to talk to. It's actually kind of funny in a way, seeing a person with such a resemblence to Lilly talk like Akira often does.")
        )

        call screen sh_diary(
            _("\n\nBut when I look at Lilly and her mother together, I still notice a difference. Even though Karla acts a lot like Akira, Lilly and Karla don't act like Lilly and Akira. Whenever she's with her sister, Lilly talks to her as if she’s talking to a good friend. The two are spontanous with each other and even like to tease each other whenever the opportunity presents itself, despite Akira being much older. Karla likes to tease Lilly on occasion as well, but Lilly seems unusually reserved when speaking to her mother directly. More reserved than she is around most people. I suppose it's somewhat understandable, seeing that they've been apart for such a long time, but it's still a bit odd."),
            _("Day 10\n\nI got out of bed early this morning in order to take pictures of the Satou residence. It's been on my to-do list for days, and I finally decided to stop putting it off. Lilly, Hisao and I had a trip planned this day, so staying in bed all morning wasn't an option to begin with. While visiting the study I spent some time in the presence of Lilly's father. We've barely seen him at all during our stay here. He leaves early and comes back late most of the time, and when he comes home, he often retreats to his study or goes straight to bed. I hadn't really spent any time in the study before, so I was unaware of this before but... The bookcase covering nearly the entire right wall is nearly completely filled with Japanese fiction!!! I think saying that Lilly's father is an avid reader is a massive understatement. He gave me permission to borrow any book I liked in case I got bored here.")
        )

        call screen sh_diary(
            _("\n\nI wonder if it'd be selfish of me to secretly wish for a world-wide airline strike, just so I could stay here long enough to take him up on that offer. Before I left, he told me to get some binoculars. I wondered why at the time. It didn't take that long to find out.\n\nLilly, Hisao and I took a bus to the village of Avoch on the other side of the bay. Just like her father, Lilly wouldn't really go into detail. Avoch turned out to be a rather small harbor village and Lilly had arranged a boat trip from there. I didn't get why we'd be taking another boat trip after having taken one on Loch Ness the day before already, but the reason quickly became clear. Three words: Seals and dolphins! It turns out they live in the very bay on whose edge I've been sitting each evening. The binoculars I borrowed came in handy when the captain of our boat took us close to a seal colony near the peninsula we were heading for."),
            _("\n\nSeeing them lying on the beach and occasionally clumsily flopping around, especially the little ones, just made my heart melt. So adorable! We didn't end up needing binoculars for the dolphins. At some point several of them started swimming around and under the boat, occasionally jumping above the water surface. We made a few marvelous pictures including one with me in it. The trip itself only took an hour, and I would have liked to take another, but unfortunately there was a rather large group waiting on the shore when we came back, and we didn't want to wait another hour for another go-around, so we took the bus to North Kessock, where a dolphin and seal center is located, instead.\n\nWe spent some more time at the center watching dolphins from both the vantage point and through the underwater cameras the center set up nearby.")
        )

        call screen sh_diary(
            _("\n\nThey also had underwater microphones installed so we could listen to the sounds they made while they were swimming nearby. One of the coworkers there seemed really eager to tell us about these animals—as if my interest hadn't been piqued enough as it was. When Lilly pried a bit, we learned he was so focussed on us because he already had us pegged for Japanese, and the center was run by the Whales and Dolphin Conservation charity organisation. He mentioned that Japan is one of the countries still engaged in the practice of whaling and Japanese fishermen kill thousands of dolphins and small whales every year, and he urged us to spread the word once we return home. That was kind of uncomfortable. I got the impression that that person thought we ate nothing but whale meat all day long, but I've never even tasted it and Lilly mentioned that the few times she had a taste, it didn't strike her as that good."),
            _("\n\nAnyway, Lilly and I made the decision then and there to officially adopt one of the dolphins as a gesture of goodwill. (this was something they offered to visitors) Lilly will be paying the monthly fee to the center, and I will be paying back my share by treating Lilly to a free lunch each month. The person at the center was really impressed by our decision. So please welcome the latest member to our little family; Moonlight the bottlenose dolphin. We got a cotton bag, certificate with her name, a sticker, information guide and they gave us a really cute picture of our dolphin as a bonus. Lilly and her mother will be visiting a theater play this evening, so we decided to return to the Satou home without making any more detours.")
        )

        call screen sh_diary(
            _("\n\nMusings:\nWhen Lilly's father spoke to me this morning, he suggested taking a traditional bath if I had the time. It's natural for a host to go out of his way to accommodate his guest, but I wonder if that was all there was to it. I remember accompanying my mother to a public bath a few times in the past. I enjoyed it back then. I don't think I could stand entering a public bath these days anymore, no matter how much confidence I'd gain. In fact, I'm willing to bet I'd be denied entry because the owners would feel the sight of me would upset the other visitors too much. Did Lilly's father mean to imply that this would be an opportunity? The bathroom's large enough to accommodate six to eight people at once. It's kind of a public bath without the public. Should I give it a try for old times sake?")
        )

        "Not having anything else in mind to write down, I peer through the binoculars again to see if I can detect any movement in the water."
        "A silly thought creeps into my mind and before I can reconsider the idea I whistle sharply on my fingers, cup my hands in front of my mouth and call out."
        ha "Moonlight!"
        "I grin. There won't be any response, of course, but I just felt like trying it."
        mystery "Hanako!"
        ha "EEK!"
        "I let out a high-pitched cry, spring to my feet and turn around."

        show hisao cross_grin_polo
        with charaenter

        "Standing behind me is Hisao, sporting a broad grin that would make the head nurse jealous. I quickly avert my eyes while trying to keep my rapidly emerging blush in check."
        "It looks like he decided to look me up, heard me on his way over here, and decided to sneak up on me. Hisao takes a moment to enjoy his own joke and then gives me a quick peck on the cheek to reassure me."

        show hisao basic_smile_polo
        with chchange

        hi "So, did you spot any more dolphins?"
        "I quietly shake my head, still a bit embarrassed."
        ha "I... d-don't think they c-come to this part of the b-bay often."
        "Hisao allows his eyes to skim the water himself and then turns back to me."
        hi "Maybe your dolphin’s busy doing typical dolphin-stuff right now. Like… you know… playing volleyball with live sea turtles."
        "I giggle at his words."
        ha "Still jealous?"
        "While Lilly and I were talking about how cute dolphins were earlier today, Hisao had to inject a pseudo-biology lesson into the conversation, and he said that dolphins are prone to what he called “sociopathic tendencies” at times."
        "Lilly was quick to playfully insinuate that Hisao was merely being jealous of the dolphins getting too much of our affection, which he immediately denied. For some time I joined up with Lilly playfully ruffling Hisao’s feathers a bit."
        "Hopefully he didn’t take that seriously."

        show hisao basic_grin_polo
        with chchange

        hi "If your dolphin isn't around, then maybe my company will do for the evening?"
        "I smile softly and nod."
        ha "I'm still d-dating you and not Moonlight."
        "As I look Hisao over, I suddenly realize something. His hair is still dry and I can still spot several sweat drops on his face."
        ha "You d-didn't take a shower yet?"
        "He shakes his head."

        show hisao basic_speak_polo
        with chchange

        hi "I was going to, but then I realized that since I have no plans for the evening and Lilly and her parents are away, I might as well go with something more extensive than a quick shower."
        "I smile."
        ha "You want to try out the bathroom?"

        show hisao basic_grin_polo
        with chchange

        hi "Yeah. I mean, it's pretty large, and we have nothing but showers in the dorms at school. I don't think I should pass up an opportunity to have what's pretty much my own private bath house."
        ha "I hope you have fun soaking."

        show hisao basic_smile_polo
        with chchange

        hi "Well..."
        "From the hesitant look on his face, I can tell there's more he wants to say, but he isn't quite sure how to say it."
        "I suddenly I get what he wants to ask."
        "He didn't come here to tell me he was going to use the bath. He came here to invite me along."
        "As I realize this, my fading blush quickly returns with a vengeance."
        hi "How about it? I don't think you take these kinds of baths very often. Why not take advantage of the opportunity?"
        "Seeing that I wrote down the very same thing less than half an hour ago, it's difficult for me to argue against that."
        ha "I... don't really handle hot b-baths very well."

        show hisao cross_smile_polo
        with chchange

        hi "I checked out the bath before coming here and there's a control panel for the heater that allows you to set the water temperature to whatever you like."
        hi "You don't have to if you don't want to, but I'd really like you to join me. Let's make it a very special occasion."
        ha "...O-okay then."

        stop music fadeout 3.0
        stop ambient fadeout 3.0

        scene black
        with endchapter

        if _in_replay:
            return

    return