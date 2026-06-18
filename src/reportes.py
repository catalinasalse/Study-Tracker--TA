from src.calculos import (
    calcular_dias_restantes,
    calcular_prioridad,
    calcular_riesgo_atraso,
    comparar_avance,
    calcular_promedio_por_materia,
    calcular_promedio_general,
    calcular_cantidad_pendientes,
    calcular_cantidad_completadas,
    calcular_porcentaje_completadas,
    ordenar_tareas_por_prioridad
)


def mostrar_alertas_proximas(tareas):
    """
    Muestra actividades que vencen pronto.

    Se consideran próximas las tareas que vencen dentro de los próximos 7 días
    y que todavía no están completadas.

    Parametros:
    
    tareas : list
        Lista de tareas cargadas.
    """

    print()
    print("=============================================")
    print("             ALERTAS PRÓXIMAS                ")
    print("=============================================")

    if len(tareas) == 0:
        print("No hay tareas cargadas.")
        return

    hay_alertas = False

    for tarea in tareas:
        dias_restantes = calcular_dias_restantes(tarea["fecha_limite"])

        if tarea["estado"] != "Completada" and dias_restantes <= 7:
            hay_alertas = True

            print(f"ID: {tarea['id']}")
            print(f"Materia: {tarea['materia']}")
            print(f"Tipo: {tarea['tipo']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Fecha límite: {tarea['fecha_limite']}")

            if dias_restantes < 0:
                print("Estado de fecha: vencida")
            elif dias_restantes == 0:
                print("Estado de fecha: vence hoy")
            elif dias_restantes == 1:
                print("Estado de fecha: vence mañana")
            else:
                print(f"Estado de fecha: vence en {dias_restantes} días")

            print("---------------------------------------------")

    if hay_alertas == False:
        print("No hay actividades próximas a vencer.")


def mostrar_recomendaciones(tareas):
    """
    Recomienda qué hacer con cada tarea

    La recomendación se basa en la prioridad, el riesgo de atraso
    y la comparación entre avance real y avance esperado.

    Parametros:
    
    tareas : list
        Lista de tareas cargadas.
    """

    print()
    print("=============================================")
    print("              RECOMENDACIONES                ")
    print("=============================================")

    if len(tareas) == 0:
        print("No hay tareas cargadas.")
        return

    tareas_ordenadas = ordenar_tareas_por_prioridad(tareas)

    hay_pendientes = False

    for tarea in tareas_ordenadas:
        if tarea["estado"] != "Completada":
            hay_pendientes = True

            prioridad = calcular_prioridad(tarea)
            riesgo = calcular_riesgo_atraso(tarea)
            mensaje_avance = comparar_avance(tarea)
            dias_restantes = calcular_dias_restantes(tarea["fecha_limite"])

            print(f"ID: {tarea['id']}")
            print(f"Materia: {tarea['materia']}")
            print(f"Actividad: {tarea['tipo']} - {tarea['descripcion']}")
            print(f"Prioridad: {prioridad}")
            print(f"Riesgo de atraso: {riesgo}")
            print(f"Avance actual: {tarea['avance']}%")
            print(f"Comentario: {mensaje_avance}")

            if dias_restantes < 0:
                print("Recomendación: esta actividad ya venció. Deberías revisarla primero.")
            elif prioridad == "Alta":
                print("Recomendación: deberías priorizar esta actividad.")
            elif prioridad == "Media":
                print("Recomendación: conviene avanzar con esta actividad durante la semana.")
            else:
                print("Recomendación: esta actividad puede esperar un poco más.")

            print("---------------------------------------------")

    if hay_pendientes == False:
        print("No hay tareas pendientes. Tenés todo completado.")


def mostrar_metricas_generales(tareas):
    """
    Muestra un resumen del estado académico del usuario.

    Incluye cantidad de tareas, pendientes, completadas, porcentaje
    de completadas y promedios.

    Parametros:
   
    tareas : list
        Lista de tareas cargadas.
    """

    print()
    print("=============================================")
    print("             MÉTRICAS GENERALES              ")
    print("=============================================")

    if len(tareas) == 0:
        print("No hay tareas cargadas.")
        return

    total_tareas = len(tareas)
    pendientes = calcular_cantidad_pendientes(tareas)
    completadas = calcular_cantidad_completadas(tareas)
    porcentaje_completadas = calcular_porcentaje_completadas(tareas)
    promedio_general = calcular_promedio_general(tareas)
    promedios_materia = calcular_promedio_por_materia(tareas)

    print(f"Cantidad total de actividades: {total_tareas}")
    print(f"Cantidad de actividades pendientes: {pendientes}")
    print(f"Cantidad de actividades completadas: {completadas}")
    print(f"Porcentaje de actividades completadas: {porcentaje_completadas}%")

    if promedio_general == None:
        print("Promedio general: todavía no hay notas cargadas.")
    else:
        print(f"Promedio general: {promedio_general}")

    print()
    print("Promedio por materia:")

    if len(promedios_materia) == 0:
        print("Todavía no hay notas cargadas por materia.")
    else:
        for materia,promedio_materia in promedios_materia.items():
            print(f"{materia}: {promedio_materia}")

    print("---------------------------------------------")


def mostrar_tareas_por_prioridad(tareas):
    """
    Muestra las actividades ordenadas según prioridad.

    Primero aparecen las de prioridad alta, luego media y finalmente baja.

    Parametros:
   
    tareas : list
        Lista de tareas cargadas.
    """

    print()
    print("=============================================")
    print("           TAREAS POR PRIORIDAD              ")
    print("=============================================")

    if len(tareas) == 0:
        print("No hay tareas cargadas.")
        return

    tareas_ordenadas = ordenar_tareas_por_prioridad(tareas)

    hay_tareas = False

    for tarea in tareas_ordenadas:
        if tarea["estado"] != "Completada":
            hay_tareas = True

            prioridad = calcular_prioridad(tarea)
            riesgo = calcular_riesgo_atraso(tarea)
            dias_restantes = calcular_dias_restantes(tarea["fecha_limite"])

            print(f"ID: {tarea['id']}")
            print(f"Materia: {tarea['materia']}")
            print(f"Tipo: {tarea['tipo']}")
            print(f"Descripción: {tarea['descripcion']}")
            print(f"Fecha límite: {tarea['fecha_limite']}")
            print(f"Días restantes: {dias_restantes}")
            print(f"Dificultad: {tarea['dificultad']}")
            print(f"Importancia: {tarea['importancia']}")
            print(f"Avance: {tarea['avance']}%")
            print(f"Prioridad: {prioridad}")
            print(f"Riesgo de atraso: {riesgo}")
            print("---------------------------------------------")

    if hay_tareas == False:
        print("No hay tareas pendientes para ordenar por prioridad.")
