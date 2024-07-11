# Preprocessing

+ En esta carpeta deben estar los scripts para crear el tablón para modelar.
+ En este READM.md se deberá incluir una breve descripción de cada scripts
+ Cada script debe empezar con una letra que represente a una familia de reporte
    * p00_prepro.R 
    * p01_prepro_test_train.R contraparte.
    * n00_prepro_mensual.R 
    * **Explicación:** "p" representa una familia de script para crear un tablón específico, distinto al tablon de los script de la familia "n"
+ Luego de cada letra, se debe incluir en número empezando con el 00 indicando temporalidad o dependencia.
    * p00_prepro.R -> "00" representa que se debe empezar con este script para el tablon "p"
    * p01_prepro_test_train.R -> "01" representa que es segunda script que se debe ejecutar de la familia "p"
    * n00_prepro_mensual.R  -> "00" representa que se debe empezar con este script para el tablón "n"
## Descripción
