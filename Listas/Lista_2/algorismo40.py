""" Entrar com dois números inteiros e imprimir a seguinte saída:
Dividendo
Divisor
Quociente
Resto """

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))
quociente = dividendo // divisor
resto = dividendo % divisor

print(f"Dividendo: {dividendo}\nDivisor: {divisor}\nQuociente: {quociente}\nResto: {resto}")