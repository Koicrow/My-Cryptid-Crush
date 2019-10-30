# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[name]")
define g = Character(_('Greg'), color="#c2e2ff")
define yi = Character(_('Yin'), color="#5e342b")
define ya = Character(_('Yang'), color="#ffdef9")
define w = Character(_('Batu'), color="#ffb05c")
define m = Character(_('Mothman'), color="#b07054")
define h = Character(_('Holland'), color="#e00d6c")
define f = Character(_('Frankie'), color="#c59cff")
define b = Character(_('Bea'), color="#c8ffc8")
define qg = Character(_('???'), color="#c2e2ff")
define qyi = Character(_('???'), color="#5e342b")
define qya = Character(_('???'), color="#ffdef9")
define qw = Character(_('???'), color="#ffb05c")
define qm = Character(_('???'), color="#b07054")
define qh = Character(_('???'), color="#e00d6c")
define qf = Character(_('???'), color="#c59cff")

# Character transitions

define char = Dissolve(0.05)
default stay = False

# Yin and Yang placements
# Yin
transform slightleft:
    xalign 0.35
    yalign 1.0
    
#Yang
transform slightright:
    xalign 0.65
    yalign 1.0

# The game starts here.
    
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    # Input name
    
    python:
            name = renpy.input(_("What's your name?"))

            name = name.strip() or __("MC")

    # These display lines of dialogue.

    $ save_name = "Prologue"
    
    "I love cryptids."

    "My parents were cryptid hunters. I grew up on stories of Bigfoot and Nessie, Chupacabra, and the Ahool."
    
    "In my teenage years, I devoured every cryptozoology book and documentary I could get my hands on. Even that series about Bigfoot that went 9 seasons without finding so much as a butt hair."
    
    "They call it \"pseudoscience.\"{w=.5} Who am I to argue? I dropped out of college. I'm no more a scientist than that guy who sells hand-painted phone cases at the corner everyday."

    "But I {i}know{/i} cryptids are real."
    
    "Maybe not all of them.{w=.5} That photograph of Nessie from 1934 is obviously fake, for example. You'd have to be an idiot not to realize that the ripple pattern doesn't like up with—"
    
    "Sorry, sorry. I'm getting distracted."
    
    "But I've always known, deep inside, that there are creatures across the Earth that we've never seen before. Creatures that we just happened to miss. Creatures waiting to be discovered."
    
    "So how could it be a coincidence that a cryptid was spotted within my own little hometown?"
    
    scene bg cemetery
    with fade
    
    play music "batu.ogg" fadeout 1
    show eileen happy
    
    b "Are you sure we're allowed to be here?"
    
    p "Shh! Not so loud!"
    
    b "But what if someone notices us?"
    
    p "It's pitch black,{w=.5} no one's going to notice unless you keep yapping!"
    
    "I flick on my flashlight and shine it around. It really is pitch black in the cemetery. I briefly illuminate the sign that reads: FISHTRAP CEMETERY, FISHTRAP, WISCONSIN."
    
    b "Besides, even if Mothman was here, wouldn't he have left by now?"
    
    p "Yes, that's why we're looking for {i}clues{/i}, before the crowd of rabid cryptozoologists come ruining the evidence."
    
    p "Honestly, why do I even bring you along?"
    
    b "I'm wondering the same thing. I could be in bed right now, watching cooking videos."
    
    b "Oh, my poor, poor pillow...{w=.5} How I miss you..."
    
    "I ignore her and approach the iron fence at the rear of the cemetery. On the other side is a dark, forboding forest."
    
    p "This is it, this is where they took the photo. That messed-up tree looks exactly the same!"
    
    b "Don't tell me you're going in {i}there{/i}."
    
    p "I {i}have{/i} to. That's the point of the investigation.{w} Look, there's something on the ground!"
    
    "I hop the fence, poking myself on the fenceposts a little more than I intended, and land with a crunch{nw}"
    with vpunch
    extend " on a bed of fallen leaves."
    
    b "Careful, [name], there's a steep drop right behind you..."
    
    p "I know, I know, I see it."
    
    "I carefully pick up a big, brown feather with my free hand, careful not to damage it.{w}Now, I'm no forensics expert, but I can tell it came from..."
    
    menu:

        "Mothman.":
            jump intro_feather1

        "A bird.":
            jump intro_feather2

label intro_feather1:
    
    p "It's one of Mothman's feathers!"
    
    "I hold up the feather toward Bea, grinning like an idiot."
    
    p "See? Evidence!"
    
    b "Honey...{w=.5} moths don't have feathers."
    
    p "Oh."
    
    p "Right, I knew that."
    
    jump intro_feather3
    
label intro_feather2:
    
    p "It's a feather from some sort of big bird."
    
    b "Uh, okay?"
    
    b "Are we birdwatching now?"
    
    p "No, just, you know, thought it looked cool."
    
    jump intro_feather3
    
label intro_feather3:
    
    "I toss the feather back onto the ground, trying to look nonchalant."
    
    b "[name]! Did you see that?"
    
    "I snap my head up, heart pounding, but the cemetery is still."
    
    p "That's not funny, Bea."
    
    b "I swear something moved in the forest! I really think you should come back over the fence..."
    
    p "It's fine, it was probably just an owl or something."
    
    "As if to demonstrate, I walk all the way up to the steep drop and squint into the darkness."
    
    b "Be careful! What if there's a murderer in there?"
    
    p "What? Don't be ridiculous. There's no murderers in Fishtrap."
    
    b "Aren't you scared?!"
    
    p "Me?{w=.5} Pshh.{w=.5} Naw."
    
    "I have to admit, I'm bending the truth a little. Don't get me wrong, I'm not usually a fearful person. It's just very dark and quiet and maybe my hands are shaking a little from the cold,{w=.5} so what?"
    
    "Something scurries through the leaves right next to me, and I let out the tiniest yelp."
    
    b "What? What is it?"
    
    p "Nothing! Nothing! Just a mouse or something."
    
    p "You know what, it's too dark to really see any clues. Maybe we should come back when—"
    
    "My foot slips on a wet leaf, and I fall right down the slope that Bea warned me about. I let out a short-lived scream before landing in a crumpled heap at the base of the hill."
    
    scene bg forest
    with hpunch and fade
    
    "I groan as I prop myself up. My arms are covered in scrapes, and there's something slimy stuck on my left pant leg that I really hope isn't deer poop."
    
    "Then I freeze. In front of me is a shadowy figure, staring right back at me."
    
    "Distantly, I hear Bea shouting my name, but I stay silent. I don't even breathe. Is it a serial killer? A wild animal?{w=.5} Or could it be what I was looking for all along?"
    
    "I pat the ground beside me until I find the flashlight. Trembling, I lift the beam to illuminate the figure, and see..."
    
    play music "greg.ogg" fadeout 1
    show greg annoyed
    
    qg "Hey! Are you trying to blind me or something?"
    
    p "Huh?"
    
    qg "Jeez, point that thing somewhere else!"
    
    "I stare at the creature in front of me for longer than is probably polite. He looks like a normal man in his 20s, save for his gray complexion and bat-like features. It's like he walked straight out of a 19th century fantasy novel and picked up an outfit at Hot Tropics."
    
