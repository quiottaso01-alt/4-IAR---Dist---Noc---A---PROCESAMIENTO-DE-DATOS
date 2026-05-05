#  Proyecto ETL - Análisis de Desastres Naturales

---

##  Descripción del proyecto

Este proyecto implementa un proceso ETL (Extract, Transform, Load) en Python aplicado a un dataset de desastres naturales. El objetivo es realizar un análisis exploratorio para identificar patrones temporales, estacionales y geográficos.

El flujo del trabajo se divide en:

* **Extract:** carga y exploración inicial de los datos
* **Transform:** limpieza y preparación del dataset
* **Load:** generación de visualizaciones para el análisis

---

##  Estructura del proyecto

```
proyecto_desastres_naturales/
├── extract/
│   └── extract.py
├── transform/
│   └── transform.py
├── load/
│   └── load.py
├── outputs/
│   └── (gráficos en formato PNG)
├── main.py
└── README.md
```

La carpeta `outputs/` contiene los gráficos generados automáticamente.

---

##  Conjunto de datos

El conjunto de datos utilizado contiene información sobre desastres naturales ocurridos a nivel global.

Para el desarrollo del análisis, se trabajó principalmente con las siguientes variables:

Year (Año): permite analizar la evolución temporal de los desastres a lo largo del tiempo.
Start Month (Mes de inicio): utilizada para identificar patrones estacionales en la ocurrencia de los eventos.
Disaster Type (Tipo de desastre): permite clasificar los eventos según su naturaleza (inundaciones, tormentas, etc.).
Country (País): posibilita analizar la distribución geográfica de los desastres y detectar regiones más afectadas.

Estas variables resultan fundamentales para comprender el comportamiento temporal, estacional y geográfico de los desastres naturales, permitiendo identificar patrones relevantes a partir del análisis exploratorio de datos.

---

##  Instalación

```
pip install pandas matplotlib seaborn
```

---

##  Ejecución

```
python main.py
```

Al ejecutar, se generan automáticamente los gráficos en la carpeta:

```
outputs/
```

---

##  Proceso ETL

---

### 1. Extract

El módulo `extract.py` se encarga de:

* Cargar los datos desde una URL con pandas
* Mostrar estructura del dataset
* Visualizar primeras filas
* Detectar valores nulos

Esta etapa permite conocer la calidad y estructura de los datos.

---

### 2. Transform

El módulo transform.py se encarga de preparar los datos para su posterior análisis, mediante las siguientes tareas:

Creación de fecha

Se combinan las variables Year y Start Month en una nueva columna de tipo fecha, lo que permite un manejo más eficiente de la información temporal.

Limpieza de datos

Se realiza un proceso de curación de datos que incluye:

Normalización de texto en variables categóricas
Eliminación de espacios innecesarios
Manejo de valores faltantes mediante imputación

Estas transformaciones permiten mejorar la calidad del dataset y asegurar la consistencia de los datos para el análisis.

Preparación para el análisis

En esta etapa no se eliminan registros del conjunto de datos original.



####  Filtrado

El filtrado por períodos específicos (por ejemplo, desde el año 2000) se realiza posteriormente durante la etapa de visualización, según las necesidades de cada análisis.

---

### 3. Load

El módulo load.py se encarga de la etapa final del proceso ETL, donde los datos transformados se convierten en información visual para su análisis.

Sus principales funciones son:

1_Generar visualizaciones utilizando las librerías matplotlib y seaborn.

2_Guardar automáticamente los gráficos generados en la carpeta outputs/ en formato PNG.

3_Aplicar filtros específicos según el análisis (por ejemplo, selección de años recientes) para construir visualizaciones comparativas.

A través de estos gráficos, se logra identificar patrones temporales, estacionales y geográficos en la ocurrencia de desastres naturales, facilitando la interpretación de los datos y la obtención de conclusiones.

---

##  Análisis de resultados

---

###  Desastres por año

![Grafico anual](outputs/grafico_anual.png)

Se observa un incremento sostenido en la cantidad de desastres desde la década de 1980, con mayor crecimiento hacia fines de los 90 y principios de los 2000. Esto puede deberse tanto a una mayor frecuencia de eventos como a mejoras en los registros.

---

###  Desastres en los últimos años

![Grafico ultimos](outputs/grafico_ultimos.png)

En las últimas décadas, la cantidad de eventos se mantiene alta, aunque con variaciones entre años. Esto indica una frecuencia sostenida de desastres.

---

###  Desastres por mes

![Grafico mensual](outputs/grafico_mensual.png)

Se identifican meses con mayor concentración de eventos, lo que sugiere patrones estacionales asociados a fenómenos climáticos.

---

###  Heatmap temporal

![Heatmap](outputs/grafico_heatmap.png)

El gráfico muestra la distribución de desastres por mes y año, evidenciando concentraciones en determinados períodos.

---

###  Tipos de desastres

![Tipos](outputs/grafico_tipos.png)

Predominan los desastres de origen climático, especialmente inundaciones y tormentas.

---

###  Países más afectados

![Paises](outputs/grafico_paises.png)

Estados Unidos, China e India presentan mayor cantidad de eventos, posiblemente por su tamaño y diversidad climática.

---

###  Tipo de desastre por país

![Cruce](outputs/grafico_cruce_tipo_pais.png)

Estados Unidos, China e India concentran la mayor cantidad de desastres, lo que puede atribuirse a su tamaño y diversidad geográfica. Asimismo, países como Filipinas o Bangladesh presentan cifras elevadas en fenómenos específicos como tormentas e inundaciones, reflejando una mayor vulnerabilidad debido a su ubicación. En contraste, Japón y México destacan por la ocurrencia de terremotos y actividad volcánica, asociados al cinturón de fuego del Pacífico.

---

##  Conclusiones general

A partir del análisis realizado, observo que los desastres naturales no se distribuyen de manera aleatoria, sino que presentan patrones claros tanto en el tiempo como en su distribución geográfica.

En primer lugar, identifico un incremento en la cantidad de eventos a lo largo de las últimas décadas, especialmente a partir de los años 90. Considero que este aumento puede estar relacionado tanto con una mayor frecuencia de fenómenos extremos como con mejoras en los sistemas de registro y monitoreo.

En segundo lugar, al analizar la distribución mensual, noto la presencia de patrones estacionales, donde ciertos meses concentran una mayor cantidad de desastres. Esto me permite inferir una relación con ciclos climáticos, como temporadas de lluvias intensas, tormentas o sequías.

Por último, observo una concentración significativa de eventos en determinados países, como Estados Unidos, China e India. Interpreto que esto puede explicarse por factores como su extensión territorial, diversidad climática y nivel de exposición a distintos riesgos naturales.

---




##  Autor

Trabajo práctico desarrollado por: Ivan Quiottaso

Materia: Procesamiento de Datos.

