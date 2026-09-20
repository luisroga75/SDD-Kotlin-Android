---
name: android-kotlin-sdd
description: "Guía el ciclo SDD de apps Android con Kotlin en Codex: entrevista, AGENTS.md, constitución, specs, planes, tareas, implementación, validación y control de versiones con Git/GitHub. Úsala para iniciar, continuar o revisar este proceso; no para consultas aisladas de Kotlin."
---

# SDD para Android con Kotlin

Convierte una idea en decisiones explícitas y documentos que acompañan al código. Habla en español salvo otra preferencia. Sirve para cualquier producto Android: no presupongas nombre, negocio, backend ni funciones.

## Inicio y alcance

1. Determina la raíz real del proyecto y la intención: iniciar, continuar, otra spec, revisar, planificar, implementar, validar o cambiar. La carpeta de esta skill no es el proyecto.
2. Lee las instrucciones AGENTS aplicables, cambios locales y documentos SDD antes de escribir. Si hay código, inspecciona configuración Gradle, catálogo de versiones, manifiestos y pruebas relevantes. En una carpeta vacía puedes documentar sin crear aún una app.
3. Lee [entrevista.md](references/entrevista.md). Pregunta lo que falta y cambia el producto, sin repetir respuestas disponibles en archivos o conversación.
4. Resume hechos, supuestos y próxima decisión. Si solo tienes un nombre, pregunta primero qué problema resuelve para quién.
5. «Prepara SDD», «documenta» o «guíame» autorizan trabajo documental. Implementar necesita una petición que lo incluya. «Haz todo, incluida la app» sí autoriza recorrer también las tareas; conserva ese alcance al continuar.

## Organización

En proyectos nuevos usa rutas relativas a su raíz:

```text
AGENTS.md
docs/constitution.md
specs/
  001-nombre-funcionalidad/
    spec.md
    plan.md
    tasks.md
  002-otra-funcionalidad/
    spec.md
    plan.md
    tasks.md
```

- Una carpeta representa un comportamiento con valor comprobable, no una capa técnica. No separes UI, datos y tests de una función en tres specs.
- Usa máximo número existente más uno, con al menos tres dígitos; comprueba colisiones. No reutilices ni renumeres specs antiguas.
- `spec.md`: QUÉ y POR QUÉ. `plan.md`: CÓMO. `tasks.md`: orden y evidencia. `AGENTS.md`: instrucciones operativas. Constitución: principios estables.
- Conserva las rutas existentes. Si el usuario pide literalmente `/spec.md`, `/tasks.md` o `/specs/plan.md`, interpreta la barra como raíz del proyecto salvo indicación contraria, conserva esos destinos y registra la correspondencia. Nunca escribas esos documentos en la raíz del sistema operativo.
- Con varias specs, un `specs/plan.md` pedido por el usuario puede ser el mapa global de funcionalidades, dependencias y enlaces a planes técnicos. No dupliques los contratos. Usa [mapa-specs.md](assets/templates/mapa-specs.md) cuando se solicite o aporte valor.
- Edita de forma acotada y preserva el contenido del usuario. Sustituye marcadores de plantilla; los datos desconocidos llevan una pregunta concreta o propuesta identificada, nunca una respuesta inventada.

## Conversación y decisiones

Pregunta una cosa cada vez; normalmente hasta seis por ciclo de especificación. Adapta la cadencia a la preferencia del usuario. Tras seis produce un borrador útil con pendientes, sin declarar cerrados los huecos ni prolongar preguntas por rutina.

Ofrece opciones, recomendación razonada y respuesta libre. En la spec son opciones de comportamiento; las librerías se eligen en el plan. Infiere detalles reversibles identificando el supuesto. No confirmes por silencio reglas de negocio, exactitud temporal, pérdida de datos, destinatarios, acceso a información o costes.

Usa preguntas asíncronas cuando estén disponibles y avanza en apartados independientes mientras esperas. De lo contrario pregunta en la conversación y espera. No simules respuestas. Una decisión material pendiente bloquea el trabajo dependiente, no todo el proyecto.

La constitución y la spec se revisan con el usuario sobre documentos concretos. No impongas aprobaciones repetidas para continuar un alcance ya encargado. Si pide revisión fase a fase, respétala. Si delega decisiones, registra qué se ha asumido y por qué; no extiendas esa delegación a acciones externas ajenas al encargo.

## Revisión humana y planificación

Aplica spec-first con continuidad spec-anchored: specs, planes, tareas, código y pruebas permanecen coherentes. No es spec-as-source ni permiso para regenerar toda la app sin revisión. El usuario debe poder revisar documentos, diseño, código y tests; la salida del agente no certifica por sí sola la intención.

En el modo docente presenta cada fase para revisión antes de avanzar, incluidos plan y tareas. Respeta un encargo explícito de varias fases sin repetir autorizaciones. AGENTS y constitución se preparan al comienzo en el orden útil para el proyecto y no se recrean para cada funcionalidad.

Recomienda el modo de planificación del agente para estudiar propuestas cuando esté disponible; no afirmes haberlo activado ni lo confundas con el documento `plan.md`. Si ese modo impide escribir, presenta el borrador y solicita el cambio de modo para guardar lo acordado, sin sortear restricciones. En modo normal, redactar documentación autorizada no implica implementar la app.

