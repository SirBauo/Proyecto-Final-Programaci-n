class OperationLogger:

    def __init__(self, filename):
        # Archivo donde se registrarán TODAS las operaciones del sistema.
        # Se almacena como texto plano para mantener simplicidad.
        self.filename = filename

    def log(self, dataset, operacion, parametros):
        # Registra una línea en el archivo de operaciones.
        # Formato: dataset | operación | parámetros
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"{dataset} | {operacion} | {parametros}\n")

    def show_all(self):
        # Muestra en pantalla todo el historial de operaciones registradas.
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                print(f.read())     # Imprime el contenido completo
        except FileNotFoundError:
            # Si nunca se ha registrado una operación, el archivo no existe
            print("No hay registros.")
