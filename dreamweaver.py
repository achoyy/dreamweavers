import pygame as py
import sys
from pygame.locals import QUIT
import random 
import time 

# initialize 
py.init()

# display setup 
# screen_info = py.display.Info() 
# WIDTH = screen_info.current_w  
# HEIGHT = screen_info.current_h 
WIDTH = 1280 
HEIGHT = 720 
FPS = 60
Running = True
s = py.display.set_mode((WIDTH, HEIGHT))
font = py.font.Font("Nexa-Heavy.ttf", 40)
clock = py.time.Clock()

# import graphics
dia = py.image.load("intro-1.png")
char = py.image.load("char.png")
rchar = char 
lchar = py.transform.flip(char, True, False)
intro1 = py.image.load("intro-1.png")
intro1 = py.transform.scale(intro1, (WIDTH, HEIGHT)) 
intro2 = py.image.load("intro-2.png")
intro2 = py.transform.scale(intro2, (WIDTH, HEIGHT)) 
s1a = py.image.load("scene1a.png")
s1a = py.transform.scale(s1a, (WIDTH, HEIGHT)) 
s1b = py.image.load("scene1b.png") 
s1b = py.transform.scale(s1b, (WIDTH, HEIGHT)) 
s2a = py.image.load("scene2a.png")
s2a = py.transform.scale(s2a, (WIDTH, HEIGHT)) 
s2b = py.image.load("scene2b.png")
s2b = py.transform.scale(s2b, (WIDTH, HEIGHT)) 
s3 = py.image.load("scene3.png")
s3 = py.transform.scale(s3, (WIDTH, HEIGHT)) 

f1 = py.image.load("f1.png")
f1 = py.transform.scale(f1, (WIDTH, HEIGHT)) 
f2 = py.image.load("f2.png")
f2 = py.transform.scale(f2, (WIDTH, HEIGHT)) 
f3 = py.image.load("f3.png")
f3 = py.transform.scale(f3, (WIDTH, HEIGHT)) 
f4 = py.image.load("f4.png")
f4 = py.transform.scale(f4, (WIDTH, HEIGHT)) 
f5 = py.image.load("f5.png")
f5 = py.transform.scale(f5, (WIDTH, HEIGHT)) 
f6 = py.image.load("f6.png")
f6 = py.transform.scale(f6, (WIDTH, HEIGHT)) 
f7 = py.image.load("f7.png")
f7 = py.transform.scale(f7, (WIDTH, HEIGHT)) 

blink = [f1, f2, f3, f4, f5, f6, f7, f7, f7, f6, f5, f4, f3, f2, f1]
current_blink = 0 
blinking = False
blinkCounter = 0 

introduction = py.image.load("intro.png") 
introduction = py.transform.scale(introduction, (WIDTH, HEIGHT)) 
ending = py.image.load("ending.png")
ending = py.transform.scale(ending, (WIDTH, HEIGHT)) 


currentbg = intro1 
STEP = 4

# dialogue typerwriter stuff 
intromessages = ["press space to continue.", 
            ".....", 
            "everyone has dreams once in a while", 
            "i'm a ghost! i live in those dreams!", 
            "most of the time, i try to get rid of bad things in their dreams.", 
            "sometimes... it doesn't go so well."] 
intropeople = ["  ...", 
               "  ...", 
               "ghost", 
               "ghost", 
               "ghost", 
               "ghost"]
scene1messagesA = ["annie! come downstairs!", 
                   "yeah okay! i'm coming!", 
                   "have breakfast", 
                   "thanks, mom", 
                   "you didn't do the dishes last night, did you?", 
                   "huh? sorry, I forgot", 
                   "you need to be more responsible, annie...", 
                   "i don't think annie will like this dream very much...", 
                   "let's change it!", 
                   "let's go wash the dishes for her!", 
                   "heres a tip! use wasd to move...", 
                   "then use x to interact with objects!"]
scene1peopleA = ["  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "  mom", 
                 "ghost", 
                 "ghost", 
                 "ghost", 
                 "ghost", 
                 "ghost"]
