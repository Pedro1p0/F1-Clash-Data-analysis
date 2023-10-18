import networkx as nx
import matplotlib.pyplot as plt
import car_setup as cs
import car_generetor as cg
import seaborn as sns

# Suponha que você já gerou todas as combinações de carros e tem a lista de Team Scores
team_scores = [car.car_atributes()[-1] for car in cg.all_cars]

# Selecionar os 20% melhores carros com base no Team Score
top_20_percent = sorted(
    cg.all_cars, key=lambda car: car.car_atributes()[-1], reverse=True)[:int(0.0001 * len(cg.all_cars))]
for car in top_20_percent:
    print(car.name, print(car.breaks.name))
# Crie um objeto de grafo
G = nx.Graph()

# Adicione nós para representar peças e carros
for car in top_20_percent:
    # Adicione um nó para o carro (usando seu nome aleatório como identificador)
    G.add_node(car.name, type='car')

    # Adicione nós para todas as peças presentes no carro e arestas que as conectam ao carro
    for part in [car.breaks, car.gearbox, car.rearwing, car.frontwing, car.suspension, car.engine]:
        part_name = part.name
        G.add_node(part_name, type='part')
        G.add_edge(car.name, part_name)

# Visualize o grafo
pos = nx.kamada_kawai_layout(G)
plt.figure(figsize=(12, 8))
# Define cores com base no tipo (carro ou parte)
node_colors = ['blue' if G.nodes[node]['type'] == 'car' else 'red' for node in G.nodes]
nx.draw(G, pos, with_labels=True, font_weight='bold', node_color=node_colors)
plt.savefig('grafo.png')

 #Calcular o "Out Degree" de cada nó no grafo
out_degrees = dict(G.degree(G.nodes(), weight=None))

# Converter os valores de Out Degree em uma lista
out_degree_values = list(out_degrees.values())

# Criar um histograma com seaborn e traçar a PDF com o KDE
plt.figure(figsize=(12, 8))
sns.histplot(out_degree_values, kde=True, color='blue')

plt.xlabel('Out Degree')
plt.ylabel('PDF')
plt.title('PDF do Out Degree dos Vértices')

plt.savefig('out_degree_pdf.png')
plt.show()