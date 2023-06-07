# Gestión

En líneas generales se trata de mantener una gestión ágil, dentro de las limitaciones impuestas por un proyecto de estas características, coordinado entre varias administraciones públicas que a su vez subcontratan la mayor parte de los esfuerzos de desarrollo a distintos adjudicatarios. El equipo de coordinación técnica del proyecto es el punto de contacto ante cualquier duda que surja sobre estas cosas.

## Trabajo en GitHub

Se trabaja "en abierto" sobre GitHub, bajo el paraguas de la [organización SITMUN](https://github.com/sitmun).

- Los desarrolladores y desarrolladoras tienen que crear cuentas en GitHub y se les darán los permisos necesarios para trabajar en repositorios en esa organización.
- La gestión del trabajo (tareas/incidencias) se hace usando GitHub Issues. En ocasiones se usan tableros de proyecto de GitHub; esto depende del subproyecto concreto y se acuerda con los desarrolladores en cada caso. En cualquier caso los tableros de proyecto solo son una forma distinta de ver las tareas/incidencias de GitHub issues.
- La construcción y despliegue automáticos se hace usando GitHub Actions.
- En general se proporciona acceso directo, en lectura y escritura, a los repositorios necesarios. No hay un equipo de desarrollo principal que haga el grueso del trabajo y luego pequeñas contribuciones puntuales de otros, así que el modelo de forks y pull requests no es, por ahora, adecuado.
- El equipo de coordinación técnica del proyecto tiene que tener acceso a los desarrollos en tiempo real para poder cumplir su papel de coordinación y de validación técnica de los resultados.

## Automatización de procesos

En general haremos siempre énfasis en la automatización de todo lo que sea automatizable en este proyecto.

- En especial, no se puede trabajar en este proyecto sin tener claro que la automatización de pruebas es una buena práctica inexcusable en el desarrollo de software. 
- La construcción y despliegue automáticos, al menos en servidores de pruebas y/o preproducción, también serán el requisito por defecto, salvo muy buena razón en contra. Ahora mismo la construcción y pruebas automáticas se hacen en GitHub Actions, y el proyecto hace las pruebas de preproducción en Heroku. Esto puede evolucionar con el tiempo.
- La construcción automática se hace con Gradle o NPM según sean proyectos Java o Angular. En general la mejor documentación sobre los procesos de construcción automática son los scripts de GitHub Actions en cada repositorio. En algunos repositorios hay algunos scripts de Bash en `/build-scripts`. Estos pueden usarse en local, pero de nuevo es importante ver cómo se usan desde los scripts de GitHub Actions, incluyendo qué variables de entorno deben estar configuradas.
- Los secretos (contraseñas o tokens) se gestionan adecuadamente usando GitHub secrets. No hay, ni debe haber, ninguna contraseña o token en ninguna parte de ningún repositorio.
- En algunos repositorios se hace uso de SonarCloud para el análisis estático del código.
- Seguiremos [semantic versioning 2.0.0](https://semver.org) cuando haya que dar identificadores de versión públicos a algo.

## Consideraciones técnicas

El desarrollo de los servicios de backend se hace en Java 11, usando Spring Boot 2.4.3. 
El desarrollo de las aplicaciones de frontend se hace en Angular 16.0.0. 
En general se usan las últimas versiones de las dependencias, 
pero hay alguna excepción como el Administrador, que está desarrollado en Angular 10.1.6.
