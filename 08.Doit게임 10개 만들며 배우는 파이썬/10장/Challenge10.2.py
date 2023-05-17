# 계산 금액과 서비스 평가 입력하기
billAmt = float(input("계산서 금액을 입력하세요: ")) #billAmt는 billAmount의 준말입니다. 
num = int(input("서비스 평가(별 1~5개): "))

# 몇 명이 식사했는지 입력하기
diners = int(input("식사 인원: "))

# 평가에 따른 팁 가중치 정하기
if num == 2:
    tipPnt = 10 #tipPnt는 tipPercent의 준말입니다. 
elif num == 3:
    tipPnt = 15
elif num == 4:
    tipPnt = 18
elif num == 5:
    tipPnt = 22
else:
    tipPnt = 0

# 계산 금액에 대한 팁과 이를 더한 전체 금액 계산하기
tip = tipPnt/100 * billAmt
total = billAmt + tip

# 결과 출력하기
# 반올림은 선택 사항이나 'round(num, 2)'라고 하면 소수점 두 자리에서 반올림한 num 반환하기
# 더하기 전 반올림하면 합계 금액의 소수점 이하가 올바르지 않을 수도 있음
print("계산 금액: $", round(billAmt, 2), ", 팁: $", round(tip, 2), ", 합계 금액: $", round(total, 2))

# 한 사람이 내야할 금액
print("1인당 금액: $", round(total/diners, 2))

