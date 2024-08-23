class Conjunto:
    def __init__(self):
        self.elements = []  # Inicializa una lista vacía para almacenar los elementos del conjunto

    def add(self, element):
        if element not in self.elements:  # Verifica si el elemento no está ya en el conjunto
            self.elements.append(element)  # Si no está, lo agrega a la lista de elementos

    def remove(self, element):
        if element in self.elements:  # Verifica si el elemento está en el conjunto
            self.elements.remove(element)  # Si está, lo elimina de la lista de elementos

    def union(self, other_conjunto):
        new_conjunto = Conjunto()  # Crea un nuevo conjunto para almacenar el resultado
        new_conjunto.elements = list(self.elements)  # Copia los elementos del conjunto actual al nuevo conjunto
        for element in other_conjunto.elements:  # Recorre los elementos del otro conjunto
            new_conjunto.add(element)  # Agrega cada elemento del otro conjunto al nuevo conjunto (si no está ya presente)
        return new_conjunto  # Retorna el nuevo conjunto que contiene la unión

    def complement(self, other_conjunto):
        new_conjunto = Conjunto()  # Crea un nuevo conjunto para almacenar el complemento
        for element in other_conjunto.elements:  # Recorre los elementos del otro conjunto
            if element not in self.elements:  # Si el elemento no está en el conjunto actual
                new_conjunto.add(element)  # Lo agrega al nuevo conjunto
        return new_conjunto  # Retorna el nuevo conjunto que contiene el complemento

    def intersection(self, other_conjunto):
        new_conjunto = Conjunto()  # Crea un nuevo conjunto para almacenar la intersección
        for element in self.elements:  # Recorre los elementos del conjunto actual
            if element in other_conjunto.elements:  # Si el elemento también está en el otro conjunto
                new_conjunto.add(element)  # Lo agrega al nuevo conjunto
        return new_conjunto  # Retorna el nuevo conjunto que contiene la intersección

    def difference(self, other_conjunto):
        new_conjunto = Conjunto()  # Crea un nuevo conjunto para almacenar la diferencia
        for element in self.elements:  # Recorre los elementos del conjunto actual
            if element not in other_conjunto.elements:  # Si el elemento no está en el otro conjunto
                new_conjunto.add(element)  # Lo agrega al nuevo conjunto
        return new_conjunto  # Retorna el nuevo conjunto que contiene la diferencia

    def __str__(self):
        # Retorna una representación en cadena del conjunto en formato {elemento1, elemento2, ...}
        return "{" + ", ".join(str(e) for e in self.elements) + "}"
