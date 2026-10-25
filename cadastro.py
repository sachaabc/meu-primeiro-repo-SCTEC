
pessoa = {
    "Nome": "Valéria", 
    "Idade": 32, 
    "Cidade": "Goiânia", 
    "Profissão": "Engenheira Agrônoma", 
    "Bairro":"Setor Marista",
    "Estado Civil": "Solteira"
    }


print("Dicionário originário:", "\n", pessoa)
print("*"*60)

#adicionando um novo item ao dicionário
pessoa.update({"E-mail": "val.engenheira@gmail.com"})

print("Dicionário com novo item:", "\n", pessoa)

#utiliza um for com .items() para imprimir cada chave e valor
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")