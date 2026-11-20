# Práctica 3.1 · Cádiz Market

!!! abstract "Datos de la práctica"
    - **Individual** · **RA2 · CE a** (interfaces) · **CE c** (estado)
    - **Se hace en clase:** lunes 23 de noviembre · **2 horas**
    - **Entrega:** al terminar, el fichero `lib/main.dart` en la plataforma del módulo
    - **Sin IA.** Puedes consultar la web del módulo y la documentación de Flutter. El profesor puede pedirte que expliques cualquier parte de tu código: si no sabes explicarla, esa parte cuenta 0

Una tienda de productos típicos de Cádiz en **una sola pantalla**: el catálogo y el carrito juntos. Usa todo lo del Tema 3 hasta el **apartado 5** (widgets, layout, listas y estado local). No hace falta navegación ni `provider`.

La práctica tiene **7 partes acumulativas**: cada una se apoya en la anterior. Ve en orden y **guarda y prueba al acabar cada parte**. Si te atascas en una, la nota de las anteriores se mantiene.

## Antes de empezar

1. Crea el proyecto y ábrelo en VS Code:
    ```bash
    flutter create cadiz_market
    ```
2. Vacía `lib/main.dart` y borra `test/widget_test.dart`, como en el apartado 2.
3. Copia al principio de `lib/main.dart` el modelo y los datos. **No los cambies**:

```dart
import 'package:flutter/material.dart';

class Producto {
  const Producto(this.nombre, this.categoria, this.precio, this.stock, this.icono);
  final String nombre;
  final String categoria;
  final double precio;
  final int stock;
  final IconData icono;
}

const categorias = ['Pescado', 'Tapas', 'Dulces', 'Vinos'];

const catalogo = [
  Producto('Tortillitas de camarones', 'Pescado', 6.50, 10, Icons.set_meal),
  Producto('Cazón en adobo', 'Pescado', 8.00, 4, Icons.set_meal),
  Producto('Papas aliñás', 'Tapas', 4.00, 12, Icons.restaurant),
  Producto('Chicharrones especiales', 'Tapas', 5.50, 3, Icons.restaurant),
  Producto('Pan de Cádiz', 'Dulces', 12.00, 2, Icons.cake),
  Producto('Tocino de cielo', 'Dulces', 3.50, 8, Icons.cake),
  Producto('Manzanilla de Sanlúcar', 'Vinos', 7.00, 6, Icons.wine_bar),
  Producto('Fino del Puerto', 'Vinos', 9.50, 0, Icons.wine_bar),
];
```

Fíjate en que el **Fino del Puerto tiene stock 0**: te servirá para probar la parte 5.

---

## Parte 1 · Pantalla base (10 %)

- `main` con `MaterialApp` y una pantalla `CadizMarket`.
- `Scaffold` con `AppBar` y el título **Cádiz Market**.
- Arriba del todo, una **cabecera**: un icono (`Icons.storefront`) y el texto «Productos típicos de Cádiz» con estilo propio (tamaño y color).

## Parte 2 · Tarjeta de producto (20 %)

Debajo de la cabecera, **una tarjeta** para el primer producto del catálogo (`catalogo[0]`), con este aspecto:

```text
┌──────────────────────────────────────────────┐
│ [icono]  Tortillitas de camarones     6,50 € │
│          [Pescado]                           │
└──────────────────────────────────────────────┘
```

- `Card` con relleno (`Padding`).
- El icono del producto en un `CircleAvatar`.
- Nombre en negrita y, debajo, la categoría en un `Chip`.
- El precio **pegado a la derecha** y con 2 decimales (`toStringAsFixed(2)`).
- **Sin franjas amarillas**, ni siquiera estrechando la ventana de Chrome.

!!! tip "Pista"
    Escribe la tarjeta como un **método** de tu pantalla que recibe un producto y devuelve un widget: `Widget _tarjeta(Producto p) { ... }`. Así en la parte 3 solo tendrás que llamarlo para cada producto.

## Parte 3 · El catálogo (15 %)

