# Prompts de ejecución, validación, cambios y continuidad

## P10. Implementar una tarea

```text
Usa la skill android-kotlin-sdd para implementar {Tn} de {carpeta-spec}/tasks.md.
Lee las instrucciones aplicables, constitución, spec y plan. Comprueba
estado Git, modificaciones locales y dependencias de la tarea.

Identifica RF/RNF y «Hecho cuando». Si el comportamiento cambió, actualiza
primero el contrato dentro del alcance solicitado; pregunta únicamente por
una decisión de producto pendiente que no puedas deducir.

Para lógica nueva o un bug reproducible, escribe primero una prueba del
comportamiento, comprueba que falla por la causa esperada e implementa lo
mínimo para pasarla. Integra pruebas Android/Compose cuando correspondan.
Para configuración o documentación usa la comprobación pertinente, sin
fabricar tests triviales. No conviertas un fallo de infraestructura en
evidencia de una prueba roja del comportamiento.

Ejecuta las verificaciones relevantes del proyecto. Registra comando,
entorno, resultado, tests reales y limitaciones. Compilar no equivale a
validar todos los RF. Si falta emulador, no marques UI como comprobada.

Marca la casilla solo si se cumple «Hecho cuando» con evidencia. Deja
pendientes verificaciones que no pudiste ejecutar. Actualiza el punto de
reanudación. Resume qué comportamiento cambió, qué RF cubre y cómo se probó.

Si pedí solo Tn, termina ahí. Si ya pedí implementar toda la spec, continúa
con las tareas autorizadas cuyas dependencias estén resueltas, sin pedir
permiso entre tareas. No incluyas nuevas funcionalidades oportunistas.
```

Si se usa Git/GitHub, enlaza con [git-github.md](git-github.md). Un commit coherente puede agrupar test y código; no publiques una prueba deliberadamente roja como si fuera un punto estable.

## P11. Validación de aceptación

```text
Valida {carpeta-spec} contra su implementación actual. Lee RF, RNF,
criterios de finalización, plan, tareas y cambios relevantes.

Para cada requisito localiza la implementación y una prueba o comprobación
que realmente observe su resultado. Ejecuta lo disponible y apropiado.
Entrega: ID → evidencia en código → prueba/escenario → resultado → hueco.
Usa estados cumplido, falla, no cubierto y no ejecutado; no conviertas una
referencia a un test en evidencia de que pasó.

Incluye el recorrido principal en dispositivo si forma parte de aceptación,
permisos/interrupciones/offline relevantes, y regresiones de specs afectadas.
Identifica módulo, variante y dispositivo/API utilizados. No exijas tests
de funciones excluidas ni repitas suites costosas sin motivo.

Comprueba criterios de finalización, dudas y casillas de tareas. Guarda la
evidencia en tasks.md o el formato existente. No marques la spec validada
mientras falte una comprobación obligatoria. Distingue validación local de
CI en GitHub y vincula el commit exacto cuando exista.

Entrega veredicto fundamentado: cumple, no cumple o verificación incompleta.
Si el encargo era solo validar, informa defectos sin arreglarlos ni alterar
la spec para que coincida con un bug. Si incluía implementar/corregir,
resuelve fallos dentro de ese alcance y vuelve a probar lo afectado.
```

## P12. Cambiar requisitos

```text
Nuevo requisito o cambio: {descripción}. Lee {spec activa}, constitución,
otras specs relacionadas y estado del código antes de actuar.

Determina si cambia el contrato existente, corrige su incumplimiento o
merece una nueva spec. Explica el impacto en RF, datos, pantallas,
permisos, automatización y aceptación. Pregunta por decisiones materiales
que no estén resueltas; propone opciones con sus consecuencias.

Si cambia comportamiento, modifica primero la spec, preservando IDs e
indicando sustituciones y límites nuevos. Muestra el diff o resumen exacto
del contrato. Después ajusta plan, dependencias y tareas de regresión.
Las evidencias antiguas siguen documentadas, pero señala cuáles caducan.

Si pedí solo documentar el cambio, termina con los documentos. Si también
pedí implementarlo, continúa dentro del alcance autorizado una vez resueltas
las dudas. No uses aprobación previa de una versión como aceptación de
una regla contradictoria nueva.
```

## P13. Reanudar en otra sesión

```text
Continúa el SDD de {proyecto}. Inspecciona AGENTS, constitución, specs,
cambios Git y, si está en alcance y disponible, la rama/PR relacionada.
No reinicies la entrevista ni vuelvas a crear documentos existentes.

Reconstruye spec activa, fase, último acuerdo, tareas cumplidas con evidencia,
pendientes, decisiones abiertas y última verificación. Si hay varias specs
plausibles y el contexto no elige una, pregunta cuál continuar antes de
modificarla. Puedes inspeccionar todas mientras tanto.

No consideres una casilla marcada prueba de un resultado vigente si cambió
el código. Prioriza la primera tarea desbloqueada según el encargo original.
«Continúa» conserva ese encargo: documentación no se transforma por sí
sola en permiso de implementar o publicar.

Resume el estado en pocas líneas y realiza el siguiente paso autorizado.
Guarda el nuevo punto de reanudación al terminar.
```
