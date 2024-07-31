# ========== Librerias ==========

import os
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import klib
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# ---------- Librerias de plotly ----------
import plotly as plotly
import plotly.io as plotly
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# ---------- Tamaño de los graficos ----------
from pylab import rcParams
rcParams['figure.figsize'] = (18,7)

# ---------- Herramientas de stats ----------
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# ---------- Herramientas para el modelado ----------
from statsforecast import StatsForecast
from statsforecast.models import SklearnModel
from statsforecast.models import AutoARIMA
from statsforecast.models import SeasonalNaive
from sklearn.linear_model import Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor
from utilsforecast.plotting import plot_series
from statsforecast.utils import ConformalIntervals
from sklearn.preprocessing import StandardScaler

# ---------- Metricas ----------
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math

# ---------- Descarga de acciones ----------
import yfinance as yf

# ---------- Warnings ----------
# import warnings
# warnings.filterwarnings("ignore")


# ========== Cargar datos ==========

df = yf.download('AAPL', 
                      start='2014-06-30', 
                      end='2024-06-28', 
                      progress=False, interval='1d')


# ========== Información general ==========

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# ========== Exploración de datos ==========

# ---------- Volumen de acciones ----------
plt.figure(figsize = (18,6))
sns.lineplot(data = df, x = df.index, y = df["Volume"]);
plt.title("Volumen de acciones")
plt.show()

# ---------- Precio de cierre ----------
plt.figure(figsize = (18,6))
sns.lineplot(data = df, x = df.index, y = 'Close')
plt.title('Precio de cierre a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Precio de cierre')
plt.show()

sns.kdeplot(df['Close'], fill = True);
plt.title("Distribución de precios de cierre")
plt.show()

klib.dist_plot(df["Close"]) 
plt.show()

fig = px.line(df,x=df.index,y="Close",title="Precio de cierre: Range Slider y Selectores")
fig.update_xaxes(rangeslider_visible=True,rangeselector=dict(
    buttons=list([
        dict(count=1,label="1m",step="month",stepmode="backward"),
        dict(count=6,label="6m",step="month",stepmode="backward"),
        dict(count=1,label="YTD",step="year",stepmode="todate"),
        dict(count=1,label="1y",step="year",stepmode="backward"),
        dict(step="all")
])))
fig.show()

# ---------- Visualización de candlestick plots ----------
fig = go.Figure(data=[go.Candlestick(x=df.index,
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'])])

# Ajustar el tamaño de la figura
fig.update_layout(width=1800, height=600)

fig.show()


# ========== Ingenieria de datos ==========

# ---------- Retorno ----------
df['Return'] = (df['Adj Close']-df['Open'])/df['Open']
print(df.sample(5))

fig = px.line(df,x=df.index,y="Return",title="Retorno: Range Slider y Selectores")
fig.update_xaxes(rangeslider_visible=True,rangeselector=dict(
    buttons=list([
        dict(count=1,label="1m",step="month",stepmode="backward"),
        dict(count=6,label="6m",step="month",stepmode="backward"),
        dict(count=1,label="YTD",step="year",stepmode="todate"),
        dict(count=1,label="1y",step="year",stepmode="backward"),
        dict(step="all")
])))
fig.show()

#  ---------- Shifts y lags ----------

# Lag de cierre
fig = go.Figure()
df['Lag_Close_M'] = df['Close'].shift(10)
fig.add_trace(go.Scatter(x=df.index,y=df.Close,name='Close'))
fig.add_trace(go.Scatter(x=df.index,y=df.Lag_Close_M,name='Lag_Close_M'))
fig.show()

# Lag de volumen
fig = go.Figure()
df['Lag_Volume_M'] = df['Volume'].shift(10)
fig.add_trace(go.Scatter(x=df.index,y=df.Volume,name='Volume'))
fig.add_trace(go.Scatter(x=df.index,y=df.Lag_Volume_M,name='Lag_Volume_M'))
fig.show()

# ---------- Media movil ----------
df['SMA_5'] = df['Close'].rolling(window = 5).mean().shift()
df['SMA_15'] = df['Close'].rolling(window = 15).mean().shift()

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index,y=df.SMA_5,name='SMA_5'))
fig.add_trace(go.Scatter(x=df.index,y=df.SMA_15,name='SMA_15'))
fig.add_trace(go.Scatter(x=df.index,y=df.Close,name='Close', opacity=0.3))
fig.show()

#  ---------- Media movil exponencial ----------
df['EMA_5'] = df['Close'].ewm(5).mean().shift()
df['EMA_15'] = df['Close'].ewm(15).mean().shift()

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index,y=df.EMA_5,name='EMA_5'))
fig.add_trace(go.Scatter(x=df.index,y=df.EMA_15,name='EMA_15'))
fig.add_trace(go.Scatter(x=df.index,y=df.Close,name='Close', opacity=0.3))
fig.show()

