#Encriptar qualquer arquivo selecionado usando a Linguagem Python com as bibliotecas criptography, PySimpleGUI e os
import PySimpleGUI as sg
from cryptography.fernet import Fernet
import os

#Função para criptografar com uma senha
def encriptarFicheiro(file_path, password):
    try:
        #Verificar se o arquivo existe
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f'O arquivo não existe!: {file_path}')

        #Extrair a extensão do arquivo original
        file_name, file_extension = os.path.splitext(file_path)
        #Ler o conteúdo do arquivo
        with open(file_path, 'rb') as file:
            file_data = file.read()

        #Gerar uma chave a partir da senha
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        #Criptografat os dados
        encrypted_data = cipher_suite.encrypt(file_data)
        #Salvar os dados criptografados em um novo arquivo com a mesma extensão
        encrypted_file_path = file_name + f'.{file_extension}'
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)
        return encrypted_file_path
    except Exception as e:
        return None

layout = [
    [sg.Text('Selecione um arquivo para criptografar: ')],
    [sg.InputText(key='file_path'), sg.FileBrowse()],
    [sg.Text('Digite uma senha: ')],
    [sg.InputText(key='password', password_char='●')],
    [sg.Button('Criptografar'), sg.Exit()]
]

window = sg.Window('Criptografar Arquivo', layout)
while True:
    event, valores = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Criptografar':
        file_path = valores['file_path']
        password = valores['password']
        if file_path and password:
            encrypted_file_path = encriptarFicheiro(file_path, password)
            if encrypted_file_path:
                sg.popup(f'Arquivo criptografado com sucesso: {encrypted_file_path}. A palavra-passe foi {password}')
            else:
                sg.popup('Erro ao criptografar o arquivo! Certifique-se de que o arquivo existe e a senha é válida!')

window.close()
