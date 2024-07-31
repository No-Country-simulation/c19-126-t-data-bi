# ========== Librerias ==========
import os,sys
sys.path.append(os.getcwd())
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error

import tensorflow as tf
from keras import Model
from keras.models import Sequential
from keras.layers import Input, Dense, Dropout
from keras.layers import LSTM

# ========== Carga de datos ==========
df = pd.read_csv('c19-126-t-data-bi/files/datasets/input/forecasting/AMZN.csv')

# ========== Preprocesamiento ==========

# ---------- Ordemaniemto d edatos ----------
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', ascending=True, inplace=True)
df.reset_index(drop=True, inplace=True)

# ---------- Tamaño del dataset de prueba ----------
test_size = df[df.Date.dt.year == 2024].shape[0]
test_size

# ---------- División de conjuntos ----------
train_data = df[:-test_size].drop('Date', axis=1)
test_data = df[-test_size:].drop('Date', axis=1)

#  ---------- Escaldo ----------
scaler = MinMaxScaler()
scaler.fit(train_data)
train_scaled = scaler.transform(train_data)
test_scaled = scaler.transform(test_data)

train_scaled.shape, test_scaled.shape

# ---------- Reestructuración de datos y creción de ventana deslizante ----------
window_size = 60

# Función para crear datos de entrenamiento
def create_dataset(data, window_size):
  X, Y = [], []
  for i in range(window_size, len(data)):
    X.append(data[i-window_size:i, np.arange(data.shape[1]) != 3])
    Y.append(data[i, 3])
  return np.array(X), np.array(Y)

X_train, Y_train = create_dataset(train_scaled, window_size)
print(X_train.shape, Y_train.shape)

X_test, Y_test = create_dataset(test_scaled, window_size)
print(X_test.shape, Y_test.shape)

# ========== Modelado ==========

model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(window_size, X_train.shape[2])))
model.add(LSTM(50))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.summary()

# ---------- Entrenamiento de modelo ----------
history = model.fit(X_train, Y_train, epochs=100, batch_size=32, validation_split=0.1, verbose=1)

# ---------- Evaluación de modelo ----------
result = model.evaluate(X_test, Y_test)
Y_pred = model.predict(X_test)
MAPE = mean_absolute_percentage_error(Y_test, Y_pred)

print("Loss:", result)
print("MAPE:", MAPE)
print("Accuracy:", 1 - MAPE)

# ========== Visualizacion de resultados ==========

# ---------- Función para invertir el escalado ----------
def prepare_for_inverse_transform(data, original_shape):
  import numpy as np

  prepared_data = np.zeros((data.shape[0], original_shape))
  prepared_data[:, 3] = data.flatten()

  return prepared_data

#  ---------- Inversión del escalado ----------
original_shape = test_data.shape[1]

y_test_true_prepared = prepare_for_inverse_transform(Y_test, original_shape)
y_test_pred_prepared = prepare_for_inverse_transform(Y_pred, original_shape)

y_test_true = scaler.inverse_transform(y_test_true_prepared)[:, 3]
y_test_pred = scaler.inverse_transform(y_test_pred_prepared)[:, 3]

print("MAE:", mean_absolute_error(y_test_true, y_test_pred))

# ---------- Grafica de resultados ----------
plt.figure(figsize=(12, 6))
plt.plot(df['Date'][:-test_size], df['Close'][:-test_size], color='black', label='Actual Price')
plt.plot(df['Date'][-test_size:], df['Close'][-test_size:], color='blue', label='Actual Price')
plt.plot(df['Date'][-test_size+60:], y_test_pred, color='red', label='Predicted Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()