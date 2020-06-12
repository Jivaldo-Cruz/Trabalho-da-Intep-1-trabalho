__autor__ = "Jivaldo Da Cruz"

h = float(input("Informe a sua altura: "))

qual = input("Qual é o seu sexo? Masculino(M) | Feminino(F): ")

if(qual.lower() == "f"):
    total = (62.1*h) - 44.7
    print(f"O seu peso ideal é {total:.3}")
elif(qual.lower() == "m"):
    total = (72.7*h) - 58
    print(f"O seu peso ideal é {total:.3}")
else:
    print("Tens que digitar M ou F para calcular peso de cada sexo.")
