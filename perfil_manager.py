# Definições de constantes
MAXNOMES = 3  # máximo de 3 nomes
MAXLETRAS = 50  # máximo de 50 letras para cada nome

# Declaração das variáveis ​​globais do programa, acessíveis por qualquer função do programa
nome = [[""] * MAXLETRAS for _ in range(MAXNOMES)]  # vetor 'nome' multidimensional (2D) de 3 x 50 elementos do tipo char, usado para salvar 3 nomes de 50 letras cada
peso = [0] * MAXNOMES  # vetor 'peso' unidimensional (1D) de 3 elementos do tipo inteiro, usado para salvar o peso de cada perfil
altura = [0] * MAXNOMES  # vetor 'altura' unidimensional (1D) de 3 elementos do tipo inteiro, usado para salvar a altura de cada perfil
idade = [0] * MAXNOMES  # vetor 'idade' unidimensional (1D) de 3 elementos do tipo inteiro, usado para salvar a idade de cada perfil
sexo = [""] * MAXNOMES  # vetor 'sexo' unidimensional (1D) de 3 elementos do tipo char, usado para salvar o sexo de cada perfil

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

def main():
    contadorPerfis = 0
    while True:
        escolhaM1 = menu()
        if escolhaM1 == 0:
            break
        elif escolhaM1 == 1:
            if contadorPerfis == 3:
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
                    if contadorPerfis == 3:
                        print("\n*** MAXIMO DE PERFIS ATINGIDO! ***")
                        break
                    continuar = input("\nDeseja Introduzir mais um perfil (1-Sim / 0-Nao)? --> ")
                    if continuar.isdigit() and int(continuar) == 0:
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

if __name__ == "__main__":
    main()