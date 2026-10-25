# Lista com 5 contatos
agenda = [
    {"nome": "Ana Silva", "telefone": "912345678", "email": "ana@email.com"},
    {"nome": "Bruno Santos", "telefone": "923456789", "email": "bruno@email.com"},
    {"nome": "Carla Sousa", "telefone": "934567890", "email": "carla@email.com"},
    {"nome": "Diego Costa", "telefone": "945678901", "email": "diego@email.com"},
    {"nome": "Eduarda Lima", "telefone": "956789012", "email": "eduarda@email.com"}
]

# Função para buscar contato pelo nome
def buscar_contato(nome_busca):
    encontrados = []
    for contato in agenda:
        if nome_busca.lower() in contato["nome"].lower():
            encontrados.append(contato)
    return encontrados

# Teste
termo = input("Digite o nome para buscar: ")
resultados = buscar_contato(termo)

if resultados:
    print(f"\n--- Contato(s) encontrado(s) ---")
    for c in resultados:
        print(f"Nome: {c['nome']} | Tel: {c['telefone']} | Email: {c['email']}")
else:
    print("\nNenhum contato encontrado.")