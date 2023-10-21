from random import choice
import matplotlib.pyplot as plt
import networkx as nx
from nxviz import CircosPlot

G = nx.barbell_graph(m1=10, m2=3)

# Adicione atributo "class" a cada nó
for n, d in G.nodes(data=True):
    G.nodes[n]["class"] = choice(["a", "b", "c", "d", "e"])

# Crie um gráfico Circus Plot
c = CircosPlot(
    G,
    node_grouping="class",
    group_order="alphabetically",
    node_color="class",
    node_order="class",
    node_labels=False,
    group_label_position="middle",
    group_label_color=True,
)
c.draw()

d = CircosPlot(
    G,
    node_grouping="class",
    group_order="default",
    node_color="class",
    node_order="class",
    node_labels=False,
    group_label_position="middle",
    group_label_color=True,
)
d.draw()

plt.show()
