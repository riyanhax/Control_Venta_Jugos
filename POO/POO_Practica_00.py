class Persona(object):
    """Clase que representa una Persona"""

    def __init__(self, cedula, nombre, apellido, sexo):
        """Constructor de clase Persona"""
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

    def __str__(self):
        """Devuelve una cadena representativa de Persona"""
        return "%s: %s, %s %s, %s." % (
            self.__doc__[25:32], str(self.cedula), self.nombre,
            self.apellido, self.getGenero(self.sexo))

    def hablar(self, mensaje):
        """Mostrar mensaje de saludo de Persona"""
        return mensaje

    def getGenero(self, sexo):
        """Mostrar el genero de la Persona"""
        genero = ('Masculino', 'Femenino')
        if sexo == "M":
            return genero[0]
        elif sexo == "F":
            return genero[1]
        else:
            return "Desconocido"


class Supervisor(Persona):
    """Clase que representa a un Supervisor"""

    def __init__(self, cedula, nombre, apellido, sexo, rol):
        """Constructor de clase Supervisor"""

        # Invoca al constructor de clase Persona
        Persona.__init__(self, cedula, nombre, apellido, sexo)

        # Nuevos atributos
        self.rol = rol
        self.tareas = ['10', '11', '12', '13']

    def __str__(self):
        """Devuelve una cadena representativa al Supervisor"""
        return "%s: %s %s, rol: '%s', sus tareas: %s." % (
            self.__doc__[26:37], self.nombre, self.apellido,
            self.rol, self.consulta_tareas())

    def consulta_tareas(self):
        """Mostrar las tareas del Supervisor"""
        return ', '.join(self.tareas)

class Destreza(object):
    """Clase la cual representa la Destreza de la Persona"""

    def __init__(self, area, herramienta, experiencia):
        """Constructor de clase Destreza"""
        self.area = area
        self.herramienta = herramienta
        self.experiencia = experiencia

    def __str__(self):
        """Devuelve una cadena representativa de la Destreza"""
        return """Destreza en el área %s con la herramienta %s, 
        tiene %s años de experiencia.""" % (
            str(self.area), self.experiencia, self.herramienta)


class JefeCuadrilla(Supervisor, Destreza):
    """Clase la cual representa al Jefe de Cuadrilla"""

    def __init__(self, cedula, nombre, apellido, sexo,
        rol, area, herramienta, experiencia, cuadrilla):
        """Constructor de clase Jefe de Cuadrilla"""

        # Invoca al constructor de clase Supervisor
        Supervisor.__init__(self, cedula, nombre, apellido, sexo,
            rol)
        # Invoca al constructor de clase Destreza
        Destreza.__init__(self, area, herramienta, experiencia)

        # Nuevos atributos
        self.cuadrilla = cuadrilla

    def __str__(self):
        """Devuelve cadena representativa al Jefe de Cuadrilla"""
        jq = "{0}: {1} {2}, rol '{3}', tareas {4}, cuadrilla: {5}"
        return jq.format(
            self.__doc__[28:46], self.nombre, self.apellido,
            self.rol, self.consulta_tareas(), self.cuadrilla)


persona1 = Persona("V-13458796", "Leonardo", "Caballero", "M")
persona2 = Persona("V-23569874", "Ana", "Poleo", "F")
supervisor1 = Supervisor("V-16987456", "Jen", "Paz", "M", "Chivo")

print(persona1.nombre, persona1.apellido)
print(persona1.getGenero(persona1.sexo))

print("\n" + str(persona1) + "\n")
print("\n" + str(supervisor1) + "\n")

print("- Cedula de identidad: {0}.".format(supervisor1.cedula))
print("- Nombre completo: {0} {1}.".format(
    supervisor1.nombre, supervisor1.apellido))
print("- Genero: {0}.".format(
    supervisor1.getGenero(supervisor1.sexo)))
print("- {0} {1} dijo: {2}".format(
    supervisor1.nombre, supervisor1.apellido,
    supervisor1.hablar("A trabajar Leonardo!!!".upper())))
print ("- Rol: {0}.".format(supervisor1.rol))
print ("- N. Tareas: {0}.".format(supervisor1.consulta_tareas()))

print ("""\nHola, Soy el {0} {1} {2}, mi cédula es '{3}', 
mi genero '{4}', con el rol '{5}' y mis tareas
asignadas '{6}'.""".format(
    supervisor1.__doc__[26:37].lower(),
    supervisor1.nombre, supervisor1.apellido, supervisor1.cedula,
    supervisor1.getGenero(supervisor1.sexo), supervisor1.rol,
    supervisor1.consulta_tareas()))

print (JefeCuadrilla.__mro__)