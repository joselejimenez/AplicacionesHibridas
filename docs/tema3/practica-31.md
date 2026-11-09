# Práctica 3.1 · Cádiz Market

!!! abstract "Datos de la entrega"
    - **Individual** · **RA2 · CE a, c, e** · **RA1 · CE e**
    - **Se hace en clase:** lunes 16 de noviembre · **Entrega:** repositorio de GitHub `cadiz_market` al terminar la clase

Una tienda de productos de Cádiz. Es la versión Flutter de la actividad del curso pasado y **la reutilizaremos en los temas 5, 6 y 7**, así que merece la pena hacerla bien.

## Requisitos

1. **Modelo:** clase `Producto` (id, nombre, categoría como `enum`, precio, stock, imagen) y una lista de al menos 12 productos en `lib/datos.dart`.
2. **Catálogo:**
    - `GridView` de tarjetas con imagen, nombre, precio y un indicador de stock (verde > 5, naranja 1-5, rojo «Agotado»).
    - Un campo de búsqueda que filtre por nombre mientras se escribe.
    - Chips (`FilterChip` o `ChoiceChip`) para filtrar por categoría.
3. **Detalle:** al tocar un producto, pantalla con imagen grande, descripción, botones **−5 / −1 / +1 / +5** de stock (sin bajar de 0) y **«Añadir al carrito»** (desactivado si no hay stock).
4. **Carrito:** gestionado con `ChangeNotifier` + `provider`. `Badge` con el número de unidades en el `AppBar` de todas las pantallas. Pantalla de carrito con cantidades, subtotal por línea, total y botón para vaciar.
5. **Navegación:** `NavigationBar` con Catálogo, Carrito y «Acerca de».
6. **Aspecto:** tema con color propio, título **CÁDIZ MARKET**, modo oscuro que sigue al sistema y que se vea bien en móvil **y** en Chrome a pantalla completa (más columnas en pantallas anchas).

## Rúbrica

| Criterio | Peso | Excelente | Adecuado | Insuficiente |
|---|---|---|---|---|
| Interfaz y layout | 25 % | Cuidada, sin desbordes, coherente con el tema | Funcional con algún desborde o incoherencia | Desordenada o con errores visibles |
| Estado compartido (`provider`) | 25 % | Carrito y stock coherentes entre pantallas, `watch`/`read` bien usados | Funciona pero con estado duplicado o `setState` innecesarios | No usa `provider` o el estado se pierde |
| Navegación | 15 % | Pestañas, detalle y vuelta con datos actualizados | Funciona con algún fallo | No navega correctamente |
| Filtros y búsqueda | 15 % | Búsqueda y categorías combinables | Solo uno de los dos | No filtra |
| Diseño adaptable y tema | 10 % | Columnas según ancho y modo oscuro | Solo uno de los dos | Ninguno |
| Código | 10 % | Widgets separados en ficheros, `const`, sin avisos del analizador | Legible | Todo en `main.dart` |
