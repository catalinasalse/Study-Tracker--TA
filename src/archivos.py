
import os
import pandas as pd


RUTA_CARPETA_ARCHIVOS = "archivos"
RUTA_MATERIAS = os.path.join(RUTA_CARPETA_ARCHIVOS, "materias.csv")
RUTA_TAREAS = os.path.join(RUTA_CARPETA_ARCHIVOS, "tareas.csv")


def crear_archivos_si_no_existen():
    """
    Crea la carpeta 'archivos' y los archivos CSV necesarios si no existen.

    Returns:
    None
    """

    if not os.path.exists(RUTA_CARPETA_ARCHIVOS):
        os.makedirs(RUTA_CARPETA_ARCHIVOS)

    if not os.path.exists(RUTA_MATERIAS):
        df_materias = pd.DataFrame(columns=["materia"])
        df_materias.to_csv(RUTA_MATERIAS, index=False)

    if not os.path.exists(RUTA_TAREAS):
        df_tareas = pd.DataFrame(columns=[
            "id",
            "materia",
            "tipo",
            "descripcion",
            "fecha_limite",
            "dificultad",
            "importancia",
            "avance",
            "nota",
            "estado"
        ])
        df_tareas.to_csv(RUTA_TAREAS, index=False)


def leer_materias():
    """
    Lee las materias guardadas en el archivo materias.csv.

    Returns:
    list
        Lista con los nombres de las materias guardadas.
    """

    crear_archivos_si_no_existen()

    try:
        df = pd.read_csv(RUTA_MATERIAS)

        if df.empty:
            return []

        materias = df["materia"].dropna().tolist()
        return materias

    except FileNotFoundError:
        return []


def guardar_materia(materia):
    """
    Guarda una nueva materia en el archivo materias.csv.

    Parametros:
    materia : str
        Nombre de la materia que se quiere guardar.

    Returns:
    None
    """

    crear_archivos_si_no_existen()

    materias = leer_materias()

    if materia in materias:
        print("Esa materia ya está cargada.")
    else:
        nueva_fila = pd.DataFrame([{"materia": materia}])
        nueva_fila.to_csv(RUTA_MATERIAS, mode="a", header=False, index=False)
        print("Materia guardada correctamente.")


def leer_tareas():
    """
    Lee las tareas guardadas en el archivo tareas.csv.

    Returns:
    list
        Lista de diccionarios con las tareas guardadas.
    """

    crear_archivos_si_no_existen()

    try:
        df = pd.read_csv(RUTA_TAREAS)

        if df.empty:
            return []

        tareas = df.to_dict("records")

        for tarea in tareas:
            tarea["id"] = int(tarea["id"])
            tarea["dificultad"] = int(tarea["dificultad"])
            tarea["importancia"] = int(tarea["importancia"])
            tarea["avance"] = int(tarea["avance"])

            if pd.isna(tarea["nota"]):
                tarea["nota"] = None
            else:
                tarea["nota"] = float(tarea["nota"])

        return tareas

    except FileNotFoundError:
        return []


def guardar_tarea(tarea):
    """
    Guarda una nueva tarea en el archivo tareas.csv.

    Parametros:
    tarea : dict
        Diccionario con los datos de la tarea.

    Returns:
    None
    """

    crear_archivos_si_no_existen()

    nueva_fila = pd.DataFrame([tarea])
    nueva_fila.to_csv(RUTA_TAREAS, mode="a", header=False, index=False)

    print("Tarea guardada correctamente.")


def sobrescribir_tareas(tareas):
    """
    Actualiza el archivo tareas.csv luego de modificar datos.

    Se usa cuando se cambia el avance, el estado o la nota de una tarea.

    Parametros:
    tareas : list
        Lista completa de tareas actualizada.

    Returns:
    None
    """

    crear_archivos_si_no_existen()

    df = pd.DataFrame(tareas)
    df.to_csv(RUTA_TAREAS, index=False)

    print("Archivo de tareas actualizado correctamente.")
