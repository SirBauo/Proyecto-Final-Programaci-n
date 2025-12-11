**Proyecto Final – Sistema Modular de Análisis de Datos**

Este proyecto implementa un sistema modular en Python que permite cargar, consultar, limpiar, analizar y generar reportes sobre un dataset ubicado en la carpeta /data.

El enfoque principal es aplicar Programación Orientada a Objetos (POO) y modularidad, utilizando únicamente librerías nativas de Python.


**Estructura**

proyecto final/

│ main.py

│ data_loader.py

│ data_query.py

│ data_analyzer.py

│ data_cleaner.py

│ data_reporter.py

│ logger_ops.py

│ utils.py
│

└── data/

      data.csv
------------------------------------------------------------

**El programa permite:**

      -Cargar un dataset CSV ubicado en /data

      -Consultar información sobre sus columnas y valores

      -Realizar análisis numéricos (máximo, mínimo, promedio, varianza, desviación estándar)

      -Limpiar datos aplicando filtros por rango o por texto

      -Generar un reporte JSON descriptivo del dataset

      -Guardar un registro local (bitácora) de todas las operaciones en operations.dat

      -Exportar resultados de consultas a archivos .txt

Todo esto mediante un menú interactivo en consola.

--------------------------------------------------------------

**Ejecución del Programa**

Asegúrate de tener Python 3 instalado.

Ubícate en la carpeta del proyecto.

Ejecuta: python main.py

Aparecerá el menú principal con las opciones:

1. Cargar dataset
2. Consultar dataset
3. Analizar datos
4. Limpiar datos
5. Generar reporte
6. Mostrar operaciones
7. Salir

-------------------------------------------------------------
**Descripción de Módulos**

**main.py**

Controla el menú principal e integra todas las clases del sistema.

**data_loader.py**

Carga un archivo CSV desde /data

Convierte el contenido en una lista de diccionarios (DictReader)

**data_query.py**

Permite:

      Listar columnas

      Listar columnas con su tipo (numérico/alfanumérico)

      Listar valores distintos de una columna

      Exportar valores únicos a .txt

      Buscar por rango (numérico) o coincidencia de texto

**data_analyzer.py**

Realiza análisis estadístico básico:

      Máximo

      Mínimo

      Promedio

      Varianza

      Desviación estándar

      Solo para columnas numéricas.

**data_cleaner.py**

Genera un nuevo archivo CSV filtrado a partir de:

Rango numérico

Coincidencia de texto (alfanumérico)

**data_reporter.py**

Genera un archivo: reporte.json

Contiene:

Listado de columnas

Tipo de datos de cada columna

Total de filas

Columnas con valores vacíos

**logger_ops.py**

Registra todas las operaciones del usuario en: operations.dat

Formato: dataset | operación | parámetros

También puede mostrar el histórico completo.

**utils.py**

Funciones utilitarias, como:

is_number() → detecta si un valor es numérico

----------------------------

**Puntos cumplidos en el proyecto**

✔ Modularidad y separación por capas

✔ Programación Orientada a Objetos

✔ Flujo básico de análisis de datos

✔ Menú por consola

✔ Reportes generados a archivos (JSON y TXT)

✔ Bitácora persistente de operaciones

✔ Uso exclusivo de librerías nativas