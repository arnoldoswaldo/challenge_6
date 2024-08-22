#description: Programa que realiza operaciones aritméticas básicas (+, -, *, /) con dos números ingresados por el usuario.
# Autor: [Arnold Acosta]
def operaciones():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            operacion = input("Ingrese la operación que desea realizar (+, -, /, *): ")  
            
            if operacion == "+":
                resultado = num1 + num2
                print("El resultado es: ", resultado)
            elif operacion == "-":
                resultado = num1 - num2
                print("El resultado es: ", resultado)
            elif operacion == "*":
                resultado = num1 * num2
                print("El resultado es: ", resultado)
            elif operacion == "/":
                if num2 == 0:
                    raise ZeroDivisionError("No se puede dividir por cero.")
                resultado = num1 / num2
                print("El resultado es: ", resultado)
            else:  
                print("Operación inválida")
            
            otra_operacion = input("¿Desea realizar otra operación? (s/n): ")
            if otra_operacion.lower() == "n":
                break
        except ValueError:
            print("Error: Entrada inválida. Por favor, ingrese números válidos.")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    operaciones()
 