menu:

    "What are you?":
        jump intro_figure1

    "(Say sorry)":
        jump intro_figure2

    "(Just keep staring)":
        jump intro_figure3
        
label intro_figure1:
    
    p "What –{w=.5} what are you?"
    
    show greg neutral
    
    qg "You mean you don't recognize me?"
    
    jump intro_figure4
    
label intro_figure2:
    
    p "S-sorry..."
    
    "My voice comes out a little squeakier than I intended, but I think it was a valiant effort at politeness, given the circumstances."
    
    show greg annoyed
    
    qg "Ugh, I guess it doesn't matter now. You already know what I am, don't you?"
    
    jump intro_figure4
    
label intro_figure3:
    
    qg "What's wrong, imp's got your tongue?"
    
    p "It's just... I've never seen anyone like you."
    
    qg "You mean you don't recognize me?"
    
    jump intro_figure4
    
label intro_figure4:
    
    p "Um..."
    
    "The creature spreads his wings and bares his fangs."
    
    qg "Really? Nothing?"
    
    p "A vampire?"
    
    show greg annoyed
    
    qg "No, I'm not a vampire!"
    
    qg "A vampire. Oh, that's rich."
    
    qg "Humans catch a glimpse of some furry flying thing and they just {i}know{/i} it's Mothman, but they couldn't recognize a gargoyle if it bit them on the ass."
    
    p "A gargoyle!"
    
    p "Oh my god...{w=.5} You're a real cryptid!"
    
    "The stories are flashing through my head now.{w} Houston, Texas. A bat-winged monstrosity that kills dogs and drains them of their blood."
    
    "The wings, the fangs, the complexion, it all fits. But somehow, I never expected a gargoyle to look so {i}handsome{/i}."
    
    show greg neutral
    
    qg "Yep, that's me, Mr. Real Cryptid."
    
    qg "Bigfoot's toe, Batu is going to {i}kill{/i} me. I wasn't supposed to be seen anywhere near humans."
    
    qg "But how am I supposed to account for them raining down on top of my head?!"
    
    "Distantly, I hear Bea yelling."
    
    b "Hang in there, [name]! I'm coming down!"
    
    qg "Oh, no you don't. One human is bad enough."
    
    "The gargoyle looks left and right, then grabs my hand and pulls me to my feet. He smells vaguely like thrift stores and cigarettes."
    
    qg "Sorry, didn't catch your name."
    
    p "It's –{w=.5} It's [name]."
    
    qg "Charmed. I'm Greg."
    
    g "You're coming with me. Maybe Batu will know what to do with you."
    
    "He starts pulling me through the forest by the hand."
    
    hide greg
    with char
    
menu:

    "(Break free)":
        jump intro_hand1
        
    "(Go with him)":
        jump intro_hand2

label intro_hand1:
    
    "Before he can take me anywhere, I break from his grip."
    
    p "Whoa, whoa, whoa! I'm pretty sure my dad warned me about following strangers through the woods."
    
    g "Listen, poop-legs. You're talking to a bona fide gargoyle."
    
    p "Poop-legs...?"
    
    g "Are you going to come with me and meet some other cryptids face-to-face? Or are you going to run back to your friend and probably never see one of us again?"
    
    p "Well..."
    
    p "I guess when you put it like {i}that{/i}, it's a no-brainer."
    
    g "Thought so. Watch your step!"
    
    jump intro_hand3
    
label intro_hand2:
    
    "I run alongside him, stumbling as I try to keep up with his surprising speed."
    
    p "Wait, wait, wait, where are we going?"
    
    g "Trust me, you're going to love it. Not every day you get to meet multiple cryptids face-to-face. Watch your step!"
    
    jump intro_hand3
    
label intro_hand3:
    
    "Greg leaps over a rotting log, disappearing out of sight. I pull out my phone to shoot Bea a quick text message – {i}be back soon, don't worry about me{/i} – then I hop over the log as well."
    
    p "Hey! Wait up!"
    
    "A tiny voice pipes up beside my ear."
    
    show yang annoyed
    with char
    
    qya "Tsk, tsk. Typical Greg, spreading his terrible influence yet again. You should turn back while you still can."
    
    "To my astonishment, there's a tiny monster hovering over my right shoulder. Another voice speaks into my left ear."
    
    show yang at slightright
    with move
    
    show yin shock at slightright
    with char
    
    qyi "Are you kidding? Look, kid, you're having the time of your life! Forget about your stinky human friend!"
    
    hide yin
    hide yang
    with char
    
    show greg annoyed
    with char
    
    g "Ying, Yang, knock it off!"
    
    hide greg
    with char
    
menu:

    "Bea is not stinky.":
        jump intro_yin_yang1

    "Greg seems alright to me.":
        jump intro_yin_yang2

    "Whoa, little demons!":
        jump intro_yin_yang3
    
