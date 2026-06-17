# Study-Tracker---TA
## Integrantes
- Catalina Salse
- Belen Blaksley
- Maia Uranga

## Objetivo del proyecto
El objetivo de este proyecto es desarrollar un sistema interactivo en Python que ayude a estudiantes a organizar sus materias, tareas, parciales, entregas, avances y notas.
El programa busca centralizar la información académica del usuario en un solo lugar y, a partir de los datos cargados, generar recomendaciones sobre qué actividades priorizar. La idea principal es que el usuario no solo pueda registrar sus obligaciones académicas, sino también consultar qué tareas son más urgentes, cúales tienen mayor riesgo de atraso y que debería estudiar primero.

## Descripción general del funcionamiento
Study Tracker Inteligente funciona mediante un menú por consola. Desde ese menú, el usuario puede cargar materias, registrar actividades académicas, consultar tareas pendientes, actualizar el avance de una tarea, cargar notas, ver recomendaciones y generar gráficos.

El sistema trabaja con información ingresada por el usuario y la guarda en archivos CSV para poder conservar los datos y volver a consultarlos en un futuro.

A partir de los datos cargados, el programa calcula distintos indicadores, como la prioridad de cada actividad, los días restantes hasta la fecha límite, el riesgo de atraso, el promedio por materia y el estado general de las tareas.

## Principales funcionalidades
- Cargar materias.
- Registrar tareas, parciales o entregas.
- Ingresar fecha límite de cada actividad.
- Indicar dificultad e importancia.
- Registrar porcentaje de avance.
- Marcar actividades como completadas.
- Cargar notas.
- Consultar tareas pendientes.
- Consultar tareas completadas.
- Calcular prioridad de las actividades.
- Detectar actividades próximas a vencer.
- Identificar riesgo de atraso.
- Generar recomendaciones sobre qué estudiar primero.
- Calcular métricas generales.
- Generar gráficos sobre el estado académico del usuario.

## Division de tareas entre integrantes
A COMPLETAR!!!!!

## Fuente de datos
El proyecto no utiliza un dataset externo. La información es ingresada manualmente por el usuario mediante el menú interactivo del programa. Los datos se guardan localmente en archivos CSV dentro de la carpeta `archivos/`.

Archivos utilizados:

- `archivos/materias.csv`: guarda las materias cargadas por el usuario.
- `archivos/tareas.csv`: guarda las actividades académicas registradas.

Cada actividad puede incluir información como:

- Materia.
- Tipo de actividad.
- Descripción.
- Fecha límite.
- Dificultad.
- Importancia.
- Porcentaje de avance.
- Nota.
- Estado.
- Fecha de carga.

## Instrucciones para ejecutar el programa
Puede ejecutarse directamente desde Spyder abriendo el archivo main.py y presionando “Run”.

## Librerias utilizadas
pandas: para leer, guardar y procesar datos en formato tabular.
matplotlib: para generar gráficos.
datetime: para trabajar con fechas, calcular días restantes y detectar actividades próximas.
os: para verificar la existencia de carpetas o archivos.

## Estructura del repositorio
TA/
- main.py
- README.md
- requirements.txt
src/
- materias.py
- tareas.py
- validaciones.py
- archivos.py
- calculos.py
- reportes.py
- graficos.py

archivos/
- materias.csv
- tareas.csv

diagramas/
- diagrama_general.png
    
## Explicación breve de las funciones principales
### main.py
Contiene el menú principal del programa. Desde este archivo se llaman las funciones de los distintos módulos del sistema.

Funciones principales:
mostrar_menu(): muestra las opciones disponibles.
main(): controla el flujo principal del programa.

### src/materias.py
Contiene las funciones relacionadas con la carga y consulta de materias.

Funciones principales:
cargar_materia(): permite ingresar una nueva materia.
mostrar_materias(): muestra las materias cargadas.

### src/tareas.py
Contiene las funciones relacionadas con las actividades académicas.

