guessedLetters = []  # 추측 문자를 저장할 리스트

for i in range (0, 5):
    # 추측 문자 입력받기
    currGuess = input("추측한 문자:").strip().lower()
    # 리스트에 추가하기
    guessedLetters.append(currGuess)

# 리스트 정렬하기
guessedLetters.sort()
# 출력하기
print(guessedLetters)