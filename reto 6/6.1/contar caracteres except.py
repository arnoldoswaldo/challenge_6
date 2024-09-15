# Descripcion: Programa que recibe palabras y al ingresar 0, se validará cuáles 
# palabras tienen las mismas letras. incluye manejo de excepciones.
# Autor: [Arnold Acosta]
def encontrar_iguales(lista_palabras):
    # Diccionario que almacena las palabras
    iguales = {}

    try:
        for palabra in lista_palabras:
            # Ordena los caracteres de la palabra
            letras = ''.join(sorted(palabra))

            # Repetidos
            if letras in iguales:
                iguales[letras].append(palabra)
            else:
                # Si no existe
                iguales[letras] = [palabra]

        # Validación
        lista_iguales = [palabras for palabras in iguales.values() if len(palabras) > 1]
    # Excepción general para manejar errores en el procesamiento
    except Exception as e:
        print(f"Ha ocurrido un error durante el procesamiento: {e}")
        lista_iguales = []
    finally:
        return lista_iguales

def main():
    lista_palabras = []
    try:
        while True:
            palabra = input("Ingrese una palabra a la vez, al escribir 0 se validará cuáles palabras tienen las mismas letras: ")
            if palabra == "0":
                break
            lista_palabras.append(palabra)
        
        lista_iguales = encontrar_iguales(lista_palabras)
        print("Elementos con los mismos caracteres:", lista_iguales)
    # Excepción general 
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
    finally:
        print("El programa ha terminado.")

if __name__ == "__main__":
    main()
