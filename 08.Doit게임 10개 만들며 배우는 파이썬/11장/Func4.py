def inputNumber(prompt):
    inp = ""
    while not inp.isnumeric():
        inp = input(prompt).strip()
    return int(inp)

num = inputNumber("숫자 입력: ")
print(num)