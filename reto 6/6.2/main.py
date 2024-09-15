# Description: Este archivo contiene el código principal que crea instancias de las clases Point, Triangle, Rectangle, Square, IsoscelesTriangle y EquilateralTriangle, y calcula el área y el perímetro de cada una de ellas.
# Autor: [Arnold Acosta]
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
