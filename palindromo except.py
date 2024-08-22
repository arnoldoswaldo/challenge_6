# Description: Programa que verifica si una cadena de texto es un palíndromo, incluye manejo de excepciones.
# Autor: [Arnold Acosta]
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

def main():
    try:
        cadena = input("Ingrese una cadena: ")
        if not isinstance(cadena, str):
            raise ValueError("Debe ingresar una cadena de texto.")
        if es_palindromo(cadena):
            print("La cadena es un palíndromo")
        else:
            print("La cadena no es un palíndromo")
    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()
