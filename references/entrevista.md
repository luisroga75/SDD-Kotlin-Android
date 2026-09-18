# Entrevista progresiva y deducción responsable

## Preparación

Construye un registro pequeño: hecho confirmado, fuente, decisión pendiente, supuesto propuesto e impacto. La existencia de una pantalla o librería describe el estado actual, no necesariamente un requisito. Un BUILD SUCCESSFUL anterior no sustituye las pruebas actuales.

Pregunta al nivel del usuario: explica «guardar solo en el móvil o compartir entre dispositivos» antes de hablar de persistencia y sincronización. No pidas elegir un proveedor cuando todavía no se conoce el problema.

## Elegir preguntas

Una pregunta por turno y máximo habitual de seis por ciclo. Ordena por impacto y omite cuestiones resueltas o irrelevantes:

1. Resultado y persona: ¿qué hace hoy, qué le cuesta y qué debería conseguir? Si dice «automatizar todo», solicita un ejemplo real.
2. Primer recorrido: acción de inicio, información aportada y resultado visible. Propón un MVP demostrable de principio a fin.
3. Datos y conectividad: qué debe funcionar sin Internet, de quién son los datos y si se comparten/recuperan al cambiar de móvil. No añadas cuenta porque exista una API.
4. Automatización: disparador, efecto, puntualidad o demora, otra app/persona afectada, cancelación y fallo.
5. Límites: elige el caso más decisivo entre duplicado, concurrencia, borrado, permiso denegado, reintento, ausencia de datos, cambio horario e interrupción.
6. Aceptación: demostración que permitiría dar la versión por útil y qué queda para después.

Una feature pequeña puede necesitar una pregunta. Un producto amplio necesita varios ciclos por resultados observables. El límite de preguntas no permite declarar resuelto lo que sigue ambiguo.

## Ejemplo de pregunta

Ante «quiero recordatorios automáticos»:

> ¿El aviso debe aparecer a una hora concreta o admite demora? Si es una cita, recomiendo una hora elegida por la persona; si es una sincronización, suele bastar una ejecución flexible. Esto cambia el comportamiento cuando el móvil está en reposo.

Da opciones de respuesta cuando ayuden, incluida la posibilidad de delegar. Una opción preseleccionada no es una respuesta enviada. Si el usuario delega, elige con motivo y registra la decisión sin volver a preguntar lo mismo.

## Qué inferir

| Situación | Conducta |
| --- | --- |
| Conversación en español | Proponer documentación española, respetando idioma del código existente. |
| Kotlin/Compose ya presentes | Conservarlos y citar archivos que lo prueban. |
| Solo una pantalla inicial | No atribuir login, nube, cobros o arquitectura completa. |
| Uso personal offline | Proponer datos locales; aclarar recuperación si condiciona la primera versión. |
| Automatizar mensajes | Aclarar canal, destinatario, disparador y confirmación; no suponer envío sin intervención. |
| «Adivina lo que necesito» | Hipótesis razonada, alternativa e impacto de equivocarse. |
| Falta una decisión material | `[NECESITA ACLARACIÓN: pregunta e impacto]`; continuar en apartados independientes. |

Registra `S-1: propuesta, motivo, impacto, estado` para supuestos y `D-1: pregunta, documento afectado, bloquea/no bloquea` para dudas. No elimines una duda al alcanzar el límite de preguntas.

## Después de cada respuesta

Actualiza el borrador autorizado, señala consecuencias si cambió una decisión anterior y formula otra pregunta solo si afecta a alcance, aceptación o una decisión difícil de revertir. Presenta la spec cuando el comportamiento sea verificable. Guarda spec activa, fase, última respuesta, pendientes y siguiente acción para reanudar.

El curso propone revisar constitución y spec explícitamente. Aquí se revisan documentos concretos sin repetir aprobaciones ya dadas. Una petición de generar todo permite completar documentos con propuestas identificadas; una preferencia de revisión fase a fase se respeta. La ausencia de respuesta a una decisión material nunca se convierte en consentimiento.
