from collections import deque
import time
import sys
import os
clear = lambda: os.system('cls')
from random import randint
import PySimpleGUI as sg
import visual as vs
import webbrowser
import matplotlib.pyplot as plt
import os.path
import PIL.Image
import io
import base64

def LEDIndicator(key=None, metadata = None, radius=30):
    return sg.Graph(canvas_size=(radius, radius),
             graph_bottom_left=(-radius, -radius),
             graph_top_right=(radius, radius),
             pad=(0, 0), key=key, metadata = metadata)

def SetLED(window, key, color):
    graph = window[key]
    graph.erase()
    graph.draw_circle((0, 0), 17, fill_color=color, line_color=color)

def delLED(window, key):
    graph = window[key]
    graph.erase()

numProcesso = 1
numFilas = 0
data = [['', '', '']]
processos = []
filas = [['', '', '']]
usuarios = [['', '', '']]
exec = 0
num = 0
resultados = []


# Create the window
window = sg.Window('Simulador de Escalonador de Processos', vs.layout, default_element_size=(15, 1), auto_size_text=False, finalize=True, icon = 'icone.ico')


class Processo:

    def __init__(self, id, tempo, prioridade):
        self.id = id
        self.tempo = tempo
        self.prioridade = prioridade
        self.tempoEspera = 0
        self.turnaround = 0

    def __repr__(self):
        return str(self.tempo)

    def get_id(self): 
        return self.id

    def get_tempo(self): 
        return self.tempo

    def get_prioridade(self): 
        return self.prioridade

   # def get_chegada(self): 
       #return self.chegada

    def set_prioridade(self, prioridade): 
       self.prioridade = prioridade

def convert_to_bytes(file_or_bytes, resize=None):
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
        except Exception as e:
            dataBytesIO = io.BytesIO(file_or_bytes)
            img = PIL.Image.open(dataBytesIO)

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height/cur_height, new_width/cur_width)
        img = img.resize((int(cur_width*scale), int(cur_height*scale)), PIL.Image.ANTIALIAS)
    with io.BytesIO() as bio:
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()

def calculaTurnround(processos, temposEspera):
    temposTurnaroud = [0] * len(processos)

    for i in range(len(processos)):
        temposTurnaroud[i] = processos[i].tempo + temposEspera[i]
    
    return temposTurnaroud

def imprimirResultados(processos, tempoTotal, temposEspera, temposTurnaroud):
    
    window['tempoExecTotal'].update(f'Tempo de Execução Total: {tempoTotal} segundos')
    window['tempoEsperaMedio'].update(f'Tempo de Espera Média: {sum(temposEspera)/len(processos):.2f} segundos')
    window['tempoMedioTurnaround'].update(f'Tempo Médio de Turnaround: {sum(temposTurnaroud)/len(processos):.2f} segundos')

    for i in range(len(processos)):
        processos[i].tempoEspera = temposEspera[i]
        processos[i].turnaround = temposTurnaroud[i]

    for i in range(len(processos)):
        resultados.append([processos[i].id , processos[i].prioridade, processos[i].tempo, processos[i].tempoEspera, processos[i].turnaround])
        values['-TABLE2-'] = resultados
        window['-TABLE2-'].update(values['-TABLE2-'])

def imprimirResultadosGarantido(processos, tempoTotal, temposEspera, temposTurnaroud, temposIniciais):
    
    window['tempoExecTotal'].update(f'Tempo de Execução Total: {tempoTotal} segundos')
    window['tempoEsperaMedio'].update(f'Tempo de Espera Média: {sum(temposEspera)/len(processos):.2f} segundos')
    window['tempoMedioTurnaround'].update(f'Tempo Médio de Turnaround: {sum(temposTurnaroud)/len(processos):.2f} segundos')

    for i in range(len(processos)):
        processos[i].tempoEspera = temposEspera[i]
        processos[i].turnaround = temposTurnaroud[i]
        processos[i].tempo = temposIniciais[i]

    for i in range(len(processos)):
        resultados.append([processos[i].id , processos[i].prioridade, processos[i].tempo, processos[i].tempoEspera, processos[i].turnaround])
        values['-TABLE2-'] = resultados
        window['-TABLE2-'].update(values['-TABLE2-'])

