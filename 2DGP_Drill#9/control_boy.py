from pico2d import *
from grass import Grass
from boy import Boy
import game_world

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)

def reset_world():
    global running
    global boy

    running = True

    # 배경 레이어에 첫 번째 잔디 추가 (y = 30)
    back_grass = Grass(y=30)
    game_world.add_object(back_grass, 0)

    # 전경 레이어에 소년 추가
    boy = Boy()
    game_world.add_object(boy, 1)

    # 전경 레이어에 두 번째 잔디 추가 (y = 40)
    front_grass = Grass(y=60)
    game_world.add_object(front_grass, 1)

def update_world():
    game_world.update()

def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()

open_canvas()
reset_world()

# 게임 루프
running = True
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

# 마무리 코드
close_canvas()
