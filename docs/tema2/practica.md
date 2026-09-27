# Práctica Tema 2 · Informe de arquitectura y diseño

!!! abstract "Datos de la entrega"
    - **En parejas** (a ser posible, una persona que venga de Java y otra de Kotlin)
    - **Entrega:** un PDF en la plataforma del módulo
    - **Fecha límite:** domingo 8 de noviembre, 23:59
    - **RA1 · CE a, b, c, d, e**

## Parte 1 · Detectives de arquitectura (CE a)

Elegid **4 apps reales** que tengáis en el móvil. Para cada una, averiguad con qué tecnología está hecha y justificad cómo lo habéis sabido.

Pistas para investigar:

- Buscad en la web de empleo o el blog técnico de la empresa ("we use Flutter", "React Native at…").
- Activad en Android **Opciones de desarrollador → Mostrar límites de diseño**: las apps nativas y React Native muestran los límites de cada componente; Flutter se ve como un único gran lienzo; un WebView también, aunque con otras pistas.
- Mirad la sección de licencias de código abierto de la app ("Acerca de" → "Licencias").

Para cada app, responded a **las tres preguntas** del tema (¿en qué se ejecuta?, ¿quién dibuja?, ¿cómo llega al hardware?).

## Parte 2 · Arquitecturas y patrones (CE b)

Dibujad (a mano y escaneado, o con cualquier herramienta) el diagrama de capas de **Flutter** y de **React Native**, señalando dónde está la diferencia entre *nativo en ejecución* y *nativo en widgets*.

Añadid una tabla con el **patrón de arquitectura** que usaríais para una app pequeña, una mediana y una grande, justificando cada elección (apartado *Diseñar la app*).

## Parte 3 · Selección de tecnología (CE c)

Resolved el **[Caso 5 del Ayuntamiento](04-comparativa.md#casos-practicos)**:

1. Responded a las 7 preguntas de la página *Elegir con criterio*.
2. Descartad razonadamente **al menos tres** enfoques.
3. Elegid uno y dad **dos riesgos** de vuestra elección y cómo los mitigaríais.

Extensión máxima: 2 páginas.

## Parte 4 · Diseño de la app (CE d, e)

Para la app del Caso 5, con la tecnología que hayáis elegido:

1. **Estructura:** diagrama de capas (vista, estado, repositorio, servicios, modelos) con las clases principales y estructura de carpetas de `lib/`.
2. **Bocetos mobile-first** de dos pantallas (el alta de una incidencia y la lista de incidencias) en tres tamaños: compacto (móvil), medio (tablet) y expandido (el ordenador de los técnicos). Marcad qué cambia entre ellos y qué navegación usa cada uno.
3. **Cinco decisiones de diseño** justificadas: al menos dos de usabilidad, una de rendimiento y una de adaptabilidad.

## Rúbrica

| Criterio | CE | Peso | Excelente | Adecuado | Insuficiente |
|---|---|---|---|---|---|
| Identificación de enfoques en apps reales | a | 20 % | 4 apps bien identificadas con evidencia | Identificadas sin evidencia clara | Errores de concepto |
| Arquitecturas y patrones | b | 20 % | Diagramas correctos, distinción ejecución/widgets precisa y patrones justificados por tamaño | Diagramas correctos pero patrones sin justificar | Confunde enfoques o patrones |
| Selección de tecnología | c | 20 % | Decisión coherente con el caso, descartes razonados y riesgos con mitigación | Decisión razonable con justificación incompleta | Sin justificar |
| Estructura de la app | d | 20 % | Capas y carpetas coherentes; decisiones de usabilidad, rendimiento y adaptabilidad concretas | Estructura correcta con decisiones genéricas | Sin estructura clara |
| Mobile-first y responsive | e | 20 % | Tres tamaños con cambios de navegación y distribución bien pensados | Solo móvil y escritorio, o cambios poco claros | Un solo tamaño |
