# Prompts de diseño y desglose

Lee [android-kotlin.md](android-kotlin.md) y las plantillas [plan.md](../assets/templates/plan.md) y [tasks.md](../assets/templates/tasks.md) antes de la fase correspondiente.

## P7. Plan técnico de Android

```text
Genera {carpeta-spec}/plan.md a partir de su spec y la constitución.
Inspecciona el Android real: módulos, Gradle Wrapper, AGP, Kotlin, Compose
o XML, SDK, JDK, dependencias, manifiestos y tests. Si todavía no hay app,
propón una base compatible y marca las comprobaciones pendientes.
En esta fase diseña; no escribas código de producción.

Detecta primero requisitos ambiguos o inviables. Resuelve lo verificable
en documentación oficial y pregunta solo lo que cambia el comportamiento
del producto. No prometas tiempos exactos o permisos que Android no garantiza.

Incluye:
1. Objetivo, spec/revisión usada, restricciones y hechos del entorno.
2. Componentes y estructura mínima con RF que cubre cada parte. Diferencia
   paquetes de módulos Gradle. Conserva arquitectura existente cuando sirva.
3. Pantallas, navegación, estado UI, acciones, errores y restauración de
   estado frente a recreación/proceso perdido cuando lo exige la función.
4. Modelo de datos, relaciones, invariantes, origen de verdad, persistencia,
   migraciones y contratos externos solo si aplican.
5. Flujo técnico de la función principal y pseudocódigo para reglas complejas,
   fechas, colisiones o reintentos. Define inyección de reloj/dispatcher/fakes
   cuando facilite pruebas deterministas.
6. Para automatización: disparador, mecanismo Android, condiciones,
   precisión posible, cancelación, reintentos, idempotencia, reinicios,
   permiso denegado y observabilidad. Justifica cada mecanismo elegido.
7. Permisos concretos según versiones soportadas, momento de solicitud y
   alternativa visible si se deniegan; datos sensibles y secretos si existen.
8. Decisiones con alternativa evaluada y motivo de descarte. No introduzcas
   nuevas funciones justificándolas como necesidades arquitectónicas.
9. Estrategia de tests: lógica JVM, repositorios, integración Android, UI
   Compose/Views y dispositivos apropiados. Mapea RF/RNF a comprobaciones.
10. Secuencia, dependencias entre specs, riesgos concretos y cuestiones abiertas.

Verifica compatibilidad de versiones sin actualizar a ciegas. Usa la ayuda
local para comandos Android CLI y tareas Gradle. No inventes nombres de
plantillas ni conviertas nuestra configuración de CachyOS/Fish en requisito
universal; adapta comandos al sistema y shell detectados.

Revisa cobertura requisito por requisito. Presenta decisiones y diferencias
frente al estado actual; conserva supuestos y pruebas aún no ejecutadas.
```

## P8. Tareas pequeñas y comprobables

```text
Genera {carpeta-spec}/tasks.md usando spec.md, plan.md y constitución.
Descompón en tareas de un resultado verificable cada una, en orden de
dependencia. Usa identificadores estables T1, T2 y casillas sin marcar.
Apunta a incrementos de aproximadamente 20–30 minutos de trabajo enfocado,
como guía de tamaño, no promesa de duración de builds o instalaciones.
Divide una tarea si combina resultados independientes o demasiados RF.

En cada tarea incluye objetivo, RF/RNF relacionados, dependencias por ID,
archivos/componentes afectados, primer escenario de prueba, trabajo previsto,
«Hecho cuando:», verificación y evidencia inicialmente no ejecutada.
Las tareas de infraestructura sin RF directo justifican qué tareas desbloquean.
No uses «Todos» como sustituto de la cobertura explícita.

Para comportamiento nuevo, pon pruebas primero cuando permitan comprobar
la regla. No fuerces tests vacíos de formato o scaffolding sin valor.
Integra unitarios en lógica, UI/instrumentados donde Android lo requiere y
comprobaciones manuales de dispositivo cuando una simulación no baste.

Incluye una tarea de aceptación que recorra RF y criterios de finalización,
además de lint/build según el proyecto. No marques terminadas tareas por
tener el archivo creado ni por haber escrito la prueba.

Comprueba que cada RF tenga diseño y al menos una tarea de verificación,
que las dependencias existan y no formen ciclos. Referencias a otra spec
incluyen su carpeta y ID. No anuncies paralelismo si hay dependencias.

Conserva historial y evidencia de tareas ya realizadas al actualizar un
documento existente. Si una modificación invalida su resultado, márcalo y
añade la regresión necesaria sin reescribir el pasado como si no ocurrió.
```

## P9. Auditoría documental antes de implementar

```text
Audita constitución, instrucciones del agente (AGENTS.md o CLAUDE.md y
sus imports), spec, plan y tareas de {feature}.
Comprueba que los mismos términos significan lo mismo y que no hay
funciones del plan ausentes de la spec ni requisitos sin tareas.

Entrega una tabla RF/RNF → componente → tarea → prueba prevista y otra
lista solo con huecos, contradicciones o decisiones pendientes relevantes.
Comprueba referencias entre specs y dependencias sin ciclos.
Si el encargo es revisión, no edites; si se pidió preparar/corregir el
paquete documental, corrige inconsistencias mecánicas sin cambiar intención.

Opcionalmente ejecuta el comprobador de solo lectura de la skill para el
formato nuevo: --agent codex, --agent claude o --agent both, según el
proyecto. Distingue su cobertura textual de una revisión semántica.
Veredicto: listo para implementar / borrador con decisiones pendientes.
Una documentación coherente no prueba todavía la corrección de la app.
```
