from datetime import datetime


def pedir_texto(mensaje):
    """
    Solicita un texto al usuario y verifica que no esté vacío.

    Parametros:
    
    mensaje : str
        Mensaje que se muestra al usuario.

    Returns:
    
    str
        Texto ingresado por el usuario.
    """

    while True:
        texto = input(mensaje).strip()

        if texto != "":
            return texto
        else:
            print("Error: el campo no puede estar vacío.")


def pedir_entero(mensaje):
    """
    Solicita un número entero al usuario.

    Parametros:
    
    mensaje : str
        Mensaje que se muestra al usuario.

    Returns:
    
    int
        Número entero ingresado por el usuario.
    """

    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: debe ingresar un número entero válido.")


def pedir_entero_en_rango(mensaje, minimo, maximo):
    """
    Solicita un número entero dentro de un rango determinado.

    Parametros:
    
    mensaje : str
        Mensaje que se muestra al usuario.
    minimo : int
        Valor mínimo permitido.
    maximo : int
        Valor máximo permitido.

    Returns:
    
    int
        Número entero válido dentro del rango.
    """

    while True:
        numero = pedir_entero(mensaje)

        if minimo <= numero <= maximo:
            return numero
        else:
            print(f"Error: el número debe estar entre {minimo} y {maximo}.")


def validar_fecha(fecha):
    """
    Verifica que una fecha tenga el formato correcto AAAA-MM-DD.

    Parametros:
    
    fecha : str
        Fecha ingresada por el usuario.

    Returns:
    
    bool
        True si la fecha es válida, False si no lo es.
    """

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def pedir_fecha(mensaje):
    """
    Solicita una fecha al usuario hasta que tenga el formato correcto.

    Parametros:
    
    mensaje : str
        Mensaje que se muestra al usuario.

    Returns:
    
    str
        Fecha válida en formato AAAA-MM-DD.
    """

    while True:
        fecha = input(mensaje).strip()

        if validar_fecha(fecha):
            return fecha
        else:
            print("Error: la fecha debe tener el formato AAAA-MM-DD. Ejemplo: 2026-06-19")


def validar_porcentaje(porcentaje):
    """
    Verifica que un porcentaje esté entre 0 y 100.

    Parametros:
    
    porcentaje : int
        Porcentaje ingresado.

    Returns:
    
    bool
        True si está entre 0 y 100, False si no.
    """

    if 0 <= porcentaje <= 100:
        return True
    else:
        return False


def pedir_porcentaje(mensaje):
    """
    Solicita un porcentaje válido entre 0 y 100.

    Parametros:
    
    mensaje : str
        Mensaje que se muestra al usuario.

    Returns:
    
    int
        Porcentaje válido.
    """

    while True:
        porcentaje = pedir_entero(mensaje)

        if validar_porcentaje(porcentaje):
            return porcentaje
        else:
            print("Error: el porcentaje debe estar entre 0 y 100.")


def validar_nota(nota):
    """
    Verifica que una nota esté entre 0 y 10.

    Parametros:
    
    nota : float
        Nota ingresada.

    Returns:
    
    bool
        True si la nota está entre 0 y 10, False si no.
    """

    if 0 <= nota <= 10:
        return True
    else:
        return False


def pedir_nota(mensaje):
    """
    Solicita una nota válida entre 0 y 10.

    Parametros:
    
    mensaje : str
        Mensaje que se muestra al usuario.

    Returns:
    
    float
        Nota válida.
    """

    while True:
        try:
            nota = float(input(mensaje))

            if validar_nota(nota):
                return nota
            else:
                print("Error: la nota debe estar entre 0 y 10.")

        except ValueError:
            print("Error: debe ingresar un número válido.")
 