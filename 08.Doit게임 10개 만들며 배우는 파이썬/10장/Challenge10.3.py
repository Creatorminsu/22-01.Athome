# 사용자가 선택한 옵션에 따라 비밀번호 생성하기
# 최소 길이는 선택한 옵션에 따라 달라짐
# 필수 사항을 처리하려면 코드는 각 유형을 하나 이상 포함해야 함
# 그밖의 모든 문자는 정해는 대상에서 무작위로 고르고 이를 섞음

# 라이브러리 불러오기
import random, string

# 옵션 선택 함수
# input() 함수에 텍스트 전달하기
# True나 False 반환하기
def promptOption(prompt):
    # result 초기화하기
    result = False
    opt = " "
    # Y나 N을 골라야 함
    while not opt in "YN":
        opt = input(prompt).strip().upper()
    # Y를 골랐다면 result를 True로 설정하기
    if opt == "Y":
        result =True
    # 반환하기
    return result

# 비밀번호 길이를 묻는 함수
# 최소 길이를 인수로 전달하기
# 길이 반환하기
def promptLength(minLen):
    # 최소 길이는 0이 아니어야 함. 0이라면 1로 변경.
    if minLen == 0:
        minLen = 1
    # result 초기화하기
    result = 0
    #prompt 문장
    prompt = "비밀번호 길이는 얼마인가요? (최소=" + str(minLen) + "): "
    # 유효한 길이가 될 때까지 반복하기
    while result < minLen:
        # 길이 묻기
        p = input(prompt).strip()
        # 유효한 숫자인지 확인하기
        if p.isnumeric():
            result = int(p)
    # 반환하기
    return result

# 비밀번호 문자 리스트(무작위로 생성한 문자 저장)
# 섞기 쉽도록 문자열이 아닌 리스트로 저장하기
pwList = []

# 사용할 문자 집합(소문자 집합부터 시작)
# 선택한 옵션에 따라 문자 집합을 추가하기
pwChars = string.ascii_lowercase

# 비빌번호 최소 길이는 선택한 옵션에 따라 다름
pwMinLen = 0

# 환영 메시지
print("비밀번호를 생성하는 데 도움을 드립니다. 준비됐나요?")

# 옵션 얻기
# 대문자
if promptOption("대문자를 포함하나요? [Y/N] "):
    # 최소 길이 늘리기
    pwMinLen += 1
    # 적어도 한 개의 대문자를 포함하기
    pwList.append(random.choice(string.ascii_uppercase))
    # 허용된 문자 집합에 대문자 추가하기
    pwChars += string.ascii_uppercase
# 숫자
if promptOption("숫자를 포함하나요? [Y/N] "):
    # 최소 길이 늘리기
    pwMinLen += 1
    # 적어도 한 개의 숫자를 포함하기
    pwList.append(random.choice(string.digits))
    # 허용된 문자 집합에 숫자 추가하기
    pwChars += string.digits
# 기호
if promptOption("기호를 포함하나요? [Y/N] "):
    # 최소 길이 늘리기
    pwMinLen += 1
    # 적어도 한 개의 기호를 포함하기
    pwList.append(random.choice(string.punctuation))
    # 허용된 문자 집합에 기호 추가하기
    pwChars += string.punctuation

# 비밀번호 길이 얻기
length = promptLength(pwMinLen)

# 반복하며 비밀번호 문자열 생성하기
while len(pwList) < length:
    # 다음 문자 추가하기
    pwList.append(random.choice(pwChars))

# 무작위로 순서를 섞어 특정 문자 유형이 항상 처음에 오지는 않도록 함 
random.shuffle(pwList)

# 리스트를 대상으로 반복하여 result 문자열 만들기 
result = ""
for c in pwList:
    result += c

# 비밀번호 출력하기
print("비밀번호:", result)