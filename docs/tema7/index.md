# Tema 7 · Despliegue y distribución

!!! abstract "Ficha del tema"
    - **Duración:** 2 sesiones (25 de enero y 1 de febrero)
    - **RA:** RA3 · CE d (preparar y empaquetar para diferentes plataformas y tiendas) · CE e (documentar desarrollo, pruebas y despliegue)
    - **Actividades:** [9 ejercicios rápidos de clase](#ejercicios-rapidos) · 2 guiados · [Boletín de 8 ejercicios](#boletin-de-ejercicios) · [Práctica 7.1 · Cádiz Market en producción](#practica-71-cadiz-market-en-produccion)

| Sesión | Contenido | En clase |
|---|---|---|
| **1 · 25 ene** | Identidad de la app, iconos y *splash*, firma de Android, `flutter build` para cada plataforma, tamaño y ofuscación | Rápidos R1-R5 · Guiado G1 · Boletín B1-B5 |
| **2 · 1 feb** | Publicar la versión web, canales de distribución, integración continua con GitHub Actions, documentación y mantenimiento | Rápidos R6-R9 · Guiado G2 · Boletín B6-B8 · Práctica 7.1 |

---

## 1. Identidad de la app

| Qué | Dónde se cambia |
|---|---|
| Versión | `pubspec.yaml` → `version: 1.2.0+5` (versión visible `1.2.0` + número de build `5`, que **debe subir** en cada publicación) |
| Nombre visible en Android | `android/app/src/main/AndroidManifest.xml` → `android:label="Cádiz Market"` |
| Nombre visible en iOS | `ios/Runner/Info.plist` → `CFBundleDisplayName` |
| Identificador (Android) | `android/app/build.gradle.kts` → `applicationId = "es.iesrafaelalberti.cadiz_market"`. **No se puede cambiar** una vez publicada |
| Título en web | `web/index.html` y `web/manifest.json` |

!!! tip "Versionado semántico"
    `MAYOR.MENOR.PARCHE`: parche para corregir errores (1.0.1), menor para funciones nuevas compatibles (1.1.0), mayor para cambios que rompen (2.0.0).

### Icono y pantalla de carga

Con dos paquetes de desarrollo que generan todos los tamaños automáticamente:

```bash
flutter pub add dev:flutter_launcher_icons dev:flutter_native_splash
```

Al final de `pubspec.yaml` (el icono, un PNG cuadrado de 1024×1024):

```yaml
flutter_launcher_icons:
  android: true
  ios: true
  image_path: "assets/icono/icono.png"
  web:
    generate: true
  windows:
    generate: true
  macos:
    generate: true

flutter_native_splash:
  color: "#3F51B5"
  image: assets/icono/icono.png
```

Genera los iconos:

```bash
dart run flutter_launcher_icons
```

Genera la pantalla de carga:

```bash
dart run flutter_native_splash:create
```

!!! example "G1 · Guiado en clase: tu app con identidad"
    Sobre Cádiz Market: versión `1.0.0+1`, nombre «Cádiz Market», identificador `es.iesrafaelalberti.cadiz_market`, icono propio y *splash* con el color del tema. Instaladla en el móvil y buscadla en el cajón de apps.

---

## 2. Android: firmar y compilar

Google Play solo acepta apps **firmadas** con una clave tuya. Esa clave identifica al autor: **si la pierdes, no podrás actualizar la app nunca más.**

### Paso 1 · Crear la clave (una vez)

`keytool` viene con el JDK de Android Studio. En macOS o Linux:

```bash
keytool -genkey -v -keystore ~/upload-keystore.jks -keyalg RSA -keysize 2048 -validity 10000 -alias upload
```

En Windows (PowerShell):

```powershell
keytool -genkey -v -keystore $env:USERPROFILE\upload-keystore.jks -storetype JKS -keyalg RSA -keysize 2048 -validity 10000 -alias upload
```

!!! note "Si `keytool` no se reconoce"
    Ejecuta `flutter doctor -v`: en la sección de Android te dice la ruta del Java de Android Studio. `keytool` está en su carpeta `bin`.

### Paso 2 · `android/key.properties`

Crea este fichero (con tus datos):

```properties
storePassword=la_contraseña_que_elegiste
keyPassword=la_contraseña_que_elegiste
keyAlias=upload
storeFile=/Users/tu_usuario/upload-keystore.jks
```

!!! danger "Nunca subas la clave ni `key.properties` a GitHub"
    Añade al `.gitignore` del proyecto:

    ```text
    android/key.properties
    *.jks
    ```

### Paso 3 · Usar la clave en `android/app/build.gradle.kts`

Al principio del fichero:

```kotlin
import java.util.Properties
import java.io.FileInputStream

val keystoreProperties = Properties()
val keystorePropertiesFile = rootProject.file("key.properties")
if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(FileInputStream(keystorePropertiesFile))
}
```

Dentro del bloque `android { ... }`, añade `signingConfigs` y cambia la firma del `release`:

```kotlin
    signingConfigs {
        create("release") {
            keyAlias = keystoreProperties["keyAlias"] as String
            keyPassword = keystoreProperties["keyPassword"] as String
            storeFile = keystoreProperties["storeFile"]?.let { file(it) }
            storePassword = keystoreProperties["storePassword"] as String
        }
    }

    buildTypes {
        release {
            signingConfig = signingConfigs.getByName("release")
        }
    }
```

!!! info "Ya lo conoces (DI)"
    Es Gradle con Kotlin DSL, como en vuestros proyectos de Compose.

### Paso 4 · Compilar

| Comando | Genera | Para qué |
|---|---|---|
| `flutter build apk` | `build/app/outputs/flutter-apk/app-release.apk` | Instalar directamente o distribuir fuera de Play |
| `flutter build apk --split-per-abi` | Un APK por arquitectura (más pequeños) | Distribución directa |
| `flutter build appbundle` | `build/app/outputs/bundle/release/app-release.aab` | **Lo que se sube a Google Play** |

Instalar el APK en el móvil conectado:

```bash
flutter install
```

**Reducir y proteger el código** (ofuscación):

```bash
flutter build appbundle --obfuscate --split-debug-info=build/simbolos
```

**Analizar el tamaño:**

```bash
flutter build apk --analyze-size
```

---

## 3. Las demás plataformas

| Plataforma | Comando | Resultado | Requisitos |
|---|---|---|---|
| **Web** | `flutter build web` | `build/web/`: ficheros estáticos para cualquier servidor | Ninguno |
| **Windows** | `flutter build windows` | `build/windows/x64/runner/Release/` (el `.exe` con sus DLL) | Windows + Visual Studio |
| **macOS** | `flutter build macos` | `build/macos/Build/Products/Release/*.app` | Mac + Xcode |
| **Linux** | `flutter build linux` | `build/linux/x64/release/bundle/` | Linux + dependencias del Tema 1 |
| **iOS** | `flutter build ipa` | Paquete para App Store Connect | Mac + Xcode + cuenta de desarrollador de Apple |

!!! warning "Web publicada en una subcarpeta"
    Si la web no va a estar en la raíz del dominio (por ejemplo `usuario.github.io/cadiz_market/`), hay que indicarlo al compilar, con la barra al principio y al final:

    ```bash
    flutter build web --base-href /cadiz_market/
    ```

---

## 4. Publicar la versión web

### Opción A · GitHub Pages con GitHub Actions

Cada `push` a `main` compila y publica la web automáticamente. Crea `.github/workflows/web.yml` en el repositorio de tu app:

```yaml
name: Publicar web

on:
  push:
    branches:
      - main

permissions:
  contents: write

jobs:
  web:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
        with:
          channel: stable
      - run: flutter pub get
      - run: flutter test
      - run: flutter build web --release --base-href /cadiz_market/
      - uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: build/web
```

Después, en GitHub: **Settings → Pages → Deploy from a branch → `gh-pages`**. Es lo mismo que hicimos con la web del curso.

### Opción B · Firebase Hosting

Si ya usas Firebase (Tema 5), desde la carpeta del proyecto:

```bash
firebase init hosting
```

Indica `build/web` como carpeta pública y responde **sí** a «configure as a single-page app». Después:

```bash
flutter build web
```

```bash
firebase deploy --only hosting
```

Te da una URL `https://<proyecto>.web.app`.

!!! example "G2 · Guiado en clase: Cádiz Market en Internet"
    Cada uno publica su Cádiz Market en GitHub Pages con el workflow del apartado. Al terminar, compartid las URL y abrid la de un compañero en el móvil.

---

## 5. Canales de distribución

| Canal | Plataforma | Coste | Qué se sube | A tener en cuenta |
|---|---|---|---|---|
| **Google Play** | Android | Pago único de 25 USD | AAB firmado | Ficha con capturas, política de privacidad y clasificación de contenido. Las cuentas personales nuevas deben pasar una **prueba cerrada** con testers durante un tiempo mínimo antes de publicar (consulta la política vigente) |
| **App Store** | iOS, macOS | 99 USD al año | IPA desde Xcode | Requiere Mac. Revisión manual de Apple |
| **Microsoft Store** | Windows | Cuenta de desarrollador | Paquete MSIX (paquete `msix` de pub.dev) | |
| **Snap Store / Flathub** | Linux | Gratis | Snap / Flatpak | |
| **Web** | Cualquiera | Gratis (GitHub Pages, Firebase Hosting) | `build/web` | Sin revisión ni tienda. Puede instalarse como PWA |
| **Distribución directa** | Android | Gratis | APK | El usuario debe permitir «orígenes desconocidos». Útil para apps internas |
| **Firebase App Distribution / TestFlight** | Android / iOS | Gratis | APK/AAB / IPA | Para **probadores** antes de publicar |

---

## 6. Integración continua

La integración continua (CI) ejecuta automáticamente el análisis, los tests y la compilación **en cada `push`**. Si alguien sube código que rompe un test, GitHub lo marca en rojo.

`.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  calidad:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: subosito/flutter-action@v2
        with:
          channel: stable
      - run: flutter pub get
      - run: flutter analyze
      - run: flutter test --coverage
      - run: flutter build apk --debug
      - uses: actions/upload-artifact@v4
        with:
          name: apk-debug
          path: build/app/outputs/flutter-apk/app-debug.apk
```

El APK queda descargable en la ejecución del workflow (pestaña **Actions** → la ejecución → **Artifacts**).

!!! tip "Insignia en el README"
    GitHub genera una insignia de estado: en la pestaña Actions, abre el workflow → **⋯ → Create status badge** y pega el código en el README.

---

## 7. Documentación y mantenimiento

### El README de una app

```markdown
# Cádiz Market

![CI](enlace-a-la-insignia)

Tienda de productos gaditanos hecha con Flutter. [Probar la versión web](https://usuario.github.io/cadiz_market/)

## Capturas
(capturas en móvil y en escritorio)

## Funcionalidades
- Catálogo con búsqueda y filtros
- Carrito persistente
- ...

## Arquitectura
Estructura de carpetas (modelos, servicios, pantallas, widgets) y gestión de estado con provider.

## Instalación y ejecución
flutter pub get / flutter run

## Tests
flutter test / flutter test integration_test

## Descargas
Enlace al APK de la última versión (GitHub Releases).

## Autoría y licencia
```

### Documentar el código

Los comentarios con **tres barras** son documentación y aparecen al pasar el ratón en el editor:

```dart
/// Carrito de la compra compartido por toda la app.
///
/// Notifica a los oyentes cada vez que cambia su contenido.
class Carrito extends ChangeNotifier { ... }
```

Generar la documentación HTML de todo el proyecto:

```bash
dart doc
```

### Publicar versiones: GitHub Releases

En GitHub: **Releases → Draft a new release** → etiqueta `v1.0.0` → adjunta el APK → describe los cambios. Es la forma estándar de distribuir el APK de un proyecto.

### Mantener las dependencias

Ver qué paquetes tienen versiones nuevas:

```bash
flutter pub outdated
```

Actualizarlos dentro de lo que permite el `pubspec.yaml`:

```bash
flutter pub upgrade
```

Lleva un `CHANGELOG.md` con los cambios de cada versión.

---

## Ejercicios rápidos de clase { #ejercicios-rapidos }

Cortos (5-15 minutos). Se hacen **en clase**, justo después de explicar cada apartado, y se corrigen en voz alta. No se entregan: son el entrenamiento para el boletín y las prácticas.

### Sesión 1 · 25 ene

| # | Ejercicio | Apartado |
|---|---|---|
| R1 | **Versión visible.** Cambia la versión a `0.9.0+3` y muéstrala en «Acerca de» con el paquete `package_info_plus` | 1 |
| R2 | **Mi nombre en el móvil.** Cambia el nombre visible de la app en Android y en web y compruébalo en el cajón de apps y en la pestaña del navegador | 1 |
| R3 | **APK al móvil.** `flutter build apk` y `flutter install` en tu móvil. Desinstala la versión de debug antes | 2 |
| R4 | **Web en local.** `flutter build web` y sírvela con `python3 -m http.server 8000` desde `build/web`. Ábrela desde el móvil con la IP de tu ordenador | 3 |
| R5 | **Debug frente a release.** Compara el tamaño del APK de debug con el de release. ¿A qué se debe la diferencia? | 2 |

### Sesión 2 · 1 feb

| # | Ejercicio | Apartado |
|---|---|---|
| R6 | **CI mínimo.** Un workflow que solo ejecute `flutter analyze`. Haz *push* y consigue el check verde | 6 |
| R7 | **Primera release.** Crea en GitHub la release `v0.1.0` de un ejercicio con su APK adjunto | 7 |
| R8 | **Documenta.** Escribe comentarios `///` en 3 clases, ejecuta `dart doc` y abre el HTML generado | 7 |
| R9 | **¿Qué está viejo?** Ejecuta `flutter pub outdated` en Mis lugares e interpreta las columnas *Current*, *Upgradable* y *Latest* | 7 |

---

## Boletín de ejercicios { #boletin-de-ejercicios }

!!! abstract "Instrucciones"
    - **Individual.** Sobre tus proyectos anteriores (indica cuál en cada ejercicio).
    - **Entrega:** documento con enlaces y capturas · **Fecha:** domingo 7 de febrero.

| # | Ejercicio | Practica |
|---|---|---|
| B1 | **Identidad.** Cambia nombre, identificador y versión de la app «Hola, Carnaval» (Tema 1). Genera icono y *splash* propios | Identidad, iconos |
| B2 | **APK por arquitecturas.** Genera el APK normal y con `--split-per-abi`. Tabla de tamaños y explicación de la diferencia | `flutter build apk` |
| B3 | **Firma.** Crea tu clave, configura la firma y genera el AAB de Cádiz Market. Demuestra con una captura del `.gitignore` que la clave no está en el repositorio | Firma de Android |
| B4 | **Análisis de tamaño.** `--analyze-size` sobre Mis lugares. ¿Qué tres elementos ocupan más? Propón cómo reducir uno | Tamaño |
| B5 | **Escritorio.** Compila una de tus apps para tu sistema de escritorio (Windows, macOS o Linux) y comprime la carpeta resultante para que otro la pueda ejecutar | `flutter build <escritorio>` |
| B6 | **Web publicada.** Publica «Hola, Carnaval» en GitHub Pages **o** Firebase Hosting | Despliegue web |
| B7 | **CI.** Añade el workflow de CI a Cádiz Market, provoca un fallo en un test, haz *push* y captura la ejecución en rojo; arréglalo y captura la verde. Añade la insignia al README | GitHub Actions |
| B8 | **Ficha de tienda.** Redacta la ficha de Google Play de Cádiz Market: descripción corta (80 caracteres) y larga, 4 capturas, icono, categoría, clasificación de contenido y un borrador de política de privacidad | Canales de distribución |

---

## Práctica 7.1 · Cádiz Market en producción { #practica-71-cadiz-market-en-produccion }

!!! abstract "Datos de la entrega"
    - **Individual** · **RA3 · CE d, e**
    - **Entrega:** URL del repositorio y de la web publicada · **Fecha:** domingo 7 de febrero

Lleva tu Cádiz Market (Temas 3, 5 y 6) a producción:

1. Versión `1.0.0`, nombre, identificador, icono y *splash* propios.
2. **AAB y APK firmados** con tu clave (sin la clave en el repositorio).
3. **Web publicada** automáticamente con GitHub Actions.
4. **CI** con análisis, tests y APK de *debug* como artefacto.
5. **GitHub Release** `v1.0.0` con el APK firmado adjunto.
6. **Una tercera plataforma**: la versión de escritorio de tu sistema, adjunta también a la release.
7. **README** completo según el modelo del apartado 7, con insignia de CI y enlace a la web.
8. **CHANGELOG.md** con al menos las versiones 0.1.0 (Tema 3), 0.2.0 (Tema 5), 0.3.0 (Tema 6) y 1.0.0.

| Criterio | Peso |
|---|---|
| Android firmado (AAB y APK) sin exponer la clave | 25 % |
| Web publicada automáticamente | 20 % |
| CI funcionando | 20 % |
| Release con dos plataformas | 15 % |
| README, CHANGELOG y documentación del código | 20 % |
