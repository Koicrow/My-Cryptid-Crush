# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.
    
label day_2:
    
    $ save_name = "Day 2"
    
    scene bg dorm
    with fade
    
    b "Oh my god, [name], are you seeing this?"
    
    "Bea angles her phone screen toward me. I lean across her bed in order to read it."
    
    b "They're offering a $5000 dollar bounty for anyone that uncovers additional evidence of cryptids before the Fishtrap Cryptid Festival!"
    
    p "Wow, that's a lot."
    
    b "No kidding."
    
    "I turn my attention back to my phone, trying to look nonchalant. Bea gives me a suspicious look, which I pretend I didn't see."
    
    b "That's all you have to say? \"That's a lot\"? No crazy cryptid hunting schemes or evidence-gathering missions?"
    
    p "Well, it {i}is{/i} a lot."
    
    if words:
        
        "My phone buzzes, telling me that Greg took his turn on Letters with Pals. Apparently just he played a Y on my SNORT to make SNORTY. There is {i}no{/i} way that's a real word."
        
        p "Ugh, fuck this game. I have, like, six consonants and a U. What am I supposed to make with that?"
        
        b "Honey, are you okay? You've been acting weird ever since that night we went to the cemetery."
        
        p "What do you mean? I'm fine."
        
        "I play RUB, which is barely not enough to take the lead."
        
        jump day2_words3
        
    b "Honey, are you okay? You've been acting weird ever since that night we went to the cemetery."
    
    p "What do you mean? I'm fine."
    
label day2_words3:
    
    b "I don't know, usually when the cryptid festival is coming up, you won't stop talking about Igopogo sightings or cryptid film screenings or whatever. Now you're all quiet."
    
    "I idly open my Tweeter feed and stare it at, trying really hard not to think about the actual cryptid I hung out with yesterday. I've known Bea since high school, and she has an uncanny way of reading my mind. Whatever I tell her, I'd better make it convincing."
    
menu:

    "Guess I'm just growing out of it.":
        jump day2_quiet1

    "Work has been really tiring lately.":
        jump day2_quiet2
   
    "I met an actual cryptid at the cemetery.":
        jump day2_quiet3

label day2_quiet1:
    
    p "I guess I'm just, you know, growing out of it or something."
    
    b "You? Growing out of {i}cryptids{/i}?"
    
    b "Pfft. Don't tell me you're going to grow out of eating next, or breathing oxygen."
    
    "I give Bea a good-natured shove."
    
    p "Oh, shut up."
    
    jump day2_quiet4

label day2_quiet2:
    
    p "It's just that work has been really tiring lately. Don't really have the energy for cryptid hunting."
    
    b "Aw, I'm sorry. Is there anything I can do to help?"
    
    p "Nah, I'm alright. Thanks, though."
    
    jump day2_quiet4

label day2_quiet3:
    
    p "The truth is... That night in the cemetery, I met an actual cryptid. Since then, all the speculative stuff lost its magic."
    
    b "Ha, good one. Are you writing a novel?"
    
    "I give Bea a good-natured shove."
    
    p "Oh, shut up."
    
    jump day2_quiet4

label day2_quiet4:
    
    p "Besides, I thought you didn't even {i}believe{/i} in cryptids, so—"
    
    b "I don't."
    
    p "—why are you so interested in the festival {i}now{/i}?"
    
    b "Well..."
    
    "Bea looks down at her phone for a few seconds, stalling."
    
    b "Don't get me wrong, I still think cryptids are all hoaxes and wishful thinking. But you must be finally rubbing off on me, because I'm starting to think..."
    
    b "I mean, look at this. They're finding all sorts of weird footprints in the forest by the cemetery. And there's this weird tuft of fur!"
    
    "Bea shows me her screen again. I rub my chin, trying to look curious rather than anxious. Could that belong to one of the Fishtrap crytids? Mothman? Frankie? Do phantom kangaroos even shed fur??"
    
    p "Could be from a deer, maybe?"
    
    b "Ugh, see what I mean? You're all boring now."
    
    "Bea gives me a thoughtful look, like I'm one of her spreadsheets that she could crunch the numbers on if she focused hard enough."
    
menu:

    "(Defuse the tension with humor)":
        jump day2_tension1

    "(Make an excuse to leave)":
        jump day2_tension2
   
label day2_tension1:
    
    p "Well excuuuse me, Your Majesty. What will you do without your faithful jester?"
    
    "Taking my cue, Bea raises her hand to her forehead dramatically. She never did get over her high school theater career."
    
    b "Oh, my loyal subject. How I miss your song and dance. Whatever has befallen you?"
    
    p "The truth is, I was a traitor all along. Long live the queen!"
    
    "I toss a pillow at her, making her yelp. She tosses it back with a laugh. Success: tension defused!"
    
    "The conversation turns to some Korean drama she's watching, which I usually couldn't care less about, but at least it takes the attention off of me. The topic of cryptids doesn't come up again."
    
    "Eventually, Bea has to go to some sort of presentation about data science, or information science, or something. I always tune out whenever she tries to explain the details. She accompanies me out of her dorm, and I give her a jaunty wave before cycling away."
    
    jump day2_tension3
   
label day2_tension2:
    
    p "Oh, shit, is it five already? I seriously gotta run."
    
    b "Really? What are you doing at five on a Friday?"
    
    p "Promised Dad I'd have dinner with him. You know."
    
    b "Oh, I see. Let me walk you out."
    
    "Bea lets me go without further interrogation, since apparently she has plans too. She's going to some sort of presentation about data science, or information science, or something. I always tune out whenever she tries to explain the details. She accompanies me out of her dorm, and I give her a jaunty wave before cycling away."
    
    jump day2_tension3
   
label day2_tension3:
    
    scene bg campus
    with fade
    
    "I allow myself a tiny sigh of relief. Lying to Bea is more stressful than I thought it would be."
    
    yi "Finally! Freedom!"
    
    show yin shock
    with char
    
    "Yin pokes their head out of my bag, taking exaggerated deep breaths. Yang pops up behind them."
    
    show yin at slightleft
    with move
    
    show yang neutral 2 at slightright
    with char
    
    ya "It {i}was{/i} getting a little stuffy in there."
    
    p "Sorry, you two. I offered to leave you at home, you know."
    
    show yang close
    
    ya "No, no, no. Our job is to keep tabs on you, and that means we have to stick to your side."
    
    show yin annoyed
    
    yi "Yes, but at what cost?!"
    
    hide yin
    hide yang
    with char
    
    "It's a dismal, chilly day, making me glad I brought a thick jacket with me. I stop my bike on the edge of campus, thinking about where to go next. Unlike me, Bea stayed in college, so I have to travel to her dorm to hang out. Thankfully, it's pretty close to my apartment."
    
    "I look around furtively, as if the gaggle of frat boys nearby are paying me any attention. Then I pull the Cryptid Coalition paper out of my pocket, wrestling against the autumn breeze."
    
    jump message_menu2
    
label message_menu2:
    
    menu:
        
        "I pull out my phone and message..."
    
        "Greg":
            jump greg2
            
        "Mothman":
            jump wip2
            
        "Batu":
            jump wip2
            
        "Holland":
            jump wip2
            
        "Frankie":
            jump wip2
            
label wip2:
    
    "(The route for this character is still not available. Spend some more time with gargoyle boy.{w=.5} He's lonely.)"
    
    jump message_menu2
