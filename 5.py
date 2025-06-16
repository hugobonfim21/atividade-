vm=80
vc=int(input("Velocidade do carro: "))

print(vc-vm)

if vc>vm:

    print("O carro está a KM/h",(vc-vm),"acima do limite da via")

if vc==vm:

    print("Você está no limite da via")

else: 
    print("O carro está KM/h",(vm-vc),"abaixo do limite da via")

 
