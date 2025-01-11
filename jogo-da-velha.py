import PySimpleGUI as sg

# Inicializar o tabuleiro
tabuleiro = [['' for _ in range(3)] for _ in range(3)]
jogador_atual = 'X'

# Função para verificar vitória
def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all([celula == jogador for celula in linha]):
            return True
    for col in range(3):
        if all([tabuleiro[linha][col] == jogador for linha in range(3)]):
            return True
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True
    return False

# Função para verificar empate
def verificar_empate(tabuleiro):
    return all([celula != '' for linha in tabuleiro for celula in linha])

# Função para atualizar o tabuleiro
def atualizar_tabuleiro(janela, tabuleiro):
    for linha in range(3):
        for col in range(3):
            janela[(linha, col)].update(tabuleiro[linha][col])

# Layout para a GUI
layout = [[sg.Button('', size=(6, 3), key=(linha, col)) for col in range(3)] for linha in range(3)]
layout.append([sg.Button('Reiniciar'), sg.Button('Sair')])

# Criar a janela
janela = sg.Window('Jogo da Velha', layout)

# Loop de eventos
while True:
    evento, valores = janela.read()
    if evento in (sg.WIN_CLOSED, 'Sair'):
        break
    if evento == 'Reiniciar':
        tabuleiro = [['' for _ in range(3)] for _ in range(3)]
        jogador_atual = 'X'
        atualizar_tabuleiro(janela, tabuleiro)
        continue
    if isinstance(evento, tuple):
        linha, col = evento
        if tabuleiro[linha][col] == '':
            tabuleiro[linha][col] = jogador_atual
            atualizar_tabuleiro(janela, tabuleiro)
            if verificar_vitoria(tabuleiro, jogador_atual):
                sg.popup(f'Jogador {jogador_atual} vence!')
                tabuleiro = [['' for _ in range(3)] for _ in range(3)]
                jogador_atual = 'X'
                atualizar_tabuleiro(janela, tabuleiro)
            elif verificar_empate(tabuleiro):
                sg.popup('Empate (Deu Velha)!')
                tabuleiro = [['' for _ in range(3)] for _ in range(3)]
                jogador_atual = 'X'
                atualizar_tabuleiro(janela, tabuleiro)
            else:
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'

janela.close()