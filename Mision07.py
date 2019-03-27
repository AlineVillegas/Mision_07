#Autor: Aline Paulette Villegas Berdejo
#Este programa contiene un menú donde se puede elegir calcular divisiones o encontrar el número mayor


def dividir(dividendo, divisor):    #Calcula el cociente y el residuo de una divisón
    cociente = 0
    if dividendo < divisor:
        cociente = 0
        residuo = dividendo
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente = cociente +1
        residuo = dividendo
    return cociente,residuo


def encontrarMayor():           #Encuentra el número mayor dentro de una serie de números
    numero = int(input("Teclea el número [-1 para salir]: "))
    if numero != -1:
        if numero < -1:
            print("Error, no puedes ingresar números negativos si no es -1")
        else:
            mayor = numero
    else:
        print("No hay valor mayor")
    while numero > -1:
        numero = int(input("Teclea un número [-1 para salir]: "))
        if mayor < numero:
            mayor = numero
        elif numero < -1:
            print("Error, no puedes ingresar números negativos si no es -1")
        elif numero == -1:
           print("El mayor es: ", mayor)


def main():            #Ejecuta las funciones y el menú
    print("Misión 07. Ciclos while \nAutor: Aline Villegas Berdejo \nMatrícula: A01375818")
    print("1. Calcular divisiones \n2. Encontrar el mayor \n3.Salir ")
    opcion= int(input("Teclea tu opción: "))
    while opcion != 3:
        if opcion == 1:
            print("\nCalculando divisones")
            dividendo= int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            division = dividir(dividendo, divisor)
            print(dividendo , "/" , divisor , "=" , division[0] , ", sobra" , division[1])
            print("\nMisión 07. Ciclos while \nAutor: Aline Villegas Berdejo \nMatrícula: A01375818")
            print("1. Calcular divisiones \n2. Encontrar el mayor \n3.Salir ")
            opcion = int(input("Teclea tu opción: "))

        elif opcion == 2:
            print("\nTeclea una serie de números para encontrar el mayor. ")
            encontrarMayor()
            print("\nMisión 07. Ciclos while \nAutor: Aline Villegas Berdejo \nMatrícula: A01375818")
            print("1. Calcular divisiones \n2. Encontrar el mayor \n3.Salir ")
            opcion = int(input("Teclea tu opción: "))

        else:
            print("ERROR, teclea 1, 2 ó 3")
            print("\nMisión 07. Ciclos while \nAutor: Aline Villegas Berdejo \nMatrícula: A01375818")
            print("1. Calcular divisiones \n2. Encontrar el mayor \n3.Salir ")
            opcion = int(input("Teclea tu opción: "))

    if opcion == 3:
        print("\nGracias por usar este programa, regresa pronto.")


main() #Llama a la función principal