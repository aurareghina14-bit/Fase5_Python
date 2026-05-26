# ==========================================
# Programa: Control de Inventario
# ==========================================

# Matriz de artículos
articulos = [
    ["A01", "Teclado", 5, 10],
    ["A02", "Mouse", 15, 10],
    ["A03", "Monitor", 3, 8],
    ["A04", "USB", 20, 15],
    ["A05", "Audifonos", 4, 12]
]

# Función para calcular cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        cantidad_pedir = 0

    return cantidad_pedir


print("========================================")
print(" REPORTE DE REABASTECIMIENTO ")
print("========================================")

# Recorrer matriz
for articulo in articulos:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    pedido = calcular_pedido(stock_actual, stock_minimo)

    print(f"Artículo: {nombre}")
    print(f"Stock actual: {stock_actual}")
    print(f"Stock mínimo: {stock_minimo}")
    print(f"Cantidad a pedir: {pedido}")
    print("----------------------------------------")