label intro_yin_yang1:
    
    p "Bea is {i}not{/i} stinky."
    
    "The two monsters are no more than a few inches tall, one white, one black. The black one – Yin, I assume – pipes up again."
    
    show yin annoyed
    with char
    
    yi "That's what you think, kid. All humans stink like a sasquatch's armpit."
    
    hide yin
    with char
    
    show yang close
    with char
    
    ya "Don't be cruel. The poor human can't help what it smells like."
    
    p "Really boosting my confidence, here."
    
    jump intro_yin_yang4
    
label intro_yin_yang2:
    
    p "Greg seems alright to me."
    
    "The two monsters are no more than a few inches tall, one white, one black. The black one – Yin, I assume – pipes up again."
    
    show yin annoyed
    with char
    
    yi "That's very diplomatic of you, kid. But I'm with Yang here. Greg's an idiot."
    
    show yin close at slightleft
    with move

    show yang neutral 2 at slightright
    with char
    
    ya "A real reprobate."
    
    show yin annoyed
    show yang close
    
    yi "A downright skunk."
    
    hide yin
    hide yang
    with char
    
    show greg annoyed
    with char
    
    g "Stop it, you two, I'm flattered."
    
    jump intro_yin_yang4
    
label intro_yin_yang3:
    
    p "Whoa, little demons!"
    
    "The two monsters are no more than a few inches tall, one white, one black. The black one – Yin, I assume – pipes up again."
    
    show yin annoyed
    with char
    
    yi "Imps, actually."
    
    show yin at slightleft
    with move
    
    show yang neutral 2 at slightright
    with char
    
    ya "We're just here to keep Greg on the right track."
    
    show yin neutral
    show yang annoyed
    
    yi "Or the wrong one!"
    
    show yang neutral 2
    
    ya "In the end, we're just looking out for his health."
    
    show yin shock
    with char
    
    yi "And my entertainment!"
    
    p "I see."
    
    jump intro_yin_yang4
    
label intro_yin_yang4:
    
    scene bg lake
    with fade
    
    "Greg comes to a stop by a dilapidated cabin overlooking a little lake. And I mean {i}dilapidated{/i}. It looks so old that the last resident could have been Abraham Lincoln."
    
    p "Wow, sick pad. Do you get cable out here?"
    
    show greg neutral
    
    g "I don't {i}live{/i} here. I'm a city boy through and through."
    
    "He picks a spiky seed pod off his jeans with an expression of disgust."
    
    g "The only thing that can convince me to trek through the forest is—"
    
    "Greg stops short, looking over my shoulder."
    
    g "Well, you're about to meet him."
    
    hide greg
    with char
    
    "I spin around and my flashlight illuminates a giant worm rearing its head through the trees."
    
    p "Holy fucking guacamole."
    
    show batu mouth
    with char
    
    "It looks like an earthworm, if earthworms were four-eyed, ten feet long, and red. The worm opens its mouth, giving me a good look at a deadly ring of sharp teeth. For a split second, I consider making a run for it."
    
    "Then it starts talking."
    
    show batu neutral
    with char
    
    play music "batu.ogg" fadeout 1
    
    qw "Greg. Do you care to explain?"
    
    show batu at right
    with move
    
    show greg neutral at left
    with char
    
    g "Heyyy, sorry I'm late. Traffic was a bitch and a half."
    
    g "By the way, can I say, your hat is looking {i}particularly{/i} rakish today?"
    
    show batu irritated
    
    qw "I meant the fact that you have a human."
    
    show greg annoyed
    
    g "Oh, yes, the human.{w=.5} Of course."
    
menu:

    "He doesn't {i}have{/i} me.":
        jump intro_met_batu1

    "I like your hat.":
        jump intro_met_batu2

label intro_met_batu1:
    
    p "Well, I wouldn't say he {i}has{/i} me, so much as he's {i}accompanying{/i} me, and I am here of my own free will."
    
    jump intro_met_batu3
    
label intro_met_batu2:
    
    p "I like your hat!"
    
    jump intro_met_batu3
    
label intro_met_batu3:
    
    "{i}(The giant worm ignores you.){/i}"
    
    show batu neutral
    
    qw "Let's convene inside. You'd better have a good explanation for this."
    
    g "Of course, of course. My explanation is going to blow you away, I promise."
    
    hide batu
    with char
    
    "The giant worm slithers into the cabin, passing right in front of me. He's even more impressive up close. Greg runs a hand through his hair, takes a deep breath, and follows him inside."
    
    yi "Ooooh, you've really kicked the imp's nest now."
    
    scene bg cottage
    with fade
    
    "I turn off my flashlight as I enter the doorway. The cabin is surprisingly nice on the inside, if a little overzealous on the floral wallpaper. It must have been one hell of a renovation project."
    
    "There's a little TV, a kitchenette, an antique chess set, and a bunch of other stuff. But you'll forgive me for glossing over the decor, because my attention was immediately drawn to the figure sitting on the couch."
    
    p "{i}GASP{/i}"
    
    p "You!"
    
    show moth startled
    with char
    
    qm "H-huh? Me?"
    
    p "Yes, you! You're Mothman!"
    
    show moth scared
    
    m "Aaah! I didn't do anything, I swear!"
    
    "He hides his face behind his wings."
    
    p "No, no, no, you don't understand! I'm your biggest fan!"
    
    "He has the head of a moth, a wingspan that's probably wider than I'm tall, and a plume of fluff around his neck that looks like the softest scarf in the world. In short, he's everything I ever expected."
    
    hide moth
    with char
    
    show greg annoyed
    with char
    
    g "Here we go again. Mothman this, Mothman that.{w=.5} Where are {i}my{/i} greatest fans?"
    
    ya "Hellooo? We're right here."
    
    show greg neutral
    
    g "I adopted you. You don't count."
    
    "You know that part of the story where the protagonist thinks, \"I must be dreaming,\" even though they're obviously not dreaming?{w=.5} Well, I'm ashamed to say, this is that part."
    
    "I subtlely pinch my arm, just to make sure it's really Mothman sitting on the couch in front of me. It's unbelievable. After so many years of research and daydreaming and terrible horror films, I finally found him."
    
    "And he's {i}cute as hell.{/i}"
    
    show greg at left
    with move
    
    show batu neutral at right
    with char
    
    qw "Ahem. I think some introductions are in order."
    
    g "Alright, alright. Everyone, I'd like you to meet [name]. [name], this is Mothman, and this is the Mongolian death worm."
    
    show batu irritated
    
    qw "That's very hurtful, you know. My name is Batu."
    
    g "Yeah, but that's what everyone knows you by."
    
    show batu neutral
    
    w "What if we called you the American death gargoyle. How would you like that?"
    
    show greg annoyed
    
    g "Excuse you.{w=.5} I'm one quarter German."
    
    hide greg
    with char
    
    show batu at center
    with move
    
    p "The Mongolian death worm! I've heard of you!"
    
    p "From the Gobi desert, right? Poisonous enough to cause instant death with a single touch?"
    
    show batu irritated
    
    w "The accounts are greatly exaggerated."
    
    p "But it really is you!"
    
    p "Ohmigosh, I have so many questions. How many of you are there? Can you all talk? Are sasquatches real too? Wait wait wait, what I really want to know about is..."
    
    hide batu
    with char
    
