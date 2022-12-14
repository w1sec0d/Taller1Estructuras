# Este programa distribuye los equipos electrónicos de un campus universitario
# Realizado por Carlos David Ramírez Muñoz

# Definicion de estructuras de datos necesarias para trabajar
class Cola():
    def __init__(self, lista=[]):
        self.lista = lista

    def añadir(self, elemento):
        self.lista.append(elemento)

    def extraer(self):
        return self.lista.pop(0)

    def __str__(self):
        return(str(self.lista))


class Facultad():
    def __init__(self, nombre: str, numero: int, estudiantes=0):
        self.nombre = nombre
        self.numero = numero
        self.estudiantes = estudiantes
        # Se usa un array de equipos, en que la posicion 0 son computadores, 1 tablets y 2 laptops
        self.equipos = 0
        self.arrayEquipos = [0, 0, 0]
        self.estudiantesSinEquipo = self.estudiantes - self.equipos


# Orderna a la lista de facultades, dependiendo de si se necesita el orden de repartición o de impresión
def ordenarFacultades(facultades: list, impresionFinal=False) -> list:
    if not(impresionFinal):
        # De mayor numero de estudiantes sin equipo a menor
        arrayReordenado = sorted(
            facultades, key=lambda facultad: (facultad.estudiantesSinEquipo, -facultad.numero), reverse=True)
    else:
        arrayReordenado = sorted(
            facultades, key=lambda facultad: (-facultad.estudiantesSinEquipo, -facultad.numero), reverse=True)

    return arrayReordenado


class Universidad():
    def __init__(self, facultades: list):
        # Se usa un array de equipos, en que la posicion 0 son computadores, 1 tablets y 2 laptops
        self.arrayEquipos = [0, 0, 0]
        self.equipos = 0
        # Array en el que se ordenan las facultades de mayor numero de estudiantes sin equipo a menor numero de estudiantes sin equipo
        self.facultades = ordenarFacultades(facultades)
        self.estudiantesSinEquipo = self.facultades[0].estudiantesSinEquipo + \
            self.facultades[1].estudiantesSinEquipo + \
            self.facultades[2].estudiantesSinEquipo + \
            self.facultades[3].estudiantesSinEquipo


# Función extractora de números de un string


def listarNumeros(mensaje: str) -> list:
    numeros = []
    mensajeSeparado = mensaje.split()

    for cadena in mensajeSeparado:
        if cadena.isdigit():
            numeros.append(int(cadena))

    return numeros


# Funcion principal distribuidora

lotes = Cola()

# Se extraen los datos de estudiantes y se guardan en los objetos facultad y universidad

listaCantidadEstudiantes = listarNumeros(input(""))
Ingenieria = Facultad("Ingenieria", 0, listaCantidadEstudiantes[0])
Humanas = Facultad("Humanas", 1, listaCantidadEstudiantes[1])
Artes = Facultad("Artes", 3, listaCantidadEstudiantes[2])
Medicina = Facultad("Medicina", 2, listaCantidadEstudiantes[3])
universidadPrueba = Universidad([Ingenieria, Humanas, Artes, Medicina])

try:
    # While para recibir instrucciones de manera indefinida
    while True:
        instruccion = input()
        # Si la instruccion es lote, se guarda en una Cola de lotes
        if instruccion.split()[0] == "Lote":
            lote = listarNumeros(instruccion)
            lotes.añadir(lote)

        elif instruccion == "Distribuir lote":
            lote = lotes.extraer()
            tipoDeEquipoAEntregar = 0
            # mientras el lote no esté vacío y los estudiantes sin equipo de la universidad sean mayores a 0, se sigue repartiendo equipos
            while lote != [0, 0, 0] and universidadPrueba.estudiantesSinEquipo > 0:
                # Se recorre cada facultad, en el orden de prioridad
                universidadPrueba.facultades = ordenarFacultades(
                    universidadPrueba.facultades)
                for facultad in universidadPrueba.facultades:
                    facultad.arrayEquipos = [0, 0, 0]
                    if facultad.estudiantesSinEquipo == 0 or lote == [0, 0, 0]:
                        continue
                    # Por cada ciclo se reparte de a un equipo y se revisa la condicion inicial
                    while lote != [0, 0, 0] and facultad.estudiantesSinEquipo > 0:
                        for i in range(0, len(lote)):
                            if tipoDeEquipoAEntregar > 0:
                                tipoDeEquipoAEntregar -= 1
                                continue

                            if facultad.estudiantesSinEquipo == 0:
                                tipoDeEquipoAEntregar = i
                                break
                            if lote[i] > 0:
                                lote[i] -= 1
                                facultad.arrayEquipos[i] += 1
                                facultad.equipos += 1
                                facultad.estudiantesSinEquipo -= 1
                                universidadPrueba.estudiantesSinEquipo -= 1
        elif instruccion == "Imprimir":
            universidadPrueba.facultades = ordenarFacultades(
                universidadPrueba.facultades, impresionFinal=True)
            for facultad in universidadPrueba.facultades:
                print(
                    f"{facultad.nombre} {facultad.estudiantesSinEquipo} - Computers {facultad.arrayEquipos[0]} Laptops {facultad.arrayEquipos[1]} Tablets {facultad.arrayEquipos[2]}")
except:
    pass
