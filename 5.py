def procesar_coleccion(lista_datos, funcion_transformacion, funcion_filtro):
    resultado = []

    for dato in lista_datos:
        if funcion_filtro(dato):
            resultado.append(funcion_transformacion(dato))

    return resultado


es_par = lambda numero: numero % 2 == 0
duplicar = lambda numero: numero * 2


numeros = [1, 2, 3, 4, 5, 6]

resultado = procesar_coleccion(
    numeros,
    duplicar,
    es_par
)

print(resultado)
