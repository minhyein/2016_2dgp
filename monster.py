import random
from pico2d import*

class Zombie:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(500, 1400), 200
        self.frame = random.randint(0, 6)
        self.speed = 2
        if Zombie.image == None:
            Zombie.image = load_image('Monster-zombie.png')


    def update(self, frame_time):
        self.frame = (self.frame + 1) % 7
        self.x -= self.speed

    def draw(self):
        self.image.clip_draw(self.frame * 120, 0, 120, 120, self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.x + 10

class Lizard:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(500, 1400), 200
        self.frame = random.randint(0, 5)
        if Lizard.image == None:
            Lizard.image = load_image('Monster-lizard.png')

    def update(self, frame_time):
        self.frame = (self.frame + 1) % 6
        self.x -= 2

    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 140, self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.x + 10

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

    def update(self, frame_time):
        self.frame = (self.frame + 1) % 6
        self.handle_state[self.state](self)

    def draw(self):
        self.image.clip_draw(self.frame * 150, self.state  * 150, 150, 150, self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.x + 10