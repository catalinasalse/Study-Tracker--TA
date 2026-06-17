def cargar_materia(materias):
    """
    Permite ingresar una nueva materia y agregarla a la lista de materias.

    Parameters
    ----------
    materias : list
        Lista donde se guardan las materias cargadas.

    Returns
    -------
    list
        Lista actualizada con la nueva materia.
    """

    print()
    print("=============================================")
    print("              CARGAR MATERIA                 ")
    print("=============================================")

    nombre_materia = input("Ingrese el nombre de la materia: ").strip()

    if nombre_materia == "":
        print("El nombre de la materia no puede estar vacío.")
        return materias

    if nombre_materia.lower() in [materia.lower() for materia in materias]:
        print("Esa materia ya fue cargada anteriormente.")
        return materias

    materias.append(nombre_materia)
    print(f"Materia '{nombre_materia}' cargada exitosamente.")

    return materias


def mostrar_materias(materias):
    """
    Muestra las materias cargadas.

    Parameters
    ----------
    materias : list
        Lista de materias cargadas.
    """

    print()
    print("=============================================")
    print("             MATERIAS CARGADAS               ")
    print("=============================================")

    if len(materias) == 0:
        print("Todavía no hay materias cargadas.")
    else:
        for numero, materia in enumerate(materias, start=1):
            print(f"{numero}. {materia}")
