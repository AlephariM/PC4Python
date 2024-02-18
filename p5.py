def guardar_tabla_m(numero):
    try:
        with open(f"tabla-{numero}.txt", "w") as archivotxt:
            for i in range(10):
                archivotxt.write(f"{i+1} x {numero} = {(i+1)*numero} \n")
        
        print(f"Tabla de multiplicar {numero} se ha creado.")
    except Exception as eror:
        print("No se ha guardado la tabla: {}".format(eror))

def mostrar_tabla_m(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivotxt:
            for _ in archivotxt:
                print(_.strip())
    except FileNotFoundError as eror:
        print("No se ha encontrado el archivo de tabla {}".format(numero))
    
def mostrar_linea_tabla_m(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivotxt:
            lineas_archivotxt = archivotxt.readlines() #lista
            if (linea >= 1 and linea <= 10):
                print(f"Linea {linea} de la tabla {numero}:") 
                print(lineas_archivotxt[linea-1].strip())
    except FileNotFoundError as eror:
        print("No se ha encontrado el archivo de tabla {}".format(numero))

def main():
    while True:
        print("""\nMenu:\n
              1) Guardar tabla de multiplicar.\n
              2) Mostrar tabla de multiplicar\n
              3) Mostrar línea de la tabla de multiplicar\n
              4) Salir\n""")
        
        opcion = int(input("Seleccione una opción: "))

        if opcion==1:
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if (1 <= numero and numero <= 10):
                guardar_tabla_m(numero)
            else:
                print("Número incorrecto.")
                
        elif opcion== 2:
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if (1 <= numero and numero <= 10):
                mostrar_tabla_m(numero)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion== 3:
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea a mostrar: "))
            if (1 <= numero and numero <= 10):
                mostrar_linea_tabla_m(numero, linea)
            else:
                print("El número y la línea deben estar entre 1 y 10.")
        elif opcion== 4:
            print("Saliendo")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
