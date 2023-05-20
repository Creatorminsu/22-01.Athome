# 불러오기
import sys, os, random, time, pickle
import pygame
from pygame.locals import *

class Game():
    # 플레이어와 적 객체를 담을 게임 객체. 빈 객체로 초기화
    gameObjects = pygame.sprite.Group()

    ### 저장 클래스
    # 게임 변수 초기화하기
    class Variables():
        # 게임 색상 정의하기 - 상수
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED   = (255, 0, 0)

        # 기타 상수
        MAX_SPEED = 10
        TEXT_FONTS = ['comicsansms','arial']
        TEXT_SIZE_GAME_OVER = 48
        TEXT_SIZE_SCORE = 36
        GAME_ROOT_FOLDER = os.path.dirname(__file__)
        SAVE_DATA_FILE = os.path.join(GAME_ROOT_FOLDER, "crazyDriverSave.p")

        # 변수
        startSpeed = 3.0
        moveSpeed = startSpeed
        tempSpeed = moveSpeed
        score = 0
        highScore = 0
        eNum = -1

        # 고득점 저장하기
        @classmethod
        def Save(self, val):
            # 데이터베이스 만들기
            db = {
                "highScore": val
            }
            # 저장하기
            pickle.dump(db, open(self.SAVE_DATA_FILE, "wb"))

        # 고득점 불러오기
        @classmethod
        def Load(self):
            # 저장 파일이 있다면
            if os.path.isfile(self.SAVE_DATA_FILE):
                # 파일을 읽어 고득점 반환하기
                db = pickle.load(open(self.SAVE_DATA_FILE, "rb"))
                self.highScore =  db["highScore"]

        # 읽기 목적으로 점수 반환하기
        @classmethod
        def GetScore(self):
            # 점수 반환하기
            return self.score

        # 읽기 목적으로 고득점 반환하기
        @classmethod
        def GetHighScore(self):
            # 고득점 반환하기
            return self.highScore

        # 색상 반환하기
        @classmethod
        def GetColor(self, col):
            # 일관성을 위해 소문자로 고정하기
            col = col.lower().strip()
            # 요청한 색상 반환하기
            if col == 'red':
                return self.RED
            elif col == 'white':
                return self.WHITE
            elif col == 'black':
                return self.BLACK

        # 읽기 목적으로 적 개수 반환하기
        @classmethod
        def GetEnemy(self):
            # 적 개수 반환하기
            return self.eNum

        # eNum 외부에서도 읽을 수 있도록 
        @classmethod
        def SetEnemy(self, val):
            # eNum을 인수로 지정
            self.eNum = val

        # 읽기 목적으로 속도 반환하기
        @classmethod
        def GetSpeed(self):
            # 속도 반환하기
            return self.moveSpeed

        # 속도 올리기
        @classmethod
        def RaiseSpeed(self):
            # 점수 추가하기
            self.RaisePoints()
            # 최고 속도를 넘지 않으면
            if self.moveSpeed < self.MAX_SPEED:
                # 속도 올리기
                self.moveSpeed += 0.5
        
        # 점수 얻기
        @classmethod
        def RaisePoints(self):
            # 점수 올리기
            # 최고 속도라면 3점
            if self.moveSpeed >= self.MAX_SPEED:
                self.score += 3
            # 절반 속도라면 2점
            elif self.moveSpeed > (self.startSpeed + self.MAX_SPEED) / 2:
                self.score += 2
            # 1 point otherwise
            # 그 외에는 1점
            else:
                self.score += 1

            # 고득점 갱신이라면
            if self.score > self.highScore:
                # 새로운 고득점으로 설정하고 저장하기
                self.highScore = self.score
                self.Save(self.highScore)

        # 속도를 시작 시점으로 되돌리기
        @classmethod
        def ResetSpeed(self):
            # 속도 되돌리기
            self.moveSpeed = self.startSpeed

        # 일시 정지와 계속 번갈아 실행하기
        @classmethod
        def PauseToggle(self):
            # 속도가 0이라면 게임은 일시 중지
            if self.moveSpeed == 0:
                # 게임 계속 - moveSpeed로 되돌리기
                self.moveSpeed = self.tempSpeed
            # 속도가 0이 아니라면 게임 계속하기
            else:
                # 임시 변수에 속도를 저장하고 속도를 0으로 설정하기
                self.tempSpeed = self.moveSpeed
                self.moveSpeed = 0
        
        # 일시 정지인지 확인하기
        @classmethod
        def IsPaused(self):
            # 속도가 0이라면 일시 정지라는 뜻이므로 True 반환하기
            return self.moveSpeed == 0

        # 게임 끝내기 화면에 표시할 텍스트 가져오기
        @classmethod
        def GetTextParams(self):
            return self.TEXT_FONTS, self.TEXT_SIZE_GAME_OVER, self.TEXT_SIZE_SCORE

    # 이미지
    class Images():
        # 게임 경로 설정하기
        GAME_ROOT_FOLDER = os.path.dirname(__file__)
        IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")

        # 이미지 초기화 - 상수
        IMG_ROAD = pygame.image.load(os.path.join(IMAGE_FOLDER, "Road.png"))
        IMG_PLAYER = pygame.image.load(os.path.join(IMAGE_FOLDER, "Player.png"))
        IMG_ENEMIES = [
            pygame.image.load(os.path.join(IMAGE_FOLDER, "Enemy.png")),
            pygame.image.load(os.path.join(IMAGE_FOLDER, "Enemy2.png")),
            pygame.image.load(os.path.join(IMAGE_FOLDER, "Enemy3.png")),
            pygame.image.load(os.path.join(IMAGE_FOLDER, "IceCube.png")),
            pygame.image.load(os.path.join(IMAGE_FOLDER, "Oil.png"))      
        ]

        # 이미지, 특정 적 이미에 필요한 인수 반환하기
        @classmethod
        def GetImage(self, name, opt = 0):
            # 일관성을 위해 소문자로 설정하기
            name = name.lower().strip()
            # 요청한 이미지 반환하기
            if name == 'road':
                return self.IMG_ROAD
            elif name == 'player':
                return self.IMG_PLAYER
            elif name == 'enemy':
                return self.IMG_ENEMIES[opt]
        
        # 적 리스트의 길이 반환하기
        @classmethod
        def GetEnemyAmt(self):
            return len(self.IMG_ENEMIES)

    ### 게임 클래스
    # 플레이어 - 역시 스프라이트이므로 모든 스프라이트 파라미터를 기본값 설정(상속)
    class Player(pygame.sprite.Sprite):
        def __init__(self, imgs):
            # 스프라이트 관련 초기화
            super().__init__()
            # 플레이어 초기 위치 계산하기
            h = imgs.GetImage('road').get_width()//2
            v = imgs.GetImage('road').get_height() - (imgs.GetImage('player').get_height()//2)
            # player 스프라이트 만들기
            self.image = imgs.GetImage('player')
            self.surf = pygame.Surface(imgs.GetImage('player').get_size())
            self.rect = self.surf.get_rect(center = (h, v))
        def move(self, imgs, vars):
            # 키보드를 눌렀을 때
            keys = pygame.key.get_pressed()
            # 일시 정지인지?
            if vars.IsPaused() :
                # 스페이스 키 확인하기
                if not keys[K_SPACE]:
                    # 일시 정지 끄기
                    vars.PauseToggle()
            else:
                # 왼쪽 화살표 키인지 확인하기
                if keys[K_LEFT] and self.rect.left > 0:
                    # 왼쪽으로 움직이기
                    self.rect.move_ip(-vars.GetSpeed(), 0)
                    # 너무 왼쪽으로 가지 않도록 하기
                    if self.rect.left < 0:
                        # 너무 갔다면 되돌리기
                        self.rect.left = 0
                # 오른쪽 화살표 키인지 확인하기
                if keys[K_RIGHT] and self.rect.right < imgs.GetImage('road').get_width():
                    # 오른쪽으로 움직이기
                    self.rect.move_ip(vars.GetSpeed(), 0)
                    # 너무 오른쪽으로 가지 않도록 하기
                    if self.rect.right > imgs.GetImage('road').get_width():
                        # 너무 갔다면 되돌리기
                        self.rect.right = imgs.GetImage('road').get_width()
                # 스페이스 키 확인하기 key
                if keys[K_SPACE]:
                    # 일시 정지 켜기
                    vars.PauseToggle()

        # 기름 웅덩이라면 순간 이동하기
        def teleport(self, imgs):
            # 다음 렌더링을 위해 무작위로 이동할 곳을 사각형으로 만들기
            h = random.randrange(imgs.GetImage('player').get_width()//2, imgs.GetImage('road').get_width() - imgs.GetImage('player').get_width()//2)
            v = imgs.GetImage('road').get_height() - (imgs.GetImage('player').get_height()//2)
            self.rect = self.surf.get_rect(center = (h, v))
            

    # 모든 적과 장애물 - 역시 스프라이트이므로 모든 스프라이트 파라미터를 기본값으로 설정(상속)
    class Enemy(pygame.sprite.Sprite):
        def __init__(self, imgs, vars):
            super().__init__()
            # 무작위로 적 발생시키기
            vars.SetEnemy(random.randrange(0, imgs.GetEnemyAmt()))
            # 적 초기 위치 계산하기
            hl = imgs.GetImage('enemy', vars.GetEnemy()).get_width()//2
            hr = imgs.GetImage('road').get_width() - imgs.GetImage('enemy', vars.GetEnemy()).get_width()//2
            h = random.randrange(hl, hr)
            v = 0
            # enemy 스프라이트 만들기
            self.image = imgs.GetImage('enemy', vars.GetEnemy())
            self.surf = pygame.Surface(imgs.GetImage('enemy', vars.GetEnemy()).get_size())
            self.rect = self.surf.get_rect(center = (h, v))           
        def move(self, imgs, vars):
            # 적을 아래쪽으로 움직이기       
            self.rect.move_ip(0, vars.GetSpeed())
            # 화면 밖으로 나갔는지 확인하기
            if (self.rect.bottom > imgs.GetImage('road').get_height()):
                # enemy 객체 없애기
                self.kill()
                # 적 없음
                vars.SetEnemy(-1)
                # 속도와 점수 올리기
                vars.RaiseSpeed()

    # 게임 초기화
    def __init__(self):
        self.Variables.Load()
        # 데이터 읽기 - 여기서는 고득점만
        # 파이게임 초기화하기
        pygame.init()
        # 프레임 매니저 초기화하기
        self.clock = pygame.time.Clock()
        # 프레임 레이트 설정하기
        self.clock.tick(60)
        # 제목 표시줄 설정하기
        pygame.display.set_caption("Crazy Driver")
        # 게임 화면 초기화하기
        self.screen = pygame.display.set_mode(self.Images.GetImage('road').get_size())
        # 플레이어를 만들고 게임 객체 그룹에 추가하기
        self.gameObjects.add(self.Player(self.Images))
        
        # 게임 시작하기
        self.Play()

    ### 게임 함수
    # 메인 플레이
    def Play(self):
        # 메인 게임 루프
        while True:
            # 제목 표시줄 점수 업데이트하기
            pygame.display.set_caption("Crazy Driver - Score " + str(self.Variables.GetScore()))

            # 배경 두기
            self.screen.blit(self.Images.GetImage('road'), (0, 0))

            # 필요하다면 적을 만들고 게임 객체 그룹에 추가하기
            if self.Variables.GetEnemy() == -1:
                self.gameObjects.add(self.Enemy(self.Images, self.Variables))

            # 모든 객체 블리트하기
            for obj in self.gameObjects:
                self.screen.blit(obj.image, obj.rect)

            # 모든 객체 움직이기
            for obj in self.gameObjects:
                obj.move(self.Images, self.Variables)

            # 충돌 확인하기
            # 스프라이트 그룹을 대상으로 루프
            for obj in self.gameObjects:
                # obj의 유형이 Enemy가 아닌 Player라면
                if type(obj) is self.Player:
                    # 충돌을 테스트하고자 그룹에서 플레이어 제거하기
                    self.gameObjects.remove(obj)
                    # 충돌이 일어나면(True는 그렇다면 적은 없애라는 뜻)
                    if pygame.sprite.spritecollide(obj, self.gameObjects, True):
                        # 얼음 덩어리라면
                        if self.Variables.GetEnemy() == 3:
                            # 시작 시점으로 속도 되돌리기
                            self.Variables.ResetSpeed()
                        # 기름 웅덩이라면
                        elif self.Variables.GetEnemy() == 4:
                            # 플레이어를 무작위 위치로 옮기기
                            obj.teleport(self.Images)
                        # 평범한 적이라면
                        else:
                            # 게임 끝내기
                            self.GameOver()
                        self.Variables.SetEnemy(-1)
                    # 게임이 끝나지 않았다면 테스트를 끝낸 player 객체를 다시 그룹에 넣기
                    self.gameObjects.add(obj)

            # 이벤트 확인하기
            for event in pygame.event.get():
                # 플레이어가 게임을 그만두는지?
                if event.type == QUIT:
                    # 게임 끝내기
                    pygame.quit()
                    sys.exit()

            # 화면 업데이트하기
            pygame.display.update()

    # GameOver 함수 - 메시지를 출력하고 정리하기
    def GameOver(self):
        # 텍스트 변수 가져오기
        (font, sizeGameOver, sizeScore) = self.Variables.GetTextParams()

        # 게임 끝내기 문자열 만들기
        fontGameOver = pygame.font.SysFont(font, sizeGameOver)
        textGameOver = fontGameOver.render("Game Over!", True, self.Variables.GetColor('red'))
        rectGameOver = textGameOver.get_rect()
        rectGameOver.center = (self.Images.GetImage('road').get_width()//2, self.Images.GetImage('road').get_height()//2)

        # 점수 텍스트 만들기
        fontScore = pygame.font.SysFont(font, sizeScore)
        textScore = fontScore.render("Score: " + str(self.Variables.GetScore()), True, self.Variables.GetColor('red'))
        rectScore = textScore.get_rect()
        rectScore.center = (self.Images.GetImage('road').get_width()//2, self.Images.GetImage('road').get_height()//2 + self.Images.GetImage('road').get_height()//8)

        # 고득점 텍스트 만들기
        textHighScore = fontScore.render("High Score: " + str(self.Variables.GetHighScore()), True, self.Variables.GetColor('red'))
        rectHighScore = textHighScore.get_rect()
        rectHighScore.center = (self.Images.GetImage('road').get_width()//2, self.Images.GetImage('road').get_height()//2 + self.Images.GetImage('road').get_height()//4)

        # 검은색 배경에 게임 오버 메시지 출력하기
        self.screen.fill(self.Variables.GetColor('black'))
        self.screen.blit(textGameOver, rectGameOver)
        self.screen.blit(textScore, rectScore)
        self.screen.blit(textHighScore, rectHighScore)

        # 출력 업데이트하기
        pygame.display.update()

        # 객체 없애기
        for obj in self.gameObjects:
            obj.kill()
        # 일시 정지하기
        time.sleep(5)
        # 게임 끝내기 
        pygame.quit()
        sys.exit()

# 클래스 호출하기
Game()