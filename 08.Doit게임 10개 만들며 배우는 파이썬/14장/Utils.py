############################################
# Utils.py
# 유틸리티 함수
############################################

# getUserChoice()
# 선택지 리스트와 선택 프롬프트를 출력하고 사용자 선택을 반환합니다.
# [["문자", "출력 텍스트"]]와 같이 리스트로 이루어진 리스트 형식으로 전달합니다.
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
        print(opt[0], "-", opt[1])
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
