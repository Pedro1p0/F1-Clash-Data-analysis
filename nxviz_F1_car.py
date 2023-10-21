import networkx as nx
import nxviz
from nxviz import CircosPlot
import matplotlib.pyplot as plt
from bottles_generator import all_bottles

# Crie um grafo direcionado
G = nx.Graph()

# Adicione os nós representando as garrafas
bottle_names = [bottle.name for bottle in all_bottles]
G.add_nodes_from(bottle_names, type = "bottle_names")

# Adicione as arestas representando os outros atributos das garrafas
for bottle in all_bottles:
    for attribute, value in vars(bottle).items():
        if attribute != 'name' and value != 0:
            G.add_edge(bottle.name, attribute, value=value)

# Crie o gráfico Circus Plot
ax = nxviz.CircosPlot(G,)
#ax.draw()
plt.show()
