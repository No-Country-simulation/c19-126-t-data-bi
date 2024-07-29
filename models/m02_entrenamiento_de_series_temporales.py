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
                      end='2024-06-30', 
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