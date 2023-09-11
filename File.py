
nome = str(input("Digite o seu nome :"))
curso = str(input("Digite o nome do seu curso:"))

def criarArquivo () :
    arquivo = open("dados.txt","w")
    arquivo.close()
def escreverArquivo () :
    arquivo = open("dados.txt","a")
    arquivo.write(nome.upper() + "\n")
    arquivo.write(curso.upper() + "\n")
    arquivo.close()

criarArquivo()
escreverArquivo()
