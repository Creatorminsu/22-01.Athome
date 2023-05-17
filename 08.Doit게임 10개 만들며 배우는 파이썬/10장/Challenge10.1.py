import datetime

# 오늘 날짜 얻기
today = datetime.datetime.now()

# 사용자가 입력한 생일 얻기
mm = int(input("태어난 월을 숫자로 입력하세요: "))
dd = int(input("내어난 날을 숫자로 입력하세요: "))

# 오늘이 생일인지 확인하기
if today.month == mm and today.day == dd:
    print("생일 축하합니다!")
else:
    # 올해 생일이 지났는지 확인하고 그 결과에 따라 생일 연도 설정하기
    # 이 if 구문은 생일 달이 지났는지 또는 같은 달이라면 날짜가 지났는지를 확인  
    if today.month > mm or (today.month == mm and today.day > dd):
        yy = today.year + 1
    else:
        yy = today.year
    print("여러분의 생일까지는 ", datetime.datetime(yy, mm, dd) - today, " 남았습니다.")