Title: Cómo comprobar si un certificado y una clave privada se corresponden
Date: 2020-05-19 11:10
Category: Security
Tags: SSL, RSA, Criptography
Slug: comprobar-si-certificado-y-clave-privada-corresponde
Authors: J.R. Lambea
Summary: Si estás habituado a trabajar con certificados, y si el trabajo no és demasiado organizado puedes encontrarte en un punto en que tienes unas pocas claves privadas otros cuantos certificados, y no sabes qué certificado deriva de qué clave privada. Esto se puede controlar sabiendo el mòdulus de los certificados, és un método muy sencillo que implemento en bash y poershell aquí.

<!-- Modified: 2010-12-05 19:30 -->

Este es un problema que me encontré hace un tiempo: tengo un certificado firmado a partir de un csr generado con alguna clave privada. Y resulta que tengo varias claves privadas candidatas a ser el derivante del certificado. ¿Cómo puedo saber qué clave privada es la correcta para ese certificado público?

Bien, sin entrar demasiado en la teoría matemática de las claves RSA, sabemos que las claves RSA se generan a partir de dos números primos, el siguiente vídeo lo explica muy bien:

<center><iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/4zahvcJ9glg?controls=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

Y por lo que se puede observar, siendo las dos fórmulas de RSA las siguientes:

| Cifrado | Descifrado |
|---|---|
| c=m^e(mod *n*) | m=c^d(mod *n*)|

Si algo tienen en común es el número con el que se realiza el módulo (*n*). Este módulo és público, y se puede extraer tanto de los certificados como de las claves con cualquier librería que gestione certificados, por ejemplo `OpenSSL`.

### Linux y OpenSSL

Para realizar esta operación con OpenSSL (realmente es indistinto de que sea Windows o Linux, sólo que el ejemplo está escrito en Bash), se hará uso del parámetro `-modulus` de los respectivos `x509` (certificado) y `rsa` (clave privada), un ejemplo sencillo de script:

```bash
# Se asignan dos variables con los ficheros cer/crt y key/pem
Public="/etc/certs/hostname.cer"
Private="/etc/certs/a_private.key"

PubMod="$(openssl x509 -modulus -noout -in ${Public} | openssl md5)"
PrivMod="$(openssl rsa -modulus -noout -in ${Private} | openssl md5)"

if [[ $PubMod == $PrivMod ]]; then
    echo -e "The certificate and the key \e[32mMATCH\e[39m."
else
    echo -e "The certificate and the key \e[31mNOT MATCH\e[39m."
fi
```

### Windows y Powershell

Si se ha decidido dividir el procedimiento uno para Linux y otro para Windows, es por que OpenSSL es bastante probable encontrárselo instalado en servidores Linux, pero no es tan frecuente en Windows, sin embargo, esta operación se puede realizar igualmente con Powershell haciendo uso de librerías .Net:

<!--

# http://www.nullskull.com/q/10052940/need-asymmetric--cryptapi-in-c-with-external-certificate-to-be-used-init.aspx
# https://sysadmins.lv/blog-en/digging-into-digital-signatures-part-2.aspx
# https://docs.microsoft.com/en-us/windows/win32/api/wincrypt/nf-wincrypt-cryptdecodeobject

-->
```