# UD1 · Actividades

| Actividad | Tipo | Entrega | CE |
|---|---|---|---|
| [A1.1 De web a app](#a11) | Individual | Lun 5 oct | RA1 a, e |
| [A1.2 Chistes de Chuck Norris](#a12) | Grupal (3–4) | Lun 19 oct | RA1 e |
| [A1.3 Ficha de análisis y diseño](#a13) | Individual | Lun 19 oct | RA1 b, c, d |

---

## A1.1 · De web a app { #a11 }

**Repaso de HTML + CSS + JavaScript y primera app con Capacitor.**

Diseña una web y conviértela en app Android con Capacitor.

### Requisitos

1. Ficheros **HTML, CSS y JS separados** (`index.html`, `css/estilos.css`, `js/app.js`) dentro de la carpeta `www/`.
2. El título de la página debe ser **«CURSO 2026-2027»**.
3. Diseño **mobile-first**: se ve bien en el móvil y se adapta a escritorio con al menos una *media query*.
4. La página tendrá:
    - A. Un párrafo con el texto inicial **«VIVA 2º DAM»**.
    - B. Un párrafo con **tu nombre**.
    - C. Un campo de texto.
    - D. Una imagen de Cádiz.
    - E. Cinco botones.

### Comportamiento

| Elemento | Evento | Acción |
|---|---|---|
| Párrafo 1 | Pasar el ratón o tocarlo | Su borde aumenta y cambia a rojo |
| Botón 1 | Clic | Cambia la imagen por otra de Cádiz |
| Botón 2 | Clic | Cambia el color del texto del párrafo 1 |
| Botón 3 | Clic | Copia el texto del campo en el párrafo 1 |
| Botón 4 | Clic | Cambia el título de la página a «APLICACIONES HÍBRIDAS» |
| Botón 5 | Doble clic | Pone el fondo del párrafo 1 en verde claro |
| Botón 5 | Clic | Cambia el estilo de las letras de tu nombre |

5. Convierte la web en app con Capacitor ([UD1, apartado 7](index.md#7-de-web-a-app-con-capacitor)) e instálala en tu móvil.

### Entrega (Moodle)

Carpeta comprimida con `www/` y **dos capturas**: la web en el navegador y la app en el móvil. No incluyas `node_modules/` ni `android/`.

### Rúbrica (10 puntos)

| Criterio | Puntos |
|---|---|
| Estructura: ficheros separados, HTML semántico, título correcto | 2 |
| Los siete comportamientos funcionan | 3,5 |
| Diseño mobile-first con media query y zonas táctiles adecuadas | 2 |
| App funcionando en el móvil (captura) | 2 |
| Código limpio (`const`/`let`, `addEventListener`, clases CSS) | 0,5 |

---

## A1.2 · Chistes de Chuck Norris { #a12 }

**Actividad grupal · HTML + CSS + JS + formulario + Capacitor.**

### Requisitos

1. Ficheros HTML, CSS y JS separados.
2. Título de la página: **«CHISTES CHUCK NORRIS»**.
3. La web tendrá:
    - A. Una imagen de Chuck Norris centrada con borde rojo de 1 px.
    - B. Un párrafo dentro de un `div` con el texto «El trabajo, constancia y motivación es la clave del éxito».
    - C. Una lista numerada con los integrantes del grupo, dentro de otro `div`.
    - D. Un área de texto (`textarea`).
    - E. Tres botones.
    - F. Un formulario con **nombre**, **correo** y **contraseña**, todos obligatorios, con botones *Enviar* y *Limpiar*. Si todo es correcto, al enviar se abre otra página con el texto «IES Rafael Alberti».
4. **Novedad 2026:** un cuarto botón **«Chiste aleatorio»** que usa `fetch` para traer un chiste de la API pública [api.chucknorris.io](https://api.chucknorris.io) y lo muestra en el `textarea`.

### Comportamiento

| Elemento | Acción |
|---|---|
| Párrafo | Al pasar el ratón o tocarlo: borde más grueso y rojo, y el texto cambia a «ÉXITO ASEGURADO» |
| Botón 1 | Cambia la imagen por otra de Chuck Norris |
| Botón 2 | Vacía el `textarea` |
| Botón 3 | Aumenta el tamaño de letra de la lista y la pone en rojo |
| Chiste aleatorio | Llama a la API con `async/await` y muestra el chiste; si falla, muestra un mensaje de error |

```js title="Pista: fetch con async/await"
async function cargarChiste() {
  try {
    const respuesta = await fetch('https://api.chucknorris.io/jokes/random');
    if (!respuesta.ok) throw new Error(`HTTP ${respuesta.status}`);
    const datos = await respuesta.json();
    areaTexto.value = datos.value;
  } catch (error) {
    areaTexto.value = 'No se ha podido cargar el chiste. Revisa tu conexión.';
  }
}
```

5. Convierte la web en app con Capacitor.

### Entrega (Moodle, un integrante por grupo)

Carpeta comprimida con el código y **dos capturas** (web y app en el móvil).

### Rúbrica (10 puntos)

| Criterio | Puntos |
|---|---|
| Elementos A–F correctos | 2,5 |
| Comportamientos de los botones y del párrafo | 2 |
| Formulario con validación y redirección | 2 |
| Chiste aleatorio con `fetch` y gestión de error | 1,5 |
| Diseño mobile-first y app en el móvil | 2 |

---

## A1.3 · Ficha de análisis y diseño { #a13 }

**Nueva en 2026 · Cubre los criterios RA1 b, c y d.**

Vas a analizar un caso real y justificar cómo lo harías. Este documento es el primer paso de la app que diseñes en la UD4 y del panel SCRUM de tu PFC.

### El caso

Elige **uno**:

1. **Cádiz Accesible:** app municipal para localizar aparcamientos para personas con movilidad reducida, rampas y aseos adaptados, con mapa y avisos de incidencias con foto.
2. **Huerto IES:** app para gestionar los cultivos del huerto escolar: fichas de cultivo, calendario de riego, fotos de la evolución y alertas.
3. **Tu PFC:** la app de tu proyecto de fin de ciclo, si ya tienes la idea.

### Qué tienes que entregar

Un documento (PDF o Markdown en GitHub) de **2 a 4 páginas** con cinco apartados:

1. **Requisitos**: usuarios, plataformas, funciones principales, hardware que necesita, ¿debe funcionar offline?
2. **Comparativa de tecnologías** (CE c): tabla con al menos **tres opciones** (por ejemplo, Ionic + Angular, Flutter y nativa Kotlin) valoradas con los criterios de la [tabla de la UD1](index.md#4-elegir-tecnologia). Termina con tu elección justificada en 5–10 líneas.
3. **Arquitectura** (CE b): diagrama de capas (presentación, servicios, datos, dispositivo) y los patrones que usarías y por qué.
4. **Estructura de la app** (CE d): mapa de pantallas y navegación (tabs, menú, detalle) y **wireframes** de las 3 pantallas principales en móvil. Puedes usar Figma, Excalidraw, Penpot o papel escaneado.
5. **Decisiones de usabilidad y rendimiento**: al menos cinco decisiones concretas (zona del pulgar, modo oscuro, carga diferida de imágenes, caché offline…).

!!! tip "Puedes usar IA para investigar"
    Pídele a un asistente que te ayude a comparar tecnologías, pero **contrasta los datos** y escribe tú la justificación. Indica al final qué *prompts* has usado.

### Rúbrica (10 puntos)

| Criterio | CE | Puntos |
|---|---|---|
| Requisitos claros y completos | — | 1,5 |
| Comparativa de tres tecnologías con criterios y elección bien justificada | c | 2,5 |
| Arquitectura en capas y patrones razonados | b | 2 |
| Mapa de navegación y wireframes mobile-first de 3 pantallas | d | 2,5 |
| Decisiones de usabilidad y rendimiento | d | 1,5 |
