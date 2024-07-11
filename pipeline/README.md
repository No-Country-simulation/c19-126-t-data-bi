# Pipeline

+ En esta carpeta se guardan los script para ejecutar en secuencia todos los scripts para entrenar el modelo o para predecir.
+ En este README.md se debe detallar la secuencias de los scripts ha ejecutar, descripcion y parametros.

## Descripción

**NOTA**: Lo siguiente es solo un ejemplo, las estructura puede ser distinta segun necesidad de cada proyecto, borrar el ejemplo al iniciar el proyecto.


# Proyecto X

## Fuente de Informacion

* Link al catalogo de tablas.

## Parámetros

* Fecha de Inicio: <descripción>
* Numero de Arboles: <descripción>

## Paso 01


**Archivo**
```
./models/m00_model.py
```

**Descripcion:**
* Script para crear un random forest

**Parametros**
* Fecha de Inicio
* Numero de Arboles


**Chunks:**
* Read tablón
* Aplicar randomforest
* Grabar modelo

## Paso 02

.
.
.