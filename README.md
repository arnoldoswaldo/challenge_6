# challenge_6
Reto 6 poo, este repositorio contiene manejo de excepciones aplicadas a ejercicios anteriores correspondientes al reto 1( calculadora, validacion si un numero es primo, etc ) con las validaciones  correspondientes, Y del reto 5 sobre ejercicio shape con las validaciones que considero necesarias  

___________________________________________________________________________________________
PARTE 1 aplicacion excepciones a los ejercicios realizados en el reto 1

ENCONTAR CARACTERES IGUALES PALABRAS
```
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
```
LISTA CON SUMA

```
def numeros_mayores(numeros):
    if len(numeros) < 2:
      # Se lanza una excepción ValueError
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
   # Excepción ValueError para manejar errores de validación
    except ValueError as ve:
        print(f"Error de valor: {ve}")
   # Excepción general para manejar errores en el procesamiento
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()
```
VALIDACION PARA UN NUMERO PRIMO
```
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
    # Excepción ValueError para manejar errores de validación
    except ValueError as ve:
        print(f"Error de valor: {ve}")
    # Excepción general para manejar errores en el procesamiento
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()
```
CALCULADORA CON OPERACIONES ELEMENTALES
```
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
       # Excepción ValueError para manejar errores de validación
        except ValueError:
            print("Error: Entrada inválida. Por favor, ingrese números válidos.")
        # Excepción ZeroDivisionError para manejar errores de división por cero
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        # Excepción general para manejar errores en el procesamiento
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    operaciones()
```
VALIDACION PALINDROMO
```
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
    # Excepción ValueError para manejar errores de validación
    except ValueError as ve:
        print(f"Error de valor: {ve}")
    # Excepción general para manejar errores en el procesamiento
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

if __name__ == "__main__":
    main()
```

________________________________________________________________________________________________
PARTE 2  aplicacion de excepciones al ejercicio de modulos shape

