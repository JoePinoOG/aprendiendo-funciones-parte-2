import func2 as fn
op=0
while op!=3:
    print("1.Calcular area circulo")
    print("2.Calcular perimetro cuadrado")
    print("3.Salir")
    try:
        op=int(input("ingrese una opcion: "))
        if op>0 and op <4:
            if op==1:
                print("calcular area circulo")
                fn.circ()
            elif op==2:
                print("calcular perimetro del cuadrado")
                fn.cuad()
            else:
                print("saliste del programa")
                break
        else:
            print("Ingrese una opcion valida")
    except:
        print("ingrese un valor numerico")