def imprimirResultadosFila(processos):

    tempoTotal = 0
    tempoEspera = 0
    tempoTurnaroud = 0

    for i in range(len(processos)):
        tempoTotal += processos[i].tempo
        tempoEspera += processos[i].tempoEspera
        tempoTurnaroud += processos[i].turnaround

    window['tempoExecTotal'].update(f'Tempo de Execução Total: {tempoTotal} segundos')
    window['tempoEsperaMedio'].update(f'Tempo de Espera Média: {tempoEspera/len(processos):.2f} segundos')
    window['tempoMedioTurnaround'].update(f'Tempo Médio de Turnaround: {tempoTurnaroud/len(processos):.2f} segundos')

def executaFila(processos):
    tempoTotal = 0
    temposEspera = [0] * len(processos)
    nomesProcessos = []
    tempoExec = 0
    numProcessos = 0

    for i in range(len(processos)):
        tempoTotal += processos[i].tempo
        nomesProcessos.append(processos[i].id)


    fig, gnt = plt.subplots()
    
    gnt.set_ylim(0, len(processos) * 15)
    
    gnt.set_xlim(0, tempoTotal)
    
    gnt.set_xlabel('Segundos')
    gnt.set_ylabel('Processos')
    
    yticks = []
    v = 5
    for i in range(len(processos)):
        v += 10
        yticks.append(v)

    gnt.set_yticks(yticks)
    
    gnt.set_yticklabels(nomesProcessos)
    
    gnt.grid(False)
    
    for i in range(len(processos)):
   
        if(i > 0):
            temposEspera[i] += tempoExec

        print("--->Processo", processos[i].id ,": Em execução...")
        executaProcesso(processos[i].tempo, processos[i].id)
        numProcessos += 1
        gnt.broken_barh([(tempoExec, processos[i].tempo)], (numProcessos * 10, 9), facecolors =('tab:green'))
        tempoExec += processos[i].tempo
        
        print("--->Processo", processos[i].id,": FINALIZADO\n")


    temposTurnaroud = calculaTurnround(processos, temposEspera)

    imprimirResultados(processos, tempoTotal, temposEspera, temposTurnaroud)

    plt.savefig("gantt.png")
    window['gantt'].update(data=convert_to_bytes("gantt.png"))

def FCFS(processos): 
    #First come, first served ->  primeiro que chega será o primeiro a ser executado
    executaFila(processos)

def SJFS(processos): 
    #Shortest Job First -> menor processo ganhará a CPU e atrás do mesmo formar uma fila de processos por ordem crescente de tempo de execução, não-preemptivo
    processos = sorted(processos, key = Processo.get_tempo)
    executaFila(processos)

def prioridade(processos, quantum):
    #Processos possuem diferentes prioridades de execução.
    #Processos de maior prioridade são escalonados preferencialmente.
    #Mediante um clock, que interrompe o processador em determinados intervalos de tempo, reavaliando prioridades e, possivelmente, escalonando outro processo
    #Prioridade estática
    tempoTotal = 0
    nomesProcessos = []
    for i in range(len(processos)):
        tempoTotal += processos[i].tempo
        nomesProcessos.append(processos[i].id)

    fig, gnt = plt.subplots()
    
    gnt.set_ylim(0, len(processos) * 15)
    
    gnt.set_xlim(0, tempoTotal)
    
    gnt.set_xlabel('Segundos')
    gnt.set_ylabel('Processos')
    
    yticks = []
    v = 5
    for i in range(len(processos)):
        v += 10
        yticks.append(v)

    gnt.set_yticks(yticks)
    
    gnt.set_yticklabels(nomesProcessos)
    
    gnt.grid(False)
    

    processos = sorted(processos, key = Processo.get_prioridade)
    filaExec = [0] * len(processos) #fila com tempos de execução
    
    for i in range(len(processos)):
        filaExec[i] = processos[i].tempo
   
    tempoTotal = sum(filaExec)
    temposEspera = [0] * len(processos)
    tempoExec = 0

    while(1): #Encontar os tempos de espera de cada processo
        
        done = True
        for i in range(len(processos)):
            if (filaExec[i] > 0):
                done = False

                if(filaExec[i] > quantum):

                    gnt.broken_barh([(tempoExec, quantum)], (int(processos[i].id) * 10, 9), facecolors =('tab:green'))
                    tempoExec += quantum
                    filaExec[i] -= quantum
                    print("--->Processo", processos[i].id ,": Em execução...")
                    executaProcessoRR(quantum, processos[i].id)
                    
                else:
                    processos = sorted(processos, key = Processo.get_prioridade)

                    gnt.broken_barh([(tempoExec, quantum)], (int(processos[i].id) * 10, 9), facecolors =('tab:green'))
                    tempoExec += filaExec[i]
                    temposEspera[i] = tempoExec - processos[i].tempo
                    print("--->Processo", processos[i].id ,": Em execução")
                    executaProcessoRR(filaExec[i], processos[i].id)
                    print()
                    filaExec[i] = 0
                    SetLED(window, str(processos[i].id), 'green')
                    print("--->Processo", processos[i].id,": FINALIZADO\n")
        if (done == True):
            break

    temposTurnaroud = calculaTurnround(processos, temposEspera)
    
    imprimirResultados(processos, tempoTotal, temposEspera, temposTurnaroud)

    plt.savefig("gantt.png")
    window['gantt'].update(data=convert_to_bytes("gantt.png"))

