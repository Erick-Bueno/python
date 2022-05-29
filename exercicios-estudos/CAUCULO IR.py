from curses import window
from weakref import finalize
import PySimpleGUI as sg


def JanelaLogin():
    sg.theme("Reddit")
    layout = [
        [sg.Text("Nome")],
        [sg.Input()],
        [sg.Button('Next')]
 ]
    return sg.Window('Tela login', layout, finalize=True)


def segundajanela():
    sg.theme("Reddit")
    layout = [
        [sg.Text("Idade"),sg.Input()],
        [sg.Text("Sexo"),sg.Input()]
        [sg.Button('Concluir')]
]
    return sg.Window('Tela Informações', layout, finalize=True)

janela1, janela2 = JanelaLogin(), None

while True:
    janela, evento, valores = sg.read_all_windows()
    if janela == janela1 and evento == sg.WIN_CLOSED:
        break
    if janela == janela1 and evento == 'Next':
        janela2 = segundajanela()
        janela1.hide() #esconde a janela anterior


    
    

    






