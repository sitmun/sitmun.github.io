# Requisitos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

- Una máquina *Windows/Linux/Mac*.
- Has instalado [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) en tu máquina.
- Tienes un conocimiento básico de Git.
- Tienes acceso a internet en tu máquina para descargar repositorios de Git.

=== "Docker"

    - Al menos 4 GB de RAM.
    - Soporte de virtualización (Hyper-V, KMV, WSL2, etc).
    - Has instalado la última versión de [Docker CE](https://docs.docker.com/engine/install/) y [Docker Compose](https://docs.docker.com/compose/install/), o [Docker Desktop](https://www.docker.com/products/docker-desktop/).
      *Docker CE* es totalmente de código abierto, mientras que *Docker Desktop* es un producto comercial.
    - Tienes un conocimiento básico de Docker y Docker Compose.
    - Tienes acceso a internet en tu máquina para descargar imágenes de Docker.

=== "Windows"

    - Java 17 SE (LTS).
    - **Node.js**. Puedes descargar **Node.js** desde el sitio oficial: https://nodejs.org/
        - Tanto el **visor de mapas** como el **administrador** requieren **Node.js** con una versión compatible con **Angular 16**,
          que debe ser `>=16.0.0`. 
    - **npm**: Puedes instalar **npm** siguiendo la guía oficial: https://docs.npmjs.com/cli/install
    - **angular cli**: Una vez que hayas cumplido con los prerrequisitos mencionados anteriormente,
      procede a instalar el Cliente Angular de la siguiente manera:
      ```shell
      npm install -g @angular/cli
      ```
    - Entorno de ejecución:  
         - Al menos 1 GB de memoria.
         - Al menos 1 CPU.
         - Acceso a una base de datos soportada (PostgreSQL u Oracle) en el caso de backend.
    - Si se va a instalar en Windows como servicio, se necesita además:
         - [WinSW](https://github.com/winsw/winsw) 2.12.0 o posterior
         - .NET Framework 2.0, 3.1, 4.0 o 4.6.1
    - Se recomienda usar un proxy inverso delante del backend y del proxy (por ejemplo, IIS Microsoft) 
      que sea capaz de proporcionar encabezados HTTP Forward (X-Forward u otros similares).

    !!! warning "No olvides activar la ejecución de scripts de PowerShell"
        Es necesario permitir la [ejecución de scripts de PowerShell](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies). 
        Para hacerlo, abre una consola de PowerShell con privilegios de administrador y ejecuta el siguiente comando:

        ```shell
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
        ```

=== "Linux/Mac"

    - Java 17 SE (LTS).
    - **Node.js**. Puedes descargar **Node.js** desde el sitio oficial: https://nodejs.org/
        - Tanto el **visor de mapas** como el **administrador** requieren **Node.js** con una versión compatible con **Angular 16**,
          que debe ser `>=16.0.0`. 
    - **npm**: Puedes instalar **npm** siguiendo la guía oficial: https://docs.npmjs.com/cli/install
    - **angular cli**: Una vez que hayas cumplido con los prerrequisitos mencionados anteriormente,
      procede a instalar el Cliente Angular de la siguiente manera:
      ```shell
      npm install -g @angular/cli
      ```
    - Entorno de ejecución:  
         - Al menos 1 GB de memoria.
         - Al menos 1 CPU.
         - Acceso a una base de datos soportada (PostgreSQL u Oracle) en el caso de backend.
    - Se recomienda usar un proxy inverso delante del backend y del proxy (por ejemplo, nginx) 
      que sea capaz de proporcionar encabezados HTTP Forward (X-Forward u otros similares).

---

Siguiente paso: [Instalación](instalacion.md)