def loteria(processos):
    #Processo com maior token sorteado ganha a vez na CPU
    for i in range(len(processos)):
        processos[i].set_prioridade(randint(1,len(processos)))
    processos = sorted(processos, key = Processo.get_prioridade)
    executaFila(processos)

def roundRobin(processos, quantum):
    #Caso quantum acabe e o processo não terminou: processo é inserido no fim da fila
    #Caso o processo termina antes de um quantum: a CPU é liberada para a execução de novos processos
    tempoTotal = 0
    nomesProcessos = []
    for i in range(len(processos)):
        tempoTotal += processos[i].tempo
        nomesProcessos.append(processos[i].id)

    fig, gnt = plt.subplots()
    
    gnt.set_ylim(0, len(processos) * 15)
    
    gnt.set_xlim(0, tempoTotal)
    
    gnt.set_xlabel('Segundos')
    gnt.set_ylabel('Processos')
    
    yticks = []
    v = 5
    for i in range(len(processos)):
        v += 10
        yticks.append(v)

    gnt.set_yticks(yticks)
    
    gnt.set_yticklabels(nomesProcessos)
    
    gnt.grid(False)

    filaExec = [0] * len(processos) #fila com tempos de execução
    for i in range(len(processos)):
        filaExec[i] = processos[i].tempo
   
    tempoTotal = sum(filaExec)
    temposEspera = [0] * len(processos)
    tempoExec = 0

    while(1): #Encontar os tempos de espera de cada processo
        
        done = True
        for i in range(len(processos)):
            if (filaExec[i] > 0):
                done = False

                if(filaExec[i] > quantum):
                    gnt.broken_barh([(tempoExec, quantum)], (int(processos[i].id) * 10, 9), facecolors =('tab:green'))
                    tempoExec += quantum
                    filaExec[i] -= quantum
                    print("--->Processo", processos[i].id ,": Em execução...")
                    executaProcessoRR(quantum, processos[i].id)
                    print()
                    
                else:
                    gnt.broken_barh([(tempoExec, quantum)], (int(processos[i].id) * 10, 9), facecolors =('tab:green'))
                    tempoExec += filaExec[i]
                    temposEspera[i] = tempoExec - processos[i].tempo
                    print("--->Processo", processos[i].id ,": Em execução")
                    executaProcessoRR(filaExec[i], processos[i].id)
                    print()
                    filaExec[i] = 0
                    SetLED(window, str(processos[i].id), 'green')
                    print("--->Processo", processos[i].id,": FINALIZADO\n")
        if (done == True):
            break

    temposTurnaroud = calculaTurnround(processos, temposEspera)
    
    imprimirResultados(processos, tempoTotal, temposEspera, temposTurnaroud)

    plt.savefig("gantt.png")
    window['gantt'].update(data=convert_to_bytes("gantt.png"))

def multiplasFilas(processos, numFilas, filas): #sem realimentacao

    processosFila = [[] for i in range(numFilas)]
    k = 0

    for i in range(numFilas):
        for j in range(len(processos)):
            if processos[j].prioridade == (i+1):
                processosFila[k].append(processos[j])
        k += 1     

    for i in range(len(filas)):
        print(f'-->FILA {i+1} - {filas[i][2]}')

        if filas[i][2] == 'FCFS':
            FCFS(processosFila[i])
        
        if filas[i][2] == 'SJFS':
            SJFS(processosFila[i])

        if filas[i][2] == 'Round Robin':
            roundRobin(processosFila[i], filas[i][1])

    imprimirResultadosFila(processos)

