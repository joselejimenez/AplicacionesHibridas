# Prueba de diciembre (RA1 + RA2)

**Lunes 21 de diciembre.** Modelo de prueba con su solución orientativa. Adáptalo cada curso.

| Parte | Duración | Peso en la prueba | Criterios |
|---|---|---|---|
| Teórica (test + preguntas cortas) | 45 min | 35 % | RA1 a, b, c · RA2 a–e |
| Panel SCRUM (A4.3) | 30 min | 15 % | RA1 d · RA2 |
| Práctica (sin IA, con documentación oficial) | 80 min | 50 % | RA2 a, b, c, d, e |

## Parte teórica

### Test (1 punto cada una, −0,25 por error)

1. En una app hecha con Ionic + Capacitor, el código de la interfaz se ejecuta en:
    - a) una máquina virtual de Java
    - b) **un WebView** ✔
    - c) componentes nativos generados en compilación
    - d) un servidor remoto
2. ¿Qué tecnología NO es híbrida web?
    - a) Ionic + Capacitor · b) Cordova · c) **Flutter** ✔ · d) Ionic + React
3. En un componente, `total = computed(() => this.precio() * this.unidades())`:
    - a) se recalcula en cada repintado
    - b) **se recalcula solo cuando cambian `precio` o `unidades`** ✔
    - c) hay que llamar a `total.set()` para actualizarlo
    - d) solo funciona con Zone.js
4. ¿Qué falta en `@for (p of productos()) { ... }`?
    - a) `let` · b) `$index` · c) **`track`** ✔ · d) `@empty`
5. Si una página de Ionic tiene que recargar datos **cada vez** que el usuario vuelve a ella, usamos:
    - a) `ngOnInit` · b) `constructor` · c) **`ionViewWillEnter`** ✔ · d) `ngAfterViewInit`
6. Para guardar los ajustes del usuario en el móvil de forma persistente es más adecuado:
    - a) una variable en un servicio · b) **`@capacitor/preferences`** ✔ · c) `sessionStorage` · d) Firestore
7. La API responde bien en Postman, pero en `ionic serve` aparece *blocked by CORS policy*. La solución está en:
    - a) la app · b) **el servidor** ✔ · c) el móvil · d) Capacitor
8. Para que un hijo avise a su padre de que el usuario ha pulsado un botón se usa:
    - a) `input()` · b) **`output()`** ✔ · c) `signal()` · d) `inject()`

### Preguntas cortas (2 puntos cada una)

1. Una ONG quiere una app para voluntarios con listado de actividades, inscripción y avisos, para Android e iOS, con un solo desarrollador web y sin presupuesto. **Propón una tecnología y justifícala** con tres criterios; indica también una alternativa y por qué la descartas. *(RA1 b, c)*
2. Explica qué ocurre, capa a capa, cuando el usuario pulsa «Hacer foto» en una app Ionic + Capacitor, desde el `(click)` hasta que la foto aparece en pantalla. *(RA1 a · RA2 b)*
3. Tu app usa el GPS en tiempo real. Indica **qué harías y en qué hook o evento** para no gastar batería cuando el usuario cambia de página o minimiza la app. *(RA2 c)*

## Parte práctica (10 puntos)

Crea el proyecto `Prueba_NombreApellidos` (standalone). Tienes la documentación oficial de Angular, Ionic y Capacitor. **No se permite IA.**

**Enunciado: «Avisos del IES»**

1. Página **Lista** con los avisos obtenidos con `GET` de `https://jsonplaceholder.typicode.com/posts?_limit=10`. Muestra título y un extracto, con estado de carga y mensaje de error. *(2 p · RA2 a, d)*
2. Un **buscador** que filtra la lista con un `computed`. *(1 p · RA2 a)*
3. Al pulsar un aviso se navega a **`/detalle/:id`**, que muestra el aviso completo y tiene botón atrás. *(2 p · RA2 e)*
4. En el detalle, un botón **Marcar como leído** que guarda el id en **Preferences**. En la lista, los avisos leídos se muestran con un icono. La información se mantiene al cerrar y abrir la app (compruébalo recargando el navegador). *(2,5 p · RA2 d)*
5. Un componente hijo **`contador-leidos`** en el pie de la lista que recibe con `input()` el número de avisos leídos. *(1 p · RA2 a)*
6. En la lista, un botón **Mi ubicación** que muestra latitud y longitud con `@capacitor/geolocation` (vale en el navegador). *(1,5 p · RA2 b)*

Entrega: carpeta `src/` comprimida en Moodle al terminar.

### Criterios de corrección de la práctica

| Nivel | Puntuación del apartado |
|---|---|
| Funciona con sintaxis moderna y código organizado en servicios | 100 % |
| Funciona con fallos menores o sintaxis antigua | 70 % |
| Funciona parcialmente | 40 % |
| No funciona o no se ha hecho | 0 % |
