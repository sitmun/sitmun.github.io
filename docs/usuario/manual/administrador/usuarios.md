# Usuarios

En este apartado se definen las características de un usuario con acceso con privilegios.

Con la combinación de los tres elementos, [territorios](territorios.md), [roles](roles.md) y usuarios, se configuran los accesos y permisos a las [aplicaciones](aplicacion.md), [tareas](tareas/index.md) e información del mapa ([capas](capas.md), [capas de fondo](capas-de-fondo.md), etc.).

Para definir un usuario, únicamente hace falta definir un parámetro mínimo:

- **Nombre de usuario**: identificador con el que el usuario accede a la plataforma con los privilegios asignados.
- **Contraseña**: aunque no se indica como obligatoria, no se podrá acceder sin contraseña (el acceso sin contraseña se reserva para el usuario público, disponible por defecto).

Aunque únicamente será requisito el nombre de usuario, hay disponible una variedad de parámetros para detallar características personales, así como para detallar los privilegios otorgados al usuario.

**Información general:**

- Nombre y apellidos
- Correo electrónico
- Usuario administrador de SITMUN
- Cuenta bloqueada

En las otras pestañas se detallan las relaciones de acceso con los otros elementos existentes en la plataforma:

- **Roles por territorio**: definir la relación con los otros componentes que permitirán el acceso a este usuario.
- **Puestos por territorio**: donde se puede definir el cargo y la relación que tenga el usuario con cada territorio al que tenga acceso. Esto permite tener una relación diferente de un mismo usuario con cada territorio.
- **Aplicaciones (punto de contacto)**: lista de solo lectura de las aplicaciones en las que este usuario es el punto de contacto. El correo electrónico institucional del usuario se publica en las aplicaciones cliente. Para cambiar el punto de contacto, edite cada aplicación.