#  ---------- Señal ----------
df['signal'] = np.where(df['SMA_5'] > df['SMA_15'], 1, 0)
df['signal'] = np.where(df['SMA_5'] < df['SMA_15'], -1, df['signal'])
df.dropna(inplace=True)
df.head()

#  ---------- Sistema de retorno ----------
df['system_return'] = df['signal'] * df['Return']
df['entry'] = df.signal.diff()
df.head()

#  ---------- Indice de fuerza relativa ----------
def RSI(df,n=14):
    close = df['Close']
    delta = close.diff()
    delta = delta[1:]
    pricesUp = delta.copy()
    pricesDown = delta.copy()
    pricesUp[pricesUp<0]=0
    pricesDown[pricesDown>0]=0
    rollUp = pricesUp.rolling(n).mean()
    rollDown = pricesDown.abs().rolling(n).mean()
    rs = rollUp/rollDown
    rsi = 100.0 - (100.0 / (1.0 + rs))
    return rsi

df['RSI'] = RSI(df).fillna(0)

fig = go.Figure(go.Scatter(x=df.index,y=df.RSI,name='RSI'))
fig.show()

#  ---------- Convergencia/Divergencia de Medias Móviles ----------
# Estimamos el promedio movil de 12 y 26 dias
df['EMA_12'] = pd.Series(df['Close'].ewm(span=12).mean())
df['EMA_26'] = pd.Series(df['Close'].ewm(span=26).mean())

# Calculamos MACD
df['MACD'] = pd.Series(df['EMA_12'] - df['EMA_26'])
df['MACD_signal'] = pd.Series(df.MACD.ewm(span=9,min_periods=9).mean())

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index,y=df.MACD,name='MACD'))
fig.add_trace(go.Scatter(x=df.index,y=df.MACD_signal,name='MACD_signal'))
fig.show()

print(df.head())


# ========== Descomposición de series temporales ==========

#  ---------- Diario ----------
series = df.Close
result = seasonal_decompose(series, model='additive',period=1)
figure = result.plot()
plt.show()

#  ---------- Semana ----------
series = df.Close
result = seasonal_decompose(series, model='additive',period=7)
figure = result.plot()
plt.show()

#  ---------- Mes ----------
series = df.Close
result = seasonal_decompose(series, model='additive',period=30)
figure = result.plot()
plt.show()

#  ---------- Año ----------
series = df.Close
result = seasonal_decompose(series, model='additive',period=365)
figure = result.plot()
plt.show()


# ========== Pruebas de estacionariedad/Prueba ADF (Dickey-Fuller aumentada) ==========

# ---------- Función para el calculo ----------
def test_stationarity(timeseries):
    
    #Determing rolling statistics
    rolmean = timeseries.rolling(12).mean()
    rolstd = timeseries.rolling(12).std()
    
    #Plot rolling statistics:
    plt.figure(figsize=(15,5))
    plt.plot(timeseries,color='blue',label='Original')
    plt.plot(rolmean,color='red',label='Rolling Mean')
    plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean and Standard Deviation')
    plt.show(block=False)
    
    print("Results of dickey fuller test")
    adft = adfuller(timeseries,autolag='AIC')
    # output for dft will give us without defining what the values are.
    #hence we manually write what values does it explains using a for loop
    output = pd.Series(adft[0:4],index=['Test Statistics','p-value','No. of lags used','Number of observations used'])
    print(output)

# ---------- Prueba de estacionariedad ----------
test_stationarity(df['Close'])

# ========== Diferenciación ==========

df['Stocks First Difference']=df['Close']-df['Close'].shift(1)
df['Stocks Seasonal Difference']=df['Close']-df['Close'].shift(12)
df['Stocks Seasonal+Daily Difference']=df['Stocks Seasonal Difference']-df['Stocks Seasonal Difference'].shift(1)

adft = adfuller(df['Stocks First Difference'].dropna(),autolag='AIC')
output = pd.Series(adft[0:4],index=['Estadísticas de prueba','valor p','No. de rezagos utilizados','Número de observaciones utilizadas'])
print(output)

adft = adfuller(df['Stocks Seasonal Difference'].dropna(),autolag='AIC')
output = pd.Series(adft[0:4],index=['Estadísticas de prueba','valor p','No. de rezagos utilizados','Número de observaciones utilizadas'])
print(output)

adft = adfuller(df['Stocks Seasonal+Daily Difference'].dropna(),autolag='AIC')
output = pd.Series(adft[0:4],index=['Estadísticas de prueba','valor p','No. de rezagos utilizados','Número de observaciones utilizadas'])
print(output)

df['Stocks First Difference'].plot();
plt.show()

# ========== Modelo ARIMA ==========

acf_values = sm.tsa.acf(df["Close"])
acf_values

