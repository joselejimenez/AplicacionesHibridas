# UD2 · Tecnologías y entornos: Angular + Ionic

**RA2** · Sesiones 3 y 4 (19 y 26 oct) · 6 horas

!!! abstract "Al terminar esta unidad sabrás"
    - Usar los componentes de Ionic para construir interfaces con aspecto de app móvil.
    - Crear un proyecto Ionic + Angular y entender cada carpeta.
    - Crear componentes *standalone* y mostrar datos con *databinding*.
    - Manejar el estado con **signals** y la plantilla con **`@if`**, **`@for`** y **`@switch`**.

## 1. Ionic: componentes de interfaz móvil

Ionic es una biblioteca de **componentes web** (`<ion-button>`, `<ion-list>`, `<ion-card>`…) que se ven como una app nativa: estilo Material en Android y estilo iOS en iPhone, de forma automática.

Se puede usar incluso sin framework, cargándolo desde un CDN. Es la forma más rápida de probarlo:

```html title="index.html"
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ionic sin framework</title>
  <script type="module" src="https://cdn.jsdelivr.net/npm/@ionic/core/dist/ionic/ionic.esm.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@ionic/core/css/ionic.bundle.css">
</head>
<body>
  <ion-app>
    <ion-header>
      <ion-toolbar color="primary">
        <ion-title>Hola Ionic</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content class="ion-padding">
      <ion-card>
        <ion-card-header>
          <ion-card-title>Cádiz</ion-card-title>
          <ion-card-subtitle>La tacita de plata</ion-card-subtitle>
        </ion-card-header>
        <ion-card-content>Una tarjeta de Ionic.</ion-card-content>
      </ion-card>
      <ion-button expand="block" id="btn-alerta">Mostrar alerta</ion-button>
      <ion-alert trigger="btn-alerta" header="¡Hola!" message="Esto es una alerta de Ionic"></ion-alert>
    </ion-content>
  </ion-app>
  <script>
    document.querySelector('ion-alert').buttons = ['Aceptar'];
  </script>
</body>
</html>
```

### Componentes que más usarás

