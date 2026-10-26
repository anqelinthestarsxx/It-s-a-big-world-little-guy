default theo_x = 960.0
default theo_y = 800.0
default target_x = 960.0
default target_y=800.0
default theo_facing = 1.0
default theo_moving = False
default explore_time = 0.0
default explore_limit = 90.0
default bedroom_done = False
default room_left = 320
default room_right = 1600
image bg_outside=Solid("#cfe8ff")
default snow_played = []
image bg_snowyard = Solid('#e8f2ff')
default lunch_played = []
default recess_played = []
image bg_lunch = Solid("#f5e6c8")
image bg_classroom = Solid("#e8e0f5")
default find_answer = 0
default zone_center = 0.5

define BEDROOM_SPOTS = [
    ("window", 700, 330, "obj_placeholder", "look_window"),
    ("dresser", 1240, 560, "obj_dresser", "look_dresser"),
    ("bed", 480, 700, "obj_placeholder", "look_bed"),
    ("dogbed", 900, 900, "obj_placeholder", "look_dogbed"),
    ("toybox", 1400, 900, "obj_placeholder", "look_toybox"),
    ("nightlight", 1100, 480, "obj_placeholder", "look_nightlight"),
    ("photo", 1450, 340, "obj_placeholder", "look_photo"),
]

define OUTSIDE_SPOTS = [
    ("snowman", 500, 800, "obj_placeholder", "look_snowman"),
    ("bird", 1000, 600, "obj_placeholder", "look_bird"),
    ("puddle", 1400, 900, "obj_placeholder", "look_puddle"),
    ("bus", 1800, 800, "obj_placeholder", "look_bus"),
    ("school", 300, 600, "obj_placeholder", "look_school"),
    ("tessa", 960, 950, "obj_placeholder", "look_tessa"),
]

define SNOW_SPOTS = [
    ("snowangel", 400, 700, "obj_placeholder", "snow_angel"),
    ("snowball", 800, 620, "obj_ placeholder", "snow_ball"),
    ("fort", 1250, 700, "obj_placeholder", "snow_fort"),
    ("snowdraw", 1600, 900, "obj_placeholder", "snow_draw"),
    ("sled", 300, 950, "obj_placeholder", "snow_sled"),
    ("husky", 960, 980, "obj_placeholder", "snow_husky"),
    ("rockhunt", 1650, 650, "obj_placeholder", "snow_rocks"),
]

define GETTING_READY = BEDROOM_SPOTS + [
    ("drawing", 1000, 340, "obj_placeholder", "look_drawing"),
]

define LUNCH_SPOTS = [
    ("cupcake", 960, 700, "obj_placeholder", "lunch_cupcake"),
    ("lunchbox", 500, 800, "obj_placeholder", "lunch_box"),
    ("oliver", 1400, 800, "obj_placeholder", "lunch_oliver"),
    ("milk", 700, 650, "obj_placeholder", "lunch_milk"),
    ("rock", 1650, 700, "obj_placeholder", "lunch_rock"),
    ("ruby", 300, 650, "obj_placeholder", "lunch_ruby"),
]

define RECESS_SPOTS = [
    ("blocks", 500, 800, "obj_placeholder", "recess_blocks"),
    ("fort", 1000, 750, "obj_placeholder", "recess_fort"),
    ("mountain", 1450, 850, "obj_placeholder", "recess_mountain"),
    ("cave", 1700, 700, "obj_placeholder", "recess_cave"),
    ("coloring", 300, 650, "obj_placeholder", "recess_coloring"),
    ("window", 900, 450, "obj_placeholder", "recess_window"),
]

define GETREADY_SPOTS = [s for s in BEDROOM_SPOTS if s[0] != "dogbed"] + [
    ("husky", 850, 950, "obj_placeholder", "look_husky_play"),
    ("drawing", 1000, 340, "obj_placeholder", "look_drawing"),
]

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
        x = clamp(x, store.room_left + 48, store.room_right - 48)
        y = clamp(y, FLOOR_TOP, FLOOR_BOTTOM)
        if x < store.theo_x - 10:
            store.theo_facing = -1.0
        elif x > store.theo_x + 10:
            store.theo_facing = 1.0
        store.target_x = float(x)
        store.target_y = float(y)
        store.theo_moving = True
       

    def update_theo():
        store.explore_time += 0.02
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

