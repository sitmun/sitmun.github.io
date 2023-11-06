# Requisitos del sistema

El **backend** y el **proxy** necesitan, como mínimo, respectivamente:

- Java 11 SE (LTS).
- 1 GB de memoria.
- 1 CPU.
- Acceso a una base de datos soportada (Postgres u Oracle) en el caso de backend. El soporte de Postgres es estable, 
  mientras que el soporte de Oracle requiere de pruebas adicionales.

Si se va a instalar en Windows como servicio, se necesita además:

- [WinSW](https://github.com/winsw/winsw) 2.12.0 o posterior
- .NET Framework 2.0, 3.1, 4.0 o 4.6.1

Se recomienda usar un proxy inverso delante del backend y del proxy (por ejemplo, nginx en Linux, IIS Microsoft en windows) 
que sea capaz de proporcionar encabezados HTTP Forward (X-Forward u otros similares).

El **visor de mapas** y la **aplicación de administración**, al ser recursos estáticos, se pueden desplegar en cualquier servidor web.

Antes de proceder con la compilación del **visor de mapas** y la **aplicación de administración**, 
asegúrate de tener los siguientes prerrequisitos en tu sistema:

- **Node.js**: El **visor de mapas** requiere **Node.js** con una versión compatible con **Angular 16**,
  que puede ser `^16.14.0 || ^18.10.0`. El **administrador** requiere **Node.js** con una versión compatible con **Angular 10**,
  que puede ser `^12.11.1`. Puedes descargar **Node.js** desde el sitio oficial: https://nodejs.org/
- **npm**: El visor de mapas depende de paquetes gestionados por **npm**. 
  Puedes instalar **npm** siguiendo la guía oficial: https://docs.npmjs.com/cli/install

Una vez que hayas cumplido con los prerrequisitos mencionados anteriormente, 
procede a instalar el Cliente Angular (**Angular CLI**) de la siguiente manera:

```shell
npm install -g @angular/cli
```

!!! warning "No olvides activar la ejecución de scripts de PowerShell en Windows"
    Si estás utilizando un sistema operativo Windows, será necesario permitir la [ejecución de scripts de PowerShell](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies). 
    Para hacerlo, abre una consola de PowerShell con privilegios de administrador y ejecuta el siguiente comando:

    ```shell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

