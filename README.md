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
**HISTOGRAMA :**
![Resultado no VSCode](https://github.com/Pedro1p0/F1-Clash-Data-analysis/blob/main/histograma_team_scores.png)

### Tarefa 02 (slide 13): Pontuação: 2,00 pontos

- Utilizar o filtro da Tarefa 01 e a biblioteca NetworkX para criar um gráfico similar ao apresentado no Slide 13.

- Escolher se o tamanho do vértice será proporcional ao "Team Score" (vértice vermelho) ou ao "Out Degree" dos cards (vértice preto).

- O entregável incluirá o código e a imagem do grafo. Na descrição, explicar as conclusões obtidas no contexto do jogo F1 Clash.

- Com o grafo do item anterior, criar um gráfico para a Função de Densidade de Probabilidade (PDF) da propriedade "Out Degree" dos vértices associados aos cards dos setups, usando além do NetworkX, a biblioteca Seaborn (KDE function). O entregável inclui o código e a explicação contextualizada para o jogo F1 Clash sobre o que o PDF do "Out Degree" revela.
Consulta por Especificações

### Tarefa 03 (slide 16): Pontuação: 1,00 ponto

- Criar um grafo bipartido para as garrafinhas do jogo F1 Clash e suas propriedades correspondentes, com dois grupos: Garrafinhas e Propriedades.

- O tamanho dos vértices das Propriedades será proporcional ao "Out Degree" dos vértices.

- O entregável incluirá o código para gerar o gráfico, a imagem do grafo e uma explicação contextualizando o resultado no jogo F1 Clash, utilizando a biblioteca nxviz para um layout circular similar ao Slide 16.

### Tarefa 04 (slide 18): Pontuação: 1,00 ponto

- Tarefa livre.

- Com base no conteúdo da Semana 05, e considerando a configuração final do jogo F1 Clash derivada das peças do carro, pilotos e garrafa, propor uma solução para auxiliar um jogador a escolher uma configuração específica.

- O entregável será o código desenvolvido, as imagens criadas e uma explicação com as principais conclusões.

Documentação e Comentários

O código está bem documentado com comentários explicativos que detalham as diferentes partes do código e sua funcionalidade.
Vídeo Explicativo

[Assista ao vídeo explicativo sobre o projeto aqui]()

Conclusão

Este projeto estendeu o projeto guiado da Dataquest, adicionando funcionalidades adicionais úteis para consultar laptops com base em preço e especificações. Além disso, foi realizada uma análise de complexidade para cada função implementada, fornecendo insights sobre o desempenho dessas operações em relação ao tamanho do conjunto de dados. O código também foi devidamente documentado e comentado para facilitar a compreensão.