screen explore_scene(bg, spots):
    add Solid("#000000")
    add bg:
        xalign 0.5

    button:
        xysize (config.screen_width, config.screen_height)
        background None
        action Function(set_target)

    for (name, x, y, img, lbl) in spots:
        imagebutton:
            idle img
            pos (x, y)
            anchor (0.5, 1.0)
            focus_mask True
            action Return(lbl)

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

    if explore_time >= explore_limit:
        timer 0.01 action Return("done")

screen tap_game(prompt, goal):
    default taps = 0

    add Solid("#00000099")

    frame:
        align (0.5, 0.5)
        padding (50, 40)
        vbox:
            spacing 25
            text prompt size 40 xalign 0.5
            bar:
                value ScreenVariableValue("taps", goal)
                xsize 600
                ysize 30
                xalign 0.5
            textbutton "TAP!":
                xalign 0.5
                text_size 60
                action [SetScreenVariable("taps", taps + 1), If(taps +1 >= goal, Return(True))]

label play_tap(prompt, goal=10):
    call screen tap_game(prompt, goal)
    return

screen timing_game(prompt, lo, hi, speed):
    default t_el = 0.0
    $ marker = abs(((t_el * speed) % 2.0) - 1.0)

    add Solid("#00000099")
    frame:
        align (0.5, 0.5)
        padding (50, 40)
        vbox:
            spacing 25
            text prompt size 40 xalign 0.5
            fixed:
                xsize 700
                ysize 40
                xalign 0.5
                add Solid("#888888") xsize 700 ysize 40
                add Solid("#5cb85c") xpos int(700 * lo) xsize int(700 * (hi - lo)) ysize 40
                add Solid("#ffffff") xpos int(700 * marker) xsize 10 ysize 40
            textbutton "NOW!":
                xalign 0.5
                text_size 60
                action If(lo <= marker <= hi, Return(True), Notify("Almost! Try again!"))

    timer 0.02 repeat True action SetScreenVariable("t_el", t_el + 0.02)

screen find_game(prompt, n, answer):
    add Solid("#00000099")
    text prompt size 40 align (0.5, 0.15)
    for i in range(n):
        imagebutton:
            idle "obj_placeholder"
            pos (300 + i * 250, 600)
            anchor (0.5, 0.5)
            action If(i == answer, Return(True), Notify("Not here!"))

screen catch_game(prompt, goal):
    default hits = 0
    default tx = 960
    default ty = 600

    add Solid("#00000099")
    text prompt size 40 align (0.5, 0.1)
    text "[hits] / [goal]" size 40 align (0.5, 0.18)

    imagebutton:
        idle "obj_placeholder"
        pos (tx, ty)
        anchor (0.5, 0.5)
        action [SetScreenVariable("hits", hits + 1),
                SetScreenVariable("tx", renpy.random.randint(300, 1500)),
                SetScreenVariable("ty", renpy.random.randint(350, 850)),
                If(hits + 1 >= goal, Return(True))]

    timer 1.2 repeat True action [SetScreenVariable("tx", renpy.random.randint(300, 1500)),
                                                SetScreenVariable("ty", renpy.random.randint(350, 850))]

label play_timing(prompt, zone=0.2, speed=0.6):
    $ zone_center = renpy.random.uniform(0.25, 0.75)
    call screen timing_game(prompt, zone_center - zone / 2.0, zone_center + zone / 2.0, speed)
    return

label play_find(prompt, n=5):
    $ find_answer = renpy.random.randint(0, n-1)
    call screen find_game(prompt, n, find_answer)
    return

label play_catch(prompt, goal=5):
    call screen catch_game(prompt, goal)
    return


label explore_outside:
    $ explore_time = 0.0
    $ explore_limit = 15.0
    $ room_left = 0
    $ room_right = 1920
    $ theo_x = 960
    $ theo_y = 800

