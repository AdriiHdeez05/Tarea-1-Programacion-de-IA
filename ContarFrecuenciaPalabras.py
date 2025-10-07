import string


def contar_frecuencia_palabras(texto):

    texto = texto.translate(str.maketrans("", "", string.punctuation))

    texto = texto.lower()

    palabras = texto.split()

    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia


def main():

    texto_usuario = input("Ingresa una frase o párrafo: ")

    frecuencias = contar_frecuencia_palabras(texto_usuario)

    print("\nFrecuencia de palabras:")
    for palabra in sorted(frecuencias):
        print(f"{palabra}: {frecuencias[palabra]}")


if __name__ == "__main__":
    main()
