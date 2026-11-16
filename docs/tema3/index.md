# Tema 3 · Interfaces y navegación

!!! abstract "Ficha del tema"
    - **Duración:** 2 sesiones (9 y 16 de noviembre). Los apartados 8 y 9 se trabajan en casa con el boletín
    - **RA:** RA2 · CE a (interfaces interactivas y adaptables) · CE c (estado) · CE e (navegación) · también RA1 · CE e (diseño responsive, apartado 9)
    - **Actividades:** [16 ejercicios rápidos de clase](#ejercicios-rapidos) · 4 guiados · [Boletín de 10 ejercicios](#boletin-de-ejercicios) · [Práctica 3.1 · Cádiz Market](practica-31.md) · [Alta de clientes (guiado)](#practica-32-alta-de-clientes)

!!! info "Ya lo conoces (DI)"
    En Desarrollo de Interfaces ya habéis hecho interfaces **declarativas** con Jetpack Compose: funciones que describen la pantalla, anidadas, que se redibujan cuando cambia el estado. **No lo volvemos a explicar.** En este tema **traducimos** lo que sabéis a Flutter y nos centramos en lo que cambia.

| Sesión | Contenido | En clase |
|---|---|---|
| **1 · 9 nov** | Widgets básicos, paso a paso | Rápido R1 |
| **2 · 16 nov** | Layout, listas, estado local, comunicación entre widgets, `provider` y navegación, todo paso a paso | Rápidos R2-R13 · Guiados G1-G4 · Práctica 3.1 |
| **En casa** | Formularios, tema y diseño adaptable (apartados 8 y 9) | Rápidos R14-R16 · Boletín B1-B10 |

---

## 1. De Compose a Flutter en una tabla

| Compose (DI) | Flutter | Diferencia importante |
|---|---|---|
| Función `@Composable` | Clase que hereda de `StatelessWidget` con un método `build` | En Flutter el widget es una **clase** |
| `remember { mutableStateOf(x) }` | `StatefulWidget` + `State` + `setState` | Hay que **avisar** con `setState` |
| `Modifier.padding(16.dp)` | Widget `Padding(padding: EdgeInsets.all(16), child: ...)` | Espaciado, tamaño y alineación **son widgets** |
| `Modifier.fillMaxWidth()` | `SizedBox(width: double.infinity, child: ...)` o `Expanded` | |
| `Modifier.clickable { }` | `InkWell(onTap: ..., child: ...)` o `GestureDetector` | |
| `Column`, `Row`, `Box` | `Column`, `Row`, `Stack` | Mismos nombres salvo `Box` |
| `LazyColumn` | `ListView.builder` | |
| `LazyVerticalGrid` | `GridView.builder` | |
| `Scaffold`, `TopAppBar`, `FloatingActionButton` | `Scaffold`, `AppBar`, `FloatingActionButton` | |
| `Text("Hola", fontSize = 20.sp)` | `Text('Hola', style: TextStyle(fontSize: 20))` | |
| `Image(painterResource(...))` | `Image.asset(...)` / `Image.network(...)` | |
| `NavController.navigate("detalle")` | `Navigator.push(context, MaterialPageRoute(...))` | |
| `ViewModel` + `StateFlow` | `ChangeNotifier` + `provider` | Lo vemos en el apartado 6 |

---

## 2. Widgets básicos, paso a paso

Todo lo que se ve en pantalla es un **widget**, y los widgets se anidan con `child:` (un hijo) o `children:` (varios).

Vamos a construir **una sola pantalla que crece**. En cada paso añades una pieza, **guardas** (hot reload) y la ves aparecer. Trabaja en el `lib/main.dart` del proyecto `t3_clase` que acabas de crear.

!!! info "Es acumulativo: no se borra lo anterior"
    A partir del paso 1 solo se toca lo que va dentro de `body:`. Cada paso dice si **sustituyes** el `body` o **añades** algo a la lista `children`:

    - **Sustituyes el `body`** solo en los pasos 2 y 3 (y en el 7 solo cambias una palabra).
    - **Añades** en los pasos 4, 5, 6 y 8: escribe la línea nueva al final de `children`, antes del `]`.

### Paso 0 · Empezar de cero: `MaterialApp`

Abre `lib/main.dart`. Trae una app de ejemplo de unas 120 líneas (el contador con el botón «+»). Selecciónalo todo (Cmd+A en Mac, Ctrl+A en Windows), bórralo y **escribe** solo esto:

```dart
import 'package:flutter/material.dart';

void main() => runApp(const MaterialApp(home: Text('Hola')));
```

Sale un texto feo sobre fondo negro. `MaterialApp` es **la app** (tema, idioma, navegación), pero aún no hay una **página** que lo dibuje bien.

!!! warning "Error en rojo en `test/widget_test.dart`"
    Ese test de ejemplo busca la clase `MyApp`, que acabas de borrar. No afecta a la app, pero lo más limpio es **borrar el archivo `test/widget_test.dart`**. Los tests se ven en el Tema 6.

### Paso 1 · Una pantalla de verdad: `Scaffold` y `AppBar`

En VS Code escribe `stless` y pulsa Tab: te crea la plantilla de un widget.

```dart
import 'package:flutter/material.dart';

void main() => runApp(const MaterialApp(home: Basicos()));

class Basicos extends StatelessWidget {
  const Basicos({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Widgets básicos')),
      body: const Text('Hola'),
    );
  }
}
```

- En Flutter un widget es una **clase** con un método `build` que devuelve lo que se ve. En Compose era una función `@Composable`.
- `Scaffold` es la estructura de la página, igual que en Compose: barra superior, cuerpo, botón flotante…

### Paso 2 · Texto con estilo y centrado

**Sustituye** el `body: const Text('Hola'),` por esto:

```dart
body: const Center(
  child: Text(
    'Hola, Cádiz',
    style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold, color: Colors.teal),
  ),
),
```

- `child:` = **un** hijo.
- Centrar **también es un widget** (`Center`). En Compose sería un `Modifier`; en Flutter, el espaciado, el tamaño y la alineación son widgets que envuelven a otros.

### Paso 3 · Varias cosas: `Column` y `children`

`Center` solo admite **un** hijo. Para poner varias cosas, **sustituye** el `body` entero por una `Column`. El texto del paso 2 pasa a ser el primero de la lista:

```dart
body: Column(
  children: [
    const Text(
      'Hola, Cádiz',
      style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold, color: Colors.teal),
    ),
    const SizedBox(height: 16),
    const Text('Segundo texto'),
  ],
),
```

- `children:` = **varios** hijos, en una lista `[ ... ]`. Ya no hay `Center`: lo quitamos.
- `SizedBox(height: 16)` es un hueco. En Flutter no hay `margin`: se separa con widgets.

### Paso 4 · Iconos

**Añade** al final de `children`, debajo de `const Text('Segundo texto'),`:

```dart
const Icon(Icons.beach_access, size: 64, color: Colors.orange),
```

Escribe `Icons.` y deja que el editor te sugiera: hay cientos. Cambia el icono por otro.

### Paso 5 · Imágenes de internet

**Añade** debajo del icono:

```dart
Image.network('https://picsum.photos/400/200', height: 150, fit: BoxFit.cover),
```

Fíjate en que la imagen **no** lleva `const` y los textos sí. Una imagen que se descarga de internet no es constante.

!!! tip "`const` delante de todo lo que no cambie"
    Un widget `const` se crea una vez y Flutter no lo reconstruye. El analizador te lo sugiere con una línea azul: acéptalo siempre.

### Paso 6 · Botones

**Añade** debajo de la imagen. Primero uno, y púlsalo mirando la consola:

```dart
ElevatedButton(onPressed: () => print('Pulsado'), child: const Text('ElevatedButton')),
```

Después, los demás tipos:

```dart
FilledButton(onPressed: () {}, child: const Text('FilledButton')),
OutlinedButton(onPressed: () {}, child: const Text('OutlinedButton')),
const TextButton(onPressed: null, child: Text('Desactivado')),
IconButton(onPressed: () {}, icon: const Icon(Icons.favorite)),
```

- `onPressed` recibe **la función** que se ejecuta al pulsar.
- **`onPressed: null` desactiva el botón.** No hay propiedad `enabled`: lo usaréis mucho en formularios.

### Paso 7 · ¡No cabe! De `Column` a `ListView`

Añade dos o tres botones más o gira el emulador. Aparece una **franja amarilla y negra**: *"A RenderFlex overflowed by … pixels"*. `Column` **no hace scroll**.

Cambia **solo la palabra** `Column` por `ListView` y añade la línea del `padding`. Todo lo que hay dentro de `children` se queda igual:

```dart
body: ListView(
  padding: const EdgeInsets.all(16),
  children: [
    // ... lo mismo que tenías
  ],
),
```

`ListView` es como `Column`, pero con scroll (en Compose, `Column` + `verticalScroll` o `LazyColumn`).

### Paso 8 · Tarjetas con `Card` y `ListTile`

**Añade** al final de `children`:

```dart
const Card(
  child: ListTile(
    leading: Icon(Icons.place),
    title: Text('La Caleta'),
    subtitle: Text('Playa urbana · Cádiz'),
    trailing: Icon(Icons.chevron_right),
  ),
),
```

`ListTile` es la fila típica de una lista, ya hecha: icono a la izquierda, título, subtítulo y algo a la derecha. Copia la tarjeta dos veces más con otras playas.

### El resultado

Si has seguido todos los pasos, tienes esto:

??? example "Código completo de la pantalla"
    ```dart
    import 'package:flutter/material.dart';

    void main() => runApp(const MaterialApp(home: Basicos()));

    class Basicos extends StatelessWidget {
      const Basicos({super.key});

      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(title: const Text('Widgets básicos')),
          body: ListView(
            padding: const EdgeInsets.all(16),
            children: [
              const Text(
                'Hola, Cádiz',
                style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold, color: Colors.teal),
              ),
              const SizedBox(height: 16),
              const Text('Segundo texto'),
              const Icon(Icons.beach_access, size: 64, color: Colors.orange),
              const SizedBox(height: 16),
              Image.network('https://picsum.photos/400/200', height: 150, fit: BoxFit.cover),
              const SizedBox(height: 16),
              ElevatedButton(onPressed: () => print('Pulsado'), child: const Text('ElevatedButton')),
              FilledButton(onPressed: () {}, child: const Text('FilledButton')),
              OutlinedButton(onPressed: () {}, child: const Text('OutlinedButton')),
              const TextButton(onPressed: null, child: Text('Desactivado')),
              IconButton(onPressed: () {}, icon: const Icon(Icons.favorite)),
              const Card(
                child: ListTile(
                  leading: Icon(Icons.place),
                  title: Text('La Caleta'),
                  subtitle: Text('Playa urbana · Cádiz'),
                  trailing: Icon(Icons.chevron_right),
                ),
              ),
            ],
          ),
        );
      }
    }
    ```

Ahora haz el ejercicio rápido **R1** (tres estilos de texto) en un fichero nuevo, `lib/r1.dart`, y ejecútalo con `flutter run -d chrome -t lib/r1.dart`.

### Para más adelante: imágenes propias (assets)

No hace falta hoy; lo usarás en el boletín (B1).

1. Crea la carpeta `assets/img/` en la raíz del proyecto y copia tus imágenes.
2. Declárala en `pubspec.yaml` (ojo con la indentación: dos espacios):

    ```yaml
    flutter:
      uses-material-design: true
      assets:
        - assets/img/
    ```

3. Úsala:

    ```dart
    Image.asset('assets/img/escudo.png', width: 80)
    ```

---

## 3. Layout, paso a paso

Vamos a aprender a **colocar** widgets: en fila, en columna, repartiendo el espacio y unos encima de otros. Igual que en el apartado 2, la pantalla **crece paso a paso**: después del paso 1 todo lo nuevo se **añade al final de `children`**, antes del `]`.

### Paso 1 · Un fichero nuevo para practicar

Crea `lib/layout.dart` con esto y ejecútalo con **Run** (el enlace gris encima del `main`):

```dart
import 'package:flutter/material.dart';

void main() => runApp(const MaterialApp(home: Layout()));

class Layout extends StatelessWidget {
  const Layout({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Layout')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          // aquí iremos añadiendo
        ],
      ),
    );
  }
}
```

Usamos `ListView` desde el principio para que no se salga por abajo cuando añadamos muchas cosas.

### Paso 2 · En fila: `Row`

**Añade** tres cajas de colores en fila:

```dart
Row(
  children: [
    Container(width: 80, height: 80, color: Colors.red),
    Container(width: 80, height: 80, color: Colors.green),
    Container(width: 80, height: 80, color: Colors.blue),
  ],
),
```

- `Row` pone sus hijos **en horizontal**; `Column`, **en vertical**. Igual que en Compose.
- `Container` con `width`, `height` y `color` es una caja de color: perfecta para ver cómo se colocan las cosas. Recuerda: `Container` **nunca** lleva `const`.

### Paso 3 · Repartir el hueco: `mainAxisAlignment`

Dentro del `Row`, **antes** de `children`, añade esta línea:

```dart
Row(
  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
  children: [
    Container(width: 80, height: 80, color: Colors.red),
    Container(width: 80, height: 80, color: Colors.green),
    Container(width: 80, height: 80, color: Colors.blue),
  ],
),
```

Guarda y prueba a cambiar `spaceEvenly` por cada uno de estos valores:

| Valor | Qué hace |
|---|---|
| `start` | Todo al principio (es el valor por defecto) |
| `center` | Todo en el centro |
| `end` | Todo al final |
| `spaceBetween` | El primero al principio, el último al final y el hueco repartido entre medias |
| `spaceAround` | Mismo hueco alrededor de cada uno |
| `spaceEvenly` | Mismo hueco entre todos, también en los bordes |

### Paso 4 · El otro eje: `crossAxisAlignment`

Haz la caja verde más alta (`height: 120`) y añade al `Row` la línea `crossAxisAlignment`:

```dart
Row(
  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
  crossAxisAlignment: CrossAxisAlignment.end,
  children: [
    Container(width: 80, height: 80, color: Colors.red),
    Container(width: 80, height: 120, color: Colors.green),
    Container(width: 80, height: 80, color: Colors.blue),
  ],
),
```

Prueba `start`, `center` y `end`. La regla:

| | `Row` | `Column` |
|---|---|---|
| Eje principal (`mainAxisAlignment`) | Horizontal | Vertical |
| Eje cruzado (`crossAxisAlignment`) | Vertical | Horizontal |

### Paso 5 · Repartir el ancho: `Expanded`

**Añade** otra fila debajo:

```dart
const SizedBox(height: 24),
Row(
  children: [
    Expanded(flex: 2, child: Container(height: 50, color: Colors.orange)),
    Expanded(child: Container(height: 50, color: Colors.purple)),
  ],
),
```

- `Expanded` hace que el hijo **ocupe el espacio que sobra**. Fíjate en que las cajas ya no tienen `width`.
- `flex` dice **en qué proporción**: aquí la naranja ocupa 2 partes y la morada 1 (2/3 y 1/3). Es el `Modifier.weight()` de Compose.

### Paso 6 · ¡No cabe! La franja amarilla

**Añade** una fila con un texto muy largo:

```dart
const SizedBox(height: 24),
const Row(
  children: [
    Icon(Icons.info),
    Text('Este texto es tan largo que no cabe en una sola línea de la pantalla del móvil'),
  ],
),
```

Sale la **franja amarilla y negra**: un `Row` no corta ni baja de línea, así que el texto se sale. **Arréglalo** envolviendo el texto en `Expanded`, que le dice «usa solo el ancho que queda»:

```dart
const Row(
  children: [
    Icon(Icons.info),
    SizedBox(width: 8),
    Expanded(
      child: Text('Este texto es tan largo que no cabe en una sola línea de la pantalla del móvil'),
    ),
  ],
),
```

!!! warning "Las franjas amarillas y negras"
    *"A RenderFlex overflowed by 42 pixels"* significa que el contenido **no cabe**. Soluciones típicas: envolver en `Expanded`, usar `Wrap` (paso 8) o meterlo en un `ListView`.

### Paso 7 · Una caja con estilo: `Container` decorado

**Añade**:

```dart
const SizedBox(height: 24),
Container(
  padding: const EdgeInsets.all(16),
  decoration: BoxDecoration(
    color: Colors.amber.shade100,
    borderRadius: BorderRadius.circular(12),
    border: Border.all(color: Colors.amber),
  ),
  child: const Text('Oferta del día: tortillitas a 5 €'),
),
```

- `padding` = relleno **por dentro** de la caja.
- `decoration` = cómo se ve: color, esquinas redondeadas, borde, sombra…

### Paso 8 · Que baje de línea: `Wrap`

**Añade** unas etiquetas:

```dart
const SizedBox(height: 24),
const Wrap(
  spacing: 8,
  children: [
    Chip(label: Text('Humor')),
    Chip(label: Text('Final')),
    Chip(label: Text('2026')),
    Chip(label: Text('Chirigota')),
    Chip(label: Text('Teatro Falla')),
    Chip(label: Text('Cádiz')),
  ],
),
```

Estrecha la ventana de Chrome: las etiquetas **bajan a la línea siguiente**. Cambia `Wrap` por `Row` y vuelve a estrechar: franja amarilla. `Wrap` es un `Row` que salta de línea.

### Paso 9 · Todo junto: la tarjeta de una agrupación (G1)

**Añade** esta tarjeta. Usa todo lo de los pasos anteriores:

```dart
const SizedBox(height: 24),
Card(
  child: Padding(
    padding: const EdgeInsets.all(16),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Row(
          children: [
            CircleAvatar(child: Icon(Icons.theater_comedy)),
            SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('Los Yesterday',
                      style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                  Text('Chirigota · Autor: Anónimo'),
                ],
              ),
            ),
            Icon(Icons.star, color: Colors.amber),
            Text(' 342 pts'),
          ],
        ),
        const SizedBox(height: 12),
        Wrap(
          spacing: 8,
          children: [for (final e in const ['Humor', 'Final', '2026']) Chip(label: Text(e))],
        ),
      ],
    ),
  ),
),
```

**Para ver qué hace el `Expanded`:** en la fila de arriba, el `Expanded` envuelve la columna del nombre. Ocupa **todo el ancho que sobra**, y por eso la estrella y los puntos quedan pegados al borde derecho:

```text
[icono]  Los Yesterday                    ⭐ 342 pts
         Chirigota · Autor: Anónimo
```

Borra `Expanded(` y su paréntesis de cierre, deja solo la `Column` y guarda. Ahora la columna mide lo que su texto, y los puntos se quedan **al lado del nombre**:

```text
[icono]  Los Yesterday        ⭐ 342 pts
         Chirigota · Autor: Anónimo
```

Vuelve a ponerlo. Es lo mismo que `Modifier.weight(1f)` en Compose.

??? example "Código completo de `lib/layout.dart`"
    ```dart
    import 'package:flutter/material.dart';

    void main() => runApp(const MaterialApp(home: Layout()));

    class Layout extends StatelessWidget {
      const Layout({super.key});

      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(title: const Text('Layout')),
          body: ListView(
            padding: const EdgeInsets.all(16),
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Container(width: 80, height: 80, color: Colors.red),
                  Container(width: 80, height: 120, color: Colors.green),
                  Container(width: 80, height: 80, color: Colors.blue),
                ],
              ),
              const SizedBox(height: 24),
              Row(
                children: [
                  Expanded(flex: 2, child: Container(height: 50, color: Colors.orange)),
                  Expanded(child: Container(height: 50, color: Colors.purple)),
                ],
              ),
              const SizedBox(height: 24),
              const Row(
                children: [
                  Icon(Icons.info),
                  SizedBox(width: 8),
                  Expanded(
                    child: Text('Este texto es tan largo que no cabe en una sola línea de la pantalla del móvil'),
                  ),
                ],
              ),
              const SizedBox(height: 24),
              Container(
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.amber.shade100,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: Colors.amber),
                ),
                child: const Text('Oferta del día: tortillitas a 5 €'),
              ),
              const SizedBox(height: 24),
              const Wrap(
                spacing: 8,
                children: [
                  Chip(label: Text('Humor')),
                  Chip(label: Text('Final')),
                  Chip(label: Text('2026')),
                  Chip(label: Text('Chirigota')),
                  Chip(label: Text('Teatro Falla')),
                  Chip(label: Text('Cádiz')),
                ],
              ),
              const SizedBox(height: 24),
              Card(
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Row(
                        children: [
                          CircleAvatar(child: Icon(Icons.theater_comedy)),
                          SizedBox(width: 12),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text('Los Yesterday',
                                    style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                                Text('Chirigota · Autor: Anónimo'),
                              ],
                            ),
                          ),
                          Icon(Icons.star, color: Colors.amber),
                          Text(' 342 pts'),
                        ],
                      ),
                      const SizedBox(height: 12),
                      Wrap(
                        spacing: 8,
                        children: [for (final e in const ['Humor', 'Final', '2026']) Chip(label: Text(e))],
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        );
      }
    }
    ```


Ahora haz los ejercicios rápidos **R2** y **R3**.

??? info "Para consultar: los demás contenedores"
    | Widget | Para qué |
    |---|---|
    | `Container` | Tamaño, color, bordes, márgenes y relleno en uno |
    | `Padding` | Solo relleno |
    | `SizedBox` | Tamaño fijo o separador (`SizedBox(height: 16)`) |
    | `Center` / `Align` | Centrar o alinear un hijo |
    | `Stack` + `Positioned` | Superponer widgets (un texto sobre una imagen). Lo usa el R4 |
    | `Wrap` | Como `Row`, pero salta de línea si no cabe |
    | `SafeArea` | Evita la muesca y la barra de estado |

---

## 4. Listas, paso a paso

Vamos a hacer la lista de playas de Cádiz, de la más sencilla a la que se usa de verdad.

### Paso 1 · Una lista fija

Crea `lib/listas.dart`:

```dart
import 'package:flutter/material.dart';

void main() => runApp(const MaterialApp(home: ListaPlayas()));

class ListaPlayas extends StatelessWidget {
  const ListaPlayas({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Playas de Cádiz')),
      body: ListView(
        children: const [
          ListTile(title: Text('La Caleta')),
          ListTile(title: Text('Santa María del Mar')),
          ListTile(title: Text('La Victoria')),
        ],
      ),
    );
  }
}
```

Funciona, pero hay que escribir cada fila a mano. ¿Y si fueran 100 playas, o vinieran de internet?

### Paso 2 · Los datos en una lista: `ListView.builder`

Primero **añade** los datos dentro de la clase, justo debajo del constructor:

```dart
static const playas = ['La Caleta', 'Santa María del Mar', 'La Victoria', 'Cortadura', 'Camposoto'];
```

Después **sustituye** el `body` entero:

```dart
body: ListView.builder(
  itemCount: playas.length,
  itemBuilder: (context, i) => ListTile(title: Text(playas[i])),
),
```

- `itemCount` = cuántas filas hay.
- `itemBuilder` = una función que Flutter llama **para cada fila**, con su posición `i` (0, 1, 2…). Devuelve el widget de esa fila.
- Solo construye las filas que se **ven** en pantalla, como `LazyColumn`. Por eso es la que se usa siempre que hay datos.

### Paso 3 · Filas más completas

**Sustituye** el `ListTile` del `itemBuilder` por uno con más cosas:

```dart
itemBuilder: (context, i) => ListTile(
  leading: CircleAvatar(child: Text('${i + 1}')),
  title: Text(playas[i]),
  subtitle: const Text('Cádiz'),
  trailing: const Icon(Icons.chevron_right),
),
```

### Paso 4 · Hacer algo al tocar: `onTap` y `SnackBar`

**Añade** al `ListTile`, debajo de `trailing`:

```dart
onTap: () => ScaffoldMessenger.of(context).showSnackBar(
  SnackBar(content: Text('Has elegido ${playas[i]}')),
),
```

Toca una fila: abajo aparece un mensaje que desaparece solo. Es el `Snackbar` de Compose.

### Paso 5 · Con separadores: `ListView.separated`

Cambia `ListView.builder` por `ListView.separated` y **añade** la línea `separatorBuilder`. El `body` queda así:

```dart
body: ListView.separated(
  itemCount: playas.length,
  separatorBuilder: (context, i) => const Divider(),
  itemBuilder: (context, i) => ListTile(
    leading: CircleAvatar(child: Text('${i + 1}')),
    title: Text(playas[i]),
    subtitle: const Text('Cádiz'),
    trailing: const Icon(Icons.chevron_right),
    onTap: () => ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text('Has elegido ${playas[i]}')),
    ),
  ),
),
```

Ahora hay una línea entre fila y fila.

### Paso 6 (opcional) · En cuadrícula: `GridView.builder`

**Sustituye** el `body`:

```dart
body: GridView.builder(
  padding: const EdgeInsets.all(8),
  itemCount: playas.length,
  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2),
  itemBuilder: (context, i) => Card(child: Center(child: Text(playas[i]))),
),
```

`crossAxisCount: 2` = dos columnas. Cambia a 3 y guarda.

??? example "Código completo de `lib/listas.dart`"
    ```dart
    import 'package:flutter/material.dart';

    void main() => runApp(const MaterialApp(home: ListaPlayas()));

    class ListaPlayas extends StatelessWidget {
      const ListaPlayas({super.key});

      static const playas = ['La Caleta', 'Santa María del Mar', 'La Victoria', 'Cortadura', 'Camposoto'];

      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(title: const Text('Playas de Cádiz')),
          body: ListView.separated(
            itemCount: playas.length,
            separatorBuilder: (context, i) => const Divider(),
            itemBuilder: (context, i) => ListTile(
              leading: CircleAvatar(child: Text('${i + 1}')),
              title: Text(playas[i]),
              subtitle: const Text('Cádiz'),
              trailing: const Icon(Icons.chevron_right),
              onTap: () => ScaffoldMessenger.of(context).showSnackBar(
                SnackBar(content: Text('Has elegido ${playas[i]}')),
              ),
            ),
          ),
        );
      }
    }
    ```

Ahora haz el ejercicio rápido **R5**.

??? info "Para consultar: qué lista usar"
    | Variante | Cuándo |
    |---|---|
    | `ListView(children: [...])` | Pocos elementos fijos |
    | `ListView.builder` | Muchos elementos o datos que vienen de una lista |
    | `ListView.separated` | Con separador entre elementos |
    | `GridView.builder` | Cuadrícula |

---

## 5. Estado local, paso a paso

Hasta ahora todo era fijo. Vamos a hacer un **contador**: un número que cambia al pulsar un botón.

### Paso 1 · Lo que NO funciona

Crea `lib/contador.dart` e intenta hacerlo con lo que ya sabes:

```dart
import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(home: Contador()));

class Contador extends StatelessWidget {
  Contador({super.key});

  int valor = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Contador')),
      body: Center(child: Text('$valor', style: const TextStyle(fontSize: 48))),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          valor++;
          print(valor);
        },
        child: const Icon(Icons.add),
      ),
    );
  }
}
```

Pulsa el botón y mira la **consola**: el número sube (1, 2, 3…), pero la **pantalla sigue en 0**. Nadie le ha dicho a Flutter que vuelva a dibujar. Además, el editor subraya la clase: un `StatelessWidget` no puede tener datos que cambien.

### Paso 2 · Con estado: `StatefulWidget` y `setState`

Pon el cursor sobre `StatelessWidget`, pulsa la **bombilla** 💡 (o Ctrl+.) y elige **Convert to StatefulWidget**. Después déjalo así:

```dart
import 'package:flutter/material.dart';

void main() => runApp(const MaterialApp(home: Contador()));

class Contador extends StatefulWidget {
  const Contador({super.key});

  @override
  State<Contador> createState() => _ContadorState();
}

class _ContadorState extends State<Contador> {
  int _valor = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Contador')),
      body: Center(child: Text('$_valor', style: const TextStyle(fontSize: 48))),
      floatingActionButton: FloatingActionButton(
        onPressed: () => setState(() => _valor++),
        child: const Icon(Icons.add),
      ),
    );
  }
}
```

Ahora sí cambia. Lo nuevo:

- Son **dos clases**: `Contador` (el widget, que no cambia) y `_ContadorState` (la **memoria**, donde viven los datos que cambian).
- **`setState(() => ...)`** = «cambio este dato **y** vuelve a dibujar». Es lo que en Compose hacía `mutableStateOf` por ti.
- El `_` delante de `_valor` y `_ContadorState` significa **privado** (solo se ve en este fichero).

### Paso 3 · Sumar y restar, sin bajar de 0

**Quita** el `floatingActionButton` (todo el bloque, hasta su `),`) y **sustituye** el `body`:

```dart
body: Center(
  child: Column(
    mainAxisSize: MainAxisSize.min,
    children: [
      Text('$_valor', style: const TextStyle(fontSize: 48)),
      Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          IconButton(
            onPressed: _valor > 0 ? () => setState(() => _valor--) : null,
            icon: const Icon(Icons.remove),
          ),
          IconButton(
            onPressed: () => setState(() => _valor++),
            icon: const Icon(Icons.add),
          ),
        ],
      ),
    ],
  ),
),
```

El botón de restar se **desactiva** en 0: `onPressed: null`, lo vimos en el apartado 2. Se decide en cada `build`.

### Paso 4 · Que cambie el aspecto

Sustituye el `Text` del número por este, que se pone rojo a partir de 10:

```dart
Text(
  '$_valor',
  style: TextStyle(fontSize: 48, color: _valor >= 10 ? Colors.red : Colors.black),
),
```

El `TextStyle` ya no es `const`: depende de `_valor`.

### Paso 5 · Un dato que llega de fuera: `widget.`

Queremos decidir el máximo desde fuera, al crear el contador. **Cambia** la clase `Contador`:

```dart
class Contador extends StatefulWidget {
  const Contador({super.key, this.maximo = 10});
  final int maximo;

  @override
  State<Contador> createState() => _ContadorState();
}
```

En el botón de sumar, **usa** `widget.maximo` para no pasarse:

```dart
onPressed: _valor < widget.maximo ? () => setState(() => _valor++) : null,
```

Y en el `main`, crea el contador con otro máximo. Sin paréntesis vale 10 (el valor por defecto); así vale 5:

```dart
void main() => runApp(const MaterialApp(home: Contador(maximo: 5)));
```

Pulsa hasta 5: el botón de sumar se desactiva.

- Los **parámetros** (lo que llega de fuera) van en la clase del widget, `Contador`.
- Desde el `State` se leen con **`widget.`** delante: `widget.maximo`.

??? example "Código completo de `lib/contador.dart`"
    ```dart
    import 'package:flutter/material.dart';

    void main() => runApp(const MaterialApp(home: Contador(maximo: 5)));

    class Contador extends StatefulWidget {
      const Contador({super.key, this.maximo = 10});
      final int maximo;

      @override
      State<Contador> createState() => _ContadorState();
    }

    class _ContadorState extends State<Contador> {
      int _valor = 0;

      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(title: const Text('Contador')),
          body: Center(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  '$_valor',
                  style: TextStyle(fontSize: 48, color: _valor >= 10 ? Colors.red : Colors.black),
                ),
                Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    IconButton(
                      onPressed: _valor > 0 ? () => setState(() => _valor--) : null,
                      icon: const Icon(Icons.remove),
                    ),
                    IconButton(
                      onPressed: _valor < widget.maximo ? () => setState(() => _valor++) : null,
                      icon: const Icon(Icons.add),
                    ),
                  ],
                ),
              ],
            ),
          ),
        );
      }
    }
    ```

Ahora haz los ejercicios rápidos **R6** y **R7**.

??? info "Para consultar: el ciclo de vida del `State`"
    Lo necesitaréis en los temas 4 y 5.

    | Método | Cuándo se llama | Para qué |
    |---|---|---|
    | `initState()` | Una vez, al crearse | Arrancar cosas: suscribirse a un stream, pedir datos |
    | `build()` | Cada vez que hay que dibujar | Solo describir la interfaz. **Nada pesado aquí** |
    | `dispose()` | Una vez, al destruirse | Liberar: cancelar suscripciones, `controller.dispose()` |

    Si una operación asíncrona termina cuando el usuario ya ha salido de la pantalla, `setState` da error. Comprueba antes `if (!mounted) return;`.

---

## 6. Comunicación entre widgets, paso a paso

Cuando la pantalla crece, se trocea en widgets pequeños. Entonces hay que **pasar datos** entre ellos. Lo vamos a ver con una pantalla para **valorar playas con estrellas** (G2).

### Paso 1 · De padre a hijo: parámetros

Crea `lib/valoracion.dart`. La pantalla (`Valoracion`, el **padre**) crea tres fichas (`FichaPlaya`, los **hijos**) y le pasa a cada una su nombre:

```dart
import 'package:flutter/material.dart';

void main() => runApp(const MaterialApp(home: Valoracion()));

class FichaPlaya extends StatelessWidget {
  const FichaPlaya({super.key, required this.nombre});
  final String nombre;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const Icon(Icons.beach_access),
      title: Text(nombre),
    );
  }
}

class Valoracion extends StatelessWidget {
  const Valoracion({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Valoración de playas')),
      body: ListView(
        children: const [
          FichaPlaya(nombre: 'La Caleta'),
          FichaPlaya(nombre: 'La Victoria'),
          FichaPlaya(nombre: 'Cortadura'),
        ],
      ),
    );
  }
}
```

Los datos **bajan** por el constructor, como los parámetros de una función composable. `required` = es obligatorio pasarlo.

### Paso 2 · Un widget que muestra estrellas

**Añade** esta clase al fichero. Pinta 5 estrellas, rellenas hasta `valor`:

```dart
class Estrellas extends StatelessWidget {
  const Estrellas({super.key, required this.valor});
  final int valor;

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        for (var i = 1; i <= 5; i++)
          Icon(i <= valor ? Icons.star : Icons.star_border, color: Colors.amber),
      ],
    );
  }
}
```

El `for` dentro de la lista es el *collection for* de Dart del Tema 1: crea un hijo por vuelta.

Ahora `FichaPlaya` tiene que recibir la nota y mostrar las estrellas. **Añade** el parámetro `nota` y el `subtitle`:

```dart
class FichaPlaya extends StatelessWidget {
  const FichaPlaya({super.key, required this.nombre, required this.nota});
  final String nombre;
  final int nota;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const Icon(Icons.beach_access),
      title: Text(nombre),
      subtitle: Estrellas(valor: nota),
    );
  }
}
```

Y en `Valoracion`, pasa una nota a cada ficha. **Sustituye** la lista `children`:

```dart
children: const [
  FichaPlaya(nombre: 'La Caleta', nota: 3),
  FichaPlaya(nombre: 'La Victoria', nota: 5),
  FichaPlaya(nombre: 'Cortadura', nota: 1),
],
```

Los datos bajan dos niveles: pantalla → ficha → estrellas.

### Paso 3 · De hijo a padre: *callbacks*

Queremos **pulsar** una estrella para cambiar la nota. Pero el hijo no puede cambiar un dato que le ha dado el padre: tiene que **avisar** al padre. Para eso recibe una **función** y la llama.

**Cambia** `Estrellas`: los `Icon` pasan a ser `IconButton`, y añade el parámetro `alCambiar`:

```dart
class Estrellas extends StatelessWidget {
  const Estrellas({super.key, required this.valor, required this.alCambiar});
  final int valor;
  final ValueChanged<int> alCambiar;   // una función que recibe un int

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        for (var i = 1; i <= 5; i++)
          IconButton(
            onPressed: () => alCambiar(i),   // avisa: «han pulsado la estrella i»
            icon: Icon(i <= valor ? Icons.star : Icons.star_border, color: Colors.amber),
          ),
      ],
    );
  }
}
```

`FichaPlaya` solo hace de intermediaria: recibe la función y se la pasa a las estrellas. **Añade** el parámetro:

```dart
class FichaPlaya extends StatelessWidget {
  const FichaPlaya({super.key, required this.nombre, required this.nota, required this.alCambiar});
  final String nombre;
  final int nota;
  final ValueChanged<int> alCambiar;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: const Icon(Icons.beach_access),
      title: Text(nombre),
      subtitle: Estrellas(valor: nota, alCambiar: alCambiar),
    );
  }
}
```

Para probarlo, en `Valoracion` pasa a cada ficha una función que solo escriba en la consola. **Sustituye** la lista `children`. Fíjate en que ya **no lleva `const`**: una función no es constante.

```dart
children: [
  FichaPlaya(nombre: 'La Caleta', nota: 3, alCambiar: (n) => print('La Caleta: $n')),
  FichaPlaya(nombre: 'La Victoria', nota: 5, alCambiar: (n) => print('La Victoria: $n')),
  FichaPlaya(nombre: 'Cortadura', nota: 1, alCambiar: (n) => print('Cortadura: $n')),
],
```

Pulsa estrellas: la consola recibe el aviso, pero las estrellas **no cambian**. Falta que alguien **guarde** la nota.

### Paso 4 · El padre guarda las notas

Las notas tienen que vivir en el **padre**, que pasa a ser un `StatefulWidget` (bombilla 💡 → *Convert to StatefulWidget*). **Sustituye** la clase `Valoracion` entera:

```dart
class Valoracion extends StatefulWidget {
  const Valoracion({super.key});

  @override
  State<Valoracion> createState() => _ValoracionState();
}

class _ValoracionState extends State<Valoracion> {
  static const playas = ['La Caleta', 'La Victoria', 'Cortadura', 'Santa María del Mar'];
  final _notas = [0, 0, 0, 0];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Valoración de playas')),
      body: ListView.builder(
        itemCount: playas.length,
        itemBuilder: (context, i) => FichaPlaya(
          nombre: playas[i],
          nota: _notas[i],
          alCambiar: (n) => setState(() => _notas[i] = n),
        ),
      ),
    );
  }
}
```

El circuito completo:

1. El usuario pulsa la estrella 4 de La Caleta.
2. `Estrellas` llama a `alCambiar(4)`.
3. El padre ejecuta `setState(() => _notas[0] = 4)`.
4. El padre se redibuja y le pasa a la ficha la nota nueva, que **baja** hasta las estrellas.

**Los datos bajan por parámetros; los avisos suben por funciones.** El estado vive en el padre (*lifting state up*, igual que en Compose).

### Paso 5 · Usar el estado del padre: la media

Como las notas están en el padre, puede usarlas para otras cosas. **Añade** en `_ValoracionState`, debajo de `_notas`:

```dart
double get _media => _notas.reduce((a, b) => a + b) / _notas.length;
```

Y **cambia** el título del `AppBar`:

```dart
appBar: AppBar(title: Text('Media: ${_media.toStringAsFixed(1)} ⭐')),
```

Pulsa estrellas: la media se actualiza sola.

??? example "Código completo de `lib/valoracion.dart`"
    ```dart
    import 'package:flutter/material.dart';

    void main() => runApp(const MaterialApp(home: Valoracion()));

    class Estrellas extends StatelessWidget {
      const Estrellas({super.key, required this.valor, required this.alCambiar});
      final int valor;
      final ValueChanged<int> alCambiar;

      @override
      Widget build(BuildContext context) {
        return Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            for (var i = 1; i <= 5; i++)
              IconButton(
                onPressed: () => alCambiar(i),
                icon: Icon(i <= valor ? Icons.star : Icons.star_border, color: Colors.amber),
              ),
          ],
        );
      }
    }

    class FichaPlaya extends StatelessWidget {
      const FichaPlaya({super.key, required this.nombre, required this.nota, required this.alCambiar});
      final String nombre;
      final int nota;
      final ValueChanged<int> alCambiar;

      @override
      Widget build(BuildContext context) {
        return ListTile(
          leading: const Icon(Icons.beach_access),
          title: Text(nombre),
          subtitle: Estrellas(valor: nota, alCambiar: alCambiar),
        );
      }
    }

    class Valoracion extends StatefulWidget {
      const Valoracion({super.key});

      @override
      State<Valoracion> createState() => _ValoracionState();
    }

    class _ValoracionState extends State<Valoracion> {
      static const playas = ['La Caleta', 'La Victoria', 'Cortadura', 'Santa María del Mar'];
      final _notas = [0, 0, 0, 0];

      double get _media => _notas.reduce((a, b) => a + b) / _notas.length;

      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(title: Text('Media: ${_media.toStringAsFixed(1)} ⭐')),
          body: ListView.builder(
            itemCount: playas.length,
            itemBuilder: (context, i) => FichaPlaya(
              nombre: playas[i],
              nota: _notas[i],
              alCambiar: (n) => setState(() => _notas[i] = n),
            ),
          ),
        );
      }
    }
    ```

Ahora haz el ejercicio rápido **R8**.

### Paso 6 · Datos para toda la app: `ChangeNotifier` + `provider`

Pasar datos por parámetros funciona entre padre e hijo. Pero cuando **varias pantallas** necesitan los mismos datos (el carrito de la compra, el usuario conectado), se vuelve inmanejable. La solución oficial más sencilla:

1. Una clase que **guarda los datos** y **avisa** cuando cambian (`ChangeNotifier`, como un `ViewModel`).
2. El paquete `provider`, que la pone **a disposición de todas las pantallas**.

**6.1 · Instala el paquete.** En la terminal de VS Code:

```bash
flutter pub add provider
```

**6.2 · La clase con los datos.** Crea `lib/carrito.dart`:

```dart
import 'package:flutter/foundation.dart';

class Producto {
  const Producto(this.nombre, this.precio);
  final String nombre;
  final double precio;
}

class Carrito extends ChangeNotifier {
  final List<Producto> _items = [];

  List<Producto> get items => List.unmodifiable(_items);
  int get cantidad => _items.length;
  double get total => _items.fold(0.0, (suma, p) => suma + p.precio);

  void anadir(Producto p) {
    _items.add(p);
    notifyListeners();   // ← avisa a quien esté escuchando
  }

  void quitar(Producto p) {
    _items.remove(p);
    notifyListeners();
  }
}
```

`notifyListeners()` es el `setState` de esta clase: «he cambiado, que se redibujen los que me usan».

**6.3 · Ponerla a disposición de la app.** Crea `lib/tienda.dart`. El `ChangeNotifierProvider` envuelve a toda la app:

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'carrito.dart';

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (_) => Carrito(),   // se crea una vez para toda la app
      child: const MaterialApp(home: Tienda()),
    ),
  );
}

