# Problemas frecuentes

??? failure "`ionic` no se reconoce como comando"
    Cierra y vuelve a abrir la terminal. Si sigue igual, reinstala con `npm install -g @ionic/cli`. En Windows comprueba que la carpeta de npm global está en el `PATH`.

??? failure "`ionic -v` muestra una versión antigua (5.x o 6.x) aunque acabas de instalar la 7"
    Hay otro Ionic que se usa antes que el nuevo. Comprueba:

    - `which -a ionic`: si aparece `/usr/local/bin/ionic` además del de `.nvm`, bórralo con `sudo rm /usr/local/bin/ionic`.
    - `ls ~/node_modules` y `ls ~/package.json`: si existen en tu carpeta personal, alguien instaló Ionic ahí por error. Muévelos a otra carpeta. Ionic usa la copia que encuentra en la carpeta actual o en las superiores.
    - Ejecuta `hash -r` o abre una terminal nueva.

??? failure "Node demasiado antiguo"
    Angular 22 necesita Node 22.22 o superior. Con `nvm`: `nvm install 24` y después `nvm alias default 24`. Vuelve a instalar el Ionic CLI, porque cada versión de Node tiene sus propios paquetes globales.

??? failure "PowerShell: *la ejecución de scripts está deshabilitada*"
    Ejecuta una vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y abre otra terminal.

??? failure "Un componente de Ionic no aparece y la consola dice *is not a known element*"
    Falta importarlo en el array `imports` del componente, desde `@ionic/angular`. Ejemplo: si usas `<ion-list>`, añade `IonList`.

??? failure "Error *Cannot find module '@ionic/angular/standalone'* o componentes que no se ven tras copiar código"
    El código es de Ionic 8. En Ionic 9 los componentes se importan de `@ionic/angular`. Cambia la ruta del `import`.

??? failure "El icono no se ve"
    Regístralo con `addIcons({ nombreIcono })` importándolo de `ionicons/icons`.

??? failure "La pantalla no se actualiza al recibir datos del GPS o de un sensor"
    Guarda el dato en un **signal** (`this.posicion.set(pos)`) en lugar de en una propiedad normal.

??? failure "Olvidé los paréntesis del signal"
    En la plantilla aparece `[Function]` o algo raro: escribe `contador()` en lugar de `contador`.

??? failure "Cambio el código pero en el móvil sigue la versión antigua"
    Tienes que volver a compilar y sincronizar: `ionic build` y después `npx cap sync android`. O usa `ionic cap run android -l --external` para recarga en vivo.

??? failure "Android Studio: *Gradle sync failed* o *SDK location not found*"
    Abre *SDK Manager* e instala el SDK. Si el error menciona la versión de Java, en *Settings → Build Tools → Gradle* elige el JDK que trae Android Studio (*jbr*).

??? failure "Android Studio: *getDefaultProguardFile('proguard-android.txt') is no longer supported*"
    En `android/app/build.gradle` cambia `proguard-android.txt` por `proguard-android-optimize.txt` y pulsa **Sync Now**. Desde la Terminal, en la carpeta del proyecto (macOS): `sed -i '' 's/proguard-android.txt/proguard-android-optimize.txt/' android/app/build.gradle`. Para que no vuelva a pasar, **no aceptes** el *AGP Upgrade Assistant* que ofrece Android Studio.

??? failure "Android Studio: *Could not read script … capacitor.settings.gradle*"
    Falta sincronizar. En la carpeta del proyecto ejecuta `npx cap sync android` y en Android Studio pulsa **Try Again**.

??? failure "*Could not find the web assets directory: ./www* o *npm error could not determine executable to run*"
    Estás en la carpeta equivocada. Los comandos `npx cap …` se ejecutan en la carpeta donde están `package.json` y `capacitor.config.json`, **nunca dentro de `www`**.

??? failure "El móvil no aparece en Android Studio"
    Activa la depuración USB, acepta el aviso en el móvil y prueba otro cable (muchos solo cargan). En Windows puede hacer falta el driver USB del fabricante.

??? failure "*blocked by CORS policy*"
    El servidor no permite peticiones desde tu app. Configura CORS en la API (Spring Boot: `@CrossOrigin` o `CorsConfigurationSource`) permitiendo `http://localhost:8100`, `https://localhost` y `capacitor://localhost`.

??? failure "La primera petición a Render tarda muchísimo"
    El plan gratuito de Render se duerme. Espera o haz una petición previa para despertarlo. Muestra un indicador de carga.

??? failure "El GPS no funciona en el móvil"
    Revisa los permisos en `AndroidManifest.xml`, que la ubicación del móvil esté activada y que llamas a `requestPermissions()`. Mira la consola en `chrome://inspect`.

??? failure "Firestore: *Missing or insufficient permissions*"
    Las reglas de seguridad no permiten la operación. Revísalas en la consola de Firebase. En modo de prueba caducan a los 30 días.

??? failure "Cypress no encuentra un elemento de Ionic"
    Añade `includeShadowDom: true` en `cypress.config.ts` y usa atributos `data-cy`.

??? failure "`npm install` falla con *ERESOLVE unable to resolve dependency tree*"
    Hay versiones incompatibles. Usa las versiones del `package.json` del curso. Como último recurso, `npm install --legacy-peer-deps`.

## Cómo pedir ayuda

Cuando preguntes (al profesor, a un compañero o a una IA), incluye siempre:

1. qué intentabas hacer;
2. el **mensaje de error completo** (texto, no foto borrosa);
3. dónde aparece: terminal, consola del navegador, `chrome://inspect` o Logcat;
4. qué has probado ya.
