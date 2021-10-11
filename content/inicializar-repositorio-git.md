Title: Inicialización de un repositorio Git
Date: 2020-06-25 02:05
Category: DevOps
Tags: Git
Slug: inicializar-repositorio-git
Authors: J.R. Lambea
Summary: Siempre que tengo que crear un repositorio nuevo y tengo que añadirlo en un servidor tipo GitLab o GitHub me surjen dudas, si te pasa lo mismo entra en este post.

<!-- Modified: 2020-06-25 02:05 -->

Y es que mi memoria es un desastre que me deja vendido en diversas situaciones. Puedo hacer la misma acción decenas de veces que no me acordaré de cómo lo hice (¿alguien dijo `ln -s`?):

<center><blockquote class="twitter-tweet"><p lang="und" dir="ltr"><a href="https://t.co/wEDPT6tPlp">pic.twitter.com/wEDPT6tPlp</a></p>&mdash; Kevin Jones 🏳️‍🌈 (@vcsjones) <a href="https://twitter.com/vcsjones/status/1275227542602100737?ref_src=twsrc%5Etfw">June 23, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script></center>

Ok, pongamos como norma para simplificar las cosas seguir siempre el mismo procedimiento:

### Inicialización

Esta es la parte más fácil y que no se olvida:

- Crear primero el repositorio (`git init`)
- Crear al menos un commit local (`git add -A` y a continuación `git commit -m "First commit"`), si no tienes ningún fichero a hacer commit, puedes crear un `README.md` o un `.gitignore`.
- Crear un repositorio en blanco en algún CVS que funcione con git (GitHub, GitLab, Bitbucket, CodeCommit...)

### Conectar con el CVS

Y esto es lo que se me olvida siempre:

- Establecer el repositorio del servidor CVS como repositorio origen con:
  - `git remote add origin git@${CVS}:${USUARIO}/${REPO_NAME}` si se hace con ssh.
  - `git remote add origin https://${CVS}/${USUARIO}/${REPO_NAME}` si se quiere hacer por https.
- Simular un push o realizar un push para sincronizar ambos repositorios:
  - `git push -u origin master` simula un push.
  - `git push origin master` realiza un push.


### Workflow

A partir de aquí ya es el uso normal de Git. Y ahora que pienso no era tan difícil, ¿verdad? No sé por que presiento que después de escribir este artículo ya no me va a hacer falta ¯\_(ツ)_/¯.


