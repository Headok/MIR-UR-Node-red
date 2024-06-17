# MIR-UR-Node-red
Este repositorio contiene todo lo necesario para automatizar la recogida de gavetas desde un punto, y dejarlas en su correspondiente posición en un almacén, mediante el uso de un MIR100 y un UR5.
![imagen](https://github.com/Headok/MIR-UR-Node-red/assets/124361989/60793ad3-2bda-414e-be08-b394ea9562f7)

El MIR y el UR5 se comunican mediante el urcap desarrollado por MIR (no es 100% estable).
## Funcionamiento básico
La información de las distintas posiciones de las gavetas se guarda en un CSV. Al mandar una misión de recogida de gaveta, se leerá el código de barras que lleva la gaveta. Con ese código, usando node-red, se entra en el CSV, y se sacan los datos de posición de la gaveta, así como el punto donde el UR tiene que empezar a hacer el movimiento de dejada.
Todo este procedimiento se lleva a cabo con node-red.
Para no mandar información repetida/errónea, se comprueba que el nº de missión en el MIR haya cambiado (mission_queue_id), así como un registro que nos informa del momento de la misión en el que estamos.
A su vez, para poder colocar una gaveta encima de otra en la misma posición, se lleva un control del número de gavetas apiladas.
También incluye un flujo de trabajo para recoger gavetas vacías en un puesto de trabajo y dejarlas para la recogida de suministradores.
Por último, se ha automatizado en jira que al mover las etiquetas de una columna a otra
Todo esto se encuentra en proceso_codigo_v1_5.json

## Flujos secundarios
Existen otros flujos secundarios para realizar otro tipo de tareas.
1. MIR_v3.1: Flujo para guardar info en influxdb (para posteriormente visualizar con grafana las distintas misiones realizadas, así como el tiempo de ejeción, batería, etc)
2. resta-altura: Flujo para informar de retirada o añadido de gavetas manual.
3. nueva_gaveta_almacen: Flujo para crear nuevas posiciones en el csv.
4. codigo_altura_v1_3: Flujo para comprobar las gavetas con un mismo código apiladas en una posición.

## Instalaciones
*Todo funciona sobre ubuntu 22.04, puede hacerse sobre Windows, pero de cara a futuro, se considera más óptimo Linux.

**Se recomienda trabajar sobre un entorno virtual para la instalación de bibliotecas de python si fuera necesario.
### Node Red
https://nodered.org/docs/getting-started/local
### InfluxDBv2
https://portal.influxdata.com/downloads/
### Grafana
https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/






   

