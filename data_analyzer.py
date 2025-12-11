from utils import is_number
import math

class DataAnalyzer:
    """
    Clase encargada de realizar análisis estadístico
    sobre columnas numéricas del dataset.
    """

    def __init__(self, data, logger):
        # El dataset se recibe como una lista de diccionarios
        self.data = data
        
        # Logger para registrar la operación realizada
        self.logger = logger

    def menu(self):
        """
        Muestra el menú para elegir una columna y 
        calcular estadísticas básicas.
        """
        print("\nANALIZAR DATOS")
        col = input("Columna numérica: ")

        # Se extraen solo los valores numéricos válidos de la columna
        valores = [
            float(row[col])              # Convertimos a float
            for row in self.data         # Recorremos cada fila
            if is_number(row[col])       # Validamos que realmente sea número
        ]

        # Si no se pudo convertir ningún valor devuelve que no es columna numérica duh
        if not valores:
            print("No es numérica.")
            return

        # ----- Cálculos básicos -----
        print("Máximo:", max(valores))
        print("Mínimo:", min(valores))

        promedio = sum(valores) / len(valores)
        print("Promedio:", promedio)

        # Varianza usando la fórmula clásica
        var = sum((x - promedio) ** 2 for x in valores) / len(valores)
        print("Varianza:", var)

        # Desviación estándar = raíz cuadrada de la varianza
        print("Desviación estándar:", math.sqrt(var))

        # Registrar operación en la bitácora
        self.logger.log("", "analizar_columna", col)
