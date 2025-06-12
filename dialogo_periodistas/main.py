from periodista_1 import consulta_periodista_1
from periodista_2 import consulta_periodista_2

def main():
    print("Ingrese el tema del cual quiere que se discuta: ")
    mensaje_usuario = input("Ingresa el tema: ")
    mensaje_p1 = consulta_periodista_1(mensaje_usuario)
    print(mensaje_p1)
    for i in range(5):
        mensaje_p2 = consulta_periodista_2(mensaje_p1)
        print(mensaje_p2)
        mensaje_p1 = consulta_periodista_1(mensaje_p2)
        print(mensaje_p1)

    print("Fin del debate")

if __name__ == "__main__":
    main()