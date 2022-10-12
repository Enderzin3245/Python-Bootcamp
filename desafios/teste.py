salario = int(input()) 
newsalario = salario

if 0<=salario and salario <=600:
    newsalario += salario * 0.17
    aumento = 10

    pf = f"{newsalario:.2f}"
    salario_mudou = str(pf).replace(".", ",")

elif 600.01<=salario and salario <=900:
    newsalario += salario * 0.13
    aumento = 13
    pf = f"{newsalario:.2f}"
    salario_mudou = str(pf).replace(".", ",")

elif 900.01<=salario and salario <=1500:
    newsalario += salario * 0.12
    aumento = 12
    pf = f"{newsalario:.2f}"
    salario_mudou = str(pf).replace(".", ",")

elif 1500.01<=salario and salario <= 2000:
    newsalario += salario * 0.10
    aumento = 10
    pf = f"{newsalario:.2f}"
    salario_mudou = str(pf).replace(".", ",")

elif 2000<salario:
    newsalario += salario * 0.05
    aumento = 5
    pf = f"{newsalario:.2f}"
    salario_mudou = str(pf).replace(".", ",")

reajuste = newsalario - salario
pf2 = f"{reajuste:.2f}"
reajuste_mudou = str(pf2).replace(".", ",")

print(f"Novo salario: {salario_mudou}")
print(f"Reajuste ganho: {reajuste_mudou}")
print(f"Em percentual: {aumento} %")