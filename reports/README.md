# Reportes
+ En esta carpeta deben estar los scripts para crear reportes que son entregados a la contraparte, vp, líderes, etc, para su reproducibilidad.
+ En este READM.md se deberá incluir una breve descripción de cada reporte que se realice.
+ Cada script debe empezar con una letra que represente a una familia de reporte
    * r00_script.R -> "r" representa un reporte para la contraparte.
    * r01_script_mensual.Rmd -> la "r" representa script para la contraparte.
    * vp00_script.R -> "vp" representa que es un reporte para nuestro VP.
+ Luego de cada letra, se debe incluir en número empezando con el 00 indicando temporalidad o dependencia.
    * r00_script.R -> "00" representa que para generar el reporte se inicia con este script.
    * r01_script_mensual.Rmd -> "01" representa que hay que ejecutar "r00_script.R" para que este script funcione correctamente.
    * vp00_script.R -> "vp" representa que es un reporte para nuestro VP.
## Descripción
