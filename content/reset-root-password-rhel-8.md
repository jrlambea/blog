Title: Recuperar contraseña de root en RHEL8
Date: 2021-01-24 18:51
Category: Troubleshooting
Tags: root, password, RHEL8, local
Slug: cambiar-RHEL8-root-password
Authors: J.R. Lambea
Summary: El procedimiento de emergencia para cambiar la contraseña de root de un equipo RHEL8 ha cambiado desde versiones anteriores, aquí se describe.

Quién no se ha encontrado en la tesitura de tener un sistema Linux y no saber la password de root ,¿cómo se debe hacer para cambiar la contraseña de este sistema? En versiones anteriores se debia editar la lí­nea de grub en la que aparecen los parámetros gen del kernel se carga, se añadí­a `init=/bin/bash`, se ejecutaba la carga con la modificación y voilà! Obtení­amos una shell con root con la que realizar el cambio de password.

La cosa es que recientemente me encontré en esta situación con un servidor RHEL/CentOS8, y este procedimiento no sirvió.

Para Red Hat 8 (y posiblemente versiones posteriores) los pasos son los siguientes:

- Arrancar la máquina con el sistema operativo a recuperar y editar la lí­nea de arranque de `grub`.
- Editar la línea donde aparecen los parámetros de carga del kernel y añadir `rd.break` al final.
- Arrancar desde esta línea modificada y aparecerá al poco un prompt con `root`.
- Montar de nuevo el filesystem `/sysroot` pero con permisos de lectura/escritura. `/sysroot` contiene el filesystem raíz del sistema operativo de carga.

```bash
mount -o remount,rw /sysroot
```

- Una vez montado con los nuevos permisos, se realizará un chroot para ejecutar el cambio de contraseña y que se refleje en el filesystem del sistema operativo local.

```bash
chroot /sysroot
```

- Realizar el cambio de password con `passwd`.
- Una vez realizado el cambio, crear en la raíz del filesystem un fichero `.autorelabel` y salir del `chroot` y sesión (esta acción de `relabeling` afecta en algún aspecto a SELinux, aunque aún no sé concretamente en qué)

```bash
touch /.autorelabel
```

- Una vez desconectado continuarí con el arranque del sistema operativo y una vez finalice el arranque (puede demorarse unos minutos por el `relabeling`) la contraseña de root será la previamente asignada.
