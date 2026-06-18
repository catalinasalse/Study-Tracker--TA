from src.archivos import (
    crear_archivos_si_no_existen,
    leer_materias,
    leer_tareas,
    sobrescribir_tareas
)

from src.materias import (
    cargar_materia,
    mostrar_materias
)

from src.tareas import (
    registrar_tarea,
    mostrar_tareas_pendientes,
    mostrar_tareas_completadas,
    actualizar_avance,
    marcar_tarea_completada,
    cargar_nota
)

from src.reportes import (
    mostrar_alertas_proximas,
    mostrar_recomendaciones,
    mostrar_metricas_generales,
    mostrar_tareas_por_prioridad
)

from src.graficos import generar_graficos


def mostrar_menu():
    """
    Muestra el menú principal del programa.

    Returns:
    
    None
    """

    print()
    print("=============================================")
    print("          STUDY TRACKER INTELIGENTE          ")
    print("=============================================")
    print("1. Cargar materia")
    print("2. Ver materias cargadas")
    print("3. Registrar tarea, parcial o entrega")
    print("4. Ver tareas pendientes")
    print("5. Ver tareas completadas")
    print("6. Actualizar avance de una tarea")
    print("7. Marcar tarea como completada")
    print("8. Cargar nota")
    print("9. Ver tareas ordenadas por prioridad")
    print("10. Ver alertas próximas")
    print("11. Ver recomendaciones")
    print("12. Ver métricas generales")
    print("13. Generar gráficos")
    print("0. Salir")
    print("=============================================")


def pedir_opcion_menu():
    """
    Solicita al usuario una opción del menú principal.

    Returns:
    
    int
        Opción elegida por el usuario.
    """

    while True:
        try:
            opcion = int(input("Ingrese una opción: "))

            if 0 <= opcion <= 13:
                return opcion
            else:
                print("La opción debe estar entre 0 y 13.")

        except ValueError:
            print("Debe ingresar un número válido.")


def main():
    """
    Controla el flujo principal del programa.

    Carga los datos guardados, muestra el menú principal y ejecuta
    la opción elegida por el usuario.

    Returns:
    
    None
    """

    crear_archivos_si_no_existen()

    materias = leer_materias()
    tareas = leer_tareas()

    while True:
        mostrar_menu()
        opcion = pedir_opcion_menu()

        if opcion == 0:
            sobrescribir_tareas(tareas)
            print("¡Fin del programa! Gracias por usar Study Tracker Inteligente.")
            break

        elif opcion == 1:
            materias = cargar_materia(materias)

        elif opcion == 2:
            mostrar_materias(materias)

        elif opcion == 3:
            tareas = registrar_tarea(tareas, materias)
            sobrescribir_tareas(tareas)

        elif opcion == 4:
            mostrar_tareas_pendientes(tareas)

        elif opcion == 5:
            mostrar_tareas_completadas(tareas)

        elif opcion == 6:
            tareas = actualizar_avance(tareas)
            sobrescribir_tareas(tareas)

        elif opcion == 7:
            tareas = marcar_tarea_completada(tareas)
            sobrescribir_tareas(tareas)

        elif opcion == 8:
            tareas = cargar_nota(tareas)
            sobrescribir_tareas(tareas)

        elif opcion == 9:
            mostrar_tareas_por_prioridad(tareas)

        elif opcion == 10:
            mostrar_alertas_proximas(tareas)

        elif opcion == 11:
            mostrar_recomendaciones(tareas)

        elif opcion == 12:
            mostrar_metricas_generales(tareas)

        elif opcion == 13:
            generar_graficos(tareas)


main()
