# UD4 · Actividades

| Actividad | Entrega | CE |
|---|---|---|
| [A4.1 Terremotos y tu API de PMDM](#a41) | Lun 14 dic | RA2 d, e |
| [A4.2 Mis lugares: local + nube](#a42) | Dom 20 dic | RA2 b, c, d |
| [A4.3 Panel SCRUM del PFC](#a43) | Lun 21 dic (en clase) | RA1, RA2 |

---

## A4.1 · Terremotos y tu API de PMDM { #a41 }

Repositorio: `AH_UD4_A1_NombreApellidos`

Proyecto standalone con **dos páginas** y navegación entre ellas (tabs o menú).

### Página 1: Terremotos (API pública)

1. Una imagen del planeta Tierra.
2. Un botón **«Último terremoto»** que hace un `GET` a la API del USGS y muestra el terremoto más reciente: magnitud, lugar, fecha, profundidad y coordenadas.
3. Un segundo botón **«Terremotos de hoy ≥ 4,5»** que muestra una lista filtrada y ordenada por magnitud.
4. Investiga el formato de la respuesta y crea **dos interfaces**: la de la respuesta de la API y tu modelo interno.
5. Estados de **carga**, **error** (mensaje claro en pantalla) y **lista vacía**.

URLs útiles del USGS:

- `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson`
- `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson`

### Página 2: tu API (Spring Boot en Render)

1. Otra imagen de tu elección.
2. Al menos un botón que hace un `GET` a la API que desplegaste en Render en **PMDM** y muestra los datos en una lista.
3. La URL base está en `environment.ts`.
4. Documenta en el `README.md` si tuviste problemas de **CORS** y cómo los resolviste.

!!! question "¿No tienes la API de PMDM desplegada?"
    Usa temporalmente [JSONPlaceholder](https://jsonplaceholder.typicode.com) y avisa al profesor. La nota de este apartado será como máximo de un 70 %.

### Entrega

Repositorio + vídeo corto (1–2 min) en el móvil mostrando las dos páginas.

### Rúbrica (10 puntos)

| Criterio | CE | Puntos |
|---|---|---|
| Servicios con `HttpClient` e interfaces de respuesta y modelo | d | 2,5 |
| Último terremoto y lista filtrada correctos | d | 2 |
| Estados de carga, error y vacío | d | 1,5 |
| Consumo de la API propia con URL en `environment` | d | 2 |
| Navegación entre páginas | e | 1 |
| README con explicación de CORS y vídeo | — | 1 |

---

## A4.2 · Mis lugares: local + nube { #a42 }

Repositorio: `AH_UD4_A2_NombreApellidos`

**Nueva en 2026 · Integra hardware, persistencia local y remota, y ciclo de vida.**

Una app para guardar tus lugares favoritos de Cádiz (o de tu pueblo).

### Requisitos

**Datos**

1. Modelo `Lugar`: `id`, `nombre`, `descripcion`, `categoria` (playa, restaurante, monumento, otro), `latitud`, `longitud`, `foto` (opcional) y `fecha`.
2. Los lugares se guardan en **Firestore** (colección `lugares`) con un servicio CRUD.
3. Una copia de la lista se guarda en **Preferences** para que la app muestre los lugares **sin conexión**.
4. Los **ajustes** del usuario (categoría favorita, orden de la lista, tema claro/oscuro) se guardan en Preferences y se recuperan al abrir la app.

**Pantallas**

5. **Lista** de lugares con buscador, filtro por categoría y un indicador de **«Sin conexión»** cuando no hay red (`@capacitor/network`).
6. **Alta / edición** con formulario reactivo:
    - botón **«Usar mi ubicación»** que rellena latitud y longitud con el GPS;
    - botón **«Añadir foto»** con la cámara (guarda la foto reducida en *base64* o como URL local; explica tu decisión).
7. **Detalle** con la foto, los datos y un enlace a Google Maps.
8. **Borrado** deslizando el elemento en la lista (`ion-item-sliding`) y vibración al confirmar.

**Ciclo de vida**

9. Cuando la app vuelve al primer plano (`appStateChange`) o recupera la conexión, **recarga los datos remotos** y actualiza la copia local.

**Seguridad**

10. Reglas de Firestore que al menos validen que `nombre` es un texto no vacío (cópialas en el `README.md`).

### Entrega

Repositorio + vídeo (2–3 min) en el móvil que muestre: alta con GPS y foto, el dato apareciendo en la consola de Firebase, y la app funcionando en **modo avión** con los datos locales.

### Rúbrica (10 puntos)

| Criterio | CE | Puntos |
|---|---|---|
| CRUD en Firestore con servicio y modelo tipado | d | 2 |
| Copia local y ajustes en Preferences; funciona sin red | d | 2 |
| GPS y cámara integrados en el formulario | b | 2 |
| Recarga al volver al primer plano / recuperar red | c | 1,5 |
| Lista con búsqueda, filtro, borrado deslizando y vibración | — | 1,5 |
| Reglas de seguridad y README | — | 1 |

---

## A4.3 · Panel SCRUM del PFC { #a43 }

**En clase, el día de la prueba de diciembre. Cuenta como parte práctica de la prueba teórica.**

Vas a planificar qué funcionalidades de este módulo usarás en tu **proyecto de fin de ciclo** y colocarlas en el panel SCRUM del aula. En PMDM y PSP harás una tarea similar.

### Qué hay que hacer

1. Pon tu nombre en letras visibles en tu zona del panel.
2. Elige de la lista las funcionalidades que usarás en tu PFC y escribe una tarea por post-it (recomendado: una por funcionalidad).
3. Colócalas en **To do**, **WIP** (en curso) o **Done** según tu avance real.
4. Para cada tarea, escribe en tu documento: objetivo, criterio de «hecho» y estimación en horas.

### Funcionalidades orientativas

| # | Funcionalidad | Objetivo | Tareas típicas |
|---|---|---|---|
| F1 | Esqueleto y paso a móvil | App mínima en navegador y Android | `ionic start`, rutas iniciales, `cap add android`, prueba en dispositivo |
| F2 | UI básica con Ionic | Listado principal | `ion-header`, `ion-list`/`ion-card`, `ion-searchbar`, servicio con datos simulados, `@for` |
| F3 | Navegación y detalle | Pulsar un elemento y ver su ficha | Ruta `/detalle/:id`, `routerLink`, parámetro como `input()` |
| F4 | Formulario de alta y edición | Crear y modificar elementos | Formulario reactivo, validaciones, botón deshabilitado, alta/edición en el servicio |
| F5 | Persistencia local | Funcionar offline | Preferences o SQLite, interfaz repositorio, prueba cerrando y abriendo la app |
| F6 | Firebase | Datos en la nube | Proyecto Firebase, AngularFire, CRUD, observable remoto, reglas |
| F7 | API REST (Spring Boot en Render) | Datos del backend | `HttpClient`, `GET`, CORS, botón «Sincronizar», errores de red |
| F8 | GPS y cámara | Funcionalidades del dispositivo | Plugins, servicio de dispositivo, coordenadas y foto en el modelo, enlace a mapa |
| F9 | Gestos y UX móvil | Interacción táctil | Deslizar para borrar, vibración, prueba en dispositivo real |
| F10 | PWA | Instalable como app web | `ng add @angular/pwa`, manifest e iconos, prueba offline de la shell |
| F11 | Calidad (UD5) | App probada y publicable | Tests Vitest, E2E Cypress, AAB firmado, README técnico |

### Entrega (Moodle)

Documento con tu lista de tareas y una **foto de tu zona del panel**.

### Rúbrica (10 puntos)

| Criterio | Puntos |
|---|---|
| Selección de funcionalidades coherente con el PFC | 3 |
| Tareas bien definidas (objetivo y criterio de «hecho») | 3 |
| Estimaciones razonables | 2 |
| Estado real y panel ordenado | 2 |
