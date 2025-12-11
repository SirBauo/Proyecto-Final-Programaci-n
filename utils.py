def is_number(value):
    """
    Verifica si un valor puede convertirse a número (float).
    Devuelve True si es numérico, False si no lo es.
    """
    try:
        float(value)      # Se intenta convertir a número
        return True
    except:
        return False      # Si falla, el valor no es numérico