menu:

    "Nessie.":
        jump intro_question1

    "The chupacabra.":
        jump intro_question2

    "Mokele-mbembe.":
        jump intro_question3
    
label intro_question1:
    
    p "Nessie!"
    
    show greg neutral
    with char
    
    g "Old Nessie passed away a long time ago. But her sister Bessie is still around."
    
    p "The Lake Erie monster! I should have known!"
    
    show greg at left
    with move
    
    jump intro_question4
    
label intro_question2:
    
    p "The chupacabra!"
    
    show greg neutral
    with char
    
    g "{i}The{/i} chupacabra? There are chupacabras all over the Americas."
    
    p "Really? How come we haven't seen them?"
    
    g "Trust me, you don't want to. They're ugly little things."
    
    show greg at left
    with move
    
    jump intro_question4
    
label intro_question3:
    
    p "Mokele-mbembe!"
    
    show greg neutral
    with char
    
    g "What, that dinosaur they spotted in Africa?"
    
    show greg at left
    with move
    
    show batu neutral at right
    with char
    
    w "She's real. But she's not a dinosaur. More like a... six-legged crocodile."
    
    p "Fascinating."
    
    hide batu
    with char
    
    jump intro_question4
    
label intro_question4:
    
    show moth neutral at right
    with char
    
    m "Um, Greg?"
    
    g "Yeah, moth boy?"
    
    m "Why do you have a human with you?"
    
    hide moth
    with char
    
    show batu neutral at right
    with char
    
    w "I am exceedingly interested in the answer to this question as well."
    
    g "Eheh, well, you see."
    
    g "I was high-tailing it to the lake, so I wouldn't keep you all waiting, when I happened across this poor human who'd fallen down the hill."
    
    g "Now, I couldn't just let them walk away after seeing my face. So I invited them along instead! They get to meet more cryptids, we get to not have our faces all over the news tomorrow morning. It's a win-win!"
    
    show batu angry
    
    w "But we can't keep them here forever. What happens once they return to their human family?"
    
    g "Ah, yes. Well."
    
    g "I didn't think that far ahead."
    
    show batu irritated
    
    "Batu sighs, squeezing his four eyes shut."
    
    w "This is exactly why we needed to have this meeting. Because of Mothman's recent incident, the area is going to be crawling with cryptid hunters. We have to be on high alert."
    
    hide greg
    with char
    
    show moth mix at left
    with char
    
    m "Sorry..."
    
    show batu neutral
    
    w "Mothman, you really have to stop swooping dramatically over humans in the dead of night."
    
    show moth startled:
        xalign -0.405
    
    m "But I {i}like{/i} swooping over humans in the dead of night. Swooping over humans is my {i}thing{/i}."
    
    p "Excuse me, don't {i}I{/i} get a say on what happens to me?"
    
    w "Unfortunately, no."
    
    hide moth
    with char
    
    show greg neutral at left
    with char
    
    g "Sorry, buddy. I know you're used to being king of the world back in humantown, but this is strictly cryptid business."
    
    g "Besides, are you saying that if we let you go right now, you {i}wouldn't{/i} go blabbing to all your friends?"
    
    p "Well..."
    
    hide greg
    hide batu
    with char
    
menu:

    "I'd be tempted.":
        jump intro_blab1

    "I'd keep your secret.":
        jump intro_blab2
    
label intro_blab1:
    
    p "I guess I'd be tempted. I mean, what do you expect? This is what I've been searching for my entire life!"
    
    p "Would it be so bad if you were revealed? There's so many people who believe in you already. Don't they deserve to know?"
    
    show greg annoyed
    with char
    
    g "Listen, you humans are assholes to people just because they have a different skin color than you. How do you think your friends would feel about a giant talking worm?"
    
    hide greg
    show batu neutral
    with char
    
    w "Greg is right, for once. As long as we remain hidden, we can live our lives in peace."
    
    p "I guess that makes sense, if you put it that way..."
    
    jump intro_blab3
    
label intro_blab2:
    
    p "No, I wouldn't. I'll keep your secret."
    
    p "I'm on your side! I have a poster of Mothman hanging in my bedroom, for God's sake. I don't want any harm to come to you."
    
    show moth mix
    with char
    
    m "R-really?"
    
    p "Sorry, I guess that's kind of weird."
    
    show moth neutral
    
    m "No, um, I'm flattered!"
    
    hide moth
    with char
    
    show batu neutral
    with char
    
    w "Forgive me if I'm reluctant to entrust a stranger with our greatest secret. Staying hidden is a serious matter."
    
    jump intro_blab3
    
label intro_blab3:
    
    w "You'll just have to stay here until we figure out what to do with you."
    
    hide batu
    with char
    
    "My phone starts vibrating in my back pocket. I pull it out to check. It's Bea – I almost forgot about her in all the commotion."
    
    show greg neutral
    with char
    
    g "Better not take that call."
    
    p "Yeah, no problem."
    
    hide greg
    with char
    
    "As I decline the call, I realize that if I want to escape, this might be my best shot. If I stick around any longer, it sounds like I might end up tied to a radiator, or worse. And there's no one standing between me and the door."
    
