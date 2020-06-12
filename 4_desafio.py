__autor__ = "Jivaldo Da Cruz"

num = []
total = 0
for x in range(7):
    num.append(int(input(f"Digite {x + 1}ª nota: ")))
    total += num[x]

total /= 7
if(total < 10):
    print(f"Tens negativa por nota ser {total}")
elif(total > 10):
    print(f"Estás no bom caminho por ter a nota de {total}")
elif(total == 10):
    print(f"Tas na balança, pois tens que estudar mais por nota no meio que é {total}")
