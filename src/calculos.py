from datetime import datetime


def calcular_dias_restantes(fecha_limite):
    """
    Calcula cuántos días faltan para la fecha límite.

    Parametros:
    
    fecha_limite : str
        Fecha límite en formato AAAA-MM-DD.

    Returns:
    
    int
        Cantidad de días restantes. Si la fecha ya pasó,
        devuelve un número negativo.
    """

    fecha_actual = datetime.today()
    fecha_entrega = datetime.strptime(fecha_limite, "%Y-%m-%d")

    diferencia = fecha_entrega - fecha_actual

    return diferencia.days


def calcular_prioridad(tarea):
    """
    Asigna una prioridad a una tarea según:
    - días restantes
    - dificultad
    - importancia
    - porcentaje de avance

    Parametros:
    
    tarea : dict
        Diccionario con los datos de una tarea.

    Returns:
    
    str
        Prioridad: "Alta", "Media" o "Baja".
    """

    dias_restantes = calcular_dias_restantes(tarea["fecha_limite"])
    dificultad = tarea["dificultad"]
    importancia = tarea["importancia"]
    avance = tarea["avance"]

    puntaje = 0

    if dias_restantes < 0:
        puntaje = puntaje + 4
    elif dias_restantes <= 2:
        puntaje = puntaje + 3
    elif dias_restantes <= 7:
        puntaje = puntaje + 2
    else:
        puntaje = puntaje + 1

    puntaje = puntaje + dificultad
    puntaje = puntaje + importancia

    if avance < 30:
        puntaje = puntaje + 3
    elif avance < 70:
        puntaje = puntaje + 2
    else:
        puntaje = puntaje + 1

    if puntaje >= 12:
        return "Alta"
    elif puntaje >= 8:
        return "Media"
    else:
        return "Baja"


def calcular_riesgo_atraso(tarea):
    """
    Detecta si una tarea tiene riesgo de atraso.

    El riesgo depende de los días restantes y del porcentaje de avance.

    Parametros:
    
    tarea : dict
        Diccionario con los datos de una tarea.

    Returns:
    
    str
        Riesgo: "Alto", "Medio", "Bajo" o "Sin riesgo".
    """

    dias_restantes = calcular_dias_restantes(tarea["fecha_limite"])
    avance = tarea["avance"]

    if tarea["estado"] == "Completada":
        return "Sin riesgo"

    if dias_restantes < 0 and avance < 100:
        return "Alto"

    if dias_restantes <= 2 and avance < 50:
        return "Alto"

    if dias_restantes <= 7 and avance < 50:
        return "Medio"

    if dias_restantes <= 7 and avance < 80:
        return "Bajo"

    return "Sin riesgo"


def calcular_avance_esperado(tarea):
    """
    Estima cuánto debería haber avanzado el usuario según el tiempo disponible.

    Como en las tareas actuales no tenemos fecha de carga, usamos una regla simple:
    - Si faltan más de 14 días, se espera 25% de avance.
    - Si faltan entre 7 y 14 días, se espera 50% de avance.
    - Si faltan entre 3 y 6 días, se espera 75% de avance.
    - Si faltan 2 días o menos, se espera 90% de avance.
    - Si la fecha ya pasó, se espera 100% de avance.

    Parametros:
    
    tarea : dict
        Diccionario con los datos de una tarea.

    Returns:
    
    int
        Porcentaje de avance esperado.
    """

    dias_restantes = calcular_dias_restantes(tarea["fecha_limite"])

    if tarea["estado"] == "Completada":
        return 100

    if dias_restantes < 0:
        return 100
    elif dias_restantes <= 2:
        return 90
    elif dias_restantes <= 6:
        return 75
    elif dias_restantes <= 14:
        return 50
    else:
        return 25


