# AGENTS.md — {{PROYECTO}}

## Contexto

{{PROPÓSITO_Y_ESTADO_REAL_EN_DOS_FRASES}}

## Fuentes de trabajo

- Principios: [docs/constitution.md](docs/constitution.md).
- Especificaciones: `specs/NNN-nombre/`; lee `spec.md`, `plan.md` y `tasks.md` de la funcionalidad del encargo.
- Para reanudar, comprueba instrucciones aplicables, estado Git, decisiones y punto de continuación de esa spec. Si hay varias candidatas sin contexto suficiente, pregunta cuál.
- Antes de cambiar comportamiento actualiza su contrato. Preserva IDs, acuerdos y cambios no relacionados.

## Estructura y convenciones

{{MÓDULOS_REALES_ESTILO_KOTLIN_RECURSOS_UI_IDIOMAS}}

## Comandos

| Propósito | Comando del proyecto | Comprobado / pendiente |
| --- | --- | --- |
| Tests unitarios | {{COMANDO_TESTS}} | {{EVIDENCIA_TESTS}} |
| Lint | {{COMANDO_LINT}} | {{EVIDENCIA_LINT}} |
| Compilar | {{COMANDO_BUILD}} | {{EVIDENCIA_BUILD}} |
| Tests Android | {{COMANDO_ANDROID_TESTS}} | {{DISPOSITIVO_Y_EVIDENCIA}} |
| Instalar para probar | {{COMANDO_INSTALL}} | {{DESTINO_Y_EVIDENCIA}} |

Si aún no existe código, sustituye esta tabla por el estado documental y las comprobaciones pendientes.

## Trabajo por tareas

- Ejecuta el alcance solicitado; documentación no autoriza por sí sola implementación.
- En código, sigue las dependencias y el «Hecho cuando» de cada tarea. Prueba el comportamiento relevante antes de marcarla completa.
- Reporta comprobaciones no ejecutadas; una compilación satisfactoria no demuestra todos los criterios funcionales.
- Guarda resultado, decisiones pendientes y siguiente paso en los documentos de la spec.

## Git y GitHub, si forman parte del proyecto

{{RAMA_BASE_CONVENCIÓN_COMMITS_POLÍTICA_PR_Y_CI_ACORDADAS_O_NO_APLICA}}

Versiona documentación y código coherentemente. Revisa diff y staged; incluye solo cambios del encargo. Conserva las autorizaciones existentes y distingue commit local, push, PR, merge y publicación.
