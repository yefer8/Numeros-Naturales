class CalculadoraMCM:
    def __init__(self, a, b):
        """
        Inicializa la calculadora con los dos números enteros para los cuales se calculará el MCM.
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

    def calcular_mcm(self):
        """
        Calcula el mínimo común múltiplo (MCM) de los dos números utilizando la relación entre el MCD y el MCM.
        :return: El mínimo común múltiplo de self.a y self.b.
        """
        mcd = self.calcular_mcd()
        return (self.a * self.b) // mcd

# Pedir al usuario que ingrese dos números enteros
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

# Crear una instancia de la clase CalculadoraMCM
calculadora = CalculadoraMCM(num1, num2)

# Calcular y mostrar el MCM de los dos números
print("El mínimo común múltiplo de", num1, "y", num2, "es:", calculadora.calcular_mcm())
