
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

[![Foo](https://user-images.githubusercontent.com/57163905/116627466-96918200-a923-11eb-87ea-6c84def9d15e.png)](https://drive.google.com/file/d/1aux05brGhv8saMChXao-SsxKQgwoiPd-/view?usp=sharing)



### Simulador de Escalonamento de Processos com propósito educacional e didático, desenvolvido para a disciplina de Sistemas Operacionais l

<p>
<h1 align="center">
    <img title="Tela Inicial" src="assets/tela-inicial.png" width = "500px"/>
</h1>
</p>


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

Escalonamento de processos é o ato de realizar o chaveamento dos processos ativos, de acordo com regras bem estabelecidas, de forma que todos os processos tenham chance de utilizar a UCP. O escalonador é a parte do SO encarregada de decidir entre os processos prontos, qual será colocado em execução. A ideia de criar um simulador é para que estudantes e interessados possam compreender e analisar o funcionamento dos algoritmos de escalonamento de processos de forma simples, visual e didática. Todos os algoritmos foram desenvolvidos em Python. A interface foi concebida utilizando a biblioteca gráfica PySimpleGUI.![Ativo 3](https://user-images.githubusercontent.com/57163905/116627223-15d28600-a923-11eb-921d-aa50fba4628a.png)


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

### ➡ Simulando o funcionamento do algoritmo
**APÓS ADICIONAR OS PROCESSOS, CLIQUE EM `SIMULAR` PARA DAR INÍCIO A UMA SIMULAÇÃO DO ALGORITMO SELECIONADO**
- 🔴 PROCESSO EM EXECUÇÃO
- 🟡 PROCESSO PAUSADO / NÃO FINALIZADO
- 🟢 PROCESSO FINALIZADO

### ➡ Visualizando Resultados
**CLIQUE NA ABA `RESULTADOS` PARA VISUALIZAR OS DADOS GERADOS PELA SIMUAÇÃO**

## Algoritmos de Escalonmaento
* Funções do escalonamento:
    * Manter a CPU ocupada a maior parte do tempo.
    * Balancear a utilização do processador entre diversos processos.
    * Maximizar o throughput do sistema
    * Oferecer tempos de respostas razoáveis para os usuários interativos.
    * Evitar starvation.
    
## FCFS
`First come, First Served:` Primeiro que chega será o primeiro a ser executado.

Demonstração:


## SJFS
`Shortest Job First:` Menor processo ganhará a CPU e atrás do mesmo formar uma fila de processos por ordem crescente de tempo de execução, não-preemptivo.

`Demonstração:`


## Prioridade
- Processos possuem diferentes prioridades de execução.
- Processos de maior prioridade são escalonados preferencialmente.
- Mediante um quantum, que interrompe o processador em determinados intervalos de tempo, reavaliando prioridades e, possivelmente, escalonando outro processo.
- Prioridade estática.

`Demonstração:`

## Loteria
Processo com maior token (prioridade) sorteado ganha a vez na CPU.  

`Demonstração:`

## Round Robin
- Caso quantum acabe e o processo não terminou: processo é inserido no fim da fila.
- Caso o processo termina antes de um quantum: a CPU é liberada para a execução de novos processos.

`Demonstração:`


## Múltiplas Filas
- Cada processo é colocado em uma fila, e cada fila tem uma política de escalonamento própria e outra entre filas.
- Cada fila tem um determinado nível de prioridade.
- Sem realimentação.

`Demonstração:`

## Garantido
Garante aos processos sua execução, dando a todos eles a mesma quantidade de tempo de execução utilizando a CPU.

`Demonstração:`


## 🛠 Ferramentas Utilizadas

- 🔗[Python](https://www.python.org/)
- 🔗[PySimpleGUI](https://pypi.org/project/PySimpleGUI/)

## Referências ✔

- 🔗[GSIGMA - UFSC](https://www.gsigma.ufsc.br/~popov/aulas/so1/cap8so.html)
- 🔗[Escalonamento de Processos - Alex Coletta](https://alexcoletta.eng.br/artigos/escalonamento-de-processos/#:~:text=Escalonamento%20de%20processos%20%C3%A9%20o,qual%20ser%C3%A1%20colocado%20em%20execu%C3%A7%C3%A3o.)
- 🔗[Scheduling (computing)](https://en.wikipedia.org/wiki/Scheduling_(computing))
