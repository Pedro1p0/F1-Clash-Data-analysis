### Objetivo Principal: Aplicar o conhecimento adquirido sobre grafos/redes na Semana 05 conforme detalhado em https://github.com/ivanovitchm/datastructure.

### Objetivos Secundários:

- Implementar o conhecimento da semana 5 no contexto apresentado do jogo F1 Clash.
- Utilizar como referência os elementos citados nos slides: componentes do veículo (cards), pontuação dos pilotos, e garrafinhas (boost).
- 
# Equipe
- Pedro Henrique Bezerra Fernandes
- Pedro Vitor Bezerra Clemente
## Tarefa 01 (slides 11 e 12): Pontuação: 1,00 ponto

- Criar um histograma para a métrica "Team Score" com as 262.144 combinações possíveis de configuração de veículo.

- Estabelecer um limite no histograma que reduza significativamente as configurações possíveis.

- O entregável será o código Python usado para criar o gráfico, similar ao apresentado no slide 12, junto com uma descrição do processo e a lógica para definir o filtro limitador para o "Team Score". Toda a explicação deverá estar no arquivo README.md do repositório no Github referente ao respectivo trabalho.
## HISTOGRAMA : ##
![Resultado no VSCode](https://github.com/Pedro1p0/F1-Clash-Data-analysis/blob/main/histograma_team_scores.png)

No gráfico acima, representamos os 262.144 carros gerados a partir das diversas combinações de peças disponíveis no jogo. O gráfico ilustra a distribuição desses carros com base em seus "teamscores," que é uma métrica de desempenho. Utilizamos esse histograma para identificar concentrações de carros com desempenho semelhante e determinar onde os carros de melhor desempenho estão agrupados.

Usando essa representação visual, conseguimos estabelecer uma linha de corte, selecionando apenas os 20% dos carros que obtiveram os melhores "teamscores." Essa seleção será usada em análises futuras, permitindo-nos concentrar nossos estudos nos carros de alto desempenho e explorar mais a fundo as características que os tornam excepcionais.
### Tarefa 02 (slide 13): Pontuação: 2,00 pontos

- Utilizar o filtro da Tarefa 01 e a biblioteca NetworkX para criar um gráfico similar ao apresentado no Slide 13.

- Escolher se o tamanho do vértice será proporcional ao "Team Score" (vértice vermelho) ou ao "Out Degree" dos cards (vértice preto).

- O entregável incluirá o código e a imagem do grafo. Na descrição, explicar as conclusões obtidas no contexto do jogo F1 Clash.

- Com o grafo do item anterior, criar um gráfico para a Função de Densidade de Probabilidade (PDF) da propriedade "Out Degree" dos vértices associados aos cards dos setups, usando além do NetworkX, a biblioteca Seaborn (KDE function). O entregável inclui o código e a explicação contextualizada para o jogo F1 Clash sobre o que o PDF do "Out Degree" revela.
Consulta por Especificações

## Gráfico : ##
![Resultado no VSCode](https://github.com/Pedro1p0/F1-Clash-Data-analysis/blob/main/grafo.png)

Aqui está um grafo que representa as relações entre os carros e as peças que compartilham entre si. Como mencionei anteriormente na primeira tarefa, inicialmente, usamos os 20% melhores carros para criar esse gráfico. No entanto, devido ao grande número de carros envolvidos, o gráfico resultante estava excessivamente complexo e difícil de interpretar. Para mitigar esse problema, decidimos focar em um subconjunto menor de carros, selecionando apenas alguns dos melhores.

Podemos observar que, mesmo com essa abordagem, o gráfico ainda apresenta alguma complexidade visual devido ao compartilhamento de peças comuns entre os carros de alta performance. No entanto, essa repetição de peças pode ser explicada pelo fato de que os melhores carros tendem a utilizar as mesmas peças de alto desempenho.

Para obter um gráfico mais uniforme e de menor complexidade visual, uma alternativa seria escolher carros aleatoriamente entre as 262.144 combinações possíveis. Isso resultaria em um conjunto de carros mais diversificado, onde as conexões representariam o compartilhamento aleatório de peças entre carros, ao invés de focar apenas nos melhores carros.

Essa abordagem proporcionaria um gráfico mais equilibrado e menos complexo, tornando a análise das relações entre os carros e as peças mais clara e informativa.

## Out Degree : ##
![Resultado no VSCode](https://github.com/Pedro1p0/F1-Clash-Data-analysis/blob/main/out_degree_pdf.png)

## Explicação ##
O "Out Degree" se refere ao número de arestas direcionadas que saem de um nó (vértice) em um grafo. Em termos simples, ele indica quantas conexões um nó possui que vão para outros nós no grafo. É uma medida importante na análise de redes, pois ajuda a entender a importância ou centralidade de um nó em relação aos seus vizinhos. Quanto maior o "Out Degree" de um nó, mais conexões ele tem saindo dele para outros nós na rede. Isso pode revelar informações sobre a influência ou o papel desse nó na rede.

### Tarefa 03 (slide 16): Pontuação: 1,00 ponto
- Criar um grafo bipartido para as garrafinhas do jogo F1 Clash e suas propriedades correspondentes, com dois grupos: Garrafinhas e Propriedades.

- O tamanho dos vértices das Propriedades será proporcional ao "Out Degree" dos vértices.

- O entregável incluirá o código para gerar o gráfico, a imagem do grafo e uma explicação contextualizando o resultado no jogo F1 Clash, utilizando a biblioteca nxviz para um layout circular similar ao Slide 16.
  
![Resultado no VSCode](https://github.com/Pedro1p0/F1-Clash-Data-analysis/blob/main/grafo_circos.png)

O gráfico demonstra a relação entre as garrafas de um jogo, onde cada nó azul representa uma garrafa específica. As arestas são usadas para mostrar a ocorrência de atributos que se repetem em diferentes garrafas. Se duas garrafas compartilham o mesmo atributo, uma aresta é desenhada entre elas no gráfico

### Tarefa 04 (slide 18): Pontuação: 1,00 ponto

- Tarefa livre.

- Com base no conteúdo da Semana 05, e considerando a configuração final do jogo F1 Clash derivada das peças do carro, pilotos e garrafa, propor uma solução para auxiliar um jogador a escolher uma configuração específica.

- O entregável será o código desenvolvido, as imagens criadas e uma explicação com as principais conclusões.

## Explicação ##

- Criação do Gráfico de Dispersão: Utilizando a biblioteca matplotlib, um gráfico de dispersão foi criado, onde o eixo x representava o "Out Degree" e o eixo y representava o "Team Score". Cada ponto no gráfico correspondia a uma configuração de veículo específica.
  
## Gráfico de Dispersão : ##
![Resultado no VSCode](https://github.com/Pedro1p0/F1-Clash-Data-analysis/blob/main/team_score_vs_out_degree.png)

- Análise do Gráfico: Os jogadores poderiam analisar o gráfico para identificar configurações de veículo que se destacavam. Por exemplo, configurações com um alto "Team Score" e um alto "Out Degree" poderiam ser consideradas ideais.

Documentação e Comentários

O código está bem documentado com comentários explicativos que detalham as diferentes partes do código e sua funcionalidade.
Vídeo Explicativo

[Assista ao vídeo explicativo sobre o projeto aqui](https://drive.google.com/file/d/1upZTB2wRNxkudQLEfQWxQyKZCBMNlUXK/view?usp=sharing)

## Conclusão ##
O projeto visa aplicar conceitos de análise de redes em um contexto de jogo (F1 Clash) e é composto por quatro tarefas. As tarefas envolvem a criação de gráficos, análises de métricas, e a geração de soluções para auxiliar jogadores na escolha de configurações. O resultado deve ser compartilhado em um repositório no GitHub e apresentado em um vídeo. O projeto oferece a oportunidade de aplicar habilidades de análise de dados e programação, enquanto fornece insights relevantes para jogadores.