Si código y documentos divergen, distingue un bug frente a un contrato acordado de una decisión nueva: no cambies el requisito para justificar un fallo. Registra corrección, regresión e impacto en la spec correspondiente.

## Fases y recursos

Lee íntegramente la referencia de la fase actual y sus plantillas necesarias. Los prompts se ejecutan adaptados al contexto; no los vuelques completos en cada respuesta. Si el usuario pide un prompt, entrégalo con sus rutas y decisiones resueltas.

| Fase | Referencia | Resultado |
| --- | --- | --- |
| Contexto, constitución y agente | [prompts-base.md](references/prompts-base.md) | Principios verificables, reglas operativas y alcance inicial. |
| Spec y clarificación | [prompts-spec.md](references/prompts-spec.md) | RF en EARS, RNF medibles, límites y dudas visibles. |
| Plan y tareas | [prompts-plan-tareas.md](references/prompts-plan-tareas.md) y [android-kotlin.md](references/android-kotlin.md) | Diseño trazable y tareas pequeñas con dependencias y aceptación. |
| Implementar y validar | [prompts-ejecucion.md](references/prompts-ejecucion.md) y [android-kotlin.md](references/android-kotlin.md) | Trabajo autorizado por tareas y evidencia real por RF. |
| Cambiar, otra spec o reanudar | [prompts-ejecucion.md](references/prompts-ejecucion.md) | Spec actualizada antes del código y estado reconstruido. |
| Versionar y colaborar en GitHub | [git-github.md](references/git-github.md) | Repositorio, ramas por spec, commits trazables, PR, CI y versiones según el alcance autorizado. |

Las seis plantillas editables están en [assets/templates](assets/templates). No crees directorios vacíos ni informes adicionales por cumplirlas: adapta apartados al producto.

## Invariantes

- IDs estables `RF-1`, `RNF-1`, `T1`; entre specs usa `001-funcion/RF-1`. No recicles IDs retirados: registra sustituciones.
- Un supuesto es una propuesta, no un requisito confirmado. Conserva el vocabulario y hechos del usuario; expón contradicciones antes de resolverlas.
- La spec expresa comportamientos observables, también frente a permisos denegados, interrupciones o falta de red si aplican. Componentes, esquemas y comandos pertenecen al plan.
- Conserva restricciones técnicas impuestas en constitución/plan y enlázalas desde la spec; no las descartes por una separación artificial.
- Una revisión sin edición genera hallazgos. Preparar o corregir documentos permite escribirlos. No modifiques otras apps ni perfiles globales como parte del SDD del proyecto.
- Kotlin y Compose son propuesta para apps nuevas; conserva Kotlin/XML existente sin migración implícita. No impongas Room, Hilt, login, nube, módulos o Clean Architecture sin necesidad.
- Verifica versiones y comandos con el proyecto y la ayuda local. No fijes JDK 17, plantilla Android CLI, tareas Gradle, seriales o applicationId por memoria.
- Un nuevo comportamiento se documenta antes de implementarlo. Distingue un bug frente a un RF de un cambio de contrato.
- Compilar un APK no demuestra aceptación. Pruebas no ejecutadas se reportan como tales; cero tests no equivale a cobertura.
- Guarda fase, decisiones, pendientes, siguiente paso y evidencia en los documentos pertinentes para poder retomar sin el historial del chat.
- Integra Git/GitHub si se solicita o ya forma parte del proyecto. Versiona también los documentos SDD y sincroniza su cambio con el código. «Generar specs» no implica publicarlas; respeta lo ya autorizado para commits, push, PR o merge sin pedirlo de nuevo.

## Comprobación

Revisa enlaces, cobertura RF → diseño → tareas → prueba, dependencias y supuestos. Para documentos nuevos con nuestras plantillas puedes ejecutar el comprobador de solo lectura:

```text
python3 <ruta-de-la-skill>/scripts/audit_sdd.py <raiz-del-proyecto>
python3 <ruta-de-la-skill>/scripts/audit_sdd.py <raiz-del-proyecto> --ready
```

El modo normal permite borradores con advertencias. `--ready` exige documentos completos, sin marcadores o dudas bloqueantes y con cobertura textual en plan/tareas. No ejecuta Gradle ni acredita conformidad del código: completa una revisión semántica. Para formatos existentes diferentes revisa manualmente, sin deformarlos para el script.

## Ejemplos de invocación

- `$android-kotlin-sdd Quiero definir una app Android. Entrevístame y prepara la documentación.`
- `$android-kotlin-sdd Continúa el SDD de este proyecto desde sus archivos.`
- `$android-kotlin-sdd Prepara otra spec para sincronización, conservando el MVP.`
- `$android-kotlin-sdd Implementa solo T2 de specs/001-ejemplo/tasks.md y verifica sus RF.`
- `$android-kotlin-sdd Muéstrame el prompt completo de planificación.`
- `$android-kotlin-sdd Configura Git y GitHub para este proyecto y vincula ramas, commits y PR con cada spec.`

Consulta [fuentes.md](references/fuentes.md) para procedencia, adaptación del curso y límites de acceso al vídeo.
