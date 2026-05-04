 Proyecto ETL - Desastres Naturales
 Descripción

Este proyecto implementa un proceso ETL (Extract, Transform, Load) en Python para analizar desastres naturales a nivel global.

El flujo del proyecto es:

Extract: carga y exploración de los datos desde una fuente externa
Transform: limpieza, procesamiento y preparación de los datos
Load: generación de gráficos para el análisis
 Estructura del proyecto
proyecto_desastres_naturales/
├── extract/
├── transform/
├── load/
├── outputs/
├── main.py
└── README.md
▶ Ejecución

Para ejecutar el proyecto:

python main.py
 Análisis y Visualizaciones
 Desastres por año




Conclusión:
A partir del gráfico se observa un incremento sostenido en la cantidad de desastres naturales desde la década de 1980, con un crecimiento más marcado hacia finales de los años 90 y principios de los 2000. Este aumento puede estar relacionado tanto con una mayor frecuencia de eventos extremos como con mejoras en los sistemas de registro y monitoreo a nivel global. También se identifican fluctuaciones interanuales que reflejan la variabilidad propia de estos fenómenos.

 Desastres en los últimos años




Conclusión:
Al analizar las últimas dos décadas, se observa que la cantidad de desastres se mantiene en niveles elevados, aunque con variaciones entre distintos años. Esto indica que la frecuencia de estos eventos continúa siendo alta, incluso sin un crecimiento lineal constante.

 Desastres por mes




Conclusión:
La distribución mensual muestra que ciertos meses concentran una mayor cantidad de eventos. Esto permite inferir la existencia de patrones estacionales, posiblemente asociados a ciclos climáticos como temporadas de lluvias intensas, tormentas o sequías.

 Heatmap de desastres




Conclusión:
El heatmap permite visualizar con claridad la distribución temporal de los desastres. Se observa una mayor concentración de eventos en períodos recientes y algunos meses presentan intensidades más elevadas, lo que confirma la presencia de patrones estacionales.

 Tipos de desastres




Conclusión:
El análisis muestra que predominan los desastres de origen climático, especialmente inundaciones y tormentas. Esto evidencia la relevancia de los fenómenos hidrometeorológicos dentro del total de eventos registrados.

 Países más afectados




Conclusión:
Se observa que países como Estados Unidos, China e India registran una mayor cantidad de desastres. Esto puede explicarse por factores como su extensión territorial, diversidad climática y alta densidad poblacional.

 Tipo de desastre por país




Conclusión:
Estados Unidos, China e India concentran la mayor cantidad de desastres, lo que puede atribuirse a su tamaño y diversidad geográfica. Asimismo, países como Filipinas o Bangladesh presentan cifras elevadas en fenómenos específicos como tormentas e inundaciones, reflejando una mayor vulnerabilidad debido a su ubicación. En contraste, Japón y México destacan por la ocurrencia de terremotos y actividad volcánica, asociados al cinturón de fuego del Pacífico.

 Conclusión general

El análisis evidencia un aumento en la frecuencia de los desastres naturales a lo largo del tiempo, con una fuerte presencia de eventos de origen climático. Además, se identifican patrones estacionales y diferencias geográficas significativas, lo que permite comprender mejor la distribución y características de estos fenómenos a nivel global.