default theo_x = 960.0
default theo_y = 800.0
default target_x = 960.0
default target_y=800.0
default theo_facing = 1.0
default theo_moving = False

define t = Character("Theo", color="#786cad")
define tess = Character("Tessa", color="#e794bd")
define mom = Character("Mom", color="#f0ad4e")
define dad = Character("Dad", color="#3498db")
define teacher = Character("Mrs. Rosie", color="#4d4f90")
define kid_ruby = Character("Ruby", color="#d9534f")
define kid_oliver = Character("Oliver", color="#e8913a")
define kid_sunny = Character("Sunny", color="#f0ad4e")
define kid_fern = Character("Fern", color="#5cb85c")
define kid_blue = Character("Bluey", color="#5bc0de")
define kid_iris = Character("Iris", color="#9b59b6")
define kid_penny = Character("Penny", color="#e88fb5")
define kid_max = Character("Max", color="#8a8a8a")
define kids = Character("Kids", color="#4a78c7")
define husky_name = "Husky" #tbd
define puppy_name = "Puppy" #tbd2

init python:
    import math

    THEO_SPEED = 250.0
    ROOM_LEFT = 320
    ROOM_RIGHT = 1600
    FLOOR_TOP = 380
    FLOOR_BOTTOM = 1060

    def clamp(v, lo, hi):
        return max(lo, min(hi, v))

    def set_target():
        x, y = renpy.get_mouse_pos()
        x = clamp(x, ROOM_LEFT + 48, ROOM_RIGHT - 48)
        y = clamp(y, FLOOR_TOP, FLOOR_BOTTOM)
        if x < store.theo_x - 10:
            store.theo_facing = -1.0
        elif x > store.theo_x + 10:
            store.theo_facing = 1.0
        store.target_x = float(x)
        store.target_y = float(y)
        store.theo_moving = True
       

    def update_theo():
        dx = store.target_x - store.theo_x
        dy = store.target_y - store.theo_y
        dist = math.hypot(dx, dy)
        step = THEO_SPEED * 0.02

        if dist <= step:
            store.theo_x = store.target_x
            store.theo_y = store.target_y
            store.theo_moving = False
        else:
            store.theo_x += (dx / dist) * step
            store.theo_y += (dy / dist) * step
        renpy.restart_interaction()

image theo_idle:
    "pj-theo.png"
    nearest True
    zoom 3.0
    crop (0, 0, 32, 64)
    pause 0.25
    crop (32, 0, 32, 64)
    pause 0.25
    crop (64, 0, 32, 64)
    pause 0.25
    crop (96, 0, 32, 64)
    pause 0.25
    repeat

image theo_walk:
    "pj-theo-run.png"
    nearest True
    zoom 3.0
    crop (0, 0, 32, 64)
    pause 0.12
    crop (32, 0, 32, 64)
    pause 0.12
    crop (64, 0, 32, 64)
    pause 0.12
    crop (96, 0, 32, 64)
    pause 0.12
    crop (128, 0, 32, 64)
    pause 0.12
    repeat

transform flip(f):
    xzoom f
    xalign 0.5

transform theo_spot:
    xpos 960
    ypos 900
    anchor (0.5, 1.0)

transform fade_to_muted:
    xalign 0.5
    matrixcolor SaturationMatrix(1.0)
    linear 2.5 matrixcolor SaturationMatrix(0.15)

transform muted_room:
    xalign 0.5
    matrixcolor SaturationMatrix(0.15)

transform outro_spot:
    xpos 960
    ypos 900
    anchor (0.5, 1.0)

screen test_room():

    add Solid("#000000")
    add "theo-room":
        xalign 0.5

    button:
        xysize (config.screen_width, config.screen_height)
        background None
        action Function(set_target)

    imagebutton:
        idle "obj_dresser"
        focus_mask True
        pos (1100, 150)
        action Return("drawers")

    fixed:
        pos (int(theo_x), int(theo_y))
        anchor (0.5, 1.0)
        xysize (96, 192)

        fixed:
            xysize (96, 192)
            at flip(theo_facing)
            if theo_moving:
                add "theo_walk"
            else:
                add "theo_idle"

    timer 0.02 repeat True action Function(update_theo)

