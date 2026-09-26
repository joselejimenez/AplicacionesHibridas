# Coordinación con PMDM y DI

El ciclo tiene **tres módulos** que tocan el desarrollo móvil. La regla del módulo es sencilla:

!!! danger "Regla"
    Si un concepto ya se ha dado en **PMDM** o en **DI**, **no se re-explica**. Como mucho, una referencia de una línea ("como ya visteis en DI…") y seguimos.

## Qué ya está dado

| Módulo | Contenido ya impartido | Cómo lo usamos aquí |
|---|---|---|
| **PMDM** | Sistemas operativos móviles, capas del SO, arquitectura Android | Se da por sabido al explicar qué hace el *embedder* de Flutter en el Tema 2 |
| **PMDM** | Emuladores / AVD, ADB, despliegue en dispositivo real | `flutter run` usa los mismos AVD y el mismo ADB. No se explican |
| **PMDM** | Elección de tecnología con criterio (visión general) | El Tema 2 **profundiza** en la arquitectura interna; no repite la visión general |
| **DI** | Paradigmas, imperativo vs declarativo, eventos, componentes | La UI de Flutter se **transfiere** desde Compose |
| **DI** | Instalación de Android Studio y su entorno | Flutter se instala **encima** del Android Studio que ya tienen (Tema 1) |
| **DI** | Primer proyecto, estructura Gradle, función composable | Solo comparamos: `pubspec.yaml` ≈ dependencias de Gradle; widget ≈ composable |
| **DI** | UI declarativa con Compose, `Scaffold` / `TopAppBar` | `Scaffold` / `AppBar` de Flutter se presentan como equivalencias |

## Qué es propio de este módulo

Nadie más lo da; aquí se explica con detalle:

- **Arquitectura multiplataforma** comparada: nativo, híbrido con WebView (Ionic/Cordova/Capacitor), multiplataforma compilado (Flutter), multiplataforma interpretado (React Native) y Kotlin Multiplatform.
- El lenguaje **Dart** y, sobre todo, la **asincronía** (`Future`, `async`/`await`, `Stream`).
- Todo el desarrollo, las pruebas y el despliegue **con Flutter**.

## Señales en el material

En los apuntes, lo que viene de otro módulo aparece siempre en un cuadro así:

!!! info "Ya lo conoces (DI)"
    Ejemplo: "El `Scaffold` de Flutter es el mismo concepto que el de Compose: estructura base de pantalla con barra superior, cuerpo y botón flotante."
