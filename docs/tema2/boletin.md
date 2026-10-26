# Boletín de ejercicios · Tema 2

!!! abstract "Cómo usar el boletín"
    - **Individual.** Se empieza en clase y se termina en casa
    - **No es evaluable:** sirve para preparar la [práctica](practica.md) y la 1ª parcial
    - Van **de menos a más**. Al lado de cada uno tienes el criterio del RA1 que trabaja
    - Se valora que **justifiques**: casi nunca hay una única respuesta correcta

| Ejercicio | Qué practicas | CE | Tiempo |
|---|---|---|---|
| [B1 · Verdadero o falso, y por qué](#b1) | Los cuatro enfoques | a | 10 min |
| [B2 · La tabla que falta](#b2) | Las tres preguntas aplicadas a algo nuevo | a | 10 min |
| [B3 · Sigue el toque](#b3) | Qué pasa por dentro al llegar al hardware | a, b | 20 min |
| [B4 · Cuatro casos más de Cádiz](#b4) | Elegir tecnología | c | 20 min |
| [B5 · El widget que lo hace todo](#b5) | Capas y estructura | b, d | 30 min |
| [B6 · Del móvil al monitor](#b6) | Mobile-first y responsive | d, e | 30 min |

---

## B1 · Verdadero o falso, y por qué { #b1 }

Di si cada afirmación es verdadera o falsa. Si es falsa, **corrígela** en una línea.

1. Una app hecha con Ionic usa los botones de Android.
2. React Native compila tu código JavaScript a código máquina.
3. Flutter necesita un WebView para mostrar su interfaz.
4. En modo debug una app Flutter va más lenta que en release.
5. Una PWA puede usar el Bluetooth en iOS igual que una app nativa.
6. En Kotlin Multiplatform clásico la interfaz se escribe una sola vez.
7. Para compilar la versión de iOS de una app Flutter hace falta un Mac.

## B2 · La tabla que falta { #b2 }

La [tabla resumen](01-enfoques.md#las-tres-preguntas-resumidas) responde a las tres preguntas para nativo, WebView, Flutter y React Native. Complétala para los dos enfoques que no están:

| | ¿En qué se ejecuta el código? | ¿Quién dibuja los botones? | ¿Cómo llega al hardware? |
|---|---|---|---|
| **PWA** | | | |
| **KMP + Compose Multiplatform** | | | |

Después responde: ¿a cuál de los cuatro enfoques de la tabla se parece más cada uno? ¿Por qué?

## B3 · Sigue el toque { #b3 }

El usuario pulsa el botón **«Mi ubicación»** y la app muestra sus coordenadas en pantalla.

1. Ordena estos pasos para una app hecha con **Flutter**:
    - El plugin (parte Kotlin) llama a `LocationManager`
    - El usuario toca la pantalla
    - El `Future` se completa y el widget se vuelve a construir
    - Tu código Dart llama a `getCurrentPosition()`
    - Android devuelve latitud y longitud
    - El plugin (parte Dart) envía un mensaje por `MethodChannel`
    - Impeller pinta el texto con las coordenadas
2. Escribe la misma secuencia para **Ionic + Capacitor** y para **React Native**. ¿Qué pasos cambian?
3. ¿En cuál de los tres hay **más cruces** de un lenguaje a otro? ¿Y en una app **nativa**?

## B4 · Cuatro casos más de Cádiz { #b4 }

Para cada caso, elige tecnología y justifícala con **al menos tres** de las [7 preguntas](04-comparativa.md#preguntas-que-deciden). Di también qué enfoque descartas y por qué.

!!! example "Caso 6 · Los celadores del hospital"
    El hospital quiere una app interna para que los celadores registren los traslados de pacientes. Solo se usará en las **tablets Android** que compra el propio hospital. Son formularios y listas, sin nada gráfico. El presupuesto es pequeño y la hará el departamento de informática, que sabe web.

!!! example "Caso 7 · El juego del Carnaval"
    Un juego casual para adivinar coplas, con **animaciones** al acertar y un ranking. Tiene que estar en Android, iOS y también **en la web** para jugar desde el ordenador. Lo hará un equipo nuevo de dos personas.

!!! example "Caso 8 · Los barcos del puerto"
    La Autoridad Portuaria quiere una app que, al apuntar con la cámara a la bahía, **señale con realidad aumentada** el nombre de cada barco. Quiere usar las últimas funciones de ARCore y ARKit en cuanto salgan.

!!! example "Caso 9 · La cadena de tiendas"
    Una cadena de tiendas tiene desde hace 6 años una app de **iOS nativa en Swift** con mucha lógica de pagos y fidelización. Ahora quiere la versión de Android. Sus clientes de iPhone están contentos y no quieren que la app «cambie de cara».

## B5 · El widget que lo hace todo { #b5 }

Este widget funciona, pero lo mezcla todo en el mismo sitio:

```dart
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class PantallaAgrupaciones extends StatefulWidget {
  const PantallaAgrupaciones({super.key});
  @override
  State<PantallaAgrupaciones> createState() => _PantallaAgrupacionesState();
}

class _PantallaAgrupacionesState extends State<PantallaAgrupaciones> {
  List<dynamic> _datos = [];

  @override
  void initState() {
    super.initState();
    http.get(Uri.parse('https://api.ejemplo.es/coac/agrupaciones')).then((r) {
      setState(() => _datos = jsonDecode(r.body));
    });
  }

  @override
  Widget build(BuildContext context) {
    return ListView(
      children: [
        for (final a in _datos)
          if (a['modalidad'] == 'Comparsa' && a['puntos'] > 400)
            ListTile(
              title: Text(a['nombre']),
              subtitle: Text('${a['puntos']} puntos'),
              trailing: a['puntos'] > 450 ? const Icon(Icons.star) : null,
            ),
      ],
    );
  }
}
```

1. Encuentra **al menos cuatro** problemas de diseño. Pista: piensa en qué pasa si falla la red, si mañana los datos vienen de SQLite o si hay que cambiar la regla de «favorita».
2. Reparte lo que hace este widget en las capas de [Diseñar la app](05-diseno.md#1-patrones-de-arquitectura): vista, estado, repositorio, servicio y modelo. Para cada capa, di **qué clase** crearías y **qué haría**.
3. Escribe en qué fichero de `lib/` iría cada clase.

No hace falta que reescribas el código: basta con un esquema.

## B6 · Del móvil al monitor { #b6 }

La app del COAC tiene esta pantalla en el **móvil**:

- Un buscador arriba.
- Las agrupaciones en tarjetas, una debajo de otra (foto, nombre y modalidad).
- Al pulsar una tarjeta se abre su detalle en otra pantalla.
- Una barra inferior con **Inicio**, **Favoritos** y **Perfil**.

1. Dibuja la pantalla en los **tres tamaños** de los [puntos de corte](05-diseno.md#puntos-de-corte): compacto, medio y expandido.
2. Para cada tamaño, decide y marca en el dibujo:
    - cuántas columnas de tarjetas hay,
    - qué navegación se usa,
    - si la lista y el detalle se ven a la vez o en pantallas distintas,
    - qué haces para que el texto del detalle no ocupe todo el ancho de un monitor.
3. ¿Qué parte de tu diseño es **responsive** y qué parte es **adaptativa**?
