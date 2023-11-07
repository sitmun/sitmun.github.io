# ¿Qué es SITMUN 3?

**SITMUN 3** es una plataforma que permite la creación y gestión de aplicaciones personalizadas en el ámbito de los [Sistemas de Información Geográfica](https://es.wikipedia.org/wiki/Sistema_de_informaci%C3%B3n_geogr%C3%A1fica) (SIG).
Está diseñada específicamente para satisfacer las necesidades de información territorial de las administraciones locales y supramunicipales.

**SITMUN 3** ha sido desarrollado con la visión de proporcionar una herramienta de gestión de información territorial a los municipios, gestionada desde una entidad supramunicipal.
Permite la integración de la información territorial con los datos de las corporaciones locales, independientemente del modelo de datos o del sistema de gestión de base de datos utilizado por cada municipio.
Es importante destacar que **SITMUN 3** agrega una capa de autenticación al acceso a los servicios cuando sea necesario, especialmente en consultas y siempre en los casos de gestión de información.
Esta medida contribuye a la seguridad y privacidad de los datos, asegurando que solo usuarios autorizados puedan acceder y gestionar la información territorial

**SITMUN 3** se presenta al usuario en forma de aplicaciones accesibles a través de **visores de mapas**, que se pueden configurar para que se adapten a las necesidades de cada municipio.

**SITMUN 3** tiene una **aplicación de administración** que configura la información cartográfica, el territorio y las tareas que cada usuario tiene acceso para cada aplicación.
Estas tareas ofrecen una amplia gama de funcionalidades, como consultas a bases de datos, generación de informes, buscadores, funciones de análisis espacial, entre otras.

**SITMUN 3** dispone de una base de datos para administrar la plataforma.
El modelo de datos permite la definición de información cartográfica, territorios, aplicaciones, tareas, usuarios, roles y permisos de acceso.

**SITMUN 3** se basa en la utilización de servicios web estándar definidos por el **[Open Geospatial Consortium](https://www.ogc.org/)** (OGC).

Todos los mensajes que se muestran en las aplicaciones de **SITMUN 3** están parametrizados en un archivo de recursos disponible en varios idiomas.

**SITMUN 3** tiene una arquitectura de 3 niveles:

- **Nivel de datos**: Puede estar en cualquier base de datos relacional, aunque actualmente se utilizan **Oracle** y **PostgreSQL**.
  El modelo de datos está documentado en [la organización de SITMUN en GitHub](https://github.com/sitmun).
- **Nivel de lógica de negocio**: Desarrollado en Java con [Spring Boot](https://spring.io/projects/spring-boot),
  tiene un modelo de entidades de [Spring Data](https://spring.io/projects/spring-data) que refleja el esquema de la base de datos.
  El acceso a la lógica de negocio de los **visores de mapas** se realiza a través de la **[API de Configuración y Autorización][api-de-configuracion-y-autorizacion]** y de la **[API de Proxy][api-de-proxy]**.
  El acceso a la lógica de negocio de la **aplicación de administración** se realiza a través de la **[API de Administración][api-de-administracion]**.
  En ambos casos, los usuarios se autentican mediante la **[API de Autenticación][api-de-autenticacion]**.
- **Nivel cliente**: Actualmente, existen una **[aplicación de administración](https://github.com/sitmun/sitmun-admin-app)** para los administradores
  y un **[visor de mapas](https://github.com/sitmun/sitmun-viewer-app)** basado en la [API SITNA](https://github.com/sitna/api-sitna)
  que es utilizado por los diferentes tipos de usuarios finales, tanto al público en general como a especialistas de los ayuntamientos, entre otros.