label start:

    #===== ACT I: Waking Up! =====
    scene black
    tess "Wake up, birthday boy! It's your big day!"
    t "Tessa! I'm FOUR!!"
    tess "You sure are, kid! Go get ready for your big day, i'm making you a surprise~"

    $ explore_time = 0.0

label bedroom_explore: 
    call screen test_room

    if _return == "drawers":
        menu: 
            "Get Dressed":
                pass
            "Keep exploring":
                jump bedroom_explore

    scene black with fade
    # $ theo_outfit = "school"
    tess "Come downstairs! It's breakfast time!"
    jump pancakes


label pancakes:
    #===== ACT II: Birthday Pancakes! =====
    scene black
    tess "Here are your pancakes, Theo."
    tess "Extra whipped cream, sprinkles, and chocolate syrup!"
    t "Yummyy Bunny!!"
    t "Tessa, they're shaped like a bunny!"
    tess "Only the best for the best little brother"
    t "Thankuuu!"
    tess "Okay, shoes on my little sidekick! Time for school."
    tess "Mom and Dad left early again today, so it's just us!"
    jump outside

label outside:
    #===== ACT III: Outside! =====
    scene black with fade
    t "The world is BIG, Tessa!"
    tess "It sure is, little guy. But I'll always be right here."
    tess "Okay, hold on. Let me fix your jacket.."
    t "I can do it!"
    tess "I know you can. I'm just checking."
    tess "Lunch is in your bag. Bunny's in there too, but don't tell Ms. Rosie."
    t "Bunny's comng to SCHOOL?!"
    tess "It's a special day. Special days get special rules."
    tess "You've got a minute before the bell. Go look around, okay? I'll be right here."
    #TO DO: EXPLORATION - Exploration outside of the school, timed (60-120s)
    tess "Theo! Bell's ringing!"
    t "Coming!!"
    tess "Have the best day. I'll see you after school, okay?"
    t "Bye Tessa!! I'm gonna be the best-est four!"
    tess "You already are, kid"
    t "..."
    t "Tessa?"
    tess "Yes, Theo?"
    t "You're my favorite."
    tess "... You're mine, too.. Go on.."
    jump preschool

label preschool:
    #===== ACT IV-A: Preschool! =====
    scene black with fade
    teacher "Good morning, everyone! We have a very special birthday today!"
    kids "Happy birthday, Theo!"
    kid_ruby "I'm the line leader today! So I get to say happy birthday first!"
    kid_ruby "Happy birthday, Theo!"
    kid_sunny "Hehehe, happy birthday!"
    t "I'm FOUR!! My sister's a superhero!"
    teacher "Is she? What's her superhero name?"
    t "Captain Cookie!!"
    kid_penny "That's not a real superhero."
    t "Yes it is, she's the best one."
    kid_max "... I have a pet rock."
    teacher "Thank you, Max."
    teacher "Theo.. is that a bunny peeking out of your bag?"
    t "Shhhh! Tessa said it's a special day. Special days get special rules!"
    teacher "... That is a very good special rule then."
    #TO DO: MINIGAME - LEARNING TIME
    jump lunch

label lunch:
    #===== ACT IV-B: Lunchtime! =====
    teacher "Lunchtime, everyone! And look, Theo, someone sent a cupcake!"
    t "A birthday cupcake!? At SCHOOL?!"
    teacher "There's a note on it! 'Happy Birthday, sidekick."
    t "Sidekick? That's me!"
    t "TESSA made it!!"
    kid_blue "Your sister is so cool."
    t "I KNOW!"
    kid_oliver "Is there pizza too?"
    kid_penny "Oliver, you can't have pizza at lunch. It's a rule."
    kid_oliver "... Is there any pizza?"
    kid_sunny "Hehehe, pizza.."
    #TO DO: MINIGAME - LUNCH TABLE
    jump naptime

