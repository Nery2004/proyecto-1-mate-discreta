from conjunto import Conjunto  # Importa la clase Conjunto desde el archivo conjunto

def menu():
    conjuntos = []  # Array vacío para almacenar los conjuntos creados

    # Diccionario de opciones del menú, donde cada clave es una opción y el valor es una función lambda que llama a la función correspondiente
    opciones = {
        '1': lambda: construir_conjuntos(conjuntos),
        '2': lambda: operar_conjuntos(conjuntos),
        '3': lambda: 'Salir'
    }

    opcion = ''
    # Bucle que mantiene el menú en ejecución hasta que el usuario elige salir (opción '3')
    while opcion != '3':
        print("\nMenú Principal:")
        print("1. Construir conjuntos")
        print("2. Operar conjuntos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")  # Solicita al usuario que elija una opción

        # Verifica si la opción elegida está en el diccionario de opciones
        if opcion in opciones:
            resultado = opciones[opcion]()  # Llama a la función correspondiente a la opción elegida
            if resultado == 'Salir':
                print("\n¡Hasta pronto!")
                break  # Sale del bucle si el usuario elige la opción '3'
        else:
            print("\nOpción no válida, por favor seleccione una opción del 1 al 3.")  # Mensaje de error para opciones inválidas

def construir_conjuntos(conjuntos):
    conjuntos.clear()  # Limpia la lista de conjuntos antes de crear nuevos

    for i in range(2):  # Bucle para crear dos conjuntos
        conjunto = Conjunto()  # Crea una nueva instancia de la clase Conjunto
        elementos = input(f"\nIngrese los elementos del conjunto {i+1} separados por comas: ")  # Solicita al usuario los elementos del conjunto
        for elemento in elementos.split(','):  # Divide los elementos ingresados por comas
            elemento = elemento.strip()  # Elimina los espacios en blanco alrededor de cada elemento
            if elemento.isalnum() and len(elemento) == 1:  # Verifica si el elemento es alfanumérico y tiene una longitud de 1
                conjunto.add(elemento)  # Agrega el elemento al conjunto
            else:
                print(f"\nElemento inválido '{elemento}' ignorado.")  # Mensaje de advertencia para elementos inválidos
        conjuntos.append(conjunto)  # Agrega el conjunto creado a la lista de conjuntos
        print(f"\nConjunto {i+1} creado: {conjunto}")  # Muestra el conjunto creado
    
    return conjuntos  # Retorna la lista de conjuntos creados

def operar_conjuntos(conjuntos):
    if len(conjuntos) < 2:  # Verifica que haya al menos dos conjuntos para operar
        print("\nDebe haber al menos dos conjuntos creados para operar.")
        return

    # Muestra las operaciones disponibles
    print("\nSeleccione la operación que desea realizar:")
    print("1. Complemento")
    print("2. Unión")
    print("3. Intersección")
    print("4. Diferencia")
    print("5. Diferencia Simétrica")

    operacion = input("Seleccione una operación: ")  # Solicita al usuario que elija una operación

    conjunto1 = conjuntos[0]  # Asigna el primer conjunto
    conjunto2 = conjuntos[1]  # Asigna el segundo conjunto

    # Realiza la operación seleccionada
    if operacion == '1':
        resultado1 = conjunto1.complement(conjunto2)  # Calcula el complemento del conjunto 1 respecto al conjunto 2
        resultado2 = conjunto2.complement(conjunto1)  # Calcula el complemento del conjunto 2 respecto al conjunto 1
        print(f"\nEl resultado del complemento del conjunto 1 {conjunto1} respecto al conjunto 2 {conjunto2} es {resultado1}")
        print(f"El resultado del complemento del conjunto 2 {conjunto2} respecto al conjunto 1 {conjunto1} es {resultado2}")
    elif operacion == '2':
        resultado = conjunto1.union(conjunto2)  # Calcula la unión de ambos conjuntos
        print(f"\nEl resultado de la unión del conjunto {conjunto1} y el conjunto {conjunto2} es {resultado}")
    elif operacion == '3':
        resultado = conjunto1.intersection(conjunto2)  # Calcula la intersección de ambos conjuntos
        print(f"\nEl resultado de la intersección del conjunto {conjunto1} y el conjunto {conjunto2} es {resultado}")
    elif operacion == '4':
        resultado1 = conjunto1.difference(conjunto2)  # Calcula la diferencia entre el conjunto 1 y el conjunto 2
        resultado2 = conjunto2.difference(conjunto1)  # Calcula la diferencia entre el conjunto 2 y el conjunto 1
        print(f"\nEl resultado de la diferencia del conjunto 1 {conjunto1} - el conjunto 2 {conjunto2} es {resultado1}")
        print(f"El resultado de la diferencia del conjunto 2 {conjunto2} - el conjunto 1 {conjunto1} es {resultado2}")
    elif operacion == '5':
        diferencia1 = conjunto1.difference(conjunto2)  # Calcula la diferencia entre el conjunto 1 y el conjunto 2
        diferencia2 = conjunto2.difference(conjunto1)  # Calcula la diferencia entre el conjunto 2 y el conjunto 1
        resultado = diferencia1.union(diferencia2)  # Calcula la diferencia simétrica
        print(f"\nEl resultado de la diferencia simétrica del conjunto {conjunto1} y el conjunto {conjunto2} es {resultado}")
    else:
        print("\nOpción no válida.")  # Mensaje de error para opciones de operación inválidas
        return

menu()  # Llama a la función del menú para iniciar el programa
