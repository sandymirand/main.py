import math
import os

def Menu():

    print("1.-Suma              5.- Potencia")
    print("2.-Resta             6.- Raiz Cudrada")
    print("3.-Multiplicacion    7.- Seno ")
    print("4.- Division         8.- Coseno")
    print("2.-Resta             9.- Tangente")
    print("10.- Borrar Pantalla   11.- Menu    12.- Salir ")


def mcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    while b != 0:
        mcd = b
        b = a % b
        a = mcd
    return mcd


def mcm(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    mcm = (a / mcd(a, b)) * b
    return mcm


def borrarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def Calculadora():
    Menu()

    opc = int(input("Selecione opcion: "))

    while (opc > 0 and opc < 12):

        if (opc == 1):
            print("")
            num1 = int(input("Ingrese Primer Numero: "))
            print("")
            num2 = int(input("Ingrese Segundo Numero: "))
            print("")
            print('La Suma es:', num1 + num2)
            print("")
            Continuar = input("¿Desea Continuar?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 1

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione una de Opcion: "))

            else:
                print("")
                Continuar = input("Ingresar(S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 1

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione una Opcion: "))


        elif (opc == 2):
            print("")
            num1 = int(input("Ingrese Primer Numero: "))
            print("")
            num2 = int(input("Ingrese Segundo Numero: "))
            print("")
            print('La Resta es:', num1 - num2)
            print("")
            Continuar = input("¿Desea Continuar?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 2

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione una opcion: "))

            else:
                print("")
                Continuar = input("Ingrese(S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 2

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione una Opcion: "))

        elif (opc == 3):
            print("")
            num1 = int(input("Ingrese Primer Numero: "))
            print("")
            num2 = int(input("Ingrese Segundo Numero: "))
            print("")
            print('La Multiplicacion es:', num1 * num2)
            print("")
            Continuar = input("¿Desea Continuar?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 3

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione una opcion: "))

            else:
                print("")
                Continuar = input("Ingrese (S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 3

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione una opciÃ³n: "))

        elif (opc == 4):
            print("")
            num1 = int(input("Ingrese Primer Numero: "))
            print("")
            num2 = int(input("Ingrese Segundo Numero: "))
            print("")

            try:
                print('La Division es:', num1 / num2)
                print("")
                Continuar = input("¿Desea Continuar?(S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 4

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione una opcion: "))

                else:
                    print("")
                    Continuar = input("Ingrese (S/N): ")

                    if Continuar == "s" or Continuar == "S":
                        opc = 4

                    elif Continuar == "n" or Continuar == "N":
                        print("")
                        opc = int(input("Selecione una opcion: "))

            except ZeroDivisionError:
                print('No se Permite la Division Entre 0')
                print("")
                Continuar = input("¿Desea Continuar?(S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 4

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione una Opcion: "))

                else:
                    print("")
                    Continuar = input("Ingrese (S/N): ")

                    if Continuar == "s" or Continuar == "S":
                        opc = 4

                    elif Continuar == "n" or Continuar == "N":
                        print("")
                        opc = int(input("Selecione una opcionn: "))


        elif (opc == 5):
            print("")
            base = int(input("Ingrese Base: "))
            print("")
            exponente = int(input("Ingrese Exponente: "))
            print("")
            print('La Potencia es:', base ** exponente)
            print("")
            Continuar = input("¿Desea Continuar?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 5

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione una opcion: "))

            else:
                print("")
                Continuar = input("Ingresa (S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 5

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione una opcion: "))

        elif (opc == 6):
            print("")
            num = int(input("Ingrese Numero: "))
            print("")
            print("La raiz cuadrada de {} es {}".format(num, math.sqrt(num)))
            print("")
            Continuar = input("¿Desea Continuar?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 6

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione una opcion: "))

            else:
                print("")
                Continuar = input("Ingrese (S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 6

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione una opcion: "))

        elif (opc == 7):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("El seno de {} es {}".format(radianes, math.sin(radianes)))
            print("")
            Continuar = input("¿Desea Continuar?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 7

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione una opcion: "))

            else:

                print("")
                Continuar = input("Ingrese (S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 7

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione una Opcion: "))



        elif (opc == 8):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("El coseno de {} es {}".format(radianes, math.cos(radianes)))
            print("")
            Continuar = input("¿Desea Continuar?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 8

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione una Opcion: "))

            else:
                print("")
                Continuar = input("ingrese (S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 8

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione una opcionn: "))


        elif (opc == 9):
            print("")
            radianes = int(input("Ingrese Radianes: "))
            print("")
            print("La tangente de {} es {}".format(radianes, math.tan(radianes)))
            print("")
            Continuar = input("¿Desea Continuar?(S/N): ")

            if Continuar == "s" or Continuar == "S":
                opc = 9

            elif Continuar == "n" or Continuar == "N":
                print("")
                opc = int(input("Selecione una opcion: "))

            else:
                print("")
                Continuar = input("Ingrese (S/N): ")

                if Continuar == "s" or Continuar == "S":
                    opc = 9

                elif Continuar == "n" or Continuar == "N":
                    print("")
                    opc = int(input("Selecione una opcion: "))




        elif (opc == 10):
            borrarPantalla()
            Menu()
            opc = int(input("Selecione una opcion: "))

        elif (opc == 11):
            Menu()
            opc = int(input("Selecione una opcion: "))

        elif (opc == 12):
            exit(0)

    while (opc < 1 or opc > 13):
        print("")
        print("No Encontrada")
        print("")
        opc = int(input("Selecione una opcion:: "))
1

Calculadora()
