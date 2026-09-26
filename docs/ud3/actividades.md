# UD3 · Actividades

Desde esta unidad **se entrega por GitHub**. Crea el repositorio con tu cuenta del IES y sube a Moodle solo el enlace.

| Actividad | Entrega | CE |
|---|---|---|
| [A3.1 Guía de Cádiz: componentes, servicios y rutas](#a31) | Lun 16 nov | RA2 a, e |
| [A3.2 Calculadora y alta de clientes](#a32) | Lun 23 nov | RA2 a, e |
| [A3.3 GPS en tiempo real con IA](#a33) | Lun 30 nov | RA2 b, c |
| [A3.4 Eureka: sensores, cámara y sonido](#a34) | Lun 30 nov | RA2 b, c |

---

## A3.1 · Guía de Cádiz: componentes, servicios y rutas { #a31 }

Repositorio: `AH_UD3_A1_NombreApellidos`

Crea un proyecto `blank` standalone y construye una pequeña guía de servicios de la ciudad.

### Requisitos

1. **Página de inicio** con un bloque de *Información general* que muestre la fecha y la hora actuales (actualizadas cada segundo con un signal).
2. **Componente `alumno`** en `src/app/components/alumno/` que se muestra debajo de la información general, con tu nombre en un párrafo. Fondo **azul oscuro** y letras **amarillas**.
3. **Servicio `datos-alumno`** en `src/app/services/`. El componente `alumno` **no** tiene los datos en su `.ts`: los obtiene del servicio con `inject()`.
4. En la página de inicio, una lista **Servicios** con al menos cuatro categorías, entre ellas **Deportes** e **Inmobiliarias**.
5. Rutas **`/deportes`** e **`/inmobiliarias`**, con carga diferida (`loadComponent`), que muestran **5 elementos** cada una con datos inventados e imágenes. Los datos vienen de un servicio `guia.service.ts`.
6. Al pulsar un elemento se abre **`/detalle/:categoria/:id`** con su ficha. Lee los parámetros con `input()` (`withComponentInputBinding()`).
7. Todas las páginas secundarias tienen botón **atrás**.

### Entrega

Enlace al repositorio y una captura de cada página en el móvil en el `README.md`.

### Rúbrica (10 puntos)

| Criterio | CE | Puntos |
|---|---|---|
| Fecha y hora en tiempo real con signal y limpieza del temporizador al destruir | a | 1,5 |
| Componente `alumno` con estilos pedidos | a | 1,5 |
| Servicio inyectado con `inject()` como única fuente de datos | a | 2 |
| Rutas con `loadComponent` y listados de 5 elementos | e | 2 |
| Detalle con parámetros por `input()` | e | 2 |
| Botón atrás y navegación coherente | e | 1 |

---

## A3.2 · Calculadora y alta de clientes { #a32 }

Repositorio: `AH_UD3_A2_NombreApellidos`

**Comunicación entre componentes, formularios reactivos y paso de datos entre páginas.**

### Parte 1: calculadora (padre ↔ hijo)

1. Crea el componente **`calculadora`** y colócalo en el `ion-footer` de la página de inicio.
2. En el **padre** hay dos `ion-input` numéricos y un botón **Calcular**.
3. Al pulsar Calcular, el padre pasa los dos valores al hijo con **`input()`**.
4. El hijo calcula **suma, resta, multiplicación y división** y devuelve el resultado al padre con **`output()`**.
5. El padre muestra los resultados junto al botón con un formato adecuado (dos decimales, aviso si se divide entre cero).

### Parte 2: alta de clientes (formulario → servicio → otra página)

1. Crea la interfaz **`Cliente`** en `src/app/models/cliente.ts` con `nombre`, `apellido`, `email` y `nacionalidad`.
2. Crea la ruta **`/cliente`** con un **formulario reactivo** de esos cuatro campos:
    - todos obligatorios;
    - email con formato válido;
    - mensajes de error bajo cada campo;
    - el botón *Guardar* está deshabilitado mientras el formulario no sea válido.
3. Al guardar, los datos se envían a un **`ClientesService`** (con signals) y se navega a **`/datos-cliente`**.
4. `/datos-cliente` muestra el último cliente y la lista de todos los guardados en la sesión.

### Entrega

Enlace al repositorio con un `README.md` que incluya capturas y un vídeo corto (menos de 1 min) mostrando la calculadora y el alta.

### Rúbrica (10 puntos)

| Criterio | CE | Puntos |
|---|---|---|
| Padre → hijo con `input()` | a | 1,5 |
| Hijo → padre con `output()` y resultados formateados | a | 2 |
| Modelo `Cliente` tipado | a | 1 |
| Formulario reactivo con validaciones y mensajes | a | 2,5 |
| Paso de datos por servicio y página de datos | e | 2 |
| Navegación y experiencia de uso | e | 1 |

---

## A3.3 · GPS en tiempo real con IA { #a33 }

Repositorio: `AH_UD3_A3_NombreApellidos`

**Primera actividad en la que se pide programar con ayuda de IA.**

### Requisitos

1. Proyecto standalone con una página principal que muestre en tiempo real **latitud, longitud, precisión y hora de la última lectura**.
2. Toda la lógica del GPS en un **servicio** (`gps.service.ts`) que exponga signals. Genera este servicio **con un asistente de IA**.
3. Gestión de **permisos**: pide permiso, muestra un mensaje claro si se deniega y declara los permisos en `AndroidManifest.xml`.
4. Botones **Iniciar** y **Detener** seguimiento.
5. **Ciclo de vida**: el seguimiento se detiene al salir de la página (`ionViewWillLeave`) y cuando la app pasa a segundo plano (`appStateChange`), y se reanuda al volver.
6. Un enlace **Ver en el mapa** que abre Google Maps con las coordenadas actuales.
7. Diseño libre.

### Informe de IA (en el `README.md`)

- Los *prompts* que usaste.
- Qué generó bien la IA y **qué tuviste que corregir** (sintaxis antigua, permisos, manejo de errores…).
- Una explicación, con tus palabras, de cómo funciona `watchPosition` y por qué hay que llamar a `clearWatch`.

### Entrega

Enlace al repositorio y un vídeo corto en el que se vea la app en el móvil mientras te mueves.

### Rúbrica (10 puntos)

| Criterio | CE | Puntos |
|---|---|---|
| Lectura en tiempo real en el móvil | b | 2,5 |
| Servicio con signals y separación de la vista | b | 1,5 |
| Permisos y mensajes de error | b | 1,5 |
| Parada y reanudación según el ciclo de vida | c | 2,5 |
| Informe de IA crítico y explicación propia | — | 2 |

---

## A3.4 · Eureka: sensores, cámara y sonido { #a34 }

Repositorio: `AH_UD3_A4_NombreApellidos`

### Estructura

Una página principal (padre) que contiene **tres componentes hijos**: `gps`, `sensores` y `camara`.

| Componente | Qué muestra |
|---|---|
| `gps` | Latitud y longitud en tiempo real (puedes reutilizar tu servicio de A3.3) |
| `sensores` | Valores del **acelerómetro** (x, y, z) y, si tu móvil lo tiene, del **sensor de luz** |
| `camara` | Botón para hacer una foto y mostrarla en el componente |

### El efecto Eureka

Cuando se cumpla la condición de disparo:

1. el hijo `sensores` lo comunica al padre con un **`output()`**;
2. el **padre** muestra el texto **«Eureka»**, reproduce una canción de tu elección (fichero en `src/assets/`) y hace vibrar el móvil;
3. si el dispositivo tiene linterna y has encontrado un plugin compatible, **se enciende la linterna** (opcional, +1 punto).

**Condición de disparo:**

- **Opción A (sensor de luz):** la luminosidad baja de un umbral (tapa el sensor con la mano). Necesitas un plugin de la comunidad.
- **Opción B (acelerómetro):** agitas el móvil y la aceleración supera un umbral. Funciona en cualquier móvil.

Implementa **al menos una** de las dos opciones y explica en el `README.md` cuál y por qué.

!!! tip "Reproducir audio"
    ```ts
    private audio = new Audio('assets/eureka.mp3');

    celebrar() {
      this.eureka.set(true);
      this.audio.play();
    }
    ```

### Ciclo de vida

Todos los sensores y el GPS **se detienen** al salir de la página o al pasar la app a segundo plano.

### Entrega

Enlace al repositorio y vídeo en el móvil mostrando el efecto Eureka.

### Rúbrica (10 puntos + 1 extra)

| Criterio | CE | Puntos |
|---|---|---|
| Estructura padre con tres hijos | — | 1,5 |
| GPS y acelerómetro en tiempo real | b | 2 |
| Cámara con foto mostrada | b | 1,5 |
| Disparo comunicado con `output()` y gestionado en el padre (texto, audio, vibración) | b | 2,5 |
| Parada de sensores según el ciclo de vida | c | 2,5 |
| **Extra:** linterna o sensor de luz con plugin de la comunidad | b | +1 |
