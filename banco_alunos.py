alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.0},
    {"nome": "Carla", "nota": 9.0},
    {"nome": "Diego", "nota": 5.5}
]

aprovados_contador = 0

print("*" * 60)
print("--- Alunos Aprovados (Nota >= 7) ---")

for aluno in alunos:
    if aluno["nota"] >= 7:
        print(f"Aluno(a): {aluno['nome']} | Nota: {aluno['nota']}")
        aprovados_contador += 1

# 3. Exibe o total de aprovados
print("-" * 60)
print(f"Total de alunos aprovados: {aprovados_contador}")