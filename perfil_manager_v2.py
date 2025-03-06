"""
Gerenciador de Perfis

Este programa permite a introdução, modificação e listagem de perfis de pessoas. Cada perfil contém as seguintes informações:
- Nome (máximo de 50 letras)
- Peso (em kg, entre 6 e 200)
- Altura (em cm, entre 50 e 250)
- Idade (em anos, entre 1 e 120)
- Sexo (M ou F)

O programa oferece um menu principal com as seguintes opções:
1. Introduzir Perfil: Permite adicionar um novo perfil.
2. Modificar Perfil: Permite modificar um perfil existente.
3. Listar Perfis: Exibe todos os perfis introduzidos e permite salvar os dados em um arquivo (formato txt ou csv).
0. Sair do Programa: Encerra o programa.

Funções principais:
- menu(): Exibe o menu principal e retorna a escolha do usuário.
- introduzirNome(index): Solicita e armazena o nome de um perfil.
- introduzirPeso(index): Solicita e armazena o peso de um perfil.
- introduzirAltura(index): Solicita e armazena a altura de um perfil.
- introduzirIdade(index): Solicita e armazena a idade de um perfil.
- introduzirSexo(index): Solicita e armazena o sexo de um perfil.
- menu2(totalPerfis): Exibe o menu de modificação de perfis e retorna a escolha do usuário.
- menu3(index): Exibe o menu de modificação de um perfil específico e retorna a escolha do usuário.
- calculaTMB(index): Calcula a Taxa Metabólica Basal (TMB) de um perfil com base no peso, altura, idade e sexo.
- salvar_perfis(formato, contadorPerfis): Salva os perfis em um arquivo no formato especificado (txt ou csv).
- main(): Função principal que controla o fluxo do programa.

Constantes:
- MAXNOMES: Número máximo de perfis (10).
- MAXLETRAS: Número máximo de letras para cada nome (50).

Variáveis globais:
- nome: Lista 2D para armazenar os nomes dos perfis.
- peso: Lista para armazenar os pesos dos perfis.
- altura: Lista para armazenar as alturas dos perfis.
- idade: Lista para armazenar as idades dos perfis.
- sexo: Lista para armazenar os sexos dos perfis.
"""

# Definições de constantes
MAXNOMES = 10  # máximo de 10 nomes
MAXLETRAS = 50  # máximo de 50 letras para cada nome

# Declaração das variáveis ​​globais do programa, acessíveis por qualquer função do programa

# vetor 'nome' multidimensional (2D) de 10 x 50 elementos do tipo char, usado para salvar 10 nomes de 50 letras cada
nome = [[""] * MAXLETRAS for _ in range(MAXNOMES)]

# vetor 'peso' unidimensional (1D) de 10 elementos do tipo inteiro, usado para salvar o peso de cada perfil
peso = [0] * MAXNOMES

# vetor 'altura' unidimensional (1D) de 10 elementos do tipo inteiro, usado para salvar a altura de cada perfil
altura = [0] * MAXNOMES

# vetor 'idade' unidimensional (1D) de 10 elementos do tipo inteiro, usado para salvar a idade de cada perfil
idade = [0] * MAXNOMES

# vetor 'sexo' unidimensional (1D) de 10 elementos do tipo char, usado para salvar o sexo de cada perfil
sexo = [""] * MAXNOMES

def menu():
    while True:
        print("\n----- MENU PRINCIPAL ----")
        print("1 - Introduzir Perfil")
        print("2 - Modificar Perfil")
        print("3 - Listar Perfis")
        print("0 - Sair do Programa")
        print("-------------------------")
        escolha = input("Indique sua escolha --> ")
        if escolha.isdigit() and 0 <= int(escolha) <= 3:
            return int(escolha)
        print("Escolha Inválida! Escolha novamente.")

def introduzirNome(index):
    nome[index] = input(f"Introduza o nome da pessoa (máx. {MAXLETRAS} letras) --> ")[:MAXLETRAS]

def introduzirPeso(index):
    while True:
        peso_str = input(f"Introduza o peso para {nome[index]} (6 - 200 kg) --> ")
        if peso_str.isdigit():
            peso_val = int(peso_str)
            if 6 <= peso_val <= 200:
                peso[index] = peso_val
                break
        print("Escolha Inválida! Escolha novamente.")

def introduzirAltura(index):
    while True:
        altura_str = input(f"Introduza a altura para {nome[index]} (50 - 250 cm) --> ")
        if altura_str.isdigit():
            altura_val = int(altura_str)
            if 50 <= altura_val <= 250:
                altura[index] = altura_val
                break
        print("Escolha Inválida! Escolha novamente.")

def introduzirIdade(index):
    while True:
        idade_str = input(f"Introduza a idade para {nome[index]} (1 - 120 anos) --> ")
        if idade_str.isdigit():
            idade_val = int(idade_str)
            if 1 <= idade_val <= 120:
                idade[index] = idade_val
                break
        print("Escolha Inválida! Escolha novamente.")

def introduzirSexo(index):
    while True:
        sexo_str = input(f"Introduza o sexo para {nome[index]} (M/F) --> ").upper()
        if sexo_str in ["M", "F"]:
            sexo[index] = sexo_str
            break
        print("Escolha Inválida! Escolha novamente.")

def menu2(totalPerfis):
    while True:
        print("\n---- MODIFICAR PERFIL ----")
        for i in range(totalPerfis):
            print(f"{i + 1} - Alterar perfil de {nome[i]}")
        print("0 - Voltar ao menu principal")
        escolha = input("Indique sua escolha --> ")
        if escolha.isdigit() and 0 <= int(escolha) <= totalPerfis:
            return int(escolha)
        print("Escolha Inválida! Escolha nova.")

