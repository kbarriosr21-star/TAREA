def aplicar_impuesto(tasa_iva, lista_precios):
  
    tasa_original = tasa_iva
    
    tasa_iva = 0.50

    for i in range(len(lista_precios)):
        lista_precios[i] = lista_precios[i] + (
            lista_precios[i] * tasa_original
        )


tasa_iva = 0.19
lista_precios = [100, 200, 300]

print("ANTES DE LA FUNCIÓN")
print("Tasa IVA:", tasa_iva)
print("Lista de precios:", lista_precios)

aplicar_impuesto(tasa_iva, lista_precios)

print("DESPUÉS DE LA FUNCIÓN")
print("Tasa IVA:", tasa_iva)
print("Lista de precios:", lista_precios)
