# Sesión 1 paso a paso · Lunes 28 de septiembre

**15:30–18:30 · UD1 · RA1 a** · Objetivo: que el alumnado entienda qué es una app híbrida, tenga el entorno funcionando (o sepa qué le falta) y vea una web convertida en app en un móvil real.

!!! abstract "La sesión en una frase"
    Empiezan preguntándose «¿qué es una app híbrida?» y se van a casa habiendo visto **la misma página diciendo WEB en el navegador y ANDROID en el móvil**.

!!! warning "Plan actualizado (26 sep)"
    **No hay evaluación inicial** y el alumnado **ya tiene Android Studio instalado**. El horario queda así:

    | Hora | Min | Bloque |
    |---|---|---|
    | 15:30 | 20 | Presentación del módulo |
    | 15:50 | 30 | Tipos de app y dinámica por parejas |
    | 16:20 | 20 | Cómo funciona una híbrida |
    | 16:40 | 20 | Comprobar el entorno (Node, Ionic, móvil o emulador) |
    | 17:00 | 10 | Pausa |
    | 17:10 | 45 | **Práctica guiada: cada alumno sigue la [Práctica guiada 0](../ud1/practica-0.md) desde el paso 6** |
    | 17:55 | 25 | A1.1 en clase |
    | 18:20 | 10 | Cierre y deberes |

    Los bloques de abajo siguen valiendo como guion; ignora los de evaluación inicial e instalación.

## Resumen del horario

| Hora | Min | Bloque | Qué haces tú | Qué hacen ellos |
|---|---|---|---|---|
| 15:30 | 5 | Arranque | Pides que **lancen ya la descarga de Android Studio** | Descargan mientras escuchan |
| 15:35 | 15 | Presentación del módulo | Proyectas el sitio: inicio, calendario, evaluación, normas | Escuchan y preguntan |
| 15:50 | 20 | Evaluación inicial | Abres el cuestionario en Moodle | Lo responden |
| 16:10 | 30 | Tipos de app | Explicas la tabla y lanzas la dinámica por parejas | Debaten el caso y lo ponen en común |
| 16:40 | 20 | Cómo funciona una híbrida | Explicas WebView + puente + plugins | Preguntas rápidas |
| 17:00 | 10 | **Pausa** | | |
| 17:10 | 45 | Puesta en marcha del entorno | Guías la instalación y resuelves bloqueos | Rellenan la hoja de comprobación |
| 17:55 | 20 | Demo: de web a app | Haces la demo «Hola DAM» en directo | Miran y, quien tenga el entorno, la repite |
| 18:15 | 15 | Actividad y cierre | Presentas A1.1 y lo que queda para casa | Empiezan A1.1 |

## Antes del lunes

### Imprescindible