class Tienda extends StatelessWidget {
  const Tienda({super.key});

  static const catalogo = [
    Producto('Tortillitas de camarones', 6.5),
    Producto('Papas aliñás', 4.0),
    Producto('Chicharrones', 5.5),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Tienda')),
      body: ListView(
        children: [
          for (final p in catalogo)
            ListTile(
              title: Text(p.nombre),
              subtitle: Text('${p.precio.toStringAsFixed(2)} €'),
              trailing: IconButton(
                icon: const Icon(Icons.add_shopping_cart),
                onPressed: () => context.read<Carrito>().anadir(p),
              ),
            ),
        ],
      ),
    );
  }
}
```

`context.read<Carrito>()` = «dame el carrito» para usarlo. Pulsa los botones: se añaden productos… pero aún no se ve nada.

**6.4 · Ver el carrito: `watch`.** **Añade** al principio del `build` de `Tienda`:

```dart
final carrito = context.watch<Carrito>();   // watch = me redibujo si cambia
```

Y **cambia** el `AppBar` para que muestre cuántos productos hay, y **añade** el total abajo del `Scaffold`:

```dart
appBar: AppBar(
  title: const Text('Tienda'),
  actions: [
    Badge(
      label: Text('${carrito.cantidad}'),
      child: const Icon(Icons.shopping_cart),
    ),
    const SizedBox(width: 16),
  ],
),
```

```dart
bottomNavigationBar: Padding(
  padding: const EdgeInsets.all(16),
  child: Text('Total: ${carrito.total.toStringAsFixed(2)} €',
      style: Theme.of(context).textTheme.titleLarge),
),
```

Así queda la clase `Tienda` completa después de este paso:

```dart
class Tienda extends StatelessWidget {
  const Tienda({super.key});

