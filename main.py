class animal:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def pasear(self):
        pass # Es como un break, así podemos inicializar una función vacía 

    def alimentar(self):
        pass


    def darInfo(self):
        return print("\n• " + self.nombre + " de raza: " + self.raza)



class mascota(animal):
    def __init__(self, nombre, raza, propietario):
        self.propietario = propietario
        super(mascota , self).__init__(nombre , raza)


class gato(mascota): # Se aplica herencia
    def pasear(self):
        print("\n♧ Paseando al gato" + " " + self.propietario)

    def alimentar(self):
        print("\n♧ Alimentando al gato")


class perro(mascota): # Se aplica herencia
    def pasear(self):
        print("\n♥ Paseando al perro" + " " + self.propietario)

    def alimentar(self):
        print("\n♥ Alimentando al perro")


class lagarto(mascota):
    def pasear(self):
        print("\n♠ Paseando al lagarto" + " " + self.propietario)

    def alimentar(self):
        print("\n♠ Alimentando al lagarto")


if __name__ == '__main__':
    mascotas = [perro("Blus" , "Chow Chow" , "Luffy") , gato("Lotus" , "Siamés" , "Zoro") , lagarto("Crocodile" , "Anolis" , "Sanji")]

    for m in mascotas:
        m.pasear()
        m.alimentar()
        m.darInfo()