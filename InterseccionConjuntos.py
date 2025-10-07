def crear_conjunto(descripcion):

    entrada = input(f"Ingrese los números del {descripcion} separados por espacios: ")
    numeros = set(map(int, entrada.split()))
    return numeros


def main():
    print("Creación de conjuntos:")

    conjunto1 = crear_conjunto("primer conjunto")
    conjunto2 = crear_conjunto("segundo conjunto")

    interseccion = conjunto1 & conjunto2
    union = conjunto1 | conjunto2
    diferencia_simetrica = conjunto1 ^ conjunto2

    print("\nResultados:")
    print(f"Conjunto 1: {conjunto1}")
    print(f"Conjunto 2: {conjunto2}")
    print(f"Intersección: {interseccion}")
    print(f"Unión: {union}")
    print(f"Diferencia simétrica: {diferencia_simetrica}")


if __name__ == "__main__":
    main()
