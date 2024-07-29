import yfinance as yf
import pandas as pd

# Descargar datos históricos de una acción (por ejemplo, Apple Inc.)
data = yf.download('AAPL', start='2010-01-01', end='2023-07-01')

print(data.head())

data = data.dropna()  # Eliminar filas con valores faltantes
data.reset_index(inplace=True)  # Resetear el índice para asegurarse de que las fechas son una columna
data['Date'] = pd.to_datetime(data['Date'])  # Convertir fechas a formato datetime

import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))
plt.plot(data['Date'], data['Close'])
plt.title('Precio de cierre de AAPL a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Precio de cierre')
plt.show()

from sklearn.model_selection import train_test_split

# Usaremos el 80% de los datos para entrenamiento y el 20% para prueba
train_size = int(len(data) * 0.8)
train, test = data[:train_size], data[train_size:]


from statsmodels.tsa.arima.model import ARIMA

# Crear y ajustar el modelo ARIMA
model = ARIMA(train['Close'], order=(5, 1, 0))
model_fit = model.fit()

# Pronosticar
forecast = model_fit.forecast(steps=len(test))


from sklearn.metrics import mean_absolute_error

# Calcular MAE
mae = mean_absolute_error(test['Close'], forecast)
print(f'MAE: {mae}')


# Pronosticar a un año (252 días hábiles en un año)
future_forecast = model_fit.forecast(steps=252)

# Crear un DataFrame para los pronósticos futuros
future_dates = pd.date_range(start=test['Date'].iloc[-1], periods=252, freq='B')
future_df = pd.DataFrame({'Date': future_dates, 'Forecast': future_forecast})

plt.figure(figsize=(14, 7))
plt.plot(data['Date'], data['Close'], label='Histórico')
plt.plot(future_df['Date'], future_df['Forecast'], label='Pronóstico a un año', color='red')
plt.title('Pronóstico de precio de cierre de AAPL a un año')
plt.xlabel('Fecha')
plt.ylabel('Precio de cierre')
plt.legend()
plt.show()