label explore_outside_loop:
    call screen explore_scene("bg_outside", OUTSIDE_SPOTS)

    if _return == "done":
        return

    call expression _return
    jump explore_outside_loop

label start:

    #===== ACT I: Waking Up! =====
    scene black
    tess "Wake up, birthday boy! It's your big day!"
    t "Tessa! I'm FOUR!!"
    tess "You sure are, kid! Go get ready for your big day, i'm making you a surprise~"

    $ explore_time = 0.0
    $ explore_limit = 9999.0
    $ bedroom_done = False
    $ room_left = 320
    $ room_right = 1600
    $ theo_x = 960.0
    $ theo_y = 800.0
    $ target_x = 960.0
    $ target_y = 800.0

label bedroom_loop:
    call screen explore_scene("theo-room", BEDROOM_SPOTS)
    call expression _return
    if not bedroom_done:
        jump bedroom_loop

    scene black with fade
    # $theo_outfit = "school"
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
    call explore_outside
    scene black with fade
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
    teacher "Go on, everyone. Eat up and have fun!"
    call explore_lunch
    scene black with fade
    jump naptime

label explore_lunch:
    $ explore_time = 0.0
    $ explore_limit = 120.0
    $ room_left = 0
    $ room_right = 1920
    $ theo_x = 960.0
    $ theo_y = 800.0
    $ lunch_played = []

label explore_lunch_loop:
    call screen explore_scene("bg, lunch", LUNCH_SPOTS)
    if _return == "done":
        return
    call expression _return
    if len(set(lunch_played)) >= len(LUNCH_SPOTS):
        return
    jump explore_lunch_loop

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
    call explore_recess
    scene black with fade
    jump pickup

label explore_recess:
    $ explore_time = 0.0
    $ explore_limit = 120.0
    $ room_left = 0
    $ room_right = 1920
    $ theo_x = 960.0
    $ theo_y = 800.0
    $ target_x = 960.0
    $ target_y = 800.0
    $ recess_played = []

label explore_recess_loop:
    call screen explore_scene("bg_classroom", RECESS_SPOTS)
    if _return == "done":
        return
    call expression _return
    if len(set(recess_played)) >= len(RECESS_SPOTS):
        return
    jump explore_recess_loop

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
    call explore_getready
    scene black with fade
    # $ theo_outfit = "party"

    t "Tessa, look! I'm the birthday boy! It says so!"
    t "[husky_name]! look! Do I look fancy?"
    tess "You look perfect."
    t "Are you coming too?"
    tess "Always. Okay, close your eyes, I'll lead you downstairs."
    t "Why?"
    tess "No questions, buddy,"
    jump party

label explore_getready:
    $ explore_time = 0.0
    $ explore_limit = 9999.0
    $ bedroom_done = False
    $ room_left = 320
    $ room_right = 1600
    $ theo_x = 960.0
    $ theo_y = 800.0
    $ target_x = 960.0
    $ target_y = 800.0

label explore_getready_loop:
    call screen explore_scene("theo-room", GETREADY_SPOTS)
    call expression _return
    if not bedroom_done:
        jump explore_getready_loop
    return

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

    t "Can we go play in the SNOW?!"
    tess "Go on. Everybody's waiting."
    call explore_snow
    scene black with fade

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
    return

#Exploration labels

label explore_snow:
    $ explore_time = 0.0
    $ explore_limit = 120.0
    $ room_left = 0
    $ room_right = 1920
    $ theo_x = 960.0
    $ theo_y = 800.0
    $ target_x = 960.0
    $ target_y = 800.0
    $ snow_played = []

label explore_snow_loop:
    call screen explore_scene("bg_snowyard", SNOW_SPOTS)

    if _return == "done":
        return

    call expression _return

    if len(set(snow_played)) >= len(SNOW_SPOTS):
        return
    jump explore_snow_loop

label look_snowman:
    t "A snowman!! He's got a carrot nose!!"
    t "He's HUGE. He's even bigger than tessa!"
    return

label look_bird:
    t "Hi, birdie! Are you going to school too?"
    t "... He's not saying anything."
    return

