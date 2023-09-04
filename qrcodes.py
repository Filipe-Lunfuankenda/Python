import qrcode as qr

print("Seja Bem-vindo(a)! Este programa o ajudará a criar um código QR do endereço que você quiser.")
url = input("Introduza o endereço ou URL para o Código QR:")
salvo = input("Que nome deseja dar a imagem?")
imagemCodigo = qr.make(url)
imagemCodigo.save(salvo+".png")
print("O seu Código QR foi criado e salvo com sucesso!")