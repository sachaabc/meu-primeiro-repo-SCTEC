# 1. Cria uma tupla com os 3 dias favoritos
dias_tupla = ("Quinta", "Sexta", "Sábado")
print("Tupla inicial:", dias_tupla)

# 2. Converte a tupla para lista usando list()
dias_lista = list(dias_tupla)

# 3. Adiciona um novo dia à lista
dias_lista.append("Quinta-feira")
print("Lista após adicionar um dia:", dias_lista)

# 4. Converte de volta para tupla usando tuple()
dias_tupla_final = tuple(dias_lista)
print("Tupla final:", dias_tupla_final)