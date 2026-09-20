# Procedencia y alcance de la adaptación

Consulta inicial: 18 de septiembre de 2026. Ampliación con transcripción aportada por el usuario: 20 de septiembre de 2026.

Fuente principal: [Hello SDD, de Brais Moure / MoureDev](https://github.com/mouredev/hello-sdd), revisión `358dfe85a818bccdd839f78e804668b3ebaa10b5`. El repositorio declara licencia Apache-2.0. Esta skill es una redacción propia que adapta su método, no una transcripción ni una copia del proyecto Python.

Materiales leídos:

- [Skill spec-generator](https://github.com/mouredev/hello-sdd/blob/358dfe85a818bccdd839f78e804668b3ebaa10b5/habits-cli/.claude/skills/spec-generator/SKILL.md) y su plantilla.
- [Prompts por fase](https://github.com/mouredev/hello-sdd/blob/358dfe85a818bccdd839f78e804668b3ebaa10b5/samples/prompts.md).
- [Práctica y prompts completos](https://github.com/mouredev/hello-sdd/blob/358dfe85a818bccdd839f78e804668b3ebaa10b5/habits-cli/README.md).
- `samples/AGENTS.md`, constitución y spec/plan/tasks del ejemplo `001-habits-mvp`.
- [Pizarra del curso](https://github.com/mouredev/hello-sdd/blob/358dfe85a818bccdd839f78e804668b3ebaa10b5/samples/sdd.excalidraw), incluidos sus bloques y diagramas.

Vídeo aportado: [El fin del Vibe Coding: Crea software robusto con este método](https://www.youtube.com/watch?v=5HaOxAAA5qI). Posteriormente el usuario proporcionó «Transcripción - El fin del Vibe Coding.md», leído completo, con marcas de 0:00 a 2:03:00. Se basa en subtítulos automáticos y advierte de posibles errores terminológicos: se contrasta con los archivos del curso, sin afirmar verificación palabra por palabra del audio. No se redistribuye la transcripción completa.

La lectura reforzó spec-first/spec-anchored y revisión del código (28:01–32:01), orden flexible de AGENTS y constitución (1:04:00–1:08:01), modo de planificación (48:01 y 1:05:01–1:07:00), revisión de plan/tareas (1:26:00–1:36:00), sincronización y bugs (1:39:02–1:40:03) y revisión humana de documentos, código y tests (1:57:00–2:01:00). El modo del agente no equivale a plan.md ni permite saltarse sus restricciones de escritura.

## Correspondencia

| Método del curso | Aplicación en esta skill |
| --- | --- |
| Constitución una vez por proyecto | Principios Android compartidos, con cambios explícitos. |
| Contexto del agente | AGENTS.md adaptado a Codex. |
| Entrevista progresiva y EARS | P0/P4, una pregunta cada vez y supuestos visibles. |
| QA antes del plan | P5/P6, detección seguida de clarificación. |
| Plan técnico | P7, pantallas/estado/datos/automatización Android. |
| Tareas pequeñas y tests primero | P8/P10, incrementos comprobables y pruebas adecuadas. |
| Validación requisito por requisito | P11, resultados reales sin confundir build con aceptación. |
| Cambiar primero el contrato | P12, impacto y regresión trazables. |
| Specs que acompañan al código | Modo spec-anchored y reanudación P13. |

Se conserva el diálogo y revisión del curso. La adaptación permite continuar trabajo ya autorizado sin aprobaciones repetidas; respeta una preferencia explícita de revisar cada fase. El mapa global opcional, Git/GitHub, CI, detector documental, controles Android y prompts de reanudación son ampliaciones para este encargo, no afirmaciones sobre el vídeo.

Codex: [AGENTS.md](https://developers.openai.com/codex/guides/agents-md/) y [skills](https://developers.openai.com/es-419/docs/build-skills). La instalación de esta entrega usa el directorio personal de skills de este entorno (`$CODEX_HOME/skills`). En instalaciones que descubren skills personales en `~/.agents/skills`, se puede colocar allí la carpeta o enlazarla, conservando una única fuente. No hace falta instalar herramientas de Claude.

Las referencias Android y GitHub están junto a los prompts que las utilizan. Consulta versiones actuales al aplicar el flujo; esta skill no fija una combinación perpetua de JDK, AGP, Kotlin, SDK ni acciones de CI.
