nome = input("Como é seu nome ?: ")
nota1 = int(input("qual sua nota do 1 bi: "))
nota2 = int(input("qual sua nota do 2 bi: "))
nota3 = int(input("qual sua nota do 3 bi: "))

def media(nota1, nota2, nota3):
    soma = nota1 + nota2 + nota3
    media = soma / 3
    return media 

result = media(nota1, nota2, nota3) 

if result == 6:
    print(f"{nome} sua media é {result}! você está na media")
elif result >= 5:
    print(f"{nome} sua media é {result}! Você está de recuperação")
else:
    print(f"{nome} sua media é {result}! vc reprovou")