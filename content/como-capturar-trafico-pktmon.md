Title: Cómo capturar tráfico en Windows con pktmon
Date: 2020-05-17 11:10
Category: Tools
Tags: Sniffing, Networking, Windows, Tools
Slug: como-capturar-trafico-pktmon
Authors: J.R. Lambea
Summary: En actualizaciones recientes de Windows se ha introducido una herramienta nueva para la captura de tráfico que muy seguramente substituya el procedimiento anterior del `netsh trace`. En este artículo le damos un vistazo rápido.

<!-- Modified: 2010-12-05 19:30 -->

Revisando Tweeter me encuentro con el siguiente RT de [Nicolas Krassas](https://twitter.com/Dinosn):
<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Windows 10 quietly got a built-in network sniffer, how to use <a href="https://t.co/6iKZYz3IZK">https://t.co/6iKZYz3IZK</a></p>&mdash; Nicolas Krassas (@Dinosn) <a href="https://twitter.com/Dinosn/status/1261792299270496257?ref_src=twsrc%5Etfw">May 16, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
</center>

Comparte una noticia en la que habla de la incorporación silenciosa de una nueva herramienta llamada `pktmon` de captura de tráfico que vendría a substituir `netsh trace`. Además por las pruebas que he podido hacer no sólo está disponible para Windows 10, si no que también para Windows Server 2019 (no así Windows Server 2016).

A continuación los pasos para utilizar esta herramienta.

### Establecer filtros

A diferencia de `netsh trace`, esta nueva herramienta permite el filtrado de la captura de paquetes según diferentes reglas, nos permitiría limitar por ejemplo el puerto (no distingue si de orígen o destino):

```text
pktmon filter add -p 80
pktmon filter add -p 8080
```

Se puede verificat qué filtros se han definido con `pktmon filter list`.

También es posible definir un filtro para capturar sólo la comunicación con una ip en concreto:

```text
pktmon filter add -i 192.168.1.25
```

Así como el protocolo de transporte (TCP, UDP, ICMP, ICMPv6...):

```text
pktmon filter add -t TCP
```

### Definir qué interfaz debe capturar

También es posible definir de qué adaptador de red debe capturar el tráfico, para ver una lista de adaptadores, se debe utilizar `pktmon comp list`. Cómo la salida de este comando es bastante extensa, podemos conseguir sólo la información que nos interesa con la siguiente instrucción Powershell:

```text
> pktmon comp list | Select-string "(^[A-z].*)|(Id:)"
vSwitch External
        Id: 13
        Id: 136
vSwitch Default Switch
        Id: 139
F5 Networks VPN Adapter
    Id: 17
Fortinet SSL VPN Virtual Ethernet Adapter
    Id: 15
Fortinet Virtual Ethernet Adapter (NDIS 6.30)
    Id: 16
PPPoP WAN Adapter
    Id: 14
Bluetooth Device (Personal Area Network)
    Id: 11
TAP-Windows Adapter V9
    Id: 18
```

### Captura

Para capturar, con la configuración actual (una vez establecidos los filtros y sabiendo el Id del adaptador de red), se deberá ejecutar la siguiente instrucción:

```text
pktmon start --etw -p 0 -c 13
```

En caso de que se quisiera capturar de todos los adaptadores sería posible hacerlo con:

```text
pktmon start --etw
```

Una vez se haya producido el evento que necesitamos capturar, o bien si simplemente se quiera parar, se deberá ejecutar:

```text
pktmon stop
```

Esto mostrará un informe de los paquetes tanto _Rx_ cómo _Tx_ de la captura. Por defecto dejará el fichero de la captura con el nombre `PktMon.etl` en el mismo directorio de la ejecución, si se quisiera especificar otro, se deberá añadir el parámetro `-f` tal que:

```text
pktmon start --etw -f c:\temp\captura.etl
```

### Conversión a PCAP

Y la buena noticia es que ya no hará falta tener instalada una versión antigua (la última disponible) de Microsoft Network Monitor 3.4, ya que esta herramienta viene con un conversor propio para pasar de `etl` a `pcap`, lo que permitirá el análisis del tráfico con Wireshark.

**Comentar que esta información no he podido reproducirla en el momento de realizar el post, en la versión que tengo acceso actualmente la opción pcapng no está disponible**

```text
pktmon pcapng c:\temp\captura.etl -i c:\temp\captura.pcap
```