# c19-126-t-data-bi
Repositorio del grupo 126 data bi, del proyecto Análisis de Tendencias de Inversiones
![image](https://github.com/No-Country-simulation/c19-126-t-data-bi/blob/main/test/Logotipo%20(3).png?raw=true)

### 📝 Índice:

- [**Introducción**](#introducción)
- [**Resumen**](#resumen)
- [**Conceptos Claves**](#conceptos-claves)
- [**Público Objetivo**](#público-objetivo)
- [**Metodología**](#metodología)
   - [**Datos**](#datos)
   - [**Etapas del Proyecto**](#etapas-del-proyecto)
       - [**Mockup técnico**](#mockup-técnico)
       - [**Mockup sentimiento**](#mockup-sentimiento)
       - [**Mockup predictivo**](#mockup-predictivo)
- [**Visualización en Power BI**](#visualización-en-power-bi)
- [**Herramientas y librerías utilizadas en el proyecto**](#herramientas-y-librerías-utilizadas-en-el-proyecto)
- [**Contacto**](#contacto)

### Introducción:
 Este proyecto tiene como objetivo analizar las tendencias financieras en tres mercados principales: USA, Europa y Asia. Hemos seleccionado 10 acciones de cada mercado para estudiar. Actuando como una empresa consultora, proporcionamos insights y recomendaciones para una institución que desea crear un fondo de inversión para clientes sin experiencia en el mercado de valores. Nuestro análisis combina la experiencia de científicos de datos y analistas de datos para ofrecer insights completos y accionables.
### Resumen:
 Recopilamos datos sobre precios de acciones y volúmenes de negociación para las 30 acciones seleccionadas (10 de cada mercado) durante un período significativo, desde el 30 de junio de 2014 hasta el 30 de junio de 2024. El conjunto de datos incluye las siguientes columnas para cada ticker: precio de apertura (open), precio de cierre (close), precio máximo (high), precio mínimo (low), precio ajustado de cierre(adj.close) y volumen de negociación (volume). Además, compilamos datos sobre los seguidores de estas acciones en diversas plataformas para medir el sentimiento e interés de los inversores.
### Conceptos Claves:
 ◘ Tendencias Financieras: Análisis de cómo los precios de las acciones y otros indicadores financieros cambian con el tiempo.
 ◘ Predicciones de Precios: Uso de modelos estadísticos y de machine learning para prever los precios futuros de las acciones.
 ◘ Sentimiento del Inversor: Medición del interés y las emociones de los inversores respecto a las acciones, basada en datos de seguidores de varias plataformas.
### Público Objetivo:
 Este informe está dirigido a inversores y gestores de fondos que buscan información detallada y basada en datos para tomar decisiones de inversión informadas en los mercados de USA, Europa y Asia. También es útil para analistas financieros y consultoras que trabajan en la identificación de oportunidades de inversión.
### Metodología:
 Utilizamos metodologías ágiles para gestionar el proyecto, con reuniones diarias y herramientas de gestión de tareas como Trello para asignar y distribuir las tareas. Los científicos de datos realizaron el análisis exploratorio de datos (EDA) y desarrollaron modelos predictivos, mientras que los analistas de datos se centraron en la visualización de datos y la respuesta a preguntas clave del negocio.
### Datos:
 Los datos fueron obtenidos de la biblioteca yfinance y abarcan el período desde el 30 de junio de 2014 hasta el 30 de junio de 2024. Los datos incluyen:

Precios de apertura (open)
Precios de cierre (close)
Precios máximos (high)
Precios mínimos (low)
Volumen de negociación (volume)
Datos de seguidores en diversas plataformas
Datasets generados a través de librerías de Python (predictivo y sentimiento)

### Etapas del Proyecto:
 Recolección y Preparación de Datos: Obtención y limpieza de los datos necesarios para el análisis.
 Análisis Exploratorio de Datos (EDA): Identificación de patrones y tendencias clave.
 Modelado Predictivo: Creación de modelos para predecir precios futuros.
 Análisis de Sentimiento: Evaluación del sentimiento de los inversores basado en datos de seguidores.
 Visualización de Resultados: Creación de dashboards interactivos en Power BI.
 
   ### Mockup técnico:
   El mockup técnico se centra en la estructura y funcionalidades de los dashboards creados en Power BI. Incluye gráficos de tendencias de precios, volúmenes de negociación y comparaciones entre mercados. Este mockup proporciona una visión clara y detallada de los principales indicadores financieros de cada mercado.
   ### Mockup sentimiento:
   El mockup de sentimiento presenta el análisis del interés y las emociones de los inversores respecto a las acciones, basado en datos de seguidores de varias plataformas. Se muestran gráficos que ilustran el sentimiento positivo, negativo y neutral a lo largo del tiempo, así como su correlación con las variaciones de los precios de las acciones.
   ### Mockup predictivo:
   El mockup predictivo incluye los resultados de los modelos de machine learning utilizados para prever los precios futuros de las acciones. Se muestran gráficos de predicción comparando los valores reales con los previstos, destacando la precisión de los modelos y los factores que más influyen en las predicciones.

### Visualización en Power BI
 La visualización en Power BI integra todos los análisis anteriores en un dashboard interactivo que permite al usuario explorar los datos de manera intuitiva. Los usuarios pueden filtrar por mercado, acción y período de tiempo para obtener insights específicos. El dashboard también incluye herramientas para comparar tendencias entre diferentes mercados y analizar el impacto de diversos factores en los precios de las acciones.

### Herramientas y librerías utilizadas en el proyecto:


|  Librería/herramienta    |   Logo                                    | Descripción                                                                                                           |
|----------------------|-----------------------------------------|----------------------------------------------|
| **Pandas**   |      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png" width="100">   | Librería de Python para manipulación y análisis de datos.       |
| **NumPy**     |  <img src="https://numpy.org/images/logo.svg" width="50">                      | Librería fundamental para computación numérica en Python.       | 
|**Matplotlib**|<img src="https://matplotlib.org/_static/logo_light.svg" width="100">| Librería fundamental para la generación de gráficos en dos dimensiones.|
|**Yfinance**|<img src="https://cdn6.aptoide.com/imgs/c/2/7/c271bd2b90b62b493e82435882c44846_icon.png?w=128" width="30">| API de Python para datos financieros de Yahoo Finance.|
|**XGBoost**|<img src="https://miro.medium.com/v2/resize:fit:1190/1*yhE3CBwTrlXcAIvNJNTQiA.png" width="100">| Librería de Python para algoritmos de boosting.|
|**Lightgbm**|<img src="https://www.kdnuggets.com/wp-content/uploads/chugh_lgbmclassifier_gettingstarted_guide_1.png" width="50">| Framework de aprendizaje automático basado en árboles.|
|**Statsmodels**|<img src="https://www.statsmodels.org/stable/_images/statsmodels-logo-v2.svg" width="75">| Librería de Python para modelado estadístico.|
|**Scikit-learn**|<img src="https://raw.githubusercontent.com/scikit-learn/scikit-learn/d20e0b9abc4a4798d1fd839db50b19c01723094e/doc/logos/scikit-learn-logo.svg" width="150">| Librería de Python para aprendizaje automático.|
|**Text Blob**|<img src="https://cdn1.technologyevaluation.com/getattachment/c18a3ee5-30fb-5b53-bb73-294d78987b26/logo.png?source=tw2&ext=.png&maxSideSize=192" width="75">| Es una biblioteca de Python (2 y 3) para procesar datos textuales.|
| **Drawdb**| <img src="https://images.opencollective.com/drawdb/5252d15/logo/256.png?height=256" width="65">| Herramienta de diseño de bases de datos para que los desarrolladores creen, colaboren y visualicen sus diagramas de relaciones entre entidades.|
| **Jupyter**|<img src="https://jupyter.org/assets/homepage/main-logo.svg" width="65">| Software gratuito, estándares abiertos y servicios web para informática interactiva en todos los lenguajes de programación.|
| **Visual Studio Code**|<img src="https://static-00.iconduck.com/assets.00/visual-studio-code-icon-512x506-2fdb6ar6.png" width="70">| Editor de código fuente.|
| **MySQL**|<img src="https://static-00.iconduck.com/assets.00/mysqlworkbench-icon-512x506-uen0mqej.png" width="65">| Herramienta visual de diseño de bases de datos que integra desarrollo de software, administración de bases de datos, diseño de bases de datos, gestión y mantenimiento para el sistema de base de datos MySQL.|
| **Colaboratory con Python**|<img src="https://colab.research.google.com/img/colab_favicon_256px.png" width="60">| Utilizaremos Colaboratory, una plataforma de Google basada en Jupyter Notebooks, junto con las potentes librerías de Python para análisis de datos como Pandas, NumPy y Matplotlib.|
| **Power BI**|<img src="https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/Analysts_PBI?resMode=sharp2&op_usm=1.5,0.65,15,0&wid=2000&qlt=99&fmt=png-alpha&fit=constrain" width="100">| Para la visualización de datos avanzada, aprovecharemos Power BI, una herramienta líder en el mercado para crear informes interactivos y paneles de control.|
| **Canva**|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Canva_Logo.svg/250px-Canva_Logo.svg.png" width="100">| Es una plataforma de diseño gráfico y composición de imágenes.|
| **Figma**|<img src="https://static-00.iconduck.com/assets.00/apps-figma-icon-512x512-uapiauws.png" width="65">| Editor de gráficos vectorial y una herramienta de generación de prototipos, principalmente basada en la web.|
| **Power Point**|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Microsoft_PowerPoint_2013-2019_logo.svg/610px-Microsoft_PowerPoint_2013-2019_logo.svg.png" width="100">| Microsoft PowerPoint (PPT) es un software de ofimática diseñado para realizar presentación de diapositivas..|
| **Slack**|<img src="https://toppng.com/uploads/preview/slack-new-logo-icon-11609376883z32jbkf8kg.png" width="45">| Plataforma de comunicación para equipos.|
| **Python**|<img src="https://seeklogo.com/images/P/python-logo-A32636CAA3-seeklogo.com.png" width="50">| Lenguaje de programación utilizado para análisis de datos y desarrollo de aplicaciones.|
| **Google Drive**|<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Google_Drive_icon_%282020%29.svg/1024px-Google_Drive_icon_%282020%29.svg.png?20221103153031" width="50">| Servicio de almacenamiento y sincronización de archivos.|
| **Zoom**|<img src="https://w7.pngwing.com/pngs/805/460/png-transparent-zoom-logo-thumbnail.png" width="70">| Plataforma de videoconferencia de Google.|
| **GitHub**|<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" width="100">| Plataforma de desarrollo colaborativo para proyectos de software.|
| **Trello**|<img src="https://upload.wikimedia.org/wikipedia/en/8/8c/Trello_logo.svg" width="100">| Herramienta de gestión de proyectos y seguimiento de problemas.|


### Contacto:

| Integrantes          |                                     |Rol                                     | GitHub                                        | LinkedIn                                                                           |
|----------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------------|------------------------------------------------------------------------------------|
| Maira Alejandra Pinilla   | <img src="https://github.com/No-Country-simulation/c19-126-t-data-bi/blob/main/files/documentation/presentations/n2--.png" width="100" height="100" style="border-radius: 50%;">      | Project Manager/Data Analyst        | [GitHub](https://github.com/Malejandrapin)  | [LinkedIn](https://www.linkedin.com/in/maira-alejandra-pinilla-pinilla)       |
| Lorena Tito Ramos       | <img src="https://github.com/No-Country-simulation/c19-126-t-data-bi/blob/main/files/documentation/presentations/n1--.png" width="100" height="100" style="border-radius: 50%;">       |Data Analyst                       | [GitHub]()       | [LinkedIn](https://www.linkedin.com/in/lorenatitoramos/)                                 |
| Sergio González Rivera | <img src="https://github.com/No-Country-simulation/c19-126-t-data-bi/blob/main/files/documentation/presentations/n9.png" width="100" height="100" style="border-radius: 50%;">     |Data Analyst / Data Scientist      | [GitHub](https://github.com/gonzalezrivera) | [LinkedIn](https://www.linkedin.com/in/gonzalez-rivera/)   
| Patricia Olivares Delgado |<img src="https://github.com/No-Country-simulation/c19-126-t-data-bi/blob/main/files/documentation/presentations/n3-.png" width="100" height="100" style="border-radius: 50%;">     | Data Analyst / Python - SQL                          | [GitHub](https://github.com/Patricia0livares)  | [LinkedIn](https://www.linkedin.com/in/patricia-olivares-delgado-64496b52/)  
| Sonia Calle   | <img src="https://github.com/No-Country-simulation/c19-126-t-data-bi/blob/main/files/documentation/presentations/n4-.png" width="100" height="100" style="border-radius: 50%;">       |Data Analyst                          | [GitHub](https://github.com/SoniaCalle)  | [LinkedIn](https://www.linkedin.com/in/sonia-calle)  
| Micaela Pequeño   | <img src="https://github.com/No-Country-simulation/c19-126-t-data-bi/blob/main/files/documentation/presentations/n5-.png" width="100" height="100" style="border-radius: 50%;">       |Data Analyst                          | [GitHub](https://github.com/micaelapequeno)  | [LinkedIn](https://www.linkedin.com/in/micaelapequeno/)  
| Yair Fabricio Cuno Rojas   |  <img src="https://github.com/No-Country-simulation/c19-126-t-data-bi/blob/main/files/documentation/presentations/n6-.png" width="100" height="100" style="border-radius: 50%;">      | Data Analyst                          | [GitHub](https://github.com/yairfabricio)  | [LinkedIn](https://www.linkedin.com/in/yair-cuno-rojas/)  |
| Johanna Procopio  |  <img src="https://github.com/No-Country-simulation/c19-126-t-data-bi/blob/main/files/documentation/presentations/n7-.png" width="100" height="100" style="border-radius: 50%;">      | Data Analyst                          | [GitHub](https://github.com/JohannaEP)  | [LinkedIn](https://www.linkedin.com/in/johanna-p-7bb0b0194)   |
| Manuel Lagunas   |<img src="https://github.com/No-Country-simulation/c19-126-t-data-bi/blob/main/files/documentation/presentations/n8-f.png" width="100" height="100" style="border-radius: 50%;">      | Data Analyst / Data Scientist                          | [GitHub](https://github.com/ManuelLagunas)  | [LinkedIn](https://www.linkedin.com/in/manuel-lagunas/)  |