def garantido(processos, usuarios, quantum):
    tempoTotal = 0
    nomesProcessos = []
    for i in range(len(processos)):
        tempoTotal += processos[i].tempo
        nomesProcessos.append(processos[i].id)

    fig, gnt = plt.subplots()
    
    gnt.set_ylim(0, len(processos) * 15)
    
    gnt.set_xlim(0, tempoTotal)
    
    gnt.set_xlabel('Segundos')
    gnt.set_ylabel('Processos')
    
    yticks = []
    v = 5
    for i in range(len(processos)):
        v += 10
        yticks.append(v)

    gnt.set_yticks(yticks)
    
    gnt.set_yticklabels(nomesProcessos)
    
    gnt.grid(False)
    

    processosUsuarios = [[] for i in range(usuarios)]
    k = 0
    executados = len(processos)

    tempoTotal = 0
    temposEspera = [0] * len(processos)
    temposIniciais = [0] * len(processos)
    tempoExec = 0
    l = 0

    for i in range(len(processos)):
        tempoTotal += processos[i].tempo
        temposIniciais[i] += processos[i].tempo

    for i in range(usuarios):
        for j in range(len(processos)):
            if processos[j].prioridade == (i+1):
                processosUsuarios[k].append(processos[j])
        k += 1     

    
    while (executados > 0):
        for i in range(len(processosUsuarios)):
            for j in range(len(processosUsuarios[i])):

                if (processosUsuarios[i][j].tempo > 0):
                    gnt.broken_barh([(tempoExec, (quantum/usuarios)/len(processosUsuarios[i]))], (int(processosUsuarios[i][j].id) * 10, 9), facecolors =('tab:green'))
                    print("--->Processo", processosUsuarios[i][j].id ,": Em execução...\n")
                    executaProcessoRR((quantum/usuarios)/len(processosUsuarios[i]), processosUsuarios[i][j].id)
                    tempoExec += (quantum/usuarios)/len(processosUsuarios[i])
                    processosUsuarios[i][j].tempo -= (quantum/usuarios)/len(processosUsuarios[i])
                    if(processosUsuarios[i][j].tempo == 0):
                        temposEspera[l] = tempoExec - temposIniciais[i + j]
                        l += 1
                        print("--->Processo", processosUsuarios[i][j].id,": FINALIZADO\n")
                        SetLED(window, str(processosUsuarios[i][j].id), 'green')
                        executados -= 1
    
   
    temposTurnaroud = [0] * len(processos)

    for i in range(len(processos)):
        temposTurnaroud[i] = temposIniciais[i] + temposEspera[i]

    imprimirResultadosGarantido(processos, tempoTotal, temposEspera, temposTurnaroud, temposIniciais)
    
    plt.savefig("gantt.png")
    window['gantt'].update(data=convert_to_bytes("gantt.png"))
    
def executaProcesso(tempo, progressoId):

    SetLED(window, str(progressoId), 'red')
    j = 0
    for _ in range(10):
        time.sleep(tempo / 10)
        j += 10
        window['-PROG-'].update(j)
 
    SetLED(window, str(progressoId), 'green')

def executaProcessoRR(tempo, progressoId):

    SetLED(window, str(progressoId), 'red')
    j = 0
    for _ in range(10):
        time.sleep(tempo / 10)
        j += 10
        window['-PROG-'].update(j)
 
    SetLED(window, str(progressoId), 'yellow')    

def adicionaProcessos(numProcesso, tempoExec, prioridade):
    processos.append(Processo(numProcesso, tempoExec, prioridade))
    if (data[0] == ['','','']):
        data[0] = [str(numProcesso), tempoExec, prioridade]
    else:
        data.append([str(numProcesso), tempoExec, prioridade])

def adicionaFilas(numFilas, quantum, algoritmo):
    if (filas[0] == ['','','']):
        filas[0] = [str(numFilas+1), quantum, algoritmo]
    else:
        filas.append([str(numFilas+1), quantum, algoritmo])


window['tempoExec'].update(disabled = True)
window['prioridade'].update(disabled = True)
window['Adicionar'].update(disabled = True)
window['quantum'].update(disabled = True)
window['Simular'].update(disabled = True)
window['filas'].hide_row()
window['-TABLEFILA-'].hide_row()
window['quantumFila'].hide_row()
window['algoritmoFila'].hide_row()
window['algoritmosFila'].hide_row()
window['adicionaFila'].hide_row()



