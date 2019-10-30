# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define punk = Character(_('Punk'), color="#fff")

default clothes_done = False
default comics_done = False
default coffee = False
default comics = False

# The game starts here.

label greg2:
    
    $ save_name = "Greg 2"
    
    "Greg. Wonder what he's up to?"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Hey, what's my favorite gargoyle up to today?{/i}{/font}{/size}"
    
    "It's a few minutes before he responds."
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}I'm the only gargoyle u know{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}You don't know that{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Actually I was thinking about going to the mall and getting some hot choclate{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Wanna come?{/i}{/font}{/size}"
    
menu:

    "Sounds great":
        jump greg2_great1

    "I might be able to fit u into my schedule":
        jump greg2_great2
   
label greg2_great1:
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Sounds great, what time??{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Now?{/i}{/font}{/size}"
    
    jump greg2_great3
   
label greg2_great2:
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Hmmm I might be able to fit u into my schedule{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}I'm a busy person you know{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Can it, poop legs{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Wanna meet now?{/i}{/font}{/size}"
    
    jump greg2_great3
   
label greg2_great3:
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Yea I can do now{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Sick, I'll be there in 15{/i}{/font}{/size}"
    
    "I shove my phone back into my pocket and mount my bike, maybe a little more excited than I should be. I start cycling toward the inner city."
    
    "It's been a hot second since I've been to the mall. I wonder if that comic book store is still there?"
    
    show yang neutral
    with char
    
    ya "Someone's in a hurry."
    
    p "We're going to see Greg at the mall, it's kind of far away."
    
    show yang at slightright with char
    show yin shock at slightleft with char
    
    yi "Oh, joy! It's been so long since we've seen him!"
    
    show yang annoyed
    
    ya "Yin, you saw him a day ago."
    
    show yin neutral
    with char
    
    yi "Longest day in the world!"
    
    show yang close
    
    ya "Are you just hungry for imp treats?"
    
    show yin annoyed
    
    yi "Hmph. I don't need an ulterior motive to miss an old friend. I just want to catch up with him, like old times."
    
    show yin neutral
    
    yi "And also eat imp treats."
    
    p "Hang on tight, you two!"
    
    scene bg mallex
    with fade
    
    "One breakneck bike ride later – I'm pretty sure I broke the speed limit just by pedaling – we arrive at the shopping center. It's Friday, so the parking lot is jam-packed. Makes me glad I don't have a car, for once."
    
    "I roll my bike around a pile of browning leaves and chain it to a bike rack. I scan the skies for a second, wondering if Greg's wheeling far above. Then I realize that's silly, and dial his number instead."
    
    p "Hey, where are you?"
    
    g "By Waldo's Pizza Emporium, what about you?"
    
    p "Waldo's? Is that near, uh, Good Buy?"
    
    g "Goodbye? Why?"
    
    p "No, no, no. {i}Good Buy.{/i}"
    
    g "Oh, what about it?"
    
    p "You know what, never mind. I'll find it."
    
    g "It's the part with a greenish roof, if that helps."
    
    p "No, that doesn't help. Why would I know the color of the roofs?"
    
    g "Hmmm, I guess having wings makes me more familiar with roofs than an average human."
    
    "After a few minute of this and a half-circuit around the massive building, I catch sight of Greg leaning against a flagpole. I hang up the call and hurry toward him."
    
    show greg neutral with char

    g "Hey, there you are! Took you long enough."
    
menu:

    "Nice to see you, too.":
        jump greg2_hi1

    "Hi again, hot wings.":
        jump greg2_hi2
    
    "Let's just go inside.":
        jump greg2_hi3
        
label greg2_hi1:
    
    p "Nice to see you, too."
    g "Well, come on, then."
    
    hide greg with char

    "He spins around and saunters toward the glass entrance. With a sigh, I follow him."
    
    jump greg2_hi4
    
label greg2_hi2:
    
    p "Hi again, hot wings."
    
    show greg smirk

    "Greg snorts in disbelief. My face flushes as I realize what I just said."
    
    g "Really? Hot wings?"
    p "It, uh, sounded better in my head. Come on, let's just go inside."
    
    hide greg with char

    "I grab his wrist and pull him toward the glass entrance, though that doesn't silence his laughter."
    
    jump greg2_hi4
    
label greg2_hi3:
    
    p "Ugh. Let's just go inside."
    
    hide greg with char

    "I stomp toward the glass entrance. Greg chuckles as he follows behind."
    
    jump greg2_hi4
    
label greg2_hi4:
    
    scene bg mall
    with fade
    
    show greg neutral with char

    "Stepping through the doors is like stepping onto another planet. A rush of warm air, the noise of a thousand shoppers, and the faint smell of cinnamon rolls hit me all at once. It's as crowded as a can of sardines during rush hour."
    
    ya "Wow, it's loud in here."
    
    show yin shock at midleft with char

    yi "Yesss, chaos,{w=.5} CHAOS!"
    g "Oh, there you are! How are you two holding up?"
    
    show yang neutral 2 at midright with char

    ya "Pretty well, thank you."
    
    "I take off my thick jacket and glance over at Greg, who is doing a poor job of hiding his bat-like features under his hoodie."

    hide yin
    hide yang
    with char
    
    p "Hey, there's like a billion people here. Aren't you worried someone's going to notice you?"
    g "You've got it all backwards. Out in the countryside, I gotta be careful who sees me. Here, I can hide in plain sight."
    
    "He looks around, then waves at a chubby woman exiting Hot Tropics with more metal pieces in her face than I have in my wallet."
    
    show greg happy

    g "Hey, nice piercings!"
    
    "The woman looks over and makes the \"rock on\" hand."
    
    punk "Love the horns, dude!"
    
    show greg neutral

    "I rub my neck as she walks away."
    
    p "That seems almost too easy."
    g "Tell me about it."
    
    "The two of us start weaving our way through the crowd, no particular destination in mind. The sensations wash over me like a sea of humanity, which a really gross analogy, come to think of it."
    
menu:

    "Its..."
    
    "(Exciting)":
        jump greg2_sea1

    "(Comforting)":
        jump greg2_sea2
    
    "(Unnerving)":
        jump greg2_sea3
        
label greg2_sea1:
    
    "...Exciting."
    
    p "Man, I should come here more often. Living in a little town like Fishtrap makes you forget that this many people exist in the whole world."    
    g "Lucky. I live right in the city center, so I have to deal with stinky humans all day. That's why I like it better at night."
    
    jump greg2_sea4
    
label greg2_sea2:
    
    "...Comforting."
    
    p "It's nice to be back here. You don't get this bustle and noise in a little town like Fishtrap. Reminds me of where I grew up."
    g "Oh yeah? I live right in the city center, so I guess I'm used to it. I like it better at night, though."
    
    jump greg2_sea4
    
label greg2_sea3:
    
    "...Unnerving."
    
    p "Man, being around this many people makes me nervous. This is why I moved to a small town like Fishtrap in the first place."
    g "Eh, it's not my favorite either."
    
    show greg worried

    "He glances sideways at me. I try to look less twitchy."
    
    g "You going to be okay?"
    p "Oh, yeah, I'm fine. I don't mind it for a little bit."
    
    show greg neutral

    g "If you say so."
    g "This is why I like the city better at night, anyway."
    
    jump greg2_sea4
    
label greg2_sea4:
    
    p "Really? Isn't it scary, with all the crime and stuff?"
    
    show greg smirk

    g "Heh. Any dumbass who tries to mug {i}me{/i} is in for a nasty surprise."

    show greg annoyed

    g "By the way. Where the hell are we going?"

    jump greg2_main1
    
label greg2_main1:
    
    menu:
        
        p "How about..."
        
        "Clothes shopping." if clothes_done == False:
            $ clothes_done = True
            jump greg2_clothes1
            
        "The comic store." if comics_done == False:
            $ comics_done = True
            jump greg2_comics1
            
        "Let's head home." if comics_done or clothes_done:
            jump greg2_leave1
            
label greg2_clothes1:
    
    p "...Looking at some clothes?"
    
    show greg neutral

    g "Sure, if you want. Been thinking about getting some new socks, anyway."
    p "Socks, huh?"
    
    show greg smirk

    g "Listen, having claws will do a number on your socks. Besides, Yin and Yang like sleeping in them."

    show greg neutral
    show yang neutral at midright with char

    ya "Clean ones, mind you!"
    p "Aww. Cute."

    hide yang with char
    
    "I gasp as we pass by a little sock stand in the center of the corridor. A particular pair catches my eye."
    
menu:
    
    p "Hey, you should get these!"

    "(Black socks covered in bats)":
        jump greg2_socks1

    "(Rainbow-striped socks)":
        jump greg2_socks2
    
    "(Socks that say \"World's Best Dad\")":
        jump greg2_socks3
        
label greg2_socks1:
    
    "I grab a pair of black socks covered in little gray bats and display them to him, barely containing a grin."
    
    show greg smirk

    g "Heh. Cute."
    p "Come on, they're perfect!"
    
    show greg neutral
    show yin shock at midleft with char

    yi "Yes! Bat socks! Bat socks!!"
    
    show yang neutral 2 at midright with char

    ya "I second the bat socks."
    
    show greg annoyed

    g "I'm {i}not{/i} spending money on that thing. It's like if you walked around with little humans on your feet."
    p "Would you wear it if it was free?"

    show greg neutral
    
    g "Hmmm. Maybe. I'd have to think about it."
    
menu:

    "(Buy it for him)":
        jump greg2_socks4

    "(Just put it back)":
        jump greg2_socks5
        
label greg2_socks4:

    "I walk up to the man at the stand and hand him the socks."
    
    p "Just this, please."
    
    show greg shock

    g "Wait, [name]!"
    p "Too late!"
    
    show greg neutral

    "I hand over a limp fiver and offer the socks to Greg. There's no use trying to hide my grin now. It's taken over my face by force."
    
    p "A gift from me to you."
    
    show greg smirk

    "Greg rolls his eyes, but a little grin belies his true feelings. He snatches the socks from my hand and stuffs them into his pocket."
    
    g "Thanks, I guess."
    p "Don't mention it~"
    
    hide greg with char
    show yang at slightright
    show yin at slightleft
    with char

    "Greg continues down the corridor. Yin, Yang and I follow, giggling among ourselves."
    
    jump greg2_socks6
    
label greg2_socks5:
    
    p "Oh, well. Missed opportunity."
    
    "I put the socks back and we continue down the corridor."
    
    jump greg2_socks6
    
label greg2_socks2:
    
    "I grab a pair of rainbow-striped socks and offer them to him, grinning."
    
    show greg smirk

    g "Heh. You figured out my style already, huh?"
    p "So you like it?"
    
    show greg neutral

    g "'Course I do. But put it back. I already have a pair at home."
    
    hide greg with char

    "He continues down the corridor. I replace the gay socks, and hurry afer him."
    
    jump greg2_socks6
    
label greg2_socks3:
    
    "I grab a pair of navy socks that say \"World's Best Dad\" and show it to him, barely containing a grin."
    
    show greg annoyed

    g "Funny."
    
    show yang close at midright with char

    ya "It's true. You're a great dad."
    
    show yang neutral 2
    show yin shock at midleft with char

    yi "Raised two adorable little kids!"
    
    "My grin is starting to overtake my face. I proffer the socks harder."
    
    show greg neutral

    g "You're not my {i}kids{/i}. You're more like downtrodden cats that showed up at my door and wouldn't leave until I fed you."
    
    show yin close

    yi "Okay, {i}daddy{/i}."
    
    show greg upset

    g "Bigfoot's toe, {i}please{/i} don't start calling me that."
    
    show yin neutral
    show yang neutral

    ya "Yes, father. Whatever you say."
    
    show greg annoyed

    g "Ugh, fine. If I'm your dad, then you're grounded. All three of you."
    
    hide greg with char
    show yang at slightright
    show yin at slightleft
    with char

    "Greg stuffs his hands in his pocket and continues down the corridor. I replace the socks and follow him as Yin, Yang and I giggle among ourselves."
    
    jump greg2_socks6
    
label greg2_socks6:
    
    scene bg clothing
    with fade
    
    show greg neutral

    "Most of these stores are big and expensive, with larger-than-life pictures of models wearing something called Pumpkin Passion Lipstick. Eventually we find a second-hand clothing store – the only kind I can afford – and step inside. "
    
    "Greg glances around, looking lost. I start leading him down one of the aisles."
    
    p "Anything you're looking for, besides socks?"
    g "Not really. I spent most of my paycheck on new paint, anyway."
    p "Ooh, I see."
    p "Where do you work, anyway? Since you're a cryptid, and all?"
    
    show greg smirk

    g "Night custodian at an insurance company. No one ever sees me and the pay is decent. Good deal all around."
    p "Nice."
    
    show greg neutral

    "I wonder what {i}I'm{/i} looking for. I'm not sure if my bank account can tank a shopping spree right now, but window shopping never hurt anyone, right?"
    
menu:
    
    "(Look for ugly sweaters)":
        jump greg2_spree1

    "(Try on a flowery skirt)":
        jump greg2_spree2
    
    "(Try on a leather jacket)":
        jump greg2_spree3
        
    "(Browse the casual wear)":
        jump greg2_spree6
        
    "(Just get Greg's socks and go)":
        jump greg2_spree5
        
label greg2_spree5:
    
    p "Well, let's just get you some socks and go, then."
    g "Didn't you want to look at clothes?"
    p "Um, no, I changed my mind."
    
    show greg worried

    "Greg looks at me strangely."
    
    g "Do you want to go home or something?"
    p "No, no, no, just decided I'm not really interested in clothes. Sorry."
    
    show greg neutral
    
    g "Whatever."

    "He saunters off toward the socks. I follow behind."
    
    scene bg mall
    with fade
    
    "Soon, we step out of the relative peace of the store and back into the throng of shoppers. Greg shoulders a bag of socks."

    show greg smirk

    g "Where to next, poop-legs?"
    
    jump greg2_main1
    
label greg2_spree1:
    
    p "Ooh, ugly sweaters! The best part of cold weather!"
    
    "I rummage through a rack of sweaters and pull out one covered in sunflowers and gourds. I hold it up in front of me."
    
    p "What do you think?"
    
    show greg smirk

    g "Heh, adorable."
    
    show greg neutral
    show yang neutral at midright with char

    ya "I like it!"
    
    show yin close at midleft with char

    yi "Eh. Tacky. You can do better."
    
    hide yin
    hide yang
    with char

    "Greg pulls out one with a ghost that says \"I'm Here for the Boos.\""
    
    show greg happy

    g "How about this?"
    p "Cute. Also accurate."
    
    show greg neutral

    "I rummage through the rack some more, looking for the ugliest sweater they have. I'm interrupted by a chuckle from Greg."
    
    show greg smirk

    g "Oh, you're going to love this one."

    "He shows me a sweater with a sasquatch that says \"Don't Sass the Squatch.\""
    
    p "Oh my GOD"
    p "I NEED IT"
    
    "I'm not proud of what happened next. Long story short, I'm now short on rent for November."
    
    scene bg mall
    with fade
    
    show greg neutral with char

    "Eventually, I step back into the crowded hallways, a bloated shopping bag dangling from my hand."
    
    show greg smirk

    g "Where to next, poop-legs?"
    
    jump greg2_main1
    
label greg2_spree2:
    
    p "Hey, this is cute as heck! I'm going to try this on."
    g "Go ahead. I'll just be looking around."
    
    hide greg with char

    "I grab the skirt that caught my attention, and a couple of blouses as an afterthought. I spend a few minutes in the changing room considering myself in the mirror."
    
    jump greg2_spree4
    
label greg2_spree3:
    
    p "Hey, this is cute as heck! I'm going to try this on."
    
    g "Go ahead. I'll just be looking around."
    
    hide greg with char
    
    "I grab the jacket that caught my attention, and a couple of shirts as an afterthought. I spend a few minutes in the changing room considering myself in the mirror."
    
    jump greg2_spree4
    
label greg2_spree4:
    
    "I feel a little more self-conscious than usual. But it's not like Greg really cares, right? I mean, {i}he{/i} showed up in a hoodie and sweatpants. The bar is not exactly high, here."
    
    "I peek through the door in the new outfit."
    
    show greg neutral with char

    p "Hey, Greg! What do you think?"
    
    "Greg looks up from his phone."
    
    g "Looks good."
    p "Really?"
    
    show greg annoyed

    g "I mean, yeah. It looks fine."
    
    "My disappointment must be obvious, because he jumps to correct himself."
    
    show greg shock

    g "I mean, you look great! You always look good. I mean..."
    
    show greg upset

    "He covers his face with his hands, while I smirk."
    
    p "I always look good?"
    
    show greg annoyed

    g "Listen, you put me on the spot! It's a nice outfit, okay? Very fashion...y. Fashionable. You know what I mean."
    p "Eh, I wasn't loving it anyway. Let's just get your socks."
    
    scene bg mall
    with fade
    
    show greg neutral with char

    "I duck into the room and change into my regular clothes. Soon, we step out of the relative peace of the store and back into the throng of shoppers. Greg shoulders a bag of socks."
    
    show greg smirk

    g "Where to next, poop-legs?"
    
    jump greg2_main1
    
label greg2_spree6:
    
    "I rummage through some jeans and T-shirts, not looking for anything fancy. Dressing up isn't my thing, anyway. Bea was always the more fashionable out of us."
    
    g "Hey, [name]. What do you think of this?"
    
    "I look up as he loops a red and yellow scarf around his neck. If I have to be honest, it doesn't really suit him. But I don't want to hurt his feelings either."
    
menu:
    
    "(Be honest)":
        jump greg2_spree7

    "(Be nice)":
        jump greg2_spree8
        
label greg2_spree7:
    
    p "Doesn't really suit you, to be honest. You look like a goth Harry Totter fan."
    
    show greg smirk

    "Greg snorts and tosses the scarf back onto the shelf."
    
    g "Glad you told me."
    p "I'm looking out for ya, pal."
    
    scene bg mall
    with fade
    
    show greg neutral with char

    "Eventually, we get Greg some socks and step back out into the crowded hallways."
    
    show greg smirk

    g "Where to next, poop-legs?"
    
    jump greg2_main1
    
label greg2_spree8:
    
    p "It looks great!"
    g "Really?"
    p "Yeah, it's, um, stylish."
    
    show greg annoyed

    "Greg turn to scrutinize himself in a mirror."
    
    g "You know, if it looks bad, you can just tell me."
    p "I mean, it's not {i}bad{/i}."
    
    show greg neutral

    "Greg shrugs and tosses the scarf back onto the shelf."
    
    g "Eh, can't afford it anyway."
    
    scene bg mall
    with fade
    
    show greg neutral with char

    "Eventually, we get Greg some socks and step back out into the crowded hallways."
    
    show greg smirk

    g "Where to next, poop-legs?"
    
    jump greg2_main1
    
label greg2_comics1:
    
    $ comics = True
    
    p "...The comic book store? My dad used to take me there all the time."
    
    show greg smirk

    g "No way. You're into comics too?"
    p "Yeah, comics are my shit! Or they {i}were{/i} my shit. I guess I kind of grew out of them."
    
    show greg neutral

    "The two of us head in its general direction. I don't have to consult the map – I could probably find it in my sleep."
    
    g "That's sick. There weren't any comic book stores where I grew up, but my parents would bring them back to our hut for me to read."
    p "Your hut?"
    
    show greg annoyed

    g "Yeah, I'd call it a house, but it doesn't deserve it. Gargoyle family. We lived out in the mountains to stay hidden."
    
    menu:
        
        p "That sounds..."
    
        "Peaceful.":
            jump greg2_mountains1
            
        "Boring.":
            jump greg2_mountains2
        
label greg2_mountains1:
    
    p "...Peaceful."
    
    show greg upset

    g "Pfft. You sound like Mothman. It was boring as hell. That's why I moved to the city as soon as my folks would let me."
    
    jump greg2_mountains3
    
label greg2_mountains2:
    
    p "...Boring."
    
    show greg smirk

    g "Tell me about it! That's why I moved to the city as soon as my folks would let me."
    
    jump greg2_mountains3
    
label greg2_mountains3:
    
    show greg neutral

    g "There's only so many times you can re-read {i}Z-Men{/i}."
    p "I disagree. {i}Z-Men{/i} is a classic."
    
    show greg annoyed

    g "Listen, I was so bored I started drawing my own comics book. That's how I got into art."
    p "Oh my gosh, that's so cute! Tell me about your comics!"
    
    show greg neutral

    g "Uh, as much as I love reminiscing about {i}Gargoyle Boy: Legacy{/i}, I think I'll pass."
    
    "I let out a squawking noise I didn't know I was capable of producing."
    
    p "GARGOYLE BOY: LEGACY?!"
    
    show greg upset

    g "Yeah, yeah. Cut me some slack, I was nine."
    p "THAT IS SOOO CUTE"
    
    scene black
    with fade

    show greg neutral with char
    
    "We arrive at the comic store before long. It must have been two or three years since I've been here, but it's exactly the same. The bright yellow walls, the ceiling-high shelves, the claustrophobic amount of action posters."
    
    "Hell, the life-sized Mister U.S.A. shield still has a scratch on it from when I knocked it over at age twelve. Yes, it's {i}that{/i} old."
    
    p "Wow, this really brings me back."
    g "Cool shield."
    
    "I wander across the store, squatting down to check the lower shelves."
    
    menu:
        
        "As usual, I gravitate toward my favorite genre..."
    
        "Superhero.":
            jump greg2_genre1
            
        "Horror.":
            jump greg2_genre2
        
        "Sci-fi.":
            jump greg2_genre2
        
label greg2_genre1:
    
    "...Superhero comics. What can I say? I was raised on the classics."
    
    p "Wow, {i}Fleaman{/i} is still a thing?"
    
    show greg smirk

    g "Ah, yes. The superhero whose power is to get tiny."
    
    show yin shock at midleft with char

    yi "Hey, being tiny rocks!"
    g "Heh, if you say so. At least I don't have to worry about being eaten by a dog."
    
    show greg neutral
    hide yin with char
    jump greg2_genre4
    
label greg2_genre2:
    
    "...Horror. Zombies, ghosts, eldritch horrors, you name it. To my delight, the store has put up a display of spooky comic books for Halloween."
    
    p "Ooh, {i}Helldude{/i}. I've wanted to get into that since the movie came out."
    
    show greg smirk

    g "Let me guess. Is it about cryptids?"
    p "Hey, not all my interests are related to cryptids!"
    
    show greg neutral

    g "Uh-huh. Sure."
    
    jump greg2_genre4
    
label greg2_genre3:
    
    "...Sci-fi. Sometimes the real world is boring, you know?"
    
    p "You know, I've always meant to get into {i}Fabulous Five{/i}."
    
    show greg annoyed

    g "Never even heard of that."
    p "Eh, I don't blame you. They're kind of lame."
    
    show greg neutral

    jump greg2_genre4
    
label greg2_genre4:

    "Greg crouches down next to me and lowers his voice."
    
    g "Are you thinking about getting it?"
    p "{i}Sigh.{/i} I really shouldn't be spending money on comics. I can probably find them illegally on the Internet, anyway."
    
    show greg smirk
    
    "Greg grins toothily."
    
    g "Want to swipe it?"
    p "What, you mean..."
    
    "I glance around the store. It's empty, which is typical. The shopkeeper is off in the corner restocking mangas."
    
    p "...Steal it?"
    
    show greg neutral
    show yin neutral at midleft with char

    yi "Do it."
    
    show yang annoyed at midright with char

    ya "Don't."
    
    show yin shock

    yi "{i}Do it.{/i} You said you were going to find them illegally, anyway!"
    p "That's different!"
    
    show yin neutral
    show yang close

    ya "You shouldn't steal it {i}or{/i} pirate it. You wouldn't download a house, would you?"
    p "You know, I know you're not really an angel and a demon, but you fulfill the roles very well."
    
    show yang neutral 2

    ya "Thank you!"
    p "Anyway, I appreciate your input, but I've already decided what I'm going to do."
    
menu:
    
    "(Steal it)":
        jump greg2_steal1

    "(Don't steal it)":
        jump greg2_steal3
        
label greg2_steal1:
    
    p "Lift this motherfucker."
    
    show yin shock
    show yang annoyed

    yi "Yes, yes, yes!"
    
    g "Sick. Just follow my lead."
    
    hide yin
    hide yang
    hide greg
    with char

    "Greg hops to his feet, walks a few steps away, and picks a book off the shelves. For a moment, I'm confused. Then I notice the camera that he's conveniently standing in front of."
    
    "With the finesse of a magician, I pick the book off the shelves and slip it into my bag. Then I stand up, dusting off my pants innocently."
    
    p "Come on, let's get out of here."

    show greg smirk with char
    
    g "Agreed."
    
    "We share a knowing smirk as we head out of the store. By the time I realize the fatal flaw in our otherwise foolproof plan, it's too late."
    
    hide greg with char

    "{i}BEEP.{nw}"
    with vpunch
    extend " BEEP.{nw}"
    with vpunch
    extend " BEEP.{/i}"
    with vpunch
    
    "I freeze as the detector gate thingy goes off. I only have a split second to make a decision."
    
    menu:
        
        "Run, or stay and apologize?"
    
        "(Run)":
            jump greg2_steal2

        "(Stay)":
            jump greg2_steal2
        
label greg2_steal2:
    
    p "We should—"
    
    show greg shock with char

    "Before I can continue, Greg makes the decision for me by grabbing my wrist and pulling me into the corridor."
    
    p "Whoa!"
    g "Come on, it's crowded as hell! No one's going to be able to follow us!"
    
    scene bg mall
    with fade

    "I fall into step beside Greg, my heart pounding. It takes all my focus to not run into potted plants, so I can't check to see if we're being chased in the first place. I think I hear Yin cheering us on."
    
    "Eventually, Greg and I duck into a family bathroom and lock the door behind us. I bend over, panting. Greg lets out a crow of excitement."
    
    show greg smirk with char
    
    g "Woo! That was great!"
    
    show greg neutral
    show yin shock at midleft with char

    yi "Hard agree!"
    p "So you took the time to block the camera, but you didn't have a plan for the detector gate thingy??"
    
    hide yin with char
    show greg smirk

    g "I did have a plan. Run like hell."
    "Greg smirks at me. Instead of deigning him with a response, I sit down on the closed toilet with a huff."
    
    show greg neutral

    p "Man, this comic book better be freaking worth it."
    
    show yang close at midright with char

    ya "Tisk, tisk. You should have listened to me."
    
    show greg annoyed

    g "Oh, can it, Yang. We got away, didn't we?"
    
    hide yang with char
    show greg neutral

    "After we catch our breath, Greg and I peek out of the bathroom. There are no alarms or mall cops or anything out of place, except a couple of old people giving us judgemental stares for going into the bathroom together. Flushing at the implication, I grab my bag and hurry outside."
    
    p "Why don't we do something a little more relaxing?"
    g "Sure, sure."
    p "Still no preference?"

    show greg smirk

    g "Nah, I've had my kicks."
    
    jump greg2_main1
    
label greg2_steal3:
    
    p "I'm just going to put it back."
    
    show yin annoyed

    yi "{i}Pbbbbbt.{/i} Boring."
    
    show yang close

    ya "You're making the right decision, dear."
    p "I just wouldn't feel right stealing from this place, you know? It was my whole freaking childhood. And the shopkeeper doesn't deserve that."

    show greg annoyed
    
    g "Ah, whatever. Guess you have a point."
    
    scene bg mall
    with fade
    
    show greg neutral with char

    "We spend a few more minutes browsing the comic books, but eventually leave empty-handed."
    
    g "Where to next?"
    
    jump greg2_main1
    
label greg2_leave1:
    
    p "I'm getting kind of tired. Do you want to head home?"
    
    show greg neutral

    g "Sounds alright to me, as long as we stop by the food court. I'm starving."
    
    show yang close at midright with char

    ya "Like usual."
    
    show greg smirk

    g "Hey, it takes a lot of food to maintain a body like this!"
    "He locks his fingers together and stretches his scrawny arms in front of him. I snort in disbelief."
    p "Come on, let's go."
    
    scene bg foodcourt
    with fade
    
    show greg neutral

    "Before long, I step over a discarded, mustard-stained napkin that's a sure sign of our destination."
    
    p "Oh, man. Lots of fond memories of eating here as a kid. Hamburger Queen, always Hamburger Queen."
    g "I'm more of a Panda Central guy myself. You know, I didn't have fast food until I was sixteen."
    p "No. That's cruel and unusual."
    
    show greg smirk

    g "Tell me about it! When I moved into civilization for the first time, I had pizza and Chinese takeout every day for a year."
    
    show greg annoyed

    g "Come to think of it, that's probably why I developed heartburn."
    p "Yeah, that'll do it."
    
    hide greg with char

    "Greg wanders off to get his cheap Chinese food, while I consider my options. I ate with Bea earlier, so I'm not super hungry. Maybe I could buy both of us drinks?"
    
    p "Pssst. Yin, Yang. What does Greg like to drink?"
    
    show yang neutral 2 at slightright

    ya "Cherry soda."
    
    show yang at slightright with char
    show yin shock at slightleft with char

    yi "Iced coffee!"
    p "Is this a \"one tells the truth, the other tells only lies\" situation?"
    
    show yin close

    yi "It's just my advice, take it or leave it."
    p "Hmm..."
    
    menu:
        "After a moment of deliberation, I decide to get Greg..."
        "Cherry soda.":
            jump greg2_drink1
        "Iced coffee.":
           jump greg2_drink2
        "Hot chocolate.":
           jump greg2_drink3
        
label greg2_drink1:
    
    "...Cherry soda. Yang is the more trustworthy of the two, right? I get a root beer for myself, while I'm at it."
    
    hide yin
    hide yang
    with char

    show greg neutral with char
    
    "I find us a table for two, complete with complementary discarded straw wrappers. Romantic. Greg soon shows up holding a to-go box full of lo mein."
    
    p "Hey, Greg! Got you a cherry soda."
    
    show greg smirk

    g "Aw, you didn't have to do that. 'Preciate it."
    p "No problem."
    
    show greg neutral

    "He sets down his food and takes a long sip through the straw."
    
    g "How'd you know I like cherry soda?"
    p "Yang told me. Also, cherry soda rocks."

    show greg smirk

    g "Right?"
    
    show greg neutral

    jump greg2_drink4
    
label greg2_drink2:
    
    $ coffee = True
    
    "...Iced coffee. Why not? Everyone likes iced coffee."
    
    hide yin
    hide yang
    with char

    show greg neutral with char

    "I find us a table for two, complete with complementary discarded straw wrappers. Romantic. Greg soon shows up holding a to-go box full of lo mein."
    
    p "Hey, Greg! Got you an iced cappuccino."
    g "Oh. Thanks."
    
    "He sets down his food and tentatively sips through the straw."
    
    show greg annoyed

    g "Bleh. Sorry, I don't really do coffee."
    p "Really?!"
    
    "I shoot Yin a dirty look, which is completely lost because they're hidden in my bag."
    
    show greg neutral

    g "'Preciate it, though."
    p "It's okay."
    
    "Yin pokes their head out of the bag."
    
    show yin neutral at midleft with char

    yi "Say, if you're not going to finish that coffee, I'll have it."
    
    show yang close at midright with char

    ya "You know caffeine is bad for you, Yin."
    
    show yin shock

    yi "A little bit won't hurt! Come on, you're just going to throw it away otherwise."
    p "Is {i}that{/i} the angle you were playing?!"
    
    show yin close

    yi "What do you mean, kid? I just hate to see an iced capp go to waste."
    p "Ugh. Fine. You can have it."

    hide yin
    hide yang
    with char
    
    "I put the clear coffee cup by my bag and angle the straw into the opening. The sound of happy slurping soon emerges."
    
    jump greg2_drink4
    
label greg2_drink3:
    
    "...Hot chocolate, with plenty of marshmallows. I get one for myself, too. Forget Yin and Yang. I remember what Greg said when I texted him earlier."
    
    hide yin
    hide yang
    with char

    show greg neutral with char

    "I find us a table for two, complete with complementary discarded straw wrappers. Romantic. Greg soon shows up holding a to-go box full of lo mein."
    
    p "Hey, Greg! Got you a hot chocolate."
    
    show greg happy

    g "Oh, you remembered!"

    "He sets down his food and cups the drink with both hands."
    
    g "Thank Nessie, I've been craving hot chocolate since forever. I really appreciate it."
    p "No probs."

    show greg neutral
       
    "He takes a gentle sip from the steaming cup."
    
    g "Ahhh, hot chocolatey milk. Perfect way to end a day out."
    
    jump greg2_drink4
    
label greg2_drink4:
    
    "Greg snaps apart a pair of disposable chopsticks, then starts going to town on the lo mein. He really does eat like a carnivore."
    
    p "Wow, those noodles must be good, huh?"
    g "Mhm."
    
    "He swallows a large mouthful of lo mein."
    
    show greg smirk

    g "Not as good as the Chinese place on Goda Street. But it'll do."
    p "Oh yeah? I don't think I've been there."

    show greg neutral
    
    g "I'm telling you, it's the best. It's just a few blocks from my place. The guy there knows me by name."
    p "He doesn't know that you're a gargoyle, right?"
    
    "Greg shrugs."
    
    show greg annoyed

    g "I'm sure he's noticed that I look kinda weird. He's probably just ignoring it to be polite."
    p "Wait, are you telling me that the only thing standing between you and discovery... is people's manners??"
    
    show greg smirk

    g "Heh, you'd be surprised. I mean..."
    
    show greg neutral

    "Greg trails off as he munches on his noodles."
    
    g "You're a cryptid hunter – you should know this better than anybody. No matter how sketchy or fake the footage is, if someone expects to see a cryptid, they'll see a cryptid. And if they expect to see a human when they look at me, they'll see a human."
    
    show greg annoyed

    g "There are people all over the city who have seen my face. It's never been a problem before."
    
menu:

    "That's dangerous! You should be more careful!":
        jump greg2_noodles2
        
    "You're not worried word will get out?":
        jump greg2_noodles3
            
label greg2_noodles2:
    
    p "That's dangerous! What if one of them tells the police? Or the government?"
    
    show greg neutral

    g "Like I said, never happened before."
    p "Still, you should be more careful, Greg. There could be serious consequences, especially with so many cryptid hunters in the area."
    
    show greg upset

    g "Ugh, you're starting to sound like Batu. I'm a big boy, alright? I know how to watch out for myself."
    g "Besides, I have wings. If they {i}do{/i} find me, I'll just fly to another state."
    
    p "I'm just worried about you, is all."
    
    show greg neutral
    
    g "Whatever."
    
    jump greg2_noodles4
            
label greg2_noodles3:
    
    p "You're not worried word will get out?"
    
    show greg smirk

    g "Nah, I got wings, baby! By the time they start looking for me in Wisconsin, I'll be in Nevada."
    
    jump greg2_noodles4
            
label greg2_noodles4:
    
    show greg neutral

    "Greg slorps up the last noodle."
    
    p "Wow. That was fast."

    show greg smirk

    g "I don't hold the South Carolina hot dog-eating record for nothing!"
    p "You hold {i}what{/i} now?"
    
    "Greg winks and gets up to throw his trash away. I huff and collect the rest of my stuff as well."
    
    hide greg with char

    "I guess it's time to go. Still cupping my drink, I shrug on my jacket and find the nearest exit."
    
    scene bg mallex
    with fade
    
    "I brace myself against the wave of cold as I go through the door. Then I look up at the sky."
    
    p "Hey, would you look at that."
    
    show greg neutral with char

    "Greg catches up and stands at my side."
    
    if snow:
        
        p "Wish came true."
        g "Sure did."
        
        scene bg mallsnow
        
        "Tiny snowflakes meander through the air, in no rush to reach their destination. Then they hit the pavement and disappear, as if they're made of nothing. It's very poetic, if you're the kind of person who's into that."
        
        jump greg2_snow3
        
    p "Sun finally came out."
    g "Sure did."
    
    "Little rays of sunlight filter through the clouds, casting dappled light onto the parking lot. It's very pretty, if you're the kind of person who's into that."
    
label greg2_snow3:
    
    "I glance at Greg, who's peering thoughtfully and handsomely at the sky. I don't want to be the first to say goodbye. It would kind of ruin the moment, you know?"
    
    "Then Yin ruins the moment anyway by bursting out of my bag and doing a loop-de-loop."
    
    show yin shock at midleft with char

    yi "Wow, it's beautiful!"

    show greg annoyed

    g "Yin, get back in the bag!"
    
    hide yin with moveoutbottom

    "Yin squeaks indignantly as Greg shoves them back inside."
    
    yi "This is undignified! Am I not allowed to experience the weather??"
    
    if coffee:
        ya "{i}This{/i} is why you don't give Yin caffeine."
    else:
        ya "Not out in plain sight, no."

    show greg smirk

    g "I'm going to get going. See you next time, [name], alright?"
    
menu:
    "Will you be okay in the cold?":
        jump greg2_bye1
    "See you later... hot wings.":
        jump greg2_bye2
    "(Just say bye like a normal person, PLEASE)":
        jump greg2_bye3
            
label greg2_bye1:
    
    p "Will you be okay in the cold?"
    
    show greg neutral

    g "I'll be okay. I'm used to it."
    p "Alright, then. Until next time!"
    g "See ya."
    
    hide greg with char

    "He heads across the parking lot, his hands in his hoodie pocket. I start walking in the other direction."
    
    jump greg2_bye4
    
label greg2_bye2:
    
    p "See you later... hot wings."
    
    hide greg with char

    "I wink and turn around before Greg can protest. I hear him laugh as I walk away."
    
    jump greg2_bye4
    
label greg2_bye3:
    
    p "See you next time."
    
    hide greg with char

    "He heads across the parking lot, his hands in his hoodie pocket. I start walking in the other direction."
    
    jump greg2_bye4
    
label greg2_bye4:
    
    "Once he's out of earshot, I talk to Yin and Yang."
    
    p "That went well, right?"
    
    show yin annoyed at center with char

    yi "Uh-huh, right up to the part where I was {i}manhandled{/i}."
    
    show yin at slightleft
    show yang neutral 2 at slightright with char

    ya "Don't worry, you did fine!"
    p "What do you mean, I \"did fine?\""
    ya "I mean you made a good impression on Greg."
    p "I wasn't {i}trying{/i} to make a good impression on Greg. We're just hanging out."
    
    show yang close

    ya "Alright, dear."
    
    "I stop in the middle of the parking lot and sigh."
    
    p "Where did I put my bike, again?"
    
    jump day_3
