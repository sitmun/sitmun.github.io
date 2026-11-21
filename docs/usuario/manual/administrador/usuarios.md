---
description: "Usuarios en el administrador de SITMUN 3: datos, usuario administrador, cuenta bloqueada y roles por territorio."
---

# Usuarios

En este apartado se definen las características de un usuario con acceso con privilegios.

Con la combinación de los tres elementos, [territorios](territorios.md), [roles](roles.md) y usuarios, se configuran los accesos y permisos a las [aplicaciones](aplicacion.md), [tareas](tareas/index.md) e información del mapa ([capas](capas.md), [capas de fondo](capas-de-fondo.md), etc.).

Para que un usuario pueda entrar en la plataforma hacen falta estos parámetros:

- **Nombre de usuario**: identificador con el que el usuario accede a la plataforma con los privilegios asignados. El formulario no lo marca como obligatorio y permite guardar sin él, pero sin nombre de usuario no se puede iniciar sesión.
- **Contraseña**: aunque no se indica como obligatoria, no se podrá acceder sin contraseña (el acceso sin contraseña se reserva para el usuario público, disponible por defecto).

Además, hay disponible una variedad de parámetros para detallar características personales, así como para detallar los privilegios otorgados al usuario.

**Información general:**

- Nombre y apellidos
- Correo electrónico
- Usuario administrador de SITMUN
- Cuenta bloqueada

En las otras pestañas se detallan las relaciones de acceso con los otros elementos existentes en la plataforma:

- **Roles por territorio**: definir la relación con los otros componentes que permitirán el acceso a este usuario.
- **Puestos por territorio**: donde se puede definir el cargo y la relación que tenga el usuario con cada territorio al que tenga acceso. Esto permite tener una relación diferente de un mismo usuario con cada territorio. El puesto se crea automáticamente al asignar un rol en un territorio. Sus fechas **Fecha de alta** y **Fecha de baja** limitan el acceso: los roles del usuario en ese territorio solo valen mientras el puesto está vigente, y con un puesto caducado el usuario deja de ver las aplicaciones de ese territorio. Los usuarios `admin` y `public` no tienen puestos y no les afecta.
- **Aplicaciones (punto de contacto)**: solo aparece en un usuario ya guardado. Es una lista de solo lectura de las aplicaciones en las que este usuario es el punto de contacto. El correo electrónico institucional del usuario se publica en las aplicaciones cliente. Para cambiar el punto de contacto, edite cada aplicación.
