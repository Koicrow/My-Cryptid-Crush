# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character(_('Trucker'), color="#fff")

# The game starts here.
    
label day_1:
    
    $ save_name = "Day 1"
    
    scene black
    with fade
    
    "The next day..."
    
    scene bg convenience
    with fade
    
    p "That'll be two forty-nine, please."
    
    t "Are you kidding? It's just a bottle of water."
    
    p "Sorry, would you like me to put it back?"
    
    "I put on my best fake smile."
    
    t "Two and a half dollars for a goddamn water."
    
menu:

    "What do you want me to do about it?":
        jump day1_water1

    "(Just stay quiet)":
        jump day1_water2

label day1_water1:
    
    p "Well, what do you want {i}me{/i} to do about it?"
    
    jump day1_water3
    
label day1_water2:
    
    "My smile twitches, but I don't say anything. I feel like the Chesire Cat."
    
    jump day1_water3
    
label day1_water3:
    
    "The trucker just grunts, pays for the water, and saunters out of the convenience store. I sigh and relax against the countertop."
    
    show yang annoyed
    with char
    
    ya "Jeez, what a prick. It's not like you're in charge of the prices."
    
    show yang at slightright
    with move
    
    show yin annoyed at slightleft
    with char
    
    yi "Yang's right. You oughta go give him a piece of your mind!"
    
    p "You're joking, right? He could probably pick me up and throw me like a football. Also, I would get fired."
    
    show yin shock
    with char
    
    yi "Who cares? Throw off the shackles of the working class! Demand justice from the oppressors!"
    
    p "Get back under the counter, there are cameras in here!"
    
    hide yin
    with char
    
    show yang at center
    with move
    
    "I shove Yin back out of sight, ignoring their squawk of complaint."
    
    show yang close
    
    ya "[name]'s right, you know. We can't keep the others safe if we're discovered first."
    
    yi "Hmph. Whatever."
    
    hide yang
    with char
    
    "If not for Yin and Yang's constant bickering reminding me of their presence, my cryptid experience would feel like a dream. It's still hard to believe it really happened."
    
    "I didn't tell Bea, like Batu insisted. She wouldn't have believed me, anyway. I don't think she believed my story about following animal tracks and being attacked by a family of raccoons, either, but at least it made her stop questioning me."
    
    "I idly unpause the video I was watching on my phone."
    
    "{i}Paranormal investigator Albert Heo analyzed the 2007 footage from south Fresno soon after it was captured.{/i}{w} The video cuts to a scrawny-looking guy with a Guy Fieri goatee."
    
    "{i}\"It's not Bigfoot, it's not Almas, it's not anything we've ever seen before. But my gut tells me it's real. My best guess? Some sort of insectoid extra-terrestrial.\"{/i}"
    
    "The voice-over takes over the mantle as a blurry clip of a white figure plays.{w} {i}But not everyone is so convinced. Is the Fresno Nightwalker an alien? Or is it just a pair of pajama pants?{/i}"
    
    "I sigh and swipe down on the video, exiting it. I've already seen this footage dozens of times."
    
    "Don't get me wrong, the Fresno Nightwalker is {i}adorable{/i}. Easily in my top five most adorable cryptids. But it seems unbearably tame after what I experienced two nights ago."
    
    "I finger the folded sheet of paper in my jacket pocket. Why watch videos about possible cryptids when I can talk directly to a real one?"
    
    "I glance around the convenience store. It's empty, and I'm pretty sure my manager ditched me to visit a nail salon. Maybe now is the time to make a move."
    
    jump message_menu1
    
label message_menu1:
    
    menu:
        
        "But one question remains... Who do I message?"
    
        "Greg":
            jump greg1
            
        "Mothman":
            jump wip1
            
        "Batu":
            jump wip1
            
        "Holland":
            jump wip1
            
        "Frankie":
            jump wip1
            
label wip1:
    
    "(The route for this character is not available. Might you like to try talking to our bona fide gargoyle pal?)"
    
    jump message_menu1
