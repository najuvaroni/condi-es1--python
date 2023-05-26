num = float(input('Digite um número: '))
num2 = float(input('Digite o seguno número: '))

if num < num2:
    print("O " , num , "é menor que " , num2)

elif num2 == num or num == num2:
    print("são iguais" )

else:
    print("O " , num , "é maior que " , num2)