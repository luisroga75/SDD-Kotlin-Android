# SDD Android con Kotlin para Codex

Skill en español para acompañar el desarrollo de una app Android desde una idea hasta especificaciones, diseño, tareas, implementación y validación. Incluye un flujo de control de versiones con Git y GitHub.

La entrevista propone opciones razonadas, hace preguntas de una en una y distingue decisiones confirmadas de supuestos. Puede utilizarse con una app nueva o con un proyecto ya existente.

## Qué incluye

- **18 prompts** adaptables: descubrimiento, constitución, instrucciones del agente, varias specs, especificación, revisión QA, clarificación, plan, tareas, auditoría, implementación, validación, cambios, reanudación, Git/GitHub, commits/PR, CI y entregas.
- **Seis plantillas** para AGENTS.md, constitución, spec, plan, tareas y mapa global opcional.
- Orientación específica de Kotlin, Compose, Gradle, datos, permisos, segundo plano y pruebas Android.
- Un comprobador documental de solo lectura y nueve pruebas de su comportamiento.

## Instalación

Repositorio: [luisroga75/android-kotlin-sdd](https://github.com/luisroga75/android-kotlin-sdd). Es privado: necesitas una cuenta con acceso. Con GitHub CLI autenticado puedes descargarlo mediante:

```sh
gh repo clone luisroga75/android-kotlin-sdd
```

1. Descarga o clona el repositorio que contiene esta skill.
2. Copia la carpeta **completa** `android-kotlin-sdd`, incluidos `references`, `assets`, `agents` y `scripts`, en el directorio de skills reconocido por tu instalación de Codex.
3. Abre Codex en el proyecto Android y escribe `$android-kotlin-sdd`. Si no se descubre, inicia una nueva sesión.

La documentación actual de Codex contempla `~/.agents/skills` para skills personales y `.agents/skills` en el repositorio para compartirlas con el equipo. Algunos entornos, incluido el usado para desarrollar esta skill, descubren `$CODEX_HOME/skills`, normalmente `~/.codex/skills`. Usa una sola instalación canónica para evitar mantener copias divergentes.

Ejemplo si estás en el directorio que contiene la carpeta descargada y tu Codex utiliza `~/.agents/skills`:

```sh
mkdir -p ~/.agents/skills
mkdir -p ~/.agents/skills/android-kotlin-sdd
cp -R ./android-kotlin-sdd/SKILL.md ./android-kotlin-sdd/README.md ./android-kotlin-sdd/agents ./android-kotlin-sdd/assets ./android-kotlin-sdd/references ./android-kotlin-sdd/scripts ~/.agents/skills/android-kotlin-sdd/
```

Si ya existe una instalación, revisa las diferencias antes de sustituirla. No copies únicamente `SKILL.md`: sus referencias y plantillas son parte del funcionamiento.

Consulta las [ubicaciones oficiales de skills de Codex](https://developers.openai.com/es-419/docs/build-skills).

## Requisitos

Para redactar especificaciones basta Codex con acceso al proyecto y a esta skill. No hace falta tener un emulador funcionando para definir el producto.

Para implementar y probar se necesita el entorno Android del proyecto: JDK compatible, SDK, Gradle Wrapper y un dispositivo/emulador para las pruebas que lo requieran. No se fija una versión universal de JDK, AGP, Kotlin o SDK; se comprueban las versiones existentes y su compatibilidad.

El comprobador opcional necesita Python 3.9 o posterior y solo usa la biblioteca estándar. La aplicación que se desarrolla sigue siendo Android/Kotlin: Python se utiliza únicamente para esta herramienta auxiliar.

GitHub requiere acceso al repositorio mediante un conector disponible o Git/GitHub CLI autenticados. No se deben incluir tokens en los prompts ni en los archivos de la skill.

## Primer uso

Escribe en la conversación de Codex, abierta en la raíz de tu app:

```text
Usa $android-kotlin-sdd para iniciar el SDD de este proyecto Android.
Revisa lo que ya existe y ayúdame a definir el producto. Hazme preguntas
de una en una, con opciones y una recomendación razonada. Genera los
documentos progresivamente e incluye una estrategia de Git y GitHub.
Empecemos por el problema que queremos resolver.
```

No es un comando para ejecutar en Bash o Fish. Es una instrucción para Codex.

La skill ejecuta el diálogo y redacta los documentos; no necesitas copiar manualmente cada prompt. Si deseas ver o adaptar uno, pide: «Muéstrame el prompt completo de la fase de planificación para este proyecto».

## Documentos generados

```text
tu-app/
├── AGENTS.md
├── docs/
│   └── constitution.md
└── specs/
    ├── 001-primera-funcionalidad/
    │   ├── spec.md
    │   ├── plan.md
    │   └── tasks.md
    └── 002-otra-funcionalidad/
        ├── spec.md
        ├── plan.md
        └── tasks.md
```

Cada carpeta representa una funcionalidad comprobable. La constitución y AGENTS.md son comunes. Si se solicita `specs/plan.md`, puede actuar como mapa global de prioridades, dependencias y enlaces, sin duplicar los planes técnicos.

Las rutas existentes o expresamente elegidas por el usuario se conservan. Una barra inicial en una ruta documental se interpreta como raíz del proyecto, no como raíz del sistema operativo.

## Flujo de trabajo

1. **Entender:** problema, usuarios, recorrido principal y límites.
2. **Acordar principios:** constitución y reglas operativas para Codex.
3. **Especificar:** requisitos observables en EARS, errores y exclusiones.
4. **Clarificar:** detectar contradicciones y resolver decisiones pendientes.
5. **Diseñar:** componentes Android, datos, permisos y pruebas trazables.
6. **Dividir:** tareas pequeñas con dependencias y «Hecho cuando».
7. **Implementar:** ejecutar las tareas autorizadas con pruebas adecuadas.
8. **Validar:** recorrer requisitos y registrar evidencia real.
9. **Evolucionar:** modificar primero el contrato cuando cambie el comportamiento.

La skill conserva el alcance del encargo: pedir documentación no implica pedir código o publicación. Si el usuario encarga todo el proceso, puede continuar entre tareas sin solicitar de nuevo autorizaciones ya dadas. Si se prefiere revisión fase a fase, se puede pedir expresamente.

## Ejemplos de uso

**Otra funcionalidad:**

```text
Usa $android-kotlin-sdd para preparar una nueva spec de sincronización.
Conserva las decisiones del MVP y aclara conmigo el comportamiento offline
y los conflictos antes de diseñar la implementación.
```

**Implementar una tarea concreta:**

```text
Usa $android-kotlin-sdd para implementar solo T2 de
specs/001-recordatorios/tasks.md. Verifica los RF relacionados y registra
la evidencia antes de marcarla como completada.
```

**Retomar:**

```text
Usa $android-kotlin-sdd para continuar desde los documentos y cambios
actuales. Resume la fase, las decisiones pendientes y la siguiente tarea
del alcance ya encargado, sin reiniciar la entrevista.
```

**GitHub:**

```text
Usa $android-kotlin-sdd para preparar Git y GitHub para este proyecto.
Revisa si ya existe repositorio y propón ramas por spec, commits trazables,
pull requests y comprobaciones Android en GitHub Actions. Pregunta por
el destino y la visibilidad si todavía no están definidos.
```

## Git y GitHub

El flujo comprende repositorio nuevo o existente, `.gitignore` Android, ramas por funcionalidad, commits coherentes de documentación/código, push, PR, CI y versiones. Cada acción se realiza cuando forma parte del encargo y hay un destino identificado.

Se preservan cambios ajenos y se revisan los archivos preparados para commit. Los documentos se versionan junto al código. Se distingue entre commit local, subida, PR, merge, tag, release y publicación en Google Play.

Los workflows de CI se adaptan al proyecto: unitarios, lint, compilación y pruebas instrumentadas cuando correspondan. No se atribuye éxito a un workflow que todavía no se ha ejecutado ni a una comprobación de otro commit.

Los prompts completos se encuentran en [references/git-github.md](references/git-github.md).

## Comprobador documental

Desde la carpeta de esta skill, indicando la raíz de tu aplicación:

```sh
python3 scripts/audit_sdd.py /ruta/a/tu-app
python3 scripts/audit_sdd.py /ruta/a/tu-app --ready
python3 scripts/audit_sdd.py /ruta/a/tu-app --ready --json
```

- Modo normal: admite borradores incompletos con advertencias; sigue señalando inconsistencias estructurales.
- `--ready`: exige documentos sin marcadores pendientes y referencias de requisitos en planes y tareas.
- Retorno `0`: sin errores estructurales; `1`: errores detectados.

Comprueba IDs duplicados, referencias inexistentes, cobertura textual, dependencias de tareas —también entre specs—, ciclos y casillas marcadas sin evidencia registrada. Utiliza el formato de las plantillas incluidas. Otros formatos deben revisarse manualmente.

**No demuestra que la app cumpla los requisitos**, no ejecuta Gradle y no sustituye la revisión semántica ni las pruebas Android.

Para probar el comprobador:

```sh
python3 -B scripts/test_audit_sdd.py
```

Las pruebas utilizan carpetas temporales y no modifican la app del usuario.

## Organización de la skill

| Ubicación | Contenido |
| --- | --- |
| [SKILL.md](SKILL.md) | Entrada, reglas y selección de fases. |
| [agents/openai.yaml](agents/openai.yaml) | Nombre visible y prompt inicial de Codex. |
| [references/entrevista.md](references/entrevista.md) | Preguntas progresivas e inferencias responsables. |
| [references/prompts-base.md](references/prompts-base.md) | Contexto, constitución, AGENTS y varias specs. |
| [references/prompts-spec.md](references/prompts-spec.md) | Especificación, EARS y clarificación. |
| [references/prompts-plan-tareas.md](references/prompts-plan-tareas.md) | Diseño, tareas y auditoría documental. |
| [references/prompts-ejecucion.md](references/prompts-ejecucion.md) | Implementación, aceptación, cambios y reanudación. |
| [references/android-kotlin.md](references/android-kotlin.md) | Decisiones técnicas Android. |
| [references/git-github.md](references/git-github.md) | Versionado, PR, CI y entregas. |
| [assets/templates](assets/templates) | Seis plantillas de documentos. |
| [scripts/audit_sdd.py](scripts/audit_sdd.py) | Comprobador opcional de solo lectura. |

## Procedencia y límites

Adaptación del método publicado en [Hello SDD, de MoureDev](https://github.com/mouredev/hello-sdd), originalmente aplicado a una CLI Python. Se consultaron su skill, los prompts, las plantillas, los artefactos del ejemplo y la pizarra del curso. El repositorio fuente declara Apache-2.0.

No se obtuvo una transcripción completa verificable del vídeo; no se afirma que cada explicación oral haya sido contrastada. Android/Kotlin, Codex, GitHub, el comprobador y la reanudación son adaptaciones o ampliaciones para este flujo.

Consulta [references/fuentes.md](references/fuentes.md) para la revisión exacta de las fuentes y sus enlaces.
