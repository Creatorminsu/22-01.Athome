############################################
# Enemies.py
# 지원 함수와 적 정의하기
############################################

# 적 목록
# 각각에는 이름, 설명과 함께
# 적에게는 체력(높은 숫자 = 적을 물리치려면 더 큰 피해를 입혀야 함)과
# 방어력(낮은 숫자 = 적을 물리치기 쉬움)이 있어야 함
enemies = [
    {
        "id": "slug",
        "description": "우주 괴물",
        "strength": 10,
        "damageMin": 1,
        "damageMax": 3,
        "defense": 2
    },
    {
        "id": "eel",
        "description": "방사능 장어",
        "strength": 50,
        "damageMin": 10,
        "damageMax": 15,
        "defense": 1
    },
    {
        "id": "alien",
        "description": "녹색 촉수의 외계인",
        "strength": 25,
        "damageMin": 5,
        "damageMax": 10,
        "defense": 3
    }
]