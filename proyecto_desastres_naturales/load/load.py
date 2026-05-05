import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Crear carpeta outputs si no existe
os.makedirs("outputs", exist_ok=True)


def grafico_anual(df):
    plt.figure()
    df.groupby('Year').size().plot()
    plt.title("Cantidad de desastres por año")
    plt.xlabel("Año")
    plt.ylabel("Cantidad")
    plt.savefig("outputs/grafico_anual.png")
    plt.close()


def grafico_ultimos(df):
    plt.figure()
    df.groupby('Year').size().plot()
    plt.title("Desastres desde el 2000")
    plt.xlabel("Año")
    plt.ylabel("Cantidad")
    plt.savefig("outputs/grafico_ultimos.png")
    plt.close()


def grafico_mensual(df):
    plt.figure()
    df.groupby('Start Month').size().plot(kind='bar')
    plt.title("Desastres por mes")
    plt.xlabel("Mes")
    plt.ylabel("Cantidad")
    plt.savefig("outputs/grafico_mensual.png")
    plt.close()


def grafico_heatmap(df):
    tabla = df.groupby(['Year', 'Start Month']).size().unstack()

    plt.figure()
    sns.heatmap(tabla, cmap="coolwarm")
    plt.title("Heatmap de desastres por mes y año")
    plt.savefig("outputs/grafico_heatmap.png")
    plt.close()


def grafico_tipos(df):
    plt.figure()
    df['Disaster Type'].value_counts().head(10).plot(kind='bar')
    plt.title("Top 10 tipos de desastres")
    plt.savefig("outputs/grafico_tipos.png")
    plt.close()


def grafico_paises(df):
    plt.figure()
    df['Country'].value_counts().head(10).plot(kind='bar')
    plt.title("Países más afectados")
    plt.savefig("outputs/grafico_paises.png")
    plt.close()


def grafico_cruce_tipo_pais(df):
    tabla = pd.crosstab(df['Country'], df['Disaster Type'])

    tabla.loc[tabla.sum(axis=1).sort_values(ascending=False).head(10).index] \
         .plot(kind='bar', stacked=True)

    plt.title("Tipos de desastres por país")
    plt.xlabel("País")
    plt.ylabel("Cantidad")
    plt.savefig("outputs/grafico_cruce_tipo_pais.png")
    plt.close()


def grafico_inundaciones(df):
    inundaciones = df[df['Disaster Type'] == 'flood']
    inundaciones['Country'].value_counts().head(10).plot(kind='bar')
    plt.title("Países con más inundaciones")
    plt.savefig("outputs/grafico_inundaciones.png")
    plt.close()


def grafico_tormentas(df):
    tormentas = df[df['Disaster Type'] == 'storm']
    tormentas['Country'].value_counts().head(10).plot(kind='bar')
    plt.title("Países con más tormentas")
    plt.savefig("outputs/grafico_tormentas.png")
    plt.close()



def load_data(df):
    # 👉 filtro SOLO para este gráfico
    df_ultimos = df[df['Year'] >= 2000]

    grafico_anual(df)           # 1970 → actual
    grafico_ultimos(df_ultimos) # 2000 → actual

    grafico_mensual(df)
    grafico_heatmap(df)
    grafico_tipos(df)
    grafico_paises(df)
    grafico_cruce_tipo_pais(df)
    grafico_inundaciones(df)
    grafico_tormentas(df)

    print("ETL completado. Gráficos guardados en /outputs")