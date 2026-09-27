# Tema 5 · Datos locales y remotos

!!! abstract "Ficha del tema"
    - **Duración:** 2 sesiones (30 de noviembre y 14 de diciembre)
    - **RA:** RA2 · CE d (almacenamiento persistente de datos, local y remoto)
    - **Actividades:** [12 ejercicios rápidos de clase](#ejercicios-rapidos) · 4 guiados · [Boletín de 10 ejercicios](#boletin-de-ejercicios) · [Práctica 5.1 · Terremotos y mi API](#practica-51-terremotos-y-mi-api) · [Práctica 5.2 · Mis lugares](#practica-52-mis-lugares)

| Sesión | Contenido | En clase |
|---|---|---|
| **1 · 30 nov** | APIs REST con `http`, JSON y modelos, `FutureBuilder`, errores de red, POST/PUT/DELETE contra vuestra API de PMDM | Rápidos R1-R6 · Guiados G1-G2 · Boletín B1-B5 · Práctica 5.1 |
| **2 · 14 dic** | `shared_preferences`, SQLite con `sqflite`, Firebase (Auth y Firestore) | Rápidos R7-R12 · Guiados G3-G4 · Boletín B6-B10 · Práctica 5.2 |

!!! info "Lo que ya sabéis y vamos a usar"
    - **Asincronía** (Tema 1): todo este tema son `Future` y `Stream`.
    - **API REST propia** (PMDM): la API Spring Boot que desplegasteis en Render será uno de los servidores de este tema.

---

## 1. Consumir una API REST

```bash
flutter pub add http
```

!!! warning "Permiso de Internet en Android"
    En modo *debug* funciona sin él, pero **la versión de producción no tendrá red** si no está declarado. Compruébalo en `android/app/src/main/AndroidManifest.xml`:

    ```xml
    <uses-permission android:name="android.permission.INTERNET" />
    ```

### El patrón: modelo + servicio + pantalla

Vamos a usar la API pública de terremotos del Servicio Geológico de EE. UU. (USGS). Abre esta URL en el navegador para ver el JSON:

`https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson`

Simplificado, tiene esta forma:

```json
{
  "features": [
    {
      "properties": { "mag": 4.6, "place": "10 km SW of Somewhere", "time": 1790000000000 },
      "geometry": { "coordinates": [-117.5, 35.7, 8.2] }
    }
  ]
}
```

**1. El modelo** (`lib/modelos/terremoto.dart`): convierte un mapa JSON en un objeto Dart.

```dart
class Terremoto {
  const Terremoto({
    required this.magnitud,
    required this.lugar,
    required this.fecha,
    required this.latitud,
    required this.longitud,
    required this.profundidad,
  });

  final double magnitud;
  final String lugar;
  final DateTime fecha;
  final double latitud;
  final double longitud;
  final double profundidad;

  factory Terremoto.fromJson(Map<String, dynamic> json) {
    final p = json['properties'] as Map<String, dynamic>;
    final c = (json['geometry']['coordinates'] as List).cast<num>();
    return Terremoto(
      magnitud: (p['mag'] as num?)?.toDouble() ?? 0,
      lugar: p['place'] as String? ?? 'Lugar desconocido',
      fecha: DateTime.fromMillisecondsSinceEpoch(p['time'] as int),
      longitud: c[0].toDouble(),        // ¡GeoJSON pone primero la longitud!
      latitud: c[1].toDouble(),
      profundidad: c[2].toDouble(),
    );
  }
}
```

!!! tip "Null safety con JSON"
    Los datos que llegan de fuera **pueden faltar**. `p['mag'] as num?` y `?? 0` evitan que la app se rompa si un terremoto viene sin magnitud. Y `num` en lugar de `double` porque el JSON puede traer `5` (int) o `5.2` (double).

**2. El servicio** (`lib/servicios/servicio_terremotos.dart`): la única clase que sabe hablar con la API.

```dart
import 'dart:convert';
import 'package:http/http.dart' as http;
import '../modelos/terremoto.dart';

class ServicioTerremotos {
  static const _url =
      'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson';

  Future<List<Terremoto>> ultimos() async {
    final respuesta = await http
        .get(Uri.parse(_url))
        .timeout(const Duration(seconds: 10));

    if (respuesta.statusCode != 200) {
      throw Exception('El servidor respondió ${respuesta.statusCode}');
    }

    // utf8.decode: sin esto, las tildes y eñes pueden salir mal
    final datos = jsonDecode(utf8.decode(respuesta.bodyBytes)) as Map<String, dynamic>;
    final features = datos['features'] as List;
    return features
        .map((f) => Terremoto.fromJson(f as Map<String, dynamic>))
        .toList();
  }
}
```

**3. La pantalla**, con `FutureBuilder`:

```dart
class ListaTerremotos extends StatefulWidget {
  const ListaTerremotos({super.key});
  @override
  State<ListaTerremotos> createState() => _ListaTerremotosState();
}

class _ListaTerremotosState extends State<ListaTerremotos> {
  final _servicio = ServicioTerremotos();
  late Future<List<Terremoto>> _futuro;

  @override
  void initState() {
    super.initState();
    _futuro = _servicio.ultimos();          // se pide UNA vez, no en build
  }

  Future<void> _recargar() async {
    setState(() => _futuro = _servicio.ultimos());
    await _futuro;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Terremotos de hoy')),
      body: FutureBuilder<List<Terremoto>>(
        future: _futuro,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          if (snapshot.hasError) {
            return Center(
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Icon(Icons.wifi_off, size: 64),
                  Text('No se han podido cargar los datos\n${snapshot.error}',
                      textAlign: TextAlign.center),
                  FilledButton(onPressed: _recargar, child: const Text('Reintentar')),
                ],
              ),
            );
          }
          final lista = snapshot.data!;
          return RefreshIndicator(          // "tirar hacia abajo" para recargar
            onRefresh: _recargar,
            child: ListView.builder(
              itemCount: lista.length,
              itemBuilder: (context, i) {
                final t = lista[i];
                return ListTile(
                  leading: CircleAvatar(
                    backgroundColor: t.magnitud >= 5 ? Colors.red : Colors.orange,
                    child: Text(t.magnitud.toStringAsFixed(1)),
                  ),
                  title: Text(t.lugar),
                  subtitle: Text('${t.fecha.toLocal()} · ${t.profundidad.toStringAsFixed(0)} km'),
                );
              },
            ),
          );
        },
      ),
    );
  }
}
```

!!! warning "Tildes y eñes rotas (`CÃ¡diz`)"
    Si el servidor no indica la codificación, el paquete `http` interpreta el texto como Latin-1 y las tildes se estropean. Decodifica siempre los bytes como UTF-8: `jsonDecode(utf8.decode(respuesta.bodyBytes))` (`utf8` está en `dart:convert`).

!!! warning "El error más típico: crear el `Future` dentro de `build`"
    `FutureBuilder(future: _servicio.ultimos(), ...)` hace **una petición nueva cada vez que se redibuja la pantalla**. Guarda el `Future` en una variable en `initState`.

### Errores de red

| Qué pasa | Qué excepción | Qué mostrar |
|---|---|---|
| Sin conexión o servidor inaccesible | `http.ClientException` (o `SocketException` en móvil) | «Sin conexión. Revisa tu red» |
| El servidor tarda demasiado | `TimeoutException` (de `dart:async`) | «El servidor no responde» |
| El servidor responde 404, 500… | La que lances tú al comprobar `statusCode` | «Error del servidor (500)» |
| El JSON no tiene la forma esperada | `FormatException` / `TypeError` | «Datos incorrectos» |

```dart
try {
  final lista = await _servicio.ultimos();
  // ...
} on TimeoutException {
  _mostrar('El servidor no responde');
} on http.ClientException {
  _mostrar('Sin conexión');
} catch (e) {
  _mostrar('Error inesperado: $e');
}
```

!!! note "Web y CORS"
    En Chrome, algunas APIs bloquean las peticiones desde otra web (política **CORS**). Si una API funciona en el móvil pero no en Chrome, es eso. La del USGS lo permite; vuestra API de PMDM puede necesitar `@CrossOrigin` en Spring Boot.

!!! example "G1 · Guiado en clase: terremotos"
    Montad entre todos el ejemplo completo. Después: al tocar un terremoto, abrir su ubicación en Google Maps con `url_launcher` (Tema 4).

### Enviar datos: POST, PUT y DELETE

Contra vuestra API de PMDM (cambia la URL y el modelo por los vuestros):

```dart
class ServicioLugares {
  static const _base = 'https://mi-api.onrender.com/api/lugares';
  static const _cabeceras = {'Content-Type': 'application/json'};

  Future<List<Lugar>> todos() async {
    final r = await http.get(Uri.parse(_base)).timeout(const Duration(seconds: 60));
    _comprobar(r);
    return (jsonDecode(utf8.decode(r.bodyBytes)) as List)
        .map((e) => Lugar.fromJson(e as Map<String, dynamic>))
        .toList();
  }

  Future<Lugar> crear(Lugar l) async {
    final r = await http.post(Uri.parse(_base), headers: _cabeceras, body: jsonEncode(l.toJson()));
    _comprobar(r);
    return Lugar.fromJson(jsonDecode(utf8.decode(r.bodyBytes)) as Map<String, dynamic>);
  }

  Future<void> actualizar(Lugar l) async {
    final r = await http.put(Uri.parse('$_base/${l.id}'), headers: _cabeceras, body: jsonEncode(l.toJson()));
    _comprobar(r);
  }

  Future<void> borrar(int id) async {
    final r = await http.delete(Uri.parse('$_base/$id'));
    _comprobar(r);
  }

  void _comprobar(http.Response r) {
    if (r.statusCode < 200 || r.statusCode >= 300) {
      throw Exception('Error ${r.statusCode}: ${r.body}');
    }
  }
}
```

Y en el modelo, el método inverso a `fromJson`:

```dart
Map<String, dynamic> toJson() => {'nombre': nombre, 'descripcion': descripcion};
```

!!! warning "Render gratuito tarda en despertar"
    Los servicios gratuitos de Render se «duermen» tras un rato sin uso y la **primera petición puede tardar casi un minuto**. Por eso el `timeout` de 60 segundos en `todos()` y un mensaje de «Despertando el servidor…» mientras tanto.

!!! example "G2 · Guiado en clase: mi API"
    Cada uno conecta su app con **su** API de PMDM: listar con `FutureBuilder` y crear un elemento desde un formulario (Tema 3). Si tu API no funciona, usa [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts), que acepta GET y POST de prueba.

---

## 2. Datos locales

| Opción | Para qué | Plataformas |
|---|---|---|
| `shared_preferences` | Pares clave-valor pequeños: ajustes, modo oscuro, último usuario, un carrito sencillo | Todas |
| `sqflite` | Base de datos SQLite: listas de registros, consultas | Android, iOS, macOS |
| Firestore con caché | Datos en la nube que también funcionan sin conexión | Todas |

### `shared_preferences`

```bash
flutter pub add shared_preferences
```

```dart
import 'package:shared_preferences/shared_preferences.dart';

class Ajustes {
  Future<void> guardarModoOscuro(bool valor) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool('modoOscuro', valor);
  }

  Future<bool> leerModoOscuro() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getBool('modoOscuro') ?? false;     // null si nunca se guardó
  }
}
```

Tipos admitidos: `bool`, `int`, `double`, `String` y `List<String>`. Para guardar un objeto, conviértelo a JSON con `jsonEncode` y guárdalo como `String`.

!!! example "G3 · Guiado en clase: carrito que sobrevive"
    En **Cádiz Market** (Tema 3), haced que el carrito se guarde en `shared_preferences` cada vez que cambia (dentro del `ChangeNotifier`) y se cargue al arrancar. Cerrad la app del todo y abridla: el carrito sigue ahí.

### SQLite con `sqflite`

```bash
flutter pub add sqflite path
```

```dart
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

class Nota {
  Nota({this.id, required this.texto, required this.fecha});
  final int? id;
  final String texto;
  final DateTime fecha;

  Map<String, Object?> toMap() =>
      {'id': id, 'texto': texto, 'fecha': fecha.millisecondsSinceEpoch};

  factory Nota.fromMap(Map<String, Object?> m) => Nota(
        id: m['id'] as int,
        texto: m['texto'] as String,
        fecha: DateTime.fromMillisecondsSinceEpoch(m['fecha'] as int),
      );
}

class BaseDatos {
  Database? _db;

  Future<Database> get db async {
    return _db ??= await openDatabase(
      join(await getDatabasesPath(), 'notas.db'),
      version: 1,
      onCreate: (db, version) => db.execute(
        'CREATE TABLE notas(id INTEGER PRIMARY KEY AUTOINCREMENT, texto TEXT NOT NULL, fecha INTEGER NOT NULL)',
      ),
    );
  }

  Future<int> insertar(Nota n) async => (await db).insert('notas', n.toMap()..remove('id'));

  Future<List<Nota>> todas() async {
    final filas = await (await db).query('notas', orderBy: 'fecha DESC');
    return filas.map(Nota.fromMap).toList();
  }

  Future<int> borrar(int id) async =>
      (await db).delete('notas', where: 'id = ?', whereArgs: [id]);
}
```

!!! info "Ya lo conoces (Acceso a Datos / PMDM)"
    Es SQL normal. Lo nuevo es que todas las operaciones son **asíncronas** (`Future`). Usa siempre `whereArgs` en lugar de concatenar valores en la consulta (evita inyección SQL).

!!! note "SQLite en web y escritorio"
    `sqflite` funciona en Android, iOS y macOS. Para Windows, Linux o web hace falta `sqflite_common_ffi` (y su variante web). En este módulo, SQLite se prueba en el móvil.

---

## 3. Firebase: autenticación y base de datos en la nube

**Firebase** es la plataforma de Google con base de datos en tiempo real (Firestore), autenticación, almacenamiento de ficheros y hosting. Tiene soporte oficial en Flutter (**FlutterFire**) y una capa gratuita más que suficiente para clase.

### Configuración (una vez por proyecto)

**1. Crea el proyecto** en [console.firebase.google.com](https://console.firebase.google.com) con tu cuenta de Google. Dentro, activa **Firestore Database** (modo producción, ubicación europea) y **Authentication → Correo electrónico/contraseña**.

**2. Instala las herramientas** (una sola vez por ordenador). La CLI de Firebase necesita Node.js:

```bash
npm install -g firebase-tools
```

```bash
firebase login
```

```bash
dart pub global activate flutterfire_cli
```

!!! warning "Si `flutterfire` no se reconoce"
    Hay que añadir la carpeta de paquetes globales de Dart al PATH: `%LOCALAPPDATA%\Pub\Cache\bin` en Windows o `$HOME/.pub-cache/bin` en macOS y Linux (igual que hicisteis con Flutter en el Tema 1).

**3. Conecta tu app**, desde la carpeta del proyecto Flutter:

```bash
flutterfire configure
```

Elige tu proyecto de Firebase y las plataformas. Genera `lib/firebase_options.dart`.

**4. Añade los paquetes:**

```bash
flutter pub add firebase_core firebase_auth cloud_firestore
```

**5. Inicializa Firebase** en `main`:

```dart
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();          // necesario antes de await
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
  runApp(const MiApp());
}
```

### Autenticación

```dart
import 'package:firebase_auth/firebase_auth.dart';

final _auth = FirebaseAuth.instance;

Future<void> registrar(String email, String clave) =>
    _auth.createUserWithEmailAndPassword(email: email, password: clave);

Future<void> entrar(String email, String clave) =>
    _auth.signInWithEmailAndPassword(email: email, password: clave);

Future<void> salir() => _auth.signOut();
```

Los errores llegan como `FirebaseAuthException` con un `code` (`invalid-email`, `weak-password`, `email-already-in-use`, `invalid-credential`…) que conviene traducir al usuario.

**Mostrar una pantalla u otra según haya sesión** (un `Stream`):

```dart
class Puerta extends StatelessWidget {
  const Puerta({super.key});

  @override
  Widget build(BuildContext context) {
    return StreamBuilder<User?>(
      stream: FirebaseAuth.instance.authStateChanges(),
      builder: (context, snap) {
        if (snap.connectionState == ConnectionState.waiting) {
          return const Scaffold(body: Center(child: CircularProgressIndicator()));
        }
        return snap.data == null ? const PantallaLogin() : const PantallaInicio();
      },
    );
  }
}
```

### Firestore

Firestore guarda **documentos** (mapas clave-valor) dentro de **colecciones**. No hay tablas ni SQL.

```text
usuarios (colección)
 └── <uid del usuario> (documento)
      └── lugares (subcolección)
           ├── abc123 → { nombre: "La Caleta", lat: 36.53, lon: -6.30, fecha: ... }
           └── def456 → { ... }
```

```dart
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';

CollectionReference<Map<String, dynamic>> get _misLugares {
  final uid = FirebaseAuth.instance.currentUser!.uid;
  return FirebaseFirestore.instance.collection('usuarios').doc(uid).collection('lugares');
}

// Crear
Future<void> crearLugar(String nombre, double lat, double lon) => _misLugares.add({
      'nombre': nombre,
      'lat': lat,
      'lon': lon,
      'fecha': FieldValue.serverTimestamp(),
    });

// Actualizar y borrar
Future<void> renombrar(String id, String nombre) => _misLugares.doc(id).update({'nombre': nombre});
Future<void> borrarLugar(String id) => _misLugares.doc(id).delete();
```

**Leer en tiempo real** con `StreamBuilder`: si otro dispositivo añade un lugar, aparece solo.

```dart
StreamBuilder<QuerySnapshot<Map<String, dynamic>>>(
  stream: _misLugares.orderBy('fecha', descending: true).snapshots(),
  builder: (context, snap) {
    if (snap.hasError) return Center(child: Text('Error: ${snap.error}'));
    if (!snap.hasData) return const Center(child: CircularProgressIndicator());
    final docs = snap.data!.docs;
    if (docs.isEmpty) return const Center(child: Text('Aún no hay lugares'));
    return ListView.builder(
      itemCount: docs.length,
      itemBuilder: (context, i) {
        final datos = docs[i].data();
        return ListTile(
          title: Text(datos['nombre'] as String? ?? ''),
          subtitle: Text('${datos['lat']}, ${datos['lon']}'),
          trailing: IconButton(
            icon: const Icon(Icons.delete),
            onPressed: () => borrarLugar(docs[i].id),
          ),
        );
      },
    );
  },
)
```

### Reglas de seguridad

Sin reglas, **cualquiera** podría leer y borrar tu base de datos. En la consola: **Firestore → Reglas**:

```text
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /usuarios/{uid}/{document=**} {
      allow read, write: if request.auth != null && request.auth.uid == uid;
    }
  }
}
```

Cada usuario solo puede leer y escribir **sus** datos.

!!! example "G4 · Guiado en clase: login + lista en la nube"
    Entre todos: pantalla de login y registro, `Puerta` con `authStateChanges`, y una lista de notas en Firestore con alta y borrado. Abrid la app en el móvil **y** en Chrome con el mismo usuario: lo que se añade en uno aparece en el otro al instante.

!!! note "Cuentas de Google en el centro"
    Si las cuentas del instituto no permiten crear proyectos de Firebase, usad una cuenta personal de Google. Cada alumno trabaja en **su propio** proyecto de Firebase.

---

## Ejercicios rápidos de clase { #ejercicios-rapidos }

Cortos (5-15 minutos). Se hacen **en clase**, justo después de explicar cada apartado, y se corrigen en voz alta. No se entregan: son el entrenamiento para el boletín y las prácticas.

### Sesión 1 · 30 nov

| # | Ejercicio | Apartado |
|---|---|---|
| R1 | **Leer un JSON.** Abre el feed de terremotos en el navegador y apunta: dónde está la lista, dónde la magnitud y en qué orden van latitud y longitud | 1 |
| R2 | **JSON en Dart puro.** En un fichero `.dart` de consola, haz `jsonDecode` de una cadena con un usuario y muestra su nombre y su ciudad | 1 |
| R3 | **Modelo `Chiste`.** Escribe `Chiste.fromJson` y conviértete una lista de 3 chistes escrita a mano en una `List<Chiste>` | 1 |
| R4 | **Un usuario de internet.** Pide `https://jsonplaceholder.typicode.com/users/1` y muestra su nombre con `FutureBuilder` | 1 |
| R5 | **Provoca un timeout.** Pon `timeout` de 1 milisegundo a la petición anterior y muestra un mensaje amable al usuario | 1 · Errores de red |
| R6 | **Mi primer POST.** Envía un post a `https://jsonplaceholder.typicode.com/posts` y muestra el `id` que devuelve el servidor | 1 · Enviar datos |

### Sesión 2 · 14 dic

| # | Ejercicio | Apartado |
|---|---|---|
| R7 | **Recuérdame.** Un `TextField` y un botón que guarda tu nombre; al reabrir la app, te saluda por tu nombre | 2 |
| R8 | **La última pestaña.** La app recuerda qué pestaña del `NavigationBar` estaba abierta al cerrarla | 2 |
| R9 | **Favoritos.** Marca ciudades como favoritas y guárdalas como `List<String>` en `shared_preferences` | 2 |
| R10 | **SQLite en consola.** Inserta 3 notas con `sqflite` y lístalas con `debugPrint` al pulsar un botón | 2 |
| R11 | **Hola, Firestore.** Un botón que añade un documento `{texto, fecha}` a una colección. Compruébalo en la consola web de Firebase | 3 |
| R12 | **Tiempo real.** Lista con `StreamBuilder` de esa colección. Cambia un documento **desde la consola web** y míralo cambiar en la app | 3 |

---

## Boletín de ejercicios { #boletin-de-ejercicios }

!!! abstract "Instrucciones"
    - **Individual.** Proyecto `boletin_t5` con una pantalla de inicio que lleve a cada ejercicio.
    - **Entrega:** repositorio de GitHub · **Fecha:** domingo 20 de diciembre.

| # | Ejercicio | Practica |
|---|---|---|
| B1 | **Chiste aleatorio.** Botón que pide un chiste a `https://official-joke-api.appspot.com/random_joke` y muestra pregunta y respuesta (la respuesta aparece al tocar). Indicador de carga y mensaje de error | GET, `jsonDecode`, estados de carga |
| B2 | **Modelo a mano.** Dado un JSON de ejemplo de un usuario con dirección anidada y lista de teléfonos (te lo da el profesor), escribe `Usuario.fromJson` y `toJson` y comprueba en `main` que `Usuario.fromJson(u.toJson())` da lo mismo | Modelos, JSON anidado |
| B3 | **Lista de posts.** `FutureBuilder` con los posts de `https://jsonplaceholder.typicode.com/posts`, `RefreshIndicator` y pantalla de detalle con los comentarios de cada post (`/posts/<id>/comments`) | `FutureBuilder`, navegación con datos |
| B4 | **Modo avión.** Al ejercicio B3 añádele gestión de errores diferenciada: sin conexión, timeout de 5 s y error del servidor (prueba una URL que dé 404). Cada caso con su icono y botón de reintentar | Errores de red |
| B5 | **Alta en mi API.** Formulario que hace POST a tu API de PMDM (o a JSONPlaceholder) y muestra la respuesta del servidor. Botón desactivado mientras se envía | POST, JSON, formularios |
| B6 | **Ajustes persistentes.** Pantalla de ajustes con modo oscuro, tamaño de letra (`Slider`) y nombre de usuario. Todo se conserva al cerrar la app y se aplica a toda la app | `shared_preferences`, tema |
| B7 | **Contador de visitas.** Muestra cuántas veces se ha abierto la app y la fecha y hora de la última vez | `shared_preferences` con `int` y `String` |
| B8 | **Diario con SQLite.** Notas con texto y fecha: alta, lista ordenada por fecha, borrado deslizando y búsqueda por texto (`where: 'texto LIKE ?'`) | `sqflite`, CRUD |
| B9 | **Login con Firebase.** Registro, entrada y salida con email y contraseña. Mensajes en español para al menos 4 códigos de error de `FirebaseAuthException` | Firebase Auth |
| B10 | **Lista compartida en tiempo real.** Lista de la compra en Firestore. Ábrela en dos dispositivos con el mismo usuario y comprueba que se sincroniza. Reglas de seguridad por usuario | Firestore, `StreamBuilder`, reglas |

---

## Práctica 5.1 · Terremotos y mi API { #practica-51-terremotos-y-mi-api }

!!! abstract "Datos de la entrega"
    - **Individual** · **RA2 · CE d**
    - **Entrega:** repositorio `terremotos` + vídeo de 1-2 minutos · **Fecha:** domingo 13 de diciembre

Adaptación de la actividad del curso pasado. Una app con **dos pestañas** (`NavigationBar`):

**Pestaña «Terremotos»** (API del USGS):

1. Botón **«Último terremoto»**: muestra el más reciente con magnitud, lugar, fecha local, profundidad y una imagen del planeta.
2. Debajo, la **lista** de los de hoy ordenada por magnitud, con color según la magnitud y filtro por magnitud mínima (`Slider`).
3. Al tocar uno, abrir su posición en mapas.
4. Investiga el feed y añade un selector para elegir entre «última hora», «hoy» y «última semana» (son URLs distintas del mismo servicio).

**Pestaña «Mi API»** (la API Spring Boot que desplegaste en PMDM):

1. Listar los elementos con `FutureBuilder` y mensaje de «Despertando el servidor…».
2. Crear uno nuevo con un formulario validado (POST).
3. Borrar deslizando (DELETE) y editar (PUT).

**En las dos:** modelo con `fromJson`/`toJson`, servicio separado de la interfaz y gestión de errores diferenciada.

| Criterio | Peso |
|---|---|
| Modelos y servicios separados, JSON bien tratado (incluidos nulos) | 25 % |
| Terremotos: último, lista, filtro y selector de periodo | 25 % |
| Mi API: CRUD completo | 30 % |
| Errores de red, carga y reintento | 20 % |

## Práctica 5.2 · Mis lugares { #practica-52-mis-lugares }

!!! abstract "Datos de la entrega"
    - **Individual** · **RA2 · CE a, b, d, e** · Práctica de síntesis del RA2
    - **Entrega:** repositorio `mis_lugares` + vídeo con la app en el móvil **y** en Chrome a la vez · **Fecha:** domingo 20 de diciembre

Una app para guardar tus sitios favoritos de Cádiz. Junta los temas 3, 4 y 5:

1. **Login** con Firebase Auth (registro, entrada, salida).
2. **Alta de un lugar:** nombre, descripción, categoría (playa, restaurante, monumento, otro), **ubicación actual por GPS** y **foto** con `image_picker`. La foto se guarda **en local** (ruta del fichero en SQLite o `shared_preferences`) y el resto de datos en **Firestore**.
3. **Lista** en tiempo real desde Firestore, con filtro por categoría y la **distancia** desde tu posición actual a cada lugar.
4. **Detalle** con la foto (si está en ese dispositivo), la descripción, un botón para abrirlo en mapas y otro para **compartirlo** con `share_plus`.
5. **Ajustes** en `shared_preferences`: modo oscuro y radio máximo para mostrar lugares cercanos.
6. **Reglas de Firestore** que solo permitan a cada usuario ver sus lugares (captura en el README).

| Criterio | Peso |
|---|---|
| Autenticación y reglas de seguridad | 20 % |
| Firestore: alta, lista en tiempo real, borrado y filtro | 25 % |
| GPS y foto integrados (Tema 4) | 20 % |
| Persistencia local (foto y ajustes) | 20 % |
| Interfaz, navegación y errores | 15 % |
