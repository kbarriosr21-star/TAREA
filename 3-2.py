def auditar_evento(nivel, *etiquetas, **metadatos):

    registro = f"[{nivel}]"

    if etiquetas:
        tags = [f"#{etiqueta}" for etiqueta in etiquetas]
        registro += f" Tags: {', '.join(tags)}"

    if metadatos:
        datos = ", ".join(
            f"{clave}: {valor}"
            for clave, valor in metadatos.items()
        )
        registro += f" | Metadatos -> {datos}"

    print(registro)


auditar_evento(
    "ERROR",
    "seguridad",
    "auth",
    usuario="admin",
    ip="192.168.1.50",
    intento=3
)

auditar_evento("INFO")

auditar_evento("WARNING", "seguridad", "login")
