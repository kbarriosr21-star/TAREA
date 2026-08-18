def agregar_bitacora(mensaje, historial=None):
    if historial is None:
        historial = []
    
    historial.append(mensaje)
    return historial
