# Instalación completa: Windows, macOS y Ubuntu

Guía para preparar un equipo desde cero y utilizar **android-kotlin-sdd con Codex o Claude Code**, hasta compilar y ejecutar una primera app Android/Kotlin. Revisión de Android: **18 de septiembre de 2026**; variantes de agentes: **20 de septiembre de 2026**.

Los comandos son instrucciones para tu equipo, no un instalador automático. Se han contrastado con documentación oficial; no se ha ejecutado una instalación limpia en los tres sistemas. Las versiones y los nombres de los menús pueden cambiar.

## Índice

1. [Qué necesitas y qué no](#1-qué-necesitas-y-qué-no)
2. [Windows](#2-windows-powershell)
3. [macOS](#3-macos-terminal-zsh)
4. [Ubuntu](#4-ubuntu-terminal-bash)
5. [SDK y JDK](#5-configurar-el-sdk-y-el-jdk-común)
6. [Codex o Claude Code](#6-instalar-y-abrir-codex-o-claude-code)
7. [GitHub e instalación de la skill](#7-github-e-instalación-de-la-skill)
8. [Primera app y comprobación](#8-crear-o-abrir-la-app-y-comprobar-el-entorno)
9. [Primer ciclo SDD](#9-empezar-el-ciclo-sdd)
10. [Problemas frecuentes](#10-problemas-frecuentes)
11. [Actualizaciones y fuentes](#11-mantenimiento-y-fuentes)

## 1. Qué necesitas y qué no

Ruta de esta guía: **Android Studio + VS Code y tu agente elegido**, todo local y en el mismo sistema operativo. Android Studio administra Android y permite depurar y previsualizar Compose; VS Code es el espacio de trabajo con la extensión de Codex o una terminal de Claude Code. También puedes abrir la misma app desde Codex de escritorio ya instalado. No necesitas los dos agentes.

| Componente | Para qué sirve | Necesidad |
| --- | --- | --- |
| VS Code y Codex o Claude Code | Conversación con el agente, archivos y skill | Elige un agente |
| Cuenta con acceso al agente elegido | Autenticación y uso del servicio | Obligatoria para esta ruta |
| Git y GitHub CLI (`gh`) | Versionado y acceso al repositorio privado | Para descargar por esta ruta y trabajar con GitHub |
| Android Studio | Gestionar SDK, proyecto y dispositivos | Ruta recomendada para preparar Android |
| JDK compatible | Ejecutar Gradle y compilar | Para construir la app |
| SDK, Platform-Tools, Build-Tools | Compilación e instalación Android | Para construir/probar |
| Emulador o teléfono Android | Ejecutar la app | Al menos uno para probarla |
| Python 3.9+ | Instalador de la skill y auditor documental | Opcional si copias la skill manualmente; no es el lenguaje de la app |

No necesitas instalar Kotlin o Gradle globalmente: el proyecto gestiona sus componentes y usa **Gradle Wrapper**. Tampoco necesitas Node.js, Docker, Firebase, una cuenta de Google Play ni un paquete de extensiones Java para seguir esta ruta. Una extensión de Kotlin en VS Code es una ayuda de edición opcional, no sustituye Android Studio ni determina si la app compila.

Para redactar specs puedes empezar sin SDK ni emulador. Para el recorrido completo prepara todo lo anterior. Reserva varias decenas de GB para SDK, imágenes y cachés; es una previsión práctica, no un requisito mínimo oficial.

Comprueba los [requisitos vigentes de Android Studio](https://developer.android.com/studio/install). Esta guía utiliza Windows x64, Ubuntu x86_64 o un Mac compatible con la descarga elegida. La página consultada no ofrece soporte para Studio en Windows/Linux ARM; no apliques esos pasos sin revisar primero la compatibilidad de tu equipo.

Ejecuta **una línea cada vez**, sin copiar el símbolo del prompt ni añadir barras `\` al final. Usa PowerShell en Windows, zsh en macOS y Bash en Ubuntu. No ejecutes `source ~/.bashrc` desde Fish.

## 2. Windows PowerShell

### 2.1 Instalar las aplicaciones

1. Descarga [Git for Windows](https://git-scm.com/install/windows). En el instalador permite usar Git desde la línea de comandos y programas externos.
2. Instala [VS Code para Windows](https://code.visualstudio.com/docs/setup/windows); activa la opción de añadirlo a PATH si aparece.
3. Instala GitHub CLI desde [su página oficial](https://cli.github.com/) con el instalador de Windows.
4. Descarga el instalador de [Android Studio](https://developer.android.com/studio/install), ejecútalo y completa el asistente inicial.
5. Opcional: instala Python desde [python.org](https://www.python.org/downloads/). Abre una nueva terminal y comprueba `python --version` o `py --version`; utiliza el comando que realmente funcione en tu instalación.
6. Cierra y vuelve a abrir PowerShell y VS Code para que reciban el nuevo PATH.

Comprueba:

```powershell
git --version
gh --version
code --version
```

No continúes con la clonación si Git o `gh` no se encuentran. Si `code` no aparece, puedes abrir VS Code desde Inicio y usar **Archivo > Abrir carpeta**.

### 2.2 Virtualización

Para usar el emulador activa VT-x/AMD-V/SVM en BIOS/UEFI si está desactivado. En **Activar o desactivar las características de Windows**, habilita **Plataforma de hipervisor de Windows / Windows Hypervisor Platform** y reinicia. No desactives funciones de seguridad para instalar controladores antiguos; la ruta recomendada es WHPX. [Documentación del emulador](https://developer.android.com/studio/run/emulator-acceleration).

### 2.3 Variables de usuario

Primero completa el [apartado 5](#5-configurar-el-sdk-y-el-jdk-común) y anota las rutas reales. En **Editar las variables de entorno de esta cuenta**, crea:

| Variable | Valor habitual, que debes comprobar |
| --- | --- |
| `ANDROID_HOME` | `C:\Users\TU_USUARIO\AppData\Local\Android\Sdk` |
| `JAVA_HOME` | `C:\Program Files\Android\Android Studio\jbr` |

Edita **Path del usuario**, conservando sus entradas, y añade:

```text
%JAVA_HOME%\bin
%ANDROID_HOME%\platform-tools
%ANDROID_HOME%\emulator
%ANDROID_HOME%\cmdline-tools\latest\bin
```

No incluyas comillas en los valores de la ventana de variables. Si existen entradas Java anteriores, comprueba qué ejecutable tiene prioridad. Evita `setx PATH ...`: puede expandir o dañar el PATH que intentas conservar.

Tras cerrar y abrir la terminal:

```powershell
$env:ANDROID_HOME
$env:JAVA_HOME
Test-Path "$env:JAVA_HOME\bin\java.exe"
Get-Command java
java -version
javac -version
adb version
emulator -accel-check
```

La ruta Windows de la skill será `$HOME\.agents\skills\android-kotlin-sdd`, donde `$HOME` lo proporciona PowerShell. No cambies el valor de esa variable.

**WSL:** esta guía usa Windows nativo. No necesitas WSL para seguirla. Si eliges trabajar en WSL, necesitarás una configuración separada y coherente de herramientas, rutas y conexión al dispositivo; no mezcles el JDK/SDK de Windows con Gradle de Linux. Consulta la [guía oficial de WSL para Codex](https://developers.openai.com/es-419/docs/windows/wsl).

## 3. macOS Terminal zsh

### 3.1 Instalar las aplicaciones

1. En **Acerca de este Mac**, identifica si tienes Apple Silicon o Intel.
2. Para Git, ejecuta `xcode-select --install`, acepta el diálogo y espera a que finalice. Si ya está instalado no es necesario reinstalar. No necesitas descargar Xcode completo para desarrollar Android. [Git en macOS](https://git-scm.com/install/mac).
3. Instala Homebrew desde [brew.sh](https://brew.sh/): puedes usar el instalador `.pkg` enlazado allí. Sigue los pasos finales que proporciona para tu PATH; no copies una ruta Intel en un Mac Apple Silicon. Comprueba `brew --version`.
4. Instala GitHub CLI y, si usarás el auditor, Python:

```zsh
brew install gh
brew install python
git --version
gh --version
python3 --version
```

5. Descarga [VS Code para macOS](https://code.visualstudio.com/docs/setup/mac), colócalo en Aplicaciones y ábrelo. En su paleta de comandos (`Cmd+Shift+P`) ejecuta **Shell Command: Install 'code' command in PATH**.
6. Descarga [Android Studio](https://developer.android.com/studio/install) para tu procesador, arrástralo a Aplicaciones y completa el asistente inicial.

### 3.2 Variables

Completa el [apartado 5](#5-configurar-el-sdk-y-el-jdk-común). Si las rutas coinciden, abre tu configuración con `code ~/.zshrc` y añade este bloque una sola vez, sin borrar el contenido previo:

```zsh
export ANDROID_HOME="$HOME/Library/Android/sdk"
export JAVA_HOME="/Applications/Android Studio.app/Contents/jbr/Contents/Home"
export PATH="$JAVA_HOME/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$ANDROID_HOME/cmdline-tools/latest/bin:$PATH"
```

Guarda y carga la configuración:

```zsh
source ~/.zshrc
test -x "$JAVA_HOME/bin/java"
java -version
javac -version
adb version
emulator -accel-check
```

`test` no imprime nada si funciona; si falla, revisa la ubicación de Studio/JDK antes de continuar. Reabre también VS Code para que herede las variables.

El emulador utiliza el hipervisor integrado de macOS. Elige una imagen ARM64 para Apple Silicon o x86_64 para Intel cuando esté disponible y sea compatible. No instales HAXM. [Aceleración del emulador](https://developer.android.com/studio/run/emulator-acceleration).

## 4. Ubuntu Terminal Bash

### 4.1 Herramientas de base

Usa una versión de Ubuntu Desktop con soporte, en x86_64. En una terminal Bash:

```bash
sudo apt update
sudo apt install git gh python3 curl ca-certificates unzip bubblewrap
git --version
gh --version
python3 --version
```

Si `gh` no tiene candidato en tus repositorios, instala primero el resto de los paquetes omitiendo `gh` y sigue la [instalación APT oficial de GitHub CLI](https://github.com/cli/cli/blob/trunk/docs/install_linux.md); no añadas PPAs desconocidos. `bubblewrap` se incluye para el [entorno restringido de Codex](https://learn.chatgpt.com/docs/sandboxing); no implica conceder al agente acceso sin límites.

Instala [VS Code para Debian/Ubuntu](https://code.visualstudio.com/docs/setup/linux): descarga el `.deb` de tu arquitectura y ábrelo con el instalador de software. Alternativamente, desde la carpeta de descarga usa `sudo apt install ./NOMBRE_REAL_DEL_ARCHIVO.deb`, sustituyendo el nombre por el descargado. Comprueba `code --version`.

### 4.2 Android Studio

Descarga el `.tar.gz` oficial de [Android Studio para Linux](https://developer.android.com/studio/install). Con el gestor de archivos, extrae la carpeta `android-studio` dentro de `~/Aplicaciones` (créala si no existe). No sobrescribas una instalación anterior.

Abre una terminal en `~/Aplicaciones/android-studio/bin`. Ejecuta `./studio` si ese lanzador existe; algunas distribuciones de Studio incluyen `./studio.sh`. Completa el asistente. Para añadirlo al menú de aplicaciones busca **Tools > Create Desktop Entry**.

Si el lanzador comunica bibliotecas ausentes, consulta el apartado de dependencias Linux de la página oficial y los paquetes disponibles para tu Ubuntu. Algunas listas antiguas contienen bibliotecas de 32 bits retiradas: no descargues paquetes de una versión obsoleta de Ubuntu para satisfacerlas sin comprobar compatibilidad.

### 4.3 KVM para el emulador

Para esta ruta con emulador local, instala los componentes de virtualización:

```bash
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients cpu-checker
sudo usermod -aG kvm "$USER"
```

Cierra **la sesión de Ubuntu** y vuelve a entrar para aplicar el grupo. Después:

```bash
id -nG
ls -l /dev/kvm
kvm-ok
```

Tu usuario debe pertenecer a `kvm` y tener acceso a `/dev/kvm`. Si el dispositivo no existe, comprueba virtualización en BIOS/UEFI; dentro de una máquina virtual también depende del host. No uses `chmod 777 /dev/kvm`. [Guía KVM de Ubuntu](https://help.ubuntu.com/community/KVM/Installation).

### 4.4 Variables

Completa el [apartado 5](#5-configurar-el-sdk-y-el-jdk-común). Abre `code ~/.bashrc` y añade, ajustando las rutas si instalaste en otra ubicación:

```bash
export ANDROID_HOME="$HOME/Android/Sdk"
export JAVA_HOME="$HOME/Aplicaciones/android-studio/jbr"
export PATH="$JAVA_HOME/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$ANDROID_HOME/cmdline-tools/latest/bin:$PATH"
```

Guarda y ejecuta en Bash:

```bash
source ~/.bashrc
test -x "$JAVA_HOME/bin/java"
java -version
javac -version
adb version
emulator -accel-check
```

Reabre VS Code. Para una sesión lanzada desde el menú que aún no herede estas variables, abre la carpeta con `code .` desde esta terminal configurada.

## 5. Configurar el SDK y el JDK común

### 5.1 SDK Manager

En Android Studio, abre **More Actions > SDK Manager** desde la bienvenida, o **Tools > SDK Manager** con un proyecto abierto. Anota **Android SDK Location**: es el valor real de `ANDROID_HOME`.

En **SDK Platforms**, instala la plataforma exigida por `compileSdk` de tu proyecto; para una app nueva, la utilizada por la plantilla estable elegida. En **SDK Tools**, instala:

- Android SDK Platform-Tools, que contiene `adb`.
- Android SDK Build-Tools, versión que necesita el proyecto.
- Android SDK Command-line Tools (latest).
- Android Emulator, si usarás un dispositivo virtual.

Aplica los cambios, lee y acepta las licencias necesarias y espera a terminar. Un SDK descargado parcialmente no equivale a un entorno listo. [Gestión oficial del SDK](https://developer.android.com/studio/intro/update#sdk-manager).

No añadas a PATH una carpeta inexistente esperando que eso instale herramientas. Si `cmdline-tools/latest/bin` no existe, revisa la instalación y la ubicación real del paquete.

### 5.2 Java y Gradle

Para un proyecto nuevo generado por la misma versión de Studio, empieza por su JDK incluido (`jbr`), siempre comprobando la compatibilidad. Para proyectos existentes respeta su versión de AGP/Gradle. En **Settings > Build, Execution, Deployment > Build Tools > Gradle**, revisa la JVM utilizada. Proyectos recientes pueden usar `gradle/gradle-daemon-jvm.properties`: sus criterios pueden determinar otra JVM y descargarla.

`JAVA_HOME` ayuda a ejecutar el Wrapper desde la terminal; no garantiza por sí solo la JVM efectiva del daemon. Confirma después con `gradlew --version`. Si necesitas otro JDK, utiliza la opción **Download JDK** de Studio, selecciona una versión compatible y ajusta la ruta de terminal. No cambies AGP, Gradle o el JDK al azar ni fijes Java 17 para todos los proyectos. [Selección del JDK y compatibilidad](https://developer.android.com/build/jdks).

Usa `ANDROID_HOME`; no crees otra ruta diferente en `ANDROID_SDK_ROOT`, que está obsoleta. Si ya existe esta última, revisa que no contradiga el SDK seleccionado. [Variables Android](https://developer.android.com/tools/variables).

### 5.3 Herramientas de línea de comandos: según tu instalación

La ruta principal de esta guía usa la interfaz de Studio, por lo que no depende del nombre de una plantilla de Android CLI.

Si tienes el `sdkmanager` tradicional, consulta `sdkmanager --help`; `sdkmanager --licenses` permite revisar licencias pendientes. Si imprime que está obsoleto y remite a `android sdk`, usa `android --help` y `android sdk --help` de **esa instalación**. No interpretes el aviso de obsolescencia como un fallo si la herramienta termina correctamente.

Si decides crear proyectos por CLI, lista primero las plantillas con la opción que muestre su ayuda. No des por disponible `empty-activity-agp-9`, ni inventes una opción `--profile`. La creación gráfica del apartado 8 evita esos errores.

## 6. Instalar y abrir Codex o Claude Code

### Codex

1. Abre VS Code y su panel **Extensiones**.
2. Desde el enlace **Instala la extensión** de la [página oficial de Codex para IDE](https://developers.openai.com/es-419/docs/codex/ide), instala la extensión publicada por OpenAI. No elijas una extensión de nombre parecido de otro autor.
3. Abre el icono de Codex o busca **Codex: Open Codex Sidebar** en la paleta.
4. Completa el inicio de sesión que ofrece la extensión con una cuenta que tenga acceso. La autenticación de GitHub es independiente. No guardes claves de API en el repositorio.
5. Trabaja sobre una carpeta local de confianza y conserva las restricciones y aprobaciones del agente. No habilites acceso total para resolver un problema de instalación.

**Alternativa de terminal:** si prefieres Codex CLI, sigue el instalador vigente para tu sistema en la [guía oficial de Codex CLI](https://developers.openai.com/es-419/docs/codex/cli), abre la raíz de tu app y ejecuta `codex`. No necesitas instalar la CLI además de la extensión para completar esta guía.

Una extensión instalada no significa que la sesión esté iniciada: comprueba que Codex puede responder a una petición de solo lectura, como «Explica qué archivos hay en esta carpeta sin modificarlos».

### Claude Code

Si eliges Claude Code, sigue [la instalación por sistema operativo](DOS-AGENTES.md#1-instalar-el-agente-elegido): Windows con WinGet, macOS con Homebrew o instalador nativo y Ubuntu con instalador nativo. Incluye autenticación y comprobación del comando. El resto del entorno Android de esta guía es el mismo. No es necesario instalar Codex además.

## 7. GitHub e instalación de la skill

### 7.1 Autenticación y autoría

Estos comandos sirven en los tres sistemas:

```text
gh auth login --hostname github.com --git-protocol https --web
gh auth status
gh auth setup-git
gh repo view luisroga75/android-kotlin-sdd
```

Sigue el inicio de sesión del navegador; no pegues tokens en la conversación. El repositorio es **privado**: debes usar la cuenta propietaria o una invitada con permiso. Si aparece «not found», comprueba la cuenta antes de intentar crear otro repositorio. [Autenticación de GitHub CLI](https://cli.github.com/manual/gh_auth_login).

Antes de hacer commits de tus apps, comprueba `git config --global user.name` y `git config --global user.email`. Si faltan, establece tus propios datos:

```text
git config --global user.name "TU NOMBRE"
git config --global user.email "TU CORREO O DIRECCION NOREPLY DE GITHUB"
```

Son valores de ejemplo que debes sustituir. El correo forma parte de los commits; usa tu dirección noreply si quieres mantenerlo privado. No cambies una identidad existente sin decidirlo.

### 7.2 Instalación personal — una sola copia por agente

Clona en una carpeta de trabajo como `Proyectos`, **no dentro de un directorio de skills**:

```text
gh repo clone luisroga75/android-kotlin-sdd
cd android-kotlin-sdd
```

En Windows, ejecuta `python scripts/install_skill.py --agent codex` o `python scripts/install_skill.py --agent claude-code`, según el agente elegido. Si tu Python se llama `py`, sustituye el comando.

En macOS/Ubuntu, usa `python3 scripts/install_skill.py --agent codex` o `python3 scripts/install_skill.py --agent claude-code`. Puedes añadir `--dry-run` antes para consultar el destino sin escribir.

Codex se instala en `~/.agents/skills/android-kotlin-sdd`; Claude Code en `~/.claude/skills/android-kotlin-sdd`. Si ya utilizas `~/.codex/skills/android-kotlin-sdd`, conserva una sola copia de Codex. El instalador no sobrescribe instalaciones.

Para instalar sin Python, actualizar una instalación antigua o instalar por proyecto, sigue [la guía de los dos agentes](DOS-AGENTES.md). Si la instalación anterior era un clon entero, muévelo fuera del directorio de skills antes de actualizarlo: ahora el repositorio incluye varias entradas.

Abre una sesión nueva en la carpeta de tu **app**, no en la carpeta de la skill. Invoca `$android-kotlin-sdd` en Codex o `/android-kotlin-sdd` en Claude Code y pide confirmar que puede leer las referencias. No redistribuyas el contenido privado a una app pública sin autorización.

## 8. Crear o abrir la app y comprobar el entorno

### 8.1 Proyecto Android

Si ya tienes una app, ábrela en Android Studio y deja que termine la sincronización de Gradle. No generes otra encima.

Para una nueva: **New Project > Phone and Tablet > Empty Activity** (plantilla Compose si está disponible). Define nombre, identificador de paquete propio, carpeta de proyecto y mínimo de Android; selecciona Kotlin cuando exista selector. Deja que Studio genere una combinación compatible y termine de descargar dependencias. No uses como destino la carpeta de esta skill. [Creación oficial de proyectos](https://developer.android.com/studio/projects/create-project).

Ejemplo de carpeta de aplicación: `Proyectos/mi-app` dentro de tu carpeta personal. En VS Code usa **Abrir carpeta** y selecciona la raíz que contiene `settings.gradle.kts` o equivalente, `gradlew` y `gradlew.bat`, no únicamente `app/`.

### 8.2 Emulador o dispositivo

En **Device Manager**, crea un dispositivo de tipo teléfono, elige una imagen compatible con el procesador del equipo y con un nivel de API igual o superior al `minSdk` de la app. Descarga la imagen y arráncalo; espera a ver la pantalla de inicio. Una lista vacía de AVD significa que aún no has creado ninguno. [Dispositivos virtuales](https://developer.android.com/studio/run/managing-avds).

Alternativa: conecta un teléfono Android por USB, activa Opciones de desarrollador y Depuración USB, y acepta la huella del equipo en el teléfono. Windows puede necesitar el controlador del fabricante; Ubuntu puede necesitar reglas udev y pertenencia a `plugdev`, según el dispositivo. La [guía oficial de dispositivos físicos](https://developer.android.com/studio/run/device) incluye la configuración por sistema. Desactiva la depuración cuando no la necesites.

En una terminal configurada:

```text
emulator -list-avds
adb devices
```

Al menos un dispositivo debe aparecer con estado `device`, no `unauthorized` ni `offline`. Si hay varios, selecciona uno explícitamente en Studio para la primera ejecución.

### 8.3 Compilar y ejecutar

Desde la raíz de una **app de confianza**, no desde la skill:

**Windows / PowerShell:**

```powershell
.\gradlew.bat --version
.\gradlew.bat tasks
.\gradlew.bat assembleDebug
.\gradlew.bat testDebugUnitTest
.\gradlew.bat lintDebug
```

**macOS / Ubuntu:**

```sh
./gradlew --version
./gradlew tasks
./gradlew assembleDebug
./gradlew testDebugUnitTest
./gradlew lintDebug
```

Si en macOS/Linux falta el permiso de ejecución, revisa que sea el Wrapper esperado y usa `chmod u+x gradlew` en esa raíz. No ejecutes Gradle con `sudo`.

Los nombres de tareas anteriores son habituales en una app sencilla con variante `debug`; con flavors o módulos distintos, utiliza las tareas que liste tu proyecto. El Wrapper puede descargar Gradle y ejecutar lógica del proyecto: no lo uses sobre código de origen desconocido.

Para instalar y abrir la app, selecciona el dispositivo y pulsa **Run** en Android Studio. Si hay exactamente un destino conectado y existe la tarea, también puedes usar `./gradlew installDebug` o `.\gradlew.bat installDebug`; esto instala, pero no necesariamente abre la actividad. Ábrela desde el dispositivo. Las pruebas instrumentadas, si existen, usan la tarea correspondiente, habitualmente `connectedDebugAndroidTest`.

Ver `BUILD SUCCESSFUL` prueba esa ejecución, no todo el comportamiento de la app. Si no hay tests, una tarea de pruebas puede terminar sin ejecutar ninguno: revisa el informe.

### 8.4 Auditor opcional

Con Python instalado, ejecuta primero las pruebas del auditor (sustituye la ubicación si tu skill está en otro directorio).

**Windows:**

```powershell
python -B "$HOME\.agents\skills\android-kotlin-sdd\scripts\test_audit_sdd.py"
```

Si tu instalación proporciona `py` en lugar de `python`, usa `py` con los mismos argumentos.

**macOS / Ubuntu:**

```sh
python3 -B "$HOME/.agents/skills/android-kotlin-sdd/scripts/test_audit_sdd.py"
```

Se esperan doce pruebas correctas. Para Claude Code, cambia `.agents` por `.claude` en las rutas. Una vez redactados los documentos de tu app, desde la raíz de **esa app**, ejecuta:

```powershell
python "$HOME\.agents\skills\android-kotlin-sdd\scripts\audit_sdd.py" . --ready
```

O en macOS/Ubuntu:

```sh
python3 "$HOME/.agents/skills/android-kotlin-sdd/scripts/audit_sdd.py" . --ready
```

Para Claude añade `--agent claude`; para una app compartida usa `--agent both`. Es normal que una app sin documentos SDD aún no pase el auditor. `--ready` valida estructura documental, no compila ni prueba Android. No hay que instalar dependencias Python con pip.

## 9. Empezar el ciclo SDD

Pega esto en el **chat de Codex** abierto en la raíz de tu app. En Claude Code, sustituye el inicio por `/android-kotlin-sdd` y pide conservar o crear CLAUDE.md con sus imports:

```text
Usa $android-kotlin-sdd para acompañarme desde el estado actual de esta app.
Primero inspecciona el proyecto y el entorno sin modificar nada: sistema,
shell, SDK, JVM efectiva de Gradle, versiones, Git y dispositivos disponibles.
No reinstales herramientas que ya funcionan ni cambies versiones sin explicar
la necesidad. Distingue las comprobaciones realizadas de las pendientes.

Después inicia la entrevista de producto. Pregunta de una en una, propone
opciones con una recomendación y marca los supuestos que debo confirmar.
Genera AGENTS.md, docs/constitution.md y carpetas specs/NNN-funcionalidad/
con spec.md, plan.md y tasks.md. Acuerda conmigo cómo dividir las specs.
Incluye Git/GitHub y pruebas Android adecuadas. En este primer paso quiero
solo diagnóstico y documentación: no implementes ni publiques todavía.
```

Más adelante autoriza explícitamente la implementación y, por separado cuando corresponda, el destino de GitHub. El repositorio de la **app** será distinto del repositorio de la **skill**. Revisa `.gitignore` antes de subir: SDK local, `local.properties`, claves, tokens y archivos de firma no deben terminar en commits.

Lista final de comprobación:

- [ ] El agente inicia sesión y descubre `$android-kotlin-sdd` (Codex) o `/android-kotlin-sdd` (Claude Code).
- [ ] GitHub CLI accede al repositorio privado con la cuenta correcta.
- [ ] Studio y el Wrapper usan JVMs compatibles con el proyecto.
- [ ] `adb` y el SDK apuntan a la instalación elegida.
- [ ] La app compila y abre en un emulador o teléfono.
- [ ] Las pruebas e informes se han revisado, sin confundir ausencia de tests con cobertura.
- [ ] Los documentos SDD se crean dentro de la app y se versionan allí.

## 10. Problemas frecuentes

| Síntoma | Qué revisar primero |
| --- | --- |
| `java`, `git` o `adb` no se encuentran | Reinicia terminal/editor, revisa PATH y que la carpeta exista. No reemplaces todo PATH. |
| Studio compila, pero la terminal falla | Compara `JAVA_HOME`, JVM efectiva del Wrapper, SDK y criterios del daemon. |
| `SDK location not found` | Abre/sincroniza la app en Studio y revisa `ANDROID_HOME` o `local.properties`; este último es local. |
| No existe `sdkmanager` | Instala Command-line Tools con SDK Manager; verifica su carpeta real. |
| `sdkmanager` avisa de sustitución por Android CLI | Consulta la ayuda instalada; la GUI de Studio sigue siendo la ruta de esta guía. |
| `Unknown template name` | No reutilices nombres de otra versión; crea desde Studio o lista plantillas actuales. |
| `emulator -list-avds` no muestra nada | Crea un dispositivo en Device Manager; instalar el emulador no crea un AVD. |
| KVM/WHPX no disponible | Revisa BIOS/UEFI, componente de virtualización, permisos y reinicio/sesión. |
| `adb devices` muestra `unauthorized` | Desbloquea el teléfono y acepta la huella RSA del equipo. |
| No se detecta teléfono por USB | Prueba cable de datos, controlador Windows o reglas udev de Ubuntu. |
| No aparece la skill | Revisa ubicación, `SKILL.md` en el nivel correcto, nueva sesión y duplicados. |
| Repositorio «not found» | Comprueba `gh auth status` y acceso al repositorio privado. |
| Error de sintaxis con `export` o `.bashrc` | Estás usando otro shell; no mezcles Bash/zsh, PowerShell y Fish. |
| Java diferente al esperado | Windows: `Get-Command java -All`; macOS/Ubuntu: `command -v java`; revisa también `gradlew --version`. |

En Fish, utiliza su propia configuración (`~/.config/fish/config.fish`), `set -gx` y `fish_add_path`. Nunca cargues `.bashrc` en Fish. Antes de modificar configuración existente, guarda una copia y comprueba qué líneas causan el problema.

## 11. Mantenimiento y fuentes

Actualiza el clon de trabajo fuera del directorio de skills tras revisar `git status` y `git remote -v`; si está limpio y el origen es el esperado, usa `git pull --ff-only`. Después compara y actualiza la copia instalada, con respaldo. Sigue [la migración de instalaciones antiguas](DOS-AGENTES.md#6-actualizar-sin-perder-personalizaciones); no uses reset forzado ni borres personalizaciones. Una instalación hecha por copia no se actualiza con `git pull`.

Actualiza Studio/SDK desde sus gestores y conserva las versiones declaradas por cada proyecto. No instales automáticamente «lo último de todo» en una app existente. Esta guía no configura firma de publicación ni despliegue en Google Play.

Fuentes oficiales adicionales para comprobar cambios:

- [Claude Code: instalación](https://code.claude.com/docs/en/quickstart), [skills](https://code.claude.com/docs/en/skills) e [imports](https://code.claude.com/docs/en/memory).

- [Codex: extensión para IDE](https://developers.openai.com/es-419/docs/codex/ide), [CLI](https://developers.openai.com/es-419/docs/codex/cli) y [skills](https://developers.openai.com/es-419/docs/build-skills).
- [Android Studio y requisitos](https://developer.android.com/studio/install), [JDK](https://developer.android.com/build/jdks), [variables](https://developer.android.com/tools/variables) y [aceleración](https://developer.android.com/studio/run/emulator-acceleration).
- [VS Code: Windows](https://code.visualstudio.com/docs/setup/windows), [macOS](https://code.visualstudio.com/docs/setup/mac) y [Linux](https://code.visualstudio.com/docs/setup/linux).
- [GitHub CLI](https://cli.github.com/), [Homebrew](https://brew.sh/) y [Python](https://www.python.org/downloads/).
