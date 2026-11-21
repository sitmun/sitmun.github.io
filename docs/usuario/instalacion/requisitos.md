---
description: "Requisitos para instalar SITMUN 3 con Docker o compilarlo desde el código fuente."
---

# Requisitos

Antes de comenzar, es necesario:

- Una máquina *Windows/Linux/Mac*.
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) instalado, y un conocimiento básico de su uso.
- Acceso a internet para descargar el repositorio [sitmun/sitmun](https://github.com/sitmun/sitmun).

=== "Docker"

    - Memoria suficiente para cinco contenedores: backend y proxy (Java), front, y una o dos bases de datos. La versión 1.3.0
      no publica un mínimo; las imágenes del backend y del proxy usan como máximo el 75 % de la memoria del contenedor.
    - Soporte de virtualización (Hyper-V, KVM, WSL2, etc.).
    - Una versión reciente de [Docker CE](https://docs.docker.com/engine/install/) y [Docker Compose](https://docs.docker.com/compose/install/), o de [Docker Desktop](https://www.docker.com/products/docker-desktop/).
      *Docker CE* es totalmente de código abierto, mientras que *Docker Desktop* es un producto comercial.
    - Un conocimiento básico de Docker y Docker Compose.
    - Acceso a internet para descargar las imágenes de Docker: las de SITMUN (`ghcr.io/sitmun/*`) y las de las bases de datos
      de Docker Hub (`postgres:16-alpine`, `gvenzl/oracle-free:23-slim`).
    - Los puertos 9000 a 9005 de la máquina libres.
    - En Linux y macOS, `openssl`, que usa `setup.sh` para generar los secretos.

    !!! warning "Windows: ejecución de scripts de PowerShell"
        `setup.ps1` es un script de PowerShell, así que es necesario permitir la
        [ejecución de scripts de PowerShell](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies).
        Para hacerlo, se abre una consola de PowerShell con privilegios de administrador y se ejecuta:

        ```shell
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
        ```

=== "Windows"

    - Java 17 SE (LTS) para el backend, el proxy y MBTiles.
    - **Node.js 24** (la versión exacta está en el archivo `.nvmrc` de la raíz del repositorio, actualmente 24.22.0).
      Se descarga desde el sitio oficial: https://nodejs.org/
    - **pnpm** (la versión exacta está en el campo `packageManager` del `package.json` de la raíz, actualmente 12.15.0).
      Se puede activar con `corepack enable` o instalar siguiendo la guía oficial: https://pnpm.io/installation
    - No hace falta instalar Angular CLI de forma global: los scripts de `pnpm` usan la versión del repositorio (Angular 22).
    - Para compilar las aplicaciones móviles, además: JDK 21 y Android SDK 36.
    - Acceso a una base de datos soportada (PostgreSQL u Oracle) para el backend, con una base de datos vacía y su usuario
      ya creados (ver [Instalación](instalacion.md)).
    - Para instalar el backend o el proxy como servicio de Windows: [WinSW](https://github.com/winsw/winsw) 2.12.0 o posterior,
      con .NET Framework 2.0, 4.0 o 4.6.1 (WinSW ofrece un ejecutable para cada uno).
    - Se recomienda usar un proxy inverso delante del backend y del proxy (por ejemplo, IIS Microsoft)
      que envíe las cabeceras `X-Forwarded-Proto`, `X-Forwarded-Host`, `X-Forwarded-Port` y `X-Forwarded-Prefix`
      (ver *Publicar en un servidor web* en [Instalación](instalacion.md)).

=== "Linux/Mac"

    - Java 17 SE (LTS) para el backend, el proxy y MBTiles.
    - **Node.js 24** (la versión exacta está en el archivo `.nvmrc` de la raíz del repositorio, actualmente 24.22.0).
      Se descarga desde el sitio oficial: https://nodejs.org/
    - **pnpm** (la versión exacta está en el campo `packageManager` del `package.json` de la raíz, actualmente 12.15.0).
      Se puede activar con `corepack enable` o instalar siguiendo la guía oficial: https://pnpm.io/installation
    - No hace falta instalar Angular CLI de forma global: los scripts de `pnpm` usan la versión del repositorio (Angular 22).
    - Para compilar las aplicaciones móviles, además: JDK 21 y Android SDK 36.
    - Acceso a una base de datos soportada (PostgreSQL u Oracle) para el backend, con una base de datos vacía y su usuario
      ya creados (ver [Instalación](instalacion.md)).
    - Se recomienda usar un proxy inverso delante del backend y del proxy (por ejemplo, nginx)
      que envíe las cabeceras `X-Forwarded-Proto`, `X-Forwarded-Host`, `X-Forwarded-Port` y `X-Forwarded-Prefix`
      (ver *Publicar en un servidor web* en [Instalación](instalacion.md)).

---

Cumplidos los requisitos, el siguiente paso es la [Instalación](instalacion.md).
