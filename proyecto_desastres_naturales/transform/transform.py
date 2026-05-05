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


# Curación de datos
def limpiar_datos(df):
  
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

    df['Disaster Type'] = df['Disaster Type'].str.lower().str.strip()
    df['Country'] = df['Country'].str.strip()

    df['Disaster Type'] = df['Disaster Type'].fillna('desconocido')
    df['Country'] = df['Country'].fillna('desconocido')

    return df



def filtrar_ultimos_20(df):
    return df[df['Year'] >= 2000]


# Función principal de transformación (SIN FILTRO)
def transform_data(df):
    df = crear_fecha(df)
    df = limpiar_datos(df)
    return df