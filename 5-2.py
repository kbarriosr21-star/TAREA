def ejecutar_mision(nombre_tarea, al_exito=None, al_error=None):
    try:
        if nombre_tarea == "":
            raise ValueError("El nombre de la tarea está vacío")

        resultado = "Tarea completada correctamente"

        if al_exito:
            al_exito(nombre_tarea, resultado)

    except Exception as error:
        if al_error:
            al_error(nombre_tarea, str(error))


def mostrar_exito(nombre_tarea, resultado):
    print(f"Éxito: {nombre_tarea} - {resultado}")


def mostrar_error(nombre_tarea, mensaje_error):
    print(f"Error: {nombre_tarea} - {mensaje_error}")


ejecutar_mision(
    "Procesar datos",
    al_exito=mostrar_exito,
    al_error=mostrar_error
)
