# ========== Librerias ==========
import os,sys
sys.path.append(os.getcwd())
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# ========== Carga de datos ==========
df_usa = pd.read_csv('c19-126-t-data-bi/files/datasets/intermediate/usa_cierre.csv', index_col=[0], parse_dates=[0])
df_asia = pd.read_csv('c19-126-t-data-bi/files/datasets/intermediate/asia_cierre.csv', index_col=[0], parse_dates=[0])
df_europe = pd.read_csv('c19-126-t-data-bi/files/datasets/intermediate/euro_cierre.csv', index_col=[0], parse_dates=[0])

# ========== Funciones ==========

#  ---------- analisys_series ----------
def analisys_series(df, period):
    """
    Aplica seasonal_decompose a cada columna de un DataFrame, muestra y guarda las gráficas correspondientes.
    
    Parámetros:
    - df: DataFrame de pandas. Cada columna es una serie temporal.
    - period: El período de la serie temporal.
    
    Retorna:
    Un diccionario con tres claves ('trend', 'seasonal', 'resid') cada una conteniendo
    un DataFrame con las componentes descompuestas correspondientes para cada columna del DataFrame original.
    Además, muestra y guarda las gráficas de las componentes descompuestas.
    """
    decomposed = {'trend': pd.DataFrame(), 'seasonal': pd.DataFrame(), 'resid': pd.DataFrame()}
    save_path = 'c19-126-t-data-bi/preprocessing/figures'
    
    # Asegurarse de que el directorio existe
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    for column in df.columns:
        # Aplicar seasonal_decompose a la columna actual
        decomposed_result = seasonal_decompose(df[column], model='additive', period=period)
        
        # Almacenar los resultados en los DataFrames correspondientes
        decomposed['trend'][column] = decomposed_result.trend
        decomposed['seasonal'][column] = decomposed_result.seasonal
        decomposed['resid'][column] = decomposed_result.resid
        
        # Mostrar las gráficas
        plt.figure(figsize=(14, 8))
        plt.subplot(411)
        plt.plot(df[column], label='Original')
        plt.legend(loc='best')
        plt.subplot(412)
        plt.plot(decomposed_result.trend, label='Tendencia')
        plt.legend(loc='best')
        plt.subplot(413)
        plt.plot(decomposed_result.seasonal,label='Estacionalidad')
        plt.legend(loc='best')
        plt.subplot(414)
        plt.plot(decomposed_result.resid, label='Residuo')
        plt.legend(loc='best')
        plt.tight_layout()
        
        # Guardar las gráficas en la ruta especificada con el nombre de la columna correspondiente
        plt.savefig(f"{save_path}/{column}_decomposition.png")
        plt.show()
    
    return decomposed

# ========== Procesamiento ==========

# ---------- ordenamiento de los datos ----------
df_usa.sort_index(inplace=True)
df_asia.sort_index(inplace=True)
df_europe.sort_index(inplace=True)

# ---------- Eliminar valores ausentes ----------
df_usa.dropna(inplace=True)
df_asia.dropna(inplace=True)
df_europe.dropna(inplace=True)

# ---------- Descomposición de la serie temporal ----------
analisys_series(df_usa, period=1)
analisys_series(df_asia, period=1)
analisys_series(df_europe, period=1)