plot_acf(df["Stocks First Difference"].dropna(),lags=5,title="AutoCorrelation")
plt.show()

plot_acf(df["Stocks Seasonal Difference"].dropna(),lags=15,title="AutoCorrelation")
plt.show()

plot_acf(df["Stocks Seasonal+Daily Difference"].dropna(),lags=10,title="AutoCorrelation")
plt.show()

plot_pacf(df["Stocks First Difference"].dropna(),lags=5,title="Partial AutoCorrelation")
plt.show()

plot_pacf(df["Stocks Seasonal Difference"].dropna(),lags=15,title="Partial AutoCorrelation")
plt.show()

plot_pacf(df["Stocks Seasonal+Daily Difference"].dropna(),lags=10,title="Partial AutoCorrelation")
plt.show()

plt.figure(figsize=(18,8))
sns.heatmap(df.corr(), annot=True, cmap="Set3_r",  fmt='.02f',)
plt.show()

# ========== Creación de cracteristicas y objetivo ==========

sipi = df.copy()
sipi = sipi.reset_index()
print(sipi.columns)
print(sipi.tail(32))

ohe = sipi[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'SMA_5', 'SMA_15', 'EMA_5' ]]
ohe = ohe.rename(columns= {"Date":"ds", "Close": "y"})
ohe["unique_id"] = 1
ohe.head()

train = ohe[ohe.ds<='2023-05-13'] 
test = ohe[(ohe['ds'] > '2023-05-13')]

test.drop("y",axis=1, inplace=True)

print(train.head())
print(test.head())
print(train.shape)
print(test.shape)


# ========== Modelado ==========

season_length = 7 

# ---------- Escalado de caracteristicas ----------
scaler = StandardScaler()
train_scaled = train.copy()
test_scaled = test.copy()

features = ['Open', 'High', 'Low', 'Adj Close', 'SMA_5', 'SMA_15', 'EMA_5']
train_scaled[features] = scaler.fit_transform(train[features])
test_scaled[features] = scaler.transform(test[features])

# ---------- Seleccion de modelos escalado ----------
models = [AutoARIMA(season_length=season_length),
          SeasonalNaive(season_length=season_length),
          SklearnModel(Lasso(max_iter=20000, alpha=0.1)),
          SklearnModel(Ridge(max_iter=20000, alpha=0.1)),
          SklearnModel(RandomForestRegressor())
          ]

# ---------- Seleccion de modelos----------
# models = [AutoARIMA(season_length=season_length),
#           SeasonalNaive(season_length=season_length),
#           SklearnModel(Lasso()),
#           SklearnModel(Ridge()),
#           SklearnModel(RandomForestRegressor())
#           ]

# ---------- Construir el modelo ----------
sf = StatsForecast( models=models,
                   freq='B', 
                   fallback_model = SeasonalNaive(season_length=season_length),
                   n_jobs=-1)

#  ---------- Entrenar el modelo ----------
# intervals = ConformalIntervals(h = 32, n_windows = 5)
# sf.fit(df=train, prediction_intervals=intervals)


#   ---------- Entrenar el modelo con datos escalados----------
intervals = ConformalIntervals(h = 32, n_windows = 5)
sf.fit(df=train_scaled, prediction_intervals=intervals)

# ========== Predicciones ==========

# h = len(test_scaled)
test_scaled_32 = test_scaled.tail(32)

preds = sf.forecast(
    df=train_scaled,
    h=32,  # Ajustar el horizonte de pronóstico
    X_df=test_scaled_32, 
    prediction_intervals=ConformalIntervals(n_windows=5, h=32),
    level=[95],
)
preds.head()






# Guardar predicciones como csv
preds.to_csv("c19-126-t-data-bi/models/predicciones_AAPL.csv", index=False)

# ---------- Visualización de predicciones ----------
# def plot_series(ohe, preds, max_insample_length=100, engine="plotly", models=None):
#     if engine == "plotly":
#         if models:
#             for model in models:
#                 fig = px.line(preds, x='ds', y=model, title=f'Series Plot - {model}')
#                 fig.show()
#         else:
#             fig = px.line(preds, x='ds', y=preds.columns[2:], title='Series Plot')
#             fig.show()
#     else:
#         pass

# plot_series(ohe,  preds.reset_index(),max_insample_length= 100, engine= "plotly")
# plot_series(ohe,  preds.reset_index(),max_insample_length= 100, engine= "plotly", models = ["AutoARIMA"])
# plot_series(ohe,  preds.reset_index(),max_insample_length= 100, engine= "plotly", models = ["Lasso"])
# plot_series(ohe,  preds.reset_index(),max_insample_length= 100, engine= "plotly", models = ["Ridge"])
# plot_series(ohe,  preds.reset_index(),max_insample_length= 100, engine= "plotly", models = ["RandomForestRegressor"])


# ========== Evaluación del modelo ==========
