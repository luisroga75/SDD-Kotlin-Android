# Git y GitHub en el proceso SDD

## Alcance y diagnóstico

Integra versionado cuando el usuario lo solicite o ya exista un flujo acordado. Inspeccionar historial, diff y estado es distinto de subirlo. «Prepara la documentación» no incluye crear un repositorio remoto. «Configura el repositorio y súbelo» sí autoriza esa operación con el destino determinado. Conserva autorizaciones entre turnos; pregunta solo por decisiones que falten o acciones nuevas.

Comprueba raíz Git real, rama actual, cambios staged/unstaged, historial y remotos. Si la carpeta está dentro de otro repo, no añadas archivos al repositorio padre inadvertidamente. Si muestras URLs, oculta credenciales incrustadas. No publiques contenido ni material de otro proyecto.

Con GitHub disponible mediante conector o `gh`, usa la vía operativa. Verifica cuenta y permisos sin imprimir tokens. Si falta autenticación, deja preparados los cambios locales y explica el paso de acceso necesario. No pidas que peguen tokens en el chat.

## Flujo propuesto

Una rama por resultado funcional: `feat/001-recordatorios` es un ejemplo, no un nombre obligatorio. Respeta nombres y rama base existentes. Si no hay convención, propón `main` como base y ramas ligadas a IDs de specs. Comprueba rama remota y divergencia antes de sincronizar; no uses force-push para resolverla.

Versiona constitución, instrucciones del agente (AGENTS y/o CLAUDE con sus imports), specs, plan, tareas, fuentes Kotlin, recursos, tests y Gradle Wrapper, incluido su JAR. Excluye cachés, builds, `local.properties`, datos personales de ejecución y claves de firma. Lee el `.gitignore` existente y fusiona reglas; `.gitignore` no elimina secretos ya rastreados. Si aparecen, detén su publicación y explica la corrección específica.

Commits pequeños y coherentes: contexto/constitución, spec clarificada, plan/tareas, incrementos implementados con sus pruebas y actualización de evidencia. Se pueden agrupar documentos relacionados; no exijas un commit por archivo. Ejemplos opcionales:

```text
docs(sdd): define la spec 001 y sus criterios de aceptación
docs(sdd): planifica la spec 001 y sus tareas
feat(recordatorios): completa T2 para RF-1 y RF-2
fix(recordatorios): evita duplicados conforme a RF-3
test(recordatorios): verifica la cancelación de avisos
```

Antes de un commit revisa `git diff` y `git diff --cached`. Añade rutas explícitas de este encargo; evita `git add .` con cambios ajenos. Si un archivo mezcla cambios del usuario y propios, no los absorbas por comodidad. No deshagas trabajo ajeno, hagas stash automático ni reescribas commits publicados.

Si se solicita PR, enlaza spec, explica comportamiento, requisitos cubiertos, validación real y pendientes. Un borrador es útil si falta revisión; no confundas crear PR con fusionar. No añadas revisores, menciones o cierres automáticos de issues sin que formen parte del encargo. Reglas y comprobaciones del repositorio siguen aplicándose.

## P14. Configurar Git/GitHub

```text
Usa la skill android-kotlin-sdd para preparar el control de versiones de {proyecto}.
Alcance solicitado: {solo local / conectar remoto / crear y publicar repo}.
Inspecciona Git y preserva historia y cambios existentes. No asumas dueño,
URL, rama principal ni visibilidad. Si falta una elección necesaria,
pregunta por ella; para un repo nuevo propón privado, sin darlo por elegido.

Prepara .gitignore Android con reglas proporcionadas. Conserva Gradle
Wrapper y los documentos SDD. Revisa lo que se incluiría y distingue
fuentes de artefactos, rutas locales y credenciales.

Registra en AGENTS.md la política acordada de ramas, commits, validación
y PR; en la constitución solo el principio estable que corresponda.
Si se autoriza Git local, inicializa únicamente la raíz correcta cuando
no exista repositorio y crea el punto inicial coherente. Si falta identidad
Git, consulta la identidad que debo usar sin inventar correo ni cambiar
configuración global. Si ya está configurada, utilízala.

Si la creación/conexión/subida remota está autorizada y el destino resuelto,
hazla y verifica el resultado. Si solo pedí preparación, deja los archivos
listos y describe el estado local/remoto sin publicar. No solicites de
nuevo permiso para una acción ya incluida en mi petición.
```

