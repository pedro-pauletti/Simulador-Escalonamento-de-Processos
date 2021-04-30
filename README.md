
<p align="center">
    <img src="https://img.shields.io/github/repo-size/pedro-pauletti/Simulador-Escalonamento-de-Processos">
    <img src="https://img.shields.io/github/downloads/pedro-pauletti/Simulador-Escalonamento-de-Processos/total">
    <img src="https://img.shields.io/github/contributors/pedro-pauletti/Simulador-Escalonamento-de-Processos">
</p>

<p>
<h1 align="center">
    <img title="Simulador Escalonmaento de Processos" src="assets/icone.png"/>
    <h1 align="center">Simulador Escalonamento de Processos</h1>
</h1>
</p>


### Simulador de Escalonamento de Processos com propósito educacional e didático, desenvolvido para a disciplina de Sistemas Operacionais l

<p>
<h1 align="center">
    <img title="Tela Inicial" src="assets/tela-inicial.png" width = "500px"/>
</h1>
</p>

<a align="center" href="https://drive.google.com/file/d/1aux05brGhv8saMChXao-SsxKQgwoiPd-/view?usp=sharing"><img src="https://user-images.githubusercontent.com/57163905/116627559-baed5e80-a923-11eb-95a2-69a67574a487.png" width = "400px"></a>

