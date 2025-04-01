import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

""" numero_01 = int(input("Insira primeiro numero para soma: "))
numero_02 = int(input("Insira segundo numero para a soma:"))
soma  = numero_01 + numero_02 """

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

""" numero_01 = int(input("Digite numero para calcular resto: "))

resto = numero_01 % 5

print(f"O resto da divisão de {numero_01} por 5 é: {resto}") """

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

""" mult01 = float(input('Insira primeiro numero: '))
mult02 = float(input('Inserasegundo numero= '))
resultado = mult01*mult02

print(resultado) """


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

""" numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 // numero_02
print(resultado)
 """
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

""" num = float(input("Insira um numero: "))
quadrado = int(input('Insira um numeroa para fatorar por ele: '))

resultado = num ** quadrado

print(resultado) """

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

""" num1 = float(input('Digite um numero flutuante: '))
num2 = float(input('digite o segundo numero flutuante: '))

resultado_soma= num1+num2

print("A soma será: ", resultado_soma) """

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

""" num1 = float(input("Digite primeiro resultado para média: "))
num2 = float(input('Digite segundo resultado para média: '))

resultado_soma = num1+num2

media = resultado_soma / 2

print('A média entre os numeros são: ', media ) """

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

""" base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
base = 2.0  # Exemplo de entrada
expoente = 3.0  # Exemplo de entrada
potencia = base ** expoente
print("O resultado da potência é:", potencia) """

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
""" celsius = float(input("Digite a temperatura em Celsius: "))
celsius = 30.0  # Exemplo de entrada
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F") """
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
""" raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
print(f"{area_do_circulo:.2f}") """

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data_do_usuario = input('Insira uma data no formato dd/mm/aaaa: ')
# lista_dia_mes_ano = data_do_usuario.split("/")

# print(f"O elemento 1 da data é: {lista_dia_mes_ano[0]}")
# print(f'O elemento 2 da data é: {lista_dia_mes_ano[1]}')
# print(f'O elemento 3 da data é: {lista_dia_mes_ano[2]}')
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_de_dia_mes_ano = data_do_usuario.split("/")
# print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
# print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
# print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
""" entrada1 = input("Digite a primeira expressão bolleana (True/False): ")
entrada2 = input("Digite a segunda expressão bolleana (True/False): ")

bool1 = entrada1.lower() == "true"
bool2 = entrada2.lower() == "true"

resultado = bool1 and bool2

print("o resultado do AND lógico é: ", resultado) """
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.()
""" entrada1 = input("Digite a primeira expressão bolleana (True/False): ")
entrada2 = input("Digite a segunda expressão bolleana (True/False): ")

bool1 = entrada1.lower() == "true"
bool2 = entrada2.lower() == "true"

resultado = bool1 or bool2

print("o resultado do AND lógico é: ", resultado) """
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
""" entrada = input("Digite um valor bolleano (True/False): ")

valor_original = entrada.lower() == 'true'

valor_invertido = not valor_original

print(f"O valor digitado foi: {valor_original}")
print(f"O valor invertido foi: {valor_invertido}") """
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
""" num1 = float(input("Digite o primeiro numero para comparação: "))
num2 = float(input("digitte o segundo numero para comparação: "))

if num1==num2:
    print(f"Os úmeros {num1} e {num2} são IGUAIS!")
else:
    print(f"os números {num1} e {num2} são DIFERENTES!") """
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
""" num1 = float(input("Digite o primeiro numero para comparação: "))
num2 = float(input("digitte o segundo numero para comparação: "))

if num1==num2:
    print(f"Os úmeros {num1} e {num2} são IGUAIS!")
else:
    print(f"os números {num1} e {num2} são DIFERENTES!") """
# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação