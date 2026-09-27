# Tema 3 · Interfaces y navegación

!!! abstract "Ficha del tema"
    - **Duración:** 2 sesiones (9 y 16 de noviembre)
    - **RA:** RA2 · CE a (interfaces interactivas y adaptables) · CE c (estado) · CE e (navegación) · también RA1 · CE e (diseño responsive, apartado 9)
    - **Actividades:** [16 ejercicios rápidos de clase](#ejercicios-rapidos) · 4 guiados · [Boletín de 10 ejercicios](#boletin-de-ejercicios) · [Práctica 3.1 · Cádiz Market](#practica-31-cadiz-market) · [Práctica 3.2 · Alta de clientes](#practica-32-alta-de-clientes)

!!! info "Ya lo conoces (DI)"
    En Desarrollo de Interfaces ya habéis hecho interfaces **declarativas** con Jetpack Compose: funciones que describen la pantalla, anidadas, que se redibujan cuando cambia el estado. **No lo volvemos a explicar.** En este tema **traducimos** lo que sabéis a Flutter y nos centramos en lo que cambia.

| Sesión | Contenido | En clase |
|---|---|---|
| **1 · 9 nov** | Widgets básicos, layout, listas, estado local, comunicación entre widgets | Rápidos R1-R8 · Guiados G1-G2 · Boletín B1-B6 |
| **2 · 16 nov** | Estado compartido con `provider`, navegación, formularios, tema y diseño adaptable | Rápidos R9-R16 · Guiados G3-G4 · Boletín B7-B10 · Prácticas |

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

## 2. Widgets básicos

Todo lo que se ve en pantalla es un **widget**, y los widgets se anidan con `child:` (un hijo) o `children:` (varios).

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
          const Text('Texto con estilo',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
          const SizedBox(height: 12),
          const Icon(Icons.beach_access, size: 48, color: Colors.orange),
          const SizedBox(height: 12),
          Image.network('https://picsum.photos/400/200', height: 150, fit: BoxFit.cover),
          const SizedBox(height: 12),
          ElevatedButton(onPressed: () {}, child: const Text('ElevatedButton')),
          FilledButton(onPressed: () {}, child: const Text('FilledButton')),
          OutlinedButton(onPressed: () {}, child: const Text('OutlinedButton')),
          TextButton(onPressed: null, child: const Text('Desactivado (onPressed: null)')),
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

### Imágenes propias (assets)

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

!!! tip "`const` delante de todo lo que no cambie"
    Un widget `const` se crea una vez y Flutter no lo reconstruye. El analizador te lo sugiere con una línea azul: acéptalo siempre.

---

## 3. Layout: colocar cosas

### `Row` y `Column`

```dart
Column(
  mainAxisAlignment: MainAxisAlignment.center,   // eje principal (vertical en Column)
  crossAxisAlignment: CrossAxisAlignment.start,  // eje cruzado (horizontal en Column)
  children: [ ... ],
)
```

| | `Row` | `Column` |
|---|---|---|
| Eje principal (`mainAxisAlignment`) | Horizontal | Vertical |
| Eje cruzado (`crossAxisAlignment`) | Vertical | Horizontal |

Valores de `mainAxisAlignment`: `start`, `center`, `end`, `spaceBetween`, `spaceAround`, `spaceEvenly`.

### `Expanded` y `Flexible`: repartir el espacio

```dart
Row(
  children: [
    Expanded(flex: 2, child: Container(height: 50, color: Colors.red)),   // 2/3
    Expanded(flex: 1, child: Container(height: 50, color: Colors.blue)),  // 1/3
  ],
)
```

### Los demás contenedores

| Widget | Para qué |
|---|---|
| `Container` | Tamaño, color, bordes, márgenes y relleno en uno |
| `Padding` | Solo relleno |
| `SizedBox` | Tamaño fijo o separador (`SizedBox(height: 16)`) |
| `Center` / `Align` | Centrar o alinear un hijo |
| `Stack` + `Positioned` | Superponer widgets (un texto sobre una imagen) |
| `Wrap` | Como `Row`, pero salta de línea si no cabe (etiquetas, chips) |
| `SafeArea` | Evita la muesca y la barra de estado |

```dart
Container(
  margin: const EdgeInsets.all(8),
  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
  decoration: BoxDecoration(
    color: Colors.amber.shade100,
    borderRadius: BorderRadius.circular(12),
    border: Border.all(color: Colors.amber),
  ),
  child: const Text('Oferta del día'),
)
```

!!! warning "Las franjas amarillas y negras"
    Si ves una franja amarilla y negra con *"A RenderFlex overflowed by 42 pixels"*, el contenido **no cabe**. Soluciones típicas: envolver en `Expanded`, usar `Wrap`, o meter la columna en un `SingleChildScrollView` / `ListView`.

!!! example "G1 · Guiado en clase: tarjeta de agrupación"
    Construye entre todos esta tarjeta con `Card`, `Row`, `Column`, `Expanded` y `Wrap`:

    ```text
    ┌─────────────────────────────────────────────┐
    │ [icono]  Los Yesterday            ⭐ 342 pts │
    │          Chirigota · Autor: Anónimo           │
    │  [Humor] [Final] [2026]                       │
    └─────────────────────────────────────────────┘
    ```

---

## 4. Listas

Para listas largas **siempre** `ListView.builder`: solo construye los elementos que se ven en pantalla (como `LazyColumn`).

```dart
class ListaPlayas extends StatelessWidget {
  const ListaPlayas({super.key});

  static const playas = ['La Caleta', 'Santa María del Mar', 'La Victoria', 'Cortadura'];

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: playas.length,
      itemBuilder: (context, i) => ListTile(
        leading: CircleAvatar(child: Text('${i + 1}')),
        title: Text(playas[i]),
        onTap: () => ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Has elegido ${playas[i]}')),
        ),
      ),
    );
  }
}
```

| Variante | Cuándo |
|---|---|
| `ListView(children: [...])` | Pocos elementos fijos |
| `ListView.builder` | Muchos elementos o datos que vienen de una lista |
| `ListView.separated` | Con separador entre elementos (`separatorBuilder`) |
| `GridView.builder` | Cuadrícula. `gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2)` |

---

## 5. Estado local: `StatefulWidget` y `setState`

```dart
class Contador extends StatefulWidget {
  const Contador({super.key, this.maximo = 10});
  final int maximo;                           // parámetro que llega de fuera

  @override
  State<Contador> createState() => _ContadorState();
}

class _ContadorState extends State<Contador> {
  int _valor = 0;                             // estado que cambia

  void _sumar() {
    if (_valor < widget.maximo) {             // "widget." accede a los parámetros
      setState(() => _valor++);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        IconButton(
          onPressed: _valor > 0 ? () => setState(() => _valor--) : null,
          icon: const Icon(Icons.remove),
        ),
        Text('$_valor', style: const TextStyle(fontSize: 24)),
        IconButton(
          onPressed: _valor < widget.maximo ? _sumar : null,
          icon: const Icon(Icons.add),
        ),
      ],
    );
  }
}
```

**Ciclo de vida** del `State` (lo necesitaréis en los temas 4 y 5):

| Método | Cuándo se llama | Para qué |
|---|---|---|
| `initState()` | Una vez, al crearse | Arrancar cosas: suscribirse a un stream, pedir datos |
| `build()` | Cada vez que hay que dibujar | Solo describir la interfaz. **Nada pesado aquí** |
| `dispose()` | Una vez, al destruirse | Liberar: cancelar suscripciones, `controller.dispose()` |

!!! warning "Nunca llames a `setState` fuera de un `State` montado"
    Si una operación asíncrona termina cuando el usuario ya ha salido de la pantalla, `setState` da error. Comprueba antes `if (!mounted) return;`.

---

## 6. Comunicación entre widgets

### De padre a hijo: parámetros del constructor

Como los parámetros de una función composable en Compose:

```dart
class Etiqueta extends StatelessWidget {
  const Etiqueta({super.key, required this.texto, this.color = Colors.blue});
  final String texto;
  final Color color;

  @override
  Widget build(BuildContext context) => Chip(label: Text(texto), backgroundColor: color);
}
```

### De hijo a padre: *callbacks*

El hijo recibe una **función** y la llama cuando pasa algo. El estado vive en el padre (*lifting state up*, igual que en Compose):

```dart
class Estrellas extends StatelessWidget {
  const Estrellas({super.key, required this.valor, required this.alCambiar});
  final int valor;
  final ValueChanged<int> alCambiar;         // equivale a void Function(int)

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        for (var i = 1; i <= 5; i++)
          IconButton(
            icon: Icon(i <= valor ? Icons.star : Icons.star_border, color: Colors.amber),
            onPressed: () => alCambiar(i),
          ),
      ],
    );
  }
}

// En el padre (StatefulWidget):
// Estrellas(valor: _nota, alCambiar: (n) => setState(() => _nota = n))
```

!!! example "G2 · Guiado en clase: valoración de playas"
    Una lista de 4 playas. Cada fila tiene el widget `Estrellas`. Arriba, en el `AppBar`, se muestra la **media** de todas las valoraciones. El estado (la lista de notas) vive en la pantalla, no en cada fila.

### Estado compartido entre pantallas: `ChangeNotifier` + `provider`

Cuando varias pantallas necesitan los mismos datos (el carrito de la compra, el usuario conectado), pasar parámetros de una a otra se vuelve inmanejable. La solución oficial más sencilla:

1. Una clase que **guarda los datos** y **avisa** cuando cambian (`ChangeNotifier`, como un `ViewModel`).
2. El paquete `provider` la pone **a disposición de todo el árbol**.

```bash
flutter pub add provider
```

```dart
// lib/carrito.dart
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
    notifyListeners();                        // ← avisa a quien esté escuchando
  }

  void quitar(Producto p) {
    _items.remove(p);
    notifyListeners();
  }
}
```

```dart
// lib/main.dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'carrito.dart';

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (_) => Carrito(),               // se crea una vez para toda la app
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
    final carrito = context.watch<Carrito>(); // watch = me redibujo si cambia

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
                // read = solo uso el objeto, no me redibujo
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

| Llamada | Qué hace | Dónde |
|---|---|---|
| `context.watch<T>()` | Obtiene el objeto **y** redibuja el widget cuando cambia | En `build` |
| `context.read<T>()` | Obtiene el objeto **sin** suscribirse | En `onPressed`, `initState`… |
| `Consumer<T>(builder: ...)` | Redibuja **solo** esa parte | Para optimizar |

!!! example "G3 · Guiado en clase: el carrito en otra pantalla"
    Añade una segunda pantalla `PantallaCarrito` que liste los productos del carrito con un botón para quitar cada uno. Al volver a la tienda, el contador del `Badge` debe estar actualizado. (Lo haremos después del apartado 7.)

---

## 7. Navegación

### Ir y volver

```dart
// Ir a otra pantalla
Navigator.push(
  context,
  MaterialPageRoute(builder: (context) => const PantallaCarrito()),
);

// Volver (también lo hace la flecha del AppBar o el botón atrás de Android)
Navigator.pop(context);
```

### Pasar datos a la pantalla nueva

Por el constructor, como a cualquier widget:

```dart
Navigator.push(
  context,
  MaterialPageRoute(builder: (_) => DetallePlaya(nombre: playas[i])),
);
```

### Recibir un resultado al volver

`push` devuelve un `Future` que se completa con lo que se pase a `pop`:

```dart
// Pantalla A
final color = await Navigator.push<Color>(
  context,
  MaterialPageRoute(builder: (_) => const SelectorColor()),
);
if (color != null) setState(() => _color = color);

// Pantalla B (SelectorColor)
onTap: () => Navigator.pop(context, Colors.green),
```

### Navegación con pestañas: `NavigationBar`

```dart
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

También existen `Drawer` (menú lateral, `Scaffold(drawer: Drawer(...))`) y `TabBar` + `TabBarView` (pestañas arriba).

!!! note "¿Y `go_router`?"
    Para apps grandes o para web (URLs con rutas) se usa el paquete `go_router`. En este módulo basta con `Navigator`. Si os sobra tiempo en el proyecto final, investigadlo.

!!! example "G4 · Guiado en clase: lista → detalle"
    Con la lista de playas del apartado 4: al tocar una playa se abre `DetallePlaya` con su nombre en el `AppBar`, una imagen y un botón **«Marcar como favorita»** que vuelve a la lista devolviendo `true`. En la lista, las favoritas muestran un corazón.

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

### Sesión 1 · 9 nov

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

### Sesión 2 · 16 nov

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

## Práctica 3.1 · Cádiz Market { #practica-31-cadiz-market }

!!! abstract "Datos de la entrega"
    - **Individual** · **RA2 · CE a, c, e** · **RA1 · CE e**
    - **Entrega:** repositorio de GitHub `cadiz_market` + vídeo corto (1-2 min) mostrándola en funcionamiento
    - **Fecha:** domingo 22 de noviembre
    - **Duración orientativa:** 5-6 horas

Una tienda de productos de Cádiz. Es la versión Flutter de la actividad del curso pasado y **la reutilizaremos en los temas 5, 6 y 7**, así que merece la pena hacerla bien.

### Requisitos

1. **Modelo:** clase `Producto` (id, nombre, categoría como `enum`, precio, stock, imagen) y una lista de al menos 12 productos en `lib/datos.dart`.
2. **Catálogo:**
    - `GridView` de tarjetas con imagen, nombre, precio y un indicador de stock (verde > 5, naranja 1-5, rojo «Agotado»).
    - Un campo de búsqueda que filtre por nombre mientras se escribe.
    - Chips (`FilterChip` o `ChoiceChip`) para filtrar por categoría.
3. **Detalle:** al tocar un producto, pantalla con imagen grande, descripción, botones **−5 / −1 / +1 / +5** de stock (sin bajar de 0) y **«Añadir al carrito»** (desactivado si no hay stock).
4. **Carrito:** gestionado con `ChangeNotifier` + `provider`. `Badge` con el número de unidades en el `AppBar` de todas las pantallas. Pantalla de carrito con cantidades, subtotal por línea, total y botón para vaciar.
5. **Navegación:** `NavigationBar` con Catálogo, Carrito y «Acerca de».
6. **Aspecto:** tema con color propio, título **CÁDIZ MARKET**, modo oscuro que sigue al sistema y que se vea bien en móvil **y** en Chrome a pantalla completa (más columnas en pantallas anchas).

### Rúbrica

| Criterio | Peso | Excelente | Adecuado | Insuficiente |
|---|---|---|---|---|
| Interfaz y layout | 25 % | Cuidada, sin desbordes, coherente con el tema | Funcional con algún desborde o incoherencia | Desordenada o con errores visibles |
| Estado compartido (`provider`) | 25 % | Carrito y stock coherentes entre pantallas, `watch`/`read` bien usados | Funciona pero con estado duplicado o `setState` innecesarios | No usa `provider` o el estado se pierde |
| Navegación | 15 % | Pestañas, detalle y vuelta con datos actualizados | Funciona con algún fallo | No navega correctamente |
| Filtros y búsqueda | 15 % | Búsqueda y categorías combinables | Solo uno de los dos | No filtra |
| Diseño adaptable y tema | 10 % | Columnas según ancho y modo oscuro | Solo uno de los dos | Ninguno |
| Código | 10 % | Widgets separados en ficheros, `const`, sin avisos del analizador | Legible | Todo en `main.dart` |

## Práctica 3.2 · Alta de clientes { #practica-32-alta-de-clientes }

!!! abstract "Datos de la entrega"
    - **Individual** · **RA2 · CE a, c**
    - Se añade al proyecto `cadiz_market` como cuarta pestaña «Clientes»
    - **Fecha:** domingo 29 de noviembre

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
