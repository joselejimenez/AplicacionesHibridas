# Tema 6 · Rendimiento, pruebas y gestión de errores

!!! abstract "Ficha del tema"
    - **Duración:** 2 sesiones (11 y 18 de enero)
    - **RA:** RA3 · CE a (optimizar recursos y rendimiento) · CE b (pruebas de funcionamiento en diferentes dispositivos y condiciones) · CE c (gestión de errores y excepciones)
    - **Actividades:** [10 ejercicios rápidos de clase](#ejercicios-rapidos) · 2 guiados · [Boletín de 8 ejercicios](#boletin-de-ejercicios) · [Práctica 6.1 · De malas a buenas prácticas](#practica-61-de-malas-a-buenas-practicas) · [Práctica 6.2 · Tests para Cádiz Market](#practica-62-tests-para-cadiz-market)

| Sesión | Contenido | En clase |
|---|---|---|
| **1 · 11 ene** | Modos de compilación, DevTools, las 10 reglas de rendimiento, `flutter analyze` | Rápidos R1-R5 · Guiado G1 · Práctica 6.1 · Boletín B1-B3 |
| **2 · 18 ene** | Tests unitarios, de widget y de integración, *mocks*, cobertura. Gestión centralizada de errores y *logs* | Rápidos R6-R10 · Guiado G2 · Práctica 6.2 · Boletín B4-B8 |

---

## 1. Medir antes de optimizar

### Los tres modos

| Modo | Comando | Para qué |
|---|---|---|
| **Debug** | `flutter run` | Desarrollar. Hot reload. **Lento a propósito** |
| **Profile** | `flutter run --profile` | **Medir el rendimiento** (casi como release, pero con herramientas) |
| **Release** | `flutter run --release` | Probar la versión final |

!!! danger "Nunca midas el rendimiento en debug"
    En debug todo va más lento. El perfilado se hace **en modo profile y en un dispositivo real** (el emulador tampoco es fiable).

### DevTools

Con la app en marcha, ábrelo desde Android Studio (*Flutter DevTools* en la barra lateral o el enlace que aparece en la consola de *Run*). Las pestañas que usaremos:

| Pestaña | Qué mirar |
|---|---|
| **Flutter Inspector** | Árbol de widgets. Botón *Highlight repaints* y *Select widget mode* |
| **Performance** | Gráfica de fotogramas. Cada barra es un fotograma: **en rojo, los que tardan más de 16 ms** (se pierde la fluidez de 60 fps). Activa *Track widget rebuilds* |
| **CPU Profiler** | Qué funciones consumen más tiempo |
| **Memory** | Consumo de memoria y fugas (objetos que no se liberan) |
| **Network** | Peticiones HTTP: tiempos, tamaños, respuestas |

**Superposición de rendimiento** directamente en la app:

```dart
MaterialApp(showPerformanceOverlay: true, home: ...)
```

Dos gráficas: la de arriba es el hilo de la GPU (*raster*) y la de abajo el de la interfaz (*UI*). Si aparecen barras rojas, hay tirones.

!!! example "G1 · Guiado en clase: cazar el tirón"
    Con la app de la [Práctica 6.1](#practica-61-de-malas-a-buenas-practicas) en modo profile: abrid la pestaña *Performance*, escribid en el buscador y observad los fotogramas rojos. Después, en *CPU Profiler*, buscad la función culpable. Spoiler: se llama como un matemático italiano.

---

## 2. Las 10 reglas de rendimiento en Flutter

| # | Regla | Por qué |
|---|---|---|
| 1 | **`const` siempre que se pueda** | Flutter no reconstruye un widget `const` |
| 2 | **Divide en widgets pequeños** | `setState` reconstruye todo el `build` de ese widget. Si el reloj es un widget aparte, solo se redibuja el reloj |
| 3 | **Nada pesado en `build`** | `build` se ejecuta muchísimas veces. Cálculos, filtros de listas grandes o lecturas de ficheros van en `initState`, en el servicio o en el `ChangeNotifier` |
| 4 | **`ListView.builder` para listas largas** | Solo construye lo visible |
| 5 | **Imágenes del tamaño que se muestran** | Una foto de 4000×3000 en un icono de 50×50 desperdicia memoria. Usa `cacheWidth`/`cacheHeight` o pide miniaturas |
| 6 | **Cálculos pesados fuera del hilo de la interfaz** | `await Isolate.run(() => calculoPesado())` lo ejecuta en otro hilo (`dart:isolate`) |
| 7 | **Libera en `dispose`** | Controladores, suscripciones y *timers* sin liberar = fugas de memoria y errores |
| 8 | **`context.watch` solo donde haga falta** | O `Consumer`/`Selector` para redibujar solo un trozo |
| 9 | **No crees `Future` en `build`** | Visto en el Tema 5: cada redibujado haría una petición |
| 10 | **Mide en profile, en un móvil real** | Ver apartado 1 |

**El analizador te ayuda** con muchas de estas reglas:

```bash
flutter analyze
```

Arregla **todos** los avisos antes de entregar. Las reglas están en `analysis_options.yaml` (el paquete `flutter_lints` viene activado por defecto).

---

## 3. Pruebas automáticas

| Tipo | Qué prueba | Velocidad | Dónde |
|---|---|---|---|
| **Unitaria** | Una función o clase **sin interfaz** (modelos, servicios, `ChangeNotifier`) | Milisegundos | `test/` |
| **De widget** | Un widget: se pinta en memoria, se pulsa, se comprueba el resultado | Rápida | `test/` |
| **De integración** | La app completa en un dispositivo real o emulador | Lenta | `integration_test/` |

!!! info "Ya lo conoces (Entornos de Desarrollo, 1º)"
    La idea es la misma que JUnit: preparar, actuar y comprobar (*Arrange, Act, Assert*). Cambian los nombres: `test()` en lugar de `@Test` y `expect()` en lugar de `assertEquals()`.

### Tests unitarios

Probamos el `Carrito` del Tema 3. Fichero `test/carrito_test.dart`:

```dart
import 'package:flutter_test/flutter_test.dart';
import 'package:cadiz_market/carrito.dart';

void main() {
  group('Carrito', () {
    late Carrito carrito;
    const p1 = Producto('Papas aliñás', 4.0);
    const p2 = Producto('Chicharrones', 5.5);

    setUp(() => carrito = Carrito());         // antes de cada test, uno nuevo

    test('empieza vacío', () {
      expect(carrito.cantidad, 0);
      expect(carrito.total, 0);
    });

    test('añadir suma cantidad y total', () {
      carrito.anadir(p1);
      carrito.anadir(p2);
      expect(carrito.cantidad, 2);
      expect(carrito.total, closeTo(9.5, 0.001));   // decimales: closeTo
    });

    test('notifica a los oyentes al añadir', () {
      var avisos = 0;
      carrito.addListener(() => avisos++);
      carrito.anadir(p1);
      expect(avisos, 1);
    });
  });
}
```

Ejecutar todos los tests:

```bash
flutter test
```

| *Matcher* | Comprueba |
|---|---|
| `expect(x, 3)` / `equals(3)` | Igualdad |
| `isTrue`, `isFalse`, `isNull`, `isNotNull` | Booleanos y nulos |
| `closeTo(9.5, 0.001)` | Decimales con margen |
| `hasLength(3)`, `isEmpty`, `contains(x)` | Colecciones |
| `throwsException`, `throwsA(isA<FormatException>())` | Excepciones |

### Probar un servicio sin Internet: *mocks*

Un test **no debe depender de la red**. El paquete `http` trae un cliente falso, `MockClient`. Para usarlo, el servicio tiene que **recibir** el cliente en lugar de crearlo él (inyección de dependencias):

```dart
// lib/servicios/servicio_terremotos.dart (modificado)
class ServicioTerremotos {
  ServicioTerremotos({http.Client? cliente}) : _cliente = cliente ?? http.Client();
  final http.Client _cliente;

  Future<List<Terremoto>> ultimos() async {
    final respuesta = await _cliente.get(Uri.parse(_url)).timeout(const Duration(seconds: 10));
    // ... igual que antes
  }
}
```

```dart
// test/servicio_terremotos_test.dart
import 'dart:convert';
import 'package:flutter_test/flutter_test.dart';
import 'package:http/http.dart' as http;
import 'package:http/testing.dart';
import 'package:terremotos/servicios/servicio_terremotos.dart';

void main() {
  test('convierte el JSON en una lista de terremotos', () async {
    final falso = MockClient((peticion) async => http.Response(
          jsonEncode({
            'features': [
              {
                'properties': {'mag': 4.5, 'place': 'Golfo de Cadiz', 'time': 0},
                'geometry': {'coordinates': [-6.9, 36.2, 10.0]},
              }
            ]
          }),
          200,
        ));

    final lista = await ServicioTerremotos(cliente: falso).ultimos();

    expect(lista, hasLength(1));
    expect(lista.first.lugar, 'Golfo de Cadiz');
    expect(lista.first.latitud, 36.2);
  });

  test('lanza una excepción si el servidor falla', () {
    final falso = MockClient((_) async => http.Response('Error', 500));
    expect(ServicioTerremotos(cliente: falso).ultimos(), throwsException);
  });
}
```

### Tests de widget

```dart
// test/contador_test.dart
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:boletin_t3/contador.dart';

void main() {
  testWidgets('suma y no pasa del máximo', (tester) async {
    await tester.pumpWidget(
      const MaterialApp(home: Scaffold(body: Contador(maximo: 2))),
    );

    expect(find.text('0'), findsOneWidget);

    await tester.tap(find.byIcon(Icons.add));
    await tester.pump();                        // redibuja tras el setState
    expect(find.text('1'), findsOneWidget);

    await tester.tap(find.byIcon(Icons.add));
    await tester.pump();
    await tester.tap(find.byIcon(Icons.add));   // ya está en el máximo
    await tester.pump();
    expect(find.text('2'), findsOneWidget);
  });
}
```

| Herramienta | Para qué |
|---|---|
| `tester.pumpWidget(w)` | Pinta el widget (envuélvelo en `MaterialApp` si usa tema o navegación) |
| `tester.pump()` | Procesa un fotograma (tras un `setState`) |
| `tester.pumpAndSettle()` | Espera a que terminen animaciones y navegaciones |
| `find.text`, `find.byIcon`, `find.byType`, `find.byKey` | Localizar widgets |
| `tester.tap`, `tester.enterText`, `tester.drag` | Interactuar |
| `findsOneWidget`, `findsNothing`, `findsNWidgets(n)` | Comprobar cuántos hay |

!!! tip "Dale `Key` a lo que quieras encontrar"
    `TextFormField(key: const Key('campoEmail'), ...)` y en el test `find.byKey(const Key('campoEmail'))`. Es más robusto que buscar por texto.

### Tests de integración

Prueban la app entera en un dispositivo. En `pubspec.yaml`, dentro de `dev_dependencies`, añade:

```yaml
  integration_test:
    sdk: flutter
```

Fichero `integration_test/app_test.dart`:

```dart
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:cadiz_market/main.dart' as app;

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  testWidgets('comprar un producto y verlo en el carrito', (tester) async {
    app.main();
    await tester.pumpAndSettle();

    await tester.tap(find.byIcon(Icons.add_shopping_cart).first);
    await tester.pumpAndSettle();

    await tester.tap(find.text('Carrito'));
    await tester.pumpAndSettle();

    expect(find.textContaining('Total'), findsOneWidget);
  });
}
```

Con el emulador o el móvil conectado:

```bash
flutter test integration_test
```

### Cobertura

```bash
flutter test --coverage
```

Genera `coverage/lcov.info` con el porcentaje de líneas cubiertas por los tests. En Android Studio: botón *Run with Coverage*.

!!! example "G2 · Guiado en clase: primer test de cada tipo"
    Sobre Cádiz Market: un test unitario del filtro de productos, un test de widget de la tarjeta de producto (muestra «Agotado» si el stock es 0) y un test de integración que compra un producto.

---

## 4. Gestión centralizada de errores

Por muy bien que programes, algo fallará en el móvil de un usuario. Hay que **capturarlo en un único sitio**, **registrarlo** y **mostrar algo digno** en lugar de la pantalla roja.

```dart
import 'dart:developer' as developer;
import 'dart:ui';
import 'package:flutter/material.dart';

void registrarError(Object error, StackTrace? pila) {
  developer.log('ERROR', name: 'cadiz_market', error: error, stackTrace: pila);
  // Aquí se enviaría a un servicio como Firebase Crashlytics o Sentry
}

void main() {
  // Errores dentro de Flutter (build, layout, pintado…)
  FlutterError.onError = (details) {
    FlutterError.presentError(details);        // lo sigue mostrando en consola
    registrarError(details.exception, details.stack);
  };

  // Errores asíncronos no capturados (un Future que falla sin try/catch)
  PlatformDispatcher.instance.onError = (error, pila) {
    registrarError(error, pila);
    return true;                               // "ya lo he gestionado"
  };

  // Sustituye la pantalla roja por algo amable (en release)
  ErrorWidget.builder = (details) => const Material(
        child: Center(child: Text('Algo ha ido mal en esta parte de la pantalla')),
      );

  runApp(const MiApp());
}
```

| Nivel | Qué usar |
|---|---|
| Error esperado (sin red, dato inválido) | `try`/`catch` en el servicio y mensaje claro al usuario (Tema 5) |
| Error inesperado | `FlutterError.onError` + `PlatformDispatcher.instance.onError` |
| Registro durante el desarrollo | `debugPrint(...)` o `developer.log(...)` (aparece en DevTools → *Logging*) |
| Registro en producción | Firebase Crashlytics o Sentry (se configuran como Firebase en el Tema 5) |

!!! warning "`print` en producción"
    El analizador marca `print` con el aviso `avoid_print`. Usa `debugPrint` o `developer.log`, y nunca registres datos personales ni contraseñas.

---

## Ejercicios rápidos de clase { #ejercicios-rapidos }

Cortos (5-15 minutos). Se hacen **en clase**, justo después de explicar cada apartado, y se corrigen en voz alta. No se entregan: son el entrenamiento para el boletín y las prácticas.

### Sesión 1 · 11 ene

| # | Ejercicio | Apartado |
|---|---|---|
| R1 | **Tres modos.** Ejecuta Cádiz Market en debug, profile y release. Anota cuánto tarda en arrancar y si notas diferencias al hacer scroll | 1 |
| R2 | **Leer la superposición.** Activa `showPerformanceOverlay`, haz scroll rápido y explica qué significan las dos gráficas | 1 |
| R3 | **Caza de `const`.** Abre un ejercicio del Tema 3, acepta todas las sugerencias `prefer_const_constructors` del analizador y cuenta cuántas eran | 2 |
| R4 | **A otro hilo.** Calcula `fibonacci(35)` al pulsar un botón: primero directamente (la app se congela) y después con `Isolate.run` (no se congela) | 2 |
| R5 | **Divide y vencerás.** En una pantalla con un reloj que se actualiza cada segundo, extrae el reloj a su propio widget y compara las reconstrucciones con *Track widget rebuilds* | 2 |

### Sesión 2 · 18 ene

| # | Ejercicio | Apartado |
|---|---|---|
| R6 | **Primer test.** Tests para `esBisiesto` (ejercicio R12 del Tema 1): 2024, 2023, 1900 y 2000 | 3 |
| R7 | **Test de clase.** Tests de `CuentaBancaria` (R15 del Tema 1) con `group` y `setUp`, incluido que retirar de más lanza una excepción | 3 |
| R8 | **Test de widget.** Test del botón «me gusta» (R6 del Tema 3): empieza vacío y, al tocarlo, se rellena y suma 1 | 3 |
| R9 | **Un test que falla.** Escribe un test que falle a propósito, lee el mensaje de `flutter test` y arréglalo | 3 |
| R10 | **Pantalla amable.** Provoca un error en un `build` y comprueba que `ErrorWidget.builder` muestra tu mensaje en lugar de la pantalla roja (prueba en `--release`) | 4 |

---

## Boletín de ejercicios { #boletin-de-ejercicios }

!!! abstract "Instrucciones"
    - **Individual.** Los ejercicios B1-B3 sobre la app lenta de la Práctica 6.1; B4-B8 en un proyecto `boletin_t6` o sobre tus proyectos anteriores (indícalo en el README).
    - **Entrega:** repositorio de GitHub · **Fecha:** domingo 24 de enero.

| # | Ejercicio | Practica |
|---|---|---|
| B1 | **Radiografía.** Ejecuta la app lenta en modo profile y haz capturas de *Performance* (fotogramas rojos) y de *CPU Profiler* (función culpable). Explica qué ves | DevTools |
| B2 | **Contador de reconstrucciones.** Activa *Track widget rebuilds* y anota cuántas veces se reconstruye cada widget en 10 segundos. ¿Cuál se reconstruye sin necesidad? | Inspector, reconstrucciones |
| B3 | **Cero avisos.** Pasa `flutter analyze` a la app lenta y a tu Cádiz Market. Arregla todos los avisos y explica 5 de ellos | Analizador |
| B4 | **Tests de funciones puras.** Escribe tests para `calificacion(double nota)` del boletín del Tema 1: todos los tramos, los límites (4.99, 5, 10) y valores fuera de rango | Tests unitarios, casos límite |
| B5 | **Test de un modelo.** Tests de `Terremoto.fromJson` (Tema 5): JSON completo, sin magnitud, sin lugar y con magnitud entera (`5` en lugar de `5.0`) | Tests de modelos y nulos |
| B6 | **Test con mock.** Tests del servicio de tu API de PMDM con `MockClient`: lista correcta, lista vacía, error 500 y JSON mal formado | `MockClient`, excepciones |
| B7 | **Test de formulario.** Test de widget del formulario de registro (Tema 3): enviar vacío muestra los errores; con datos válidos no hay errores | `enterText`, `find.byKey`, validación |
| B8 | **Errores centralizados.** Añade a Cádiz Market la gestión centralizada del apartado 4 y un botón oculto en «Acerca de» que lance una excepción. Demuestra en un vídeo que se registra y que la app no se cierra | `FlutterError.onError`, `developer.log` |

---

## Práctica 6.1 · De malas a buenas prácticas { #practica-61-de-malas-a-buenas-practicas }

!!! abstract "Datos de la entrega"
    - **Parejas** · **RA3 · CE a** · Actividad evaluable del RA3 (15 %)
    - **Entrega:** repositorio con dos ramas (`lenta` y `optimizada`) + informe PDF · **Fecha:** domingo 17 de enero

Esta app **funciona**, pero está escrita con todos los errores de rendimiento posibles. Crea un proyecto nuevo `tienda_lenta` y sustituye `lib/main.dart` por este código:

```dart
import 'dart:async';
import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(home: PantallaLenta()));

int fibonacci(int n) => n < 2 ? n : fibonacci(n - 1) + fibonacci(n - 2);

class PantallaLenta extends StatefulWidget {
  @override
  State<PantallaLenta> createState() => _PantallaLentaState();
}

class _PantallaLentaState extends State<PantallaLenta> {
  int _segundos = 0;
  String _filtro = '';
  final _buscador = TextEditingController();

  @override
  void initState() {
    super.initState();
    Stream.periodic(Duration(seconds: 1)).listen((_) {
      setState(() => _segundos++);
    });
  }

  @override
  Widget build(BuildContext context) {
    final numeroMagico = fibonacci(32);
    final productos = List.generate(5000, (i) => 'Producto $i');
    final filtrados = productos.where((p) => p.contains(_filtro)).toList();

    return Scaffold(
      appBar: AppBar(title: Text('Tienda lenta · abierta hace $_segundos s')),
      body: Column(
        children: [
          Padding(
            padding: EdgeInsets.all(8),
            child: TextField(
              controller: _buscador,
              decoration: InputDecoration(labelText: 'Buscar'),
              onChanged: (v) => setState(() => _filtro = v),
            ),
          ),
          Text('Número mágico del día: $numeroMagico'),
          Expanded(
            child: ListView(
              children: [
                for (final p in filtrados)
                  ListTile(
                    leading: Image.network(
                      'https://picsum.photos/id/${filtrados.indexOf(p) % 100}/2000/2000',
                      width: 50,
                      height: 50,
                    ),
                    title: Text(p),
                  ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
```

### Qué tenéis que hacer

1. Súbela a la rama `lenta` tal cual.
2. **Mide:** en modo profile y en un móvil real, captura *Performance*, *CPU Profiler* y *Memory*. Anota el tiempo medio por fotograma y el consumo de memoria.
3. **Encuentra los problemas.** Hay **al menos 8**. Para cada uno: qué es, qué regla del apartado 2 incumple y cómo lo habéis detectado.
4. **Arréglalos** en la rama `optimizada`. La app debe hacer exactamente lo mismo.
5. **Vuelve a medir** en las mismas condiciones.
6. **Informe** (máximo 4 páginas): tabla de problemas, capturas antes/después y conclusiones.

!!! tip "Puedes usar IA para el informe o para ideas"
    Pero **las medidas tienen que ser vuestras**, con capturas de vuestro DevTools. En la defensa del proyecto se puede preguntar por esta práctica.

| Criterio | Peso |
|---|---|
| Medición inicial correcta (modo profile, dispositivo real, capturas) | 20 % |
| Problemas identificados y justificados (mínimo 8) | 30 % |
| Soluciones correctas sin cambiar el comportamiento | 30 % |
| Medición final y comparación razonada | 20 % |

## Práctica 6.2 · Tests para Cádiz Market { #practica-62-tests-para-cadiz-market }

!!! abstract "Datos de la entrega"
    - **Individual** · **RA3 · CE b, c**
    - Sobre tu proyecto `cadiz_market` (Temas 3 y 5) · **Fecha:** domingo 24 de enero

1. **Unitarios** (mínimo 8): modelo `Producto`, `Carrito` (añadir, quitar, total, vaciar, persistencia simulada) y filtros.
2. **De widget** (mínimo 4): tarjeta de producto (stock y «Agotado»), botones de stock del detalle, `Badge` del carrito y formulario de clientes.
3. **De integración** (mínimo 1): buscar un producto, añadirlo al carrito y comprobar el total.
4. **Cobertura** superior al 60 % de `lib/` (sin contar `main.dart`), con captura.
5. **Gestión centralizada de errores** (apartado 4).
6. Un apartado en el README que explique cómo ejecutar los tests.

| Criterio | Peso |
|---|---|
| Tests unitarios significativos (casos normales y límite) | 30 % |
| Tests de widget | 25 % |
| Test de integración funcionando | 20 % |
| Cobertura y README | 10 % |
| Gestión de errores | 15 % |
