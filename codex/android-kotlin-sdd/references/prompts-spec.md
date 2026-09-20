# Prompts de especificación y clarificación

Lee [spec.md](../assets/templates/spec.md) y aplica la entrevista. La spec define comportamiento; clases, tablas, librerías y archivos de código pertenecen al plan.

## P4. Entrevista y spec

```text
Usa la skill android-kotlin-sdd para especificar {funcionalidad} de {proyecto}.
Objetivo: {resultado}. Lee constitución, AGENTS.md y specs relacionadas.
En esta fase no escribas código.

Pregunta de una en una, normalmente hasta seis en este ciclo, priorizando
respuestas que cambien alcance o aceptación. Usa respuestas previas y
ofrece una recomendación de comportamiento con motivo y alternativa.
Aplaza implementación al plan. Si el alcance es amplio, propone un
incremento útil y acotado.

Aclara actor, acción, entradas, resultado visible, estados de pantalla,
errores y exclusiones. Cuando afecten a la función, considera datos sin
Internet, permiso denegado, notificaciones, segundo plano y precisión
horaria. No preguntes por requisitos ajenos al producto.

Genera specs/NNN-nombre/spec.md con el siguiente número disponible y la
plantilla: contexto, actores, historias, RF numerados en EARS, RNF medibles,
escenarios, límites, fuera de alcance, finalización y dudas abiertas.

Escribe una obligación verificable por RF. Relaciona historias con RF y
límites con resultados esperados. Define duplicado, fecha actual, ordenación
y vacío si aplican. No inventes umbrales ni reglas de negocio.

Identifica cada supuesto con motivo e impacto. Marca decisiones materiales
pendientes como [NECESITA ACLARACIÓN: pregunta concreta]. Distingue lo que
la persona quiere de lo que Android puede garantizar; registra dudas de
viabilidad para investigar antes del plan.

Presenta el documento y las dudas que impiden avanzar. Conserva decisiones
aprobadas y no implementes ante una petición exclusivamente documental.
```

## EARS

Usa el patrón de condición/disparador y respuesta más claro:

| Patrón | Forma |
| --- | --- |
| Permanente | EL SISTEMA deberá {comportamiento observable}. |
| Evento | CUANDO {evento}, EL SISTEMA deberá {respuesta}. |
| Estado | MIENTRAS {estado}, EL SISTEMA deberá {comportamiento}. |
| Error | SI {condición no deseada}, ENTONCES EL SISTEMA deberá {respuesta}. |
| Opción | DONDE {opción habilitada}, EL SISTEMA deberá {comportamiento}. |

Ejemplo de recordatorios, únicamente si se acordaron esos comportamientos:

- RF-1: CUANDO la persona guarde un recordatorio con título válido, EL SISTEMA deberá mostrarlo en la lista de pendientes.
- RF-2: SI el título está vacío tras retirar espacios exteriores, ENTONCES EL SISTEMA deberá mostrar un error junto al campo.
- RF-3: SI el título está vacío tras retirar espacios exteriores, ENTONCES EL SISTEMA deberá conservar la lista sin registros nuevos.
- RF-4: SI no se permite mostrar notificaciones, ENTONCES EL SISTEMA deberá identificar el recordatorio como aviso deshabilitado en su detalle.

Separa resultados que puedan fallar independientemente. Escenarios Dado/Cuando/Entonces ilustran los RF, no los reemplazan. No exijas Cucumber o archivos `.feature` sin necesidad.

Los RNF necesitan método de evaluación: texto ampliado sin ocultar la acción principal en pantallas acordadas, ausencia de datos definidos como sensibles en registros, o tiempo de operación con entorno y volumen concretos. Un umbral desconocido se registra pendiente.

## P5. Revisión QA sin edición

```text
Revisa {spec.md} frente a la constitución y las specs relacionadas.
Este encargo es de revisión: no modifiques documentos ni código.

Agrupa hallazgos en ambigüedades, contradicciones, casos límite ausentes
y conflictos con la constitución. Para cada uno indica ID/ubicación,
contraejemplo concreto, impacto y pregunta que lo resolvería. Prioriza
lo que cambia producto, datos, permisos o aceptación.

Comprueba vocabulario, actores, errores, persistencia observable,
repeticiones, interrupciones y límites Android pertinentes. Identifica
requisitos no verificables y supuestos presentados como hechos.
No exijas funciones expresamente fuera de alcance.

En esta pasada detecta sin resolver ni diseñar arquitectura. Si no hay
hallazgos relevantes, dilo sin inventar objeciones.
```

## P6. Clarificar e incorporar respuestas

```text
Resuelve conmigo los hallazgos de {spec}. Empieza por el de mayor impacto;
pregunta una cosa cada vez y ofrece opciones de comportamiento con motivo.
Resuelve directamente lo deducible de decisiones previas o delegado por mí,
identificando la fuente o el supuesto.

Actualiza la spec con las respuestas y conserva IDs. Añade requisitos sin
reutilizar IDs retirados. Mantén límites y finalización coherentes. Muestra
el cambio de comportamiento y pendientes; no repitas preguntas resueltas.

Revisa otra vez hasta eliminar contradicciones y dudas bloqueantes, o
deja un borrador útil con la pregunta pendiente. Declara lista para plan
solo una spec cuyos comportamientos puedan comprobarse.
```
