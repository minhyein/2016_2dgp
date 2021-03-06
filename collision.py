import game_framework
import end_state

from pico2d import*

from monster import Zombie
from monster import Lizard
from monster import Octopus
from boy import Boy
from background import Background
from heart import Heart

name = "collision"

zombies = None
lizards = None
octopuses = None
boy = None
background = None
hearts = None


def create_world():
    global boy, background, zombies, lizards, octopuses, hearts
    boy = Boy()
    background = Background(600, 600)
    hearts = [Heart() for i in range(5)]
    zombies = [Zombie() for i in range(4)]
    lizards = [Lizard() for i in range(4)]
    octopuses = [Octopus() for i in range(4)]




def destroy_world():
    global boy, background, zombies, lizards, octopuses, hearts
    del(boy)
    del(background)
    del(zombies)
    del(lizards)
    del(octopuses)
    del(hearts)



def enter():
    open_canvas(600, 600)
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                boy.handle_event(event)
                background.handle_event(event)



def collide(a, b):
    left_a, right_a = a.get_bb()
    left_b, right_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False

    return True

def pause():
    pass

def resume():
    pass

def update(frame_time):

    for i in range(0, len(hearts) - 1):
        hearts[i].x = hearts[i + 1].x - 40

    boy.update(frame_time)
    background.update(frame_time)

    for zombie in zombies:
        zombie.update(frame_time)
    for lizard in lizards:
        lizard.update(frame_time)
    for octopus in octopuses:
        octopus.update(frame_time)

    for zombie in zombies:
        if collide(boy, zombie):
            zombies.remove(zombie)
            for heart in hearts:
                hearts.remove(heart)

    for lizard in lizards:
        if collide(boy, lizard):
            lizards.remove(lizard)
    for octopus in octopuses:
        if collide(boy, octopus):
            octopuses.remove(octopus)



def draw(frame_time):
    clear_canvas()
    background.draw()
    boy.draw()
    for heart in hearts:
        heart.draw()
    for zombie in zombies:
        zombie.draw()
    for octopus in octopuses:
        octopus.draw()
    for lizard in lizards:
        lizard.draw()

    update_canvas()