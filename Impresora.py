def calcular_descuento(precio_con_iva, forma_de_pago):
    descuento = 0
    if forma_de_pago == "efectivo":
        descuento = precio_con_iva * 0.10
    elif forma_de_pago == "tarjeta de crédito":
        descuento = precio_con_iva * 0.05
    elif forma_de_pago == "vale de regalo":
        descuento = precio_con_iva * 0.15
    return descuento
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de impresoras a comprar: "))
        if cantidad <= 0:
            print("La cantidad debe ser un número entero positivo.")
            continue
        else:
            break
    except ValueError:
        print("La cantidad debe ser un número entero.")

forma_pago = input("Seleccione la forma de pago (efectivo, tarjeta de crédito, vale de regalo): ")
forma_pago = forma_pago.lower()

if forma_pago not in ["efectivo", "tarjeta de crédito", "vale de regalo"]:
    print("Forma de pago no válida.")
else:
    precio_unitario_con_iva = 80000 * 1.16  # Precio unitario con IVA
    total_sin_descuento = cantidad * precio_unitario_con_iva
    descuento_realizado = calcular_descuento(precio_unitario_con_iva, forma_pago)
    total_a_pagar = total_sin_descuento - descuento_realizado
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de impresoras a comprar: "))
        if cantidad <= 0:
            print("La cantidad debe ser un número entero positivo.")
            continue
        else:
            break
    except ValueError:
        print("La cantidad debe ser un número entero.")

forma_pago = input("Seleccione la forma de pago (efectivo, tarjeta de crédito, vale de regalo): ")
forma_pago = forma_pago.lower()

if forma_pago not in ["efectivo", "tarjeta de crédito", "vale de regalo"]:
    print("Forma de pago no válida.")
else:
    precio_unitario_con_iva = 80000 * 1.16  # Precio unitario con IVA
    total_sin_descuento = cantidad * precio_unitario_con_iva
    descuento_realizado = calcular_descuento(precio_unitario_con_iva, forma_pago)
    total_a_pagar = total_sin_descuento - descuento_realizado

