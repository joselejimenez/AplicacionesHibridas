# Práctica Tema 2 · Informe de arquitectura

!!! abstract "Datos de la entrega"
    - **En parejas** (a ser posible, una persona que venga de Java y otra de Kotlin)
    - **Entrega:** un PDF en la plataforma del módulo
    - **Fecha límite:** domingo 8 de noviembre, 23:59
    - **RA1 · CE a, b, c, d** (esta práctica **cierra el RA1**)

## Parte 1 · Detectives de arquitectura (CE a, b)

Elegid **4 apps reales** que tengáis en el móvil. Para cada una, averiguad con qué tecnología está hecha y justificad cómo lo habéis sabido.

Pistas para investigar:

- Buscad en la web de empleo o el blog técnico de la empresa ("we use Flutter", "React Native at…").
- Activad en Android **Opciones de desarrollador → Mostrar límites de diseño**: las apps nativas y React Native muestran los límites de cada componente; Flutter se ve como un único gran lienzo; un WebView también, aunque con otras pistas.
- Mirad la sección de licencias de código abierto de la app ("Acerca de" → "Licencias").

Para cada app, responded a **las tres preguntas** del tema (¿en qué se ejecuta?, ¿quién dibuja?, ¿cómo llega al hardware?).

## Parte 2 · Diagrama (CE b)

Dibujad (a mano y escaneado, o con cualquier herramienta) el diagrama de capas de **Flutter** y de **React Native**, señalando dónde está la diferencia entre *nativo en ejecución* y *nativo en widgets*.

## Parte 3 · Informe de decisión (CE c, d)

Resolved el **[Caso 5 del Ayuntamiento](04-comparativa.md#casos-practicos)**:

1. Responded a las 7 preguntas de la página *Elegir con criterio*.
2. Descartad razonadamente **al menos tres** enfoques.
3. Elegid uno y dad **dos riesgos** de vuestra elección y cómo los mitigaríais.

Extensión máxima: 2 páginas.

## Rúbrica

| Criterio | CE | Peso | Excelente | Adecuado | Insuficiente |
|---|---|---|---|---|---|
| Identificación de enfoques en apps reales | a | 25 % | 4 apps bien identificadas con evidencia | Identificadas sin evidencia clara | Errores de concepto |
| Arquitectura interna y diagrama | b | 25 % | Diagramas correctos y distinción ejecución/widgets explicada con precisión | Diagramas correctos pero explicación superficial | Confunde enfoques |
| Valoración de ventajas e inconvenientes | c | 25 % | Compara con criterios técnicos y del proyecto, sin tópicos | Compara pero con argumentos genéricos | Sin comparación real |
| Decisión justificada | d | 25 % | Decisión coherente, descartes razonados y riesgos con mitigación | Decisión razonable con justificación incompleta | Sin justificar |
