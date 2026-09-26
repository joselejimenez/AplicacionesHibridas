# Demo «Hola DAM» · De web a app

Demo de la [sesión 1](sesion-1.md) (17:55). Los ficheros están también en `materiales-docente/sesion-1/demo-hola-dam/`.

Qué enseña: **el mismo HTML, CSS y JS** se ve en el navegador y dentro de una app Android instalada. En el navegador la página dice **WEB** y en el móvil dice **ANDROID**.

## Antes de clase (hazlo una vez en casa)

Ejecuta los pasos 1 a 8 completos en tu Mac para que Android Studio descargue Gradle y las dependencias. La primera vez tarda 5–10 minutos. En clase ya irá rápido.

## Pasos (uno por línea)

Entra en la carpeta de la demo:

    cd ~/Desktop/demo-hola-dam

1. Ver primero la web en el navegador: abre `www/index.html` con doble clic. Debe decir **WEB**.

2. Crear el `package.json`:

        npm init -y

3. Instalar Capacitor:

        npm install @capacitor/core @capacitor/cli @capacitor/android

4. Configurar Capacitor (nombre de la app, identificador y carpeta de la web):

        npx cap init "Hola DAM" es.iesrafaelalberti.holadam --web-dir www

5. Crear el proyecto Android:

        npx cap add android

6. Sincronizar (copia la web al proyecto Android y genera los ficheros de Gradle):

        npx cap sync android

7. Abrir Android Studio:

        npx cap open android

8. En Android Studio: espera a que termine *Gradle sync* (barra inferior), elige tu móvil en el desplegable de arriba y pulsa ▶ **Run**. La app se instala y dice **ANDROID**.

!!! tip "Atajo recomendado: un solo comando"
    En lugar de los pasos 7 y 8 puedes ejecutar `npx cap run android`. Sincroniza, compila, te pregunta en qué dispositivo instalar (móvil o emulador ya arrancado) y abre la app. En el emulador, arráncalo antes desde *Device Manager* (▶ junto a su nombre).

## Cambiar algo en directo

Edita `www/index.html` (por ejemplo, el título), guarda y ejecuta:

    npx cap sync android

Vuelve a pulsar ▶ **Run** en Android Studio, o ejecuta de nuevo `npx cap run android`.

## Si algo falla

!!! warning "No actualices Gradle"
    Si Android Studio propone *Project update recommended* o *Start AGP Upgrade Assistant*, ciérralo. Las versiones las fija Capacitor.

| Síntoma | Solución |
|---|---|
| `npx cap add android` falla por la versión de Node | `node -v` debe ser 22.22 o superior (tienes 24) |
| *Could not read script … capacitor.settings.gradle* | Falta sincronizar: `npx cap sync android` y en Android Studio **Try Again** |
| *getDefaultProguardFile('proguard-android.txt') is no longer supported* | En `android/app/build.gradle` cambia `proguard-android.txt` por `proguard-android-optimize.txt` y pulsa **Sync Now**. No aceptes el *AGP Upgrade Assistant* |
| *Gradle sync failed* | En Android Studio: *Settings → Build Tools → Gradle → Gradle JDK* → elige el JDK que trae Android Studio (*jbr*) |
| El móvil no aparece | Desbloquéalo, acepta «Permitir depuración USB» y prueba otro cable |
| Sin móvil | Usa el emulador de *Device Manager* |
| Pulsas ▶ y no pasa nada | Comprueba que arriba está seleccionada la configuración **app** (no *Tests in…*) o usa `npx cap run android` |

## Código de la demo

Crea una carpeta `demo-hola-dam` con esta estructura (o copia la del zip):

```text
demo-hola-dam/
└── www/
    ├── index.html
    ├── css/estilos.css
    └── js/app.js
```

??? example "www/index.html"

    ```html
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
        <p class="subtitulo">Desarrollo de Aplicaciones Híbridas · IES Rafael Alberti</p>

        <section class="tarjeta">
          <p>Estás viendo esta página en:</p>
          <p id="plataforma" class="plataforma">…</p>
          <p id="explicacion" class="nota"></p>
        </section>

        <section class="tarjeta">
          <p>Has pulsado el botón <strong id="contador">0</strong> veces</p>
          <button id="btn-sumar" class="boton">Púlsame</button>
        </section>
      </main>

      <script src="js/app.js"></script>
    </body>
    </html>
    ```

??? example "www/css/estilos.css"

    ```css
    /* Mobile-first: estilos base pensados para el móvil */
    :root {
      --azul: #1e3a8a;
      --amarillo: #facc15;
      --fondo: #f1f5f9;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      background: var(--fondo);
      color: #0f172a;
      /* respeta la zona de la cámara y la barra del sistema */
      padding: env(safe-area-inset-top) 0 env(safe-area-inset-bottom);
    }

    .contenedor {
      max-width: 480px;
      margin: 0 auto;
      padding: 1.5rem 1rem;
    }

    h1 {
      color: var(--azul);
      font-size: 2rem;
      margin: 0 0 .25rem;
    }

    .subtitulo { color: #475569; margin: 0 0 1.5rem; }

    .tarjeta {
      background: #fff;
      border-radius: 12px;
      padding: 1rem 1.25rem;
      margin-bottom: 1rem;
      box-shadow: 0 1px 3px rgb(0 0 0 / .1);
    }

    .plataforma {
      font-size: 2.5rem;
      font-weight: 700;
      margin: .25rem 0;
      color: var(--azul);
    }

    .plataforma.nativa { color: #15803d; }

    .nota { color: #475569; font-size: .95rem; }

    .boton {
      width: 100%;
      min-height: 48px;           /* zona táctil cómoda */
      border: none;
      border-radius: 8px;
      background: var(--azul);
      color: #fff;
      font-size: 1.1rem;
      cursor: pointer;
    }

    .boton:active { background: #172554; }

    /* Pantallas grandes */
    @media (min-width: 768px) {
      h1 { font-size: 2.75rem; }
    }
    ```

??? example "www/js/app.js"

    ```js
    // Cuando la página se ejecuta dentro de una app de Capacitor, el puente nativo
    // crea un objeto global window.Capacitor. En el navegador ese objeto no existe.
    const plataforma = window.Capacitor?.getPlatform?.() ?? 'web';
    const esNativa = plataforma !== 'web';

    const textoPlataforma = document.querySelector('#plataforma');
    const explicacion = document.querySelector('#explicacion');

    textoPlataforma.textContent = plataforma.toUpperCase();
    textoPlataforma.classList.toggle('nativa', esNativa);
    explicacion.textContent = esNativa
      ? 'El mismo HTML, CSS y JS se está ejecutando dentro de una app instalada, con acceso al puente nativo de Capacitor.'
      : 'Es una web normal en el navegador. Instálala como app con Capacitor y este texto cambiará.';

    // Contador: el mismo código funciona igual en web y en la app
    let pulsaciones = 0;
    const contador = document.querySelector('#contador');
    document.querySelector('#btn-sumar').addEventListener('click', () => {
      pulsaciones++;
      contador.textContent = pulsaciones;
    });
    ```
