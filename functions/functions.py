# Librerias
import pandas as pd

# close_value
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
            df_filtrado[columna] = df_original[columna]
    
    return df_filtrado