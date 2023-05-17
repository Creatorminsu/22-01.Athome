##########################################
# 스페이스 어드벤처 게임
# 벤 & 쉬무엘 만듦
##########################################
 
# 플레이어 환영 메시지
def doWelcome():
    # 텍스트 출력하기
    print("탐험가 여러분을 환영합니다!")
    print("혼란스러운 상태에서 잠을 깬 여러분은 아무것도 떠오르지 않습니다.")
    print("방문까지 겨우 기어가 손잡이를 돌렸더니 문이 열립니다.")
    print("밖으로 나가 봐도 모든 것이 낯설기만 합니다.")
    print("바깥 풍경은 척박하고 황량한 붉은 흙만이 흩날릴 뿐입니다.")
    print("우주복을 입은 자신을 발견하곤 모든 것이 궁금해집니다.")
 
# 장소: 출발점
def doStart():
    # 텍스트 출력하기
    print("주위를 둘러봐도 붉은 사막과 바위 더미와 먼지뿐입니다.")
    print("여러분 앞에는 이상하게 생긴 팔각형 구조물이 있습니다.")
    print("가까이 가니 삐 소리가 들립니다. 그리곤 멈춥니다. 아니, 계속됩니다.")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "PSBR":
        print("여러분이 할 수 있는 일:")
        print("P = 바위 더미를 조사한다")
        print("S = 구조물에 접근한다")
        print("B = 삐 소리가 나는 곳으로 간다")
        print("R = 도망간다!")
        choice = input("무엇을 하고 싶으세요? [P/S/B/R]").strip().upper()
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
# 인벤토리 시스템 구현용 개발자 메모 
# 이곳이 열쇠가 숨겨진 장소가 됩니다.
def doBoulders():
    # 텍스트 출력하기
    print("정말인가요? 그건 바위 더미입니다.")
    print("크고 무겁고 단순한 바위입니다.")
    # 시작 위치로 돌아가기
    doStart()

# 장소: 구조물
def doStructure():
    # 텍스트 출력하기
    print("여러분은 이상한 구조물을 조사합니다.")
    print("안에서는 오싹하면서도 기이한 소리가 들립니다.")
    print("문도 없고 창문도 없습니다.")
    print("아니, 문처럼 보여서 한번 열어 보려고 합니다.")
    print("그리고 삐 소리가 들립니다. 어디서 나는 소리일까요?")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "SDBR":
        print("여러분이 할 수 있는 일:")
        print("S = 시작 지점으로 돌아간다")
        print("D = 문을 연다")
        print("B = 삐 소리가 나는 곳으로 간다")
        print("R = 도망간다!")
        choice = input("무엇을 하고 싶으세요? [S/D/B/R]").strip().upper()
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
# 인벤토리 시스템 구현용 개발자 메모 
# 열쇠가 있을 때만 열 수 있습니다.
def doStructureDoor():
    # 텍스트 출력하기
    print("문은 잠긴 듯합니다.")
    print("둥근 구멍이 보입니다. 열쇠 구멍일까요?")
    print("그쪽으로 손을 내밀지만 파란빛이 번쩍이며 닫혀 버립니다!")
    print("계획한 대로는 잘 안 되는군요.")
    # 플레이어 행동 선택 프롬프트
    choice = " "
    while not choice in "SR":
        print("여러분이 할 수 있는 일:")
        print("S = 구조물로 돌아간다")
        print("R = 도망간다!")
        choice = input("무엇을 하고 싶으세요? [S/R]").strip().upper()
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
    print("한동안 달립니다.")
    print("그리곤 허공에 뜬 자신을 발견합니다. 아래로, 아래로, 아래로.")
    print("아주 깊은 골짜기로 떨어지며 다시는 빛을 보지 못하리라는 생각이 듭니다.")
    print("그리 용감한 행동은 아니었네요. 그렇죠?")
    # 사망, 게임 끝내기
    gameOver()

# 게임 끝내기
def gameOver():
    print("게임 오버!")
 
# 실제 게임 시작은 이곳에서
# 환영 메시지 출력하기
doWelcome()
# 게임 시작하기
doStart()