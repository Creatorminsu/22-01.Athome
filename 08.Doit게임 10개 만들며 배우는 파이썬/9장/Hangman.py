import random

maxLives = 7
maskChar = "_"
livesUsed = 0
guessedLetters = []

gameWords = ["anvil", "boutique", "cookie", "fluff",
            "jazz", "pneumonia", "sleigh", "society",
            "topaz", "tsunami", "yummy", "zombie"]

gameWord = random.chocie(gameWords)

displayWord = maskChar * len(gameWord)

while gameWord != displayWord and livesUsed < maxLives:
    print(displayWord)

    if len(guessedLetters) > 0:
        youTried = ""
        for letter in guessedLetters:
            youTried += letter        
        print("시도한 문자:", youTried)
    print(maxLives - livesUsed, "번 남았습니다.")
    print()
    currGuess = input("추측 문자:").strip().lower()
    if len(currGuess) > 1:
        currGuess = currGuess[0]
    
    if currGuess in guessedLetters:
        print("이미 추측한 문자입니다:", currGuess)
    else:
        # 새로운 추측 문자이므로 추측 문자 리스트에 저장하기 
        guessedLetters.append(currGuess)
        # 리스트 정렬하기
        guessedLetters.sort()

        # 마스킹 업데이트하기
        # 빈 문자열로 시작하기
        displayWord = ""
        # 1자씩 루프하기
        for letter in gameWord:
            # 필요한 마스킹 또는 문자 추가하기
            # 추측한 문자가 맞는지?
            if letter in guessedLetters:
                # 맞힌 문자이므로 출력할 문자열에 추가하기
                displayWord += letter
            else:
                # 아직 맞히지 않은 문자는 마스킹하기
                displayWord += maskChar
        
        # 올바른 추측인가요?
        if currGuess in gameWord:
            # 정답이라면
            print ("올바른 추측입니다.")
        else:
            # 정답이 아니라면
            print ("틀렸습니다.")
            # 시도한 횟수 하나 늘리기
            livesUsed += 1
    
    # 보기 좋게 빈 줄 출력하기
    print()

# 게임을 끝내고 결과 출력하기
if displayWord == gameWord:
    # 이겼다면
    print ("여러분이 이겼습니다. 단어는", gameWord, "입니다!")
else: 
    # 졌다면
    print ("여러분이 졌습니다. 정답:", gameWord)