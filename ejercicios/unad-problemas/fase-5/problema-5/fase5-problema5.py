

# Diccionario que almacena a los estudiantes con sus notas:
REGISTRO = {}

# --------------------------
# FUNCIONES
# --------------------------


def registro_notas():
    """Registra 3 notas para cada estudiante y las retorna en forma de lista."""
    # lista que almacenara las notas del estudiante:
    notas = []

    # bucle for, que recibe las 3 notas del estudiante.
    for n in range(1, 4):
        while True:
            try:
                nota = float(input(f"Nota {n}: "))
                if 0 <= nota <= 100:
                    break
                print("Debe ingresar una nota en el rango de 0 y 100.")
            except ValueError:
                print("Ha escrito una nota no valida.")

        # agrega cada nota ingresada a la lista.
        notas.append(nota)
    # retorna la lista de notas.
    return notas


def registro_estudiantes():
    """
    Agrega a los estudiantes con sus respectivas notas 
    y promedio al diccionario REGISTRO.
    """

    print("\nREGISTRO DE ESTUDIANTES\n")

    while True:
        try:
            # Pide el numero de estudiantes que se añadirán al registro.
            num_estudiantes = int(input('Numero de estudiantes a registrar: '))
            if num_estudiantes > 0:
                # Se detiene el bucle.
                break
            print("Debe ingresar un numero mayor a cero.")
        except ValueError:
            print("Ha escrito un valor no valido.")

    # Iniciando un bucle que recibirá los datos de cada estudiante:
    for num in range(1, num_estudiantes + 1):
        print(f"\nEstudiante {num}:\n")

        while True:
            nombre = input("Nombre del Estudiante: ").capitalize()
            if not nombre in REGISTRO:
                # El nombre del estudiante no debe estar en el registro para que el bucle se detenga.
                break
            print(f"El estudiante '{nombre}' ya se encuentra registrado(a).")

        # LLamando a la function que registra las 3 notas del estudiante.
        # La lista resultante se almacena en la variable notas.
        notas = registro_notas()

        # Calculando el promedio de notas del estudiante.
        promedio = round(sum(notas) / len(notas), 2)

        # Se añade el estudiante al diccionario, con su lista de notas y promedio.
        REGISTRO[nombre] = {"notas": notas, "promedio": promedio}
        print(f"\nEl estudiante {nombre} se ha registrado exitosamente.")

    print(f"\nSe han registrado {num_estudiantes} estudiantes exitosamente.")


def ranking_estudiantes(registro):
    """
    Recibe el registro de notas. Calcula y muestra el ranking de estudiantes (Mejor promedio, ordenados 
    de manera descendente y promedio general).
    """

    # Si hay estudiantes en el registro.
    if len(registro) > 0:
        # Diccionario que almacenara solamente el nombre y el promedio de notas.
        promedios = {}

        # Recorriendo cada estudiante del registro.
        for estudiante, datos in registro.items():
            promedios[estudiante] = datos['promedio']

        # Convirtiendo los valores (promedios) en una sola lista.
        solo_promedios = list(promedios.values())
        # Ordenando la lista de manera descendente con el método sorted():
        solo_promedios = sorted(solo_promedios, reverse=True)

        # Calculando el promedio mas alto de la lista.
        max_promedio = max(solo_promedios)
        # Calculando el promedio general de todos los estudiantes.
        promedio_general = round(sum(solo_promedios)/len(solo_promedios), 2)

        # Diccionario que almacenara los resultados finales.
        resultados = {}
        # Lista que almacena los nombres en orden descendente, basado en el promedio.
        ranking_promedio = []

        # Buscando el nombre del estudiante al que pertenece cada promedio ordenado.
        for p in solo_promedios:
            for nombre, promedio in promedios.items():
                if p == max_promedio:
                    resultados["mejor promedio"] = nombre

                if p == promedio:
                    ranking_promedio.append(nombre)
                    break

        resultados["ranking"] = ranking_promedio
        resultados["promedio general"] = promedio_general

        # mostrando los resultados:
        print("\nRESULTADOS:\n")
        print(f"Promedios Obtenidos: {promedios}\n")
        for clave, valor in resultados.items():
            print(f"- {clave.capitalize()}: {valor}")

        return True

    print("\nNo se ha registrado ningún estudiante.")
    return False


def menu():
    """
    Muestra las opciones del menu principal, y recibe la opción
    escogida por el usuario y la retorna.
    """

    print("REGISTRO DE NOTAS\n")
    print("1. Registrar Notas\n2. Generar Ranking\n3. Salir")

    while True:
        opcion = input("\nSeleccione una opción (1-3): ")
        if opcion in ("1", "2", "3"):
            return opcion

        print("Ingrese una opción valida.")


# --------------------------
# PROGRAMA PRINCIPAL
# --------------------------

def main():
    """
    Programa principal.
    """

    while True:
        opcion = int(menu())

        if opcion == 1:
            # Registrando a los estudiantes.
            registro_estudiantes()
        elif opcion == 2:
            # Calculando y mostrando el ranking.
            ranking_estudiantes(REGISTRO)
        elif opcion == 3:
            input("\nPresione ENTER para continuar.")
            print("\n")
            break

        input("\nPresione ENTER para volver al menu.")
        print("\n")


# Ejecutando el programa principal.
main()
