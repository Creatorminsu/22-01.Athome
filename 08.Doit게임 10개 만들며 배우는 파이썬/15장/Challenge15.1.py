############################################
# Inventory.py
# 인벤토리 시스템
############################################

inv = {
    "StructureKey": False,
    "Coins": 0,
    "LaserBlaster": False,
    "QuantumGrenades": 0,
    "PlasmaShield": False,
    "GalacticMap": False,
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

# 인벤토리에 광선총 추가하기
def takeLaserBlaster():
    inv["LaserBlaster"] = True

# 인벤토리에서 광선총 없애기
def dropLaserBlaster():
    inv["LaserBlaster"] = False

# 플레이어가 광선총을 가졌는지?
def hasLaserBlaster():
    return inv["LaserBlaster"]

# 인벤토리에 수류탄 추가하기
def takeGrenades(grenades):
    inv["QuantumGrenades"] += grenades

# 인벤토리에서 수류탄 없애기
def dropGrenades(grenades):
    inv["QuantumGrenades"] -= grenades

# 플레이어가 몇 개의 수류탄을 가졌는지?
def numGrenades():
    return inv["QuantumGrenades"]

# 인벤토리에 플라스마 방패 추가하기
def takePlasmaShield():
    inv["PlasmaShield"] = True

# 인벤토리에서 플라스마 방패 없애기
def dropPlasmaShield():
    inv["PlasmaShield"] = False

# 플레이어가 플라스마 방패를 가졌는지?
def hasPlasmaShield():
    return inv["PlasmaShield"]

# 인벤토리에 은하계 지도 추가하기
def takeGalacticMap():
    inv["GalacticMap"] = True

# 인벤토리에서 은하계 지도 없애기
def dropGalacticMap():
    inv["GalacticMap"] = False

# 플레이어가 은하계 지도를 가졌는지?
def hasGalacticMap():
    return inv["GalacticMap"]

# 인벤토리 출력하기
def display():
    print("******* 인벤토리 *******")
    print("가진 동전은 ", numCoins(), "개입니다.")
    if hasStructureKey():
        print("파랗게 빛나는 열쇠가 있습니다.")
    if hasGalacticMap():
        print("은하계 지도가 있습니다.")
    if hasPlasmaShield():
        print("플라스마 방패가 있습니다.")
    if hasLaserBlaster() == False and numGrenades() == 0:
        print("아무런 무기도 없습니다.")
    if hasLaserBlaster():
        print("광선총이 있습니다.")
    if numGrenades() > 0:
        print(numGrenades(),"개의 퀀텀 수류탄이 있습니다.")
    print("************************")