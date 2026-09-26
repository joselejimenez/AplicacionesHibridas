# Elegir con criterio

!!! info "Ya lo conoces (PMDM)"
    En PMDM visteis una visión general de cómo elegir tecnología. Aquí la aplicamos **con lo que ahora sabéis de la arquitectura interna** de cada opción.

## Tabla comparativa

| Criterio | Nativo | Híbrido WebView (Ionic + Capacitor) | Flutter | React Native | KMP |
|---|---|---|---|---|---|
| **Lenguaje** | Kotlin + Swift | HTML/CSS + JS/TS | Dart | JS/TS | Kotlin (+ Swift para UI iOS) |
| **Código compartido** | 0 % | ~100 % | ~100 % | ~90-100 % | Lógica sí; UI opcional |
| **Ejecución** | Nativa | Motor JS del navegador | Código máquina (AOT) | Motor JS (Hermes) | Nativa |
| **Interfaz** | Componentes del SO | HTML en WebView | Dibujada por Flutter | Componentes del SO | Del SO o Compose |
| **Rendimiento** | ★★★★★ | ★★☆☆☆ | ★★★★☆ | ★★★★☆ | ★★★★★ |
| **Aspecto nativo** | ★★★★★ | ★★☆☆☆ | ★★★☆☆ (imitado) | ★★★★★ | ★★★★★ / ★★★☆☆ |
| **Coherencia entre plataformas** | ★★☆☆☆ | ★★★★☆ | ★★★★★ | ★★★☆☆ | ★★☆☆☆ / ★★★★★ |
| **Acceso a hardware** | Directo e inmediato | Plugins + puente | Plugins (channels/FFI) | Módulos nativos (JSI) | Directo |
| **Web y escritorio** | No | Web muy natural | Sí (web, Win, Mac, Linux) | Web parcial; escritorio con proyectos aparte | Sí con Compose MP |
| **Tamaño de la app** | Mínimo | Pequeño | Mayor (incluye motor) | Medio (incluye Hermes) | Pequeño-medio |
| **Curva para un DAM** | Dos lenguajes y dos SDK | Baja si sabe web | Media (Dart es fácil) | Media si sabe JS/React | Baja si sabe Kotlin |
| **Coste de mantenimiento** | Alto (x2) | Bajo | Bajo | Bajo-medio | Medio |

Las estrellas son **orientativas**: sirven para discutir, no para memorizar.

## Preguntas que deciden

Antes de mirar la tabla, responde a esto sobre el proyecto:

1. **¿Qué sabe hacer el equipo que ya tengo?** Un equipo web rinde antes con Ionic o React Native; uno Android, con KMP.
2. **¿Tiene que parecer 100 % de Android y de iOS, o tiene que parecer "de mi marca"?** Marca propia → Flutter. Aspecto de plataforma → nativo, React Native o KMP.
3. **¿Cuánto rendimiento gráfico necesita?** Juegos casuales, animaciones, mapas con mucho movimiento → descarta WebView.
4. **¿Usa hardware muy específico o APIs recién salidas?** (realidad aumentada, Bluetooth avanzado, widgets de pantalla de inicio) → nativo o KMP.
5. **¿También tiene que funcionar en web o escritorio?**
6. **¿Hay ya una app nativa en marcha?** → KMP permite ir compartiendo poco a poco.
7. **¿Presupuesto y plazo?**

## Casos prácticos

!!! example "Caso 1 · App de la Hermandad"
    Una hermandad de Cádiz quiere una app con horarios de salida, recorrido en un mapa y noticias. Presupuesto mínimo, la hará un único alumno de prácticas que sabe HTML, CSS y algo de JavaScript. Tiene que estar también en la web.

    ??? success "Una respuesta razonable"
        **Híbrido WebView (Ionic + Capacitor)** o incluso una **PWA**. Es contenido, no hay exigencia gráfica, el perfil es web y la web sale "gratis". Flutter también serviría, pero obliga a aprender Dart sin necesidad.

!!! example "Caso 2 · Startup de fitness"
    Una startup quiere una app con animaciones muy cuidadas, gráficas de progreso y una identidad visual fuerte e idéntica en Android e iOS. Equipo nuevo de 3 personas, sin experiencia previa en móvil. Quieren salir en 4 meses.

    ??? success "Una respuesta razonable"
        **Flutter.** Marca visual idéntica en ambas plataformas, buen rendimiento en animaciones, un solo código y un equipo pequeño sin herencia tecnológica.

!!! example "Caso 3 · Banco con app Android madura"
    Un banco tiene una app Android nativa de 8 años con Kotlin y Compose, y quiere lanzar la versión de iOS sin reescribir la lógica de seguridad, validaciones y cifrado. Los usuarios de iOS esperan que la app se sienta "de Apple".

    ??? success "Una respuesta razonable"
        **Kotlin Multiplatform (clásico).** Se extrae la lógica existente a un módulo común, la app Android sigue igual y se hace la UI de iOS en SwiftUI.

!!! example "Caso 4 · Red social con web en React"
    Una empresa tiene una web grande hecha en React y un equipo de 15 desarrolladores de JavaScript. Quiere una app móvil que se sienta nativa en cada plataforma.

    ??? success "Una respuesta razonable"
        **React Native.** Aprovecha el equipo, las bibliotecas y parte de la lógica de la web, y usa componentes nativos.

!!! example "Caso 5 · Tú decides"
    El Ayuntamiento quiere una app para avisar de incidencias en la vía pública: el ciudadano hace una **foto**, la app toma la **ubicación GPS** y lo envía. Debe funcionar en Android, iOS **y** en el ordenador de los técnicos municipales (Windows). Lo va a mantener una empresa pequeña durante 5 años.

    Elige tecnología y justifícala respondiendo a las 7 preguntas. **No hay una única respuesta correcta; hay respuestas bien o mal justificadas.**
