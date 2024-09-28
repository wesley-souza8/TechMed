## Alunos

- Deivison Pertel – **RM 550803**
- Eduardo Akira Murata – **RM 98713**
- Guilherme Jacob Soares da Costa – **RM 84581**
- Fabrizio El Ajouri Romano – **RM 550410**
- Wesley Souza de Oliveira – **RM 97874**
---

# TechMed - Sistema de Agendamento e Avaliação de Treinamentos para Laparoscopia

## Introdução

O **TechMed** é uma solução desenvolvida para auxiliar na capacitação e treinamento de estudantes de medicina na área de laparoscopia. O sistema oferece funcionalidades de agendamento de horários de treinamento, avaliação de desempenho, armazenamento de progresso e análise dos pontos corretos e errados durante os treinamentos. A principal inovação é a inclusão de um algoritmo de Dijkstra que permite avaliar os passos realizados pelos alunos durante os treinamentos, comparando-os com a sequência ideal de ...

O sistema foi projetado para oferecer níveis de treinamento (básico, intermediário e avançado) e acompanhar o progresso individual de cada aluno. A cada treinamento, o aluno pode visualizar seu desempenho e identificar os pontos que precisam de melhorias.

## Funcionalidades

- **Agendamento de Treinamento**: Permite que os alunos escolham horários disponíveis para os treinamentos de laparoscopia.
- **Acompanhamento de Progresso**: Armazena o desempenho do aluno em diferentes níveis de treinamento e até onde ele conseguiu avançar.
- **Análise de Desempenho com Dijkstra**: Implementação do algoritmo de Dijkstra para identificar os pontos certos e errados dos alunos durante o treinamento, sugerindo melhorias com base na rota ideal.
- **Níveis de Treinamento**: Classificação dos treinamentos em três níveis: Básico, Intermediário e Avançado, com acompanhamento de progresso específico para cada um.
- **Avaliação e Feedback Final**: Após o treinamento, o aluno recebe uma nota e feedback, com uma análise dos passos corretos e incorretos.

## Metodologia

O projeto foi desenvolvido utilizando a metodologia ágil, com entregas incrementais e desenvolvimento contínuo do MVP (Minimum Viable Product). O principal foco foi fornecer um sistema que pudesse ser expandido para múltiplos níveis de treinamento e diferentes tipos de análises de desempenho.

### Estrutura de Dados

Foram utilizadas estruturas de dados simples e eficazes para armazenar os dados dos alunos, progresso e análise de desempenho:

- **Dicionários** para armazenar as informações dos alunos, seus horários de treinamento e avaliações.
- **Matriz** para armazenar o progresso de cada aluno nos diferentes níveis de treinamento.
- **Grafo** para modelar os módulos do treinamento e aplicar o algoritmo de Dijkstra para analisar os passos dos alunos.

### Algoritmo de Dijkstra

O algoritmo de Dijkstra foi implementado para avaliar a rota que o aluno seguiu durante o treinamento. Isso nos permite identificar os pontos certos e errados, comparando com a sequência ideal de ações que o aluno deveria ter tomado.

Exemplo de grafo para os módulos do treinamento:

```python
grafo_treinamento = {
    'Inicio': [('Modulo1', 1), ('Modulo2', 4)],
    'Modulo1': [('Fim', 1)],
    'Modulo2': [('Fim', 2)],
    'Fim': []
}
```

### Funções em Python

O sistema conta com várias funções que implementam a lógica do sistema:

- **Agendar Treinamento:** Função que permite o aluno selecionar um horário disponível.
- **Atualizar Progresso:** Função que armazena o progresso do aluno em cada nível de treinamento.
- **Avaliação com Dijkstra:** Função que utiliza o algoritmo de Dijkstra para determinar quais os passos corretos e quais passos errados o aluno tomou durante o treinamento.

### Resultados
Com o sistema **TechMed**, foi possível:

- Organizar e gerenciar os horários de treinamento dos alunos.
- Acompanhar o progresso em diferentes níveis de treinamento de forma eficiente.
- Analisar de forma detalhada o desempenho dos alunos, identificando pontos corretos e incorretos.
- Proporcionar feedback personalizado para cada aluno, melhorando assim o processo de aprendizado.

### Conclusão
O **TechMed** é uma solução inovadora que combina tecnologias simples com algoritmos avançados para proporcionar uma experiência de treinamento mais eficaz para estudantes de medicina. A inclusão do algoritmo de Dijkstra permite uma análise mais profunda do desempenho dos alunos, ajudando-os a identificar os passos corretos que deveriam ter tomado.

### Próximos Passos
- Expansão para novos tipos de treinamentos médicos.
- Melhorias na interface do sistema.
- Integração com plataformas de e-learning para fornecer mais recursos aos alunos.

### Como Executar o Projeto

1. Clone este repositório:

```bash
git clone https://github.com/wesley-souza8/TechMed.git
```

2. Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

3. Execute o código principal:

``` bash
python techmed.py
```

### Diagrama
Segue um exemplo de como o sistema funciona, passo a passo, utilizando o algoritmo de Dijkstra para o agendamento e avaliação de desempenho:

1. Receber Input: O aluno escolhe seu horário de treinamento.
2. Atribuir Nível: O sistema identifica o nível de treinamento do aluno (Básico, Intermediário ou Avançado).
3. Registrar Progresso: O progresso do aluno é salvo em uma estrutura de matriz.
4. Avaliação do Desempenho: Após o treinamento, o algoritmo de Dijkstra é utilizado para identificar os pontos certos e errados baseados na sequência ideal.
5. Exibir Resultados e Feedback: O aluno visualiza seu desempenho e recebe sugestões de melhorias.

### Estruturas de Dados
 - **Dicionário:** Usado para armazenar alunos e suas respectivas informações.
 - **Matriz:** Usada para armazenar o progresso nos treinamentos.
 - **Grafo:** Representa a sequência ideal dos passos no treinamento e é usado no algoritmo de Dijkstra.
