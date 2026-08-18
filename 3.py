def calcular_metricas(*numeros, **opciones):
    
    operacion = opciones.get("operacion", "suma")
    
    if operacion == "suma":
        resultado = sum(numeros)
        
    elif operacion == "promedio":
        resultado = sum(numeros) / len(numeros)
        
    else:
        return "Error: operación no válida."
    
    if "redondear" in opciones:
        redondear = opciones["redondear"]
        
        if redondear is True:
            resultado = round(resultado, 2)
        elif isinstance(redondear, int):
            resultado = round(resultado, redondear)
    
    return resultado
