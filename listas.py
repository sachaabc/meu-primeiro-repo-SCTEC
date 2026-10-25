frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]

print(frutas[0])  # Acessa o primeiro elemento da lista
print(frutas[2])  # Acessa o terceiro elemento da lista
print(frutas[-1])  # Acessa o último elemento da lista

#fatiamento/slicing
numeros = [10, 20, 30, 40, 50]
print(numeros[1:3])  # Acessa os elementos de índice 1 a 3
print(numeros[:2])   # Acessa os três primeiros elementos
print(numeros[::-1]) # Acessa os elementos em ordem reversa


# Exercício: COMMIT SUA 1ª LISTA

preferidos = ["celular", "cama", "livro", "notebook", "carro"]

preferidos.append("tablet")  # Adiciona um item ao final da lista
print(preferidos)

preferidos.remove("livro")  # Remove um item da lista
print(preferidos)  

preferidos.sort()  # Ordena a lista em ordem alfabética
print(preferidos)