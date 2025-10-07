def dividir_lista(lista):

    negativos = sorted([x for x in lista if x < 0])
    positivos = sorted([x for x in lista if x > 0])
    return negativos, positivos


def main():

    listaEjemplo = [6, 2, -90, -1, 89, 75874, -945643]

    negativos, positivos = dividir_lista(listaEjemplo)

    print("Lista de números negativos ordenados:", negativos)
    print("Lista de números positivos ordenados:", positivos)


if __name__ == "__main__":
    main()