while True:
    window['processoNum'].update(f'Processo {numProcesso}:') #atualiza a numeração do processo a cada um que é adicionado

    if(exec == 0): #limpa ao abrir o simulador na primeira vez
        window['-OUTPUT-'].update('') 
        exec = 1

    event, values = window.read()

    
    if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Sair':
        break

    if event == 'Sobre':
        webbrowser.open('https://pt.duolingo.com/')

    if event == 'Adicionar':
        window.extend_layout(window['-COL1-'], [[sg.Text(f'Processo {numProcesso}:', key= f'-PL{num}-', font=("Helvetica", 11)), LEDIndicator(str(numProcesso))]])
        adicionaProcessos(numProcesso, values['tempoExec'], values['prioridade'])
        values['-TABLE-'] = data
        window['-TABLE-'].update(values['-TABLE-'])
        numProcesso += 1
        num += 1
        
    if event == 'adicionaFila':
        adicionaFilas(numFilas, values['quantumFila'], values['algoritmosFila'])
        values['-TABLEFILA-'] = filas
        window['-TABLEFILA-'].update(values['-TABLEFILA-'])
        numFilas += 1


    if event == 'ajuda':
        if values['algoritmos'] == 'FCFS':
            sg.popup('First come, first served',      
                'Primeiro que chega será o primeiro a ser executado',
                ) 
        
        if values['algoritmos'] == 'SJFS':
            sg.popup('Shortest Job First',      
                'Menor processo ganhará a CPU e atrás do mesmo formar uma fila de processos por ordem crescente de tempo de execução, não-preemptivo',   
                ) 

        if values['algoritmos'] == 'Prioridade':
           sg.popup('Prioridade',      
                    'Processos possuem diferentes prioridades de execução.',
                    'Processos de maior prioridade são escalonados preferencialmente.',
                    'Mediante um quantum, que interrompe o processador em determinados intervalos de tempo, reavaliando prioridades e, possivelmente, escalonando outro processo',
                    'Prioridade estática',
                ) 

        if values['algoritmos'] == 'Loteria':
            sg.popup('Algoritmo Loteria',      
                'Processo com maior token (prioridade) sorteado ganha a vez na CPU',   
                ) 

        if values['algoritmos'] == 'Round Robin':
            sg.popup('Algoritmo Round Robin',      
                'Caso quantum acabe e o processo não terminou: processo é inserido no fim da fila',
                'Caso o processo termina antes de um quantum: a CPU é liberada para a execução de novos processos',      
                )   

        if values['algoritmos'] == 'Múltiplas Filas':
            sg.popup('Algoritmo Múltiplas Filas',      
                'Cada processo é colocado em uma fila, e cada fila tem uma política de escalonamento própria e outra entre filas',
                'Cada fila tem um determinado nível de prioridade',      
                )   

    if event == 'estados':
        sg.popup('🔴 PROCESSO EM EXECUÇÃO',      
                '🟡 PROCESSO PAUSADO / NÃO FINALIZADO',
                '🟢 PROCESSO FINALIZADO',
                ) 

    if event == 'Simular':
        if values['algoritmos'] == 'FCFS':
            FCFS(processos)
        
        if values['algoritmos'] == 'SJFS':
            SJFS(processos)

        if values['algoritmos'] == 'Prioridade':
           prioridade(processos, values['quantum'])

        if values['algoritmos'] == 'Loteria':
            loteria(processos)

        if values['algoritmos'] == 'Round Robin':
            roundRobin(processos, values['quantum'])
        
        if values['algoritmos'] == 'Múltiplas Filas':
            multiplasFilas(processos, numFilas, filas)

        if values['algoritmos'] == 'Garantido':
            garantido(processos, 2, values['quantum'])


    if event == 'Salvar':
        if values['algoritmos'] == 'FCFS':
            window['tempoExec'].update(disabled = False)
            window['Adicionar'].update(disabled = False)
            window['Simular'].update(disabled = False)
            window['tempoExec'].update(disabled = False)
            window['prioridade'].update(disabled = True)
            window['quantum'].update(disabled = True)
            window['filas'].hide_row()
            window['-TABLEFILA-'].hide_row()
            window['quantumFila'].hide_row()
            window['algoritmoFila'].hide_row()
            window['algoritmosFila'].hide_row()
            window['adicionaFila'].hide_row()
            window['textPrioridade'].update('Prioridade')

           

        if values['algoritmos'] == 'SJFS':
            window['tempoExec'].update(disabled = False)
            window['Adicionar'].update(disabled = False)
            window['Simular'].update(disabled = False)
            window['prioridade'].update(disabled = True)
            window['quantum'].update(disabled = True)
            window['filas'].hide_row()
            window['-TABLEFILA-'].hide_row()
            window['quantumFila'].hide_row()
            window['algoritmoFila'].hide_row()
            window['algoritmosFila'].hide_row()
            window['adicionaFila'].hide_row()
            window['textPrioridade'].update('Prioridade')

        if values['algoritmos'] == 'Prioridade':
            window['tempoExec'].update(disabled = False)
            window['Adicionar'].update(disabled = False)
            window['Simular'].update(disabled = False)
            window['prioridade'].update(disabled = False)
            window['quantum'].update(disabled = False)
            window['quantum'].unhide_row()
            window['filas'].hide_row()
            window['-TABLEFILA-'].hide_row()
            window['quantumFila'].hide_row()
            window['algoritmoFila'].hide_row()
            window['algoritmosFila'].hide_row()
            window['adicionaFila'].hide_row()
            window['textPrioridade'].update('Prioridade')

        if values['algoritmos'] == 'Loteria':
            window['tempoExec'].update(disabled = False)
            window['Adicionar'].update(disabled = False)
            window['Simular'].update(disabled = False)
            window['prioridade'].update(disabled = True)
            window['quantum'].update(disabled = True)
            window['filas'].hide_row()
            window['-TABLEFILA-'].hide_row()
            window['quantumFila'].hide_row()
            window['algoritmoFila'].hide_row()
            window['algoritmosFila'].hide_row()
            window['adicionaFila'].hide_row()
            window['textPrioridade'].update('Prioridade')


        if values['algoritmos'] == 'Round Robin':
            window['tempoExec'].update(disabled = False)
            window['Adicionar'].update(disabled = False)
            window['Simular'].update(disabled = False)
            window['quantum'].update(disabled = False)
            window['prioridade'].update(disabled = True)
            window['quantum'].unhide_row()
            window['filas'].hide_row()
            window['-TABLEFILA-'].hide_row()
            window['quantumFila'].hide_row()
            window['algoritmoFila'].hide_row()
            window['algoritmosFila'].hide_row()
            window['adicionaFila'].hide_row()
            window['textPrioridade'].update('Prioridade')
        
        if values['algoritmos'] == 'Múltiplas Filas':
            window['tempoExec'].update(disabled = False)
            window['Adicionar'].update(disabled = False)
            window['Simular'].update(disabled = False)
            window['prioridade'].update(disabled = False)
            window['barra2'].hide_row()
            window['quantum'].hide_row()
            window['filas'].unhide_row()
            window['-TABLEFILA-'].unhide_row()
            window['quantumFila'].unhide_row()
            window['algoritmoFila'].unhide_row()
            window['algoritmosFila'].unhide_row()
            window['adicionaFila'].unhide_row()
            window['textPrioridade'].update('Fila')

        if values['algoritmos'] == 'Garantido':
            window['tempoExec'].update(disabled = False)
            window['Adicionar'].update(disabled = False)
            window['Simular'].update(disabled = False)
            window['tempoExec'].update(disabled = False)
            window['prioridade'].update(disabled = False)
            window['quantum'].update(disabled = False)
            window['filas'].hide_row()
            window['-TABLEFILA-'].hide_row()
            window['quantumFila'].hide_row()
            window['algoritmoFila'].hide_row()
            window['algoritmosFila'].hide_row()
            window['adicionaFila'].hide_row()
            window['textPrioridade'].update('Usuário')
       
    
    if event == 'Resetar':
        
        for i in range(num):
            window[f'-PL{i}-'].hide_row()
            
        for i in range(len(data)):
            delLED(window, data[i][0])

        data = [['', '', '']] 

        resultados = []
        processos = []
        window['-OUTPUT-'].update('')
        values['-TABLE-'] = data
        window['tempoExec'].update(0)
        window['prioridade'].update(0)
        window['quantum'].update(0)
        window['-TABLE-'].update(values['-TABLE-'])

    if event == 'Limpar':
        window['-OUTPUT-'].update('')
        for i in range(len(data)):
            delLED(window, data[i][0])
        
        
    # Output a message to the window
    #window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()