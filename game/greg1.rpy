# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default warm = False
default interests_done = False
default tai_done = False
default day_done = False
default words = False
default snow = False

# The game starts here.
    
label greg1:
    
    $ save_name = "Greg 1"
    
    "I decide to message Greg. He's kind of charming, I have to admit. Besides, he might like to know how Yin and Yang are doing."
    
    "I pull out the paper and punch in Greg's phone number."
    
    show yang neutral 2
    with char
    
    ya "Texting at work, huh?"
    
    p "Shhh."
    
    hide yang
    with char
    
    "I shoo Yang away halfheartedly, trying to figure out how to word my first message."
    
menu:

    "Hey, it's [name]. Frankie gave me ur number":
        jump greg1_message1

    "What's up gargoyle boyo":
        jump greg1_message2
   
    "(Get a little flirty)":
        jump greg1_message3

label greg1_message1:
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Hey, it's [name]. Frankie gave me ur number{/i}{/font}{/size}"
    
    "Satisfied, I return to scrolling through social media as I wait for a response. My phone doesn't vibrate until ten minutes later."
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Whats up poop legs?{/i}{/font}{/size}"
    
    show yang neutral
    with char
    
    ya "Are you texting Greg?"
    
    p "Maybe."
    
    hide yang
    with char
    
    "I shoo Yang away again, then type in my response. I frown, then erase it and type something else. That sounds casual enough, right?"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Wanted to let you know that yin and yang are doing ok{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}They argue about EVERYTHING{/i}{/font}{/size}"
    
    jump greg1_message6

label greg1_message2:
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}What's up gargoyle boyo{/i}{/font}{/size}"
    
    "Satisfied, I return to scrolling through social media as I wait for a response. My phone doesn't vibrate until ten minutes later."
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Who's this?{/i}{/font}{/size}"
    
    show yang neutral
    with char
    
    ya "Are you texting Greg?"
    
    p "Maybe."
    
    hide yang
    with char
    
    "I shoo Yang away again, then type in my response."
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}It's poop legs{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}No way, how are yin and yang?{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}They're fine, but they argue about EVERYTHING{/i}{/font}{/size}"
    
    jump greg1_message6

label greg1_message3:
    
    "I type in a message and confidently hit send."
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Heyyyy how's ur day goin gargoyle boy~ (;{/i}{/font}{/size}"
    
    "I read the message over a few times. Then I hit my head with my palm. Why did I think that was a good idea?!"
    
    "I return to scrolling through social media as I wait for a response. My phone doesn't vibrate until ten agonizing minutes later."
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Not bad, but it'd be even better with u ;*{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Also, who is this{/i}{/font}{/size}"
    
    show yang neutral
    with char
    
    ya "Are you texting Greg?"
    
    p "Maybe."
    
    hide yang
    with char
    
    "I shoo Yang away again, then type in my response."
    
    menu:

        "(Try to salvage the conversation)":
            jump greg1_message4

        "(Fuck it, just go all in)":
            jump greg1_message5
   
label greg1_message4:
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Sorry, it's [name]. Just wanted to say hi{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}No way, how are yin and yang?{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}They're fine, but they argue about EVERYTHING{/i}{/font}{/size}"
    
    jump greg1_message6

label greg1_message5:
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}It's [name]{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Was just thinking about how big and sexy ur wings are~{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Wonder how they would feel wrapped around me (;{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Wait, are u serious{/i}{/font}{/size}"
    
    "I stare at my phone for a few seconds. How did I get myself into this situation, again?"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Nah I just wanted to say hi{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Sorry if that was weird{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}It was a little{/i}{/font}{/size}"
    
    "I set down my phone and put my head in my hands, feeling an immeasurable amount of shame. A few moments later, my phone vibrates again."
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}So how are yin and yang?{/i}{/font}{/size}"
    
    "Grateful for the change of topic, I quickly thumb out a response."
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}They're fine, but they argue about EVERYTHING{/i}{/font}{/size}"
    
    jump greg1_message6

