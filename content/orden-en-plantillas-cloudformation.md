Title: Orden en plantillas Cloudformation
Date: 2020-05-13 13:19
Category: Cloud
Tags: CloudFormation, IaC, AWS
Slug: orden-en-plantillas-cloudformation
Authors: J.R. Lambea
Summary: Tengo que reconocer que esta parte de infraestructura se me hace cuesta arriba. En esta entrada describo un par de consejos que me han sido útiles para realizar mis plantillas.
Modified: 2010-12-05 19:30

Realizar plantillas de CloudFormation no es sencillo, no al menos para mi. Por eso, y a modo de nota para mi yo del futuro (y para el que le sea útil), aquí van unos cuantos consejos para realizar plantillas con CloudFormation.

### Utiliza YAML

Las plantillas se pueden escribir tanto en YAML como en JSON, pero definitivamente YAML es mucho más sencillo tanto a la hora de redactar cómo en el momento de leer.

### Utiliza múltiples plantillas y ordena la creación de elementos

Leer y mantener una plantilla con todos los elementos de una infraestructura, por pequeña que sea se hace un infierno. Es preferible crear múltiples plantillas y enlazarlas con los `outputs` que generen cada una.

Además, el orden puede ser importante para no dejarse nada, y que en el momento de lectura o revisión uno no se vuelva loco saltando de `Auto-Scaling Groups` a `Subnets` pasando por `Security Groups` desde `Launch Templates` saliendo por `Nat Gateways`.

Por ejemplo, se pueden crear las siguientes plantillas y por este orden:

- Networking
    - VPC e Internet Gateway
    - NAT Gateway y Subnets
    - Routing
- Permissions
    - Políticas y roles de IAM
- Computing
    - Security Groups
    - Auto-Scaling Groups
    - Launch Configurations
    - Target Groups
    - Load Balancer
- Others
    - Lo que reste (CloudFront, WAF, Route53, etc.)

### Ve paso a paso

Tanto si es una infraestructura compleja como si no, te recomiendo que vayas componente por componente, siguiendo el orden anterior. Primero configurar el VPC, si se despliega bien, segui con Internet Gateways, Subnets... etc.

Intentar tener todos los elementos de la infraestructura y que desplieguen a la primera es una locura, no sólo por que es harto improbable que eso tenga un resultado satisfactório, si no que además en caso de error depurar una plantilla de cierto tamaño es terrible.

¡Asegúrate un paso antes de dar el siguiente!