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

from profiling.tracing import label

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
    jump outside

label outside:
    #===== ACT III: Outside! =====
    scene black with fade
    t "The world is BIG, Tessa!"
    tess "It sure is, little guy. But I'll always be right here."
    #TO DO: EXPLORATION - Exploration outside of the school, timed (60-120s)
    tess "Have the best day. I'll see you after school, okay?"
    t "Bye Tessa!! I'm gonna be the best-est four!"
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
    teacher "Tessa? What's her superhero name?"
    t "Captain Cookie!!"
    kid_max "... I have a pet rock."
    teacher "Thank you, Max."
    #TO DO: MINIGAME - LEARNING TIME
    jump lunch

label lunch:
    #===== ACT IV-B: Lunchtime! =====
    teacher "Lunchtime, everyone! And look, Theo, someone sent a cupcake!"
    t "A birthday cupcake!? At SCHOOL?!"
    t "Thank you!"
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
    kid_iris "... I made you something theo.."
    t "A drawing?! Is that me and Tessa?"
    kid_iris "... Yes.."
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
    #TO DO: Minigame - playing with fluffy for the first time
    t "The best day ever is getting even bester!"

label getting_ready:
    scene black with fade
    tess "Go change into your birthday outfit! I'll be right here!"
    #TODO: Exploration, bedroom again but husky follows theo
    #TODO minigame - timed play w husky
    #TODO dresser interaction (aka continue)
    # $theo_outfit = "party"

    t "Tessa, look! I'm the birthday boy! It says so!"
    t "[husky_name]! look! Do I look fancy?"
    tess "You look perfect, come on, let's go downstairs!"
    jump party:

label party:
    scene black with fade
    kids "SURPRISE!!"
    t "WHAT?! Everybody's here!"
    mom "Happy birthday, sweet boy!"
    dad "Four years old! You're getting too big!"
    t "I'm still little, Dad. The world is big."
    kid_oliver "PIZZA!"
    kid_penny "We have to sing first. That's the rule."
    # TODO: MINIGAME - party games (musical chairs, pin the tail, etc.)
    # TODO: pizza scene (optional)

    kids "Happy birthday to you, happy birthday to you..."
    kids "Happy birthday, dear Theo, happy birthday to you!"
    t "I'm gonna burst."

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
    t "Wait. Where's Tessa's present?"
    t "Maybe she forgot..."
    # (Keep this beat quiet and short. This is the little-sad moment.)

    # ===== ACT IX: Hot cocoa =====
label cocoa:
    scene black with fade
    mom "Everybody inside! Hot cocoa time."
    kid_oliver "Marshmallows!"
    t "Marshmallows!"
    kid_penny "You have to wait until it cools. It's a rule."
    tess "Theo, I'll be right back, okay? Don't go anywhere."
    t "Okay..."
    t "Where's Tessa going?"

    # ===== ACT X: The real present =====
label real_present:
    scene black with fade
    tess "Okay, close your eyes. No peeking, sidekick."
    t "I'm not peeking!"
    tess "Open them."
    t "A... BOX?"
    t "..."
    t "It's wiggling."
    t "TESSA. IT'S A SECOND PUPPY?! I have TWO dogs now!!"
    kid_sunny "Hehehe, PUPPY!"
    kid_fern "Aww, he's so tiny..."
    tess "Happy birthday, little guy."

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
    # TODO: EXPLORATION (optional) - Tessa walks to her own room (muted colors)
    # PLACEHOLDER: Tessa's real reason is still undecided
    tess "..."
    tess "I'm glad he had a good day."
    tess "That's the part that matters."
    tess "..."
    tess "Goodnight, little guy."

    return