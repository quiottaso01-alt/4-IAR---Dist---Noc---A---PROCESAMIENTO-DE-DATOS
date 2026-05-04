import pandas as pd

def crear_fecha(df):
    df['Start Month'] = df['Start Month'].fillna(1).astype(int)

    df['fecha'] = pd.to_datetime(
        df[['Year', 'Start Month']]
        .rename(columns={'Year': 'year', 'Start Month': 'month'})
        .assign(day=1)
    )

    return df

def filtrar_ultimos_20(df):
    return df[df['Year'] >= 2000]

def limpiar_datos(df):
    df['Disaster Type'] = df['Disaster Type'].str.lower().str.strip()
    df['Country'] = df['Country'].str.strip()

    df['Disaster Type'] = df['Disaster Type'].fillna('desconocido')
    df['Country'] = df['Country'].fillna('desconocido')

    return df

def desastres_por_anio(df):
    return df.groupby('Year').size()

def desastres_por_mes(df):
    return df.groupby('Start Month').size().sort_index()

def top_tipos(df):
    return df['Disaster Type'].value_counts()

def top_paises(df):
    return df['Country'].value_counts()

def filtrar_por_tipo(df, tipo):
    return df[df['Disaster Type'] == tipo]

#  FUNCIÓN PRINCIPAL
def transform_data(df):
    df = crear_fecha(df)
    df = limpiar_datos(df)
    df = filtrar_ultimos_20(df)
    return df
