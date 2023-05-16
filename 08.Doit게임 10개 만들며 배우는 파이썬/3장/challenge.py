import random

animals = ["강아지","앵무새","물고기","고양이","호랑이"]
adj = ["귀여운","아름다운","강한","멋진","냄새나는"]

choiceAnimal = random.choice(animals)
choiceAdjective = random.choice(adj)

print("저에게는", choiceAdjective, choiceAnimal, "가 있습니다.")