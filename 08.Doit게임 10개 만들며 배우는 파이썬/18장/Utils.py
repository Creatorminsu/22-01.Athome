############################################
# Utils.py
# 유틸리티 함수
############################################

from Items import items
from colorama import Fore

# getUserChoice()
# 선택지 리스트와 선택 프롬프트를 출력하고 사용자 선택을 반환합니다.
# [["문자", "츨력 텍스트"]]와 같이 리스트로 이루어진 리스트 형식으로 전달합니다.
# 예: [["A", "A 선택"],["B", "B 선택"],["C", "C 선택"]]
# 선택한 문자 반환하기
def getUserChoice(options):
    # 유효한 입력을 저장할 변수 초기화
    validInputs = ""
    # 선택지 루프
    for opt in options:
        # 유효한 입력 목록에 선택 가능한 문자 추가하기 
        validInputs += opt[0]
        # 출력하기
        print(Fore.YELLOW + opt[0], "-", opt[1])
    # 프롬프트 만들기
    prompt = "무엇을 하고 싶으세요? [" + validInputs + "]: "
    # 변수 초기화하기
    choice = ""
    done = False
    # 메인 루프
    while not done:
        # 대문자 하나 가져오기
        choice = input(prompt).strip().upper()
        # 사용자가 2자 이상 입력했을 때
        if len(choice) > 1:
            # 첫 문자만 사용
            choice = choice[0]
        # 입력한 문자가 유효한지?
        if len(choice) == 1 and choice in validInputs:
            # 그렇다면 빠져나가기
            done = True
    # 선택한 옵션 반환하기
    return choice

# inputNumber()
# 숫자 입력 함수
def inputNumber(prompt):
    # 입력 변수
    inp = ""
    # 변수가 숫자일 때까지 반복하기
    while not inp.isnumeric():
        # 입력 프롬프트
        inp = input(prompt).strip()
    # 숫자 반환하기
    return int(inp)

# inputYesNo()
# 사용자가 "Y"를 고르면 True, "N"를 고르면 False 
def inputYesNo(text):
    # 루프
    while True:
        # 프롬프트 출력하기
        x = input(text + " [Y/N]").upper()
        # 응답 확인하기
        if x in ["Y", "YES"]:
            return True
        elif x in ["N", "NO"]:
            return False

# 아이템 얻기
# getUserChoice()에서 사용하는 형식으로 반환하기
def getItems():
    # 결과 저장 변수
    result = []
    # 아이템 루프
    for item in items:
        # 빈 리스트 만들기
        i = []
        # 이름(키) 추가하기
        i.append(item["key"])
        # description + cost 추가하기
        i.append(item["description"] + " (" + str(item["cost"]) + ")")
        # 이 아이템을 결과에 추가하기
        result.append(i)
    # 결과 반환하기
    return result