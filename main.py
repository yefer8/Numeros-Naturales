class CalculadoraMCD:
    def __init__(self, a, b):
        """
        Inicializa la calculadora con los dos números enteros para los cuales se calculará el MCD.
        """
        self.a = a
        self.b = b

    def calcular_mcd(self):
        """
        Calcula el máximo común divisor (MCD) de los dos números utilizando el algoritmo de Euclides.
        :return: El máximo común divisor de self.a y self.b.
        """
        a = self.a
        b = self.b
        while b != 0:
            a, b = b, a % b
        return a

# Pedir al usuario que ingrese dos números enteros
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

# Crear una instancia de la clase CalculadoraMCD
calculadora = CalculadoraMCD(num1, num2)

# Calcular y mostrar el MCD de los dos números
print("El máximo común divisor de", num1, "y", num2, "es:", calculadora.calcular_mcd())