| Necesidad | Componentes |
|---|---|
| Estructura de página | `ion-app`, `ion-header`, `ion-toolbar`, `ion-title`, `ion-content`, `ion-footer` |
| Listas | `ion-list`, `ion-item`, `ion-label`, `ion-avatar`, `ion-thumbnail` |
| Tarjetas | `ion-card` y sus partes |
| Botones e iconos | `ion-button`, `ion-fab`, `ion-icon` ([catálogo de iconos](https://ionic.io/ionicons)) |
| Formularios | `ion-input`, `ion-textarea`, `ion-select`, `ion-toggle`, `ion-checkbox`, `ion-datetime` |
| Avisos | `ion-alert`, `ion-toast`, `ion-action-sheet`, `ion-loading`, `ion-modal` |
| Navegación | `ion-tabs`, `ion-menu`, `ion-back-button` |
| Otros | `ion-accordion-group`, `ion-searchbar`, `ion-refresher`, `ion-infinite-scroll`, `ion-badge`, `ion-chip` |

Cada componente tiene ejemplos listos para copiar en la [documentación de Ionic](https://ionicframework.com/docs/components).

## 2. Angular: el framework

Angular organiza la app en **componentes** (piezas de pantalla), **servicios** (lógica y datos compartidos) y **rutas** (qué componente se ve en cada URL). Está escrito en **TypeScript**, JavaScript con tipos.

### Angular en 2026: lo que tienes que saber

| Hoy se hace así | En lugar de (tutoriales antiguos) |
|---|---|
| Componentes **standalone**, sin `NgModule` | `app.module.ts` con `declarations` |
| Estado con **signals**: `signal()`, `computed()` | Propiedades normales + Zone.js |
| **`@if`**, **`@for`**, **`@switch`** en la plantilla | `*ngIf`, `*ngFor`, `[ngSwitch]` |
| `inject(Servicio)` | Inyección en el constructor |
| `input()` y `output()` | `@Input()` y `@Output()` |
| Tests con **Vitest** | Karma + Jasmine |

!!! warning "Cuidado con la IA y los tutoriales viejos"
    Muchos tutoriales y respuestas de IA siguen generando `NgModule`, `*ngIf` o `@Input()`. Funcionan, pero no es la forma actual. En este curso **se pide la sintaxis moderna**.

## 3. Crear un proyecto Ionic + Angular

```bash
ionic start MiApp blank --type=angular
```

Si pregunta, elige **Standalone**. Después:

```bash
cd MiApp
```

```bash
ionic serve
```

`ionic serve` abre la app en `http://localhost:8100` y la recarga cada vez que guardas un fichero.

!!! tip "Ver la app como en un móvil"
    En Chrome pulsa ++f12++ y activa la barra de dispositivos (icono de móvil) para simular un teléfono.

### Estructura del proyecto

```text
MiApp/
├── src/
│   ├── app/
│   │   ├── home/                 ← una página
│   │   │   ├── home.page.ts      ← lógica (TypeScript)
│   │   │   ├── home.page.html    ← plantilla
│   │   │   └── home.page.scss    ← estilos de esta página
│   │   ├── app.component.ts      ← componente raíz (contiene <ion-router-outlet>)
│   │   └── app.routes.ts         ← rutas de la app
│   ├── assets/                   ← imágenes y recursos
│   ├── theme/variables.scss      ← colores de Ionic
│   ├── global.scss               ← estilos globales
│   ├── index.html
│   └── main.ts                   ← arranque: bootstrapApplication(...)
├── capacitor.config.ts           ← nombre e id de la app para Capacitor
├── angular.json                  ← configuración de compilación
├── ionic.config.json
└── package.json                  ← dependencias y scripts
```

`main.ts` arranca la app y registra los *providers* globales (Ionic, router, más adelante HttpClient y Firebase):

```ts title="src/main.ts"
import { bootstrapApplication } from '@angular/platform-browser';
import { RouteReuseStrategy, provideRouter, withPreloading, PreloadAllModules } from '@angular/router';
import { IonicRouteStrategy, provideIonicAngular } from '@ionic/angular';
import { routes } from './app/app.routes';
import { AppComponent } from './app/app.component';

bootstrapApplication(AppComponent, {
  providers: [
    { provide: RouteReuseStrategy, useClass: IonicRouteStrategy },
    provideIonicAngular(),
    provideRouter(routes, withPreloading(PreloadAllModules)),
  ],
});
```

## 4. Anatomía de un componente

```ts title="src/app/home/home.page.ts"
import { Component } from '@angular/core';
import { IonHeader, IonToolbar, IonTitle, IonContent, IonButton } from '@ionic/angular';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
  imports: [IonHeader, IonToolbar, IonTitle, IonContent, IonButton],
})
export class HomePage {
  titulo = 'Huerto IES Rafael Alberti';
}
```

- `selector`: la etiqueta HTML del componente.
- `templateUrl` y `styleUrls`: su plantilla y sus estilos.
- `imports`: **cada componente de Ionic que uses en la plantilla hay que importarlo aquí** desde `@ionic/angular`.

!!! warning "Ionic 9 (agosto de 2026) cambió la ruta de importación"
    En Ionic 9 los componentes standalone se importan de **`@ionic/angular`**. En Ionic 8 y en muchos tutoriales y respuestas de IA verás `@ionic/angular/standalone`: es la forma antigua. Además, `ion-img` ya no existe: usa `<img loading="lazy">`. Si se te olvida, el componente no se ve y la consola muestra un error.

Los iconos se registran con `addIcons`:

```ts
import { addIcons } from 'ionicons';
import { leaf, water } from 'ionicons/icons';

export class HomePage {
  constructor() {
    addIcons({ leaf, water });
  }
}
```

```html
<ion-icon name="leaf"></ion-icon>
```

## 5. Databinding: conectar lógica y vista

| Tipo | Sintaxis | Dirección | Ejemplo |
|---|---|---|---|
| Interpolación | `{{ valor }}` | TS → vista | `<h1>{{ titulo }}</h1>` |
| Propiedad | `[propiedad]="valor"` | TS → vista | `<ion-button [disabled]="cargando()">` |
| Evento | `(evento)="metodo()"` | Vista → TS | `<ion-button (click)="guardar()">` |
| Bidireccional | `[(ngModel)]="valor"` | TS ↔ vista | `<ion-input [(ngModel)]="nombre">` |

Para `[(ngModel)]` hay que importar `FormsModule` en el componente.

## 6. Signals: el estado reactivo

Un **signal** es una caja que guarda un valor y **avisa a la vista cuando cambia**. Angular solo vuelve a pintar lo que depende de ese valor.

```ts title="contador.page.ts"
import { Component, signal, computed } from '@angular/core';
import { IonContent, IonButton } from '@ionic/angular';

@Component({
  selector: 'app-contador',
  template: `
    <ion-content class="ion-padding">
      <h2>Clics: {{ clics() }}</h2>
      <p>El doble es {{ doble() }}</p>
      <ion-button (click)="sumar()">+1</ion-button>
      <ion-button color="medium" (click)="reiniciar()">Reiniciar</ion-button>
    </ion-content>
  `,
  imports: [IonContent, IonButton],
})
export class ContadorPage {
  clics = signal(0);                          // valor inicial
  doble = computed(() => this.clics() * 2);   // se recalcula solo

  sumar() {
    this.clics.update(valor => valor + 1);    // a partir del valor actual
  }

  reiniciar() {
    this.clics.set(0);                        // valor nuevo
  }
}
```

| Operación | Código |
|---|---|
| Crear | `nombre = signal('Ana')` |
| Leer (en TS y en la plantilla) | `nombre()` — **con paréntesis** |
| Cambiar | `nombre.set('Luis')` |
| Cambiar a partir del valor anterior | `contador.update(n => n + 1)` |
| Valor derivado | `total = computed(() => this.precio() * this.cantidad())` |
| Ejecutar algo cuando cambia | `effect(() => console.log(this.nombre()))` |

Los signals también funcionan con `[(ngModel)]`:

```ts
filtro = signal('');
```

```html
<ion-searchbar [(ngModel)]="filtro"></ion-searchbar>
```

## 7. Control flow: `@if`, `@for` y `@switch`

```html
<!-- Condicional -->
@if (stock() > 0) {
  <ion-badge color="success">En stock: {{ stock() }}</ion-badge>
} @else {
  <ion-badge color="danger">Agotado</ion-badge>
}

<!-- Bucle: track es obligatorio y mejora el rendimiento -->
<ion-list>
  @for (producto of productos(); track producto.id) {
    <ion-item>
      <ion-label>{{ $index + 1 }}. {{ producto.nombre }}</ion-label>
    </ion-item>
  } @empty {
    <ion-item>No hay productos</ion-item>
  }
</ion-list>

<!-- Selección múltiple -->
@switch (tipo()) {
  @case ('fruta') { <ion-chip color="warning">Fruta</ion-chip> }
  @case ('verdura') { <ion-chip color="success">Verdura</ion-chip> }
  @default { <ion-chip>Otro</ion-chip> }
}
```

Dentro de `@for` tienes variables como `$index`, `$first`, `$last`, `$even` y `$odd`.

## 8. Ejemplo completo: lista con buscador

```ts title="productos.page.ts"
import { Component, signal, computed } from '@angular/core';
import { FormsModule } from '@angular/forms';
import {
  IonHeader, IonToolbar, IonTitle, IonContent, IonSearchbar,
  IonList, IonItem, IonLabel, IonBadge,
} from '@ionic/angular';

interface Producto {
  id: number;
  nombre: string;
  stock: number;
}

@Component({
  selector: 'app-productos',
  templateUrl: 'productos.page.html',
  imports: [FormsModule, IonHeader, IonToolbar, IonTitle, IonContent,
            IonSearchbar, IonList, IonItem, IonLabel, IonBadge],
})
export class ProductosPage {
  filtro = signal('');
  productos = signal<Producto[]>([
    { id: 1, nombre: 'Tomates', stock: 12 },
    { id: 2, nombre: 'Lechugas', stock: 0 },
    { id: 3, nombre: 'Pimientos', stock: 5 },
  ]);

  filtrados = computed(() =>
    this.productos().filter(p =>
      p.nombre.toLowerCase().includes(this.filtro().toLowerCase())
    )
  );
}
```

```html title="productos.page.html"
<ion-header>
  <ion-toolbar color="primary">
    <ion-title>Productos</ion-title>
  </ion-toolbar>
</ion-header>

<ion-content>
  <ion-searchbar [(ngModel)]="filtro" placeholder="Buscar"></ion-searchbar>
  <ion-list>
    @for (p of filtrados(); track p.id) {
      <ion-item>
        <ion-label>{{ p.nombre }}</ion-label>
        <ion-badge slot="end" [color]="p.stock > 0 ? 'success' : 'danger'">{{ p.stock }}</ion-badge>
      </ion-item>
    } @empty {
      <ion-item>Sin resultados para «{{ filtro() }}»</ion-item>
    }
  </ion-list>
</ion-content>
```

## 9. Generar piezas con la CLI

```bash
ionic generate page productos
```

```bash
ionic generate component components/tarjeta
```

```bash
ionic generate service services/datos
```

## Para saber más

- [Angular: documentación oficial](https://angular.dev) · [tutorial interactivo](https://angular.dev/tutorials)
- [Angular: signals](https://angular.dev/guide/signals)
- [Angular: control flow](https://angular.dev/guide/templates/control-flow)
- [Ionic: componentes](https://ionicframework.com/docs/components)
