# ========== Librerias ==========
import os,sys
sys.path.append(os.getcwd())
import pandas as pd

# ========== Carga de datos ==========
df_usa = pd.read_csv('c19-126-t-data-bi/files/datasets/input/USA_historical_data.csv')
df_asia = pd.read_csv('c19-126-t-data-bi/files/datasets/input/ASIA_historical_data.csv')
df_europe = pd.read_csv('c19-126-t-data-bi/files/datasets/input/EURO_historical_data.csv')

# ========== Funciones ==========

#  ---------- close_value ----------
def close_value(dataframe):
    """
    Función que recibe un DataFrame y retorna un nuevo DataFrame con la primera columna y las columnas que terminan con "_Close".
    dataframe: DataFrame original
    return: DataFrame filtrado
    """
    # Crear un nuevo DataFrame con la primera columna del DataFrame original
    df_filtrado = pd.DataFrame(dataframe.iloc[:, 0])
    
    # Iterar sobre las columnas del DataFrame original
    for columna in dataframe.columns:
        # Verificar si el nombre de la columna termina con "_Close"
        if columna.endswith("_Close"):
            # Añadir la columna al nuevo DataFrame
            df_filtrado[columna] = dataframe[columna]
    
    return df_filtrado

# ========== Procesamiento ==========
df_cierre_usa = close_value(df_usa)
df_cierre_asia = close_value(df_asia)
df_cierre_euro = close_value(df_europe)

# ========== Guardar datos ==========
df_cierre_usa.to_csv('c19-126-t-data-bi/files/datasets/intermediate/usa_cierre.csv', index=False)
df_cierre_asia.to_csv('c19-126-t-data-bi/files/datasets/intermediate/asia_cierre.csv', index=False)
df_cierre_euro.to_csv('c19-126-t-data-bi/files/datasets/intermediate/euro_cierre.csv', index=False)