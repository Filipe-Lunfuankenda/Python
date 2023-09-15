
a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:")) 
c = float(input("Digite o valor de c:"))

delta = b**2 - 4*a*c
raiz_delta = delta**(1/2)

print ("-"*60)
print ("O valor de delta é", delta)
print ("A raiz quadrada de", delta, "é", raiz_delta)

x1 = (-b + raiz_delta)/2*a
x2 = (-b - raiz_delta)/2*a

print ("-"*60)
if delta > 0:
    print ("A equação possui duas raízes diferentes")
    print ("O valor de x1 é", x1)
    print ("O valor de x2 é", x2)
elif delta == 0:
    print ("A equação possui uma única raiz igual")
    print ("O valor de x1 é", x1)
    print ("O valor de x2 é", x2)
else:
    print ("Delta negativo, logo não possui raiz")
    print ("A raiz quadrada de", delta, "não existe no conjunto de números reais")




