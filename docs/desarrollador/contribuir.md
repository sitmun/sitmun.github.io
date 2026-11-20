---
description: "Cómo se organiza el desarrollo de SITMUN 3 y cómo contribuir: repositorio, automatización y requisitos técnicos y metodológicos."
---

# Cómo contribuir

## Gestión

En líneas generales se trata de mantener una gestión ágil, dentro de las limitaciones impuestas por un proyecto de estas características, coordinado entre varias administraciones públicas que a su vez subcontratan la mayor parte de los esfuerzos de desarrollo a distintos adjudicatarios. El equipo de coordinación técnica del proyecto es el punto de contacto ante cualquier duda que surja sobre estas cosas.

## Trabajo en GitHub

Se trabaja en abierto sobre GitHub, bajo el paraguas de la [organización SITMUN](https://github.com/sitmun).

- Los desarrolladores y desarrolladoras tienen que crear cuentas en GitHub y se les darán los permisos necesarios para trabajar en repositorios en esa organización.
- La gestión del trabajo (tareas/incidencias) se hace usando [GitHub Issues](https://docs.github.com/es/issues). En ocasiones se usan [tableros de proyecto de GitHub](https://docs.github.com/es/issues/trying-out-the-new-projects-experience/about-projects), esto depende del subproyecto concreto y se acuerda con los desarrolladores en cada caso. En cualquier caso, los tableros de proyecto solo son una forma distinta de ver las tareas/incidencias de GitHub Issues.
- La construcción y despliegue automáticos se hace usando [GitHub Actions](https://docs.github.com/es/actions).
- Todo cambio entra mediante *pull request*, según [CONTRIBUTING.md](https://github.com/sitmun/sitmun/blob/main/CONTRIBUTING.md):
    - Se crea una rama desde `dev` y se abre la *pull request* contra `dev`.
    - `main` solo recibe las *pull requests* de publicación que vienen de `dev`.
    - Hace falta la revisión de un responsable del código (`tech-com`) y que las comprobaciones de CI (`ci-gate` y las pruebas de base de datos que correspondan) estén en verde.
    - No se admiten *push* directos a `dev` ni a `main`.
- El equipo de coordinación técnica del proyecto tiene que tener acceso a los desarrollos en tiempo real para poder cumplir su papel de coordinación y de validación técnica de los resultados.

## Automatización de procesos

En general haremos siempre énfasis en la automatización de todo lo que sea automatizable en este proyecto.

- En especial, no se puede trabajar en este proyecto sin tener claro que la automatización de pruebas es una buena práctica inexcusable en el desarrollo de software.
- La construcción y despliegue automáticos, al menos en servidores de pruebas y/o preproducción, también serán el requisito por defecto, salvo muy buena razón en contra. Ahora mismo la construcción y pruebas automáticas se hacen en [GitHub Actions](https://docs.github.com/en/actions). Esto puede evolucionar con el tiempo.
- La construcción automática se hace con [Gradle](https://gradle.org) para los componentes Java y con [pnpm](https://pnpm.io) para las aplicaciones Angular e Ionic, desde la raíz del repositorio [sitmun/sitmun](https://github.com/sitmun/sitmun). Las órdenes de construcción, pruebas y comprobaciones están en [CONTRIBUTING.md](https://github.com/sitmun/sitmun/blob/main/CONTRIBUTING.md) y en los flujos de GitHub Actions del repositorio.
- Los secretos (contraseñas o tokens) se gestionan adecuadamente usando [GitHub secrets](https://docs.github.com/es/actions/security-guides/encrypted-secrets). No hay, ni debe haber, ninguna contraseña o token en ninguna parte de ningún repositorio.
- Seguiremos [semantic versioning 2.0.0](https://semver.org) cuando haya que dar identificadores de versión públicos a algo.

## Consideraciones técnicas

El desarrollo de los servicios de backend (backend, proxy y MBTiles) se hace en Java 17, usando [Spring Boot 4.1](https://spring.io/projects/spring-boot).
El desarrollo de las aplicaciones de frontend se hace con TypeScript y [Angular 22](https://angular.dev):
tanto el Administrador como el Visor de mapas están desarrollados en Angular 22,
y las aplicaciones móviles en [Ionic 8](https://ionicframework.com) y [Capacitor 8](https://capacitorjs.com) sobre Angular 22.
Las versiones exactas de todas las herramientas están en el [README](https://github.com/sitmun/sitmun#toolchain) del repositorio.

## Consideraciones metodológicas

Cualquier desarrollo dentro del marco **SITMUN 3** debe cumplir con los siguientes requisitos metodológicos:

- Utilizar una metodología ágil que permita una gestión eficiente del proyecto y una adaptabilidad a los cambios.
- Emplear un conjunto de herramientas que ayuden en las diferentes fases y gestiones del ciclo de desarrollo, facilitando tareas como la planificación, el seguimiento y la colaboración.
- Utilizar git/GitHub para la gestión de versiones, lo que proporciona un control de cambios efectivo y un trabajo colaborativo seguro.
- Aplicar una metodología de pruebas que permita validar automáticamente las funcionalidades desarrolladas, asegurando la estabilidad de la aplicación al introducir nuevas versiones o desarrollos.
- Establecer una metodología para el mantenimiento del sistema, garantizando la correcta gestión de actualizaciones, correcciones de errores y mejoras continuas.
- Realizar una gestión y control eficiente de las funcionalidades incorporadas al sistema, asegurando su correcta implementación y coherencia con los requisitos.
- Realizar auditorías y control de calidad periódicos para asegurar la fiabilidad, seguridad y eficiencia del sistema.
- Utilizar el idioma inglés en el código y los comentarios del mismo, así como en la documentación generada, para facilitar la comprensión y colaboración entre los desarrolladores.

Es importante cumplir con estos requisitos metodológicos para asegurar un desarrollo coherente, eficiente y de alta calidad dentro de **SITMUN 3**.

## Repositorio de GitHub

Desde la versión 1.3.0 todo el código de SITMUN está en un único repositorio,
[sitmun/sitmun](https://github.com/sitmun/sitmun). Cada componente es una carpeta:

| Componente | Carpeta | Tecnología |
| --- | --- | --- |
| Administrador | `sitmun-admin` | Angular 22 |
| Visor de mapas | `sitmun-viewer` | Angular 22, API SITNA |
| App móvil de edición | `sitmun-mobile/sitmun-edition` | Ionic 8, Angular 22, Capacitor 8 |
| App turística | `sitmun-mobile/sitmun-touristic` | Ionic 8, Angular 22, Capacitor 8 |
| Backend | `sitmun-backend` | Spring Boot 4.1, Java 17 |
| Proxy middleware | `sitmun-proxy` | Spring Boot 4.1, Java 17 |
| MBTiles | `sitmun-addons/sitmun-mbtiles` | Spring Boot 4.1, Java 17 |
| Bibliotecas comunes | `sitmun-common` | Java 17 |
| Despliegue con Docker | `compose.yaml`, `docker/`, `profiles/` | Docker Compose |

Los repositorios anteriores (`sitmun-admin-app`, `sitmun-viewer-app`, `sitmun-backend-core`, `sitmun-proxy-middleware`,
`sitmun-application-stack`, `edition-mobile-app`, `administration-mobile-app` y `touristic-mobile-app`) corresponden a la versión 1.2.9 y anteriores.
Las versiones publicadas de los repositorios web y de servicios se conservan en el repositorio único como etiquetas `legacy/<repositorio>/…`.

Las normas de contribución están en [CONTRIBUTING.md](https://github.com/sitmun/sitmun/blob/main/CONTRIBUTING.md).