menu:

    "(Snap a pic and run for it)":
        jump intro_run1

    "(Just go along with it)":
        jump intro_stay1
    
label intro_run1:
    
    "I open the camera, subtlely angle the phone upward, and take a picture with all three cryptids in the frame. However, because I'm an idiot, I didn't account for the annoying shutter sound that the phone makes."
    
    "For a second, there's a silence in the cabin."
    
    p "I'm-really-sorry-bye!"
    
    "I turn around and sprint out the door."
    
    scene bg lake
    with fade
    
    show batu mouth
    with char
    
    w "Get back here, human!"
    
    show batu angry
    with char
    
    w "Mothman—"
    
    hide batu
    with char
    
    show moth startled
    with char
    
    m "On it!"
    
    "I glance over my shoulder to see Mothman burst out of the cabin, his impressive wingspan blotting out the stars. Breathing hard, I duck into the treeline. "
    
    scene bg forest
    with fade
    
    "I can't remember which way I came from, so I just choose a direction and stick to it, tree trunks zooming past in the dark. Mothman won't be able to fly through the undergrowth for long, right?"
    
    "I run for what seems like hours but was probably minutes, then squat down, gasping. I put one hand against a tree trunk as the world sways around me. I haven't gotten this much exercise since the time Bea dragged me to a Zumba workshop."
    
    show yin neutral
    with char
    
    yi "Good work, kid, I think you lost him!"
    
    p "Yin? {i}gasp{/i}...{w=.5} What are you... {i}gasp{/i}...{w=.5} doing here?"
    
    show yin at slightleft
    with move
    
    show yang close at slightright
    with char
    
    ya "I'm here too, despite my better judgement."
    
    show yin shock
    
    yi "Why am I here? Are you kidding? This is the most fun I've had since the police caught Greg tagging the water tower!"
    
    show yang neutral 2
    
    ya "We're here because Greg asked us to keep an eye on you."
    
    p "Well, you can... {i}gasp{/i}...{w=.5} go back now, because I'm... {i}gasp{/i}...{w=.5} doing completely fine on my own, thank you very much."
    
    "I make a halfhearted shooing motion at them. Then I hear a low chuckle from nearby."
    
    hide yin
    hide yang
    with char
    
    qh "Well, well, well. What's a tasty morsel like you doing wandering the forest?"
    
    jump intro_holly1
    
label intro_stay1:
    
    $ stay = True
    
    "I obediently decline the call and put the phone back in my pocket. I don't know why, but getting on the bad side of something called a \"death worm\" strikes me as a bad idea."
    
    show batu neutral
    with char
    
    w "My colleagues, let's discuss our predicament somewhere a little more private. Mothman, why don't you make sure our new human friend is... comfortable?"
    
    hide batu
    with char
    
    show moth neutral
    with char
    
    m "Alright, boss, right away!"
    
    "Mothman hops up and seats me on the couch, then makes sure I'm surrounded with plenty of pillows. His wings flutter adorably as he does so."
    
    m "Would you like a glass of water? Tea? Blins and sour cream?"
    
    p "Just water would be nice, thank you."
    
    "Batu lets out a rumbling sigh."
    
    hide moth
    with char
    
    show batu irritated
    with char
    
    w "I meant to tie them up, Mothman."
    
    hide batu
    with char
    
    show moth startled
    with char
    
    m "Oh! Why didn't you just say so?"
    
    show moth neutral
    
    "Before long, I'm seated in an armchair with my ankle tied to a chair leg. Mothman makes sure I had a padded seat and plenty of mobility. It's not even the most uncomfortable I've been all day."
    
    hide moth
    with char
    
    "The three cryptids disappear into some sort of loft, and soon I hear the sound of indistinct argument."
    
    show yang close
    with char
    
    ya "What did I say, dear? You should have turned around while you had the chance."
    
    show yang at slightright
    with move
    
    show yin shock at slightleft
    with char
    
    yi "Are you kidding? This is the most fun I've had since the police caught Greg tagging the town hall!"
    
    p "What are you two doing downstairs?"
    
    show yin neutral
    
    yi "Just keeping you company, kid!"
    
    show yang neutral 2
    
    ya "Greg asked us to keep an eye on you."
    
    p "There's no need. I already decided to play along."
    
    scene black
    with fade
    
    "Suddenly, the lights in the cabin turn off, making the room almost pitch black. I hear a low chuckle nearby."
    
    qh "Well, well, well. What's a tasty morsel like you doing all tied up?"
    
    jump intro_who4
    
label intro_holly1:
    
    "The voice is like the sound of snapping branches. I freeze for a second then, jump to my feet and fumble for the flashlight that's still in my back pocket."
    
menu:

    "Who's there?":
        jump intro_who1

    "(Stay silent)":
        jump intro_who2
    
    "(Throw the flashlight)":
        jump intro_who3
        
label intro_who1:
    
    p "Who's there? I've already dealt with gargoyles and giant worms tonight! I'm not in the mood for any shenanigans!"
    
    qh "Oh, don't worry. This will be over in a second..."
    
    jump intro_who3
    
label intro_who2:    
    
    "I stay completely silent, thinking back to those documentaries about predators who can only detect moving targets. My only movement is the trembling of my arms."
    
    qh "Oh, good, have you given up already? That'll make this even easier..."
    
    jump intro_who3
    
label intro_who3:
    
    "My fight-or-flight response must have been triggered, because my first impulse is to lob the flashlight in the direction of the voice."
    
    p "Stay away!"
    
    "The flashlight thunks uselessly on the ground, some distance away."
    
    qh "Nice try, little human. But I'm over here..."
    
    jump intro_who4
    
