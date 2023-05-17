# 특정 범위의 숫자를 맞히는 게임입니다.
# 사용자는 숫자가 큰지 작은지 힌트를 얻습니다.
# 게임이 끝나면 몇 번 시도했는지를 알려 줍니다.

# 라이브러리 불러오기
import random

# 변수 정의하기
userInput = ""  # 사용자 입력 저장하기
userGuess = 0   # 사용자 입력 숫자로 저장하기

# 무작위 숫자 생성하기
randNum = random.randrange(1, 101)

# 게임 설명하기
print("1과 100 사이의 숫자 하나를 정했습니다.")
print("이 숫자는 무엇일까요?")

# 사용자가 맞힐 때까지 반복하기
while randNum != userGuess:
    # 사용자 답 입력받기
    userInput = input("예상 숫자: ").strip()
    # 입력한 값이 숫자인지 확인하기
    if userInput.isnumeric() == False:
        # 입력한 값이 숫자가 아니라면
        print(userInput, "이것은 숫자가 아닙니다!")
    else:
        # 입력한 값이 숫자라면 계속 진행하기
        # 입력한 값을 숫자로 변환하기
        userGuess = int(userInput)
        # 숫자 확인하기
        if userGuess < randNum:
            print("너무 작습니다. 다시 입력하세요.")
        elif userGuess > randNum:
            print("너무 큽니다. 다시 입력하세요.")
        else:
            print("정답입니다!")

# 끝날 때 출력할 메시지
print("즐거우셨나요? 또 만나요!")