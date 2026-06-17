def registrar_tarea(tareas, materias):
    """
    Permite cargar una nueva actividad académica.

    La actividad puede ser una tarea, parcial o entrega. Se guarda como
    un diccionario dentro de la lista de tareas.

    Parameters
    ----------
    tareas : list
        Lista donde se guardan las actividades académicas.
    materias : list
        Lista de materias cargadas previamente.

    Returns
    -------
    list
        Lista de tareas actualizada.
    """

    print()
    print("=============================================")
    print("              REGISTRAR TAREA                ")
    print("=============================================")

    if len(materias) == 0:
        print("Primero debe cargar al menos una materia.")
        return tareas

    print("Materias disponibles:")
    for numero, materia in enumerate(materias, start=1):
        print(f"{numero}. {materia}")

    while True:
        try:
            opcion_materia = int(input("Seleccione el número de la materia: "))

            if 1 <= opcion_materia <= len(materias):
                materia_elegida = materias[opcion_materia - 1]
                break
            else:
                print("La opción ingresada no corresponde a una materia existente.")

        except ValueError:
            print("Debe ingresar un número válido.")

    while True:
        tipo = input("Ingrese el tipo de actividad (tarea/parcial/entrega): ").strip().lower()

        if tipo in ["tarea", "parcial", "entrega"]:
            break
        else:
            print("El tipo debe ser: tarea, parcial o entrega.")

    while True:
        descripcion = input("Ingrese una descripción de la actividad: ").strip()

        if descripcion != "":
            break
        else:
            print("La descripción no puede estar vacía.")

    while True:
        fecha_limite = input("Ingrese la fecha límite (AAAA-MM-DD): ").strip()

        if fecha_limite != "":
            break
        else:
            print("La fecha límite no puede estar vacía.")

    while True:
        try:
            dificultad = int(input("Ingrese la dificultad del 1 al 5: "))

            if 1 <= dificultad <= 5:
                break
            else:
                print("La dificultad debe estar entre 1 y 5.")

        except ValueError:
            print("Debe ingresar un número válido.")

    while True:
        try:
            importancia = int(input("Ingrese la importancia del 1 al 5: "))

            if 1 <= importancia <= 5:
                break
            else:
                print("La importancia debe estar entre 1 y 5.")

        except ValueError:
            print("Debe ingresar un número válido.")

    while True:
        try:
            avance = int(input("Ingrese el porcentaje de avance entre 0 y 100: "))

            if 0 <= avance <= 100:
                break
            else:
                print("El avance debe estar entre 0 y 100.")

        except ValueError:
            print("Debe ingresar un número válido.")

    if avance == 100:
        estado = "Completada"
    else:
        estado = "Pendiente"

    nueva_tarea = {
        "id": len(tareas) + 1,
        "materia": materia_elegida,
        "tipo": tipo,
        "descripcion": descripcion,
        "fecha_limite": fecha_limite,
        "dificultad": dificultad,
        "importancia": importancia,
        "avance": avance,
        "nota": None,
        "estado": estado
    }

    tareas.append(nueva_tarea)

    print("Actividad registrada exitosamente.")

    return tareas


def mostrar_tareas_pendientes(tareas):
    """
    Muestra las actividades que todavía no fueron completadas.

    Parameters
    ----------
    tareas : list
        Lista de actividades académicas.
    """

    print()
    print("=============================================")
    print("             TAREAS PENDIENTES               ")
    print("=============================================")

    pendientes = []

    for tarea in tareas:
        if tarea["estado"] != "Completada":
            pendientes.append(tarea)

    if len(pendientes) == 0:
        print("No hay tareas pendientes.")
    else:
        for tarea in pendientes:
            print(f"ID: {tarea['id']}")
            print(f"Materia: {tarea['materia']}")
            print(f"Tipo: {tarea['tipo']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Fecha límite: {tarea['fecha_limite']}")
            print(f"Dificultad: {tarea['dificultad']}")
            print(f"Importancia: {tarea['importancia']}")
            print(f"Avance: {tarea['avance']}%")
            print(f"Estado: {tarea['estado']}")
            print("---------------------------------------------")


def mostrar_tareas_completadas(tareas):
    """
    Muestra las actividades que ya fueron finalizadas.

    Parameters
    ----------
    tareas : list
        Lista de actividades académicas.
    """

    print()
    print("=============================================")
    print("            TAREAS COMPLETADAS               ")
    print("=============================================")

    completadas = []

    for tarea in tareas:
        if tarea["estado"] == "Completada":
            completadas.append(tarea)

    if len(completadas) == 0:
        print("No hay tareas completadas.")
    else:
        for tarea in completadas:
            print(f"ID: {tarea['id']}")
            print(f"Materia: {tarea['materia']}")
            print(f"Tipo: {tarea['tipo']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Fecha límite: {tarea['fecha_limite']}")
            print(f"Avance: {tarea['avance']}%")
            print(f"Nota: {tarea['nota']}")
            print(f"Estado: {tarea['estado']}")
            print("---------------------------------------------")


