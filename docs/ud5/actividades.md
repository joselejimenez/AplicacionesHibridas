# UD5 · Actividades

| Actividad | Entrega | CE |
|---|---|---|
| [A5.1 De malas a buenas prácticas con IA](#a51) | Lun 18 ene | RA3 a |
| [A5.2 Proyecto final](#a52) | Dom 14 feb · defensa lun 15 feb | RA3 a, b, c, d, e |

---

## A5.1 · De malas a buenas prácticas con IA { #a51 }

Repositorio: `AH_UD5_A1_NombreApellidos`

Te damos una pequeña red social, **RedSocialMalasPracticas**, que funciona pero está mal hecha a propósito. Tienes que medir sus KPIs, corregirla con ayuda de IA y demostrar la mejora con datos.

### Código de partida

El proyecto completo está en Moodle. Estos son sus dos ficheros principales para que veas el tipo de problemas:

??? example "feed.page.ts (malas prácticas)"

    ```ts
    import { Component } from '@angular/core';
    import { HttpClient } from '@angular/common/http';
    import { NgFor, NgIf } from '@angular/common';
    import { interval } from 'rxjs';
    import { IonContent, IonList, IonItem, IonLabel, IonAvatar, IonHeader, IonToolbar, IonTitle } from '@ionic/angular';

    @Component({
      selector: 'app-feed',
      templateUrl: 'feed.page.html',
      imports: [NgFor, NgIf, IonContent, IonList, IonItem, IonLabel, IonAvatar, IonHeader, IonToolbar, IonTitle],
    })
    export class FeedPage {
      posts: any[] = [];
      usuarios: any[] = [];
      segundos = 0;

      constructor(private http: HttpClient) {
        interval(1000).subscribe(() => this.segundos++);          // nunca se cancela
      }

      ionViewWillEnter() {
        // se piden todos los datos cada vez que se entra en la página
        this.http.get<any[]>('https://jsonplaceholder.typicode.com/posts').subscribe(p => this.posts = p);
        this.http.get<any[]>('https://jsonplaceholder.typicode.com/users').subscribe(u => this.usuarios = u);
        this.http.get<any[]>('https://jsonplaceholder.typicode.com/users').subscribe(u => this.usuarios = u);
      }

      autor(post: any) {
        console.log('calculando autor');                          // se ejecuta en cada repintado
        return this.usuarios.find(u => u.id === post.userId)?.name;
      }

      imagen(id: number) {
        return `https://picsum.photos/seed/${id}/1200/1200`;     // imágenes enormes para un avatar
      }
    }
    ```

??? example "feed.page.html (malas prácticas)"

    ```html
    <ion-header><ion-toolbar><ion-title>Feed ({{ segundos }} s)</ion-title></ion-toolbar></ion-header>
    <ion-content>
      <ion-list>
        <ion-item *ngFor="let post of posts">
          <ion-avatar slot="start"><img [src]="imagen(post.id)"></ion-avatar>
          <ion-label>
            <h2>{{ post.title }}</h2>
            <p *ngIf="autor(post)">{{ autor(post) }}</p>
            <p>{{ post.body }}</p>
          </ion-label>
        </ion-item>
      </ion-list>
    </ion-content>
    ```

    Además, `app.routes.ts` importa todas las páginas directamente (sin `loadComponent`).

### Qué tienes que hacer

1. **Mide** los KPIs de la versión mala: tamaño del bundle inicial, Lighthouse (rendimiento, accesibilidad, buenas prácticas), número de peticiones al entrar en el feed, mensajes «calculando autor» en la consola en 10 s y memoria tras navegar 10 veces entre páginas.
2. Crea **RedSocialBuenasPracticas** aplicando lo visto en la [UD5, apartado 2](index.md#2-optimizacion): lazy loading, signals y `computed`, `@for` con `track`, `inject()`, tipos en lugar de `any`, caché de peticiones, limpieza con `takeUntilDestroyed`, imágenes del tamaño adecuado con `loading="lazy"`, textos alternativos, `@defer` donde tenga sentido.
3. Usa un **asistente de IA** para detectar y corregir problemas. Guarda los *prompts* y revisa críticamente lo que genera.
4. **Mide de nuevo** los mismos KPIs en la versión buena.

### Entrega

Repositorio con las dos versiones y un **informe** (`INFORME.md` o PDF) con:

- tabla de KPIs **antes / después** y la mejora en %;
- cada problema detectado, la práctica que incumplía y cómo lo resolviste;
- qué propuso la IA que **no** aceptaste y por qué.

### Rúbrica (10 puntos)

| Criterio | Puntos |
|---|---|
| Medición correcta de KPIs antes y después | 2,5 |
| Corrección de todos los problemas con sintaxis moderna | 3,5 |
| Mejora demostrada en los KPIs | 2 |
| Uso crítico de la IA documentado | 2 |

---

## A5.2 · Proyecto final { #a52 }

Repositorio: `AH_UD5_ProyectoFinal_NombreApellidos`

Desarrolla una aplicación híbrida **de temática libre** con navegación por tabs, consumo de API, pruebas completas y despliegue en el móvil. Se valoran la originalidad y la estética. Puede ser una parte de tu PFC.

### 1. Requisitos de la aplicación

**Estructura**

- Al menos **5 tabs** en la barra inferior (`ion-tabs`), cada uno con su página.
- Al menos **2 páginas fuera de los tabs** accesibles con navegación interna (por ejemplo *Detalle* y *Ajustes*).
- Todas las rutas con `loadComponent`.

```bash
ionic start ProyectoFinal tabs --type=angular
```

**Datos**

- Consumo de al menos **una API externa real** con `HttpClient`, con modelo de respuesta, modelo interno y mapeo.
- Toda la lógica en **servicios** (carpeta `core/services` o similar), no en las páginas.
- **Estado** con un *store* basado en signals (por ejemplo, favoritos) y **persistencia** con Preferences o Firestore.

**Calidad**

- Gestión de errores **centralizada**: interceptor HTTP + toasts + estados de carga y vacío.
- Sintaxis moderna: standalone, signals, `@if/@for`, `inject()`, `input()/output()`.
- Informe Lighthouse de la versión de producción con puntuación de rendimiento y accesibilidad.

### 2. Pruebas

**Vitest (mínimo 20 tests)**

| Tipo | Mínimo | Ejemplos |
|---|---|---|
| Servicios y *stores* | 8 | Construye bien la URL, mapea la respuesta, añade / quita / evita duplicados, persiste |
| Componentes y páginas | 6 | Renderiza la lista, al pulsar buscar llama al servicio, el botón borrar elimina |
| Integración con HTTP simulado (`HttpTestingController`) | 4 | Respuesta correcta, error 500, lista vacía, reintento |
| Navegación | 2 | «Ver detalle» navega a `/detalle/:id`; el detalle muestra el elemento del parámetro |

**Cypress (mínimo 3 tests E2E deterministas)**

- Con `cy.intercept()` y *fixtures*: **no** pueden depender de internet ni de la API real.
- Flujos completos, por ejemplo: buscar → ver resultados → abrir detalle; añadir a favoritos → comprobar en el tab Favoritos; cambiar un ajuste → comprobar que se aplica.

### 3. Despliegue

- App instalada y funcionando en un **móvil real**.
- **AAB o APK firmado** generado con Android Studio, con icono y *splash* propios y `versionName` 1.0.0.
- El keystore **no** se sube al repositorio.

### 4. Documentación

`README.md` completo con la estructura de la [UD5, apartado 6](index.md#6-documentacion): instalación, arquitectura, pruebas (con captura de los resultados), despliegue, problemas y soluciones, y uso de IA.

### 5. Entregables

- Repositorio GitHub con `src/`, `cypress/`, `package.json` y la configuración de tests (sin `node_modules/`).
- El APK firmado como *release* de GitHub o en Moodle.
- **Vídeo de 3 a 6 minutos** que muestre:
    1. la app en el PC: tabs, navegación y carga de datos de la API;
    2. `npx ng test` y sus resultados;
    3. `npx cypress run` y sus resultados;
    4. la app en el móvil real (grabado con cámara o `scrcpy`), recorriendo al menos un flujo principal.

### 6. Defensa (15 de febrero, 10 minutos)

Presentas la app, explicas una decisión de arquitectura y una de pruebas, y el profesor te pide **un cambio pequeño en directo** (por ejemplo, añadir un campo o un test).

### Rúbrica (10 puntos)

| Criterio | CE RA3 | Puntos |
|---|---|---|
| Estructura tabs / páginas / rutas lazy | a | 0,75 |
| API + servicios + estado y persistencia | a | 1,25 |
| Informe Lighthouse y optimizaciones aplicadas | a | 0,5 |
| Vitest: ≥ 20 tests con la distribución pedida | b | 2 |
| Cypress: ≥ 3 tests E2E deterministas | b | 1,25 |
| Todos los tests pasan (vídeo) | b | 0,75 |
| Gestión de errores centralizada | c | 1 |
| App en móvil real + AAB/APK firmado con icono y versión | d | 1 |
| README técnico completo | e | 0,75 |
| Estética, originalidad y UX | — | 0,25 |
| Defensa y cambio en directo | todos | 0,5 |

!!! warning "La defensa es obligatoria"
    Si no puedes explicar tu código o hacer el cambio en directo, la nota del proyecto puede reducirse hasta en un 50 %.
