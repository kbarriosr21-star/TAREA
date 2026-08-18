def generar_reporte(titulo, *secciones, **firmas):
    print("Título:", titulo)
    print("Secciones:", secciones)
    print("Firmas:", firmas)


secciones_basicas = (
    "Introducción",
    "Resultados"
)

secciones_adicionales = [
    "Conclusiones",
    "Recomendaciones"
]

generar_reporte(
    "Informe anual",
    *secciones_basicas,
    *secciones_adicionales
)
