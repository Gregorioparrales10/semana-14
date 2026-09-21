def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total


def main():
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad de productos: "))

    total = calcular_total(precio, cantidad)

    print("El precio total de la compra es: $", total)


if __name__ == "__main__":
    main()






