import matplotlib.pyplot as plt
import numpy as np
import car_generetor as cg

#  F1 Clash project



# Suponha que você já gerou todas as combinações de carros e tem uma lista de Team Scores

# Criar o histograma
plt.hist(cg.team_scores, bins=20, edgecolor='k')
plt.title('Histograma de Team Scores')
plt.xlabel('Team Score')
plt.ylabel('Frequência')
plt.grid(True)


# Encontre o valor que corresponde ao percentil 80 (os 20% melhores)
percentile_80 = np.percentile(cg.team_scores, 80)

# Defina o limite/corte para considerar os 20% melhores valores
limite = percentile_80

# Adicione uma linha vermelha no histograma para marcar o limite
plt.axvline(limite, color='r', linestyle='dashed', linewidth=2, label=f'Corte: {limite}')
plt.legend()

# Salvar o gráfico em um arquivo, por exemplo, em formato PNG
plt.savefig('histograma_team_scores.png')


# Suponha que 'all_cars' seja a lista de todas as combinações de carros que você já gerou

# Ordene a lista de carros com base no 'Team Score' em ordem decrescente
cg.all_cars.sort(key=lambda car: car.car_atributes()[-1], reverse=True)

# Calcule o índice a partir do qual os 20% melhores carros começam
percent_20 = int(0.2 * len(cg.all_cars))

# Selecione os 20% melhores carros
melhores_carros = cg.all_cars[:percent_20]
for carro in melhores_carros:
    print(carro.display_status())
# Agora, 'melhores_carros' contém os 20% melhores carros com base no 'Team Score'
