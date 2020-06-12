__autor__ = "Jivaldo Da Cruz"

peso = int(input("Insira o peso do peixe em kilo: "))

if(peso <= 50):
    print("Esta tudo de boa!")
else:
    cont = 0
    x = 50
    multa = 0
    while x != peso:
        cont += 1
        multa += 4
        x += 1
    print(f"Total de kilo ultrapassado é {cont}")
    print(f"A multa por {cont}kilo ultrapassado é {multa}")
