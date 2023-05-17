gameWord = "apocalypse"
guessedLetters = ["a", "e"]
maskChar = "_"

# 빈 문자열로 시작하기
displayWord = ""
# 1자씩 루프하기
for letter in gameWord:
    print(letter)
    # 추측한 문자가 맞는지?
    if letter in guessedLetters:
        print("맞힌 문자입니다.")
        # 맞힌 문자이므로 출력할 문자열에 추가하기
        displayWord += letter
    else:
        print("틀린 문자입니다.")
        # 틀린 문자이므로 숨기기
        displayWord += maskChar
    print("displayWord는", displayWord, "입니다.")

# 결과 단어 출력하기
print("원래 단어:", gameWord)
print("마스킹한 단어:", displayWord)