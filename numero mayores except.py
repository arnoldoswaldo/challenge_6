# Description: Programa que solicita al usuario una cantidad de números y luego solicita los números. El programa debe devolver la suma de los dos números mayores ingresados. Si la cantidad de números ingresados es menor a 2, el programa debe lanzar una excepción ValueError con el mensaje "La lista debe contener al menos dos números.".
# Autor: [Arnold Acosta]
def numeros_mayores(numeros):
    if len(numeros) < 2:
        raise ValueError("La lista debe contener al menos dos números.")
    a = max(numeros)
    numeros.remove(a)
    b = max(numeros)
    return [a, b]

def lista_con_suma(numeros):
    mayores = numeros_mayores(numeros)
    suma = sum(mayores)
    return suma

def main():
    try:
        numeros = []
        cantidad = int(input("Cuantos números desea sumar: "))
        
        if cantidad < 2:
            raise ValueError("Debe ingresar al menos dos números.")

        for _ in range(cantidad):
            num = int(input("Ingrese un número: "))
            numeros.append(num)
        
        print("La suma de los dos mayores números es:", lista_con_suma(numeros))
    except ValueError as ve:
        print(f"Error de valor: {ve}")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()