label greg1_message6:
    
    "Yin scoffs. I look up to see the two imps reading over my shoulder."
    
    show yin shock
    with char
    
    yi "No we don't! We're in agreement about lots of things."
    
    show yin at slightleft
    with move
    
    show yang neutral 2 at slightright
    with char
    
    ya "Actually, I think they're right. Arguing is kind of our thing."
    
    hide yin
    hide yang
    with char
    
    show yinyang 2
    
    yi "Oh yeah? When was the last time we argued about anything?!"
    
    show yinyang 1
    
    yi "Wait. Okay, I see your point."
    
    hide yinyang
    with char
    
    "Another message pops up from Greg."
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Lol, I know right?{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}What are you up to?{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Not much. Batu told me to stop going out during the day so I'm bored as hell{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}I'm working at kwik mart for the next eight hours, wish something interesting would happen{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}The one on madison st?{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Yeah, why?{/i}{/font}{/size}"
    
    "I wait for a long moment, but there's no reply. I didn't say something wrong, did I? Does he have a secret traumatic past involving the Madison Street Kwik Mart?"
    
    "No, he's probably just busy draining dogs of blood or whatever gargoyles do during the day. I set down my phone and lean against the wall with a sigh."
    
    "I'm almost bored enough to double text when a jangle alerts me to a new customer. It's a skinny guy in sunglasses and a black hoodie. I straighten my back slightly. People dressed like that always make me think we're about to get robbed. Maybe I just watch too many true crime videos."
    
    "He scans the store, which makes me think he's looking for the bathroom. But then he heads directly toward me and reaches into his pocket, which makes me think, HOLY SHIT,{w=.5} WE'RE GETTING ROBBED."
    
    p "Um,{w=.5} hello,{w=.5} can I help you?"
    
    "The stranger pulls out something that looks like a dog biscuit, if dog biscuits were purple. Then he speaks in a familiar voice."
    
    g "Hey, have you seen any imps around here?"
    
    p "Greg!"
    
    "Yin pokes their head over the counter and gasps."
    
    show yin shock
    with char
    
    yi "Is that for us?"
    
    hide yin
    with char
    
    g "Bon appetit."
    
    "He tosses the dog biscuit over the counter, and Yin and Yang immediately dive after it."
    
    g "Imp treats. They can't get enough of them."
    
menu:

        "It's nice to see you again!":
            jump greg1_greet1

        "What are you even doing here?":
            jump greg1_greet2
   
label greg1_greet1:
    
    p "It's nice to see you again!"
    
    g "You too. You look better."
    
    p "Yeah, probably because I haven't fallen down a hill yet today. It's on my to-do list."
    
    g "Heh."
    
    jump greg1_greet3
    
label greg1_greet2:
    
    p "What are you even doing here?"
    
    p "Goddammit, I thought you were going to rob me."
    
    g "You said you wished something interesting would happen."
    
    "He spreads his arms as if to say, \"here I am.\""
    
    p "Haha, very funny."
    
    jump greg1_greet3
    
label greg1_greet3:
    
    p "Didn't Batu tell you not to go out?"
    
    g "Eh, what he doesn't know can't hurt him."
    
    g "Besides, when I'm dressed like this, I look just like a human."
    
    p "What about your wings? And your tail? Are they, like, folded up?"
    
    g "Nah, I can make them disappear whenever. Handy, right?"
    
    p "Huh. Convenient."
    
    "Greg rummages around his pocket again and pulls out a wallet."
    
    g "By the way, since we're already here, can I get some Marlports?"
    
menu:

    "Sure thing.":
        jump greg1_marlboros1

    "You know that's bad for you.":
        jump greg1_marlboros2
   
label greg1_marlboros1:
    
    p "Sure thing."
    
    jump greg1_marlboros3
   
label greg1_marlboros2:
    
    $ warm = True
    
    p "You know that's bad for you."
    
    g "Whatever. You humans are going to kill us all with global heating anyway, right?"
    
    p "You mean global warming?"
    
    g "Yeah, that."
    
    ya "[name] is right. You should really stop."
    
    yi "You know what I always say. You're here for a good time, not a long time! Skate fast, eat—"
    
    g "Alright, that's enough from you."
    
    "He tosses another imp treat, and Yin and Yang disappear after it."
    
    g "Are you gonna give me my cancer sticks or not?"
    
    p "Sure, sure."
    
    jump greg1_marlboros3
   
label greg1_marlboros3:
    
    "I ring up a pack of cigarettes for Greg. He pays with a folded-up dollar bill and a bunch of quarters."
    
    p "Where did you get all these quarters from?"
    
    g "You'd be surprised how much people leave in the fountains."
    
    "Yang pokes their head over the countertop."
    
    ya "More treats?"
    
    g "Not right now. You two are going to get fat."
    
    yi "He's starving us! Oh, the humanity!"
    
    "Greg pockets the cigarettes and grins toothily at me."
    
    g "Wanna get out of here?"
    
    p "What, right now? I have two hours left in my shift."
    
    g "Come on, I wanna go visit the churro stand."
    
menu:

    "I can't, my manager will kill me.":
        jump greg1_get_out1

    "A quick break can't hurt.":
        jump greg1_get_out2
   
    "Skate fast, eat ass.":
        jump greg1_get_out3
            
label greg1_get_out1:
    
    p "I can't, my manager will kill me. I really can't afford to lose this job."
    
    g "Ugh, alright."
    
    p "I can hang out after my shift, though?"
    
    g "But I want churros {i}now{/i}."
    
    show yang annoyed
    with char
    
    ya "Don't be whiny, Greg."
    
    p "Just two hours."
    
    hide yang
    with char
    
    g "Fine, fine."
    
    "He stuffs his hands in his hoodie pocket and slinks away from the counter."
    
    g "Meet me at the big fountain!"
    
    p "'Kay!"
    
    "The door jangles as he exits, leaving the store in silence once again. I sigh and turn my phone back on. Time for more conspiracy theory videos."
    
    "The rest of my shift passes without incident. The most interesting thing that happens is a guy buying a bottle of orange soda and a single condom. My replacement takes my spot behind the counter – my manager never came back, come to think of it – and I head outside with Yin and Yang hidden in my bag."
    
    scene bg gas
    with fade
    
    show yin shock
    with char
    
    yi "Finally! I thought I'd never see the sun again!"
    
    hide yin
    show yang close
    with char
    
    ya "I can't believe you have to do that for eight hours every day."
    
    p "Yeah, me neither."
    
    hide yang
    with char
    
    if warm:
        
        "I shield my eyes against a surprisingly bright autumn sun. Looks like Greg is right about global warming. October is nearly over and it's still 70 degrees."
        
        jump greg1_global_warming3
    
    "I shield my eyes against a surprisingly bright autumn sun. What is the world coming to? October is nearly over and it's still 70 degrees."
    
label greg1_global_warming3:
    
    show yin shock
    with char
    
    yi "Is it churro time?!"
    
    p "Yes, my friend. It is churro time."
    
    hide yin
    with char
    
    "I retrieve my bike from behind the store and head to the city. It's not far from Fishtrap, though I do have to deal with the beeping traffic on the way in and out. I make sure to signal my turns like a good cyclist."
    
    scene bg plaza
    with fade
    
    "Soon, we arrive at what I assume Greg meant by the \"big fountain.\""
    
    p "You two see him at all?"
    
    "The imps poke their heads out from my bag."
    
    show yang neutral 2
    with char
    
    ya "Nope. Are you sure this is the right fountain?"
    
    hide yang
    show yin neutral
    with char
    
    yi "It's gotta be. See, there's the churro stand!"
    
    hide yin
    with char
    
    g "[name]!"
    
    "I turn around to see him jogging toward me, holding a grease-stained paper bag in each hand."
    
    g "I already got churros. I couldn't wait."
    
    jump greg1_churros1
    
label greg1_get_out2:
    
    p "I guess a quick break can't hurt. My manager probably won't even notice, to be honest."
    
    g "Sick! Come on, then."
    
    jump greg1_get_out4
    
label greg1_get_out3:
    
    "I return his grin with a crooked smile."
    
    p "Skate fast, eat ass, right?"
    
    show yin shock
    with char
    
    yi "Wooo! That's the spirit!!"
    
    hide yin
    with char
    
    g "{i}Sigh.{/i} I can tell these two are a bad influence on you."
    
    jump greg1_get_out4
    
label greg1_get_out4:
    
    scene bg gas
    with fade
    
    "I quickly close down the shop and follow Greg outside, with Yin and Yang hidden in my bag."
    
    if warm:
        
        "I shield my eyes against a surprisingly bright autumn sun. Looks like Greg is right about global warming. October is nearly over and it's still 70 degrees."
        
        jump greg1_global_warming5
        
    "I shield my eyes against a surprisingly bright autumn sun. What is the world coming to? October is nearly over and it's still 70 degrees."
    
    jump greg1_global_warming5
    
label greg1_global_warming5:
    
    p "So how are we getting to the city? Are we flying?"
    
    g "Sure, do you want to fly a banner behind us too, in case they miss the flying gargoyle in broad daylight?"
    
    p "Oh. Right. Whoops."
    
    p "Uhhh, I guess we could take my bike, then, if you don't mind sitting on the luggage rack."
    
    g "Hmmm. Can I pedal?"
    
menu:

    "No, it's my bike.":
        jump greg1_bike1

    "If you want.":
        jump greg1_bike2
   
label greg1_bike1:
    
    p "No, it's {i}my{/i} bike."
    
    "Greg shrugs as I retrieve my bike from behind the store."
    
    g "Worth a shot."
    
    p "Hop on, gargoyle boy."
    
    "He sits down behind me and steadies himself by putting his hands on my sides. My face goes slightly warm as I realize how close we're going to be for the duration of this trip."
    
    p "Uh, are you comfortable?"
    
    g "Never been better, why?"
    
    yi "Let's go! I want churros!"
    
    p "Alright, hang on tight!"
    
    scene bg plaza
    with fade
    
    "It's not flying, but cycling with Greg is exhilarating in its own way. Also, not particularly safe. We manage to arrive at the main plaza without any accidents. Well, without any major accidents. Let's just say we arrived in one piece."
    
    jump greg1_bike3
    
label greg1_bike2:
    
    p "If you want, I guess."
    
    g "Alright!"
    
    "I retrieve my bike from behind the store, then Greg gets comfortable on the seat. I sit down behind and steady myself by putting my hands on his sides. My face goes slightly warm as I realize how close we're going to be for the duration of this trip."
    
    p "Uh, are you comfortable?"
    
    g "Never been better, why?"
    
    yi "Let's go! I want churros!"
    
    g "Alright, hang on tight. I've always wanted to learn how to ride a bike."
    
    p "Wait, you don't know how to ride a bike?!"
    
    g "Don't worry, I'm a quick study!"
    
    scene bg plaza
    with fade
    
    "Despite me shouting bad words for the first few minutes of the trip, we manage to arrive at the main plaza without any accidents. Well, without any major accidents. Let's just say we arrived in one piece."
    
    jump greg1_bike3
    
label greg1_bike3:
    
    yi "Look! There's the churro stand!"
    
    ya "Oh, thank Nessie. I think I'm about to barf."
    
    "We both hop off, and I start chaining the bike to a bike rack."
    
    g "You work on that, I'll be right back."
    
    p "Hm? Alright."
    
    "It's only a few moments before Greg jogs back toward us, holding a grease-stained paper bag in each hand. I'm busy texting my coworker that I might not be there when their shift starts."
    
    g "Churros, nice and warm."
    
    jump greg1_churros1
    
label greg1_churros1:
    
    "He offers one of the bags to me."
    
menu:

    "(Take it)":
        jump greg1_churros2

    "(Politely decline)":
        jump greg1_churros3
   
label greg1_churros2:
    
    p "Sweet, how much do I owe you?"
    
    g "Don't worry about it. My treat."
    
    p "Oh, thanks!"
    
    "We tacitly wander over to the fountain at the center of the plaza. I sneak one of the fried dough sticks into my bag for Yin and Yang to snack on."
    
    jump greg1_churros4
    
label greg1_churros3:
    
    p "Sorry, I'm not really hungry. Thanks, though."
    
    "Greg shrugs."
    
    g "More for me, then."
    
    "We tacitly wander over to the fountain at the center of the plaza. Greg sneaks one of the fried dough sticks into my bag for Yin and Yang to snack on."
    
    jump greg1_churros4
    
label greg1_churros4:
    
    "I give the fountain a critical look. It features a big sculpture of a chunk of cheese and a basket of cranberries, with water spouting out of the top. I think it's supposed to represent Wisconsin's primary exports, or something. It's pretty much the worst fountain in the world."
    
    "I peer down into the water. The floor is dotted with coins of varying denominations, occasional stray leaves, and a single baby's pacifier."
    
    p "Nice day, huh?"
    
    g "Eh. Wish it was colder."
    
    "I wonder if he meant anything by buying me food, or if he was just being friendly. I'm probably overthinking this. Churros aren't exactly a romantic gesture, right?"
    
    "I look over at Greg, who's shooing away a pigeon. His teeth are unusually sharp, and one of his lower incisors is made of gold. Now might be a good time to get to know him better."
    
    jump greg1_convo1
    
label greg1_convo1:
    
    menu:
        
        "(Ask about his interest)" if interests_done == False:
            $ interests_done = True
            jump greg1_interests1
            
        "(Ask about Yin and Yang)" if tai_done == False:
            $ tai_done = True
            jump greg1_taiwan1
            
        "(Ask how his day was)" if  day_done == False:
            $ day_done = True
            jump greg1_day1
            
        "Maybe I should get going.":
            jump greg1_end1
            
label greg1_interests1:
    
    p "So what are you interested in?"
    
    g "Hm?"
    
    p "Like, what do you do in your free time?"
    
    g "What is this, an interview?"
    
menu:
        
    "Yes.":
        jump greg1_interview1
            
    "It's called small talk.":
        jump greg1_interview2
            
    "Just curious.":
        jump greg1_interview3
            
label greg1_interview1:
    
    p "Yes. I hope you have your resume with you."
    
    g "I already got you churros, what more do you want?"
    
    p "Resorting to bribery already? I'm starting to reconsider your application, Mr. Gargoyle."
    
    "He chuckles a little."
    
    jump greg1_interview4
    
label greg1_interview2:
    
    p "It's called small talk, have you heard of it?"
    
    g "It's called a dumb question, if you ask me."
    
    p "It's called {i}dodging{/i} the question, if you ask me."
    
    g "Heh, fine, you got me."
    
    jump greg1_interview4
    
label greg1_interview3:
    
    p "Just curious. Sorry if that was weird."
    
    g "Nah, it's fine."
    
    jump greg1_interview4
    
label greg1_interview4:
    
    g "But yeah, I like painting walls."
    
    p "Painting walls?"
    
    g "Doing street art. Graffiti. Whatever you call it."
    
menu:
        
    "Isn't that illegal?":
        jump greg1_graffiti1
            
    "That's awesome.":
        jump greg1_graffiti2
            
label greg1_graffiti1:
    
    p "Isn't that illegal?"
    
    g "Of course it's illegal! That's half the point of it. Shoplifting is illegal, that doesn't stop anyone."
    
    p "What do you mean it doesn't stop anyone? It stops plenty of people!"
    
    g "Yeah, but... well, it doesn't stop {i}some{/i} people."
    
    p "Greg, how many stores have you shoplifted lately?"
    
    g "You know what, forget it."
    
    p "Aw, I'm just poking fun at you."
    
    g "Forget it."
    
    "He tosses another churro into his mouth. I rub my head and stare at the cheese. Touchy subject, I guess."
    
    jump greg1_convo1
    
label greg1_graffiti2:
    
    p "That's awesome."
    
    g "You think? Maybe I can show you some of my stuff around the city, sometime."
    
    p "Oh, I'd love that! What kind of stuff do you draw?"
    
    g "Eh, whatever I feel like. Tags. Monsters."
    
    g "I do regular art, too. Sometimes I go around the city and sketch buildings and shit."
    
    p "Sounds relaxing."
    
    g "Mhm."
    
    p "What else do you like to do?"
    
    "Greg taps his chin as he thinks."
    
    g "Not much, to be honest. Being a cryptid's the easy life."
    
    g "Shopping. Flying around. Hanging out with Holly. Mobile games."
    
    p "Hey, we should play Letters with Pals!"
    
    g "Pshh, could you have chosen a more boring game?"
    
    p "You just don't want to lose to a human."
    
    g "Hey, I didn't say no. What's your username?"
    
    $ words = True
    
    "We exchange our info. He is {i}so{/i} going down."
    
    jump greg1_convo1
    
label greg1_taiwan1:
    
    p "So how'd you meet Yin and Yang?"
    
    show yin neutral
    with char
    
    yi "That's easy, kid. God sent Yang to guide Greg down the path of good, but Satan sent me to turn him evil. We hold each other in check until Greg chooses a side and decides his fate!"
    
    hide yin
    show yang close
    with char
    
    ya "That's not true. We were wandering through the forest when we discovered Greg as a baby, all alone, and we raised him as our own."
    
    hide yang
    with char
    
    g "They're both lying. I found them in a box behind a Taiwanese restaurant."
    
    p "Haha, really?"
    
    show yin annoyed
    with char
    
    yi "Come ooon, that's the most boring backstory ever!"
    
    hide yin
    show yang annoyed
    with char
    
    ya "You could at least say you found us somewhere nice! Like in a hollow tree trunk at the center of a clearing."
    
    hide yang
    with char
    
    g "Shush and eat your churros."
    
    "He sticks another churro into my bag, silencing their complaints."
    
    g "They're basically just strays that I took in."
    
    p "That's very charitable of you."
    
    g "I know, I know. Just one of the great perks of being me."
    
    jump greg1_convo1
    
label greg1_day1:
    
    p "So how was your day?"
    
    g "Like I said, pretty boring, until I met you."
    
    "I won't lie, that makes me feel a little fluttery. I'm not sure if it's a compliment or not, but I'll take what I can get."
    
    g "Batu put me under house arrest during daytime. So I took the opportunity to work on some art and organize my marker collection a little."
    
    p "But then you decided to ignore him and come visit me anyway?"
    
    g "Yep! No one can chain {i}this{/i} gargoyle down."
    
    p "Heh, I see."
    
    g "Also, I was out of cigs. So I needed to go to the store anyway."
    
    p "Oh, I see. It was never about me. You just wanted your smokes, huh?"
    
    g "It wasn't {i}just{/i} for the cigs. I also wanted churros."
    
    p "Great, that makes me feel much better."
    
    jump greg1_convo1
    
label greg1_end1:
    
    "To my surprise, the sun is already going down. Maybe that perilous bike ride to the city took longer than I thought."
    
    p "Maybe I should get going. It's getting late."
    
    g "Ah, yeah, true. I told Holly I'd play ping pong with her tonight, anyway."
    
    p "Ooh, fun."
    
    "We get up and stretch. Greg dumps the rest of his churros into my bag, to the delight of Yin and Yang."
    
    "I pat my pockets to make sure I still have all my stuff. Phone, wallet, some spare change. On a whim, I toss a dime into the fountain, where it lands with the tiniest {i}plop{/i}."
    
    g "Gonna make a wish?"
    
    p "Huh? Oh. Sure, I guess."
    
    "I blink into the water, thinking about it. What do I really want right now, more than anything?"
    
    p "I wish that..."
    
menu:
        
    "We'll get snow tomorrow.":
        jump greg1_wish1
            
    "You and the other cryptids will stay safe.":
        jump greg1_wish2
            
    "The Sackers will win the Powerbowl.":
        jump greg1_wish3
            
    "I'll get to see you again.":
        jump greg1_wish4
        
label greg1_wish1:
    
    $ snow = True
    
    p "...We'll get snow tomorrow. Lots of it. "
    
    g "I can get behind that. You can make great snow angels if you have wings."
    
    p "Heh, amazing."
    
    jump greg1_wish5
    
label greg1_wish2:
    
    p "...You and the other cryptids will stay safe."
    
    g "Oh, not that nonsense again."
    
    g "Listen, I know Batu makes it sound like the end of the world, but we've been spotted once or twice before. Nothing bad ever comes out of it. A few shitty documentaries at worst."
    
    p "Okay, okay. Just concerned about you."
    
    g "Eh, whatever. Thanks, I guess."
    
    jump greg1_wish5
    
label greg1_wish3:
    
    p "...That the Sackers will win the Powerbowl this year."
    
    g "Pfft, are you kidding? They're more likely to turn into bats and fly away."
    
    p "Just watch. Now that I wished it, they'll win."
    
    g "Didn't know you watched football."
    
    p "Eh, my dad has it on sometimes."
    
    jump greg1_wish5
    
label greg1_wish4:
    
    p "...That I'll get to see you again."
    
    "I put on a crooked, hopeful grin. Greg snorts."
    
    g "Are you serious?"
    
    "I shrug. He punches me lightly on the shoulder."
    
    g "If you wanna see me again, you can just ask. You have my number, don't you?"
    
    p "Oh good. Wish came true!"
    
    g "Oh, shut up."
    
    jump greg1_wish5
    
label greg1_wish5:
    
    g "I'm gonna head out. I'll catch ya later."
    
menu:
        
    "Thanks for coming all the way to see me.":
        jump greg1_bye1
            
    "See ya later, alligator.":
        jump greg1_bye2
            
    "(Just say bye like a normal person)":
        jump greg1_bye3

label greg1_bye1:
    
    p "Thanks for coming all the way to see me, by the way. I was kind of worried I'd never see you again, after that first night."
    
    g "Hey, I had nothing better to do. But, uh, it was nice to see you too, I guess."
    
    "He smiles awkwardly. I try to stop myself from grinning like an idiot. He's even cuter when he's embarrassed."
    
    g "So, uhhh, see ya."
    
    p "See ya!"
    
    "Greg spins on his heels and wanders off into the crowd. I grab my bag and head back to my bicycle."
    
    jump greg1_bye4
    
label greg1_bye2:
    
    p "See ya later, alligator."
    
    g "In a while, crocodile."
    
    "He spins on his heels and wanders off into the crowd. I grab my bag and head back to my bicycle."
    
    jump greg1_bye4
    
label greg1_bye3:
    
    p "See ya later."
    
    g "Don't be a stranger."
    
    "He spins on his heels and wanders off into the crowd. I grab my bag and head back to my bicycle."
    
    jump greg1_bye4
    
label greg1_bye4:
    
    show yin shock
    with char
    
    yi "I think he likes you."
    
    p "Oh, shush."
    
    p "Wait.{w=.5} Really?"
    
    show yin at slightleft
    with move
    
    show yang neutral at slightright
    with char
    
    ya "Hm... Could be. He's never this nice."
    
    p "That was him being {i}nice{/i}?"
    
    show yin neutral
    with char
    
    yi "Just a little observation of mine, kid. Take it or leave it.~"
    
    p "I think you're crazy."
    
    scene bg suburban
    with fade
    
    "I unlock my bike and start the long trip back to Fishtrap. The air is starting to get a little crisper, and the setting sun throws shadows over the street. My mind drifts as the skyscrapers turn into discount Indian restaurants and then into trees."
    
    "I don't want to get ahead of myself, but I can't help but let my imagination run away. We'd be quite a pair, huh? A gargoyle and a cryptid hunter."
    
    "But I probably shouldn't read into it too much. It was just a bag of churros, after all."
    
    jump day_2
