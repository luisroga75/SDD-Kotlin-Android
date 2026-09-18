# Prompts de contexto, constitución y AGENTS.md

Adapta los campos entre llaves al caso real o conviértelos en una pregunta concreta. Estos prompts funcionan en Codex, sin comandos slash ni APIs de Claude.

## P0. Arrancar o entender un proyecto

```text
Usa $android-kotlin-sdd para ayudarme a definir {idea de app Android}.
Trabaja en {raíz}; el alcance es {documentación / también implementación}.
Inspecciona archivos e instrucciones aplicables. Distingue plantilla,
funciones existentes y documentos SDD. No deduzcas el producto del nombre.
Separa hechos observados, requisitos expresados, hipótesis y dudas.

Guíame con preguntas de una en una, empezando por la de mayor impacto.
Ofrece alternativas comprensibles y tu recomendación razonada. Reutiliza
respuestas de archivos y conversación. No conviertas recomendaciones en
decisiones confirmadas sin indicarlo.

Define conmigo usuarios, problema, resultado, primer recorrido completo,
datos, automatizaciones y límites. Describe un ejemplo observable de uso.
Para automatizaciones aclara disparador, efecto, precisión temporal,
cancelación y fallos en la medida necesaria para este caso.

Propón un primer corte funcional pequeño. Si hay resultados independientes,
sugiere specs separadas con dependencias. Conserva una constitución y un
AGENTS.md comunes. Guarda decisiones en ellos y/o la primera spec; no
añadas documentos de visión o arquitectura separados sin necesidad.

Empieza por la primera pregunta cuya respuesta falte. Si la información
es suficiente, genera directamente el borrador documental.
```

## P1. Constitución

Lee [constitution.md](../assets/templates/constitution.md). No heredes la prohibición de red o base de datos de la app Python del curso.

```text
Genera o actualiza docs/constitution.md para {proyecto} usando hechos del
repositorio y decisiones de nuestra conversación.

Redacta de seis a ocho principios breves y verificables sobre relación
spec/código, simplicidad Android/Kotlin, separación de lógica e interfaz,
verificación, datos, permisos e idiomas cuando afecten al producto.
Justifica las decisiones no obvias. Cada principio debe comprobarse;
«calidad máxima» o «arquitectura robusta» no bastan.

Para una app nueva propone Kotlin, Compose y Gradle Wrapper; para una
existente conserva su base compatible. No hagas obligatorias librerías
opcionales ni confundas un principio con una función del MVP. No fijes
versiones por intuición. Registra restricciones expresas y decisiones
delegadas. Persistencia y conectividad deben responder a este producto.

Mantén los principios en unas quince líneas y separa debajo estado,
revisión, decisiones pendientes y mecanismo de cambio. Ante contradicción,
explica el impacto en specs y código. Preserva acuerdos existentes.

Presenta el documento para revisión. Continúa el alcance ya encargado en
lo que no dependa de dudas materiales. Si he pedido revisión fase a fase,
espera mi respuesta antes de pasar a la siguiente.
```

## P2. AGENTS.md para Codex

Lee [AGENTS.md](../assets/templates/AGENTS.md).

```text
Crea o mejora AGENTS.md en la raíz de {proyecto} para trabajar con Codex.
Lee los AGENTS.md/AGENTS.override.md aplicables y la constitución.
Preserva instrucciones del equipo e incorpora lo necesario para el SDD
Android acordado. No edites instrucciones globales.

Incluye descripción fiel, estructura relevante, enlace a constitución y
regla para localizar la spec activa y sus planes/tareas. No fijes para
siempre la primera funcionalidad como única spec activa.

Incluye comandos de compilación, tests, lint e instalación adecuados al
módulo y variante reales. Distingue verificados de pendientes. Si no hay
Gradle Wrapper, indica fase documental; no inventes comandos ejecutados
ni generes una app fuera del encargo.

Incluye convenciones necesarias de Kotlin, recursos UI e idioma; límites;
regla de actualizar requisitos antes del código; y verificaciones según
tipo de tarea. Tests de UI requieren dispositivo/emulador, y pruebas no
ejecutadas se reportan como tales. No traslades pytest ni comandos Python.

Remite a documentos, sin duplicarlos. No crees CLAUDE.md para Codex.
AGENTS.md no anula instrucciones de sistema ni permisos de herramientas.
Muestra los cambios y comandos pendientes. Redactar estas instrucciones
no incluye hacer commits ni cambiar el sistema operativo.
```

## P3. Varias especificaciones

```text
Organiza {funcionalidades} en incrementos comprobables. Lee constitución
y specs relacionadas. Reutiliza una spec al cambiar el mismo contrato;
crea otra para un resultado independiente con aceptación y dependencias.

Asigna máximo número existente más uno, sin renumerar. Cada carpeta tendrá
spec.md, plan.md y tasks.md cuando llegue su fase. No planifiques en detalle
ideas todavía vagas. Identifica dependencias por carpeta/requisito,
responsabilidad y límites para no duplicar comportamiento.

Si pedí specs/plan.md, úsalo como mapa global de orden, estado, dependencias
y enlaces. Si indiqué otra estructura, mantenla y registra el mapa de
rutas. Evita contratos duplicados en raíz y carpetas.

Recomienda una spec siguiente y qué valor permitirá demostrar. Conserva
el resto como alcance futuro, sin confundir prioridad con aprobación.
```
