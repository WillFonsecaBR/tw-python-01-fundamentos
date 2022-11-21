## ESTRUTURA DO WHILE
while [CONDICAO]:
    [CODIGO]

numero = 0
soma = 0

while numero < 20:
    numero = int(input("Digite um número menor que 20: "))
    soma = soma + numero

## WHILE-ELSE
numero = 0
soma = 0

while numero < 20:
    numero = int(input("Digite um número menor que 20"))
    soma = soma + numero
else:
    print("loop encerrado com sucesso") # MOSTRA UM RESULTADO OU MENSAGEM APÓS A ITERAÇÃO
print(soma)

## WHILE BREAK
numero = 0
soma = 0
while numero < 20:
    numero = int(input("Digite um número menor que 20"))
    if numero == 16:
       break
    soma = soma + numero
print(soma)

## WHILE CONTINUE
numero = 0
soma = 0
while numero < 20:
    numero = int(input("Digite um número menor que 20"))
    if numero == 16:
        continue
    soma = soma + numero

print(soma)