  static const catalogo = [
    Producto('Tortillitas de camarones', 6.5),
    Producto('Papas aliñás', 4.0),
    Producto('Chicharrones', 5.5),
  ];

  @override
  Widget build(BuildContext context) {
    final carrito = context.watch<Carrito>();

    return Scaffold(
      appBar: AppBar(
        title: const Text('Tienda'),
        actions: [
          Badge(
            label: Text('${carrito.cantidad}'),
            child: const Icon(Icons.shopping_cart),
          ),
          const SizedBox(width: 16),
        ],
      ),
      body: ListView(
        children: [
          for (final p in catalogo)
            ListTile(
              title: Text(p.nombre),
              subtitle: Text('${p.precio.toStringAsFixed(2)} €'),
              trailing: IconButton(
                icon: const Icon(Icons.add_shopping_cart),
                onPressed: () => context.read<Carrito>().anadir(p),
              ),
            ),
        ],
      ),
      bottomNavigationBar: Padding(
        padding: const EdgeInsets.all(16),
        child: Text('Total: ${carrito.total.toStringAsFixed(2)} €',
            style: Theme.of(context).textTheme.titleLarge),
      ),
    );
  }
}
```

Pulsa los botones: el contador y el total cambian solos.

| Llamada | Qué hace | Dónde se usa |
|---|---|---|
| `context.watch<T>()` | Obtiene el objeto **y** redibuja el widget cuando cambia | En `build` |
| `context.read<T>()` | Obtiene el objeto **sin** redibujar | En `onPressed`, `initState`… |

En el paso 6 de la navegación llevaremos el carrito a otra pantalla. Ahora haz el ejercicio rápido **R13**.

---

## 7. Navegación, paso a paso

Vamos a pasar de una pantalla a otra: una lista de playas que abre el detalle de cada una (G4).

### Paso 1 · Dos pantallas: ir con `Navigator.push`

Crea `lib/navegacion.dart`:

```dart
import 'package:flutter/material.dart';

void main() => runApp(const MaterialApp(home: ListaPlayas()));

class ListaPlayas extends StatelessWidget {
  const ListaPlayas({super.key});

  static const playas = ['La Caleta', 'Santa María del Mar', 'La Victoria', 'Cortadura'];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Playas de Cádiz')),
      body: ListView.builder(
        itemCount: playas.length,
        itemBuilder: (context, i) => ListTile(
          title: Text(playas[i]),
          trailing: const Icon(Icons.chevron_right),
          onTap: () => Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => DetallePlaya(nombre: playas[i])),
          ),
        ),
      ),
    );
  }
}

class DetallePlaya extends StatelessWidget {
  const DetallePlaya({super.key, required this.nombre});
  final String nombre;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(nombre)),
      body: const Center(
        child: Icon(Icons.beach_access, size: 96, color: Colors.orange),
      ),
    );
  }
}
```

- `Navigator.push` **abre** una pantalla nueva encima de la actual.
- `MaterialPageRoute(builder: ...)` dice **qué pantalla** abrir, con la animación de cada plataforma.
- Los datos se pasan **por el constructor**, como a cualquier widget: `DetallePlaya(nombre: playas[i])`.
- La **flecha** del `AppBar` y el botón atrás de Android vuelven solos.

### Paso 2 · Volver con un botón: `Navigator.pop`

En `DetallePlaya`, **sustituye** el `body`:

```dart
body: Center(
  child: Column(
    mainAxisSize: MainAxisSize.min,
    children: [
      const Icon(Icons.beach_access, size: 96, color: Colors.orange),
      const SizedBox(height: 24),
      TextButton(
        onPressed: () => Navigator.pop(context),
        child: const Text('Volver'),
      ),
    ],
  ),
),
```

Las pantallas funcionan como una **pila**: `push` pone una encima y `pop` quita la de arriba.

### Paso 3 · Volver con un resultado

Queremos marcar playas como **favoritas** desde el detalle. `pop` puede llevar un dato de vuelta. En `DetallePlaya`, **añade** un botón antes del `TextButton`. El `body` queda así:

```dart
body: Center(
  child: Column(
    mainAxisSize: MainAxisSize.min,
    children: [
      const Icon(Icons.beach_access, size: 96, color: Colors.orange),
      const SizedBox(height: 24),
      FilledButton.icon(
        onPressed: () => Navigator.pop(context, true),   // vuelve devolviendo true
        icon: const Icon(Icons.favorite),
        label: const Text('Marcar como favorita'),
      ),
      TextButton(
        onPressed: () => Navigator.pop(context),
        child: const Text('Volver'),
      ),
    ],
  ),
),
```

La lista tiene que **recordar** cuáles son favoritas, así que pasa a ser `StatefulWidget` (bombilla 💡 → *Convert to StatefulWidget*). **Sustituye** la clase `ListaPlayas` entera:

```dart
class ListaPlayas extends StatefulWidget {
  const ListaPlayas({super.key});

