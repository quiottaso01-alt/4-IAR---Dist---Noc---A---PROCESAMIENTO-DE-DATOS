import pandas as pd

def cargar_datos(url):
    df = pd.read_csv(url)
    return df

def explorar_datos(df):
    print("Columnas del dataset:")
    print(df.columns)

    print("\nPrimeras filas:")
    print(df.head())

    print("\nInformación general:")
    print(df.info())

    print("\nValores nulos:")
    print(df.isnull().sum())

def extract_data(url):
    df = cargar_datos(url)
    explorar_datos(df)
    return df