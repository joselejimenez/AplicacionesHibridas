# Práctica Tema 2 · Informe de arquitectura y diseño

!!! abstract "Datos de la entrega"
    - **En parejas** (a ser posible, una persona que venga de Java y otra de Kotlin)
    - **Se hace en clase:** el lunes 9 de noviembre, en la primera hora (≈ 50 minutos)
    - **Entrega:** al terminar la clase, un PDF en la plataforma del módulo. Vale hacerlo en papel y subir las fotos
    - **RA1 · CE a, b, c, d, e**

!!! tip "Reparto del tiempo"
    | Parte | Minutos |
    |---|---|
    | 1 · Detectives de arquitectura | 10 |
    | 2 · Arquitectura y patrón | 10 |
    | 3 · Selección de tecnología | 15 |
    | 4 · Diseño de la app | 15 |

    Respuestas cortas: se valora que esté **bien justificado**, no que sea largo.

## Parte 1 · Detectives de arquitectura (CE a)

Elegid **2 apps reales** que tengáis en el móvil. Para cada una, averiguad con qué tecnología está hecha y decid cómo lo habéis sabido.

Pistas para investigar:

- Activad en Android **Opciones de desarrollador → Mostrar límites de diseño**: las apps nativas y React Native muestran los límites de cada componente; Flutter se ve como un único gran lienzo; un WebView también, aunque con otras pistas.
- Mirad la sección de licencias de código abierto de la app ("Acerca de" → "Licencias").
- Buscad en la web de empleo o el blog técnico de la empresa ("we use Flutter", "React Native at…").

Para cada app, responded a **las tres preguntas** del tema: ¿en qué se ejecuta?, ¿quién dibuja?, ¿cómo llega al hardware?

## Parte 2 · Arquitectura y patrón (CE b)

1. Dibujad el **diagrama de capas de Flutter** (de vuestra app hasta el sistema operativo) y explicad en dos líneas en qué se diferencia de un enfoque *nativo en widgets* como React Native.
2. Decid qué **patrón de arquitectura** usaríais para la app del Caso 5 (parte 3) y por qué, según su tamaño.

## Parte 3 · Selección de tecnología (CE c)

Resolved el **[Caso 5 del Ayuntamiento](04-comparativa.md#casos-practicos)**:

1. Responded a las 7 preguntas de la página *Elegir con criterio* (una línea por pregunta).
2. Descartad razonadamente **al menos dos** enfoques.
3. Elegid uno y dad **un riesgo** de vuestra elección y cómo lo mitigaríais.

## Parte 4 · Diseño de la app (CE d, e)

Para la app del Caso 5, con la tecnología que hayáis elegido:

1. **Estructura:** las carpetas de `lib/` (vista, estado, repositorio, servicios, modelos) con una o dos clases en cada una.
2. **Boceto mobile-first** de la pantalla de **alta de una incidencia** en dos tamaños: móvil y el ordenador de los técnicos. Marcad qué cambia entre uno y otro y qué navegación usa cada uno.
3. **Tres decisiones de diseño** justificadas: una de usabilidad, una de rendimiento y una de adaptabilidad.

## Rúbrica

| Criterio | CE | Peso | Excelente | Adecuado | Insuficiente |
|---|---|---|---|---|---|
| Identificación de enfoques en apps reales | a | 20 % | 2 apps bien identificadas con evidencia y las tres preguntas respondidas | Identificadas sin evidencia clara | Errores de concepto |
| Arquitectura y patrón | b | 20 % | Diagrama correcto, diferencia con *nativo en widgets* precisa y patrón justificado | Diagrama correcto pero patrón sin justificar | Confunde enfoques o patrones |
| Selección de tecnología | c | 20 % | Decisión coherente con el caso, descartes razonados y riesgo con mitigación | Decisión razonable con justificación incompleta | Sin justificar |
| Estructura de la app | d | 20 % | Carpetas y clases coherentes; decisiones de usabilidad, rendimiento y adaptabilidad concretas | Estructura correcta con decisiones genéricas | Sin estructura clara |
| Mobile-first y responsive | e | 20 % | Dos tamaños con cambios de distribución y navegación bien pensados | Dos tamaños con cambios poco claros | Un solo tamaño |
