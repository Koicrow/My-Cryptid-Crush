# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character(_('Dad'), color="#fff")

# The game starts here.
    
label day_3:
    
    $ save_name = "Day 3"
    
    stop music fadeout 1
    
    scene black
    with fade
    
    "The next day..."

    scene black
    with fade
    
    "I'm enjoying a lazy evening when the ringing of the doorbell startles me right off my bed. I hit my ankle on my dresser on the way down."
    
    p "Ow! Coming!"
    
    p "Yin, Yang, hide!"
    
    "I toss my phone aside, scramble across my one-room apartment, and grab a shirt off my chair. Yin and Yang dart under my bed. I'm still shrugging on one of the sleeves as I pull open the door."
    
    p "Dad! What's up?"
    
    d "[name], how're ya doing?"
    
    p "Good, good. Do you want to come in?"
    
    "I lead him inside, kicking an empty pizza box out of the way. Without even looking, I know what expression my dad is making at the state of my apartment."
    
    p "Eheh, sorry about the mess. If I knew you were coming I would have cleaned a little."
    
    d "Nah, I should have called ahead. Just wanted to stop by and ask if everything is okay."
    
    "I brush some trash off my desk chair so he can sit in it. Meanwhile, I perch on the bed."
    
    p "Huh? Of course. Why wouldn't everything be okay?"
    
    d "Well, I was a little concerned when you didn't show up yesterday, bud."
    
    "I stare at him. It's taking me longer than I'd like to admit to figure out what he's talking about. It must be obvious, because Dad gives me a hint."
    
    d "Let me tell you, those boxes did a number on my old bones..."
    
    p "OHHH"
    
    p "Oh my gosh, I completely forgot! Did you get moved out okay?"
    
    d "Oh yeah, oh yeah. Zach from next door offered to help out. He's a sweetheart."
    
    p "Great. I'm really sorry I forgot."
    
    d "It's alright! I'm just glad to hear you're okay."
    
    d "You must have been up to something fun yesterday, to forget all about your old man."
    
    p "Well, uh..."
    
    "I rub my neck. In fact, I was hanging out with a cryptid yesterday. But I can't tell him that!"
    
menu:

    "I was cryptid hunting.":
        jump day3_alibi1

    "I was hanging out with Bea.":
        jump day3_alibi2
   
    "(Just keep stalling)":
        jump day3_alibi3
   
label day3_alibi1:
    
    p "I was, you know, cryptid hunting."
    
    "From the look on his face, I know that was the wrong response. But {i}maybe{/i} I can still spin this in my favor."
    
    jump day3_alibi4
    
label day3_alibi2:
    
    p "I was just hanging out with Bea."
    
    d "Oh, how's she doing? Still studying, what was it, math?"
    
    p "Econ and math, yeah."
    
    d "Good for her. Good work in that field. "
    
    d "I don't suppose you've considered getting back into school...?"
    
    "I shake my head, mutely."
    
    d "Too busy cryptid hunting, huh?"
    
    p "I haven't been cryptid hunting!"
    
    p "That much."
    
    p "At least, not in the past few days."
    
    "From the look on his face, I know there's a lecture brewing. But {i}maybe{/i} I can still spin this in my favor."
    
    jump day3_alibi4
    
label day3_alibi3:
    
    p "I was, uhhh,{w=.5} you know, uhhhhh,{w=.5} doing stuff and things, you know?"
    
    d "Ohhh, I get it. Finally starting to get out a little, huh?"
    
    "He pokes me with his elbow."
    
    p "Wait, what? No, no, no, that's not—"
    
    d "It's okay, it's okay. Spare me the details! I know what you youngsters get up to these days."
    
    "I clamp my mouth shut, my face feeling warm. I might as well let him think what he wants. It's as good of an excuse as any, right?"
    
    d "Don't suppose you're thinking about settling down?"
    
    p "{i}No{/i}, Dad."
    
    d "Too busy cryptid hunting, huh?"
    
    p "I haven't been cryptid hunting!"
    
    p "That much."
    
    p "At least, not in the past few days."
    
    "From the look on his face, I know there's a lecture brewing. But {i}maybe{/i} I can still spin this in my favor."
    
    jump day3_alibi4
    
