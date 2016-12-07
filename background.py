from pico2d import*

class Background:
    PIXEL_PER_METER = (10.0 / 0.3)
    SCROLL_SPEED_KMPH = 20.0
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, w, h):
        self.image = load_image('background.png') #1067x600
        self.speed = 100
        self.left = 0
        self.screen_width = w
        self.screen_height = h
        self.high = 0

    def draw(self):
        x = int(self.left)
        w = min(self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width - w, self.screen_height, w, 0)


    def update(self, frame_time):
        self.left = (self.left + frame_time * self.speed) % self.image.w


    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                self.speed -= Background.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT:
                self.speed += Background.SCROLL_SPEED_PPS
            elif event.key == SDLK_UP:
                self.speed -= Background.SCROLL_SPEED_PPS
        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                self.speed += Background.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT:
                self.speed -= Background.SCROLL_SPEED_PPS


class TileBackground:

    SCROLL_SPEED_PPS = 1

    def __init__(self, width, height):
        self.tile_map = load_tile_map('field.json')
        self.speed = 0
        self.left = 0
        self.width = width
        self.height = height

    def draw(self):
        pass

    def update(self, frame_time):
        pass

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT: self.speed -= TileBackground.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT: self.speed += TileBackground.SCROLL_SPEED_PPS
        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT: self.speed += TileBackground.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT: self.speed -= TileBackground.SCROLL_SPEED_PPS