MAIN
```
import shape
from shape import Point, Triangle, Rectangle, Square, IsoscelesTriangle, EquilateralTriangle

def main():
    try:
        p1 = Point(0, 0)
        p2 = Point(0, 2)
        p3 = Point(11, 11)
        
        # Crea un triángulo y determina su tipo
        triangle = Triangle(vertices=[p1, p2, p3], inner_angles=[60, 60, 60])
        triangle_type = triangle.type
        print("Tipo de triángulo:", triangle_type)
        
        # Dependiendo del tipo de triángulo, crea una instancia de la clase correcta
        if triangle_type == "Rectángulo":
            triangle = Rectangle(vertices=[p1, p2, p3], inner_angles=[90, 45, 45])
        elif triangle_type == "Isosceles":
            triangle = IsoscelesTriangle(vertices=[p1, p2, p3], inner_angles=[70, 70, 40])
        elif triangle_type == "Equilatero":
            triangle = EquilateralTriangle(vertices=[p1, p2, p3], inner_angles=[60, 60, 60])
        elif triangle_type == "Escaleno":
            triangle = EquilateralTriangle(vertices=[p1, p2, p3], inner_angles=[80, 60, 40])
        
        # Validación para el método compute_area
        if not hasattr(triangle, 'compute_area'):
            # Lanza una excepción si la clase no tiene un método para calcular el área
            raise AttributeError(f"La clase {type(triangle).__name__} no tiene un método para calcular el área.")
        
        # Calcula e imprime el área y el perímetro del triángulo
        print("Área del triángulo:", triangle.compute_area())
        print("Perímetro del triángulo:", triangle.compute_perimeter())
        
        # Para el rectángulo y el cuadrado, se crean instancias de las clases Rectangle y Square, respectivamente
        rectangle = Rectangle(vertices=[p1, Point(5, 0), Point(5, 3), Point(0, 3)], inner_angles=[90, 90, 90, 90])
        print("Área del rectángulo:", rectangle.compute_area())
        print("Perímetro del rectángulo:", rectangle.compute_perimeter())
        
        square = Square(vertices=[p1, Point(3, 0), Point(3, 3), Point(0, 3)], inner_angles=[90, 90, 90, 90])
        print("Área del cuadrado:", square.compute_area())
        print("Perímetro del cuadrado:", square.compute_perimeter())
    # Manejo de excepciones, con mensajes personalizados para cada tipo de error, y un mensaje genérico para cualquier otro error
   # excepcion de valor para el caso de que se ingrese un valor incorrecto 
    except ValueError as ve:
        print("Error de valor:", ve)
    # excepcion de tipo para el caso de que se ingrese un tipo incorrecto
    except TypeError as te:
        print("Error de tipo:", te)
    # excepcion de atributo para el caso de que se intente acceder a un atributo que no existe
    except AttributeError as ae:
        print("Error de atributo:", ae)
    # excepcion de indice para el caso de que se intente acceder a un indice que no existe
    except Exception as e:
        print("Error inesperado:", e)

if __name__ == "__main__":
    main()
```
SHAPE
```
import math
class Point:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
           # excepcion de tipo para el caso de que se ingrese un tipo incorrecto
            raise ValueError("Las coordenadas del punto deben ser numéricas.")
        self._x = x
        self._y = y

    def set_x(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_y(self, y):
        self._y = y

    def get_y(self):
        return self._y

    def compute_distance(self, other):
        return ((self._x - other._x) ** 2 + (self._y - other._y) ** 2) ** 0.5


class Line:
    def __init__(self, start_point, end_point):
        self._start_point = start_point
        self._end_point = end_point
        self.length = start_point.compute_distance(end_point)

    def get_start_point(self):
        return self._start_point

    def set_start_point(self, start_point):
        self._start_point = start_point

    def get_end_point(self):
        return self._end_point

    def set_end_point(self, end_point):
        self._end_point = end_point


class Shape:
    def __init__(self, vertices, inner_angles):
        self.vertices = vertices
        self._inner_angles = inner_angles
        self.edges = [Line(vertices[i], vertices[(i + 1) % len(vertices)]) for i in range(len(vertices))]
        self._inner_angles = self.compute_inner_angles()
        self.is_regular = self.compute_is_regular()

    def compute_inner_angles(self):
        angles = []
        for i in range(len(self.vertices)):
            p1 = self.vertices[i]
            p2 = self.vertices[(i + 1) % len(self.vertices)]
            p3 = self.vertices[(i + 2) % len(self.vertices)]
            angle = self.compute_angle(p1, p2, p3)
            angles.append(angle)
        return angles

    def compute_angle(self, p1, p2, p3):
        d1 = p1.compute_distance(p2)
        d2 = p2.compute_distance(p3)
        d3 = p3.compute_distance(p1)
        numerator = d1 ** 2 + d3 ** 2 - d2 ** 2
        denominator = 2 * d1 * d3
        # Manejar divisiones por cero
        if denominator == 0:
            return 0
        # Calcular el ángulo utilizando teorema de coseno
        angle_rad = math.acos(numerator / denominator)
        # Convertir radianes a grados
        angle_deg = angle_rad * 180 / math.pi
        return angle_deg

    def compute_is_regular(self):
        return len(set(self._inner_angles)) == 1

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, vertices):
        self._vertices = vertices

    def get_inner_angles(self):
        return self._inner_angles

    def set_inner_angles(self, inner_angles):
        self._inner_angles = inner_angles


class Triangle(Shape):
    def __init__(self, vertices, inner_angles):
        super().__init__(vertices, inner_angles)
        self.type = self.determine_type()
        # Validación de los argumentos, asegurando que los vértices sean instancias de Point
        if len(vertices) != 3:
           # excepcion de valor para el caso de que se ingrese un valor incorrecto
            raise ValueError("Un triángulo debe tener exactamente 3 vértices.")
        if not all(isinstance(vertex, Point) for vertex in vertices):
            # excepcion de tipo para el caso de que se ingrese un tipo incorrecto
            raise TypeError("Todos los vértices deben ser instancias de Point.")
        if len(inner_angles) != 3 or not all(isinstance(angle, (int, float)) for angle in inner_angles):
            # excepcion de valor para el caso de que se ingrese un valor incorrecto
            raise ValueError("Debe haber exactamente 3 ángulos numéricos.")
        if not math.isclose(sum(inner_angles), 180):
            # excepcion de valor para el caso de que se ingrese un valor incorrecto
            raise ValueError("La suma de los ángulos internos debe ser 180 grados para un triángulo.")

    def determine_type(self):
        # Clasificación de triángulos según la longitud de sus lados
        a, b, c = sorted([edge.length for edge in self.edges])
        # tolerancia de error (1e-6) para comparar las longitudes de los lados.
        if abs(a ** 2 + b ** 2 - c ** 2) < 1e-6:
            return "Rectangulo"
        elif a == b == c:
            return "Equilatero"
        elif a == b or b == c:
            return "Isosceles"
        else:
            return "Escaleno"

    def compute_area(self):
        a, b, c = sorted([edge.length for edge in self.edges])
        if self.type == "Rectangulo":
            # Para un triangulo rectangulo, el área es (base * altura)/2
            return 0.5 * a * b
        elif self.type == "Isósceles":
            # Para un triángulo isósceles, el area es base * raiz cuadrada((lado^2) - (base^2 / 4)) / 2
            base = a if a != b else c
            side = b if a == b else a
            return base * ((side ** 2 - (base ** 2 / 4)) ** 0.5) / 2
        elif self.type=="Equilatero":
            #Para un tirangulo equilatero calculamos el area con ((raizcuadrada 3)/) * lado al cuadrado
            a = self.edges[0].length
            return ((3 ** 0.5) / 4) * a ** 2
        else:
            # Para un triángulo escaleno, utilizamos la formula de Heron donde s=semiperimetro
            s = (a + b + c) / 2
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def compute_perimeter(self):
        # La suma de los lados
           
           return sum(edge.length for edge in self.edges)
    
class EquilateralTriangle(Triangle):
    def __init__(self, vertices, inner_angles):
        super().__init__(vertices, inner_angles)

    def compute_area(self):
        # Área de un triángulo equilátero
        a = self.edges[0].length
        return ((3 ** 0.5) / 4) * a ** 2

    def get_vertices(self):
        return super().get_vertices()

    def set_vertices(self, vertices):
        super().set_vertices(vertices)


class RectangleTriangle(Triangle):
    def __init__(self, vertices, inner_angles):
        super().__init__(vertices, inner_angles)

    def compute_area(self):
        # area de un triángulo rectangulo
        a = self.edges[0].length
        b = self.edges[1].length
        return 0.5 * a * b

    def get_vertices(self):
        return super().get_vertices()

    def set_vertices(self, vertices):
        super().set_vertices(vertices)


class ScaleneTriangle(Triangle):
    def __init__(self, vertices, inner_angles):
        super().__init__(vertices, inner_angles)

    def compute_area(self):
        # Usando la fórmula de Heron
        a = self.edges[0].length
        b = self.edges[1].length
        c = self.edges[2].length
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def get_vertices(self):
        return super().get_vertices()

    def set_vertices(self, vertices):
        super().set_vertices(vertices)


class IsoscelesTriangle(Triangle):
    def __init__(self, vertices, inner_angles):
        super().__init__(vertices, inner_angles)

    def compute_area(self):
        # area de un triángulo isosceles
        a, b, c = sorted([edge.length for edge in self.edges])
        base = a if a != b else c
        side = b if a == b else a
        return base * ((side ** 2 - (base ** 2 / 4)) ** 0.5) / 2

    def get_vertices(self):
        return super().get_vertices()

    def set_vertices(self, vertices):
        super().set_vertices(vertices)


class Rectangle(Shape):

    def __init__(self, vertices, inner_angles):
        super().__init__(vertices, inner_angles)

        #validacion de los argumentos, asegurando que los vertices sean instancias de Point
        if len(vertices) != 4:
           # excepcion de valor para el caso de que se ingrese un valor incorrecto
            raise ValueError("Un rectángulo debe tener exactamente 4 vértices.")
        if not all(isinstance(vertex, Point) for vertex in vertices):
            # excepcion de tipo para el caso de que se ingrese un tipo incorrecto
            raise TypeError("Todos los vértices deben ser instancias de Point.")
        self.vertices = vertices
        

    def compute_area(self):
        # la multiplicacion de los lados b*h
        return self.edges[0].length * self.edges[1].length

    def compute_perimeter(self):
        # se suma la medida de los lados 
        return 2 * (self.edges[0].length + self.edges[1].length)

    def get_vertices(self):
        return super().get_vertices()

    def set_vertices(self, vertices):
        super().set_vertices(vertices)


class Square(Rectangle):
    def compute_area(self):
        # para el area multiplicamos l*l
        return self.edges[0].length ** 2

    def compute_perimeter(self):
        # sumamos 4 veces la medida del lado  
        return 4 * self.edges[0].length

    def get_vertices(self):
        return super().get_vertices()

    def set_vertices(self, vertices):
        super().set_vertices(vertices)
```


