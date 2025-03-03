def verifica_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def verifica_numero(numero):
    if verifica_primo(numero):
        return "Primo"
    else:
        return "Composto"

# Exemplo de uso
numero = int(input("Digite um número: "))
resultado = verifica_numero(numero)
print(f"O número {numero} é {resultado}.")

while True:
    continuar = input("Deseja verificar outro número? (s/n): ").strip().lower()
    if continuar == 's':
        numero = int(input("Digite um número: "))
        resultado = verifica_numero(numero)
        print(f"O número {numero} é {resultado}.")
    elif continuar == 'n':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")