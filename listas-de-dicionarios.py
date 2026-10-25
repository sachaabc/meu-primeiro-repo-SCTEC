#listas de dicionários
alunos = [
    {"Nome": "Brida", "Idade": 22, "Curso": "Contábeis"},
    {"Nome": "Valéria", "Idade": 32, "Curso": "Engenharia Agronômica"},
    {"Nome": "Carlos", "Idade": 28, "Curso": "Administração"},
]

print(alunos[0]["Nome"])  # Acessando o nome do primeiro aluno
print(alunos[1]["Nome"])  # Acessando o nome do segundo aluno
print(alunos[2]["Nome"])  # Acessando o nome do terceiro aluno

empresa = {
    "Nome": "Tech Solutions",
    "Fundação": 2010,
    "Endereço": {"cidade": "Florianópolis", "estado": "SC"},
    "Funcionários": [
        {"Nome": "Alice", "Cargo": "Desenvolvedora"},
        {"Nome": "Bob", "Cargo": "Analista de Dados"},
        {"Nome": "Charlie", "Cargo": "Gerente de Projetos"},
    ],
}

print(empresa["Endereço"]["cidade"]) # Acessando a cidade do endereço da empresa
print(empresa["Funcionários"][1]["Nome"]) # Acessando o nome do segundo funcionário

############################################################
#percorrendo listas de dicionários com FOR
alunos = [
    {"Nome": "Brida", "Nota": 6.5},
    {"Nome": "Valéria", "Nota": 9.0},
    {"Nome": "Carlos", "Nota": 7.5},
]

for aluno in alunos:
    if aluno ["Nota"] >= 7:
        print(aluno["Nome"], "foi aprovado")
