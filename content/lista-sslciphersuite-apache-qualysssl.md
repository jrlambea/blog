Title: La lista SSLCipherSuite para Apache perfecta para QualysSSL
Date: 2020-05-08 10:20
Category: Hardening
Tags: SSL, CipherSuites, Apache, Web, Security
Slug: lista-sslciphersuite-apache-qualyssl
Authors: J.R. Lambea
Summary: En este artículo se presenta la política de configuración que debe tener un Apache para pasar perfecto el test de SSLCipherSuite de QualysSSL.

<!-- Modified: 2010-12-05 19:30 -->

Esta es la lista perfecta de mecanismos de cifrados para Apache según QualysSSL a fecha de mayo de 2020, cómo se puede ver se excluye la gran mayoría de mecanismos de cifrado y al final quedan, literalmente cuatro:

```text
SSLCipherSuite ALL:!RSA:!CAMELLIA:!aNULL:!eNULL:!LOW:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS:!RC4:!SHA1:!SHA256:!SHA384
```

![Ejemplo](..\img\ab0b272a-73aa-4730-bf34-c5fa081c90e5.png)
