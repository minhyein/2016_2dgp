from pico2d import *
import random

class Char:
    image = None

    Attack1, Attack2, RUN, JUMP = 0, 1, 2, 3


    def handle_run(self):
        self.x += self.xchange
        if self.x > 800:
            self.x = 800
        elif self.x < 0:
            self.x = 0

    def handle_jump(self):
        self.frame = 5
        self.ychange += 1
        if self.ychange < 10:
            self.y += 5
            self.state = self.JUMP
        elif self.ychange >= 10 and self.ychange < 20:
            self.y -= 5
            if self.y < 200:
                self.y = 200
            self.state = self.JUMP
        elif self.ychange == 20:
            self.ychange = 0
            self.state = self.RUN
    def handle_attack1(self):
        self.attackframe += 1
        if self.attackframe == 6:
            self.state = self.RUN
            self.attackframe = 0

    def handle_attack2(self):
        self.attackframe += 1
        if self.attackframe == 6:
            self.state = self.RUN
            self.attackframe = 0

    handle_state = {
        RUN: handle_run,
        JUMP: handle_jump,
        Attack1: handle_attack1,
        Attack2: handle_attack2
    }

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.handle_state[self.state](self)

    def __init__(self):
        self.x, self.y = 100, 200
        self.frame = 0
        self.xchange, self.ychange = 0, 0
        self.attackcount = 0
        self.attackframe = 0
        self.state = self.RUN
        if Char.image == None:
            Char.image = load_image('Untitled-2.png')

    def draw(self):
        self.image.clip_draw(self.frame * 150, self.state * 150, 150, 150, self.x, self.y)

class Background:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(400, 300)

class Zombie:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(500, 1400), 200
        self.frame = random.randint(0, 6)
        if Zombie.image == None:
            Zombie.image = load_image('Monster-zombie.png')

    def update(self):
        self.frame = (self.frame + 1) % 7
        self.x -= 2

    def draw(self):
        self.image.clip_draw(self.frame * 120, 0, 120, 120, self.x, self.y)

class Lizard:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(500, 1400), 200
        self.frame = random.randint(0, 5)
        if Lizard.image == None:
            Lizard.image = load_image('Monster-lizard.png')

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.x -= 2

    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 140, self.x, self.y)

class Octopus:
    image = None
    Attack, Run = 0, 1

    def __init__(self):
        self.x, self.y = random.randint(200, 1400), 200
        self.frame = random.randint(0, 5)
        self.runframe = 0
        self.attackframe = 0
        self.attackcount = random.randint(1, 10)
        self.state = self.Run
        if Octopus.image == None:
            Octopus.image = load_image('octopus.png')

    def handle_run(self):
        self.x -= 2
        self.runframe += 1
        if self.runframe % random.randint(30, 100) == 0:
            self.state = self.Attack
            self.attackframe = 0

    def handle_attack(self):
        self.attackframe += 1
        if self.attackframe == 12:
            self.state = self.Run
            self.runframe = 0

    handle_state = {
        Run: handle_run,
        Attack: handle_attack
    }

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.handle_state[self.state](self)

    def draw(self):
        self.image.clip_draw(self.frame * 150, self.state  * 150, 150, 150, self.x, self.y)

open_canvas()
boy = Char()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                boy.xchange += 5
            elif event.key == SDLK_LEFT:
                boy.xchange -= 5
            elif event.key == SDLK_SPACE:
               boy.state = boy.JUMP
            elif event.key == SDLK_LCTRL:
                boy.attackcount += 1
                if boy.attackcount % 2 == 0:
                    boy.state = boy.Attack1
                elif boy.attackcount % 2 == 1:
                    boy.state = boy.Attack2

        elif event.type == SDL_KEYUP:
            boy.xchange = 0

running = True
back = Background()
monsters = [Zombie() for i in range(4)]
lizards = [Lizard() for i in range (4)]
oct = [Octopus() for i in range(4)]

while running:
    handle_events()
    boy.update()
    for zombie in monsters:
        zombie.update()
    for lizard in lizards:
        lizard.update()
    for octopus in oct:
        octopus.update()

    clear_canvas()
    back.draw()
    boy.draw()
    for zombie in monsters:
        zombie.draw()
    for lizard in lizards:
        lizard.draw()
    for octopus in oct:
        octopus.draw()
    update_canvas()

    delay(0.05)

close_canvas()