Title: Función AWS Lambda para arrancar instancias según tag
Date: 2020-06-10 17:20
Category: AWS
Tags: AWS, DevOps
Slug: arrancar-instancias-con-aws-lambda
Authors: J.R. Lambea
Summary: Una de las ventajas del Cloud es poder pagar únicamente por el uso de los recursos. Y una muy buena forma de ahorrar en el uso de los recursos es programar una serie de apagados y arranques automáticos para máquinas que no se están utilizando en un tramo horario en concreto.

<!-- Modified: 2010-12-05 19:30 -->

La solución es sencilla (aunque se puede complicar según se quiera personalizar), en este caso lo que se hará es habilitar un sistema para poder configurar apagados y arranques de máquina automáticos, la única condición es que las horas deberán ser horas en punto.

Para planificar las dos acciones se puede utilizar `CloudWatch Event Rules`, que tiene un planificador con sintaxis similar a `crontab`.

Hay que tener en cuenta que la configuración horaria de CloudWatch és en modo GMT, por lo que para hacerlo funcionar de forma precisa se necesitará hacer conversión horaria entre GMT y CEST (o GMT +1 o +2 según horario de verano/invierno), en este caso se ha optado por poner esta lógica dentro del script Python.

Realizar el apagado sin Python es muy sencillo, ya que directamente desde las `CloudWatch Event Rules` se puede establecer como target una funcion built-in llamada `EC2 StopInstances`, pasando como parámetro, eso sí el ID de la instancia. Esta configuración, aunque funciona, no sería la deseable por que el mantenimiento de estas reglas es completamente manual, además que la forma de ejecución del apagado como del encendido serían diferentes.

`AWS Lambda` puede ser una solución para poder tener una configuración que permita tener un proceso homogeneizado tanto de paradas y arranques, como además de permitir gestionar esta configuración desde los `Tags` de cada instancia en vez de tener que manipular la configuración de CloudWatch constantemente.

Para poder llegar a ese objetivo:

- Se crearán dos etiquetas nuevas por cada instancia a configurar (autostart y autostop).
- Se realizará una función lambda de arranque por cada hora del dia (24 funciones en total) y de lunes a viernes.
- Cada función revisará las etiquetas que contengan la hora de ejecución, es decir:
  - La función de autostart y autostop de las 8:00 AM buscarán todas las máquinas que tengan como valor de las etiquetas `autostart` y `autostop` `8:00`, y en función de en qué propiedad encuentre la hora, realizará una acción u otra.
  - La función de autostart y autostop de las 3:00 PM buscarán todas las máquinas que tengan como valor de las etiquetas `autostart` y `autostop` `15:00` (formato 24h para hacerlo más sencillo) y lo mismo que la anterior, en función de en qué propiedad encuentre la hora, realizará una acción u otra.

### Creación de función Lambda

Se deberá crear una función lambda con un nombre fácilmente identificable (`auto-stop-start` por ejemplo) y un perfil para Lambda en IAM asociado con los siguientes permisos:

- Escribir eventos en CloudWatch
- Describe Instances
- Stop Instances
- Start Instances

El código será tal como el siguiente (modificar la zona horaria por la necesaria):

```python
import boto3
import dateutil.tz
import datetime

ec2 = boto3.resource('ec2')

def stop_instances(instances):
    for instance in instances:
        try:
            ec2.Instance(instance.id).stop()
            print(f'Stopped your instances: {instance}')
        except:
            print(f'Error: Cannot stop {instance}')

def start_instances(instances):
    for instance in instances:
        try:
            ec2.Instance(instance.id).start()
            print(f'Started your instances: {instance}')
        except:
            print(f'Error: Cannot start {instance}')

def lambda_handler(event, context):
    timezone = dateutil.tz.gettz('Europe/Andorra') # Modificar aquí la zona horaria
    current_time = datetime.datetime.now(tz=timezone)
    current_hour = f'{current_time.hour}:00'

    print(f"Starting auto start-stop at {current_hour}")

    autostart_filter = [{
        'Name':'tag:autostart',
        'Values': [current_hour]
    }]

    autostop_filter = [{
        'Name':'tag:autostop',
        'Values': [current_hour]
    }]

    instances_to_stop = ec2.instances.filter(Filters=autostop_filter)
    instances_to_start = ec2.instances.filter(Filters=autostart_filter)

    stop_instances(instances_to_stop)
    start_instances(instances_to_start)
```

### Planificación de los eventos

Por último la periodicidad de ejecución de la `CloudWatch Event Rule` se configurará como sigue: `0 0/1 ? * MON-FRI *`, de esta forma se ejecutará cada hora y de lunes a viernes. Una posible mejora podría ser establecer otro campo con un valor similar a _WeekDays_, _FullWeek_ o _WeekEnd_ para adaptar los horarios de estas máquinas.

¡Y esto es todo! Ahora sólo quedaría añadir las etiquetas a las máquinas para configurar las horas de apagado.