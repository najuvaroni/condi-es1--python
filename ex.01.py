nota = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota + nota2) / 2

if media <= 6:
    print("reprovado")
else:
    print("Aprovado")