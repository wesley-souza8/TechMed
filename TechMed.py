import heapq

# Dicionários para armazenar informações
alunos = {}
agendamentos = {}
treinamento_niveis = ['Iniciante', 'Intermediário', 'Avançado']

# Função para cadastrar alunos
def cadastrar_aluno(nome):
    if nome not in alunos:
        alunos[nome] = {
            "notas": [],
            "avaliacoes": [],
            "progresso": {"nível": 0, "pontos_acertados": 0, "pontos_errados": 0, "passos_totais": []}
        }
        print(f"Aluno(a) {nome} cadastrado com sucesso!")
    else:
        print(f"Aluno(a) {nome} já está cadastrado(a).")

# Função para agendar treinamentos
def agendar_treinamento(nome, data, horario, nivel):
    if nome not in alunos:
        print(f"Aluno(a) {nome} não encontrado(a).")
        return
    if nivel not in treinamento_niveis:
        print(f"Nível {nivel} inválido. Os níveis disponíveis são: {treinamento_niveis}")
        return
    agendamento = f"{data} às {horario} - Nível: {nivel}"
    if nome in agendamentos:
        agendamentos[nome].append(agendamento)
    else:
        agendamentos[nome] = [agendamento]
    print(f"Treinamento agendado para {nome} em {agendamento}.")

# Função para adicionar notas
def adicionar_nota(nome, nota):
    if nome in alunos:
        alunos[nome]["notas"].append(nota)
        print(f"Nota {nota} adicionada para {nome}.")
    else:
        print(f"Aluno(a) {nome} não encontrado(a).")

# Função para adicionar avaliação
def adicionar_avaliacao(nome, avaliacao):
    if nome in alunos:
        alunos[nome]["avaliacoes"].append(avaliacao)
        print(f"Avaliação adicionada para {nome}: '{avaliacao}'")
    else:
        print(f"Aluno(a) {nome} não encontrado(a).")

# Função para atualizar o progresso do aluno
def atualizar_progresso(nome, pontos_acertados, pontos_errados, passos_realizados):
    if nome in alunos:
        alunos[nome]["progresso"]["pontos_acertados"] += pontos_acertados
        alunos[nome]["progresso"]["pontos_errados"] += pontos_errados
        alunos[nome]["progresso"]["passos_totais"].extend(passos_realizados)
        print(f"Progresso atualizado para {nome}.")
    else:
        print(f"Aluno(a) {nome} não encontrado(a).")

# Função para exibir informações detalhadas de alunos
def exibir_informacoes_aluno(nome):
    if nome in alunos:
        info = alunos[nome]
        print(f"\nInformações de {nome}:")
        print(f"Notas: {info['notas']}")
        print(f"Avaliações: {info['avaliacoes']}")
        print(f"Progresso: Nível {treinamento_niveis[info['progresso']['nível']]}")
        print(f"Pontos Acertados: {info['progresso']['pontos_acertados']}")
        print(f"Pontos Errados: {info['progresso']['pontos_errados']}")
        print(f"Passos Realizados: {info['progresso']['passos_totais']}")
        if nome in agendamentos:
            print(f"Agendamentos: {agendamentos[nome]}")
        else:
            print("Nenhum treinamento agendado.")
    else:
        print(f"Aluno(a) {nome} não encontrado(a).")

# Função para avançar o nível do aluno
def avancar_nivel(nome):
    if nome in alunos:
        if alunos[nome]["progresso"]["nível"] < len(treinamento_niveis) - 1:
            alunos[nome]["progresso"]["nível"] += 1
            print(f"{nome} avançou para o nível {treinamento_niveis[alunos[nome]['progresso']['nível']]}")
        else:
            print(f"{nome} já atingiu o nível máximo.")
    else:
        print(f"Aluno(a) {nome} não encontrado(a).")

# Função para usar Dijkstra e avaliar o progresso do aluno em um treinamento
def analisar_caminho(nome, grafo, inicio, fim):
    if nome not in alunos:
        print(f"Aluno(a) {nome} não encontrado(a).")
        return
    # Dijkstra para encontrar o caminho mais curto
    fila = [(0, inicio)]
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    caminhos = {nodo: [] for nodo in grafo}
    while fila:
        dist_atual, nodo_atual = heapq.heappop(fila)
        if dist_atual > distancias[nodo_atual]:
            continue
        for vizinho, peso in grafo[nodo_atual].items():
            distancia = dist_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila, (distancia, vizinho))
                caminhos[vizinho] = caminhos[nodo_atual] + [vizinho]
    # Resultado do caminho correto
    caminho_certo = caminhos[fim]
    print(f"O caminho correto do ponto {inicio} até {fim} para {nome} é: {caminho_certo}")
    print(f"Distância total: {distancias[fim]}")
    # Comparação com os passos do aluno
    passos_realizados = alunos[nome]["progresso"]["passos_totais"]
    pontos_errados = len(set(passos_realizados) - set(caminho_certo))
    pontos_acertados = len(set(caminho_certo).intersection(passos_realizados))
    atualizar_progresso(nome, pontos_acertados, pontos_errados, passos_realizados)

# Exemplo de uso do sistema:

# Cadastrando alunos
cadastrar_aluno("João Silva")
cadastrar_aluno("Maria Oliveira")

# Agendando treinamentos
agendar_treinamento("João Silva", "25/09/2024", "14:00", 'Iniciante')
agendar_treinamento("Maria Oliveira", "26/09/2024", "09:00", 'Intermediário')

# Adicionando notas e avaliações
adicionar_nota("João Silva", 8.5)
adicionar_avaliacao("João Silva", "Bom desempenho, pode melhorar precisão.")
adicionar_nota("Maria Oliveira", 9.0)
adicionar_avaliacao("Maria Oliveira", "Excelente controle durante o treinamento.")

# Atualizando progresso
atualizar_progresso("João Silva", 5, 2, ["A", "B", "C", "E"])
atualizar_progresso("Maria Oliveira", 7, 1, ["A", "C", "D", "E"])

# Avançar nível
avancar_nivel("João Silva")

# Exibindo informações
exibir_informacoes_aluno("João Silva")
exibir_informacoes_aluno("Maria Oliveira")

# Análise de caminho com Dijkstra
grafo_treinamento = {
    'A': {'B': 1, 'C': 2},
    'B': {'D': 2},
    'C': {'D': 1, 'E': 4},
    'D': {'E': 1},
    'E': {}
}
analisar_caminho("João Silva", grafo_treinamento, 'A', 'E')
analisar_caminho("Maria Oliveira", grafo_treinamento, 'A', 'E')

# Exibindo todos os agendamentos
print("\nAgendamentos:")
for aluno, agendas in agendamentos.items():
    print(f"{aluno}: {agendas}")
