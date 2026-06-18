from src.validaciones import (
    pedir_texto,
    pedir_entero_en_rango,
    pedir_fecha,
    pedir_porcentaje,
    pedir_nota
)

from src.materias import mostrar_materias


def registrar_tarea(tareas, materias):
    """
    Permite cargar una nueva actividad académica.

    La actividad puede ser una tarea, parcial o entrega. Se guarda como
    un diccionario dentro de la lista de tareas.

  Parametros:
    
    tareas : list
        Lista donde se guardan las actividades académicas.
    materias : list
        Lista de materias cargadas previamente.

    Returns:
  
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
    mostrar_materias(materias)

    opcion_materia = pedir_entero_en_rango("Seleccione el número de la materia: ",1,len(materias))

    materia_elegida = materias[opcion_materia - 1]

    tipo = pedir_tipo_actividad()

    descripcion = pedir_texto("Ingrese una descripción de la actividad: ")

    fecha_limite = pedir_fecha("Ingrese la fecha límite (AAAA-MM-DD): ")

    dificultad = pedir_entero_en_rango("Ingrese la dificultad del 1 al 5: ",1,5)

    importancia = pedir_entero_en_rango("Ingrese la importancia del 1 al 5: ",1,5)

    avance = pedir_porcentaje("Ingrese el porcentaje de avance entre 0 y 100: ")
    
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


def pedir_tipo_actividad():
    """
    Solicita el tipo de actividad y verifica que sea válido.

    Los tipos permitidos son: tarea, parcial o entrega.

    Returns
 
    str
        Tipo de actividad válido.
    """

    while True:
        tipo = pedir_texto("Ingrese el tipo de actividad (tarea/parcial/entrega): ")
        tipo = tipo.lower()

        if tipo in ["tarea", "parcial", "entrega"]:
            return tipo
        else:
            print("El tipo debe ser: tarea, parcial o entrega.")


def mostrar_tareas_segun_estado(tareas, estado_a_mostrar):
    """
    Muestra las actividades que todavía no fueron completadas.

    Parametros: 
    
    tareas : list
        Lista de actividades académicas.
    """

    print()
    print("=============================================")
    print("             TAREAS {estado_a_mostrar.upper()}               ")
    print("=============================================")

    tareas_filtradas = []

    for tarea in tareas:
        if tarea["estado"] == estado_a_mostrar:
            tareas_filtradas.append(tarea)

    if len(tareas_filtradas) == 0:
        print(f"No hay tareas en el estado {estado_a_mostrar}.")
    else:
        for tarea in tareas_filtradas:
            imprimir_tarea(tarea)
            

def actualizar_avance(tareas):
    """
    Permite modificar el porcentaje de avance de una actividad.

    Si el avance nuevo es 100, la tarea pasa automáticamente a estado
    'Completada'. Si el avance es menor a 100, queda como 'Pendiente'.

    Parametros:
    
    tareas : list
        Lista de actividades académicas.

    Returns:
    
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

    mostrar_resumen_tareas(tareas)

    tarea_encontrada = seleccionar_tarea_por_id(tareas)

    nuevo_avance = pedir_porcentaje("Ingrese el nuevo porcentaje de avance entre 0 y 100: ")

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

    Parametros:
    
    tareas : list
        Lista de actividades académicas.

    Returns
    
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

    mostrar_resumen_tareas(tareas)

    tarea_encontrada = seleccionar_tarea_por_id(tareas)

    tarea_encontrada["avance"] = 100
    tarea_encontrada["estado"] = "Completada"

    print("La tarea fue marcada como completada.")

    return tareas


def cargar_nota(tareas):
    """
    Permite registrar una nota obtenida en una actividad académica.

    Parametros:
    
    tareas : list
        Lista de actividades académicas.

    Returns:
    
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

    mostrar_resumen_tareas(tareas)

    tarea_encontrada = seleccionar_tarea_por_id(tareas)

    nota = pedir_nota("Ingrese la nota obtenida entre 0 y 10: ")

    tarea_encontrada["nota"] = nota

    print("Nota cargada exitosamente.")

    return tareas


def seleccionar_tarea_por_id(tareas):
    """
    Solicita al usuario un ID de tarea y devuelve la tarea correspondiente.

    Parametros:
    
    tareas : list
        Lista de actividades académicas.

    Returns:
    
    dict
        Tarea encontrada.
    """

    while True:
        id_tarea = pedir_entero_en_rango("Ingrese el ID de la tarea: ", 1,len(tareas))

        for tarea in tareas:
            if tarea["id"] == id_tarea:
                return tarea

        print("No existe una tarea con ese ID.")


def mostrar_resumen_tareas(tareas):
    """
    Muestra un resumen breve de todas las tareas cargadas.

    Parametros:
    
    tareas : list
        Lista de actividades académicas.
    """

    for tarea in tareas:
       print(f"{tarea['id']}. {tarea['materia']} - {tarea['descripcion']} - Avance: {tarea['avance']}% - Estado: {tarea['estado']}")


def imprimir_tarea(tarea):
    """
    Imprime en pantalla la información completa de una tarea.

    Parametros:
    
    tarea : dict
        Diccionario con los datos de una actividad académica.
    """

    print(f"ID: {tarea['id']}")
    print(f"Materia: {tarea['materia']}")
    print(f"Tipo: {tarea['tipo']}")
    print(f"Descripción: {tarea['descripcion']}")
    print(f"Fecha límite: {tarea['fecha_limite']}")
    print(f"Dificultad: {tarea['dificultad']}")
    print(f"Importancia: {tarea['importancia']}")
    print(f"Avance: {tarea['avance']}%")
    print(f"Nota: {tarea['nota']}")
    print(f"Estado: {tarea['estado']}")
    print("---------------------------------------------")