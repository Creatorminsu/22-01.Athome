asciiMin = 32
asciiMax = 126

key = 314159
key = str(key)

message = input("복호화할 메시지를 입력하세요: ")

messEncr = ""

for index in range(0, len(message)):
    char = ord(message[index])
    if char < asciiMin or char > asciiMax:
        messEncr += message[index]
    else:
        ascNum = char - int(key[index % len(key)])
        if ascNum < asciiMin:
           ascNum += (asciiMax - asciiMin)
        messEncr = messEncr + chr(ascNum)

print("복호화한 메시지:", messEncr)