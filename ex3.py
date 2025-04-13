def verificar_numero():
    numero = int(input("Qual número você quer descobrir?: "))
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

result = verificar_numero()
print(f"O seu número é {result}")