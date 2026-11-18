# Gestión

En líneas generales se trata de mantener una gestión ágil, dentro de las limitaciones impuestas por un proyecto de estas características, coordinado entre varias administraciones públicas que a su vez subcontratan la mayor parte de los esfuerzos de desarrollo a distintos adjudicatarios. El equipo de coordinación técnica del proyecto es el punto de contacto ante cualquier duda que surja sobre estas cosas.

## Trabajo en GitHub

Se trabaja en abierto sobre GitHub, bajo el paraguas de la [organización SITMUN](https://github.com/sitmun).

- Los desarrolladores y desarrolladoras tienen que crear cuentas en GitHub y se les darán los permisos necesarios para trabajar en repositorios en esa organización.
- La gestión del trabajo (tareas/incidencias) se hace usando [GitHub Issues](https://docs.github.com/es/issues). En ocasiones se usan [tableros de proyecto de GitHub](https://docs.github.com/es/issues/trying-out-the-new-projects-experience/about-projects), esto depende del subproyecto concreto y se acuerda con los desarrolladores en cada caso. En cualquier caso, los tableros de proyecto solo son una forma distinta de ver las tareas/incidencias de GitHub Issues.
- La construcción y despliegue automáticos se hace usando [GitHub Actions](https://docs.github.com/es/actions).
- En general, se proporciona acceso directo, en lectura y escritura, a los repositorios necesarios. No hay un equipo de desarrollo principal que haga el grueso del trabajo y luego pequeñas contribuciones puntuales de otros, así que el modelo de forks y pull requests no es, por ahora, adecuado.
- El equipo de coordinación técnica del proyecto tiene que tener acceso a los desarrollos en tiempo real para poder cumplir su papel de coordinación y de validación técnica de los resultados.

## Automatización de procesos

En general haremos siempre énfasis en la automatización de todo lo que sea automatizable en este proyecto.

- En especial, no se puede trabajar en este proyecto sin tener claro que la automatización de pruebas es una buena práctica inexcusable en el desarrollo de software.
- La construcción y despliegue automáticos, al menos en servidores de pruebas y/o preproducción, también serán el requisito por defecto, salvo muy buena razón en contra. Ahora mismo la construcción y pruebas automáticas se hacen en [GitHub Actions](https://docs.github.com/en/actions). Esto puede evolucionar con el tiempo.
- La construcción automática se hace con [Gradle](https://gradle.org) o [NPM](https://www.npmjs.com) según sean proyectos Java o Angular. En general, la mejor documentación sobre los procesos de construcción automática son los scripts de GitHub Actions en cada repositorio. En algunos repositorios hay algunos scripts de Bash en `/build-scripts`. Estos pueden usarse en local, pero de nuevo es importante ver cómo se usan desde los scripts de GitHub Actions, incluyendo qué variables de entorno deben estar configuradas.
- Los secretos (contraseñas o tokens) se gestionan adecuadamente usando [GitHub secrets](https://docs.github.com/es/actions/security-guides/encrypted-secrets). No hay, ni debe haber, ninguna contraseña o token en ninguna parte de ningún repositorio.
- En algunos repositorios se hace uso de [SonarCloud](https://sonarcloud.io) para el análisis estático del código.
- Seguiremos [semantic versioning 2.0.0](https://semver.org) cuando haya que dar identificadores de versión públicos a algo.

## Consideraciones técnicas

El desarrollo de los servicios de backend se hace en Java 17, usando [Spring Boot 3.5.4](https://spring.io/projects/spring-boot).
El desarrollo de las aplicaciones de frontend se hace con TypeScript y [Angular 16.2.12](https://angular.io).
Tanto el Administrador como el Visor de mapas están desarrollados en Angular 16.2.12.

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

## Repositorios de GitHub

A continuación se listan los repositorios de la organización SITMUN junto con una breve descripción de cada uno:

- **[sitmun-viewer-app](https://github.com/sitmun/sitmun-viewer-app)**: Aplicación web para visualizar mapas en la plataforma SITMUN, desarrollada con TypeScript, JavaScript, npm y Angular. [Más información](https://github.com/sitmun/sitmun-viewer-app).
- **[sitmun-admin-app](https://github.com/sitmun/sitmun-admin-app)**: Aplicación de administración para la plataforma SITMUN.
- **[sitmun-backend-core](https://github.com/sitmun/sitmun-backend-core)**: Proporciona la lógica de negocio del backend mediante una API REST. Desarrollado en Java 17 y Spring Boot 3. [Más información](https://github.com/sitmun/sitmun-backend-core).
- **[sitmun-proxy-middleware](https://github.com/sitmun/sitmun-proxy-middleware)**: Proxy a servicios web restringidos y middleware a bases de datos. Desarrollado en Java 17 y Spring Boot 3. [Más información](https://github.com/sitmun/sitmun-proxy-middleware).
- :material-new-box: **[sitmun-application-stack](https://github.com/sitmun/sitmun-application-stack)**: Contiene las configuraciones necesarias para desplegar la plataforma SITMUN utilizando Docker. [Más información](https://github.com/sitmun/sitmun-application-stack).
- :material-new-box: **[administration-mobile-app](https://github.com/sitmun/administration-mobile-app)**: Aplicación móvil para la administración de SITMUN. [Más información](https://github.com/sitmun/administration-mobile-app).
- :material-new-box: **[touristic-mobile-app](https://github.com/sitmun/touristic-mobile-app)**: Aplicación móvil turística desarrollada para SITMUN. [Más información](https://github.com/sitmun/touristic-mobile-app).

Estos repositorios contienen el código y las configuraciones necesarias para los distintos componentes del sistema SITMUN, abarcando tanto el backend como el frontend y las aplicaciones móviles.
