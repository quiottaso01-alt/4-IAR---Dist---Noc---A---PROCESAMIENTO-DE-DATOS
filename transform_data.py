import pandas as pd

# Crear columna fecha
def crear_fecha(df):
    df['Start Month'] = df['Start Month'].fillna(1).astype(int)

    df['fecha'] = pd.to_datetime(
        df[['Year', 'Start Month']]
        .rename(columns={'Year': 'year', 'Start Month': 'month'})
        .assign(day=1)
    )

    return df


# Filtrar últimos 20 años
def filtrar_ultimos_20(df):
    return df[df['Year'] >= 2000]


# Curación de datos
def limpiar_datos(df):
    df['Disaster Type'] = df['Disaster Type'].str.lower().str.strip()
    df['Country'] = df['Country'].str.strip()

    df['Disaster Type'] = df['Disaster Type'].fillna('desconocido')
    df['Country'] = df['Country'].fillna('desconocido')

    return df


# Análisis
def desastres_por_anio(df):
    return df.groupby('Year').size()

def desastres_por_mes(df):
    return df.groupby('Start Month').size().sort_index()

def top_tipos(df):
    return df['Disaster Type'].value_counts()

def top_paises(df):
    return df['Country'].value_counts()


# Cruces
def filtrar_por_tipo(df, tipo):
    return df[df['Disaster Type'] == tipo]