Conheça o projeto:
=================
<!--ts-->
   * [Sobre](#Sobre)
   * [Interface](#interface)
   * [Como utilizar?](#Como-utilizar)
   * [Algoritmos de Escalonamento](#Algoritmos-de-Escalonamento)
      * [FCFS](#FCFS)
      * [SJFS](#SJFS)
      * [Prioridade](#prioridade)
      * [Loteria](#loteria)
      * [Round Robin](#Round-Robin)
      * [Múltiplas Filas](#múltiplas-Filas)
   * [Ferramentas Utilizadas](#ferramentas-utilizadas)
   * [Referências](#referências)
   * [Autor](#Autor)
<!--te-->

## Sobre 💬

Escalonamento de processos é o ato de realizar o chaveamento dos processos ativos, de acordo com regras bem estabelecidas, de forma que todos os processos tenham chance de utilizar a UCP. O escalonador é a parte do SO encarregada de decidir entre os processos prontos, qual será colocado em execução. A ideia de criar um simulador é para que estudantes e interessados possam compreender e analisar o funcionamento dos algoritmos de escalonamento de processos de forma simples, visual e didática. Todos os algoritmos foram desenvolvidos em Python. A interface foi concebida utilizando a biblioteca gráfica PySimpleGUI.


## Interface 💻
![interface](https://user-images.githubusercontent.com/57163905/116623742-16681e00-a91d-11eb-9de1-5688a097490b.png)



## Como Utilizar? 💡

### ➡ Dúvida sobre o funcionamento do algoritmo?
Clique no ❔ para mostrar o popup com a descrição do algoritmo:
<p>
<h1 align="center">
    <img title="Tela Inicial" src="https://user-images.githubusercontent.com/57163905/116347582-db51d780-a7c2-11eb-8f7b-5d499fc036ff.gif" width = "400px"/>
</h1>
</p>

### ➡ Selecionando algoritmo
⚠ **SEMPRE CLIQUE EM `ATUALIZAR ENTRADAS` APÓS SELECIONAR O ALGORITMO** ⚠
<p>
<h1 align="center">
    <img title="Tela Inicial" src="https://user-images.githubusercontent.com/57163905/116348616-cece7e80-a7c4-11eb-85eb-9817bd6d55f9.gif" width = "400px"/>
</h1>
</p>

### ➡ Adicionando processos
**PREENCHA OS DADOS REQUISITADOS POR CADA ALGORITMO E CLIQUEM EM `ADICIONAR` PARA INSERIR UM NOVO PROCESSO NA FILA**
<p>
<h1 align="center">
    <img src="https://user-images.githubusercontent.com/57163905/116647255-775d1980-a950-11eb-9dd2-c16bc44de48d.gif" width = "300px"/>
</h1>
</p>

### ➡ Simulando o funcionamento do algoritmo
**APÓS ADICIONAR OS PROCESSOS, CLIQUE EM `SIMULAR` PARA DAR INÍCIO A UMA SIMULAÇÃO DO ALGORITMO SELECIONADO**
- 🔴 PROCESSO EM EXECUÇÃO
- 🟡 PROCESSO PAUSADO / NÃO FINALIZADO
- 🟢 PROCESSO FINALIZADO
<p>
<h1 align="center">
    <img src="https://user-images.githubusercontent.com/57163905/116647388-cd31c180-a950-11eb-99ae-67c7ef79c155.gif" width = "250px"/>
</h1>
</p>

### ➡ Visualizando Resultados
- **CLIQUE NA ABA `RESULTADOS` PARA VISUALIZAR OS DADOS GERADOS PELA SIMUAÇÃO**
- **CLIQUE NA ABA `GRÁFICO` PARA VISUALIZAR O GRÁFICO DE GANTT GERADO PELA SIMUAÇÃO**
<p>
<h1 align="center">
    <img src="https://user-images.githubusercontent.com/57163905/116646913-aaeb7400-a94f-11eb-90b3-528a8f255cd1.gif" width = "400px"/>
</h1>
</p>

## Algoritmos de Escalonmaento
* Funções do escalonamento:
    * Manter a CPU ocupada a maior parte do tempo.
    * Balancear a utilização do processador entre diversos processos.
    * Maximizar o throughput do sistema
    * Oferecer tempos de respostas razoáveis para os usuários interativos.
    * Evitar starvation.
    
* Gráfico de Gantt:
    O gráfico mostra visualmente a ordem e o tempo de execução de cada processo de acordo com o algoritmo que foi selecuionado
    
* Tempo de Espera:  
    Soma dos períodos em que o processo estava no seu estado pronto.
    
* Tempo de Turnaround:
    Tempo transcorrido desde o momento em que o software entra e o instante em que termina sua execução.
    
## FCFS
`First come, First Served:` Primeiro que chega será o primeiro a ser executado.

`Demonstração:`

<p>
<h1 align="center">
    <h4>Simulação</h4><br>
    <img src="https://user-images.githubusercontent.com/57163905/116646024-737bc800-a94d-11eb-9df5-571ffc799e8d.gif" width = "400px"/>
    <h4>Resultados Obtidos</h4>
    <img src="https://user-images.githubusercontent.com/57163905/116646126-b50c7300-a94d-11eb-8a28-fd9cbca0dcb1.png" width = "400px"/>
    <h4>Gráfico de Gantt do escalonamento dos processos</h4>
    <img src="https://user-images.githubusercontent.com/57163905/116646158-c9507000-a94d-11eb-83d7-884fd475b3a8.png" width = "400px"/><br>
</h1>
</p>

## SJFS
`Shortest Job First:` Menor processo ganhará a CPU e atrás do mesmo formar uma fila de processos por ordem crescente de tempo de execução, não-preemptivo.

`Demonstração:`

<p>
<h1 align="center">
    <h4>Simulação</h4><br>
    <img src="https://user-images.githubusercontent.com/57163905/116715261-ec5e3c80-a9ac-11eb-9944-e3c0eb4f6afb.gif" width = "400px"/>
    <h4>Resultados Obtidos</h4>
    <img src="https://user-images.githubusercontent.com/57163905/116715348-013ad000-a9ad-11eb-8e26-527b56252cda.png" width = "400px"/>
    <h4>Gráfico de Gantt do escalonamento dos processos</h4>
    <img src="https://user-images.githubusercontent.com/57163905/116715397-0c8dfb80-a9ad-11eb-94ef-7e9879672bfc.png" width = "400px"/><br>
</h1>
</p>



## Prioridade
- Processos possuem diferentes prioridades de execução.
- Processos de maior prioridade são escalonados preferencialmente.
- Mediante um quantum, que interrompe o processador em determinados intervalos de tempo, reavaliando prioridades e, possivelmente, escalonando outro processo.
- Prioridade estática.

`Demonstração:`

<p>
<h1 align="center">
    <h4>Simulação</h4><br>
    <img src="https://user-images.githubusercontent.com/57163905/116715784-65f62a80-a9ad-11eb-9182-8c28722e0452.gif" width = "400px"/>
    <h4>Resultados Obtidos</h4>
    <img src="https://user-images.githubusercontent.com/57163905/116715834-75757380-a9ad-11eb-833e-59c68af81625.png" width = "400px"/>
    <h4>Gráfico de Gantt do escalonamento dos processos</h4>
    <img src="https://user-images.githubusercontent.com/57163905/116715884-81f9cc00-a9ad-11eb-9406-48677df25fd5.png" width = "400px"/><br>
</h1>
</p>

## Loteria
Processo com maior token (prioridade) sorteado ganha a vez na CPU.  

`Demonstração:`

<p>
<h1 align="center">
    <h4>Simulação</h4><br>
    <img src="https://user-images.githubusercontent.com/57163905/116716080-b66d8800-a9ad-11eb-8c53-d7a50e3a08a1.gif" width = "400px"/>
    <h4>Resultados Obtidos</h4>
    <img src="https://user-images.githubusercontent.com/57163905/116716136-c71dfe00-a9ad-11eb-8bf2-1d9eb656765a.png" width = "400px"/>
    <h4>Gráfico de Gantt do escalonamento dos processos</h4>
    <img src="https://user-images.githubusercontent.com/57163905/116716175-d3a25680-a9ad-11eb-9fdd-0354454b8a5a.png" width = "400px"/><br>
</h1>
</p>



## Round Robin
- Caso quantum acabe e o processo não terminou: processo é inserido no fim da fila.
- Caso o processo termina antes de um quantum: a CPU é liberada para a execução de novos processos.

`Demonstração:`

<p>
<h1 align="center">
    <h4>Simulação</h4><br>
    <img src="https://user-images.githubusercontent.com/57163905/116716386-12381100-a9ae-11eb-8526-969a981fce2e.gif" width = "400px"/>
    <h4>Resultados Obtidos</h4>
    <img src="https://user-images.githubusercontent.com/57163905/116716425-1e23d300-a9ae-11eb-8448-946c0b113ae1.png" width = "400px"/>
    <h4>Gráfico de Gantt do escalonamento dos processos</h4>
    <img src="https://user-images.githubusercontent.com/57163905/116716468-2b40c200-a9ae-11eb-8e6f-4f8ef091029f.png" width = "400px"/><br>
</h1>
</p>


## Múltiplas Filas
- Cada processo é colocado em uma fila, e cada fila tem uma política de escalonamento própria e outra entre filas.
- Cada fila tem um determinado nível de prioridade.
- Sem realimentação.

`Demonstração:`

<p>
<h1 align="center">
    <h4>Simulação</h4><br>
    <img src="https://user-images.githubusercontent.com/57163905/116717091-e5382e00-a9ae-11eb-84bd-556ca2231043.gif" width = "400px"/>
    <h4>Resultados Obtidos</h4>
    <img src="https://user-images.githubusercontent.com/57163905/116717144-f6813a80-a9ae-11eb-8381-0d2ca95dcaf0.png" width = "400px"/>
    <h4>Gráfico de Gantt Fila 1 (FCFS)</h4>                             
    <img src="https://user-images.githubusercontent.com/57163905/116717285-19abea00-a9af-11eb-8cb5-5e8929fcfb85.png" width = "400px"/>
    <h4>Gráfico de Gantt Fila 2 (Round Robin)</h4>
    <img src="https://user-images.githubusercontent.com/57163905/116717445-43fda780-a9af-11eb-8cb9-52ee03dc68da.png" width = "400px"/><br>
</h1>
</p>

## Garantido
Garante aos processos sua execução, dando a todos eles a mesma quantidade de tempo de execução utilizando a CPU.

`Demonstração:`

<p>
<h1 align="center">
    <h4>Simulação</h4><br>
    <img src="https://user-images.githubusercontent.com/57163905/116716740-7bb81f80-a9ae-11eb-9a9e-3bd70cf6a2aa.gif" width = "400px"/>
    <h4>Resultados Obtidos</h4>
    <img src="https://user-images.githubusercontent.com/57163905/116716790-8c689580-a9ae-11eb-933c-c05a81d8a2e9.png" width = "400px"/>
    <h4>Gráfico de Gantt do escalonamento dos processos</h4>
    <img src="https://user-images.githubusercontent.com/57163905/116716836-98ecee00-a9ae-11eb-911f-29a8a30464ea.png" width = "400px"/><br>
</h1>
</p>


## 🛠 Ferramentas Utilizadas

- 🔗[Python](https://www.python.org/)
- 🔗[PySimpleGUI](https://pypi.org/project/PySimpleGUI/)
- 🔗[Matplotlib](https://matplotlib.org/)

## Referências ✔

- 🔗[GSIGMA - UFSC](https://www.gsigma.ufsc.br/~popov/aulas/so1/cap8so.html)
- 🔗[Escalonamento de Processos - Alex Coletta](https://alexcoletta.eng.br/artigos/escalonamento-de-processos/#:~:text=Escalonamento%20de%20processos%20%C3%A9%20o,qual%20ser%C3%A1%20colocado%20em%20execu%C3%A7%C3%A3o.)
- 🔗[Scheduling (computing)](https://en.wikipedia.org/wiki/Scheduling_(computing))
- 🔗[Escalonamento de processos](https://pt.wikipedia.org/wiki/Escalonamento_de_processos)

## Autor👨🏼‍💻

<p align="center">
    <a align="center" href="https://pedro-pauletti.github.io/pedropauletti.github.io/"><img src="https://user-images.githubusercontent.com/57163905/116717987-e0c04500-a9af-11eb-835f-81939e7c8bf1.jpeg" width = "150px"></a>
    <h3 align="center">Pedro Pauletti</h3>
</p>