- [ ] **Hacer tú la demo completa en tu Mac** siguiendo la página [Demo Hola DAM](demo-hola-dam.md), con tu móvil. La primera vez Android Studio descarga Gradle (5–10 min); el lunes ya irá rápido.
- [ ] **Importar el cuestionario** `evaluacion-inicial.gift.txt` en Moodle (*Banco de preguntas → Importar → Formato GIFT*) y crear un cuestionario con esas 18 preguntas, sin calificación y con un único intento.
- [ ] **Preguntar en el centro qué tienen los PC del aula:** Node, Android Studio, Git y si los alumnos tienen permisos para instalar. Esto decide cómo va el bloque de las 17:10 (ver [plan A y B](#1710-puesta-en-marcha-del-entorno-45-min)).
- [ ] **Imprimir la hoja de comprobación** (`hoja-comprobacion-entorno.md`), una por alumno, o subirla a Moodle.
- [ ] **Tener abierto el sitio del curso** con `mkdocs serve` para proyectarlo.

### Recomendable

- [ ] 2 o 3 **cables USB de datos** de repuesto (USB-C y micro-USB).
- [ ] 1 o 2 **móviles Android de préstamo** con depuración USB ya activada.
- [ ] Instalar [`scrcpy`](https://github.com/Genymobile/scrcpy) en tu Mac (`brew install scrcpy`) para **proyectar la pantalla de tu móvil**. Es lo que hace que la demo impacte.
- [ ] Revisar la [solución de A1.1](#solucion-de-a11) para tenerla a mano si preguntan.

### Qué llevar abierto en tu Mac

1. El sitio del curso (`http://127.0.0.1:8000`) en una pestaña.
2. Moodle con el cuestionario.
3. La carpeta `demo-hola-dam` en VS Code y una Terminal dentro de ella.
4. Android Studio abierto (el proyecto de la demo ya compilado una vez).
5. Tu móvil conectado y `scrcpy` listo.

---

## 15:30 · Arranque (5 min)

Lo primero, antes de presentarte en detalle:

> «Antes de nada, abrid el navegador y empezad a descargar Android Studio desde developer.android.com/studio. Pesa más de 1 GB y lo vamos a necesitar dentro de hora y media. Si estáis en los PC del aula, esperad un momento, que os digo si ya está instalado.»

Así la descarga avanza mientras explicas.

## 15:35 · Presentación del módulo (15 min)

Proyecta el sitio y recorre estas páginas **sin detenerte demasiado** (todo está escrito y lo pueden releer):

1. **[Inicio](../index.md):** «Al final del curso sabréis hacer una app que funciona en Android, iOS y web, que usa la cámara, el GPS y los sensores, y que guarda datos en el móvil y en la nube». Enseña la tabla de las cuatro capas con la analogía: *materiales, esqueleto, ropa y manos*.
2. **[Calendario](../curso/calendario.md):** un lunes a la semana, 15 sesiones, la FFEOE empieza el 16 de febrero, prueba el 21 de diciembre y defensa del proyecto el 15 de febrero.
3. **[Evaluación](../curso/evaluacion.md):** tres RA (20 %, 40 %, 40 %) y **hay que aprobar los tres**.
4. **[Cómo funciona el curso](../curso/funcionamiento.md):** entregas, GitHub desde la UD3, **móvil obligatorio** y las tres reglas de la IA.

!!! tip "Frase clave para la IA"
    «Podéis usar IA y en algunas prácticas os lo voy a pedir. Pero todo lo que entreguéis lo tenéis que saber explicar, porque en la prueba y en la defensa no hay IA.»

## 15:50 · Evaluación inicial (20 min)

- Comparte el enlace de Moodle. Son 18 preguntas y **no cuentan para la nota**.
- Mientras responden, **pasea por el aula** y fíjate en quién tiene portátil propio y qué sistema usa.
- Al terminar, mira los resultados de EI01 y EI02: te dicen cuántos móviles Android y qué sistemas tienes. Úsalo para el bloque del entorno.

## 16:10 · Tipos de aplicaciones (30 min)

Usa la [UD1, apartado 1](../ud1/index.md#1-tipos-de-aplicaciones-moviles).

**Explicación (15 min).** Recorre la tabla de cinco tipos con un ejemplo que conozcan de cada uno:

| Tipo | Pregunta para el grupo |
|---|---|
| Nativa | «¿Qué app de vuestro móvil creéis que está hecha así? ¿Por qué?» (WhatsApp, la del banco) |
| Web | «¿Usáis Gmail desde el navegador del móvil?» |
| PWA | «¿Alguien ha instalado una web en la pantalla de inicio?» |
| Híbrida | «Lo que vamos a hacer en este módulo» |
| Multiplataforma | «Flutter y React Native: ¿alguien los ha oído?» |

**Dinámica por parejas (10 min).** Proyecta el caso del cuadro «Piensa» de la UD1:

> «Una cadena de tiendas quiere una app de fidelización con tarjeta de puntos, catálogo y notificaciones. Tiene 3 desarrolladores web y poco presupuesto. ¿Qué tipo de app elegiríais y por qué?»

Dales 5 minutos por parejas y 5 para ponerlo en común. **Respuesta esperada:** híbrida o PWA, porque el equipo ya sabe web, tienen poco presupuesto y la app no necesita un rendimiento extremo. Premia a quien mencione que las notificaciones en iOS funcionan mejor como app instalada que como PWA.

**Cierre (5 min):** «¿Cuándo NO elegiríais híbrida?» Tienen que salir los juegos 3D, la realidad aumentada intensiva y la edición de vídeo.

## 16:40 · Cómo funciona una app híbrida (20 min)

Usa la [UD1, apartado 2](../ud1/index.md#2-como-funciona-una-app-hibrida-por-dentro). Proyecta el diagrama y explícalo con esta secuencia:

1. **WebView:** «Imaginad Chrome sin la barra de direcciones, ocupando toda la pantalla. Ahí dentro se ejecuta nuestra web.»
2. **Puente:** «Cuando nuestro JavaScript quiere la foto, le pide al puente de Capacitor que hable con Android.»
3. **Código nativo y plugins:** «Capacitor ya trae un proyecto Android hecho; nosotros casi no lo tocamos. Cada cosa del hardware es un plugin: cámara, GPS…»

**Ejemplo que lo resume todo:** el botón «Hacer foto». El botón bonito es Ionic, la lógica es Angular y la cámara la abre Capacitor.

**Preguntas rápidas para comprobar (a mano alzada):**

- «Si la app es una web, ¿se puede publicar en Google Play?» → Sí, Capacitor la empaqueta.
- «¿Necesito saber Kotlin para usar la cámara?» → No, para eso está el plugin.
- «¿Qué es más rápido para un juego 3D, nativo o híbrido?» → Nativo.

## 17:00 · Pausa (10 min)

Recuérdales que comprueben si ha terminado la descarga de Android Studio.

## 17:10 · Puesta en marcha del entorno (45 min) { #1710-puesta-en-marcha-del-entorno-45-min }

Reparte la **hoja de comprobación** y proyecta la guía [Preparar el entorno](../curso/entorno.md).

=== "Plan A: los PC del aula ya lo tienen"

    Solo tienen que **comprobar** (pasos 1–6 de la hoja), activar la depuración USB en su móvil (paso 7) y conectarlo (paso 8). Sobra tiempo: quien acabe, crea su cuenta de GitHub con el correo del IES (paso 9) y empieza a seguir la demo.

=== "Plan B: hay que instalar"

    Por orden, porque cada paso depende del anterior:

    1. **Node.js 24 LTS** (5 min).
    2. **Git** (3 min).
    3. **`npm install -g @ionic/cli`** (2 min).
    4. **VS Code** (3 min).
    5. **Android Studio**: lanzar el instalador y el asistente *Standard*. Tarda: que lo dejen instalando y sigan con el móvil.
    6. **Móvil**: opciones de desarrollador y depuración USB.

    Objetivo mínimo del día: **pasos 1 a 4 hechos**. Android Studio puede terminar en casa.

**Cómo gestionar el aula:**

- Método **semáforo**: quien va bien pone el móvil boca arriba sobre la mesa; quien está atascado, boca abajo. Así ves de un vistazo a quién atender.
- Los que terminan antes **ayudan a su compañero de al lado** antes que llamarte a ti.
- **Atascos de más de 5 minutos:** que lo apunten en la hoja y sigan con el siguiente paso. Lo resuelves al final o el lunes siguiente.

**Problemas que vas a ver (y la solución):**

| Problema | Solución rápida |
|---|---|
| Windows: PowerShell no deja ejecutar `ionic` o `npm` | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| `ionic -v` da 5.x o 6.x | Hay un Ionic antiguo: `which -a ionic` y [Problemas frecuentes](../recursos/problemas.md) |
| `node -v` da 18 o 20 | Instalar Node 24; con `nvm`: `nvm install 24` |
| Mac: permisos al instalar con npm | **Nunca `sudo`**: usar Node de Homebrew o `nvm` |
| El móvil no aparece | Otro cable, desbloquear el móvil y aceptar el aviso de depuración |
| Android Studio pide un JDK | El que trae incluido (*jbr*) |
| Sin móvil Android | Emulador en *Device Manager* o compartir con un compañero |

## 17:55 · Demo en directo: de web a app (20 min)

Es el momento clave de la sesión. Tenlo todo abierto y **tu móvil proyectado con `scrcpy`**. Sigue la página [Demo Hola DAM](demo-hola-dam.md).

1. **Enseña el código** (2 min): tres ficheros en `www/` (HTML, CSS y JS). Señala en `app.js` la línea de `window.Capacitor`: «Esto solo existe cuando la web se ejecuta dentro de la app».
2. **Ábrelo en el navegador** (1 min): dice **WEB**. Activa la vista de móvil de Chrome (F12 → icono de móvil) y muestra que el diseño se adapta.
3. **Convierte en app** (8 min), comentando cada comando:
    - `npm init -y` → «Creamos el fichero que lista las dependencias».
    - `npm install @capacitor/core @capacitor/cli @capacitor/android` → «Instalamos Capacitor».
    - `npx cap init "Hola DAM" es.iesrafaelalberti.holadam --web-dir www` → «Nombre de la app, identificador único como un dominio al revés, y dónde está nuestra web».
    - `npx cap add android` → «Capacitor genera un proyecto Android completo. Mirad la carpeta `android/` que ha aparecido».
    - `npx cap sync android` → «Copia nuestra web dentro del proyecto Android». **No te lo saltes**: sin él, Android Studio da *Could not read script capacitor.settings.gradle*.
    - `npx cap open android` → abre Android Studio.
4. **Ejecuta en el móvil** (3 min): ▶ **Run** en Android Studio, o directamente `npx cap run android` en la Terminal (más fiable en directo). En pantalla aparece **ANDROID**. Pulsa el botón unas veces: «Mismo código, ahora es una app instalada».
5. **Cambio en directo** (4 min): cambia el título a «Hola, [nombre de un alumno]», ejecuta `npx cap sync android` y vuelve a pulsar ▶. Así entienden el ciclo **editar → sync → run**.
6. **Enséñales dónde está la app** (2 min): en el cajón de aplicaciones del móvil, con su icono, como cualquier otra.

!!! warning "Plan B si falla la demo"
    Si Android Studio se bloquea o el móvil no aparece, **no pierdas más de 3 minutos**. Abre directamente la app que ya instalaste el fin de semana en tu móvil (por eso conviene haber hecho la demo antes) y explica los pasos sobre la carpeta `android/` generada.

Quien tenga el entorno listo puede repetir la demo con la carpeta `demo-hola-dam` (súbela a Moodle).

## 18:15 · Actividad A1.1 y cierre (15 min)

1. **Presenta [A1.1 De web a app](../ud1/actividades.md#a11)** (5 min): lee la tabla de comportamientos y la rúbrica. Se entrega **antes del lunes 5 de octubre**.
2. **Tres avisos** que evitan la mitad de los errores:
    - «Usad `<script src="js/app.js" defer>`. Con `type="module"` no funciona al abrir el HTML con doble clic.»
    - «En el móvil no hay ratón: el `mouseover` también tiene que funcionar al tocar.»
    - «El botón 5 tiene clic y doble clic. Un doble clic también lanza dos clics; pensad cómo distinguirlos.»
3. **Deberes para el lunes que viene:**
    - Entorno terminado (lo que quede pendiente en la hoja).
    - A1.1 entregada.
    - Leer los apartados 3 a 5 de la UD1.
4. **Recoge las hojas de comprobación**: sabrás a quién tienes que ayudar el día 5.

---

## Materiales de la sesión

Están en la carpeta `materiales-docente/sesion-1/` del zip (fuera del sitio web, para que el alumnado no los vea):

| Fichero | Para qué |
|---|---|
| `demo-hola-dam/` | La web de la demo y `PASOS.md` con los comandos. Súbela a Moodle después de clase |
| `evaluacion-inicial.gift.txt` | Las 18 preguntas del cuestionario para importar en Moodle |
| `hoja-comprobacion-entorno.md` | La hoja que rellenan en el bloque del entorno (imprimir o subir a Moodle) |
| `solucion-A1.1/` | Solución completa de la actividad A1.1, con dos ilustraciones de Cádiz de ejemplo |

## Solución de A1.1 { #solucion-de-a11 }

Está en `materiales-docente/sesion-1/solucion-A1.1/www/`. Puntos que conviene saber explicar:

- **Párrafo con ratón y toque:** usa `mouseenter`/`mouseleave` para el ratón y `pointerdown` para el dedo (comprobando `pointerType`), porque en el móvil no hay *hover*.
- **Clic y doble clic en el mismo botón:** un doble clic dispara dos `click` y después un `dblclick`. La solución espera 250 ms antes de ejecutar el clic simple y lo cancela si llega el doble clic. Es un buen detalle para comentar el día 5.
- **`<script defer>` en lugar de `type="module"`:** los módulos no se cargan al abrir el HTML con doble clic (`file://`). Es un error típico si el alumnado copia código de la IA.
- **Cambios de estilo con clases CSS** (`classList`) en lugar de tocar `style` a mano, salvo el color rotatorio.
- **Mobile-first:** estilos base para móvil y una *media query* a partir de 768 px que reorganiza en dos columnas; botones de 48 px de alto.
- **Imágenes:** las ilustraciones SVG son de relleno. Sustitúyelas por fotos reales de Cádiz si quieres enseñar la solución.
