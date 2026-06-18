

import os
import matplotlib.pyplot as plt

from src.calculos import calcular_prioridad, calcular_promedio_por_materia


RUTA_CARPETA_GRAFICOS = "graficos"


def crear_carpeta_graficos():
    """
    Crea la carpeta 'graficos' si no existe.

    Returns:
    None
    """

    if not os.path.exists(RUTA_CARPETA_GRAFICOS):
        os.makedirs(RUTA_CARPETA_GRAFICOS)


def grafico_tareas_por_materia(tareas):
    """
    Genera un gráfico de barras con la cantidad de tareas por materia.

    Parametros:
    tareas : list
        Lista de tareas cargadas.

    Returns:
    None
    """

    print()
    print("Generando gráfico de tareas por materia...")

    if len(tareas) == 0:
        print("No hay tareas cargadas para graficar.")
        return

    crear_carpeta_graficos()

    tareas_por_materia = {}

    for tarea in tareas:
        materia = tarea["materia"]

        if materia not in tareas_por_materia:
            tareas_por_materia[materia] = 0

        tareas_por_materia[materia] = tareas_por_materia[materia] + 1

    materias = []
    cantidades = []

    for materia in tareas_por_materia:
        materias.append(materia)
        cantidades.append(tareas_por_materia[materia])

    plt.figure()
    plt.bar(materias, cantidades)
    plt.title("Cantidad de tareas por materia")
    plt.xlabel("Materia")
    plt.ylabel("Cantidad de tareas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("graficos/tareas_por_materia.png")
    plt.show()

    print("Gráfico guardado en graficos/tareas_por_materia.png")


def grafico_estado_tareas(tareas):
    """
    Genera un gráfico circular con la proporción de tareas pendientes
    y completadas.

    Parametros:
    tareas : list
        Lista de tareas cargadas.

    Returns:
    None
    """

    print()
    print("Generando gráfico de estado de tareas...")

    if len(tareas) == 0:
        print("No hay tareas cargadas para graficar.")
        return

    crear_carpeta_graficos()

    pendientes = 0
    completadas = 0

    for tarea in tareas:
        if tarea["estado"] == "Completada":
            completadas = completadas + 1
        else:
            pendientes = pendientes + 1

    etiquetas = ["Pendientes", "Completadas"]
    cantidades = [pendientes, completadas]

    plt.figure()
    plt.pie(cantidades, labels=etiquetas, autopct="%1.1f%%")
    plt.title("Estado de las tareas")
    plt.tight_layout()
    plt.savefig("graficos/estado_tareas.png")
    plt.show()

    print("Gráfico guardado en graficos/estado_tareas.png")


def grafico_prioridades(tareas):
    """
    Genera un gráfico de barras con la cantidad de actividades según
    prioridad alta, media o baja.

    Parametros:
    tareas : list
        Lista de tareas cargadas.

    Returns:
    None
    """

    print()
    print("Generando gráfico de prioridades...")

    if len(tareas) == 0:
        print("No hay tareas cargadas para graficar.")
        return

    crear_carpeta_graficos()

    cantidad_alta = 0
    cantidad_media = 0
    cantidad_baja = 0

    for tarea in tareas:
        if tarea["estado"] != "Completada":
            prioridad = calcular_prioridad(tarea)

            if prioridad == "Alta":
                cantidad_alta = cantidad_alta + 1
            elif prioridad == "Media":
                cantidad_media = cantidad_media + 1
            else:
                cantidad_baja = cantidad_baja + 1

    prioridades = ["Alta", "Media", "Baja"]
    cantidades = [cantidad_alta, cantidad_media, cantidad_baja]

    plt.figure()
    plt.bar(prioridades, cantidades)
    plt.title("Cantidad de tareas por prioridad")
    plt.xlabel("Prioridad")
    plt.ylabel("Cantidad de tareas")
    plt.tight_layout()
    plt.savefig("graficos/prioridades.png")
    plt.show()

    print("Gráfico guardado en graficos/prioridades.png")


def grafico_promedio_por_materia(tareas):
    """
    Genera un gráfico de barras con los promedios de notas por materia.

    Parametros:
    tareas : list
        Lista de tareas cargadas.

    Returns:
    None
    """

    print()
    print("Generando gráfico de promedio por materia...")

    if len(tareas) == 0:
        print("No hay tareas cargadas para graficar.")
        return

    crear_carpeta_graficos()

    promedios = calcular_promedio_por_materia(tareas)

    if len(promedios) == 0:
        print("No hay notas cargadas para generar este gráfico.")
        return

    materias = []
    notas = []

    for materia in promedios:
        materias.append(materia)
        notas.append(promedios[materia])

    plt.figure()
    plt.bar(materias, notas)
    plt.title("Promedio por materia")
    plt.xlabel("Materia")
    plt.ylabel("Promedio")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("graficos/promedio_por_materia.png")
    plt.show()

    print("Gráfico guardado en graficos/promedio_por_materia.png")


def generar_graficos(tareas):
    """
    Ejecuta la generación de todos los gráficos disponibles.

    Parametros:
    tareas : list
        Lista de tareas cargadas.

    Returns:
    None
    """

    print()
    print("=============================================")
    print("              GENERAR GRÁFICOS               ")
    print("=============================================")

    if len(tareas) == 0:
        print("No hay tareas cargadas para generar gráficos.")
        return

    grafico_tareas_por_materia(tareas)
    grafico_estado_tareas(tareas)
    grafico_prioridades(tareas)
    grafico_promedio_por_materia(tareas)

    print()
    print("Todos los gráficos disponibles fueron generados.")