scene1messagesB = ["annie! come downstairs!", 
                   "yeah okay! i'm coming!", 
                   "have breakfast.", 
                   "thanks, mom", 
                   "have a nice day at school!", 
                   "yep! i'll see you after school."]
scene1peopleB = ["  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "  mom", 
                 "annie"]
scene2messagesA = ["annie! can you cut the carrots?", 
                   "yeah, sure!", 
                   "how should i cut them?", 
                   "just into sticks, thanks!", 
                   "ah!", 
                   "annie?", 
                   "i think i cut my finger...", 
                   "is it bleeding?", 
                   "yeah, i'll just go get a band-aid", 
                   "you should be more careful, annie.", 
                   "yeah yeah, I know.", 
                   "i'm just worried about you", 
                   "....", 
                   "i know.", 
                   "okay so... annie didn't like that just now, i guess.", 
                   "lets put some instructions next to the chopping board", 
                   "maybe it'll help her be careful?"]
scene2peopleA = ["  mom", 
                 "annie", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "annie", 
                 "ghost", 
                 "ghost", 
                 "ghost"]
scene2messagesB = ["annie! can you cut the carrots?", 
                   "yeah, sure!", 
                   "how should I cut them?", 
                   "check the recipe book! it's out on the counter.", 
                   "alright!", 
                   "hold the carrot like... hands like... and then...", 
                   "all done! anyting else I can do for you?", 
                   "nope! just give those to me, annie."]
scene2peopleB = ["  mom", 
                 "annie", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "annie", 
                 "annie", 
                 "  mom"]
scene3messagesA = ["annie! come downstairs!", 
                   "yeah okay! i'm coming!", 
                   "have breakfast.", 
                   "thanks mom.", 
                   "annie, can I ask you something?", 
                   "what's up?", 
                   "you know that I won't be here forever, right?", 
                   "you'll be here for a while, at least...", 
                   "annie. you need to let me go", 
                   "...", 
                   "i've stayed with you for too long.", 
                   "....what?", 
                   "i need to go.", 
                   "...rewind. this wasn't supposed to happen.", 
                   "she can do that?", 
                   "this is my dream afterall..."]
scene3peopleA = ["  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "ghost", 
                 "annie"]
scene3messagesB = ["annie! come downstairs!", 
                   "yeah okay! i'm coming!", 
                   "have breakfast.", 
                   "thanks mom. i'm going to head to school early today.", 
                   "ah- can I talk to you?", 
                   "can it wait?", 
                   "....", 
                   "i guess", 
                   "mom. you can't leave this dream.", 
                   "i don't know what i'd do if you did"]
scene3peopleB = ["  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "  mom", 
                 "annie", 
                 "  mom", 
                 "  mom", 
                 "annie", 
                 "annie"]

active_message = 0
active_talker = 0
messages = intromessages
talkers = intropeople 
message = messages[active_message] 
talker = talkers[active_talker]
snip = font.render('', True, "white") 
counter = 0
speed = 1
done = False
cx = WIDTH / 2
cy = HEIGHT / 2

Running = True 

phase = 10 

def DIALOGUE(dia, bg, counter, speed, message, done): 
    s.blit(bg, (0, 0)) 
    s.blit(dia, (0, 4*HEIGHT/5)) 

    if counter < speed * len(message): 
        counter += 1 
    elif counter >= speed * len(message): 
        done = True

    return counter, done

def BLINK(blink, current_blink, blinkCounter, done): 
    while done == False: 
        s.blit(blink[current_blink], (0, 0)) 
        blinkCounter += 1
        if current_blink == len(blink) - 1 and blinkCounter >= 4: 
            done = True 
            current_blink = 0
            blinkCounter = 0
        if blinkCounter >= 4: 
            current_blink += 1 
            blinkCounter = 0
        py.display.flip()
    return current_blink, blinkCounter, done

def RESET(phase, nextSet, nextbg, nextPeople): 
    phase += 1 
    messages = nextSet 
    active_message = 0 
    active_talker = 0
    message = messages[active_message]
    talker = nextPeople[active_talker]
    counter = 0 
    done = 0
    return phase, messages, nextbg, active_message, active_talker, message, talker, counter, done, nextPeople