def actualizar_avance(tareas):
    """
    Permite modificar el porcentaje de avance de una actividad.

    Si el avance nuevo es 100, la tarea pasa automáticamente a estado
    'Completada'. Si el avance es menor a 100, queda como 'Pendiente'.

    Parameters
    ----------
    tareas : list
        Lista de actividades académicas.

    Returns
    -------
    list
        Lista de tareas actualizada.
    """

    print()
    print("=============================================")
    print("              ACTUALIZAR AVANCE              ")
    print("=============================================")

    if len(tareas) == 0:
        print("No hay tareas cargadas.")
        return tareas

    for tarea in tareas:
        print(f"{tarea['id']}. {tarea['materia']} - {tarea['descripcion']} - Avance: {tarea['avance']}%")

    while True:
        try:
            id_tarea = int(input("Ingrese el ID de la tarea que desea actualizar: "))

            tarea_encontrada = None

            for tarea in tareas:
                if tarea["id"] == id_tarea:
                    tarea_encontrada = tarea
                    break

            if tarea_encontrada is not None:
                break
            else:
                print("No existe una tarea con ese ID.")

        except ValueError:
            print("Debe ingresar un número válido.")

    while True:
        try:
            nuevo_avance = int(input("Ingrese el nuevo porcentaje de avance entre 0 y 100: "))

            if 0 <= nuevo_avance <= 100:
                break
            else:
                print("El avance debe estar entre 0 y 100.")

        except ValueError:
            print("Debe ingresar un número válido.")

    tarea_encontrada["avance"] = nuevo_avance

    if nuevo_avance == 100:
        tarea_encontrada["estado"] = "Completada"
    else:
        tarea_encontrada["estado"] = "Pendiente"

    print("Avance actualizado exitosamente.")

    return tareas


def marcar_tarea_completada(tareas):
    """
    Cambia el estado de una actividad a completada.

    También modifica el avance de la tarea a 100%.

    Parameters
    ----------
    tareas : list
        Lista de actividades académicas.

    Returns
    -------
    list
        Lista de tareas actualizada.
    """

    print()
    print("=============================================")
    print("          MARCAR TAREA COMPLETADA            ")
    print("=============================================")

    if len(tareas) == 0:
        print("No hay tareas cargadas.")
        return tareas

    for tarea in tareas:
        print(f"{tarea['id']}. {tarea['materia']} - {tarea['descripcion']} - Estado: {tarea['estado']}")

    while True:
        try:
            id_tarea = int(input("Ingrese el ID de la tarea que desea marcar como completada: "))

            tarea_encontrada = None

            for tarea in tareas:
                if tarea["id"] == id_tarea:
                    tarea_encontrada = tarea
                    break

            if tarea_encontrada is not None:
                break
            else:
                print("No existe una tarea con ese ID.")

        except ValueError:
            print("Debe ingresar un número válido.")

    tarea_encontrada["avance"] = 100
    tarea_encontrada["estado"] = "Completada"

    print("La tarea fue marcada como completada.")

    return tareas


def cargar_nota(tareas):
    """
    Permite registrar una nota obtenida en una actividad académica.

    Parameters
    ----------
    tareas : list
        Lista de actividades académicas.

    Returns
    -------
    list
        Lista de tareas actualizada.
    """

    print()
    print("=============================================")
    print("                CARGAR NOTA                  ")
    print("=============================================")

    if len(tareas) == 0:
        print("No hay tareas cargadas.")
        return tareas

    for tarea in tareas:
        print(f"{tarea['id']}. {tarea['materia']} - {tarea['descripcion']} - Nota actual: {tarea['nota']}")

    while True:
        try:
            id_tarea = int(input("Ingrese el ID de la tarea a la que desea cargarle una nota: "))

            tarea_encontrada = None

            for tarea in tareas:
                if tarea["id"] == id_tarea:
                    tarea_encontrada = tarea
                    break

            if tarea_encontrada is not None:
                break
            else:
                print("No existe una tarea con ese ID.")

        except ValueError:
            print("Debe ingresar un número válido.")

    while True:
        try:
            nota = float(input("Ingrese la nota obtenida entre 0 y 10: "))

            if 0 <= nota <= 10:
                break
            else:
                print("La nota debe estar entre 0 y 10.")

        except ValueError:
            print("Debe ingresar un número válido.")

    tarea_encontrada["nota"] = nota

    print("Nota cargada exitosamente.")

    return tareas