  @override
  State<ListaPlayas> createState() => _ListaPlayasState();
}

class _ListaPlayasState extends State<ListaPlayas> {
  static const playas = ['La Caleta', 'Santa María del Mar', 'La Victoria', 'Cortadura'];
  final _favoritas = <String>{};

  Future<void> _abrir(String playa) async {
    final favorita = await Navigator.push<bool>(
      context,
      MaterialPageRoute(builder: (context) => DetallePlaya(nombre: playa)),
    );
    if (favorita == true && mounted) {
      setState(() => _favoritas.add(playa));
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Playas de Cádiz')),
      body: ListView.builder(
        itemCount: playas.length,
        itemBuilder: (context, i) => ListTile(
          title: Text(playas[i]),
          trailing: _favoritas.contains(playas[i])
              ? const Icon(Icons.favorite, color: Colors.red)
              : const Icon(Icons.chevron_right),
          onTap: () => _abrir(playas[i]),
        ),
      ),
    );
  }
}
```

- `push` devuelve un **`Future`**: se completa cuando la otra pantalla hace `pop`, con el dato que le pase. Por eso lleva `await`, como en el Tema 1.
- Si se vuelve con la flecha, el resultado es `null`. Por eso se compara con `== true`.
- `<String>{}` es un conjunto (`Set`): no admite repetidos.

??? example "Código completo de `lib/navegacion.dart`"
    ```dart
    import 'package:flutter/material.dart';

    void main() => runApp(const MaterialApp(home: ListaPlayas()));

    class ListaPlayas extends StatefulWidget {
      const ListaPlayas({super.key});

      @override
      State<ListaPlayas> createState() => _ListaPlayasState();
    }

    class _ListaPlayasState extends State<ListaPlayas> {
      static const playas = ['La Caleta', 'Santa María del Mar', 'La Victoria', 'Cortadura'];
      final _favoritas = <String>{};

      Future<void> _abrir(String playa) async {
        final favorita = await Navigator.push<bool>(
          context,
          MaterialPageRoute(builder: (context) => DetallePlaya(nombre: playa)),
        );
        if (favorita == true && mounted) {
          setState(() => _favoritas.add(playa));
        }
      }

      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(title: const Text('Playas de Cádiz')),
          body: ListView.builder(
            itemCount: playas.length,
            itemBuilder: (context, i) => ListTile(
              title: Text(playas[i]),
              trailing: _favoritas.contains(playas[i])
                  ? const Icon(Icons.favorite, color: Colors.red)
                  : const Icon(Icons.chevron_right),
              onTap: () => _abrir(playas[i]),
            ),
          ),
        );
      }
    }

    class DetallePlaya extends StatelessWidget {
      const DetallePlaya({super.key, required this.nombre});
      final String nombre;

      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(title: Text(nombre)),
          body: Center(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                const Icon(Icons.beach_access, size: 96, color: Colors.orange),
                const SizedBox(height: 24),
                FilledButton.icon(
                  onPressed: () => Navigator.pop(context, true),
                  icon: const Icon(Icons.favorite),
                  label: const Text('Marcar como favorita'),
                ),
                TextButton(
                  onPressed: () => Navigator.pop(context),
                  child: const Text('Volver'),
                ),
              ],
            ),
          ),
        );
      }
    }
    ```

Ahora haz los ejercicios rápidos **R9**, **R10** y **R11**.

### Paso 4 · Pestañas abajo: `NavigationBar`

Para cambiar entre secciones sin apilar pantallas se usa una barra inferior. Crea `lib/pestanas.dart`:

```dart
import 'package:flutter/material.dart';

