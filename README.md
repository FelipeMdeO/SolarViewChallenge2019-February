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
basemap # Para plotar o mapa do Brasil e preencher com incidencia de irradiacao

A solução do problema consistiu em 4 etapas para sua conclusão completa, inclusive a etapa bonus.
1 - Acesso a API da Nasa ponto a ponto com offset de 0.2 graus de todo o territorio brasileiro e alimentar um banco de dados. O Script API_Reader é responsável por esta tarefa.
2 - A partir de uma entrada de latitude e longitude, o Script Result_Mean_Generator.py irá buscar os dados de todos os anos daquela latitude, irá desconsiderar os invalidos, calcular a média e gerar um gráfico

![Point plot](https://github.com/FelipeMdeO/SolarViewChallenge2019-February/blob/master/Images/Point_Incidation.png)

3 - Para solução da etapa bonus, utilizou-se um script do jupyter notebook por a biblioteca basemap, utilizada para plotar o mapa, ser mais facilmente instalada e configurada (utilizando o conda environment). O script Inicidence_Map_Data_Generator.py, a partir de uma entrada de um dado ano, calcula as medias para cada coordenada e escreve um arquivo, esse arquivo irá alimentar o arquivo jupyter de nome AT1Bonus.ipynb


![Brazil Irradiation Calc](https://github.com/FelipeMdeO/SolarViewChallenge2019-February/blob/master/Images/Brazil_Incidence.png)

( O Banco de dados não havia sido completamente preenchido ao gerar esta imagem

Respostas as perguntas:

O que significa enérgia fotovoltaica?
  Energia fotovoltaica é a energia gerada a partir de células voltáicas. Células fotovoltaicas possuem tecnologia para gerar energia a partir da luz solar, sem necessidade de partes móveis.

O que são séries temporais?
  São conjuntos de dados ordenados no tempo. Esses dados possuem relação entre si, de forma que a observação da série pode predizer acontecimentos futuros ou de espaços sem preenchimento.

Que algoritimo de machine learning você pensou em utilizar?
  Por não conhecer series temporais, a primeira opção pensada foi utilizar técnicas de regressão com base em minimização de erro, uma rede neural básica, tipo multi layer perceptron ou adaline. No entanto, após estudar brevemente sobre séries temporais e sua classe de séries estacionárias, é bem possível que uma metodologia utilizando séries temporais tenham resultados melhores.
  
  Como a SolarView utiliza dados para gerar valor para seus clientes?
    No momento tecnologico em que vivemos, a posse dados não é máximo que se pode conseguir quando se deseja conhecer e melhor um processo. É necessario processar dados, procurar padrões e informar resultados. A SolarView possui equipamentos de monitoramento em tempo real que captam dados evitando erro e falta de processo humano e além disto, faz analise desses resultados entregando aos seus clientes sugestões para melhoramento de suas soluções.
