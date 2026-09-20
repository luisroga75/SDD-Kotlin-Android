# Decisiones Android/Kotlin para el plan y la verificación

Esta referencia es un mapa de preguntas técnicas, no un stack obligatorio. Consulta documentación oficial vigente al fijar APIs, versiones, permisos o políticas.

## Descubrir el entorno

Lee `settings.gradle(.kts)`, archivos de build, `gradle/libs.versions.toml` si existe, wrapper, manifiestos y tests. Identifica módulo, variantes, minSdk/targetSdk/compileSdk, JDK de Gradle, AGP, Kotlin y Compose. Registra evidencia o «no verificado».

Usa `./gradlew --version` y tareas locales si procede; ejecutarlas puede descargar dependencias y escribir cachés, por lo que sigue los permisos del entorno. El proyecto controla Gradle y Kotlin; no requiere instalarlos globalmente. AGP 9 incorpora soporte Kotlin: verifica el modo usado antes de añadir `org.jetbrains.kotlin.android`. No migres a AGP 9 por defecto.

Para Android CLI consulta `android create --help` y `android emulator create --help` de la instalación: nombres de plantilla, listado y flags han variado. No traslades comandos de otra versión. Usa un serial obtenido de `adb devices`, nunca uno supuesto. Emulador disponible no significa iniciado.

Adapta sintaxis a Fish/Bash/Zsh/PowerShell. En Fish no cargues `.bashrc` ni reemplaces PATH para configurar Android; si se solicita configuración usa `fish_add_path`. Verifica ANDROID_HOME/ruta real; no añadas ANDROID_SDK_ROOT obsoleto como requisito. No reinstales ni cambies Java globalmente al resolver documentación.

## Arquitectura proporcionada

Para apps nuevas propone Compose, estado explícito, lógica fuera de composables y acceso a datos mediante una capa adecuada. ViewModel y Coroutines/Flow se eligen donde aporten gestión de estado y asincronía. Usa capa de dominio si la complejidad/reutilización la justifica; paquetes suelen bastar al principio.

Decide por necesidad: Room para datos estructurados, DataStore para preferencias pequeñas, inyección manual o Hilt según dependencias. No añadas backend, autenticación o modularización de antemano. En apps XML existentes planifica dentro de su estructura.

Pantallas: navegación atrás, estados vacíos/carga/error, accesibilidad, tamaño de texto y adaptación relevantes. Distingue estado temporal, restaurable y persistente. Recreación de Activity y muerte del proceso requieren pruebas diferentes; ViewModel por sí solo no conserva datos después de perder el proceso.

## Automatización

| Necesidad | Investigar y justificar |
| --- | --- |
| Trabajo mientras la persona usa la pantalla | Coroutines con alcance y cancelación apropiados. |
| Trabajo persistente diferible | WorkManager: restricciones, reintentos, nombre único e idempotencia. No promete horario exacto. |
| Alarma visible con puntualidad requerida | AlarmManager y requisitos vigentes de alarmas exactas; alternativa si no se concede acceso. |
| Trabajo continuo visible | Tipo y restricciones de foreground service, notificación y límites actuales. No asumir ejecución perpetua. |
| Evento externo | API, push, callback o mecanismo permitido; autenticación y entrega según el caso. |
| Interactuar con otra app | Preferir API/Intent/deep link soportado. Verificar acciones posibles y participación del usuario. |
| Pruebas de otras pantallas/apps | UI Automator/Appium son herramientas de test, no permiso de control para una app de producción. |

AccessibilityService no es una autorización general para automatizar todo. Si se propone, justifica la función, consentimiento y compatibilidad con reglas vigentes de distribución. No lo elijas como atajo automático.

Documenta disparador → condiciones → acción → resultado → fallo/cancelación. Considera solo cuando aplique: reinicio, Doze, red perdida, doble evento, desfase horario, reprogramación, hora local/zona e interrupción. Distingue cerrar pantalla, terminar proceso y forzar detención; no prometas la misma continuidad para los tres.

## Datos y permisos

Planifica formato, unidades, identificadores y normalización. Define origen de verdad, conflictos de sincronización y migraciones antes de depender de datos remotos o cambiar esquemas. Si la spec no requiere red, no agregues sincronización.

Para cada permiso necesario: API/versiones afectadas, motivo visible, cuándo se solicita, respuesta al rechazo/revocación y criterio de prueba. Incluye notificaciones, ubicación, cámara, Bluetooth o archivos únicamente cuando la función los usa. No pongas credenciales privilegiadas en el APK. Almacenamiento seguro no convierte una clave de servidor embebida en secreta.

## Evidencia

| Tipo de comportamiento | Verificación apropiada |
| --- | --- |
| Reglas, fechas, duplicados, orden e idempotencia | Test JVM con reloj/datos controlados. |
| Estado y concurrencia de ViewModel | Tests de estado/coroutines deterministas. |
| Persistencia/migración/contrato | Prueba de repositorio y de integración que realmente use ese mecanismo. |
| Navegación y aceptación visual | Tests Compose/Views e inspección en dispositivo cuando importe. |
| Workers y permisos del SO | Pruebas enfocadas y escenarios de dispositivo en APIs relevantes. |

Comandos frecuentes, **solo si el proyecto confirma módulo/variante**: `./gradlew :app:testDebugUnitTest`, `:app:lintDebug`, `:app:assembleDebug`, `:app:connectedDebugAndroidTest`, `:app:installDebug`. El último instala; no acredita que la UI se haya abierto o probado. Sustituye `app` y `Debug` según el proyecto. En Windows usa el wrapper correspondiente.

## Fuentes técnicas

- [Arquitectura Android](https://developer.android.com/topic/architecture/recommendations)
- [Trabajo en segundo plano](https://developer.android.com/develop/background-work/background-tasks)
- [WorkManager](https://developer.android.com/develop/background-work/background-tasks/persistent)
- [Kotlin integrado en AGP](https://developer.android.com/build/migrate-to-built-in-kotlin)
- [Compilación por terminal](https://developer.android.com/build/building-cmdline)
- [Permisos](https://developer.android.com/training/permissions/requesting)
- [Pruebas Android](https://developer.android.com/training/testing)