void main() => runApp(const MaterialApp(home: Inicio()));

class Inicio extends StatefulWidget {
  const Inicio({super.key});

  @override
  State<Inicio> createState() => _InicioState();
}

class _InicioState extends State<Inicio> {
  int _indice = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(child: Text('Pestaña $_indice', style: const TextStyle(fontSize: 32))),
      bottomNavigationBar: NavigationBar(
        selectedIndex: _indice,
        onDestinationSelected: (i) => setState(() => _indice = i),
        destinations: const [
          NavigationDestination(icon: Icon(Icons.store), label: 'Catálogo'),
          NavigationDestination(icon: Icon(Icons.shopping_cart), label: 'Carrito'),
          NavigationDestination(icon: Icon(Icons.person), label: 'Perfil'),
        ],
      ),
    );
  }
}
```

La pestaña elegida es **estado local**: un número (`_indice`) y un `setState` al tocar, como el contador.

### Paso 5 · Una pantalla distinta en cada pestaña

**Añade** en `_InicioState`, debajo de `_indice`, la lista de pantallas:

```dart
static const _pantallas = [
  Center(child: Text('Catálogo')),
  Center(child: Text('Carrito')),
  Center(child: Text('Perfil')),
];
```

Y **cambia** el `body` para que muestre la de la pestaña elegida:

```dart
body: _pantallas[_indice],
```

En una app real, cada elemento de la lista sería una pantalla completa, por ejemplo `ListaPlayas()`.

??? example "Código completo de `lib/pestanas.dart`"
    ```dart
    import 'package:flutter/material.dart';

    void main() => runApp(const MaterialApp(home: Inicio()));

    class Inicio extends StatefulWidget {
      const Inicio({super.key});

      @override
      State<Inicio> createState() => _InicioState();
    }

    class _InicioState extends State<Inicio> {
      int _indice = 0;

      static const _pantallas = [
        Center(child: Text('Catálogo')),
        Center(child: Text('Carrito')),
        Center(child: Text('Perfil')),
      ];

      @override
      Widget build(BuildContext context) {
        return Scaffold(
          body: _pantallas[_indice],
          bottomNavigationBar: NavigationBar(
            selectedIndex: _indice,
            onDestinationSelected: (i) => setState(() => _indice = i),
            destinations: const [
              NavigationDestination(icon: Icon(Icons.store), label: 'Catálogo'),
              NavigationDestination(icon: Icon(Icons.shopping_cart), label: 'Carrito'),
              NavigationDestination(icon: Icon(Icons.person), label: 'Perfil'),
            ],
          ),
        );
      }
    }
    ```

Ahora haz el ejercicio rápido **R12**.

### Paso 6 · El carrito en otra pantalla (G3)

Volvemos a `lib/tienda.dart`, la del paso 6 del apartado anterior. **Añade** al final del fichero una pantalla que lista el carrito:

```dart
class PantallaCarrito extends StatelessWidget {
  const PantallaCarrito({super.key});

