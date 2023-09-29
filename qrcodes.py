# Generate a QR CODE at any time. You just need to have the module 'qrcode' installed
import qrcode as qr

print("Este programa o ajudará a criar um código QR do endereço que você quise!")
url = input("Introduza o endereço ou URL para o Código QR: ")
salvo = input("Que nome deseja dar a imagem? ")
imagemCodigo = qr.make(url)
imagemCodigo.save(salvo+".png")
print(f"O seu Código QR foi criado e salvo com sucesso com o nome {salvo}!")
