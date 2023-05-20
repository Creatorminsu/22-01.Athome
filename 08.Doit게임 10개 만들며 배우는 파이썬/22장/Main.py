# 불러오기
import sys, os, random
import pygame
from pygame.locals import *
 
# 게임 색상 정의하기
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

# 게임 변수 초기화하기
moveSpeed = 5
maxSpeed = 10
score = 0

# 게임 경로 설정하기
GAME_ROOT_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")

# 게임 끝내기 함수
def GameOver():
    # 게임 끝내기 
    pygame.quit()
    sys.exit()

# 게임 시작은 이곳에서
# 파이게임 초기화하기
pygame.init()

# 프레임 매니저 초기화하기
clock = pygame.time.Clock()

# 프레임 레이트 설정하기
clock.tick(60)

# 제목 표시줄 설정하기
pygame.display.set_caption("Crazy Driver")

# 이미지 가져오기
IMG_ROAD = pygame.image.load(os.path.join(IMAGE_FOLDER, "Road.png"))
IMG_PLAYER = pygame.image.load(os.path.join(IMAGE_FOLDER, "Player.png"))
IMG_ENEMY = pygame.image.load(os.path.join(IMAGE_FOLDER, "Enemy.png"))

# 게임 화면 초기화하기
screen = pygame.display.set_mode(IMG_ROAD.get_size())

# 게임 객체 만들기
# 플레이어 초기 위치 계산하기
h = IMG_ROAD.get_width()//2
v = IMG_ROAD.get_height() - (IMG_PLAYER.get_height()//2)
# player 스프라이트 만들기
player = pygame.sprite.Sprite()
player.image = IMG_PLAYER
player.surf = pygame.Surface(IMG_PLAYER.get_size())
player.rect = player.surf.get_rect(center = (h, v))

# 적
# 적 초기 위치 계산하기
hl = IMG_ENEMY.get_width()//2
hr = IMG_ROAD.get_width() - (IMG_ENEMY.get_width()//2)
h = random.randrange(hl, hr)
v = 0
# enemy 스프라이트 만들기
enemy = pygame.sprite.Sprite()
enemy.image = IMG_ENEMY
enemy.surf = pygame.Surface(IMG_ENEMY.get_size())
enemy.rect = enemy.surf.get_rect(center = (h, v))

# 메인 게임 루프
while True:
    # 제목 표시줄 점수 업데이트하기
    pygame.display.set_caption("Crazy Driver - Score " + str(score))

    # 배경 두기
    screen.blit(IMG_ROAD, (0, 0))

    # 플레이어 화면에 두기
    screen.blit(player.image, player.rect)

    # 키보드를 눌렀을 때
    keys = pygame.key.get_pressed()
    # 왼쪽 화살표 키인지 확인하기
    if keys[K_LEFT] and player.rect.left > 0:
        # 왼쪽으로 움직이기
        player.rect.move_ip(-moveSpeed, 0)
        # 너무 왼쪽으로 가지 않도록 하기
        if player.rect.left < 0:
            # 너무 갔다면 되돌리기
            player.rect.left = 0
    # 오른쪽 화살표 키인지 확인하기
    if keys[K_RIGHT] and player.rect.right < IMG_ROAD.get_width():
        # 오른쪽으로 움직이기
        player.rect.move_ip(moveSpeed, 0)
        # 너무 오른쪽으로 가지 않도록 하기
        if player.rect.right > IMG_ROAD.get_width():
            # 너무 갔다면 되돌리기
            player.rect.right = IMG_ROAD.get_width()

    # 적 화면에 두기
    screen.blit(enemy.image, enemy.rect)

    # 적을 아래쪽으로 움직이기       
    enemy.rect.move_ip(0, moveSpeed)

    # 화면 밖으로 나갔는지 확인하기
    if (enemy.rect.bottom > IMG_ROAD.get_height()):
        # 새로 무작위 위치 계산하기
        hl = IMG_ENEMY.get_width()//2
        hr = IMG_ROAD.get_width() - (IMG_ENEMY.get_width()//2)
        h = random.randrange(hl, hr)
        v = 0
        # 화면에 두기
        enemy.rect.center = (h, v)
        # 점수 업데이트하기
        score += 1
        # 속도 올리기
        if moveSpeed < maxSpeed:
            moveSpeed += 1

    # 충돌 확인하기
    if pygame.sprite.collide_rect(player, enemy):
        # 충돌! 게임 오버
        GameOver()

    # 이벤트 확인하기
    for event in pygame.event.get():
        # 플레이어가 게임을 그만두는지?
        if event.type == QUIT:
            # 게임 끝내기
            pygame.quit()
            sys.exit()

    # 화면 업데이트하기
    pygame.display.update()