label naptime:
    #===== ACT IV-C: Naptime! =====
    teacher "Okay, sleepyheads. Nap time."
    t "But I'm not sleepy.. I'm just resting my eyes..."
    teacher "Shhh you guys.. Theo's resting his eyes.."
    t "Shhh.. I'm resting my eyes.."
    t "..."
    t "Tessa's picking me up after school."
    t "She always does.."
    teacher "Sweet dreams, Theo."
    #TO DO: MINIGAME - NAPTIME
    jump snow_day

label snow_day:
    #===== ACT V: Snow Day! =====
    scene black with fade
    teacher "Look outside, everyone. It's snowing too hard to go out and play!"
    kids "Awwww!"
    kid_fern "But I love the snow..."
    teacher "So we're having indoor playtime instead!"
    kid_ruby "I'm in charge of the blocks!"
    kid_blue "Someone come build a fort with me!"
    t "The whole classroom is a playground!"
    t "That pillow is a mountain! That table is a CAVE."
    kid_sunny "Hehehehe, a cave!"
    kid_iris "... I made you something theo.."
    t "A drawing?! Is that me and Tessa?"
    kid_iris "... Yes.."
    t "She's got a cape!"
    kid_iris "...She's a superhero."
    t "I'm putting it on my wall. Thank you, Iris!"
    #TO DO: MINIGAME - SNOW DAY INDOOR PLAY
    jump pickup

label pickup:
    #===== ACT VI: Pickup Time! =====
    scene black with fade
    tess "Hey, birthday boy! Look who came to pick you up!"
    t "[husky_name]!!"
    kid_blue "Whoa! He's so fluffy!"
    kid_fern "Can I pet him? Please?"
    t "That's my dog! His name is [husky_name]!"
    t "He's my best friend, besides tessa!"
    tess "He wanted to be the first to wish you a happy birthday!"
    t "Hi [husky_name]! So fluffy!!"
    #TO DO: Minigame - playing with the husky  for the first time
    t "Tessa, did you see? He missed me!"
    tess "Of course he did. Everybody does."
    t "The best day ever is getting even bester!"
    jump getting_ready

label getting_ready:
    scene black with fade
    tess "Go change into your birthday outfit! I'll be right here!"
    t "What outfit?"
    tess "It's on your bed. It's got something extra special on it."
    #TODO: Exploration, bedroom again but husky follows theo
    #TODO minigame - timed play w husky
    #TODO dresser interaction (aka continue)
    # $theo_outfit = "party"

    t "Tessa, look! I'm the birthday boy! It says so!"
    t "[husky_name]! look! Do I look fancy?"
    tess "You look perfect."
    t "Are you coming too?"
    tess "Always. Okay, close your eyes, I'll lead you downstairs."
    t "Why?"
    tess "No questions, buddy,"
    jump party

label party:
    scene black with fade
    kids "SURPRISE!!"
    t "WHAT?! Everybody's here!"
    mom "Happy birthday, sweet boy! Sorry we're late, work ran long."
    dad "Four years old! You're getting too big!"
    t "I'm still little, Dad. The world is big."
    dad "Tessa, you did all this? You're a lifesaver."
    tess "It was nothing. Go have fun, Theo."
    kid_oliver "PIZZA!"
    kid_penny "We have to sing first. That's the rule."
    # TODO: MINIGAME - party games (musical chairs, pin the tail, etc.)
    # TODO: pizza scene (optional)

    kids "Happy birthday to you, happy birthday to you..."
    kids "Happy birthday, dear Theo, happy birthday to you!"
    t "I'm gonna burst."
    t "Tessa, did you see?! They sang to ME!"
    tess "I saw, little guy. Make a wish."

    # TODO: EXPLORATION - playing in the snow with friends (and the husky!)
    kid_fern "Look, Theo! A snow angel!"
    kid_ruby "I'm the best at snowballs."
    kid_sunny "Hehehe, SNOW."

    # presents
    kid_blue "Here, Theo! I picked this one just for you."
    t "It's... a TRUCK! Bluey, you're the best!"
    kid_iris "...This is for you too."
    t "Another drawing! Thank you, Iris!"
    kid_max "I got you a rock."
    t "...I love it, Max."
    mom "Here's from me and Dad, sweetheart."
    t "Thank you for my presents! Thank you, thank you!"
    t "..."
    t "Tessa's been cleaning up this whole time.."
    t "Wait. Where's Tessa's present?"
    t "Maybe she forgot..."

    # ===== ACT IX: Hot cocoa =====
