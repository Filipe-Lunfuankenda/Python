#Generate a text file
nome = str(input("Digite o seu nome: "))
content = str(input("Digite o que está a pensar:\n"))

def criarArquivo ():
    arquivo = open("dados.txt","w")
    arquivo.close()
def escreverArquivo ():
    arquivo = open("dados.txt","a")
    arquivo.write(nome.upper() + "\n")
    arquivo.write(content.upper() + "\n")
    arquivo.close()

criarArquivo()
escreverArquivo()
