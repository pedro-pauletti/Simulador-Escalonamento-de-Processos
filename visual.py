import PySimpleGUI as sg
sg.theme('Dark Grey 1')

numProcesso = 1
data = [['', '', '']]
filas = [['', '', '']]
headings = ["Processo", "Tempo de Execução", "Prioridade"]
headingsFila = ["Fila", "Quantum", "Algoritmo"]

menu = [['&Aplicação', ['Sair']],
        ['&Ajuda', ['&Sobre']] ]

left_col = [[sg.Text('Selecione um Algoritmo:', size=(20,1), key='Selecione um Algoritmo'), 
                sg.Combo(values=('FCFS', 'SJFS', 'Prioridade', 'Loteria', 'Round Robin', 'Múltiplas Filas', 'Garantido'), default_value='FCFS', key = 'algoritmos'),
                sg.Button('❓', key = 'ajuda')],
                [sg.Button('Atualizar Entradas', key = 'Salvar')],
            [sg.HorizontalSeparator()],
            [sg.Text('PROCESSOS', font=("Helvetica", 11))],
            [sg.Table(values=data, headings=headings,
                                auto_size_columns=True,
                                display_row_numbers=False,
                                justification='center',
                                num_rows= 6,
                                key='-TABLE-',
                                row_height=25,      
                                )],
            [sg.HorizontalSeparator(key = 'barra1')],
            [sg.Text(f'Processo {numProcesso}:', font=("Helvetica", 11), justification='center', key = 'processoNum')],
            [sg.Text('Tempo de Execução:', font=("Helvetica", 11)), sg.Spin([i for i in range(0,999)], initial_value=0, size=(5, 5), key = 'tempoExec')],
            [sg.Text('Prioridade:', font=("Helvetica", 11), key = 'textPrioridade'), sg.Spin([i for i in range(0,999)], initial_value=0, size=(5, 5), key = 'prioridade')],
            [sg.Button('Adicionar', key ='Adicionar')],
            [sg.HorizontalSeparator(key = 'barra2')],
            [sg.Text('Quantum:', font=("Helvetica", 11)), sg.Slider(range=(0, 20), orientation='h', key='quantum', size=(20, 15))],
            [sg.HorizontalSeparator(key = 'barra3')],
            [sg.Text('FILAS', font=("Helvetica", 11), key = 'filas', justification='center')],
            [sg.Table(values=filas, headings=headingsFila,
                                auto_size_columns=True,
                                display_row_numbers=False,
                                justification='center',
                                num_rows= 6,
                                key='-TABLEFILA-',
                                row_height=25,      
                                )],
                [sg.Text('Quantum Fila:', font=("Helvetica", 11)), sg.Spin([i for i in range(0,999)], initial_value=0, size=(5, 5), key = 'quantumFila')],
            [sg.Text('Algoritmo da Fila:', size=(20,1), key='algoritmoFila'), 
                sg.Combo(values=('FCFS', 'SJFS', 'Round Robin'), default_value='FCFS', key = 'algoritmosFila')],
            [sg.Button('Adicionar Fila', key = 'adicionaFila')]]

#[sg.Text('Tempo de Chegada:', font=("Helvetica", 11)), sg.Spin([i for i in range(0,999)], initial_value=0, size=(5, 5), key = 'tempoChegada')],
#[sg.Text('Quantum:'), sg.Spin([i for i in range(0,999)], initial_value=0, size=(5, 5), key = 'quantum')],
right_col = [
                [sg.Button('Resetar', key = 'Resetar'), sg.Button('Simular')],
                [sg.Frame('SIMULAÇÃO',[[sg.Text('Estados de execução:', size=(20,1), font=("Helvetica", 11)), sg.Button('❓', key = 'estados')]], key='-COL1-', font=("Helvetica", 13),)],
                [sg.HorizontalSeparator()],
                [sg.Text('Tempo de Execução do Processo:', size=(25, 1), font=("Helvetica", 11))],       
                [sg.ProgressBar(100, orientation='h', size=(20,20), key='-PROG-')],
                [sg.Output(size=(30, 20), key='-OUTPUT-')],
                [sg.Button('Limpar', key = 'Limpar')]
                ]
#

headings2 = ["Processo", "Prioridade", "T.Execução", "T.Espera", "T.Turnround"]
resultados = []

resultados_layout = [[sg.Text('PROCESSOS', font=("Helvetica", 16))],
            [sg.Table(values=resultados, headings=headings2,
                                auto_size_columns=False,
                                display_row_numbers=False,
                                justification='center',
                                num_rows= 10,
                                key='-TABLE2-',
                                row_height=25, col_widths = 100,
                                font=("Helvetica", 13),
                                )],
                    [sg.HorizontalSeparator()],
                    [sg.Text("Tempo de Execução Total: ", font=("Helvetica", 16), size=(38, 1), key = 'tempoExecTotal')],
                    [sg.HorizontalSeparator()],
                    [sg.Text("Tempo de Espera Médio: ", font=("Helvetica", 16), size=(38, 1), key = 'tempoEsperaMedio')],
                    [sg.HorizontalSeparator()],
                    [sg.Text("Tempo Médio de Turnaround: ", font=("Helvetica", 16), size=(38, 1), key = 'tempoMedioTurnaround')]
                                ]

# Define the window's contents
escolha_layout = [[sg.Menu(menu, key='-MENU-')],
            [sg.Column(left_col, element_justification='c'), sg.VSeperator(),sg.Column(right_col, element_justification='c')]
            ]


grafico_layout = [[sg.Image(key= 'gantt')]]

layout = [[sg.Text('Simulador Escalonamento de Processos', size=(38, 1), justification='center', font=("Helvetica", 16), relief=sg.RELIEF_RIDGE, k='-TEXT HEADING-', enable_events=True)]]
layout +=[[sg.TabGroup([[sg.Tab('Simulação', escolha_layout),
                        sg.Tab('Resultados', resultados_layout),
                        sg.Tab('Gráfico', grafico_layout, key='grafico'),]], key='-TAB GROUP-')]]

