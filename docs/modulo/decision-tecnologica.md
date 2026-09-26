# Decisión tecnológica: Flutter + Dart

La decisión está **tomada**. Esta página recoge los argumentos para defenderla ante el departamento o la inspección.

## Resumen en una frase

> Flutter es el framework multiplataforma más usado, su lenguaje (Dart) no da ventaja ni a quien viene de Java ni a quien viene de Kotlin, y su forma de construir interfaces es la misma que el alumnado ya practica con Jetpack Compose en DI.

## 1. Es el líder del mercado multiplataforma

En la encuesta de Statista a desarrolladores de frameworks multiplataforma, **Flutter aparece en torno al 46 %** de uso frente al **~35 % de React Native**. Es el dato de referencia que se sigue citando en 2026 en los análisis del sector.

!!! warning "Cita el dato con precisión"
    El 46 % / 35 % procede de la **encuesta de Statista de 2023**, no de una encuesta de 2026: los artículos de 2026 lo reproducen. Si lo citas en la programación o ante inspección, pon *"Statista, encuesta a desarrolladores (2023), dato vigente como referencia en 2026"*. Evita que alguien lo desmonte por una fecha.

!!! info "Contrapunto honesto (conviene tenerlo preparado)"
    React Native tiene **más ofertas de empleo** en algunos mercados (sobre todo EE. UU.) por su cercanía al ecosistema web/React. El argumento de fondo no cambia: lo que buscamos es que el alumnado **entienda la arquitectura multiplataforma** y la transfiera. Lo aprendido con Flutter (widgets declarativos, estado, asincronía, despliegue) se transfiere a React Native, a Compose Multiplatform o a SwiftUI.

## 2. Dart es el punto medio exacto entre Java y Kotlin

El aula llega partida en dos: **la mitad solo ha programado en Java** en 1º y **la otra mitad solo en Kotlin**. Elegir Kotlin (KMP) daría ventaja a una mitad; elegir JavaScript/TypeScript (React Native, Ionic) obligaría a las dos a cambiar de paradigma de tipos.

| Rasgo | Java | Kotlin | **Dart** |
|---|---|---|---|
| Tipado estático | ✔ | ✔ | ✔ |
| Llaves y `;` | ✔ | llaves sí, `;` no | ✔ |
| Clases, constructores, `extends` | ✔ | con otra sintaxis | ✔ (estilo Java) |
| Null safety en el tipo (`String?`) | ✘ | ✔ | ✔ (estilo Kotlin) |
| Inferencia (`var`) | ✔ (Java 10+) | ✔ | ✔ |
| Funciones de extensión | ✘ | ✔ | ✔ |
| Lambdas cortas | `x -> x * 2` | `{ x -> x * 2 }` | `(x) => x * 2` |

Resultado: **ninguna mitad arranca con ventaja** y ambas reconocen la mayor parte de la sintaxis el primer día. Por eso el Dart del Tema 1 se apoya siempre en comparaciones con Java y Kotlin.

## 3. Misma mentalidad que Jetpack Compose (DI)

En Desarrollo de Interfaces el alumnado construye UIs **declarativas** con Compose: funciones que describen la interfaz, anidadas, que se redibujan cuando cambia el estado. Flutter hace exactamente eso con **widgets**.

=== "Compose (DI)"

    ```kotlin
    Scaffold(
        topBar = { TopAppBar(title = { Text("Hola") }) }
    ) { padding ->
        Column(Modifier.padding(padding)) {
            Text("Contador: $contador")
            Button(onClick = { contador++ }) { Text("Sumar") }
        }
    }
    ```

=== "Flutter"

    ```dart
    Scaffold(
      appBar: AppBar(title: const Text('Hola')),
      body: Column(
        children: [
          Text('Contador: $contador'),
          ElevatedButton(
            onPressed: () => setState(() => contador++),
            child: const Text('Sumar'),
          ),
        ],
      ),
    )
    ```

Mismo `Scaffold`, mismo `Column`, mismo `Text`. La UI declarativa **no se re-explica**: se **transfiere**.

## 4. Herramientas pensadas para aprender

| Herramienta | Por qué ayuda en el aula |
|---|---|
| `flutter doctor` | Diagnostica el entorno y dice qué falta y cómo arreglarlo. Menos tiempo perdido en instalaciones. |
| Hot reload | Cambias el código y lo ves en el emulador en menos de un segundo sin perder el estado. Ciclo prueba-error muy corto. |
| DartPad | Dart (y Flutter) en el navegador, sin instalar. Permite empezar el primer día. |
| Catálogo de widgets oficial | Documentación visual con ejemplos ejecutables. |
| DevTools | Inspector de widgets, rendimiento, memoria y red. Base del RA3. |

## 5. Encaje con los RA

- **RA1** (arquitectura): Flutter es el mejor ejemplo para explicar la diferencia entre *compilar a nativo* y *usar componentes nativos*, frente a WebView y React Native.
- **RA2** (desarrollo): cubre interfaz, acceso a hardware mediante plugins y datos locales/remotos (incluido Firebase, con soporte oficial).
- **RA3** (calidad y despliegue): trae pruebas unitarias, de widget y de integración de serie, perfilado con DevTools y generación de builds para Android, iOS, web y escritorio.

## Fuentes

- [Statista — Cross-platform mobile frameworks used by developers worldwide](https://www.statista.com/statistics/869224/worldwide-software-developer-working-hours/)
- [Quash — Flutter vs React Native statistics 2026 (origen del dato 46/35)](https://quashbugs.com/blog/flutter-vs-react-native-statistics)
- [Documentación oficial de Flutter](https://docs.flutter.dev)
