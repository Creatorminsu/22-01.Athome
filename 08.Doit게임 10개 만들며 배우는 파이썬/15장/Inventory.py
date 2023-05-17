############################################
# Inventory.py
# 인벤토리 시스템
############################################

inv = {
    "StructureKey": False,
    "Coins": 0
}

# 열쇠를 인벤토리에 추가하기
def takeStructureKey():
    inv["StructureKey"] = True

# 인벤토리에서 열쇠 없애기
def dropStructureKey():
    inv["StructureKey"] = False

# 플레이어는 열쇠를 가졌나요?
def hasStructureKey():
    return inv["StructureKey"]

# 동전을 인벤토리에 추가하기
def takeCoins(coins):
    inv["Coins"] += coins

# 인벤토리에서 동전 없애기
def dropCoins(coins):
    inv["Coins"] -= coins

# 플레이어가 가진 동전은 몇 개인가요?
def numCoins():
    return inv["Coins"]

# 인벤토리 출력하기
def display():
    print("**** 인벤토리 ****")
    print("가진 동전은 ", numCoins(), "개입니다.")
    if hasStructureKey():
        print("파랗게 빛나는 열쇠가 있습니다.")
    print("******************")