def comparar_avance(tarea):
    """
    Compara el avance real con el avance esperado.

    Parametros:
    
    tarea : dict
        Diccionario con los datos de una tarea.

    Returns:
    
    str
        Mensaje interpretativo sobre el estado del avance.
    """

    avance_real = tarea["avance"]
    avance_esperado = calcular_avance_esperado(tarea)

    if avance_real >= avance_esperado:
        return "Vas al día"
    elif avance_real >= avance_esperado - 20:
        return "Estás levemente atrasado"
    else:
        return "Deberías priorizar esta actividad"


def calcular_promedio_por_materia(tareas):
    """
    Calcula el promedio de notas por materia.

    Solo tiene en cuenta tareas que tengan nota cargada.

    Parametros:
    
    tareas : list
        Lista de tareas.

    Returns:
    
    dict
        Diccionario con el promedio de cada materia.
    """

    notas_por_materia = {}

    for tarea in tareas:
        materia = tarea["materia"]
        nota = tarea["nota"]

        if nota is not None:
            if materia not in notas_por_materia:
                notas_por_materia[materia] = []

            notas_por_materia[materia].append(nota)

    promedios = {}

    for materia in notas_por_materia:
        notas = notas_por_materia[materia]
        suma = 0

        for nota in notas:
            suma = suma + nota

        promedio = suma / len(notas)
        promedios[materia] = promedio

    return promedios


def calcular_promedio_general(tareas):
    """
    Calcula el promedio general del usuario.

    Solo tiene en cuenta tareas que tengan nota cargada.

    Parametros:
    
    tareas : list
        Lista de tareas.

    Returns:
    
    float or None
        Promedio general. Si no hay notas cargadas, devuelve None.
    """

    notas = []

    for tarea in tareas:
        nota = tarea["nota"]

        if nota is not None:
            notas.append(nota)

    if len(notas) == 0:
        return None

    suma = 0

    for nota in notas:
        suma = suma + nota

    promedio = suma / len(notas)

    return promedio


def calcular_cantidad_pendientes(tareas):
    """
    Calcula cuántas tareas están pendientes.

    Parametros:
    
    tareas : list
        Lista de tareas.

    Returns:
    
    int
        Cantidad de tareas pendientes.
    """

    cantidad = 0

    for tarea in tareas:
        if tarea["estado"] != "Completada":
            cantidad = cantidad + 1

    return cantidad


def calcular_cantidad_completadas(tareas):
    """
    Calcula cuántas tareas están completadas.

    Parametros:
    
    tareas : list
        Lista de tareas.

    Returns:
    int
        Cantidad de tareas completadas.
    """

    cantidad = 0

    for tarea in tareas:
        if tarea["estado"] == "Completada":
            cantidad = cantidad + 1

    return cantidad


def calcular_porcentaje_completadas(tareas):
    """
    Calcula qué porcentaje de tareas están completadas.

    Parametros:
    
    tareas : list
        Lista de tareas.

    Returns:
    
    float
        Porcentaje de tareas completadas.
    """

    if len(tareas) == 0:
        return 0

    completadas = calcular_cantidad_completadas(tareas)

    porcentaje = (completadas / len(tareas)) * 100

    return porcentaje


def ordenar_tareas_por_prioridad(tareas):
    """
    Ordena las tareas según prioridad: Alta, Media y Baja.

    No se usa sorted ni lambda. Se crean tres listas separadas
    y luego se unen.

    Parametros:
    
    tareas : list
        Lista de tareas.

    Returns:
    
    list
        Lista de tareas ordenada por prioridad.
    """

    tareas_alta = []
    tareas_media = []
    tareas_baja = []

    for tarea in tareas:
        prioridad = calcular_prioridad(tarea)

        if prioridad == "Alta":
            tareas_alta.append(tarea)
        elif prioridad == "Media":
            tareas_media.append(tarea)
        else:
            tareas_baja.append(tarea)

    tareas_ordenadas = tareas_alta + tareas_media + tareas_baja

    return tareas_ordenadas

    

   