label cocoa:
    scene black with fade
    mom "Everybody inside! Hot cocoa time."
    kid_oliver "Marshmallows!"
    t "Marshmallows!"
    kid_penny "You have to wait until it cools. It's a rule."
    "Tessa checks her phone."
    tess "Save me one, okay? I'll be right back."
    t "Where are you going?"
    tess "Just something I forgot. Don't go anywhere."
    t "Okay..."
    t "..."
    t "She forgot something? On MY birthday?"
    kid_fern "Maybe it's a surprise."
    t "...Maybe."
    jump real_present

    # ===== ACT X: The real present =====
label real_present:
    scene black with fade
    tess "Okay, close your eyes. No peeking, sidekick."
    t "I'm not peeking!"
    tess "Are you sure?"
    t "... Maybe a little peeking."
    tess "Ha! Knew it! Okay, now really close them tight."
    tess "Open them."
    t "A... BOX?"
    t "..."
    t "It's wiggling."
    t "TESSA. IT'S A SECOND PUPPY?! I have TWO dogs now!!"
    kid_sunny "Hehehe, PUPPY!"
    kid_fern "Aww, he's so tiny..."
    t "You didn't forget!"
    tess "I'd never forget, buddy, I just had to pick him up from the shelter."
    t "Was he scared?"
    tess "A little.. but he's with us now."
    t "The world is a little scary."
    t "...But not when somebody's with you."
    tess "..."
    tess "Happy birthday, little guy."
    jump thank_you

    # ===== ACT XI: Thank you, Captain Cookie =====
label thank_you:
    scene black with fade
    mom "Thank you all for coming!"
    kid_blue "Bye, Theo! Best birthday ever!"
    kid_ruby "Bye! I'm the first one out the door!"
    kid_max "Bye. Don't lose the rock."
    kids "Happy birthday, Theo!"
    dad "Drive safe, everyone!"
    # TODO: MINIGAME - playing with both dogs (husky meets the new puppy)
    t "Look, [husky_name] and [puppy_name] are best friends already!"
    t "Thank you Tess!! You're the best!!"
    tess "...Anytime, kid."
    mom "Tessa, honey, can you get Theo to bed? We're wiped."
    tess "Of course, Mom. I'll take care of him."
    jump goodnight

    # ===== ACT XII: Goodnight, little guy =====
label goodnight:
    scene black with fade
    # TODO: PERSPECTIVE SWITCH - desaturate everything except Theo
    tess "Okay, time for bed, birthday boy."
    t "Can [husky_name] and [puppy_name] sleep with me?"
    tess "They'll be right here. Come on."
    t "...goodnight captain cookie.."
    tess "Goodnight, my special sidekick."

    # ===== ACT XIII: Tessa's world =====
label tessa_world:
    scene black with fade
    scene theo-room at muted_room with dissolve

    "..."
    "Tessa closes her door softly, so she doesn't wake him."
    tess "Okay.. Lunch for tomorrow. Puppy food. Permission slip."
    tess "..."
    tess "Mom and dad were really happy tonight.."
    tess "That's good. They're good at parties."
    tess "They love him. I know they do.."
    tess "But they're not the ones who know he needs the hall light on."
    tess "Or that the bunny goes in the wash on Sundays, when he isnt paying attention."
    tess "..."
    tess "It's okay."
    tess "I used to be the one who got surprised on my birthday.."
    tess "It's okay."
    tess "It's okay.. I'm not mad.. I'm just.. tired.."
    tess "..."
    tess "He said I'm the best."
    tess "'You're the best, Tess!'"
    tess "I think that's enough to keep going."
    tess "The world is really big. And someone has to make it feel a little smaller for him."
    tess "Goodnight, little guy."

    scene black with fade
    "It's a big world, Little Guy.."