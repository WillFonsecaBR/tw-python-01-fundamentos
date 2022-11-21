## ESTRUTURA DO FOR
for [VARIAVEL] in [SEQUÊNCIA]:
    [CÓDIGO]
    continue # PULA UMA ITERAÇÃO
    break # INTERROMPE A ITERAÇÃO

for x in range(1, 10):
    y = x + 1
print(y) #10

## FOR-ELSE
for x in range(1, 10):
    y = x + 1
else:
    print("loop encerrado com sucesso") # PRINTA UM RESULTADO DEPOIS DE TODAS AS ITERAÇÕES
print(y) #10
