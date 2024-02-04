ftotal = float(input('Introduce el precio de todo el carrito: '))

def con_iva(ftotal, iva=21):
    total_con_iva = ftotal + (ftotal * iva / 100)
    return total_con_iva

iva_personalizado = float(input('Introduce la tasa de IVA personalizada (por defecto es 21%): '))
resultado_con_iva = con_iva(ftotal, iva_personalizado)

print(f'Precio total con IVA ({iva_personalizado}%): {resultado_con_iva}')
