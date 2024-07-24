# ========== Librerias ==========
import os,sys
sys.path.append(os.getcwd())
import pandas as pd


# ========== Carga de datos ==========
df_usa = pd.read_csv('c19-126-t-data-bi/files/datasets/intermediate/usa_cierre.csv', index_col=[0], parse_dates=[0])
df_asia = pd.read_csv('c19-126-t-data-bi/files/datasets/intermediate/asia_cierre.csv', index_col=[0], parse_dates=[0])
df_europe = pd.read_csv('c19-126-t-data-bi/files/datasets/intermediate/euro_cierre.csv', index_col=[0], parse_dates=[0])

# ========== Funciones ==========

#  ---------- column_dataframes ----------
def column_dataframes(df, save_path):
    """
    Crea y guarda DataFrames individuales para cada columna de un DataFrame original.
    
    Parámetros:
    - df: DataFrame original de pandas.
    - save_path: Ruta de la carpeta donde se guardarán los DataFrames.
    """
    # Asegurarse de que el directorio de guardado existe
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    # Iterar sobre las columnas del DataFrame
    for column in df.columns:
        # Crear un nuevo DataFrame para la columna actual
        new_df = pd.DataFrame(df[column])
        
        # Ordenar el DataFrame por el índice
        new_df.sort_index(inplace=True)
        
        # Eliminar valores ausentes
        new_df.dropna(inplace=True)
        
        # Construir la ruta completa del archivo
        file_path = os.path.join(save_path, f"{column}.csv")
        
        # Guardar el DataFrame en un archivo CSV
        new_df.to_csv(file_path)

# ========== Procesamiento ==========

column_dataframes(df_usa, 'c19-126-t-data-bi/files/datasets/intermediate/usa')
column_dataframes(df_asia, 'c19-126-t-data-bi/files/datasets/intermediate/asia')
column_dataframes(df_europe, 'c19-126-t-data-bi/files/datasets/intermediate/euro')