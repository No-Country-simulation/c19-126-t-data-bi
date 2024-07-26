# ========== Librerias ==========
import os,sys
sys.path.append(os.getcwd())
import pandas as pd
import numpy as np

import xgboost as xgb
import lightgbm as lgb
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV, TimeSeriesSplit
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# ========== Carga de datos ==========
df = pd.read_csv('c19-126-t-data-bi/files/datasets/intermediate/usa/AAPL_Close.csv', index_col=[0], parse_dates=[0])

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

# Creacion de caracteristicas y objetivo día siguiente
df_next_day = make_features(df,2, 3)

train, test = train_test_split(df_next_day, shuffle=False, test_size=0.1)

features_train_next_day = train.drop(train.columns[0], axis=1)
target_train_next_day = train.iloc[:, 0]
features_test_next_day = test.drop(test.columns[0], axis=1)
target_test_next_day = test.iloc[:, 0]

# Creacion de caracteristicas y objetivo semana
df_week = make_features(df,5, 6)

train, test = train_test_split(df_week, shuffle=False, test_size=0.1)

features_train_week = train.drop(train.columns[0], axis=1)
target_train_week = train.iloc[:, 0]
features_test_week = test.drop(test.columns[0], axis=1)
target_test_week = test.iloc[:, 0]

# Creacion de caracteristicas y objetivo mes
df_month = make_features(df,20, 21)

train, test = train_test_split(df_month, shuffle=False, test_size=0.1)

features_train_month = train.drop(train.columns[0], axis=1)
target_train_month = train.iloc[:, 0]
features_test_month = test.drop(test.columns[0], axis=1)
target_test_month = test.iloc[:, 0]

# ========== Entrenamiento de modelos ==========

# DataFrame para almacenar los resultados
results_df = pd.DataFrame(columns=['Model', 'Timeframe', 'Best Parameters', 'Best RMSE Score'])

# Función para realizar GridSearchCV y almacenar resultados
def perform_grid_search(model, param_grid, features_train, target_train, model_name, timeframe):
    # TimeSeriesSplit para la validación cruzada
    tscv = TimeSeriesSplit(n_splits=5)
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, scoring=rmse_scorer, cv=tscv, verbose=1)
    grid_search.fit(features_train, target_train)
    results_df.loc[len(results_df)] = [model_name, timeframe, grid_search.best_params_, grid_search.best_score_]

# Configuracion del scoring de RMSE
rmse_scorer = make_scorer(mean_squared_error, squared=False)

#  ---------- Xgboost ----------
xgb_model = xgb.XGBRegressor()
xgb_param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.8, 1.0]
}

perform_grid_search(xgb_model, xgb_param_grid, features_train_next_day, target_train_next_day, 'XGBoost', 'Next Day')
perform_grid_search(xgb_model, xgb_param_grid, features_train_week, target_train_week, 'XGBoost', 'Week')
perform_grid_search(xgb_model, xgb_param_grid, features_train_month, target_train_month, 'XGBoost', 'Month')

#  ---------- LightGBM ----------
lgb_model = lgb.LGBMRegressor()
lgb_param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'learning_rate': [0.01, 0.1, 0.2],
    'subsample': [0.8, 1.0]
}

perform_grid_search(lgb_model, lgb_param_grid, features_train_next_day, target_train_next_day, 'LightGBM', 'Next Day')
perform_grid_search(lgb_model, lgb_param_grid, features_train_week, target_train_week, 'LightGBM', 'Week')
perform_grid_search(lgb_model, lgb_param_grid, features_train_month, target_train_month, 'LightGBM', 'Month')

#  ---------- Linear Regression ----------
lr_param_grid = {
    'regressor__fit_intercept': [True, False]
}

# Crear un pipeline que incluya el escalado y el modelo
lr_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

# Actualizar las llamadas a perform_grid_search para usar el pipeline
perform_grid_search(lr_pipeline, lr_param_grid, features_train_next_day, target_train_next_day, 'Linear Regression', 'Next Day')
perform_grid_search(lr_pipeline, lr_param_grid, features_train_week, target_train_week, 'Linear Regression', 'Week')
perform_grid_search(lr_pipeline, lr_param_grid, features_train_month, target_train_month, 'Linear Regression', 'Month')

# Mostrar el DataFrame con los resultados
print(results_df)

#  ---------- Guardar datos ----------
results_df.to_csv('c19-126-t-data-bi/models/test_results.csv', index=False)


# ========== Prueba de modelos con conjunto de validación ==========

# ---------- Mejores parametros ----------
best_params_xgb = {'n_estimators': 50, 'max_depth': 3, 'learning_rate': 0.01, 'subsample': 0.8}
best_params_lgb = {'n_estimators': 50, 'max_depth': 3, 'learning_rate': 0.01, 'subsample': 0.8}
best_params_lr = {'regressor__fit_intercept': False}

#  ---------- Entrenamiento con los mejoresmodelos ----------
xgb_model.set_params(**best_params_xgb)
xgb_model.fit(features_train_next_day, target_train_next_day)

lgb_model.set_params(**best_params_lgb)
lgb_model.fit(features_train_next_day, target_train_next_day)

lr_model = LinearRegression()
lr_model.fit(features_train_next_day, target_train_next_day)

#  ---------- Predicciones en el conjunto de validación ----------
xgb_predictions = xgb_model.predict(features_test_next_day)
lgb_predictions = lgb_model.predict(features_test_next_day)
lr_predictions = lr_model.predict(features_test_next_day)

#  ---------- Calculo de RMSE ----------
xgb_rmse = np.sqrt(mean_squared_error(target_test_next_day, xgb_predictions))
lgb_rmse = np.sqrt(mean_squared_error(target_test_next_day, lgb_predictions))
lr_rmse = np.sqrt(mean_squared_error(target_test_next_day, lr_predictions))

print(f'XGBoost RMSE: {xgb_rmse}')
print(f'LightGBM RMSE: {lgb_rmse}')
print(f'Linear Regression RMSE: {lr_rmse}')


# ========== Graficado de resultados ==========
plt.figure(figsize=(14, 7))

#  Predicciones de XGBoost
plt.subplot(1, 3, 1)
plt.plot(target_test_next_day.index, target_test_next_day, label='Original', alpha=0.7)
plt.plot(target_test_next_day.index, xgb_predictions, label='Predicción', alpha=0.7)
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Predicciones de XGBoost')
plt.legend()

# Predicciones de LightGBM
plt.subplot(1, 3, 2)
plt.plot(target_test_next_day.index, target_test_next_day, label='Original', alpha=0.7)
plt.plot(target_test_next_day.index, lgb_predictions, label='Predicción', alpha=0.7)
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Predicciones de LightGBM')
plt.legend()

# Predicciones de Linear Regression
plt.subplot(1, 3, 3)
plt.plot(target_test_next_day.index, target_test_next_day, label='Original', alpha=0.7)
plt.plot(target_test_next_day.index, lr_predictions, label='Predicción', alpha=0.7)
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Predicciones de Regresión Lineal')
plt.legend()

plt.tight_layout()

# Guardar la figura
output_dir = 'c19-126-t-data-bi/models'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'predicciones_modelos.png'))

plt.show()