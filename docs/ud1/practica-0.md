# Práctica guiada 0 · Del ordenador vacío a tu primera app

**Sesión 1 · 28 de septiembre** · No puntúa, pero es imprescindible para la A1.1.

## Qué vas a conseguir

Al terminar esta práctica tendrás todo instalado y verás **la misma página web diciendo WEB en el navegador y ANDROID en tu móvil**. Es tu primera app híbrida. Calcula entre 1 y 2 horas si partes de cero; Android Studio es lo que más tarda en descargarse.

| Herramienta | Versión | Para qué |
| --- | --- | --- |
| Node.js y npm | 24 LTS (mínimo 22.22) | Ejecutar las herramientas de Ionic y Capacitor |
| Git | La más reciente | Control de versiones y entregas por GitHub |
| Visual Studio Code | La más reciente | Editor de código |
| Ionic CLI | 7.x | Crear y gestionar proyectos Ionic |
| Android Studio | La más reciente | Compilar e instalar la app en Android (incluye Java y el SDK) |
| Móvil Android o emulador | Android 8 o superior | Probar la app |

!!! tip "Regla de oro"
    Copia y ejecuta **los comandos de uno en uno**. Pega uno, pulsa Enter, espera a que termine y pasa al siguiente. Si sale un error en rojo, para y mira [Si algo falla](#si-algo-falla).

## Paso 1 · Node.js

Node.js ejecuta las herramientas que usaremos (Ionic, Capacitor, Angular). Instala la versión **24 LTS**.

=== "Windows"

    1. Descarga el instalador **LTS** de [nodejs.org](https://nodejs.org) y ejecútalo con las opciones por defecto.
    2. Cierra y vuelve a abrir PowerShell.
    3. Si PowerShell no deja ejecutar `npm`, ejecuta una vez:

    ```powershell
    Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
    ```

=== "macOS y Ubuntu (con nvm)"

    `nvm` permite tener varias versiones de Node y evita problemas de permisos. Instala nvm:

    ```bash
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
    ```

    Cierra la Terminal, abre una nueva e instala Node 24:

    ```bash
    nvm install 24
    ```

    Déjalo como versión por defecto:

    ```bash
    nvm alias default 24
    ```

**Comprueba** (en cualquier sistema) que sale `v24.x`:

```bash
node -v
```

!!! warning "Nunca uses `sudo` con `npm`"
    Si te da errores de permisos en Mac o Linux, es porque Node no está instalado con nvm.

## Paso 2 · Git y Visual Studio Code

**Git**

- Windows: instala [Git for Windows](https://git-scm.com/download/win) con las opciones por defecto.
- macOS: ejecuta `git --version`; si no está, el sistema te ofrece instalar las herramientas de desarrollo. Acepta.
- Ubuntu: `sudo apt install git`

Comprueba:

```bash
git --version
```

Crea una cuenta en [GitHub](https://github.com) con **el correo del IES** si no la tienes. La usaremos a partir de la UD3.

**Visual Studio Code**

Descárgalo de [code.visualstudio.com](https://code.visualstudio.com) e instálalo. Después, en la pestaña *Extensiones*, instala:

- *Angular Language Service*
- *Ionic*
- *ESLint*

En macOS, abre VS Code, pulsa ⇧⌘P y ejecuta **Shell Command: Install 'code' command in PATH**. Así podrás abrir carpetas desde la Terminal con `code .`.

## Paso 3 · Ionic CLI

El Ionic CLI es la herramienta de terminal que crea y gestiona proyectos Ionic. Instálala de forma global:

```bash
npm install -g @ionic/cli
```

Verás avisos amarillos `npm warn deprecated`: son normales, ignóralos.

Comprueba que sale **7.x**:

```bash
ionic -v
```

| Comprobación | Debe salir |
| --- | --- |
| `node -v` | v24.x (mínimo v22.22) |
| `npm -v` | 10 u 11 |
| `git --version` | Un número |
| `ionic -v` | 7.x |

!!! note "¿`ionic -v` da 5.x o 6.x?"
    Tienes un Ionic antiguo que se usa antes que el nuevo. Mira [Si algo falla](#si-algo-falla).

## Paso 4 · Android Studio y emulador

Android Studio compila la app y la instala en el móvil. Incluye Java y el SDK de Android, así que no hace falta instalarlos aparte.

**Instalar**

1. Descarga Android Studio de [developer.android.com/studio](https://developer.android.com/studio). Pesa más de 1 GB.
    - macOS con Homebrew: `brew install --cask android-studio`
    - Ubuntu: `sudo snap install android-studio --classic`
2. Ábrelo y, en el asistente, elige **Standard**. Deja que descargue todo lo que propone.

**Configurar el SDK**

1. En la pantalla de bienvenida: **More Actions → SDK Manager**.
2. Pestaña *SDK Platforms*: marca la versión de Android más reciente.
3. Pestaña *SDK Tools*: marca **Android SDK Build-Tools**, **Android SDK Platform-Tools** y **Android Emulator**. Pulsa **Apply**.

**Crear un emulador** (si no tienes móvil Android, o como reserva)

1. **More Actions → Virtual Device Manager** (o *Device Manager* dentro de un proyecto).
2. **+ → Create Virtual Device**, elige un **Pixel** reciente → **Next**.
3. Elige la imagen de Android recomendada (descárgala si lo pide) → **Finish**.
4. Pulsa ▶ junto al emulador para arrancarlo. La primera vez tarda uno o dos minutos.

!!! warning "No actualices Gradle"
    Si Android Studio te propone **Project update recommended** o **AGP Upgrade Assistant**, **no actualices**: las versiones las fija Capacitor.

## Paso 5 · Preparar el móvil Android

La cámara, el GPS y los sensores se prueban mejor en un móvil real. Si no tienes Android, usa el emulador del paso 4.

1. *Ajustes → Información del teléfono* → pulsa **7 veces** sobre **Número de compilación**. Aparece «Ya eres desarrollador».
2. *Ajustes → Sistema → Opciones de desarrollador* → activa **Depuración USB**.
3. Conecta el móvil al ordenador con un **cable de datos**; muchos cables solo cargan.
4. Desbloquea el móvil y acepta **«¿Permitir depuración USB?»**, marcando *Permitir siempre desde este ordenador*.
5. En Android Studio, el móvil aparece en el desplegable de dispositivos de arriba.

La ruta exacta de los menús cambia según la marca (Samsung, Xiaomi…). Si no la encuentras, busca «número de compilación» en el buscador de Ajustes.

## Paso 6 · Tu primera app: de web a app

Vas a crear una web muy sencilla y convertirla en una app Android con **Capacitor**. La web detecta dónde se está ejecutando: en el navegador dice **WEB** y dentro de la app dice **ANDROID**.

### 6.1 · Crea la web

Crea en el Escritorio una carpeta `demo-hola-dam` con esta estructura (también puedes descargarla de Moodle):

```text
demo-hola-dam/
└── www/
    ├── index.html
    ├── css/estilos.css
    └── js/app.js
```

```html title="www/index.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>Hola DAM</title>
  <link rel="stylesheet" href="css/estilos.css">
</head>
<body>
  <main class="contenedor">
    <h1>Hola, 2º DAM</h1>
    <section class="tarjeta">
      <p>Estás viendo esta página en:</p>
      <p id="plataforma" class="plataforma">…</p>
    </section>
    <section class="tarjeta">
      <p>Has pulsado el botón <strong id="contador">0</strong> veces</p>
      <button id="btn-sumar" class="boton">Púlsame</button>
    </section>
  </main>
  <script src="js/app.js" defer></script>
</body>
</html>
```

```css title="www/css/estilos.css"
body { margin: 0; font-family: system-ui, sans-serif; background: #f1f5f9; }
.contenedor { max-width: 480px; margin: 0 auto; padding: 1.5rem 1rem; }
h1 { color: #1e3a8a; }
.tarjeta { background: #fff; border-radius: 12px; padding: 1rem; margin-bottom: 1rem; }
.plataforma { font-size: 2.5rem; font-weight: 700; color: #1e3a8a; margin: 0; }
.plataforma.nativa { color: #15803d; }
.boton { width: 100%; min-height: 48px; border: none; border-radius: 8px;
         background: #1e3a8a; color: #fff; font-size: 1.1rem; }
```

```js title="www/js/app.js"
// Dentro de una app de Capacitor existe window.Capacitor; en el navegador, no.
const plataforma = window.Capacitor?.getPlatform?.() ?? 'web';
const texto = document.querySelector('#plataforma');
texto.textContent = plataforma.toUpperCase();
texto.classList.toggle('nativa', plataforma !== 'web');

let pulsaciones = 0;
document.querySelector('#btn-sumar').addEventListener('click', () => {
  pulsaciones++;
  document.querySelector('#contador').textContent = pulsaciones;
});
```

Abre `www/index.html` con doble clic: debe decir **WEB**.

### 6.2 · Abre la Terminal en la carpeta del proyecto

```bash
cd ~/Desktop/demo-hola-dam
```

En Windows: `cd $HOME\Desktop\demo-hola-dam`. También puedes abrir la carpeta en VS Code y usar *Terminal → New Terminal*.

!!! danger "Muy importante"
    Todos los comandos siguientes se ejecutan en `demo-hola-dam`, **nunca dentro de `www`**. El prompt de la Terminal debe terminar en `demo-hola-dam`.

### 6.3 · Instala y configura Capacitor (uno a uno)

Crea el fichero de dependencias:

```bash
npm init -y
```

Instala Capacitor:

```bash
npm install @capacitor/core @capacitor/cli @capacitor/android
```

Configura el nombre de la app, su identificador y la carpeta de la web:

```bash
npx cap init "Hola DAM" es.iesrafaelalberti.holadam --web-dir www
```

### 6.4 · Crea el proyecto Android

```bash
npx cap add android
```

Ha aparecido una carpeta `android/`: es un proyecto completo de Android Studio.

### 6.5 · Ejecuta la app

Arranca antes el emulador (Device Manager → ▶) o conecta tu móvil. Después:

```bash
npx cap run android
```

Elige tu dispositivo con las flechas y pulsa Enter. La primera vez tarda un par de minutos. Se abre **Hola DAM** diciendo **ANDROID** en verde.

## Paso 7 · Cambia el código y vuelve a ejecutar

1. En `www/index.html` cambia `Hola, 2º DAM` por `Hola, [tu nombre]` y guarda.
2. Vuelve a ejecutar:

```bash
npx cap run android
```

El cambio aparece en la app. Este es el ciclo que usarás todo el curso: **editar en `www` → `npx cap run android`**.

!!! warning "Edita siempre `www/`"
    Dentro de `android/app/src/main/assets/public/` hay una **copia** que Capacitor sobrescribe en cada ejecución: si la editas, pierdes los cambios.

## Si algo falla

| Síntoma | Solución |
| --- | --- |
| `ionic` o `npm` «no se reconoce» | Cierra y abre la Terminal. En Windows, revisa que Node se instaló bien |
| PowerShell: *la ejecución de scripts está deshabilitada* | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| `node -v` da menos de 22.22 | `nvm install 24` y `nvm alias default 24`; después reinstala Ionic |
| `ionic -v` da 5.x o 6.x | `which -a ionic` para ver cuántos hay; borra el que no esté en `.nvm`. Si existe `~/node_modules`, muévela a otra carpeta. Luego `hash -r` |
| Errores de permisos (`EACCES`) con npm | No uses `sudo`: instala Node con nvm |
| *Could not find the web assets directory: ./www* | Estás dentro de `www`. Sal con `cd ..` |
| *npm error could not determine executable to run* | Estás en una carpeta sin Capacitor instalado. Ve a `demo-hola-dam` |
| *Could not read script … capacitor.settings.gradle* | `npx cap sync android` y en Android Studio **Try Again** |
| *proguard-android.txt is no longer supported* | En `android/app/build.gradle` cambia `proguard-android.txt` por `proguard-android-optimize.txt` y pulsa **Sync Now** |
| `npx cap run android` no ofrece ningún dispositivo | Arranca el emulador en Device Manager o conecta el móvil y acepta la depuración USB |
| El móvil no aparece | Desbloquéalo, acepta el aviso y prueba otro cable |
| En Android Studio pulsas ▶ y no pasa nada | Arriba debe estar seleccionada la configuración **app**, no *Tests in…* |
| Los cambios desaparecen | Estás editando la copia de `android/`. Edita `www/` |

Si el error no está aquí, copia el **mensaje completo** (texto, no una foto borrosa) y pásaselo al profesor, indicando en qué paso estabas. Más casos en [Problemas frecuentes](../recursos/problemas.md).

## Comprobación final y entrega

- [ ] `node -v` da v24.x (mínimo v22.22)
- [ ] `ionic -v` da 7.x
- [ ] `git --version` responde y tengo cuenta de GitHub con el correo del IES
- [ ] Android Studio abre y tiene un SDK instalado
- [ ] Tengo el móvil con depuración USB o un emulador que arranca
- [ ] La web dice **WEB** en el navegador
- [ ] La app dice **ANDROID** en el móvil o emulador
- [ ] He cambiado el título por mi nombre y lo veo en la app

**Entrega en Moodle:** dos capturas, la web en el navegador diciendo **WEB** y la app con tu nombre diciendo **ANDROID**. No subas ninguna carpeta.
