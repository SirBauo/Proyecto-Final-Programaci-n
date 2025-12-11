import os
from utils import is_number

class DataQuery:

    def __init__(self, data, logger):
        # Guardamos el dataset cargado y el logger de operaciones
        self.data = data
        self.logger = logger

    def menu(self):
        # Menú de opciones para consultar los datos del CSV
        print("\nCONSULTAR DATASET")
        print("1. Listar columnas")
        print("2. Listar columnas y tipos")
        print("3. Listar valores distintos")
        print("4. Consultar por rango o texto")
        op = input("Opción: ")

        # --- OPCIÓN 1: Mostrar nombres de columnas ---
        if op == "1":
            # Se imprimen los nombres de columnas leyendo las llaves del primer registro
            print(list(self.data[0].keys()))
            self.logger.log("", "listar_columnas", "")

        # --- OPCIÓN 2: Mostrar columnas y su tipo detectado ---
        elif op == "2":
            # Para cada columna verificamos si el primer valor es numérico o no
            for col in self.data[0].keys():
                tipo = "numérico" if is_number(self.data[0][col]) else "alfanumérico"
                print(col, tipo)
            self.logger.log("", "listar_columnas_tipos", "")

        # --- OPCIÓN 3: Mostrar valores únicos de una columna ---
        elif op == "3":
            col = input("Columna: ")

            # Un set permite obtener valores únicos de forma automática
            valores = {row[col] for row in self.data}

            # Si hay demasiados valores, solo mostramos la cantidad
            if len(valores) > 50:
                print("Muchos valores:", len(valores))
            else:
                print(valores)

            # Preguntamos si se desea exportar los valores a un archivo .txt
            exp = input("Exportar a archivo? (s/n): ")
            if exp == "s":
                filename = f"output-{col}.txt"
                with open(filename, "w", encoding="utf-8") as f:
                    for v in valores:
                        f.write(str(v) + "\n")
                print("Guardado:", filename)

            self.logger.log("", "valores_distintos", col)

        # --- OPCIÓN 4: Consultas con filtros numéricos o de texto ---
        elif op == "4":
            col = input("Columna: ")

            # Buscamos un valor no vacío para determinar si la columna es numérica o no
            muestra = next(v[col] for v in self.data if v[col] != "")

            # Si la columna es numérica -> búsqueda por rango
            if is_number(muestra):
                low = float(input("Valor mínimo: "))
                high = float(input("Valor máximo: "))

                # Filtramos filas dentro del rango especificado
                filtrados = [
                    row for row in self.data
                    if row[col] != "" and low <= float(row[col]) <= high
                ]
            else:
                # Si es texto -> búsqueda parcial insensible a mayúsculas
                txt = input("Texto a buscar: ")
                filtrados = [
                    row for row in self.data
                    if txt.lower() in row[col].lower()
                ]

            print("Coincidencias:", len(filtrados))

            # Opción para exportar resultados
            exp = input("Guardar resultados? (s/n): ")
            if exp == "s":
                filename = f"consulta-{col}.txt"
                with open(filename, "w", encoding="utf-8") as f:
                    for row in filtrados:
                        f.write(str(row) + "\n")
                print("Guardado:", filename)

            self.logger.log("", "consulta_columna", col)
