# Instalación y uso: Codex y Claude Code

Revisión: 20 de septiembre de 2026. Son dos paquetes independientes con el mismo método SDD Android/Kotlin, no dos agentes que deban ejecutarse simultáneamente. La [guía completa](GUIA-INSTALACION.md) prepara Android Studio, VS Code, JDK, SDK, dispositivos, Git y GitHub en Windows, macOS y Ubuntu. No es una guía para iOS.

## 1. Instalar el agente elegido

### Codex

Instala la extensión oficial de OpenAI en VS Code siguiendo el apartado 6 de la guía completa, inicia sesión y abre una carpeta local de confianza. Si ya utilizas Codex en escritorio o CLI, no necesitas otra interfaz. Las [skills oficiales](https://learn.chatgpt.com/docs/build-skills) usan `~/.agents/skills` (personal) o `.agents/skills` en el proyecto. Algunos entornos existentes usan `~/.codex/skills`: no dupliques la misma skill.

### Claude Code

Necesitas una cuenta y un método de autenticación admitido por Claude Code. El acceso a GitHub y el acceso al agente son independientes; descargar la skill no incluye una suscripción ni créditos. Consulta la [guía oficial de instalación](https://code.claude.com/docs/en/quickstart) antes de ejecutar instaladores.

**Windows, PowerShell:** con Git for Windows instalado como en la guía completa, ejecuta:

```powershell
winget install Anthropic.ClaudeCode
```

**macOS:** si tienes Homebrew:

```sh
brew install --cask claude-code
```

**Ubuntu, o macOS sin Homebrew:** el instalador nativo oficial descarga y ejecuta un script. Úsalo solo tras revisar y confiar en su origen, sin `sudo`:

```sh
curl -fsSL https://claude.ai/install.sh | bash
```

Estos métodos nativos no requieren Node.js. Reabre la terminal, comprueba `claude --version`, entra en la carpeta de tu aplicación y ejecuta `claude` para completar el inicio de sesión. Si el comando no se encuentra, sigue la ruta indicada por el instalador; no reemplaces todo el PATH. No desactives aprobaciones para solucionar la instalación. Windows se describe de forma nativa: no mezcles SDK/JDK de Windows con una sesión WSL.

## 2. Descargar el repositorio privado

El propietario debe invitar a cada alumno y este debe aceptar la invitación. Autentícate con la cuenta invitada; no compartas tokens ni credenciales del profesor.

Desde una carpeta de trabajo, por ejemplo `Proyectos`, **fuera** de `.agents/skills`, `.codex/skills` y `.claude/skills`:

```text
gh auth login --hostname github.com --git-protocol https --web
gh auth status
gh auth setup-git
gh repo clone luisroga75/android-kotlin-sdd
cd android-kotlin-sdd
```

Si el clon ya existe, revisa `git status` y `git remote -v`. Solo si no hay cambios locales y el origen es el esperado, utiliza `git pull --ff-only`. Un error de acceso no se arregla creando otro repositorio.

## 3. Instalar una o ambas skills

### Con el instalador incluido

Python 3.9+ y su biblioteca estándar bastan; no necesitas pip ni dependencias externas. En Windows usa `python` o `py` con los mismos argumentos de los ejemplos. En macOS/Ubuntu, usa `python3`.

Desde el clon, primero puedes consultar el destino:

```sh
python3 scripts/install_skill.py --agent codex --dry-run
python3 scripts/install_skill.py --agent claude-code --dry-run
```

Después ejecuta **solo los que necesites**:

```sh
python3 scripts/install_skill.py --agent codex
python3 scripts/install_skill.py --agent claude-code
```

Para compartirla dentro de una app, en lugar de la instalación personal:

```sh
python3 scripts/install_skill.py --agent codex --scope project --project /ruta/a/mi-app
python3 scripts/install_skill.py --agent claude-code --scope project --project /ruta/a/mi-app
```

En Windows sustituye la ruta, por ejemplo `--project "C:\Proyectos\mi-app"`. El proyecto debe existir. El instalador copia únicamente el paquete elegido: nunca añade un repositorio Git anidado, no modifica documentos de la app y rechaza sobrescribir el destino. Comprueba también ubicaciones personalizadas como `CODEX_HOME`; no intenta adivinar todas las configuraciones del equipo.

### Instalación manual, sin Python

Con el explorador de archivos, copia la carpeta completa `codex/android-kotlin-sdd` a la carpeta personal `.agents/skills/`, o `claude-code/android-kotlin-sdd` a `.claude/skills/`. Crea las carpetas padre si faltan; no copies encima de una instalación existente. En Windows ambas están dentro de tu perfil de usuario; en macOS/Ubuntu, dentro de tu carpeta personal.

El resultado debe contener `skills/android-kotlin-sdd/SKILL.md`, `references/`, `assets/` y `scripts/`. Codex incluye además `agents/openai.yaml`; Claude Code no lo necesita. No añadas otro nivel `android-kotlin-sdd/android-kotlin-sdd` ni copies el repositorio entero.

## 4. Comprobar y empezar

Abre una sesión nueva del agente en la raíz de la **app**, no en el repositorio de la skill. Escribe en su conversación:

**Codex:**

```text
$android-kotlin-sdd Revisa este proyecto Android sin modificar código.
Guíame con preguntas de una en una para definir el producto y preparar
AGENTS.md, la constitución y specs por funcionalidad con plan y tareas.
Quiero revisar cada fase antes de avanzar. Incluye Git/GitHub, pero
no publiques ni implementes todavía.
```

**Claude Code:**

```text
/android-kotlin-sdd Revisa este proyecto Android sin modificar código.
Guíame con preguntas de una en una para definir el producto y preparar
las instrucciones del agente, la constitución y specs por funcionalidad
con plan y tareas. Quiero revisar cada fase antes de avanzar. Incluye
Git/GitHub, pero no publiques ni implementes todavía.
```

Pide al agente que confirme qué archivo de skill ha leído y cuál es la raíz de la app. Si no aparece, comprueba ubicación, nombre, nueva sesión y posibles duplicados. No asumas que instalar la skill instala Kotlin, Android ni el propio agente.

## 5. Mismos documentos, instrucciones nativas

Codex lee `AGENTS.md`. Para una app nueva con Claude Code, la skill propone también `AGENTS.md` como contrato común y un `CLAUDE.md` con esta línea:

```text
@AGENTS.md
```

Claude Code admite [imports en CLAUDE.md](https://code.claude.com/docs/en/memory); no se presupone que lea AGENTS.md automáticamente. En proyectos con instrucciones existentes, se conservan, incluidos los que solo usan CLAUDE.md. Nunca sustituyas un CLAUDE.md existente solo por el import sin revisar su contenido.

Con ambos agentes, constitución, specs, planes, tareas y evidencias son únicos, no copias por agente. Alterna tareas y revisa cambios antes de cambiar de agente; evita que ambos escriban a la vez sobre los mismos archivos. La skill no otorga permisos adicionales ni inventa herramientas de la otra plataforma.

El auditor admite `--agent codex` (predeterminado), `--agent claude` o `--agent both`. Desde el clon, para una app con Claude:

```sh
python3 scripts/audit_sdd.py /ruta/a/mi-app --agent claude --ready
```

Comprueba estructura y el import directo `@AGENTS.md` cuando corresponde; no interpreta toda la memoria del agente ni acredita requisitos Android. Para validar la distribución:

```sh
python3 -B scripts/test_audit_sdd.py
python3 -B -m unittest discover -s tests -v
python3 scripts/sync_packages.py --check
```

## 6. Actualizar sin perder personalizaciones

1. Localiza la instalación activa. Si era un clon completo dentro del directorio de skills, **muévelo fuera de todos esos directorios antes de actualizarlo**. Así no se descubren las nuevas entradas anidadas. Conserva su historial y modificaciones; no lo borres.
2. Conserva una copia de seguridad fuera de los directorios que explora el agente. Renombrar la carpeta dentro de `skills/` puede seguir creando duplicados.
3. Actualiza el clon de trabajo solo tras revisar sus cambios. Compara tus personalizaciones con el paquete nuevo y decide cuáles mantener.
4. Con el destino de instalación libre y el respaldo conservado, usa el instalador o copia únicamente el paquete seleccionado. Para una ubicación compatible `.codex/skills`, usa la copia manual y no crees otra en `.agents/skills`.
5. Abre una nueva sesión, comprueba la invocación y conserva el respaldo hasta validar. Para desinstalar, mueve únicamente la carpeta de esta skill fuera del directorio de skills; no toques la aplicación ni sus documentos.

El instalador no realiza actualizaciones destructivas ni hay un `--force`. Una skill instalada por copia no cambia al hacer `git pull` en el clon: hay que actualizar esa copia conscientemente.

## Límites y fuentes

La documentación de ambas plataformas se ha consultado, y los scripts se prueban en Linux. No se afirma haber realizado una instalación limpia de Windows/macOS ni una sesión completa de Claude Code en cada sistema. El método y las fuentes del curso se conservan en [fuentes.md](references/fuentes.md); no se redistribuye la transcripción.

- [Skills de Codex](https://learn.chatgpt.com/docs/build-skills).
- [Skills de Claude Code y ubicaciones](https://code.claude.com/docs/en/skills).
- [Instalación de Claude Code](https://code.claude.com/docs/en/quickstart).
- [Memoria e imports de Claude Code](https://code.claude.com/docs/en/memory).
