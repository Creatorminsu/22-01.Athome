def displayWelcome(txt):
    borderChar = "*"
    print(borderChar * (len(txt) + 4))
    print(borderChar, txt, borderChar)
    print(borderChar * (len(txt) + 4))

displayWelcome("Welcome to Coding World!")