label intro_who4:
    
    "A gaunt, winged figure steps out of the shadows, standing far taller than any human. It has two winding antlers and a perpetually sneering skull for a face."
    
    "I'm petrified. I know I sounded scared when I met Greg for the first time, but in comparison, that was like a trip to Make-A-Moose Workshop."
    
    "Right now, I'm staring at death. And it's staring back at me."
    
    qh "Pfft..."
    
    play music "jersey-devil.ogg" fadeout 1
    
    qh "Bwahahahaha!"
    
    "The creature doubles over in laughter."
    
    qh "Holy Yowie, you should have seen your face!"
    
    p "H-huh?!"
    
    if stay:
        
        jump intro_stay1_5
    
    jump intro_run1_5
    
label intro_run1_5:
    
    "To add to my confusion, another creature appears right out of thin air, like a ghost."
    
    jump intro_holly2
    
label intro_stay1_5:
    
    scene bg cottage
    with fade
    
    "To add to my confusion, another creature appears right out of thin air, like a ghost. She flips a switch on the wall, and the lights turn back on."
    
    jump intro_holly2
    
label intro_holly2:
    
    qf "Come on, Holland, you scared the poor human half to death."
    
    h "Oh my gosh, I feel bad now! I swear I'm not going to eat you. I'm actually vegetarian."
    
    p "Oh... okay... vegetarian..."
    
    "I sit down on the floor, put my head in my hands, and breathe deeply, trying to calm my racing heart."
    
    "Now that Holland is wearing a contrite epression, with her claw-like hands clasped together, she isn't half as scary. If I wasn't recovering from a near-death experience, I would almost call her endearing."
     
    qf "Hey, you. Are you alright?"
    
menu:

    "Just need a moment to recover.":
        jump intro_recover1

    "Heh, you really got me good.":
        jump intro_recover2
    
    "You can't just do that to people!":
        jump intro_recover3
            
label intro_recover1:
    
    p "Yes, I'm fine... just need a moment to recover...{w=.5} waiting for my life to stop flashing before my eyes..."
    
    h "Oh my gosh, I'm sorry!! I know I look scary, but I'm actually very nice, I promise!"
    
    h "You don't think I traumatized them, do you?"
    
    qf "At this point, I wouldn't be surprised."
    
    jump intro_recover4
    
label intro_recover2:
    
    p "Heh, I'm fine. You really got me good."
    
    h "I know, right? Finally, someone who appreciates a good prank."
    
    jump intro_recover4
    
label intro_recover3:
    
    p "You can't just do that to people! You scared me to death!"
    
    h "Aw, I'm really sorry. I was just trying to make this meeting more exciting."
    
    p "If this day gets any more exciting, I think I'm going to have a heart attack."
    
    jump intro_recover4
    
label intro_recover4:
    
    h "I don't get it. Humans think I look terrifying. I don't look {i}that{/i} bad, right, Frankie?"
    
    f "Don't sweat it, you look fine. That top really suits you."
    
    h "Aw, shucks, thanks!"
    
    "Frankie offers me a hand. I'm taken by surprise, but I accept it and pull myself off the ground. Her touch is surprisingly cold, and I catch a whiff of peppermint."
    
    "Her gaze lingers on me a little longer than normal, but I can't tell what she's thinking. She looks vaguely shimmery, like a distant road on a summer day. She's wrapped up in several sweaters and a scarf."
    
    "She's also a kangaroo. I know that sounds like some sort of obscure insult, but I'm serious. She has the head and legs of a kangaroo, and otherwise the body of a human woman."
    
    f "I'm Frankie. This prankster over here is Holland."
    
    h "Call me Holly!"
    
    p "I'm [name]. Pleased to meet you, I guess."
    
    if stay:
        
        jump intro_stay2
       
    jump intro_run2
    
label intro_run2:
    
    h "Let me make it up to you for spooking you! Can I buy you a drink?{w=.5} Do you drink? Coffee is fine, too, if you'd rather."
    
    "I might have taken her up on the offer, if I wasn't interrupted by a fluttering sound from above. I look up to see Mothman perched in a tree like an oversized bird."
    
    show moth mix
    with char
    
    m "Um, actually, Batu wants me to bring the human back to the cabin. Sorry."
    
    p "{i}Sigh.{/i} All that running for nothing."
    
    show moth at right
    with move
    
    f "Mothman, dude, it's been forever. How've you been?"
    
    show moth neutral
    
    m "Oh, you know, same old, same old."
    
    f "Is your garden doing well?"
    
    m "Oh yes, the carrots are just coming in!"
    
    f "That's awesome. I hate carrots, actually, but I'm happy for you."
    
    show moth mix
    
    m "Let's head back. I don't want to keep Batu waiting..."
    
    hide moth
    with char
    
    "I briefly consider making another run for it, but I can feel Mothman's eyes trained on me. With my luck, Holland and Frankie are probably supernaturally fast too. Oh, well. I know when I'm beat."
    
    "We walk through the forest as a group. The cryptids chatter the entire way."
    
    h "...So they call me the \"Jersey Devil,\" which is just silly, if you ask me. I go on a {i}tiny{/i} bender and maybe spook a {i}few{/i} partygoers, and suddenly HUNDREDS of people claim to have seen a devil."
    
    h "None of them got the description right, either. I mean, \"blood-curdling scream\"? That's a {i}very{/i} rude way to describe someone's laugh."
    
    f "What do you expect when you keep letting people see you?"
    
    h "Well, easy for {i}you{/i} to say. Not everyone can turn invisible at will, Ms. Phantom Kangaroo."
    
    p "Oh, oh, oh! I know about phantom kangaroos!"
    
    p "The 1978 Wisconsin sightings... That must have been you!"
    
    f "Pfft. Nope. As far as I know, that's someone's pet wallaby that escaped."
    
    p "Oh."
    
    h "But she HAS been spotted multiple times. Not to mention her big old kangaroo prints that she leaves everywhere!"
    
    f "Well excuuuse me. If I could float, I'd be doing it already."
    
    scene bg lake
    with fade
    
    "The cabin draws near, with a very exasperated Batu at the doorway."
    
    show batu irritated
    with char
    
    w "Holland, Frankie. Glad you could make it. [name], I hope you got that out of your system."
    
    p "Ah, yes, I suppose so."
    
    show batu neutral
    
    w "Come in."
    
    scene bg cottage
    with fade
    
    "This time, I put up no protest as Mothman sits me down on an armchair and ties my ankle to a chair leg. Greg has on an insufferable grin."
    
    g "Welcome back, [name]. Had a nice run?"
    
    p "Yeah, I think that about covered my exercise for the next lifetime or so."
    
    g "Bet you wish you'd known we were going to let you go anyway, huh?"
    
    jump intro_meeting
    