label day3_alibi4:
    
    p "It's just like old times! Remember how we used to go out in the woods together and look for evidence?"
    
    d "Yes, [name]. When you were ten."
    
    p "Uhhh, right, but, but you've heard all the news about the Mothman sighting, right? And with the festival so soon? Come on. It's a {i}sign{/i}."
    
    "Dad sighs and runs his hand through what remains of his hair."
    
    d "Listen, I can't pin all the blame on you, because I know you got your interest in cryptids from me, but... don't you think there's a better use of your time?"
    
    "I know what angle he's going for, but I play dumb anyway."
    
    p "Not... really?"
    
    d "Maybe instead of hunting for {i}cryptids{/i}, you could be hunting for something a little more tangible, like..."
    
    menu:
        
        "He gestures expectantly with his hand."

        "A better job?":
            jump day3_hunting1

        "A giraffe?":
            jump day3_hunting2
   
label day3_hunting1:
    
    p "Fine, I know, a better job."
    
    d "Bingo!"
    
    jump day3_hunting3
   
label day3_hunting2:
    
    p "A giraffe?"
    
    d "A {i}job{/i}, [name]. A decent one."
    
    jump day3_hunting3
   
label day3_hunting3:
    
    d "I'm glad you can still find joy in cryptozoology, I really do. Hell, I've spent years of my own life looking for cryptids. But at the end of the day, you have to realize that cryptids aren't real."
    
    "It takes every inch of self control I have not to correct him, knowing what I do. Instead, I just nod."
    
    d "I think it's about time you started a proper career. Maybe found a nice person to settle down with, too. And hey, in your free time, if you want to keep looking for Mothman, then that's fine by me."
    
    p "Come on, Dad. It's 2019. I don't have to be married off by the time I'm thirty."
    
    d "Just a suggestion! Just a suggestion."
    
    d "Listen, I have to jet. I'm going bowling with some of the guys from the office. But think about what I said, alright?"
    
    p "Okay, Dad."
    
    d "And maybe go easy on the cryptid hunting."
    
    "He stands up with a noise like a sasquatch waking up from hibernation. I get up to open the door."
    
    p "Hey, we're still going to the cryptid festival together, right? I heard the author of {i}Finding the Big Squid{/i} is going to be there!"
    
    d "Ah, I don't know, bud. I'm going to be really busy with unpacking. And things are rough at work right now, got hit with a big budget cut. Maybe next year?"
    
    "For some reason, that hits me really hard, right in the throat region. I have to stop talking for a second."
    
    p "But... we {i}always{/i} go to the FCF together."
    
    d "Hey, missing one year can't hurt, right? Promise we'll go next time. Things will have settled down by then."
    
    p "Right. You're right. Sorry."
    
    d "It's alright, bud. Take it easy! I love you!"
    
    p "Love you, too."
    
    "Like that, he's gone again. I close the door."
    
    "I collapse on my bed and put my face in my hands. Ugh. Hanging out with cryptids really makes you forget about your regular, non-cryptid problems."
    
    yi "You alright, kid?"
    
    p "I'm fine. Nothing new, really."
    
    ya "Your father has a point. You don't want to work at a convenience store for the rest of your life."
    
    p "I {i}know{/i}, thanks."
    
    yi "Hey, leave the kid alone! They're distressed!"
    
    ya "They're an adult, they can handle it."
    
    p "What's with the \"kid\" business?! How old are you, anyway?"
    
    yi "Couple hundred years, why?"
    
    p "Goddamn. Okay, then."
    
    ya "Three hundred years and they still haven't lost the mentality of a child."
    
    yi "Hey, what's the point of living if you're not having fun?!"
    
    p "You know what? It's Saturday night, I have nothing to do, I'm going out. Maybe one of the others is free."
    
    "I hop off my bed and start hunting down my clothes."
    
    ya "Remember what your father said."
    
    p "He said no cryptid {i}hunting{/i}, not cryptid {i}dating{/i}."
    
    yi "Dating? Did I hear that right?!"
    
    "I throw a sock at Yin, which is about as effective as throwing a baseball at a butterfly."
    
    p "You heard what I said!"
    
    jump message_menu3
    
label message_menu3:
    
    menu:
        
        "I grab my phone and pick a cryptid to message."
    
        "Greg":
            jump greg3
            
        "Mothman":
            jump wip3
            
        "Batu":
            jump wip3
            
        "Holland":
            jump wip3
            
        "Frankie":
            jump wip3
            
label wip3:
    
    "(You already know.)"
    
    jump message_menu3