while Running: 

    clock.tick(FPS)

    for event in py.event.get(): 
        if event.type == py.QUIT: 
            Running = False 
        elif event.type == py.KEYDOWN: 
            if event.key == py.K_ESCAPE: 
                Running = False
            elif event.key == py.K_SPACE and phase == 10: 
                phase = 1
            elif event.key == py.K_SPACE and done: 
                if active_message < len(messages) -1: 
                    active_talker += 1
                    active_message += 1
                    done = False 
                    talker = talkers[active_talker]
                    message = messages[active_message]
                    counter = 0
                    if active_message == 3 and phase == 1: 
                        currentbg = intro2
                elif active_message == len(messages) -1: 
                    if phase == 1: 
                        BLINK(blink, current_blink, blinkCounter, blinking)
                        phase, messages, currentbg, active_message, active_talker, message, talker, counter, done, talkers = RESET(phase, scene1messagesA, s1a, scene1peopleA)
                    elif phase == 2: 
                        phase += 1 
                    elif phase == 4: 
                        BLINK(blink, current_blink, blinkCounter, blinking)
                        phase, messages, currentbg, active_message, active_talker, message, talker, counter, done, talkers = RESET(phase, scene2messagesA, s2a, scene2peopleA)
                    elif phase == 5: 
                        phase += 1
                    elif phase == 7: 
                        BLINK(blink, current_blink, blinkCounter, blinking)
                        phase, messages, currentbg, active_message, active_talker, message, talker, counter, done, talkers = RESET(phase, scene3messagesA, s3, scene3peopleA)
                    elif phase == 8: 
                        BLINK(blink, current_blink, blinkCounter, blinking)
                        phase, messages, currentbg, active_message, active_talker, message, talker, counter, done, talkers = RESET(phase, scene3messagesB, s3, scene3peopleB)
                    elif phase == 9: 
                        phase = 11
                        BLINK(blink, current_blink, blinkCounter, blinking)
            elif event.key == py.K_x: 
                if phase == 3 and (cy > 112) and (cy < 228) and (cx > 120) and (cx < 344): 
                    BLINK(blink, current_blink, blinkCounter, blinking)
                    phase, messages, currentbg, active_message, active_talker, message, talker, counter, done, talkers = RESET(phase, scene1messagesB, s1b, scene1peopleB)
                elif phase == 6 and (cy > 100) and (cy < 228) and (cx > 320) and (cx < 452): 
                    BLINK(blink, current_blink, blinkCounter, blinking)
                    phase, messages, currentbg, active_message, active_talker, message, talker, counter, done, talkers = RESET(phase, scene2messagesB, s2b, scene2peopleB)


    keys = py.key.get_pressed() 
    if keys[py.K_w] and (cy - STEP) > 0:
        cy -= STEP
    if keys[py.K_a] and (cx - STEP) > 0: 
        cx -= STEP
        char = lchar
    if keys[py.K_s] and (cy + STEP + 143) < HEIGHT: 
        cy += STEP
    if keys[py.K_d] and (cx + STEP + 129) < WIDTH: 
        cx += STEP
        char = rchar

    if phase == 10: 
        s.blit(introduction, (0, 0))
    elif phase == 11: 
        s.blit(ending, (0, 0))
    elif phase == 3: 
        s.blit(s1a, (0, 0))
        s.blit(char, (cx, cy))
    elif phase == 6: 
        s.blit(s2a, (0, 0))
        s.blit(char, (cx, cy))
    else: 
        counter, done = DIALOGUE(dia, currentbg, counter, speed, message, done)
        snip = font.render(message[0:counter//speed], True, 'white') 
        person = font.render(talker, True, 'white')
        s.blit(snip, (50, 4*HEIGHT/5 + 10))
        s.blit(person, (WIDTH-200, HEIGHT-70))


    py.display.flip() 

py.quit() 
sys.exit() 
