import json
from utils import is_number

class DataReporter:

    def __init__(self, data, logger):
        # Guardamos el dataset y el logger para registrar la operación
        self.data = data
        self.logger = logger

    def create_report(self):
        # Obtenemos los nombres de todas las columnas del archivo
        cols = self.data[0].keys()

        # Estructura base del reporte a generar
        reporte = {
            "columnas": [],              # Lista con nombre y tipo de cada columna
            "rows_totales": len(self.data),  # Cantidad total de filas del dataset
            "columnas_con_vacios": []    # Columnas que contienen al menos un valor vacío
        }

        # --- Analizamos cada columna del dataset ---
        for col in cols:

            # Obtenemos una muestra no vacía para determinar el tipo de dato
            muestra = next(
                (row[col] for row in self.data if row[col] != ""),
                ""
            )
            tipo = "numérico" if is_number(muestra) else "alfanumérico"

            # Guardamos la metadata de la columna en el reporte
            reporte["columnas"].append({
                "nombre": col,
                "tipo": tipo
            })

            # Verificamos si la columna contiene valores vacíos
            if any(row[col] == "" for row in self.data):
                reporte["columnas_con_vacios"].append(col)

        # --- Guardamos el reporte final en formato JSON ---
        with open("reporte.json", "w", encoding="utf-8") as f:
            json.dump(reporte, f, indent=4)   # indent = 4 → formato legible

        print("Reporte generado: reporte.json")

        # Registramos la operación en el archivo de logs
        self.logger.log("", "generar_reporte", "")
