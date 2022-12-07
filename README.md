# Interface grafica PENELOPE


Este programa é uma interface gráfica para realizar simulações Monte Carlo focado no ensino de Física das Radiações.
As simulações são realizadas usando um código PENELOPE versão 2014 com a extensão penEasy versão 2015.

Uma explicação detalhada do programa e seu funcionamento está presente no artigo: "pyPEN: uma interface gráfica user-friendly para simulação Monte Carlo em física médica"

https://www.scielo.br/j/rbef/a/w33R7jZWq6YML46x63frHKj/?lang=pt


A Figura abaixo mostra a interface gráfica ao ser iniciada.

<p align="center">
  <img src="first_screen.png" width="350" title="Imagem da interface gráfica ao abri-la">
</p>

Nesta tela estão links para o Manual do PENELOPE 2014 [1] e também do penEasy 2015 [2]. É possível escolher dois tipos de simulação: "Deposição de dose" e "Tracking de partículas".


## 1. Deposição de dose
A Figura 2 mostra a tela da interface no modo "Deposição de Dose".

<p align="center">
  <img src="dose_screen.png" width="350" title="Imagem da interface gráfica no modo 'Deposição de Dose'">
</p>

Com o uso da interface gráfica é possível selecionar o tipo de partícula a ser simulada (elétron, fóton ou pósitron) e o número de partículas iniciais (número de histórias). A geometria de simulação consiste de uma caixa com área de 10x10 cm² e espessura variando de 1 a 5 cm. A caixa é homogênea e usando a interface gráfica é possível selecionar o material que a comp~oe. A Tabela 1 mostra composição atômica de cada material. Uma fonte monoenergética, cuja energia pode ser selecionada usando a interface, incide na superfície da caixa.

Uma vez selecionados os parâmetros da simulação, clique em "Simular", a mensagem "INICIANDO SIMULACÃO" irá aparecer, quando a simulação terminar aparecerá a mensagem "SIMULAÇÃO ACABOU". E imediatamente após o término da simulação aparecerá um gráfico da dose em profundidade. A dose em profundidade foi obtida subdividindo a caixa em fatias e determinando a dose depositada em cada fatia. Acima do gráfico é mostrada da dose média depositada em todo o objeto. Todas as doses estão em unidade de eV/g/história. Para salvar o gráfico no formato PNG clique em "Salvar Imagem" e para extrair os dados usados para gerar o gráfico clique em "Exportar gráfico como csv". Em ambos os casos o arquivo será salvo na pasta **resultados**.


Figura

O executável para Windows: https://drive.google.com/file/d/1YUrdKLbMRGNZhF5aVkr7je4U2rcBuPcR/view?usp=sharing