label intro_stay2:
    
    h "Oh, I didn't even finish introducing myself! They call me the \"Jersey Devil,\" which is just silly, if you ask me. I go on a {i}tiny{/i} bender and maybe spook a {i}few{/i} partygoers, and suddenly HUNDREDS of people claim to have seen a devil."
    
    h "None of them got the description right, either. I mean, \"blood-curdling scream\"? That's a {i}very{/i} rude way to describe someone's laugh."
    
    f "What do you expect when you keep letting people see you?"
    
    h "Well, easy for {i}you{/i} to say. Not everyone can turn invisible at will, Ms. Phantom Kangaroo."
    
    p "Oh, oh, oh! I know about phantom kangaroos!"
    
    p "The 1978 Wisconsin sightings... That must have been you!"
    
    f "Pfft. Nope. As far as I know, that's someone's pet wallaby that escaped."
    
    p "Oh."
    
    h "But she HAS been spotted multiple times. Not to mention her big old kangaroo prints that she leaves everywhere!"
    
    f "Well excuuuse me. If I could float, I'd be doing it already."
    
    h "[name], let me make it up to you for spooking you! Can I buy you a drink?{w=.5} Do you drink? Coffee is fine, too, if you'd rather."
    
    "I might have taken her up on the offer, if I wasn't interrupted by the sound of footsteps – and one worm – descending the stairs. Batu, Mothman, and Greg appear once more."
    
    show batu neutral
    with char
    
    w "I'm afraid your date will have to wait. Frankie, Holland, glad you could make it."
    
    hide batu
    with char
    
    h "Batu! Wouldn't miss it for the world!!"
    
    f "Mothman, dude, it's been forever. How've you been?"
    
    show moth neutral at right
    with char
    
    m "Oh, you know, same old, same old."
    
    f "Is your garden doing well?"
    
    m "Oh yes, the carrots are just coming in!"
    
    f "That's awesome. I hate carrots, actually, but I'm happy for you."
    
    "Greg saunters over and clasps me on the back."
    
    hide moth
    with char
    
    g "Good news, human! We decided to let you go!"
    
    jump intro_meeting
    
label intro_meeting:
    
    p "Huh? Really?!"
    
    show batu content
    with char
    
    w "Yes, we made a decision. We can't spare the resources to confine you to the cabin for an extended period of time. So instead, we're going to keep an eye on you from afar."
    
    p "How? Through cryptid magic?"
    
    show batu happy
    
    w "Yin and Yang will keep watch over you."
    
    hide batu
    with char
    
    show yin shock
    with char
    
    yi "Hell yeah! We get to stay with the human!"
    
    hide yin
    with char
    
menu:

    "Do I really have to deal with these guys all the time?":
        jump intro_deal1

    "Phew, guess I'm getting off easy.":
        jump intro_deal2
    
label intro_deal1:
    
    p "Do I really have to deal with these guys {i}all the time{/i}?"
    
    show greg neutral
    with char
    
    g "Now you know how I feel 24/7."
    
    hide greg
    with char
    
    show batu angry
    with char
    
    w "Quiet, human. The alternative was to tie you up and throw you into the lake."
    
    jump intro_deal3
    
label intro_deal2:
    
    p "Phew, guess I'm getting off easy after all."
    
    show batu neutral
    with char
    
    w "That's right. The alternative was to tie you up and throw you into the lake."
    
    jump intro_deal3
    
label intro_deal3:
    
    show batu at right
    with move
    
    show moth startled at left with char:
        
        xalign -0.405
    
    m "Oh, no! We wouldn't really do that, would we?"
    
    show batu irritated
    
    "Batu closes his eyes and takes a deep breath."
    
    w "No, Mothman, we wouldn't. But the human didn't know that."
    
    show moth mix at left
    
    m "Oh.{w=.5} Sorry."
    
    "I snicker, despite myself."
    
    hide moth
    with char
    
    show batu neutral at center
    with move
    
    w "Anway, now that we're all here, let's begin our meeting properly. And thirty minutes late, too. Chop chop, cryptids."
    
    hide batu
    with char
    
    "The five cryptids move over to the kitchen and sit around a circular table. Mothman puts out five cups of tea. He hurries over to offer me one as well, but I politely refuse."
    
    "They start discussing in earnest about curfews, message systems, Holland's latest ping-pong match, stuff like that. They seem especially concerned about the upcoming Fishtrap Cryptid Festival. No wonder; it's the largest gathering of cryptozoologists on this side of the Mississippi."
    
    "How do I know? My dad used to take me every year. A full four days of vendors hawking Nessie plushies, arguments about Bigfoot's muscle mass, and way more {i}Monster Mash{/i} than any one person should be subjected to. "
    
    "I loved every minute of it. It was like second Christmas to me. But it's nothing compared to what's in front of me right now."
    
    "It kinda sounds like a bad joke, if you think about it. A gargoyle, a Mongolian death worm, Mothman, the Jersey Devil, and a phantom kangaroo walk into a bar. \"Hey!\" says the bartender. \"Haven't I sighted you somewhere before?\""
    
    "Anyway, by the time the meeting adjourns, the light of dawn is starting to dribble through the windows. Despite the earlier rushes of adrenaline, my head is drooping hard."
    
    "Mothman comes to untie me, then hands me a Ziploc bag full of cookies."
    
    show moth neutral
    with char
    
    m "Here's something for the way home. If you want, that is. They're homemade!"
    
    "I take it reverently. Homemade cookies made by Mothman. {i}And they're chocolate chip.{/i}"
    
    p "Thank you, Mothman."
    
    show moth mix
    
    m "You're welcome. :)"
    
    hide moth
    with char
    
    w "You'll take the human back to their home, right, Greg?"
    
    g "Yeah, yeah. I'm already the messenger boy, I might as well do deliveries too."
    
    w "Good, good. Then let's hurry. We shouldn't be out and about in the daytime."
    
    scene bg lakeday
    with fade
    
    "One by one, we filter out the door. There's some idle chatter, but it looks like everyone is about to head separate ways."
    
    "This might be the last chance I ever get to talk to a real cryptid."
    
    p "Um, everyone, I have something I want to say."
    
    "All five cryptids turn to look at me, which is a very intimidating experience, by the way. I guess I'd better figure out what I want to say."
    