label look_puddle:
    t "A puddle! It's frozen!"
    t "Tessa says don't stomp on it. I'm not gonna stop."
    t "... Just a little stomp.."
    return

label look_bus:
    t "That bus is SO big. How do the wheels get that big?"
    t "The world is BIG."
    return

label look_school:
    t "That's my school. It's one of the biggest buildings I've ever seen!"
    t "I'm gonna learn everything in there."
    return

label look_tessa:
    t "Tessa's looking at her phone.."
    t "...She looks tired. She's probably just thinking about breakfast."
    return

label look_dresser:
    menu: 
        "Get Dressed":
            $ bedroom_done = True
        "Keep exploring":
            pass
    return

label look_window:
    t "It's SNOWING!"
    t "Everything's white. The whole world is like sugar!"
    t "Maybe there'll be a snow day. Please, please, please.."
    return

label look_bed:
    t "My bed! It's still warm."
    t "Bunny's still sleeping. Shh.."
    t "Tessa says I'm not allowed to jump on it..."
    t "... Just one jump."
    return

label look_dogbed:
    t "[husky_name]'s bed is empty."
    t "He never misses my birthday!"
    t "Tessa says he's busy. Dogs aren't busy."
    return

label look_toybox:
    t "My toy box! It has trucks and blocks and a dinosaur."
    t "The dinosaur only has one eye. He's the boss of everybody."
    return

label look_nightlight:
    t "My moon nightlight!"
    t "Tessa leaves the hall light on for me, too."
    t "So the dark isn't scary."
    return

label look_photo:
    t "That's me and Tessa!"
    t "She's holding me up like a trophy."
    t "I was SO tiny. Now I'm four!"
    return

label snow_angel:
    kid_fern "Theo, lie down! Like this! Then move your arms!"
    t "I'm making wings!"
    call minigame_snow_angel
    $ snow_played.append("snowangel")
    kid_fern "That's the best angel I've ever seen."
    return

label snow_ball:
    kid_ruby "I'm the best at snowballs. Bet you can't hit the tree!"
    t "Watch me!"
    call minigame_snowball
    $ snow_played.append("snowball")
    kid_ruby "...Okay. That was a good one."
    return

label snow_fort:
    kid_blue "Theo! Help me build the for! IT needs a door!"
    t "And a tower! And a flag!"
    call minigame_fort
    $ snow_played.append("fort")
    kid_blue "Best fort ever."
    return

label snow_draw:
    kid_iris "... I'm drawing in the snow with a stick."
    t "Is that [husky_name]?"
    kid_iris "... Yes."
    call minigame_snow_draw
    $ snow_played.append("snowdraw")
    return

label snow_sled:
    kid_sunny "Hehehe, the hill is SO slippery!"
    t "Can I go next?"
    call minigame_sled
    $ snow_played.append("sled")
    kid_sunny "Hehehehe, again, again!"
    return

label snow_husky:
    t "[husky_name]! He's covered in snow!"
    t "He looks like a snowman with ears."
    call minigame_husky_fetch
    $ snow_played.append("husky")
    t "Good boy, [husky_name]!"
    return

label snow_rocks:
    kid_max "I'm looking for rocks. Under the snow."
    t "Did you find one?"
    kid_max "...Not yet."
    call minigame_rocks
    $ snow_played.append("rockhunt")
    kid_max "Found one. It's cold."
    return

label minigame_snow_angel:
    call play_tap("Wave your arms to make the wings!", 12)
    return

label minigame_snowball:
    call play_timing("Throw when the marker is in the green!", 0.18, 0.9)
    return

label minigame_fort:
    call play_tap("Pack the snow to build the fort!", 14)
    return

label minigame_snow_draw:
    call play_tap("Draw in the snow with the stick!", 8)
    return

label minigame_sled:
    call play_catch("Grab the sled as it slides past!", 4)
    return

label minigame_husky_fetch:
    call play_catch("Grab the sled as it slides past!", 4)
    return

label minigame_rocks:
    call play_find("Which snowdrift has Max's rock?", 5)
    return

label look_drawing:
    t "Iris's drawing! I put it on my wall!"
    t "That's me. That's tessa. She's got a cape!"
    t "...She really is a superhero."
    return

