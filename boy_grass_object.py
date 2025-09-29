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
class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x=400
        self.frame =0
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,90)
    def update(self):#소년을 오른쪽으로 이동시키는 상호작용
        self.x+=5
        self.frame=(self.frame+1)%8
        pass

def reset_world():
    global running 
    global grass
    global boy
    
    running = True
    grass = Grass() # 클래스 생성 이름은 대문자로 하는 것이 좋음

    boy = Boy()
    pass
# 게임 로직
def update_world():
    boy.update()# 소년의 상호작용을 시뮬레이션 계산
    pass

def render_world():
    # 월드에 객체(= grass)들을 그린다
    clear_canvas()
    grass.draw()
    boy.draw()
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
