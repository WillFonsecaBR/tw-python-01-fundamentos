# EXEMPLO DE LISTAS EM PYTHON

nome_da_lista = ["elemento1", "elemento2", "elemento3"] #Exemplo de lista simples.

# INSERINDO ELEMENTO NO FINAL DA LISTA
lista = ["Arroz", "Feijão"]
lista.append("Macarrão") # Adiciona um elemento no final da lista
print(lista) #Arroz, Feijão, Macarrão

# INSERINDO ELEMENTO EM UMA PISIÇÃO DA LISTA
lista2 = ["Arroz", "Feijão"]
lista2.insert(1, "Macarrão") # Insere um elemento em determinada posição
print(lista) #Arroz, Macarrão, Feijão

# REMOVENDO ELEMENTO DA LISTA
lista3 = ["Arroz", "Feijão", "Macarrão"]
lista3.remove("Macarrão") # Remove o elemento escolhido da lista
print(lista) #Arroz, Feijão

# OUTROS METODOS DE GERENCIAMENTO DE LISTAS
lista3.pop("índice") # remove o elemento da lista;
lista3.index("elemento") # retorna o índice do elemento na lista;
lista3.count("elemento") # retorna a quantidade de vezes em que um elemento aparece na lista;
lista3.sort() # Ordena a lista;
lista3.reverse() # inverte a ordem da lista.