Funciones principales:
registrar_tarea(): permite cargar una nueva tarea, parcial o entrega.
mostrar_tareas_pendientes(): muestra las actividades que todavía no fueron completadas.
mostrar_tareas_completadas(): muestra las actividades finalizadas.
actualizar_avance(): permite modificar el porcentaje de avance de una actividad.
marcar_tarea_completada(): cambia el estado de una actividad a completada.
cargar_nota(): permite registrar una nota obtenida.

### src/validaciones.py
Contiene funciones para validar los datos ingresados por el usuario.

Funciones principales:
pedir_texto(): solicita texto y verifica que no esté vacío.
pedir_entero(): solicita un número entero válido.
validar_fecha(): verifica que la fecha tenga el formato correcto.
validar_porcentaje(): verifica que el avance esté entre 0 y 100.
validar_nota(): verifica que la nota esté dentro del rango permitido.

### src/archivos.py
Contiene funciones para leer y guardar información en archivos CSV.

Funciones principales:

leer_materias(): lee las materias guardadas.
guardar_materia(): guarda una nueva materia.
leer_tareas(): lee las tareas guardadas.
guardar_tarea(): guarda una nueva tarea.
sobrescribir_tareas(): actualiza el archivo de tareas luego de modificar datos.

### src/calculos.py
Contiene la lógica principal del sistema.

Funciones principales:

calcular_dias_restantes(): calcula cuántos días faltan para la fecha límite.
calcular_prioridad(): asigna una prioridad a cada actividad según fecha, dificultad, importancia y avance.
calcular_riesgo_atraso(): detecta si una actividad tiene riesgo bajo, medio o alto.
calcular_avance_esperado(): estima cuánto debería haber avanzado el usuario según el tiempo disponible.
calcular_promedio_por_materia(): calcula el promedio de notas por materia.
calcular_promedio_general(): calcula el promedio general del usuario.

### src/reportes.py
Contiene funciones para mostrar resultados y recomendaciones.

Funciones principales:

mostrar_alertas_proximas(): muestra actividades que vencen pronto.
mostrar_recomendaciones(): recomienda qué estudiar primero.
mostrar_metricas_generales(): muestra un resumen del estado académico.
mostrar_tareas_por_prioridad(): muestra las actividades ordenadas según prioridad.

### src/graficos.py
Contiene funciones para generar visualizaciones.

Funciones principales:

grafico_tareas_por_materia(): genera un gráfico con la cantidad de tareas por materia.
grafico_estado_tareas(): muestra la proporción de tareas pendientes y completadas.
grafico_prioridades(): muestra la cantidad de actividades según prioridad alta, media o baja.
grafico_promedio_por_materia(): genera un gráfico de promedios.
generar_graficos(): ejecuta la generación de gráficos disponibles.

## Resultados, salidas y métricas generadas
### Salidas por consola
- Listado de materias cargadas.
- Listado de tareas pendientes.
- Listado de tareas completadas.
- Actividades ordenadas por prioridad.
- Alertas de fechas próximas.
- Recomendaciones sobre qué estudiar primero.
- Mensajes de riesgo de atraso.
- Métricas generales.
### Métricas
- Cantidad total de tareas.
- Cantidad de tareas pendientes.
- Cantidad de tareas completadas.
- Porcentaje de actividades completadas.
- Promedio por materia.
- Promedio general.
- Cantidad de tareas por materia.
- Cantidad de actividades con prioridad alta, media y baja.
- Días restantes hasta cada fecha límite.
### Gráficos
- Gráfico de barras con tareas por materia.
- Gráfico circular de tareas completadas y pendientes.
- Gráfico de barras con cantidad de actividades por prioridad.
- Gráfico de barras con promedio por materia.
- Gráfico comparativo entre avance real y avance esperado.

## Diagramas de diseño
El proyecto incluye diagramas de diseño dentro de la carpeta diagramas/.
El diagrama muestra cómo el usuario interactúa con el menú principal y cómo ese menú se conecta con los distintos módulos: materias, tareas, cálculos, reportes, archivos, validaciones y gráficos.

## Declaración de uso de IA
La IA fue utilizada para:
- Ordenar la idea general del proyecto.
- Dividir responsabilidades entre integrantes.
- Sugerir nombres de archivos y funciones.
- Redactar partes del README.
- Resolver dudas puntuales sobre errores o funcionamiento del código.
