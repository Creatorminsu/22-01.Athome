# 마일을 킬로미터로 변환하기
def miles2km(num):
    return num * 1.6

# 킬로미터를 마일로 변환하기
def km2miles(num):
    return num * 0.6

# 함수 사용하기
miles = int(input("마일 단위로 값을 입력하세요: "))
print(miles, "마일 = ", miles2km(miles), "킬로미터")
km = int(input("킬로미터 단위로 값을 입력하세요: "))
print(km, "킬로미터 = ", km2miles(km), "마일")