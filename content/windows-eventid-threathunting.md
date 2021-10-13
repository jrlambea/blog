Title: Event ID a tener en cuenta en un threathunting Windows
Date: 2021-10-13 16:40
Category: Security
Tags: Windows, EventID, Defense, AD
Slug: eventid-windows-threathunting
Authors: J.R. Lambea
Summary: Este post trata de ser un compendio de eventos de Windows para tener una referéncia de rápida consulta en caso de estar investigando una posible amenaza en estos sistemas.

En este post vamos a hacer un repaso de los que son quizá los eventos de Windows más importantes a tener en cuenta en caso de una investigación ante un posible incidente de seguridad, esta lista no se considera completa, y será ampliada. Las listas de eventos serán agrupadas segúnel tipo de objeto que genera esos eventos.

- Ficheros
- Procesos
- Objetos AD
- Conexiones remotas

## Ficheros

| Event ID | Descripción original | Detalle |
|---|---|---|
|4656|A handle to an object was requested|Solicitud de acceso a un fichero, en este tipo de eventos no aparecen los permisos solicitados ni si el acceso es satisfactorio o no.|
|4663|An attempt was made to access an object| Este objeto aparece entre los eventos de apertura (4656) y cierre de fichero (4658), pueden vincularse mediante el Handle ID. De aquí se pueden extraer diferentes datos del objeto: Nombre del fichero, id de manejador, tipo de permisos solicitados, etc.|
|4658|The handle to an object was closed|Informa de que el fichero se ha cerrado.
|4660|An object was deleted|Este evento aparece cuando se elimina el objeto.|

## Procesos

| Event ID | Descripción original | Detalle |
|---|---|---|
|4688|A new process has been created|Evento que informa que un proceso nuevo ha sido creado|
|4689|A process has exited|Evento que informa que un proceso ha sido cerrado|

## Active Directory

| Event ID | Descripción original | Detalle |
|---|---|---|
|4724|An attempt was made to reset an accounts password|Registra quién y para quién ha realizado un cambio de contraseña.|