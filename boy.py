from pico2d import*

class Boy:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    Attack1, Attack2, RUN, JUMP = 0, 1, 2, 3


    def handle_run(self):
        self.x += 5
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
    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                self.state = self.RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.xchange -= 5
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LCTRL):
            self.attackcount += 1
            if (self.attackcount % 2 == 0):
                self.state = self.Attack1
            else:
                self.state = self.Attack2

    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 6

        self.x = clamp(0, self.x, 800)

    def __init__(self):
        self.x, self.y = 100, 200
        self.frame = 0
        self.xchange, self.ychange = 0, 0
        self.attackcount = 0
        self.attackframe = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.state = self.RUN
        if Boy.image == None:
            Boy.image = load_image('Untitled-2.png')

    def draw(self):
        self.image.clip_draw(self.frame * 150, self.state * 150, 150, 150, self.x, self.y)

    def get_bb(self):
        return self.x - 50, self.x + 50