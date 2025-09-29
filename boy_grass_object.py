from pico2d import *
import random


# Game object class here
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()
# game loop

reset_world()
while 1:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code
close_canvas()