label lunch_cupcake:
    t "My cupcakeI It's got sprinkles AND a candle!"
    kid_penny "You have to wait to blow it out. It's a rule."
    t "I'm waiting. I'm REALLY waiting."
    call minigame_cupcake
    $ lunch_played.append("cupcake")
    kid_penny "Okay. Now you can."
    return

label lunch_box:
    t "Bunny's in my bag, but Tessa packed me snacks too!"
    kid_blue "Wanna trade? I have crackers."
    t "I have... a mysery sandwich."
    call minigame_trade_snacks
    $ lunch_played.append("lunchbox")
    kid_blue "That was a good trade."
    return

label lunch_oliver:
    kid_oliver "Is there pizza under the table?"
    t "Oliver, that's the floor."
    kid_oliver "...Pizza could be the floor."
    call minigame_pizza_hunt
    $ lunch_played.append("oliver")
    kid_oliver "...No pizza. But I found a crayon."
    return

label lunch_milk:
    kid_sunny "Hehehe, watch me pour my own milk!"
    t "Don't spill it!"
    call minigame_milk
    $ lunch_played.append("milk")
    kid_sunny "Hehehe, I spilled it a little."
    return

label lunch_rock:
    kid_max "This is my rock. He's eating lunch too."
    t "What does he eat?"
    kid_max "...Rocks."
    $ lunch_played.append("rock")
    return

label lunch_ruby:
    kid_ruby "I'm the like leader, so I get the first napkin."
    t "That's not a rule."
    kid_ruby "It's MY rule."
    $ lunch_played.append("ruby")
    return

label recess_blocks:
    kid_ruby "I'm in charge of the blocks! Hand me a red one."
    t "I'm building a tower for Tessa!"
    call minigame_blocks
    $ recess_played.append("blocks")
    kid_ruby "That's almost as tall as me."
    return

label recess_fort:
    kid_blue "Theo! Help me with the pillow fort!"
    t "It need a door! And a flag!"
    call minigame_pillow_fort
    $ recess_played.append("fort")
    kid_blue "Best fort ever."
    return

label recess_mountain:
    t "This pillow is a mountain! I'm gonna climb it!"
    call minigame_mountain
    $ recess_played.append("mountain")
    t "I'm the king of the mountain!"
    return

label recess_cave:
    kid_sunny "Hehehe, come in the cave!"
    t "It's dark in here!"
    kid_sunny "Hehehehe, that's the table."
    call minigame_cave
    $ recess_played.append("cave")
    return

label recess_coloring: 
    kid_iris "...Want to color with me?"
    t "Can I make tessa a card?"
    kid_iris "...Yes."
    call minigame_coloring
    $ recess_played.append("coloring")
    kid_iris "...It's a good card."
    return

label recess_window:
    kid_fern "It's still snowing."
    t "It's like the sky is a snow globe!"
    kid_fern "...I wish we could go out."
    $ recess_played.append("window")
    return

label look_husky_play:
    t "[husky_name]! Come here!"
    t "Do you want to see my fancy birthday outfit?"
    call minigame_husky_play
    t "He says I look fancy."
    return

label minigame_cupcake:
    call play_timing("Blow out the candle when the marker hits green!", 0.25, 0.5)
    return

label minigame_trade_snacks:
    call play_tap("Pass the snacks back and forth!", 6)
    return

label minigame_pizza_hunt:
    call play_find("Which spot has the pizza?", 5)
    return

label minigame_milk:
    call play_timing("Stop pouring at just the right moment!", 0.2, 0.7)
    return

label minigame_blocks:
    call play_timing("Place the block when it lines up!", 0.2, 0.8)
    return

label minigame_pillow_fort:
    call play_tap("Stack the pillows for the fort", 12)
    return

label minigame_mountain:
    call play_tap("Climb the pillow mountain!", 12)
    return

label minigame_cave:
    call play_find("Which way out of the cave?", 4)
    return

label minigame_coloring:
    call play_tap("Color in the card for Tessa!", 10)
    return

label minigame_husky_play:
    call play_catch("Pet [husky_name] when he zooms by!", 5)
    return