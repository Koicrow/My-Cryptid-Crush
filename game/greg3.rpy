# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default piggy_done = False

# The game starts here.
    
label greg3:
    
    $ save_name = "Greg 3"
    
    "I'm sure Greg is up for some fun. Gargoyles are usually out at night, right?"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Whatchu up to tonite?{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Not much dawg{/i}{/font}{/size}"
    
    "I hesitate. Now's the time to ask him out."
    
menu:

    "Wanna chill?":
        jump greg3_invite1

    "You. Me. City center.":
        jump greg3_invite2
   
    "Wanna have some fun, hot stuff (;":
        jump greg3_invite3
   
label greg3_invite1:
    
    "Best to keep it low-key, right?"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Wanna chill? Put on some Netblix or something?{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Sure{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}My place or yours?{/i}{/font}{/size}"
    
    "I chew my lip as I evaluate the state of my apartment. It's not that I don't want Greg to see how messy I am. I'm more worried about finding two clear spots for us to sit."
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Better do yours. Mine's a dump{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Lol okay, but don't come expecting a 3 star hotel{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}You mean 5 star?{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Trust me, if my place was a hotel it would be less than 3 stars{/i}{/font}{/size}"
    
    jump greg3_invite4
   
label greg3_invite2:
    
    "Best to be confident, right?"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}You. Me. City center. Are you in?{/i}{/font}{/size}"
    
    "Yang pipes up from behind me."
    
    ya "What about us? Are we invited?"
    
    p "Okay, you've {i}got{/i} to stop reading over my shoulder!"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Sure, why not?{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Do you wanna meet me at my place{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Sounds good{/i}{/font}{/size}"
    
    jump greg3_invite4
   
label greg3_invite3:
    
    "Best to get to the point, right?"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Wanna have some fun, hot stuff (;{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Listen{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Ur gonna have to try harder than that if you want to hit this{/i}{/font}{/size}"
    
    "I bite my lip. That got shot down hard."
    
    show yin neutral with char

    yi "Yikes."
    
    p "Okay, you've {i}got{/i} to stop reading over my shoulder!"
    
    hide yin with char

    "I angle my phone away from Yin and Yang and type in another response. Maybe I can still salvage this?"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}What if I buy you a drink first?{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}No promises{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}I'll take that free drink tho{/i}{/font}{/size}"
    
    "I allow myself a slightly self-indulgent fistpump."
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}That's what I like to hear!!{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}U free now?{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Sure{/i}{/font}{/size}"
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}Do you wanna meet me at my place{/i}{/font}{/size}"
    
    p "{size=+7}{font=Iceland-Regular.ttf}{i}Sounds good{/i}{/font}{/size}"
    
    jump greg3_invite4
   
label greg3_invite4:
    
    g "{size=+7}{font=Iceland-Regular.ttf}{i}I'll send you an address, if you come by I'll give you a lift{/i}{/font}{/size}"
    
    "I stare at the screen for a bit."
    
    p "I hope he doesn't mean that literally."
    
    scene bg city1
    with fade
    
    "Before long, I'm dressed nice and cozy and biking my way into the city. It's a crisp, clear night, just overflowing with stars, like the sky is showing off."
    
    "Even at midnight, the city is active. Even on the outskirts of the city, I pass about five taxis, a dozen drunk people, and one very persistent phone case vendor."
    
    "Eventually, I coast to a stop, my tires gently bumping over the cracks in the sidewalk. I look down at my navigation app, then around at the deserted street, then straight up at the top of the skyscrapers."
    
    p "There's no way this is the right place."
    
    show yin neutral with char

    yi "Nah, this is the place."
    p "Really? Out in the middle of the business district?"
    
    show yin at slightleft
    show yang neutral at slightright
    with char

    ya "It's the right place, horizontally. But about five hundred feet too low."
    
    "I give Yin and Yang a look of disbelief, then crane my head to look at the skyscrapers again. That's when I see him."

    hide yin
    hide yang
    with char

    play music "greg.ogg" fadeout 1
    
    "You wouldn't expect me to be so shocked, since I knew who it was. But there's nothing that can prepare you for a sight like this. His wings are huge and block out the stars, as if he's made of shadow. It looks like I'm about to be picked up by giant bat claws, or something like that."
    
    "Now I understand why people thought he killed dogs and drained them of their blood. When you see him like {i}that{/i}, you sort of expect it."
    
    show greg wing smirk with char

    "He lands in front of me and folds up his wings, wearing a cocky grin."
    
    g "Hey, [name]."
    p "Sup."
    g "Impressed?"
    
menu:

    "You wish.":
        jump greg3_impressed1

    "A little.":
        jump greg3_impressed2
        
label greg3_impressed1:
    
    p "You {i}wish{/i}. Just a bit startled."
    
    show greg wing annoyed

    g "Aw, not even a little impressed?"
    p "Yes, your wings are very big, congratulations."
    
    show greg wing smirk

    g "Thank you, thank you, I know."

    jump greg3_impressed3
        
label greg3_impressed2:
    
    p "Maybe a little."
    
    show greg wing neutral

    g "Heh. Don't feel bad, I have that effect on everybody."
    p "Oh, shush."
    
    jump greg3_impressed3
        
label greg3_impressed3:
    
    show greg neutral

    g "Yin, Yang, good to see ya."
    
    show yang neutral 2 at midright with char

    ya "Hope you're keeping out of trouble."
    g "Eh, no promises."
    
    hide yang with char

    p "So, are you ready to go?"
    g "Actually, I came up with a better idea."
    
    "He pulls out a can of spray paint and shakes it, making that satisfying {i}chka-chka-chka{/i} sound."
    
    show greg smirk
    
    g "Tagging."
    p "Oh??"
    
    show greg happy

    g "It'll be fun! We sneak around the city, tag a couple of walls, maybe throw up some other art. You in?"
    p "Sure, why not?"
    
    show greg neutral

    g "Sick."
    
menu:

    "Are you sure we won't get caught?":
        jump greg3_you_in1

    "What are you going to paint?":
        jump greg3_you_in2
   
    "Let's GO.":
        jump greg3_you_in3
   
label greg3_you_in1:
    
    p "Are you sure we won't get caught?"
    
    show greg smirk

    g "Come on, no cop is ever going to keep up with {i}this{/i}."
    
    "He points with his thumb at his wings."
    
    p "Uh-huh. And what about me? The bumbling human?"
    
    show greg worried

    g "Uhhh, well..."
    
    "Greg scratches his head."
    
    show greg neutral

    g "You'll be alright. We won't let them see us in the first place! Sound good?"
    p "{i}Sigh.{/i} Comforting."
    
    jump greg3_you_in4
   
label greg3_you_in2:
    
    p "What are you going to paint?"
    g "Oh, a little bit of this and that. Maybe throw up my icon in a couple of hard-to-reach spots. See what inspiration strikes."
    
    show greg smirk

    g "I have a big burner cooking, but I'll save that for another time. It's going to be sweet."
    p "Cool, cool."
    
    show greg neutrla

    jump greg3_you_in4
   
label greg3_you_in3:
    
    p "Man, I'm pumped. Let's GO!"
    
    show greg smirk

    g "Heh. Love the enthusiasm."
    
    show greg neutral

    jump greg3_you_in4
   
label greg3_you_in4:
    
    g "First, I gotta stop by my place. Need to grab the rest of my equipment. Do you mind if I, uh, give you a lift?"
    p "Hey, you asked this time. You're learning!"
    
    show greg smirk

    g "Yep, model of courtesy right here."
    p "Go ahead."

    show greg worried
    
    "I chain my bike to a nearby bench. Greg awkwardly approaches me and reaches out with his hands. Then he pulls them right back. He looks like a nervous kid at a middle school dance."
    
    g "Uh, how should I...?"
    p "You didn't ask me {i}last{/i} time."
    
    show greg annoyed

    g "Yeah, well, I didn't {i}know{/i} you last time. And we're going a lot higher now."
    
    jump greg3_carry0
    
label greg3_carry0:
    
    menu:

        "Under the arms.":
            jump greg3_carry1

        "Princess carry.":
            jump greg3_carry2
   
        "Piggyback." if piggy_done == False:
            $ piggy_done = True
            jump greg3_carry3
   
label greg3_carry1:
    
    p "Under the arms is fine, like before."
    
    show greg neutral

    g "Alright, here goes."

    hide greg with char
    
    "Greg steps behind me and puts his arms under mine. Unlike last time, he smells strongly of cologne. He didn't put that on just for me, did he?"
    
    jump greg3_carry4
    
label greg3_carry2:
    
    p "Do a princess carry!"
    
    show greg neutral

    g "What do I look like, a superhero?"
    
    if comics:
        p "Not quite, Gargoyle Boy."
        
        show greg annoyed

        g "Ugh, I already regret telling you about that."
        
    p "Come on, just do it! I've always wanted to be princess carried."
    
    hide greg with char

    "Greg leans over, then picks me up with one arm under my knees and the other under my back. It's actually pretty comfortable." 
    
    "Unlike last time, he smells strongly like cologne. He didn't put that on just for me, did he?"
    
    jump greg3_carry4
    
label greg3_carry3:
    
    p "Give me a piggyback ride!"
    
    show greg annoyed

    g "Uh, no can do, poop-legs. I need my wings to fly."
    p "Oh, yeah. Whoops."
    
    jump greg3_carry0
    
label greg3_carry4:
    
    scene bg cityview
    with fade
    
    play music "mothman.ogg" fadeout 1

    "He lifts off with a powerful jump. I yelp as my feet leave the ground, then we're soaring up and up into an endless sky." with vpunch
    
    show yin shock at slightleft
    show yang neutral 2 at slightright
    with moveinbottom

    "Yin and Yang zip through the air beside me."
    
    yi "Hope you're not afraid of heights!"
    p "Bit late for that now!!"
    
    hide yin
    hide yang
    with moveouttop

    "Seeing the streets shrink below me is more exhilarating than any rollercoaster I've been on. Let me tell you, these skyscrapers are {i}way{/i} taller than they seem on the inside. Thankfully, Greg's grip feels secure."
    
    scene bg rooftop
    with fade

    "Before long, we summit one of the tallest buildings, and Greg sets me gently on the roof. My legs feel wobbly, like I just ran a marathon. I peer over the edge to see exactly how high up we are. Which is to say, hella high."
    
    p "Wow, that was a ride!"
    
    show greg annoyed with char

    g "Glad {i}one{/i} of us had fun. Humans are freaking heavy."
    p "They are? I mean, we are?"
    g "Yeah, in comparison. Have you ever tried lifting Mothman? Boy's a feather."
    
    show greg neutral

    "Greg saunters across the roof, bringing my attention to the construction on the other side of the building."
    
    show greg smile

    g "Anyway, welcome to my pad!"
    
    "To my astonishment, there's a sizeable shelter right on top of the roof. It's built against the roof access building, with the other walls made of sheet metal and colorful fabric curtains. A smaller room juts out of one side, this one fashioned out of a canvas tent."
    
    p "Whoa."
    
    show greg neutral

    g "Make yourself at home. Mi casa es you casa."
    p "It's \"mi casa es tu casa.\""
    
    show greg annoyed

    g "Whatever."
    
    hide greg with char

    "Greg disappears through a flap in the fabric, and I poke my head inside."
    
    "It's surprisingly spacious, complete with floor pillows and a collapsible drawing desk. One corner has a minifridge and a bunsen burner, their cords disappearing under the wall."
    
    "In another corner, clothes hang from a makeshift rack. Fairy lights droop down from the ceiling. The whole thing looks thrown-together, but comfy."
    
    show greg neutral with char

    p "Do you really live here?"
    
    show yin shock at midleft with char

    yi "Didn't you know? Gargoyles live on roofs!"
    yi "The stone kind, anyway."
    
    show greg smirk

    g "This is the building that I janitor...ize. The place where I'm a janitor."
    g "The location is great, and the view is killer. Best part about it? No rent."
    
    show greg neutral
    hide yin with char

    "He drops onto a purple floor pillow with a {i}foomp{/i}."

    g "So, what do you think?"
    
menu:

    "It's... charming.":
        jump greg3_pad1

    "I love it.":
        jump greg3_pad2
   
    "Where do you use the bathroom?":
        jump greg3_pad3
   
label greg3_pad1:
    
    p "It's... charming."
    
    show greg annoyed

    g "Just charming?"
    p "I mean, I can't really talk. I live in a shitty one-room apartment."
    
    show greg neutral

    g "Eh. I guess I could have cleaned a little."
    
    "He uses his foot to nudge an old GameJoy that lays forgotten on the floor, alongside a tin can full of markers and a stuffed penguin."
    
    jump greg3_pad4
   
label greg3_pad2:
    
    p "I love it. I don't know what I expected a cryptid's home to look like, but this is amazing."
    
    show greg smirk

    g "Heh, that's what I thought."

    jump greg3_pad4
   
label greg3_pad3:
    
    p "Where do you use the bathroom??"
    
    show greg annoyed

    "Greg rolls his eyes."
    
    g "Downstairs, in the building. I have the keys."
    p "Oh, that makes sense."
    
    jump greg3_pad4
   
label greg3_pad4:
    
    show greg smirk

    g "I'm a bit of a homemaker, you see. Put this together myself. With a little help from Holly, of course."
    p "Really? That's pretty impressive."
    
    show yang close at midright with char

    ya "Pfft. The place looked like a prison cell before Holly."
    
    show greg upset

    g "Oh, come on. Let me have this!"
    
    hide yang with char

    "Greg waves Yang away. Meanwhile, Yin perches happily on a little bed."
    
    show greg neutral
    show yin neutral at midleft with char

    yi "Oh, home sweet cat bed! It's been too long!"
    g "Don't get too comfortable. There's public property to be defaced."

    "Greg hops back up and starts loading things into a bookbag: spray cans of every size, homemade stencils, notebooks. He zips up the top and shrugs it on."
    
    g "Ready to go?"
    p "You bet."
    
    show yin annoyed

    yi "Ugh, can I have five minutes to rest in peace?"
    
    show yang neutral 2 at midright with char

    ya "Come on, Yin. Don't be a lazy 'squatch."
    
    scene bg city1
    with fade
    
    show greg neutral with char

    "Once Yin is up, Greg takes me on another breathtaking flight back to the ground. While I get my legs to stop wobbling, he inspects the wall of a narrow alleyway."
    
    show greg upset

    g "Damn, someone crossed out my throw-up."
    p "What? English, please?"
    
    show greg annoyed

    "Greg illuminates the brick wall with a flashlight. It's marked with a street artist's elaborate signature, done in plain black. There's a hint of something pink underneath."
    
    g "Another writer put something on top of my stuff. Bastard."
    p "Ohh. Are you going to put yours back on top?"
    
    show greg neutral

    g "Think I should?"
    
menu:

    "Yes.":
        jump greg3_cross_out1

    "No.":
        jump greg3_cross_out2
   
label greg3_cross_out1:
    
    p "Yes, tell them who's boss!"
    g "Ehhh..."
    
    "Greg pulls out a solid red can and shakes it."
    
    show greg smirk

    g "Probably just some new guy, 'cause I don't recognize the tag. Not worth the effort. But I {i}will{/i} do this."
    "He paints an X on top of the graffiti with broad strokes."
    
    p "Nice."
    
    jump greg3_cross_out3
   
label greg3_cross_out2:
    
    p "Nah, just leave it."

    show greg annoyed

    g "You're probably right. Not worth getting into a fight over a shitty alleyway."
    
    jump greg3_cross_out3
   
label greg3_cross_out3:
    
    show greg happy

    g "Come on, let's find a clean wall to mark up!"
    
    scene bg city2
    with fade

    show greg neutral with char
    
    play music "kangaroo.ogg" fadeout 1

    "We travel a couple of blocks, heading toward the older, slummier side of the city. The only movement on the street is a flickering lamp. This is exactly the sort of place I wouldn't go at night, but why be afraid of muggers when your escort is a monster?"
    
    "I never really paid attention to the street art before now, but there's more than I expected. Big bubble letters on the side of an apartment building, stickers slapped on street signs, even a leering dragon made of dripping paint."
    
    p "Are there a lot of street artists here?"
    g "Not really. City's not {i}that{/i} big, and they'll paint over most things in the nicer part of town."
    
    show greg happy

    g "I should take you to the rail yard someday! Lots of cool graffiti there."
    
    show greg neutral

    "Eventually, Greg stops in front of a couple of storefronts protected by metal curtains."
    
    g "Alright, this is the place."
    p "Here? There's not a lot of flat wall."
    
    show greg wing smirk
    
    g "Not at ground level. Hold the flashlight for me?"
    
    hide greg with char

    "He hands me the flashlight. Then he flaps into the air, buffeting me very rudely with wind, and comes to a rest on a second-story windowsill, like some sort of deranged bird."
    
    p "Whoa! What if someone sees you?"
    g "I'll be fast! Shine the light on that wall. And look out for people passing by."
    
    "I shine the light as he prepares a can of pink paint, then starts drawing deft strokes on the wall. I make sure to look left and right on occasion, but I'm not entirely sure what I'm supposed to do if someone {i}does{/i} pass by."
    
    "Then I realize with a jolt that a hunched figure is walking down the street nearby."
    
menu:

    "(Ignore them)":
        jump greg3_passerby1

    "(Warn Greg, quietly)":
        jump greg3_passerby2
   
    "(Warn Greg and run)":
        jump greg3_passerby3
   
label greg3_passerby1:
    
    "It's probably nothing to worry about, right? If this whole experience has taught me anything, it's that people tend to mind their own business, even if there's a freaking gargoyle right in front of their faces."
    
    "The pedestrian stops on the other side of the street. I get the chilling feeling that they're looking at us, but I just keep my flashlight steady and pretend like I know what I'm doing."
    
    "Then they keep walking. Phew."
    
    show greg wing neutral with char

    "I'll admit, the sound of Greg dropping back to the floor startles me a little." with hpunch
    
    p "Ah!!{w} Oh, you're done?"
    
    show greg smirk

    g "Yeah, told you it'd be quick."
    
    "I look up at the new painting on the wall. It's a monstrous monochrome face, with jutting fangs and horns. The symbol from his hoodie."
    
    jump greg3_passerby4
   
label greg3_passerby2:
    
    p "Pssst. Greg. Pedestrian across the street."
    
    "Greg turns his head and squints."
    
    g "Eh, they're probably just going to the corner store for a snack or something. Or they're trying to mug someone. Either way, it doesn't concern us."
    p "How does that second one not concern us?!"
    
    show greg wing neutral with char

    "He drops back down on the floor." with hpunch
    
    p "Wait. You're done?"
    
    show greg smirk

    g "Yeah, told you it'd be quick."
    
    "I look up at the new painting on the wall. It's a monstrous monochrome face, with jutting fangs and horns. The symbol from his hoodie."
    
    jump greg3_passerby4
    
label greg3_passerby3:
    
    p "Greg! Someone's coming!"
    
    "I look frantically around, then turn off the flashlight and dash down the street." 
    
    scene bg alley
    with fade

    stop music fadeout 1
    
    "I duck into an alleyway where hopefully no one will see me. My heart is beating like crazy. Shouldn't Greg have briefed me on this?!"
    
    show greg shock with moveinleft

    "Soon, Greg dashes into the alleyway after me, clutching his bag in one hand. Yin and Yang fly behind him."
    
    g "[name], what is it? Did you see a cop?"
    p "I'm not sure, but {i}someone{/i} was about to see us. I told you as soon as I noticed."
    
    show greg annoyed

    g "Just one person? In a cop uniform?"
    p "Uh, no, just a regular person, I think."
    
    show greg upset

    "Greg sighs and drags his hands down his face."
    
    p "What? What's wrong?"

    show greg annoyed
    
    g "You don't have to run as soon as someone passes by, [name]. What are they going to do, call 911 because they saw someone painting on a wall?"
    p "Oh. I didn't think of that. My bad."
    
    show greg neutral

    g "Whatever. It's alright. Should have told you."
    p "I'm sorry, really! Should we go back and finish it?"
    g "Nah, already finished."
    p "Wait... really?"

    show greg smirk
    
    g "Yeah, told you it'd be quick."
    
    scene bg city2
    with fade

    show greg neutral with char

    play music "kangaroo.ogg" fadeout 1
    
    "We walk back to the wall, and I look up at the new painting. It's a monstrous monochrome face, with jutting fangs and horns. The symbol from his hoodie."
    
    jump greg3_passerby4
    
label greg3_passerby4:
    
    show greg neutral
    
    g "Being a gargoyle has its perks. My tags are all over the city, on hard-to-reach walls. No one knows how I do it."
    p "That is wicked."

    show greg smirk
    
    g "Thank you, thank you. All in a day's work."
    
    hide greg with char

    "Greg hits a couple of other walls in the neighborhood. I dutifully stand watch, eating chocolate-coated pretzels out of a bag that he brought with him. I give Yin and Yang a few too."
    
    show greg neutral with char

    p "Why do you have to do so many walls?"
    g "It's about staking a claim, baby. Making my presence known."
    
    show greg happy

    g "You know, my graffiti was on the news once. The mysterious winged street artist!"
    p "Heh. That's funny."
    
    show greg annoyed

    g "What is?"
    p "You're a cryptid, so you have to stay out of sight. But your graffiti is all about being seen."
    
    show greg neutral

    g "Guess so."
    "I grab a paint can out of his backpack."
    p "Let me draw something!"
    g "What? Right here?"
    p "Yeah, next to yours. I'm making my debut as the winged street artist's bumbling sidekick."
    
    show greg smirk

    g "Heh. Go ahead."

    "I stick out my tongue in concentration as I draw a shape next to Greg's monster tag."
    
menu:

    "A heart":
        jump greg3_sidekick1

    "A skull":
        jump greg3_sidekick2
   
    "An eye":
        jump greg3_sidekick3
   
    "A :3 face":
        jump greg3_sidekick4
   
label greg3_sidekick1:
    
    show greg neutral

    g "A heart?"
    p "Yep!"
    g "Cute."
    
    jump greg3_sidekick5
    
label greg3_sidekick2:
    
    show greg neutral

    g "A skull?"
    p "It's almost Halloween!"
    g "Very seasonal of you."
    
    jump greg3_sidekick5
    
label greg3_sidekick3:
    
    show greg neutral

    g "An eye?"
    p "Yeah. Now when people look at your graffiti, it'll look back at them."
    g "Sick."
    
    jump greg3_sidekick5
    
label greg3_sidekick4:
    
    show greg annoyed

    g "...Really?"
    p "Really :3"
    
    show greg shock

    g "H-how did you do that with your voice??"
    
    jump greg3_sidekick5
    
label greg3_sidekick5:
    
    hide greg with char

    "Time passes in a blur. It's exhilarating in its own way, dashing through the streets with Greg and turning the city into our canvas. We're both cryptids tonight, seen only by the marks we leave behind."
    
    "Sorry. That was really corny. I get like that sometimes when I stay up too late."
    
    scene black
    with fade
    
    stop music fadeout 1

    "Once we're done with our mayhem, Greg flies me to the top of a building. It's some sort of laundromat, or a company that sells washing machines, or something. I wasn't really paying attention."
    
    p "Oh, man, my legs are sore. If I keep hanging out with you, I might get back into shape."
    g "Uh-huh. And if I have to keep lugging you through the air, I'm going to end up ripped."
    
    scene bg cityview
    with fade
    
    "I carefully sit down on the edge of the building, taking in the view. After a moment, Greg sits down beside me. Yin and Yang plop themselves down on either side."
    
    show greg worried with char

    g "You're not scared of falling?"
    p "A little, I guess. But you'll catch me if I fall, right?"
    
    show greg smirk

    g "Of course. I mean, I'll try. No guarantee of success. Maybe just don't fall to begin with."
    p "Hah, I'll keep that in mind."
    
    show greg neutral

    "The wind whips around us and blows our hair into unflattering shapes, although Greg's is so messy to begin with that it hardly makes a difference. He pulls out a pack of cigarettes and offers one to me."
    
menu:

    "Thanks.":
        jump greg3_cigs1

    "No thanks.":
        jump greg3_cigs2
   
label greg3_cigs1:
    
    p "Thanks."
    
    "we both grab one, and lights us both up. I take a deep draft."
    
    show greg annoyed

    g "Holly hates when I smoke. She always says it's a deal-breaker for her."
    
    jump greg3_cigs3
    
label greg3_cigs2:
    
    p "No thanks."
    g "Alright."
    
    "He takes one out for himself, then pauses."
    
    show greg worried

    g "Is it alright if I...? I mean, do you mind?"
    p "I'm not going to stop you."
    
    show greg annoyed

    g "I mean, some people really hate smokers. Holly always says it's a deal-breaker for her."
    
    jump greg3_cigs3
    
label greg3_cigs3:
    
    p "Oh, are you two dating?"

    show greg neutral

    g "What? No, no, no. Just friends. Drinking buddies."
    p "Cool, cool."
    g "How about you, are you seeing anyone?"
    p "Nah."
    
    "The biggest yawn of the century hits me all of a sudden."
    
    p "Oh, man, I'm so sleepy. I don't usually stay up this late."
    
    show greg worried

    g "You're not actually going to fall, are you? Maybe you should get away from the edge."
    p "Heh, why are you so worried about me, all of a sudden?"
    
    show greg smirk

    g "Come on, what will I do without my bumbling sidekick?"
    
    show yang annoyed at midright with char

    ya "Oh, get a room."
    
    show greg neutral

    "We both shush Yang at the same time."
    
    hide yang with char

    "Some time passes in silence, with cigarette smoke drifting through the air. I finally decide to say what's on my mind."
    
    p "Man, I don't want to go back home."
    g "How come?"
    
menu:

    "Bea is getting suspicious.":
        jump greg3_home1

    "My dad keeps telling me to get a life.":
        jump greg3_home2
   
    "I'd rather be with you.":
        jump greg3_home3
   
label greg3_home1:
    
    p "Bea is getting suspicious. She thinks something's wrong because I'm trying to avoid talking about cryptids, and I think {i}she{/i} thinks it's something worse than it actually is."
    p "It's just a lot to deal with. If this keeps up, she's probably going to stage an intervention or something."
    
    show greg worried

    g "Oh."
    p "I never thought keeping a secret could be this hard! My whole life I was searching for answers, and now I'm on the other side, keeping the truth from Bea."
    
    "Greg is silent for a few beats, making me think I said too mcuh."
    
    show greg smirk

    g "I guess that's a tough situation to {i}Bea{/i} in."
    p "..."
    
    show greg neutral

    g "You know, like, the name? Bea?"
    
    jump greg3_home4
   
label greg3_home2:
    
    p "My dad keeps telling me to get a life. Well, not in those words, but that's the gist of it."
    p "He thinks I'm still running around cryptid hunting, and I can't correct him without telling him what I've {i}actually{/i} been doing."
    
    show greg worried

    g "Oh."
    p "And the worst part is that he's right! Like damn, my life really ground to a halt after I dropped out of college. My job sucks! And I'm losing touch with my friends!"
    
    "Greg is silent for a few beats, making me think I said too much."
    
    show greg smirk

    g "I guess you're losing your {i}touch{/i}."
    p "..."
    
    show greg neutral

    g "You know, like, losing touch with your friends? Losing your touch?"
    
    jump greg3_home4
   
label greg3_home3:
    
    p "I'd rather be here with you."
    p "I mean, not in a creepy way! It's just that the human world is so boring now. I'm guess I'm worried I'll have to go back to being normal one day, and nothing will ever top meeting you."
    
    show greg worried

    g "Oh."
    p "Really, hanging out with you and the others has been amazing. But I can't even tell my friends what I've been doing the past few days! You know?"
    
    "Greg is silent for a few beats, making me think I said the wrong thing."
    
    show greg smirk

    g "I guess we left you in a {i}daze{/i}."
    p "..."
    
    show greg neutral
    
    g "You know, like, the past few {i}days{/i}? Left you in a {i}daze{/i}?"
    
    jump greg3_home4
   
label greg3_home4:
    
    p "I get it. Funny."
    
    show greg worried

    g "Sorry."
    p "No, it's alright."
    g "Not great at the whole emotional support thing."
    p "Heh, I can see that."
    
    show greg neutral

    "Another moment of silence passes."
    
    g "I'm sorry that you have to deal with shit like that, just because you met us."

    show greg happy

    g "But I'm glad you did."
    p "Me too."
    
    show greg neutral

    "Eventually, Greg stubs out his cigarette on the rough roof and stands up."
    
    g "I'd better get some sleep. There's a Cryptid Coalition meeting tomorrow."
    p "Really? So soon after the last one?"
    g "Yep. This one's a regular meeting. Last time was because Mothman slipped up."
    
    show greg smirk

    g "You're welcome to come too, if you want. I think you're an honorary cryptid by now."
    p "Heh, thanks. I'll see if I have time."
    
    show greg neutral

    g "Ready for one last flight?"
    p "Ready."
    
    scene bg city1
    with fade

    "Greg takes me back to my bike, and we say a quick goodbye before he flies back up to his rooftop roost. Fighting back yawns, I start the long trip back home."
    
    "Yin and Yang must be sleepy too, because they don't make any quips on the way home. Or maybe they fell asleep in my bag. Either way, I appreciate the silence to work through my thoughts."
    
    "It's crazy to think that falling down that hill changed my life forever. Now that I've met Greg and the others, I can't ever close my eyes to the hidden world of cryptids. Not that I'd ever want to. What kind of cryptid hunter would I be, otherwise?"
    
    scene bg suburbannight
    with fade
    
    play music "forest_night.ogg" fadeout 1

    "As I round the bend to my apartment building, I wonder what I am to the cryptids. A liability, for knowing their secret? Just an onlooker? A friend? Or could I be something more?"
    
    "Maybe I'll be able to untangle all of this at the meeting tomorrow. Right now, I'm going to collapse if I don't get some sleep."