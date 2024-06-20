# Archivo

Mantenemos en esta sección algo de información que, aunque posiblemente está desactualizada y está parcialmente en inglés, aún podría ser valiosa para entender algunas cosas.

## Repositorios y paquetes

Originalmente, algunos componentes se publicaban como paquetes en el registro de GitHub.
Esto complicaba las cosas más de lo necesario sin aportar ventajas evidentes a corto plazo y en la escala de este proyecto y ahora mismo no se está haciendo.
La documentación sobre esto era esta:

> The three libraries that can be imported by different applications are published in the GitHub packages registry:
> `org.sitmun.plugin.core` package, developed in this repository, `@sitmun/frontend-core` package, developed in this repository
> and `@sitmun/frontend-gui` package, developed in this repository. GitHub packages only supports scoped packages in their npm registry.
> SITMUN npm packages must be scoped as `@sitmun`. Even if you are only importing those packages in an application,
> you still need a GitHub personal access token, created for your GitHub user and with at least the `read:packages` scope
> besides read permission on the corresponding GitHub repository.
>
> Every SITMUN repository which library/application publishes, or imports, npm packages from/on the GitHub registry
> includes a `.npmrc` file with its URL, `registry=https://npm.pkg.github.com/sitmun`, to make it more difficult to
> accidentally publish on a different package registry. The package.json of those libraries that intend to publish to
> this registry must include a line such as `"repository": "git://github.com/sitmun/REPOSITORY_NAME.git"`.
> The packages must be public in order to be publishable (e.g., you can add `"private" : "false"` to `packages.json`).
> Be careful because npm install will now try to fetch everything from that registry, so when you want to fetch packages
> from the public npm registry, you may have to write, for instance, `npm install --registry=https://registry.npmjs.org`.

## Scripts de construcción

Esto es anterior al paso a GitHub Actions. Originalmente, se trabajaba con Travis CI.
Pero hay información que posiblemente no está documentada en otros sitios.

> Currently, every plugin/library/application includes in its repository a /build-scripts folder with some Bash shell
> scripts that help to build and deploy them. However, the canonical definition of the build process in each repository
> is in the configuration file for the CI server. The CI server used to be Travis CI, but after changes to their policy
> towards open source projects, we migrated to GitHub Actions. These configuration files are thus currently the GitHub
> Actions workflows in the .github/workflows directory in each repository. These files will generally use `npm` and `ng`
> for the front-end libraries and applications, and gradle for the back-end components. They use `sonarcloud` for static
> code analysis, `compodoc` to create the angular libraries documentation (accessible then in <https://sitmun.github.io/>)
> etc. They also deploy some applications and components (currently to GitHub pages and Heroku) for testing.
>
> The scripts require a number of values that are different for each developer / build environment, and other values
> which are secrets that can't be shared in the repositories. If you want to build locally, those values generally
> must be in environment variables. Depending on the repository and your needs your environment will need to have
> defined:
>
> - `JAVA_HOME`: Make sure it points to a proper installation of the required version of Java.
> - `USERNAME`: Your GitHub user. Required to access to the packages in the GitHub registry, and to publish packages
>   there, with the proper access token (see next point).
> - `GITHUB_API_KEY`: A GitHub personal access token, created for `USERNAME` and with, at least, the required scopes.
>   These scopes are, in a nutshell, `read:packages` to download and install packages from GitHub packages and
>   `write:packages` to upload and publish. Your GitHub user needs also read permissions on the repository to
>   download packages, and write permission to publish them.
> - `SONAR_TOKEN`: A SonarCloud authentication token is required for the sonarqube Gradle task to work on your computer.
>
> The CI build scripts need values for these too. Those are stored as secrets associated to the SITMUN organization in
> GitHub and currently are: `SONAR_TOKEN`, `TOKEN_FOR_WORKFLOWS` (the `GITHUB_API_KEY`), `USERNAME_FOR_WORKFLOWS` (`USERNAME`),
> `HEROKU_TOKEN` and `HEROKU_EMAIL` (currently used for the automatic deployment of the back-end to Heroku for testing purposes).
>
> Regarding the libraries which are published to the GitHub packages registry, they are published only on tagged commits.
> So you can push changes to a library as you like, but if you want that to be published as a package by the CI server,
> you must tag the commit before (see Versioning for more details). Of course, you can run locally the deployment steps
> (see the CI server configuration files) and then it will deploy to the repository whatever you have built locally,
> but again, before doing this read the Versioning page.
>
> **Travis CI**
>
> The SITMUN organization in Travis is kept for now, but we are not using it anymore, because of their new policy
> regarding open source projects. We fulfill every requirement except for one: if there are developers being paid for
> the project, then you can't use Travis CI for free.
>
> **SonarCloud**
>
> Each repository has a `sonar-project.properties` file with the proper configuration to make it possible to analyze its
> code on SonarCloud.
>
> **Programming languages, runtimes and tools**
>
> Some repositories use only Java (e.g. the backend-core), others use only Node.js and others use both.
> For the required versions, again the CI server configuration files should be taken as the canonical ones.
> You also need the Git client.

## Documentación del código

Hubo algunos esfuerzos iniciales de documentación automatizada a partir de comentarios en el código.
Dados los recursos disponibles, y los plazos de tiempo en los que se mueve el proyecto, ahora intentamos documentar
tan solo lo esencial y tratar de mantener eso razonablemente actualizado.

> **Tools used for code documentation**
>
> The documentation is generated automatically from the proper comments and markup in the code every time that a
> `git push` to master is done to the repository. The tools currently used are:
>
> - Compodoc for the Typescript/Angular code.
> - Swagger2markup for the REST API.
> - Javadoc for the Java classes in the server.