menu:

    "Thank you.":
        jump intro_bye1

    "Goodbye.":
        jump intro_bye2
    
label intro_bye1:
    
    p "I know this is going to sound weird, but... thank you."
    
    p "I believed in you my entire life. It's crazy to finally meet you face to face. So,{w=.5} I guess, thank you for existing. "
    
    f "Heh, you're not too bad for a human, dude."
    
    h "That's so sweet! Hope I can see you again sometime, [name]!!"
    
    jump intro_bye3
    
label intro_bye2:
    
    p "I guess I just want to say goodbye."
    
    p "This has been the strangest experience of my life. It's weird to think that everything is going to go back to normal after this. "
    
    f "Heh, it's been weird for us too, dude."
    
    h "Maybe we'll get to see you again sometime, [name]!"
    
    jump intro_bye3
    
label intro_bye3:
    
    w "Hmph. If all goes well, we won't be seeing {i}any{/i} human again."
    
    "The cryptids all say farewell before disappearing into the forest. Frankie nudges my shoulder as she passes and hands me a piece of paper. She makes a \"call me\" motion, winks, then disappears into the forest."
    
    "I glance down at the paper, confused. At the top, it says {i}Cryptid Coalition, Fishtrap Chapter{/i}. Below is the names of all five cryptids, with a phone number beside each of them."
    
    "I can't believe it. A cryptid just gave me her number."
    
    g "Come on, poop-legs, we don't have all day!"
    
    p "I'm coming!"
    
    scene bg forestday
    with fade
    
    "I pocket the paper and hurry to Greg's side. We walk silently for a bit, leaves crunching underfoot. The flashlight is unnecesssary, as the sun is up, casting long shadows through the forest."
    
    p "Oh, man. I just remembered."
    
    g "What?"
    
    p "Bea is going to be worried {i}sick{/i}."
    
    "I check my phone again, and I see five frantic text messages at least a dozen missed calls. Knowing Bea, she's probably registered me as a missing person already."
    
    p "Forget Mongolian death worms, Bea's the one who's going to eat me alive."
    
    g "Heh. Sucks to be you."
    
    p "You know, would it really hurt if I told one person? Bea is trustworthy, she'll—"
    
    g "Don't even think about it. I'm already in enough trouble."
    
    show yin annoyed
    with char
    
    yi "If you tell someone, we'll bite you!"
    
    show yin at slightleft
    with move
    
    show yang annoyed at slightright
    with char
    
    ya "No we won't, Yin."
    
    show yin shock
    with char
    
    yi "Yes we wiiiill~!"
    
    show yang neutral
    with char
    
    ya "We won't bite you, [name], but we will give you a very stern talking-to. Then we'll go tell Batu, and you'll {i}wish{/i} he'd just eaten you to begin with."
    
    p "Okay, okay, geez. I guess I'll think of a lie, then."
    
    hide yin
    hide yang
    with char
    
    "Before long, we arrive at the steep hill that leads up to the cemetery."
    
    g "Well, here we are, poop-legs."
    
menu:

    "Are you really going to keep calling me that?":
        jump intro_poop_legs1

    "We sure are, rock-head.":
        jump intro_poop_legs2
    
label intro_poop_legs1:
    
    p "Are you really going to keep calling me that?"
    
    g "Yeah, why not? You falling down that hill was the funniest thing I've seen all day."
    
    p "Ugh, of all the things to be remembered for..."
    
    jump intro_poop_legs3
    
label intro_poop_legs2:
    
    p "We sure are, rock-head."
    
    g "Nice to meet you, human-face."
    
    p "Right back at ya, gargoyle-torso."
    
    g "That one doesn't even make sense."
    
    p "Whatever."
    
    jump intro_poop_legs3
    
label intro_poop_legs3:
    
    "I stare apprehensively up the slope, which is covered in tangled undergrowth and likely more treacherous deer poop."
    
    p "Are we just doing this the hard way, then? There has to be another way around that doesn't –{nw}"
    with hpunch
    extend " HEY!"
    
    "Without warning, Greg picks me up by my armpits, and then we're flying through the air."
    
    p "Whoa, whoa, WHOA, what are you doing?!"
    
    g "Hold still, would you? You're heavy enough without you flailing around like that!"
    
    p "GREG! LET ME DOWN!!"
    
    g "I will, in a second! Jeez!"
    
    scene bg cemeteryday
    with fade
    
    "He's unexpectedly strong, for such a scrawny guy. We arrive at the cemetery, and Greg drops me on the other side of the fence. I pick myself up and dust myself off."
    
    p "Listen, buddy, you gotta warn someone before you just lift them into the air like that!"
    
    g "My B, my B. Listen, I'd love to stay and chat, but I'm tired as hell and I think I can hear my rooftop calling me. Take care of Yin and Yang, alright?"
    
    p "Alright, I will."
    
    show yin shock
    with char
    
    yi "Take care of us? We're the ones who's taking care of them!"
    
    g "Yeah, yeah, whatever. See you next time."
    
    p "There going to be a next time, then?"
    
    "Greg calls back to me as he flies through the sky."
    
    g "We'll see!"
    
    "I watch him until I can't tell him apart from the birds wheeling through the sky. Then I'm all alone in a cemetery, with nothing but my memories to prove that I just met five cryptids in the flesh."
    
    "Well... my memories, and a bag of cookies, and a slip of paper with five phone numbers on it."
    
    "With a deep breath, I start the long trek back to my aparment. I take out my phone and dial Bea. Might as well get this over with."
    
    jump day_1
    
    # This ends the game.

    return
