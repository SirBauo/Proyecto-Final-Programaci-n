import csv
import os

class DataLoader:

    def load(self, filename):
        # Construimos la ruta completa del archivo dentro de la carpeta /data
        path = os.path.join("data", filename)

        # Abrimos el archivo CSV y lo leemos como una lista de diccionarios
        # Cada fila se convierte en un dict: {columna: valor}
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)  # Convertimos el lector en una lista completa

        # Regresamos los datos para ser usados por el programa
        return data
