def circ():
    while True:
        try:
            r=int(input("ingrese el radio del circulo: "))
            if r>0:
                per=3.14*(r^4)
                print(f"el area es:{per}")
                break
            else:
                print("ingrese un numero mayor a cero")
                
        except:
            print("ingrese un valor numerico")
def cuad():
    while True:
        try:
            lad=int(input("ingrese el lado del cuadrado: "))
            if lad>0:
                per=lad*4
                print(f"el perimetro es:{per}")
                break
            else:
                print("ingrese un numero mayor a cero")
        except:
            print("ingrese un valor numerico")         
        

