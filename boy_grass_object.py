from pico2d import *
import random
class Grass:
    # 생성자 함수 , 초기화 수행
    def __init__(self): #== 생성자 == 객체 생성, 속성 알려주는 것
        self.image = load_image('grass.png') #== 객체 속성
        #== grass 객체의 속성을 정의하고 초기화 하는 것
    pass # pass == 아무것도 없을 때 쓰는 것

    def draw(self):
        self.image.draw(400,30)
        pass


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

def reset_world():
    global running 
    global grass
    
    running = True
    grass = Grass() # 클래스 생성 이름은 대문자로 하는 것이 좋음
    pass

def update_world():
    pass

def render_world():
    # 월드에 객체(= grass)들을 그린다
    clear_canvas()
    grass.draw()
    update_canvas()
    pass


reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code
close_canvas()