- Sustituye la tarjeta suelta por la **lista de todos los productos** del catálogo, con `ListView.builder` y tu tarjeta de la parte 2.
- La cabecera de la parte 1 sigue arriba y la lista ocupa el resto de la pantalla (`Expanded`).
- Debe hacer scroll si los productos no caben.

## Parte 4 · El carrito (25 %)

Ahora la pantalla tiene **estado**: convierte `CadizMarket` en un `StatefulWidget`.

- En cada tarjeta, botones **−** y **+** con la **cantidad** de ese producto en el carrito entre ellos (empieza en 0).
- El botón **−** está **desactivado** cuando la cantidad es 0.
- Abajo del todo (`bottomNavigationBar`), una barra con el **total** del carrito en euros con 2 decimales, que se actualiza al pulsar.

!!! tip "Pista"
    Guarda las cantidades en un mapa con el nombre del producto como clave: `final _carrito = <String, int>{};`. La cantidad de un producto es `_carrito[p.nombre] ?? 0`.

## Parte 5 · El stock (10 %)

- El botón **+** se **desactiva** cuando la cantidad en el carrito llega al stock del producto.
- Cada tarjeta muestra un **indicador de lo que queda** (stock menos lo que hay en el carrito):
    - más de 5 → «Quedan N» en **verde**,
    - de 1 a 5 → «Últimas N» en **naranja**,
    - 0 → «Agotado» en **rojo**.

## Parte 6 · Filtro por categoría (10 %)

- Entre la cabecera y la lista, una fila de **chips** con «Todas» y las 4 categorías.
- Al tocar uno, la lista muestra **solo** los productos de esa categoría. «Todas» los muestra todos.
- El chip elegido se ve seleccionado.
- **Las cantidades del carrito no se pierden** al cambiar de filtro.
- Si se estrecha la pantalla, los chips bajan de línea (sin franjas amarillas).

!!! tip "Pista"
    Usa `ChoiceChip`. Funciona como un `Switch`: recibe si está seleccionado (`selected:`) y una función que se llama al tocarlo (`onSelected:`).

    ```dart
    ChoiceChip(
      label: const Text('Pescado'),
      selected: _categoria == 'Pescado',
      onSelected: (_) => setState(() => _categoria = 'Pescado'),
    )
    ```

## Parte 7 · Resumen del carrito (10 %)

- En el `AppBar`, a la derecha, el icono del carrito con un `Badge` que muestra el **número total de unidades**.
- En la barra del total, un botón **«Vaciar»** que pone todas las cantidades a 0 y muestra un `SnackBar` con el mensaje «Carrito vaciado». Está **desactivado** si el carrito ya está vacío.

## Para subir nota (hasta +1)

- **Vista de cuadrícula (+0,5):** un `IconButton` en el `AppBar` que cambia entre lista y cuadrícula de 2 columnas (`GridView.builder`).
- **Código limpio (+0,5):** `const` donde se puede, sin avisos del analizador y sin código repetido.

---

## Rúbrica

| Parte | Peso | Completa | A medias | No hecha o no funciona |
|---|---|---|---|---|
| 1 · Pantalla base | 10 % | `AppBar` y cabecera con estilo | Falta la cabecera o el estilo | No compila |
| 2 · Tarjeta | 20 % | Como el dibujo, precio a la derecha, sin desbordes | Todos los datos, pero mal colocados o con desbordes | Falta información |
| 3 · Catálogo | 15 % | `ListView.builder` con todos los productos y scroll | Lista escrita a mano o sin scroll | No hay lista |
| 4 · Carrito | 25 % | Cantidades, − desactivado en 0 y total correcto | Cantidades sin total, o total incorrecto | No hay estado |
| 5 · Stock | 10 % | + desactivado e indicador con sus tres colores | Solo una de las dos cosas | No hecha |
| 6 · Filtro | 10 % | Filtra, se ve el elegido y no pierde el carrito | Filtra pero pierde el carrito o no marca el elegido | No hecha |
| 7 · Resumen | 10 % | `Badge` correcto y «Vaciar» con `SnackBar` y desactivado | Solo una de las dos cosas | No hecha |

**Penalización:** una franja amarilla visible resta un 10 % de la parte en la que aparece.
