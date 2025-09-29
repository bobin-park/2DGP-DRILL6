#객체 지향 방식으로 구현한 코드
#-> 개발에 효율적인
#--> 왜? : 새로운 기능 추가 GOOD
from pico2d import *
import random
class Grass:
    # 생성자 함수 , 초기화 수행
    def __init__(self): #== 생성자 == 객체 생성, 속성 알려주는 것
        self.image = load_image('grass.png') #== 객체 속성
        #== grass 객체의 속성을 정의하고 초기화 하는 것

    def draw(self):
        self.image.draw(400,30)
    def update(self):
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
class Zombie:
    def __init__(self):
        self.x,self.y = 100,170
        self.frame =0
        self.image= load_image('zombie_run_animation.png')
    def update(self):
        self.fream = (self.frame+1)%10
        self.x+=5
    def draw(self):
        frame_width=self.image.w//10
        frame_height=self.image.h
        self.image.clip_draw(self.frame*frame_width,0,frame_width,frame_height,self.x,self.y,frame_width//2,frame_height//2)

class smallball:
    def __init__(self):
        self.x, self.y = random.randint(100, 300), 599;
        self.image = load_image('ball21x21.png')

    def update(self):
        self.y -= random.randint(1, 5)
        self.x += random.randint(1, 5)
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class bigball:
    def __init__(self):
        self.x,self.y=random.randint(100,300),599;
        self.image=load_image('ball41x41.png')
    def update(self):
        self.y-=random.randint(1,5)
        self.x += random.randint(1, 5)
        pass
    def draw(self):
        self.image.draw(self.x,self.y)

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x,self.y=random.randint(100,300),90
        self.frame =random.randint(1,7)
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
    def update(self):#소년을
        # 오른쪽으로 이동시키는 상호작용
        self.x+=5
        self.frame=(self.frame+1)%8

def reset_world():
    global running
    global world # == 모든 객체들을 갖고 있는 리스트

    world=[] # 하나도 객체가 없는 월드

    running = True
    #땅을 만들고 월드 추가
    grass = Grass() # 클래스 생성 이름은 대문자로 하는 것이 좋음
    world.append(grass)

    # 소년 11명을 만들고 월드에 추가
    team =[Boy() for _ in range(11)]
    world+=team
    zombie = Zombie()
    world.append(zombie)

    smallballs = [smallball() for _ in range(10)]
    world += smallballs
    bigballs = [bigball() for _ in range(10)]
    world += bigballs

    pass
# 게임 로직
def update_world():
    for game_obj in world:
        game_obj.update()
    # grass.update()  #world에 객체들을 넣어 update 작성
    # for boy in team:
    #     boy.update()# 소년의 상호작용을 시뮬레이션 계산

def render_world():
    # 월드에 객체(= grass)들을 그린다
    clear_canvas()
    for game_obj in world:
        game_obj.draw()
    # grass.draw()
    # for boy in team:
    #     boy.draw()
    update_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code
close_canvas()