  @override
  Widget build(BuildContext context) {
    final carrito = context.watch<Carrito>();

    return Scaffold(
      appBar: AppBar(title: const Text('Mi carrito')),
      body: carrito.items.isEmpty
          ? const Center(child: Text('El carrito está vacío'))
          : ListView(
              children: [
                for (final p in carrito.items)
                  ListTile(
                    title: Text(p.nombre),
                    trailing: IconButton(
                      icon: const Icon(Icons.delete),
                      onPressed: () => context.read<Carrito>().quitar(p),
                    ),
                  ),
              ],
            ),
    );
  }
}
```

En el `AppBar` de `Tienda`, **sustituye** el `Badge` por un botón que abra esa pantalla:

```dart
IconButton(
  onPressed: () => Navigator.push(
    context,
    MaterialPageRoute(builder: (context) => const PantallaCarrito()),
  ),
  icon: Badge(
    label: Text('${carrito.cantidad}'),
    child: const Icon(Icons.shopping_cart),
  ),
),
```

Añade productos, abre el carrito, borra alguno y vuelve: el contador de la tienda está actualizado. **Las dos pantallas comparten el mismo `Carrito`** sin pasarse nada por parámetros: eso es lo que da `provider`.

??? example "Código completo de `lib/tienda.dart`"
    ```dart
    import 'package:flutter/material.dart';
    import 'package:provider/provider.dart';
    import 'carrito.dart';

    void main() {
      runApp(
        ChangeNotifierProvider(
          create: (_) => Carrito(),
          child: const MaterialApp(home: Tienda()),
        ),
      );
    }

    class Tienda extends StatelessWidget {
      const Tienda({super.key});

      static const catalogo = [
        Producto('Tortillitas de camarones', 6.5),
        Producto('Papas aliñás', 4.0),
        Producto('Chicharrones', 5.5),
      ];

      @override
      Widget build(BuildContext context) {
        final carrito = context.watch<Carrito>();

        return Scaffold(
          appBar: AppBar(
            title: const Text('Tienda'),
            actions: [
              IconButton(
                onPressed: () => Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => const PantallaCarrito()),
                ),
                icon: Badge(
                  label: Text('${carrito.cantidad}'),
                  child: const Icon(Icons.shopping_cart),
                ),
              ),
              const SizedBox(width: 16),
            ],
          ),
          body: ListView(
            children: [
              for (final p in catalogo)
                ListTile(
                  title: Text(p.nombre),
                  subtitle: Text('${p.precio.toStringAsFixed(2)} €'),
                  trailing: IconButton(
                    icon: const Icon(Icons.add_shopping_cart),
                    onPressed: () => context.read<Carrito>().anadir(p),
                  ),
                ),
            ],
          ),
          bottomNavigationBar: Padding(
            padding: const EdgeInsets.all(16),
            child: Text('Total: ${carrito.total.toStringAsFixed(2)} €',
                style: Theme.of(context).textTheme.titleLarge),
          ),
        );
      }
    }

    class PantallaCarrito extends StatelessWidget {
      const PantallaCarrito({super.key});

      @override
      Widget build(BuildContext context) {
        final carrito = context.watch<Carrito>();

        return Scaffold(
          appBar: AppBar(title: const Text('Mi carrito')),
          body: carrito.items.isEmpty
              ? const Center(child: Text('El carrito está vacío'))
              : ListView(
                  children: [
                    for (final p in carrito.items)
                      ListTile(
                        title: Text(p.nombre),
                        trailing: IconButton(
                          icon: const Icon(Icons.delete),
                          onPressed: () => context.read<Carrito>().quitar(p),
                        ),
                      ),
                  ],
                ),
        );
      }
    }
    ```

??? info "Para consultar: otras formas de navegar"
    - `Drawer`: menú lateral, con `Scaffold(drawer: Drawer(...))`.
    - `TabBar` + `TabBarView`: pestañas arriba.
    - `go_router`: para apps grandes o para web (URLs con rutas). En este módulo basta con `Navigator`; si os sobra tiempo en el proyecto final, investigadlo.

---

## 8. Formularios y validación

```dart
class Registro extends StatefulWidget {
  const Registro({super.key});
  @override
  State<Registro> createState() => _RegistroState();
}

class _RegistroState extends State<Registro> {
  final _formKey = GlobalKey<FormState>();       // identifica el formulario
  final _nombre = TextEditingController();
  final _email = TextEditingController();
  String _ciclo = 'DAM';
  bool _acepto = false;

  @override
  void dispose() {                               // ¡liberar los controladores!
    _nombre.dispose();
    _email.dispose();
    super.dispose();
  }

