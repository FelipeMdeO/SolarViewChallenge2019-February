# SolarViewChallenge2019-February
This Repository have development of Solar View Challenge 2019 February

Você encontrará arquivos tanto .py quanto .ipynb (jupyter).
Muitas bibliotecas foram utilizadas, portanto, prepare sua máquina antes executar os arquivos

As seguintes bibliotecas foram utilizadas:
mysql # Acesso ao banco de dados Mysql
numpy # Montagem de vetores
time # Contagem de tempo de execucao do script
matplotlib # Plotar Grafico
request # Para requisitar dados do API da NASA
gmaps # Para plotar o mapa do Brasil e preencher com incidencia de irradiacao

A solução do problema consistiu em 4 etapas para sua conclusão completa, inclusive a etapa bonus.
1 - Acesso a API da Nasa ponto a ponto com offset de 0.2 graus de todo o territorio brasileiro e alimentar um banco de dados. O Script API_Reader é responsável por esta tarefa.
2 - A partir de uma entrada de latitude e longitude, o Script Result_Mean_Generator.py irá buscar os dados de todos os anos daquela latitude, irá desconsiderar os invalidos, calcular a média e gerar um gráfico

![alt text](http://url/to/img.png)

3 - Para solução da etapa bonus, utilizou-se um script do jupyter notebook por a biblioteca gmaps, utilizada para plotar o mapa, ser mais facilmente instalada e configurada. O script Inicidence_Map_Data_Generator.py, a partir de uma entrada de um dado ano, calcula as medias para cada coordenada e escreve um arquivo, esse arquivo irá alimentar o arquivo jupyter de nome AT1Bonus.ipynb

![alt text](http://url/to/img.png)

