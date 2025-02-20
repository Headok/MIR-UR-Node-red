# MIR-UR-Node-red
Este repositorio contiene todo lo necesario para automatizar la recogida de gavetas desde un punto, y dejarlas en su correspondiente posición en un almacén, mediante el uso de un MIR100, un UR5, cámara y una pinza impresa con filamento.
![imagen](https://github.com/Headok/MIR-UR-Node-red/assets/124361989/60793ad3-2bda-414e-be08-b394ea9562f7)

El MIR y el UR5 se comunican mediante el urcap desarrollado por MIR (no es 100% estable, pero se ha superado este problema con distintos bucles en el programa del Ur5).

## Funcionamiento básico
La información de las distintas posiciones de las gavetas se guarda en un CSV (codigos_pos.csv). Al mandar una misión de recogida de gaveta, se leerá el código de barras que lleva la gaveta. Con ese código, usando node-red, se entra en el CSV, y se sacan los datos de posición de la gaveta, así como el punto donde el UR tiene que empezar a hacer el movimiento de dejada.
![imagen](https://github.com/Headok/MIR-UR-Node-red/assets/124361989/9e1daad4-2d21-4ced-a4b0-0001171aad62)

Todo este procedimiento se lleva a cabo con node-red.
![imagen](https://github.com/Headok/MIR-UR-Node-red/assets/124361989/51217ddb-89f7-42c1-ad83-1067bb3612a4)

Para no mandar información repetida/errónea, se comprueba que el nº de missión en el MIR haya cambiado (mission_queue_id), así como un registro que nos informa del momento de la misión en el que estamos.
A su vez, para poder colocar una gaveta encima de otra en la misma posición, se lleva un control del número de gavetas apiladas (alturas.csv).
También incluye un flujo de trabajo para recoger gavetas vacías en un puesto de trabajo y dejarlas para la recogida de suministradores.
Por último, se ha automatizado en jira que al mover las etiquetas de una columna a otra comience la misión de recoger gaveta.
Todo esto se encuentra en proceso_codigo_v1_5.json

## Flujos secundarios
Existen otros flujos secundarios para realizar otro tipo de tareas.
1. MIR_v3.1: Flujo para guardar info en influxdb (para posteriormente visualizar con grafana las distintas misiones realizadas, así como el tiempo de ejeción, batería, etc)
2. resta-altura: Flujo para informar de retirada o añadido de gavetas manual.
3. nueva_gaveta_almacen: Flujo para crear nuevas posiciones en el csv.
4. codigo_altura_v1_3: Flujo para comprobar las gavetas con un mismo código apiladas en una posición.

## Material usado
* UR5e
* MIR100
* Intel Real Sense D435i (para esta fase de proyecto valdría una webcam más sencilla.
* VM Ubuntu 22.04
  
  De cara a futuro,  se espera usar una jetson nano para embarcarla en el mir100 y hacer ahí todo el procesamiento.

## Instalaciones
*Todo funciona sobre ubuntu 22.04, puede hacerse sobre Windows, pero de cara a futuro, se considera más óptimo Linux.
**Se recomienda trabajar sobre un entorno virtual para la instalación de bibliotecas de python si fuera necesario.
### Node Red
https://nodered.org/docs/getting-started/local
### InfluxDBv2
https://portal.influxdata.com/downloads/
### Grafana
https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/

## Script cámara + programa UR + archivo pinza
### Script cámara
Camara01.py
### Programa UR
Programa_UR5_Gavetas.urp
### Archivo pinza
UTIL_GAVETAS_V2.stl
![imagen](https://github.com/Headok/MIR-UR-Node-red/assets/124361989/f483a78e-9340-49ee-9349-e3ebaa02c934)






   

