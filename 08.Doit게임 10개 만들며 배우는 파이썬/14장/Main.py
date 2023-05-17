##########################################
# 스페이스 어드벤처 게임
# 벤 & 쉬무엘 만듦
##########################################

# 불러오기
import Strings
import Utils

# 플레이어 환영 메시지
def doWelcome():
    # 텍스트 출력하기
    print(Strings.get("Welcome"))
 
# 장소: 출발점
def doStart():
    # 텍스트 출력하기
    print(Strings.get("Start"))
    # 플레이어 선택 얻기
    choices = [
        ["P", "바위 더미를 조사한다"],
        ["S", "구조물에 접근한다"],
        ["B", "삐 소리가 나는 곳으로 간다"],
        ["R", "도망간다!"]
    ]
    # 플레이어 행동 선택 프롬프트
    choice = Utils.getUserChoice(choices)
    # 행동 실행하기
    if choice == 'P':
        doBoulders()
    elif choice == 'S':
        doStructure()
    elif choice == 'B':
        doBeeping()
    elif choice == 'R':
        doRun()

# 장소: 바위 더미
def doBoulders():
    # 텍스트 출력하기
    print(Strings.get("Boulders"))
    # 시작 위치로 돌아가기
    doStart()

# 장소: 구조물
def doStructure():
    # 텍스트 출력하기
    print(Strings.get("Structure"))
    # 플레이어가 선택할 수 있는 행동은?
    choices = [
        ["S", "시작 지점으로 돌아간다"],
        ["D", "문을 연다"],
        ["B", "삐 소리가 나는 곳으로 간다"],
        ["R", "도망간다!"]
    ]
    # 플레이어 행동 선택 프롬프트
    choice = Utils.getUserChoice(choices)
    # 행동 실행하기
    if choice == 'S':
        doStart()
    elif choice == 'D':
        doStructureDoor()
    elif choice == 'B':
        doBeeping()
    elif choice == 'R':
        doRun()
 
# 장소: 구조물 입구
def doStructureDoor():
    # 텍스트 출력하기
    print(Strings.get("StructureDoor"))
    print(Strings.get("StructureDoorNoKey"))
    # 플레이어가 선택할 수 있는 행동은?
    choices = [
        ["S", "구조물로 돌아간다"],
        ["R", "도망간다!"]
    ]
    # 플레이어 행동 선택 프롬프트
    choice = Utils.getUserChoice(choices)
    # 행동 실행하기
    if choice == 'S':
        doStructure()
    elif choice == 'R':
        doRun()
 
# 장소: 삐 소리 탐색하기
def doBeeping():
    pass
 
# 플레이어가 도망가기를 선택하기
def doRun():
    # 텍스트 출력하기
    print(Strings.get("Run"))
    # 사망, 게임 끝내기
    gameOver()

# 게임 끝내기
def gameOver():
    print(Strings.get("GameOver"))
 
# 실제 게임 시작은 이곳에서
# 환영 메시지 출력하기
doWelcome()
# 게임 시작하기
doStart()