def menu3(index):
    while True:
        print("\n---- MODIFICAR PERFIL ----")
        print(f"1 - Alterar nome ({nome[index]})")
        print(f"2 - Alterar peso ({peso[index]} kg)")
        print(f"3 - Alterar altura ({altura[index]} cm)")
        print(f"4 - Alterar idade ({idade[index]} anos)")
        print(f"5 - Alterar sexo ({sexo[index]})")
        print("6 - Voltar ao menu principal")
        print("0 - Voltar ao menu anterior")
        escolha = input("Indique sua escolha --> ")
        if escolha.isdigit() and 0 <= int(escolha) <= 6:
            return int(escolha)
        print("Escolha Inválida! Escolha novamente.")

def calculaTMB(index):
    if sexo[index] == 'M':
        tmb = (10.0 * peso[index]) + (6.25 * altura[index]) - (5.0 * idade[index]) + 5
    else:
        tmb = (10.0 * peso[index]) + (6.25 * altura[index]) - (5.0 * idade[index]) - 161
    return tmb

def salvar_perfis(formato, contadorPerfis):
    import csv

    if formato == 'txt':
        with open("perfils.txt", "w") as file:
            file.write("NOME, PESO, ALTURA, IDADE, SEXO, TMB\n")
            for i in range(contadorPerfis):
                file.write(f"{nome[i]}, {peso[i]}, {altura[i]}, {idade[i]}, {sexo[i]}, {calculaTMB(i):.2f}\n")
    elif formato == 'csv':
        with open("perfils.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["NOME", "PESO", "ALTURA", "IDADE", "SEXO", "TMB"])
            for i in range(contadorPerfis):
                writer.writerow([nome[i], peso[i], altura[i], idade[i], sexo[i], f"{calculaTMB(i):.2f}"])

def main():
    contadorPerfis = 0
    while True:
        escolhaM1 = menu()
        if escolhaM1 == 0:
            break
        elif escolhaM1 == 1:
            if contadorPerfis == MAXNOMES:
                print("\n*** MAXIMO DE PERFIS ATINGIDO! ***")
            else:
                while True:
                    introduzirNome(contadorPerfis)
                    introduzirPeso(contadorPerfis)
                    introduzirAltura(contadorPerfis)
                    introduzirIdade(contadorPerfis)
                    introduzirSexo(contadorPerfis)
                    contadorPerfis += 1
                    print(f"\n*** Perfil {contadorPerfis} introduzido com sucesso! ***")
                    if contadorPerfis == MAXNOMES:
                        print("\n*** MAXIMO DE PERFIS ATINGIDO! ***")
                        break
                    while True:
                        continuar = input("\nDeseja Introduzir mais um perfil (S/s para sim / N/n para nao)? --> ").upper()
                        if continuar in ["S", "N"]:
                            break
                        print("Escolha Inválida! Escolha novamente.")
                    if continuar == 'N':
                        break
        elif escolhaM1 == 2:
            if contadorPerfis == 0:
                print("\n*** NAO EXISTEM PERFIS INTRODUZIDOS! ***")
            else:
                continuar = True
                while continuar:
                    escolhaM2 = menu2(contadorPerfis)
                    if escolhaM2 == 0:
                        break
                    while True:
                        escolhaM3 = menu3(escolhaM2 - 1)
                        if escolhaM3 == 0:
                            break
                        elif escolhaM3 == 1:
                            introduzirNome(escolhaM2 - 1)
                        elif escolhaM3 == 2:
                            introduzirPeso(escolhaM2 - 1)
                        elif escolhaM3 == 3:
                            introduzirAltura(escolhaM2 - 1)
                        elif escolhaM3 == 4:
                            introduzirIdade(escolhaM2 - 1)
                        elif escolhaM3 == 5:
                            introduzirSexo(escolhaM2 - 1)
                        elif escolhaM3 == 6:
                            continuar = False
                            break
        elif escolhaM1 == 3:
            if contadorPerfis == 0:
                print("\n*** NAO EXISTEM PERFIS INTRODUZIDOS! ***")
            else:
                print("\n*** TABELA DE PERFIS ***")
                print("+--------------------------------------------------+----+------+-----+----+--------+")
                print("|{:50}|{:4}|{:6}|{:5}|{:4}|{:8}|".format("NOME", "PESO", "ALTURA", "IDADE", "SEXO", "TMB"))
                print("+--------------------------------------------------+----+------+-----+----+--------+")
                for i in range(contadorPerfis):
                    print("|{:50}|{:4}|{:6}|{:5}|{:4}|{:8.2f}|".format(nome[i], peso[i], altura[i], idade[i], sexo[i], calculaTMB(i)))
                    print("+--------------------------------------------------+----+------+-----+----+--------+")

                while True:
                    salvar = input("\nDeseja salvar os perfis em um arquivo? (S/s para sim / N/n para nao)? --> ").upper()
                    if salvar in ["S", "N"]:
                        break
                    print("Escolha Inválida! Escolha novamente.")
                
                if salvar == 'S':
                    while True:
                        formato = input("Escolha o formato do arquivo (txt/csv) --> ").lower()
                        if formato in ["txt", "csv"]:
                            salvar_perfis(formato, contadorPerfis)
                            print(f"Perfis salvos como {formato.upper()} com sucesso!")
                            break
                        print("Escolha Inválida! Escolha novamente.")

if __name__ == "__main__":
    main()
