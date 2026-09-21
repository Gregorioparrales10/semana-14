# Ejercicio Semana 14 - Funciones con parámetros y retorno

Descripción

Este programa fue desarrollado en Python como parte de la actividad de la Semana 14.

El programa permite calcular el precio total de una compra a partir del precio de un producto y la cantidad de productos adquiridos.

Objetivo

Aplicar el uso de funciones en Python utilizando:

- Una función.
- Parámetros de entrada.
- La palabra clave `return`.
- Una llamada a la función.
- Mostrar el resultado en pantalla.

Funcionamiento

El usuario debe ingresar:

1. El precio del producto.
2. La cantidad de productos.

El programa utiliza la función `calcular_total()` para multiplicar el precio por la cantidad y obtener el total de la compra.

Código principal

```python
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
