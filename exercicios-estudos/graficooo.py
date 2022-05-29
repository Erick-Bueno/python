
from weakref import finalize
import PySimpleGUI as sg


def JanelaLogin():
    sg.theme("Reddit")
    layout = [
        [sg.Text("Nome")],
        [sg.Input()],
        [sg.Button('Next')]
 ]
    return sg.Window('Cadastro', layout, finalize=True)


def segundajanela():
    sg.theme("Reddit")
    layout = [
        [sg.Text("Idade"),sg.Input()],
        [sg.Text("Sexo"),sg.Input()],
        [sg.Button('Concluir')],
        [sg.Button('Voltar')]
]
    return sg.Window('Tela Informações', layout, finalize=True)

janela1, janela2 = JanelaLogin(), None

while True:
    janela, evento, valores= sg.read_all_windows()
    if janela == janela1 and evento == sg.WIN_CLOSED:
        break
    if janela == janela2 and evento == sg.WINDOW_CLOSED:
        break
    if janela == janela1 and evento == 'Next':
        janela2 = segundajanela()
        janela1.hide() #esconde a janela anterior
    if janela == janela2 and evento == 'Voltar':
        janela1.un_hide() #tirar de escondida.
        janela2.hide()
    if janela == janela2 and evento == 'Concluir':
        sg.popup("Seu cadastro foi realizado com sucesso")