  void _enviar() {
    if (!_formKey.currentState!.validate()) return;   // ejecuta todos los validator
    if (!_acepto) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Debes aceptar las condiciones')),
      );
      return;
    }
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text('Bienvenido/a, ${_nombre.text} ($_ciclo)')),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Registro')),
      body: Form(
        key: _formKey,
        child: ListView(
          padding: const EdgeInsets.all(16),
          children: [
            TextFormField(
              controller: _nombre,
              decoration: const InputDecoration(labelText: 'Nombre', border: OutlineInputBorder()),
              validator: (v) => (v == null || v.trim().length < 2) ? 'Mínimo 2 caracteres' : null,
            ),
            const SizedBox(height: 16),
            TextFormField(
              controller: _email,
              keyboardType: TextInputType.emailAddress,
              decoration: const InputDecoration(labelText: 'Email', border: OutlineInputBorder()),
              validator: (v) {
                if (v == null || v.isEmpty) return 'Obligatorio';
                if (!RegExp(r'^[^@\s]+@[^@\s]+\.[^@\s]+$').hasMatch(v)) return 'Email no válido';
                return null;                     // null = válido
              },
            ),
            const SizedBox(height: 16),
            DropdownButtonFormField<String>(
              initialValue: _ciclo,
              decoration: const InputDecoration(labelText: 'Ciclo', border: OutlineInputBorder()),
              items: const [
                DropdownMenuItem(value: 'DAM', child: Text('DAM')),
                DropdownMenuItem(value: 'DAW', child: Text('DAW')),
                DropdownMenuItem(value: 'ASIR', child: Text('ASIR')),
              ],
              onChanged: (v) => setState(() => _ciclo = v!),
            ),
            CheckboxListTile(
              value: _acepto,
              onChanged: (v) => setState(() => _acepto = v ?? false),
              title: const Text('Acepto las condiciones'),
            ),
            FilledButton(onPressed: _enviar, child: const Text('Enviar')),
          ],
        ),
      ),
    );
  }
}
```

| Pieza | Para qué |
|---|---|
| `GlobalKey<FormState>` | Permite llamar a `validate()` y `reset()` del formulario |
| `TextEditingController` | Leer (`.text`) y cambiar el texto de un campo. **Se libera en `dispose`** |
| `validator` | Devuelve `null` si es válido, o el **mensaje de error** |
| `keyboardType` | Teclado numérico, de email, de teléfono… |
| `obscureText: true` | Campo de contraseña |
| `SnackBar` | Mensaje breve en la parte inferior |

!!! note "Si tu versión de Flutter se queja de `initialValue`"
    En versiones antiguas de Flutter el parámetro de `DropdownButtonFormField` se llamaba `value`. Si el analizador marca `initialValue` como desconocido, cámbialo por `value`.

---

## 9. Tema, modo oscuro y diseño adaptable

### Tema

```dart
MaterialApp(
  theme: ThemeData(colorSchemeSeed: Colors.indigo),                                  // claro
  darkTheme: ThemeData(colorSchemeSeed: Colors.indigo, brightness: Brightness.dark), // oscuro
  themeMode: ThemeMode.system,        // sigue al sistema (también .light / .dark)
  home: const Inicio(),
)
```

Dentro de un widget, usa los colores y estilos del tema en lugar de valores fijos:

```dart
Text('Título', style: Theme.of(context).textTheme.headlineSmall)
Container(color: Theme.of(context).colorScheme.primaryContainer)
```

### Diseño adaptable

Los criterios de diseño (puntos de corte, mobile-first, responsive frente a adaptativo) están en [Tema 2 · Diseñar la app](../tema2/05-diseno.md). Aquí los aplicamos.

Una app multiplataforma se verá en un móvil, en una tablet y en un monitor. `LayoutBuilder` te dice cuánto espacio hay:

```dart
LayoutBuilder(
  builder: (context, constraints) {
    if (constraints.maxWidth < 600) {
      return const ListaProductos();            // móvil: lista
    }
    final columnas = constraints.maxWidth < 1000 ? 3 : 5;
    return RejillaProductos(columnas: columnas); // tablet o escritorio: cuadrícula
  },
)
```

`MediaQuery.sizeOf(context)` da el tamaño de toda la pantalla y `MediaQuery.orientationOf(context)` la orientación.

!!! tip "Pruébalo en escritorio o en Chrome"
    La forma más rápida de probar el diseño adaptable es ejecutar en Chrome o en escritorio y **cambiar el tamaño de la ventana**: la interfaz se reorganiza en directo.

---

## Ejercicios rápidos de clase { #ejercicios-rapidos }

Cortos (5-15 minutos). Se hacen **en clase**, justo después de explicar cada apartado, y se corrigen en voz alta. No se entregan: son el entrenamiento para el boletín y las prácticas.

### Widgets, layout, listas, estado y comunicación (apartados 2 a 6)

| # | Ejercicio | Apartado |
|---|---|---|
| R1 | **Tres estilos.** Tu nombre tres veces: grande y en negrita, con el color primario del tema (`Theme.of(context).colorScheme.primary`) y en cursiva gris | 2 |
| R2 | **Fila de iconos.** Un `Row` con 5 iconos repartidos con `spaceEvenly`. Después cambia a un `Wrap` con 15 `Chip` y estrecha la ventana | 3 |
| R3 | **Bandera de Andalucía.** Tres franjas (verde, blanca, verde) que ocupen toda la pantalla con `Column` + `Expanded`. Después hazla vertical con `Row` | 3 |
| R4 | **Avatar con aviso.** Un `CircleAvatar` grande con un circulito rojo y un número en la esquina superior derecha (`Stack` + `Positioned`) | 3 |
| R5 | **Lista de 100.** `ListView.builder` con 100 elementos; los pares con fondo gris claro y los múltiplos de 10 en negrita | 4 |
| R6 | **Me gusta.** Un corazón que se rellena y se vacía al tocarlo, con el número de «me gusta» al lado | 5 |
| R7 | **Luz de la habitación.** Un `Switch` que cambia el fondo de la pantalla entre amarillo y gris oscuro | 5 |
| R8 | **Botones que suman.** Un widget `BotonNumero(valor: n, alPulsar: ...)`. El padre pinta cinco (1, 2, 5, 10, 20) y muestra la suma total | 6 |

### Navegación, `provider`, formularios y diseño (apartados 6 a 9)

| # | Ejercicio | Apartado |
|---|---|---|
| R9 | **Acerca de.** Un botón que abre una pantalla «Acerca de» con tu nombre; vuelve con la flecha y con un botón propio | 7 |
| R10 | **Ciudades.** Lista de 5 ciudades de la provincia; al tocar una se abre su detalle con el nombre en el `AppBar` | 7 |
| R11 | **¿Cómo te llamas?** La pantalla B tiene un `TextField` y devuelve el texto al volver; la pantalla A lo muestra | 7 |
| R12 | **Tres pestañas.** `NavigationBar` con 3 pestañas y un texto que diga cuántas veces se ha visitado cada una | 7 |
| R13 | **Contador global.** Un `ChangeNotifier` con un contador; se suma en la pantalla A y se ve actualizado en la B | 6 |
| R14 | **Código postal.** `TextFormField` que solo acepte 5 dígitos que empiecen por `11` (provincia de Cádiz) | 8 |
| R15 | **Ver contraseña.** Campo de contraseña con un icono de ojo que muestra u oculta el texto (`obscureText` + `suffixIcon`) | 8 |
| R16 | **¿Qué pantalla soy?** Con `LayoutBuilder`, muestra «móvil», «tablet» o «escritorio» según el ancho. Pruébalo en Chrome cambiando el tamaño de la ventana | 9 |

---

## Boletín de ejercicios { #boletin-de-ejercicios }

!!! abstract "Instrucciones"
    - **Individual.** Un único proyecto Flutter `boletin_t3` con una pantalla de inicio que lleve a cada ejercicio (un `ListView` de `ListTile`, uno por ejercicio: ¡así practicas la navegación desde el primer día!).
    - **Entrega:** enlace al repositorio de GitHub. **Fecha:** domingo 22 de noviembre.
    - **Tiempo orientativo:** 20-30 min por ejercicio.

| # | Ejercicio | Practica |
|---|---|---|
| B1 | **Tarjeta de visita.** Tu tarjeta: foto (asset), nombre, ciclo, email y teléfono con iconos, y una fila de 3 iconos de redes. Centrada y con `Card` | Widgets básicos, assets, `Row`/`Column` |
| B2 | **Teclado de calculadora.** Solo la interfaz: pantalla de resultado arriba y rejilla de botones 4×5 que ocupe todo el espacio restante sin desbordar en ningún tamaño de ventana | `Expanded`, `GridView` o `Row`/`Column` anidados |
| B3 | **Carta de la freiduría.** `ListView.separated` con 12 platos (nombre, precio, icono de categoría). Los de más de 10 € llevan una etiqueta «Especialidad» | `ListView.separated`, *collection if* |
| B4 | **Semáforo.** Tres círculos; un botón «Siguiente» enciende el siguiente color (rojo → verde → ámbar → rojo). El apagado se ve gris | `StatefulWidget`, `setState` |
| B5 | **Contador con límites.** Reutiliza el widget `Contador` del apartado 5 tres veces con máximos distintos (5, 10, 20). Añade un botón «Reiniciar todos» en el padre | Parámetros, estado en el padre, *callbacks* |
| B6 | **Encuesta de satisfacción.** 4 preguntas con el widget `Estrellas`. Un botón «Enviar» muestra un `SnackBar` con la media y se desactiva si alguna pregunta está sin contestar | *Lifting state up*, botón desactivado |
| B7 | **Lista de la compra con `provider`.** Un `ChangeNotifier` con la lista. Pantalla 1: añadir productos con un `TextField`. Pantalla 2: ver la lista y tachar lo comprado. Un `Badge` con los pendientes en el `AppBar` | `ChangeNotifier`, `watch`/`read`, navegación |
| B8 | **Selector de color.** Pantalla A con un cuadrado de color; al pulsarlo se abre la pantalla B con 8 colores; al elegir uno se vuelve a A y el cuadrado cambia | `Navigator.push` con resultado |
| B9 | **Registro validado.** Formulario con nombre, email, contraseña, repetir contraseña (deben coincidir), edad (número entre 16 y 99) y un `Switch` de «recibir novedades». Al enviar, muestra un resumen en una pantalla nueva | `Form`, `validator`, controladores, `dispose` |
| B10 | **Galería adaptable.** 30 imágenes de `https://picsum.photos/id/<n>/300/300`. Menos de 600 px: lista; 600-1000: 3 columnas; más de 1000: 5. Un `IconButton` en el `AppBar` cambia entre modo claro y oscuro | `LayoutBuilder`, `GridView.builder`, `themeMode` |

---

## Alta de clientes (guiado) { #practica-32-alta-de-clientes }

!!! abstract "Cómo se trabaja"
    - **Ejercicio guiado en clase, no evaluable** · RA2 · CE a, c
    - Se añade al proyecto `cadiz_market` como cuarta pestaña «Clientes»

1. Lista de clientes (nombre, email, teléfono, tipo: particular o empresa) gestionada con un `ChangeNotifier` propio.
2. Botón flotante que abre un **formulario de alta** con validación: nombre obligatorio, email válido, teléfono de 9 dígitos que empiece por 6, 7, 8 o 9, tipo con `DropdownButtonFormField` y, si es empresa, un campo CIF obligatorio que **solo aparece** cuando se elige «empresa».
3. Al tocar un cliente se abre el **mismo formulario relleno** para editarlo (reutiliza el widget pasando un `Cliente?` opcional).
4. Deslizar un cliente para borrarlo (`Dismissible`), con un `SnackBar` que permita **deshacer**.

| Criterio | Peso |
|---|---|
| Validaciones correctas (incluido el CIF condicional) | 35 % |
| Alta y edición reutilizando el mismo formulario | 30 % |
| Borrado con deshacer | 20 % |
| Controladores liberados y código limpio | 15 % |
