from adicao import adicao
from fatorial import fatorial
from multiplicacao import multiplicacao

numero1 = 10
numero2 = 20

opcao = 1

resultado = 0

if opcao == 1:
    resultado = adicao(numero1, numero2)
elif opcao == 2:
    resultado = fatorial(numero1, numero2)
elif opcao == 3:
    resultado = multiplicacao(numero1, numero2)

print('Resultado:', resultado)