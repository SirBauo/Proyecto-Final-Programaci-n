from utils import is_number

class DataCleaner:

    def __init__(self, data, logger):
        # Guardamos el dataset y el logger para registrar operaciones
        self.data = data
        self.logger = logger

    def menu(self):
        # Pedimos las columnas que el usuario desea filtrar
        columnas = input("Columnas a filtrar (coma-separadas): ").split(",")
        filtrado = self.data  # Comenzamos con todos los datos

        for col in columnas:
            col = col.strip()  # Quitamos espacios extra

            # Buscamos un valor de muestra para saber si la columna es numérica o texto
            muestra = next((row[col] for row in self.data if row[col] != ""), "")

            # Si la columna contiene números, aplicamos filtros numéricos
            if is_number(muestra):
                # Pedimos límites inferior y superior
                low = float(input(f"[{col}] mínimo: "))
                high = float(input(f"[{col}] máximo: "))

                # Nos quedamos solo con los registros que cumplen el rango
                filtrado = [
                    row for row in filtrado
                    if row[col] != "" and low <= float(row[col]) <= high
                ]

            else:
                # Si la columna es texto, pedimos un texto a buscar
                txt = input(f"[{col}] texto a buscar: ")

                # Filtramos filas cuyo valor contenga la subcadena
                filtrado = [
                    row for row in filtrado
                    if txt.lower() in row[col].lower()
                ]

        # Exportamos el dataset limpio a un nuevo archivo CSV
        filename = "dataset_limpio.csv"
        import csv
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(filtrado)

        print("Dataset limpio creado:", filename)

        # Registramos la acción realizada
        self.logger.log("", "limpiar_dataset", str(columnas))
