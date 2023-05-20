############################################
# Player.py
# player 클래스
############################################

import Items

# player 클래스 정의하기
class player:   

    # 속성
    name = "탐험가"
    livesLeft = 3
    boulderVisits = 0
    maxHealth = 100
    health = maxHealth

    # name 속성 얻기
    def getName(self):
        return self.name

    # 플레이어 라이프 개수 얻기
    def getLivesLeft(self):
        return self.livesLeft

    # 플레이어 죽음
    def died(self):
        if self.livesLeft > 0:
            self.livesLeft -= 1

    # 플레이어가 살았다면
    def isAlive(self):
        return True if self.livesLeft > 0 else False

    # 바위 더미 방문 횟수 얻기
    def getBoulderVisits(self):
        return self.boulderVisits

    # 플레이어 바위 더미 방문하기
    def visitBoulder(self):
        self.boulderVisits += 1
    
    # 라이프 추가하기
    def addLife(self, lives = 1):
        # 라이프 늘리기
        self.livesLeft += lives
        # 체력 충전하기
        self.health = self.maxHealth

    # 플레이어 라이프 감소하기
    def loseLife(self, lives = 1):
        # 라이프 줄이기
        self.livesLeft -= lives
        # 0 아래로 내려가지 않도록 하기
        if self.livesLeft < 0:
            # 그렇다면 0으로 지정하기
            self.livesLeft = 0
        # 라이프가 없다면
        if self.livesLeft == 0:
            # 체력도 없다면
            self.health = 0
        # 라이프가 남았다면
        elif self.livesLeft >= 1:
            # 체력을 최댓값으로 설정하기
            self.health = self.maxHealth

    # 체력 얻기
    def getHealth(self):
        return self.health

    # 체력 더하기
    def addHealth(self, health):
        self.health += health
        # maxHealth를 넘지 않도록
        if self.health > self.maxHealth:
            # 더 높아지면 최댓값으로
            self.health = self.maxHealth
        
    # 체력 잃기
    def loseHealth(self, health):
        self.health -= health
        # 0 아래로 내려가지 않도록
        if self.health < 0:
            # 라이프 잃기
            self.loseLife()
