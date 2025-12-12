from data_loader import DataLoader
from data_query import DataQuery
from data_analyzer import DataAnalyzer
from data_cleaner import DataCleaner
from data_reporter import DataReporter
from logger_ops import OperationLogger


def main():
    loader = DataLoader()
    logger = OperationLogger("operations.dat")
    data = None

    opcion = 0
    while opcion != 7:
        print("\nMENU PRINCIPAL")
        print("1. Cargar dataset")
        print("2. Consultar dataset")
        print("3. Analizar datos")
        print("4. Limpiar datos")
        print("5. Generar reporte")
        print("6. Mostrar operaciones")
        print("7. Salir")

        try:
            opcion = int(input("Opción: "))
        except:
            print("Opción inválida.")
            continue

        if opcion == 1:
            filename = input("Nombre del dataset (en /data): ")
            data = loader.load(filename)
            logger.log(filename, "cargar_dataset", "")
            print("Dataset cargado.\n")

        elif opcion == 2:
            if not data:
                print("Debe cargar un dataset.")
                continue
            DataQuery(data, logger).menu()

        elif opcion == 3:
            if not data:
                print("Debe cargar un dataset.")
                continue
            DataAnalyzer(data, logger).menu()

        elif opcion == 4:
            if not data:
                print("Debe cargar un dataset.")
                continue
            DataCleaner(data, logger).menu()

        elif opcion == 5:
            if not data:
                print("Debe cargar un dataset.")
                continue
            DataReporter(data, logger).create_report()

        elif opcion == 6:
            logger.show_all()

    print("Adieu")


if __name__ == "__main__":
    main()