## P15. Versionar una spec y su implementación

```text
Versiona los cambios de {carpeta-spec} y su implementación conforme al flujo
Git del proyecto. Identifica rama base y estado real antes de crear/reutilizar
la rama de la feature. Conserva modificaciones no relacionadas.

Revisa consistencia spec → plan → tareas → código/tests y la evidencia
correspondiente. Forma commits coherentes con rutas explícitas y mensajes
que permitan identificar spec y tareas. No marques tareas verificadas por
el simple hecho de hacer commit. Guarda SHA y estado de trabajo al terminar.

Si he pedido push, verifica destino y divergencia y sube la rama concreta.
Si he pedido PR, crea/actualiza la PR con problema, comportamiento, enlace
a documentos, pruebas ejecutadas y pendientes. Si pedí solo commits locales,
termina en ellos. No fusiones por el mero hecho de que CI esté verde.
```

## P16. Preparar CI Android en GitHub Actions

```text
Prepara o ajusta CI para este proyecto Android usando sus módulos,
variantes, JDK y SDK reales. Reutiliza workflows existentes y evita trabajos
duplicados. Consulta documentación vigente y versiones verificadas de las
acciones; no inventes etiquetas o SHA.

El flujo debe obtener el repo, configurar JDK/Android SDK necesarios y
usar Gradle Wrapper para los unitarios, lint y compilación pertinentes.
Instala explícitamente paquetes SDK requeridos si el runner no los ofrece.
No asumas que el runner puede acceder a dependencias privadas ni que las
licencias ya están aceptadas. Sigue el mecanismo de licencias autorizado.

Usa permisos mínimos adecuados, normalmente contents: read para verificación.
Para contribuciones externas no ejecutes código de PR con secretos mediante
pull_request_target. No incluyas firma release ni despliegue por defecto.
Si pruebas instrumentadas son necesarias, define un trabajo de emulador
compatible o deja claramente documentada la verificación manual pendiente;
no las declares cubiertas por los tests JVM.

Guarda reportes apropiados con retención razonable cuando sean útiles.
Un workflow preparado no es un workflow ejecutado. Si tengo autorizado
subirlo, verifica la ejecución para el commit correcto y reporta su estado.
Si no, informa de que queda pendiente su primera ejecución en GitHub.
```

## P17. Cerrar y versionar una entrega

```text
Prepara el cierre de {spec o entrega}. Contrasta aceptación, tareas,
evidencia local, estado de PR y CI para el último commit. Señala cualquier
validación obsoleta tras cambios nuevos.

Si solicité merge, comprueba aprobaciones, checks y ausencia de conflictos,
y usa el método permitido por el repo. No evites protecciones. Si no lo
solicité, entrega el estado y los enlaces sin fusionar.

Si solicité una versión, distingue versionName/versionCode Android de tag
Git y release GitHub. Obtén la convención y último valor; propone el siguiente
sin reutilizar un versionCode publicado. Identifica commit y artefactos.
Un tag o release no equivale a publicación en Google Play, que requiere
un encargo distinto. No borres ramas ni reescribas historial como rutina.
```

## Referencias

- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [Gradle en GitHub Actions](https://docs.github.com/en/actions/tutorials/build-and-test-code/java-with-gradle)
- [Área de preparación de Git](https://git-scm.com/docs/git-add)

Estas capacidades amplían el curso para este usuario; no se atribuyen al vídeo.
