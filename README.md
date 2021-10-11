# Blog

## Notas

Blog personal basado en la tecnología de [Pelican](https://github.com/getpelican/pelican) y la plantilla [Flex](https://github.com/alexandrevicenzi/flex).

## Inicialización

Para hacerlo funcionar en local, se deberán clonar los repositorios de `pelican-themes` (algunos temas como `Flex` están fuera de ese repositorio):

```shell
git clone --depth=1 https://github.com/getpelican/pelican-themes
git clone --depth=1 https://github.com/alexandrevicenzi/Flex ./pelican-themes/Flex
git clone --depth=1 https://github.com/nairobilug/pelican-alchemy/ ./pelican-themes/alchemy
git clone --depth=1 https://github.com/Pelican-Elegant/elegant ./pelican-themes/elegant
git clone --depth=1 https://github.com/gfidente/pelican-svbhack ./pelican-themes/svbhack
git clone --depth=1 https://github.com/petrnohejl/MinimalXY ./pelican-themes/MinimalXY
git clone --depth=1 https://github.com/molivier/nest ./pelican-themes/nest
git clone --depth=1 https://github.com/jvanz/pelican-hyde ./pelican-themes/hyde

```

Instalar requisitos de python:

```shell
pip3 install -r requirements.txt
```