#descripcion: Programa que determina si un número es primo o no, utilizando excepciones para manejar errores de valor.
# Autor: [Arnold Acosta]
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    try:
        num = int(input("Ingrese un número: "))
        if num < 0:
            raise ValueError("Debe ingresar un número positivo.")
        if es_primo(num):
            print("El número es primo")
        else:
            print("El número no es primo")
    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()
