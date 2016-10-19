from pico2d import *
import random

class Char:
    image = None

    RUN, JUMP = 0, 1


    def handle_run(self):
        self.x += self.xchange
        if self.x > 800:
            self.x = 800
        elif self.x < 0:
            self.x = 0

    def handle_jump(self):
        self.ychange += 1
        if self.ychange < 10:
            self.y += 5
            self.state = self.JUMP
        elif self.ychange >= 10 and self.ychange < 20:
            self.y -= 5
            self.state = self.JUMP
        elif self.ychange == 20:
            self.ychange = 0
            self.state = self.RUN

    handle_state = {
        RUN: handle_run,
        JUMP: handle_jump
    }

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.handle_state[self.state](self)

    def __init__(self):
        self.x, self.y = 100, 90
        self.frame = 0
        self.xchange, self.ychange = 0, 0
        self.state = self.RUN
        if Char.image == None:
            Char.image = load_image('run_animation.png')

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Zombie:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(500, 1400), 90
        self.frame = random.randint(0, 6)
        if Zombie.image == None:
            Zombie.image = load_image('Monster-zombie.png')

    def update(self):
        self.frame = (self.frame + 1) % 7
        self.x -= 2

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Lizard:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(500, 1400), 90
        self.frame = random.randint(0, 5)
        if Lizard.image == None:
            Lizard.image = load_image('Monster-lizard.png')

    def update(self):
        self.frame = (self.frame + 1) % 6
        self.x -= 2

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


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
                boy.state = boy.Attack1

        elif event.type == SDL_KEYUP:
            boy.xchange = 0


grass = Grass()
running = True
monsters = [Zombie() for i in range(4)]
lizards = [Lizard() for i in range (4)]

while running:
    handle_events()
    boy.update()
    for zombie in monsters:
        zombie.update()
    for lizard in lizards:
        lizard.update()

    clear_canvas()
    grass.draw()
    boy.draw()
    for zombie in monsters:
        zombie.draw()
    for lizard in lizards:
        lizard.draw()
    update_canvas()

    delay(0.05)

close_canvas()