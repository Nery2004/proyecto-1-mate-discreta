class Conjunto:
    def __init__(self):
        self.elements = []

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def union(self, other_conjunto):
        new_conjunto = Conjunto()
        new_conjunto.elements = list(self.elements)
        for element in other_conjunto.elements:
            new_conjunto.add(element)
        return new_conjunto
    
    def complement(self, other_conjunto):
        new_conjunto = Conjunto()
        for element in other_conjunto.elements:
            if element not in self.elements:
                new_conjunto.add(element)
        return new_conjunto

    def intersection(self, other_conjunto):
        new_conjunto = Conjunto()
        for element in self.elements:
            if element in other_conjunto.elements:
                new_conjunto.add(element)
        return new_conjunto

    def difference(self, other_conjunto):
        new_conjunto = Conjunto()
        for element in self.elements:
            if element not in other_conjunto.elements:
                new_conjunto.add(element)
        return new_conjunto

    def __str__(self):
        return "{" + ", ".join(str(e) for e in self.elements) + "}"
