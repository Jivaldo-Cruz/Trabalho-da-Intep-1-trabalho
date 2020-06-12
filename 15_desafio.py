__autor__ = "Jivaldo Da Cruz"

hora = float(input("Insira quanto que ganhas por hora: "))
horaMes = float(input("Insira o número de horas trabalhadas por mês: "))

#desconto e os calculos
bruto = hora * horaMes

social = (bruto * 11) / 100
irs = (bruto * 8) / 100
sindicato = (bruto * 5) / 100

totalDesc = (bruto * 24) / 100
totalBruto = bruto - totalDesc
print(f"{'='*80}")
print("Total de salário bruto: ",bruto,"€")
print("Segurança Social: ", social, "€, IRS: ", irs, "€, Sindicato: ", sindicato,"€")
print("Total de desconto: ",totalDesc,"€")
print("Total de salário liquido: ",totalBruto,"€")
