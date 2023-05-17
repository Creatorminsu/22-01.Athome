guessedLetters = []  # 사용자 추측 문자를 저장할 리스트

if len(guessedLetters) > 0:
    # 입력한 내용이 있다면 빈 문자열로 시작하기
    youTried = ""
    # 추측한 문자 더하기
    for letter in guessedLetters:
        youTried += letter
    # 출력하기
    print("시도한 문자:", youTried)