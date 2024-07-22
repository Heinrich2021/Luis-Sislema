class Personaje:

    def __init__(self, apellido, fuerza, inteligencia, astucia, vida):
        self.apellido = apellido
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.astucia = astucia
        self.vida = vida

    def atributos(self):

        print(self.apellido, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·astucia:", self.astucia)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, astucia):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.astucia = self.astucia + astucia

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.apellido, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.astucia

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.apellido, "ha realizado", daño, "puntos de daño a", enemigo.apellido)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.apellido, "es", enemigo.vida)
        else:
            enemigo.morir()


class Arquero(Personaje):

    def __init__(self, apellido, fuerza, inteligencia, astucia, vida, arco):
        super().__init__(apellido, fuerza, inteligencia, astucia, vida)
        self.arco = arco

    def cambiar_arco(self):
        opcion = int(input("Elige un arco: (2) Arco Largo, daño 5. (1) Arco Compuesto, daño 6"))
        if opcion == 1:
            self.arco = 5
        elif opcion == 2:
            self.arco = 6
        else:
            print("Número de arco incorrecto")

    def atributos(self):
        super().atributos()
        print("·Arco:", self.arco)

    def daño(self, enemigo):
        return self.fuerza * self.arco - enemigo.astucia


class Clerigo(Personaje):

    def __init__(self, apellido, fuerza, inteligencia, astucia, vida, baston):
        super().__init__(apellido, fuerza, inteligencia, astucia, vida)
        self.baston = baston

    def atributos(self):
        super().atributos()
        print("·Bastón:", self.baston)

    def curar(self, aliado):
        if self.esta_vivo():
            cura = self.inteligencia * self.baston
            aliado.vida = aliado.vida + cura
            print(self.apellido, "ha curado a", aliado.apellido, "por", cura, "puntos de vida")
            print("Vida de", aliado.apellido, "es", aliado.vida)

    def daño(self, enemigo):
        return self.inteligencia - enemigo.astucia


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de", jugador_1.apellido, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de", jugador_2.apellido, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.apellido)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.apellido)
    else:
        print("\nEmpate")


# Ejemplo de uso
personaje_1 = Arquero("Merino", 15, 8, 5, 80, 4)
personaje_2 = Clerigo("Sislema", 8, 20, 6, 90, 2)

personaje_1.atributos()
personaje_2.atributos()

# Ejemplo de combate
combate(personaje_1, personaje_2)