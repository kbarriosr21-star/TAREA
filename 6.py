def buscar_clave_profunda(estructura, clave_objetivo):

    for clave, valor in estructura.items():

        if clave == clave_objetivo:
            return valor

        if isinstance(valor, dict):
            resultado = buscar_clave_profunda(valor, clave_objetivo)

            if resultado is not None:
                return resultado

    return None


datos = {
    "usuario": {
        "nombre": "Carlos",
        "informacion": {
            "edad": 25,
            "direccion": {
                "ciudad": "Cartagena",
                "codigo_postal": "130001"
            }
        }
    }
}


print(buscar_clave_profunda(datos, "ciudad"))
print(buscar_clave_profunda(datos, "edad"))
print(buscar_clave_profunda(datos, "telefono"))
