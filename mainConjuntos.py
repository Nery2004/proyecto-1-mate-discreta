from conjunto import Conjunto

def menu():
    conjuntos = []

    opciones = {
        '1': lambda: construir_conjuntos(conjuntos),
        '2': lambda: operar_conjuntos(conjuntos),
        '3': lambda: 'Salir'
    }

    opcion = ''
    while opcion != '3':
        print("\nMenú Principal:")
        print("1. Construir conjuntos")
        print("2. Operar conjuntos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion in opciones:
            resultado = opciones[opcion]()
            if resultado == 'Salir':
                print("\n¡Hasta pronto!")
                break
        else:
            print("\nOpción no válida, por favor seleccione una opción del 1 al 3.")

def construir_conjuntos(conjuntos):
    conjuntos.clear()

    for i in range(2):
        conjunto = Conjunto()
        elementos = input(f"\nIngrese los elementos del conjunto {i+1} separados por comas: ")
        for elemento in elementos.split(','):
            elemento = elemento.strip()
            if elemento.isalnum() and len(elemento) == 1:
                conjunto.add(elemento)
            else:
                print(f"\nElemento inválido '{elemento}' ignorado.")
        conjuntos.append(conjunto)
        print(f"\nConjunto {i+1} creado: {conjunto}")
    
    return conjuntos

def operar_conjuntos(conjuntos):
    if len(conjuntos) < 2:
        print("\nDebe haber al menos dos conjuntos creados para operar.")
        return

    print("\nSeleccione la operación que desea realizar:")
    print("1. Complemento")
    print("2. Unión")
    print("3. Intersección")
    print("4. Diferencia")
    print("5. Diferencia Simétrica")

    operacion = input("Seleccione una operación: ")

    conjunto1 = conjuntos[0]
    conjunto2 = conjuntos[1]

    if operacion == '1':
        resultado1 = conjunto1.complement(conjunto2)
        resultado2 = conjunto2.complement(conjunto1)
        print(f"\nEl resultado del complemento del conjunto 1 {conjunto1} respecto al conjunto 2 {conjunto2} es {resultado1}")
        print(f"El resultado del complemento del conjunto 2 {conjunto2} respecto al conjunto 1 {conjunto1} es {resultado2}")
    elif operacion == '2':
        resultado = conjunto1.union(conjunto2)
        print(f"\nEl resultado de la union del conjunto {conjunto1} y el conjunto {conjunto2} es {resultado}")
    elif operacion == '3':
        resultado = conjunto1.intersection(conjunto2)
        print(f"\nEl resultado de la intersección del conjunto {conjunto1} y el conjunto {conjunto2} es {resultado}")
    elif operacion == '4':
        resultado1 = conjunto1.difference(conjunto2)
        resultado2 = conjunto2.difference(conjunto1)
        print(f"\nEl resultado de la diferencia del conjunto 1 {conjunto1} - el conjunto 2 {conjunto2} es {resultado1}")
        print(f"El resultado de la diferencia del conjunto 2 {conjunto2} - el conjunto 1 {conjunto1} es {resultado2}")
    elif operacion == '5':
        diferencia1 = conjunto1.difference(conjunto2)
        diferencia2 = conjunto2.difference(conjunto1)
        resultado = diferencia1.union(diferencia2)
        print(f"\nEl resultado de la diferencia simetrica del conjunto {conjunto1} y el conjunto {conjunto2} es {resultado}")
    else:
        print("\nOpción no válida.")
        return

menu()
