# ========== Librerias ==========
import os,sys
sys.path.append(os.getcwd())
import pandas as pd

import xgboost as xgb
from lightgbm import LGBMRegressor
from sklearn.model_selection import train_test_split

# ========== Carga de datos ==========
df = pd.read_csv('c19-126-t-data-bi/files/datasets/intermediate/usa/AAPL_Close.csv', index_col=[0], parse_dates=[0])

df

# ========== Funciones ==========

#  ---------- Make features ----------

def make_features(df, lag, rolling_mean_size):
    """
    Crea características adicionales para un DataFrame de series temporales.

    Parametros:
    -df: Dataframe original
    -lag: Número de retrasos a considerar
    -rolling_mean_size: Tamaño de la ventana para el promedio móvil

    """
    df_copy = df.copy()
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month
    df_copy['day'] = df_copy.index.day
    df_copy['dayofweek'] = df_copy.index.dayofweek

    for lag in range(1, lag + 1):
        df_copy['lag_{}'.format(lag)] = df_copy.iloc[:, 0].shift(lag)

    df_copy['rolling_mean'] = (df_copy.iloc[:, 0].shift().rolling(rolling_mean_size).mean())
       
    df_cleaned = df_copy.dropna()
    
    return df_cleaned

# ========== Preprocesamiento ==========

# ---------- Creación de caracteristicas ----------

# Creacion de features día siguiente
df_next_day = make_features(df,2, 3)

df_next_day.head()

train, test = train_test_split(df_next_day, shuffle=False, test_size=0.1)

features_train_next_day = train.drop(['num_orders'], axis=1)
target_train_next_day = train['num_orders']
features_test_next_day = test.drop(['num_orders'], axis=1)
target_test_next_day = test['num_orders']