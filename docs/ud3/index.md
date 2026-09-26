# UD3 · Componentes y funcionalidades específicas del móvil

**RA2** · Sesiones 5, 6 y 7 (9, 16 y 23 nov) · 9 horas

!!! abstract "Al terminar esta unidad sabrás"
    - Dividir la app en componentes que se comunican con `input()` y `output()`.
    - Compartir datos y lógica con servicios e `inject()`.
    - Navegar entre páginas con rutas, parámetros, tabs y menú.
    - Crear formularios reactivos con validación.
    - Usar el GPS, la cámara, los sensores y la vibración del móvil con Capacitor.
    - Gestionar el ciclo de vida de páginas y de la app.

## 1. Componentes propios

Un componente es una pieza reutilizable. Se genera con:

```bash
ionic generate component components/tarjeta-alumno
```

### Comunicación padre → hijo con `input()`

```ts title="components/tarjeta-alumno/tarjeta-alumno.component.ts"
import { Component, input } from '@angular/core';
import { IonCard, IonCardHeader, IonCardTitle, IonCardSubtitle } from '@ionic/angular';

@Component({
  selector: 'app-tarjeta-alumno',
  template: `
    <ion-card>
      <ion-card-header>
        <ion-card-title>{{ nombre() }}</ion-card-title>
        <ion-card-subtitle>{{ curso() }}</ion-card-subtitle>
      </ion-card-header>
    </ion-card>
  `,
  imports: [IonCard, IonCardHeader, IonCardTitle, IonCardSubtitle],
})
export class TarjetaAlumnoComponent {
  nombre = input.required<string>();   // obligatorio
  curso = input('2º DAM');              // con valor por defecto
}
```

En el padre (recuerda añadir `TarjetaAlumnoComponent` a sus `imports`):

```html
<app-tarjeta-alumno nombre="Lucía García" />
<app-tarjeta-alumno [nombre]="alumno().nombre" curso="1º DAM" />
```

### Comunicación hijo → padre con `output()`

```ts title="components/valorar/valorar.component.ts"
import { Component, output } from '@angular/core';
import { IonButton } from '@ionic/angular';

@Component({
  selector: 'app-valorar',
  template: `
    @for (estrella of [1, 2, 3, 4, 5]; track estrella) {
      <ion-button fill="clear" (click)="valorado.emit(estrella)">★{{ estrella }}</ion-button>
    }
  `,
  imports: [IonButton],
})
export class ValorarComponent {
  valorado = output<number>();
}
```

```html title="En el padre"
<app-valorar (valorado)="guardarNota($event)" />
<p>Nota: {{ nota() }}</p>
```

!!! tip "`model()`: ida y vuelta"
    Si el hijo tiene que leer **y** modificar un valor del padre, usa `valor = model(0)` en el hijo y `[(valor)]="miSignal"` en el padre.

## 2. Servicios e inyección de dependencias

Un **servicio** guarda lógica y datos que comparten varios componentes: la lista de clientes, la conexión a la API, el acceso al GPS…

```bash
ionic generate service services/datos-alumno
```

```ts title="services/datos-alumno.service.ts"
import { Injectable, signal, computed } from '@angular/core';

export interface Alumno {
  nombre: string;
  curso: string;
  centro: string;
}

@Injectable({ providedIn: 'root' })   // una única instancia para toda la app
export class DatosAlumnoService {
  private alumno = signal<Alumno>({
    nombre: 'Lucía García',
    curso: '2º DAM',
    centro: 'IES Rafael Alberti',
  });

  readonly datos = this.alumno.asReadonly();   // los componentes leen, pero no escriben
  readonly saludo = computed(() => `Hola, ${this.alumno().nombre}`);

  actualizar(cambios: Partial<Alumno>) {
    this.alumno.update(a => ({ ...a, ...cambios }));
  }
}
```

En cualquier componente:

```ts
import { inject } from '@angular/core';
import { DatosAlumnoService } from '../services/datos-alumno.service';

export class HomePage {
  private datosAlumno = inject(DatosAlumnoService);
  alumno = this.datosAlumno.datos;
}
```

```html
<p>{{ alumno().nombre }} · {{ alumno().curso }}</p>
```

Como el servicio es único, **si una página lo modifica, las demás lo ven al instante**. Así se pasan datos entre páginas.

## 3. Navegación

### Rutas

```ts title="src/app/app.routes.ts"
import { Routes } from '@angular/router';

export const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', loadComponent: () => import('./home/home.page').then(m => m.HomePage) },
  { path: 'deportes', loadComponent: () => import('./deportes/deportes.page').then(m => m.DeportesPage) },
  { path: 'detalle/:id', loadComponent: () => import('./detalle/detalle.page').then(m => m.DetallePage) },
  { path: '**', redirectTo: 'home' },
];
```

`loadComponent` carga cada página **solo cuando se visita** (*lazy loading*): la app arranca más rápido.

### Enlaces y navegación por código

```html
<ion-item [routerLink]="['/detalle', item.id]">{{ item.nombre }}</ion-item>
<ion-button routerLink="/deportes">Deportes</ion-button>
```

Importa `RouterLink` de `@angular/router` en el componente. Desde TypeScript:

```ts
private router = inject(Router);

irADetalle(id: number) {
  this.router.navigate(['/detalle', id]);
}
```

### Leer parámetros de la ruta como `input()`

Activa la opción en `main.ts`:

```ts
provideRouter(routes, withPreloading(PreloadAllModules), withComponentInputBinding()),
```

Y en la página de detalle el parámetro `:id` llega solo:

```ts title="detalle.page.ts"
export class DetallePage {
  id = input.required<string>();
  private datos = inject(DatosService);
  item = computed(() => this.datos.buscar(Number(this.id())));
}
```

### Botón «atrás», tabs y menú

- `<ion-back-button defaultHref="/home">` dentro de `ion-buttons slot="start"` añade el botón atrás.
- Para tabs, crea el proyecto con la plantilla `tabs` (`ionic start MiApp tabs --type=angular`) y estudia `tabs.routes.ts`.
- Para un menú lateral, usa la plantilla `sidemenu` o `ion-menu` + `ion-menu-button`.

## 4. Formularios reactivos

Los **formularios reactivos** definen los campos y sus validaciones en TypeScript. Son los más usados en empresa.

```ts title="cliente.page.ts"
import { Component, inject } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { IonContent, IonList, IonItem, IonInput, IonButton, IonNote } from '@ionic/angular';
import { ClientesService } from '../services/clientes.service';

@Component({
  selector: 'app-cliente',
  templateUrl: 'cliente.page.html',
  imports: [ReactiveFormsModule, IonContent, IonList, IonItem, IonInput, IonButton, IonNote],
})
export class ClientePage {
  private fb = inject(FormBuilder);
  private clientes = inject(ClientesService);
  private router = inject(Router);

  formulario = this.fb.nonNullable.group({
    nombre: ['', [Validators.required, Validators.minLength(2)]],
    email: ['', [Validators.required, Validators.email]],
  });

  guardar() {
    if (this.formulario.invalid) {
      this.formulario.markAllAsTouched();
      return;
    }
    this.clientes.guardar(this.formulario.getRawValue());
    this.router.navigate(['/datos-cliente']);
  }
}
```

```html title="cliente.page.html"
<ion-content class="ion-padding">
  <form [formGroup]="formulario" (ngSubmit)="guardar()">
    <ion-list>
      <ion-item>
        <ion-input label="Nombre" labelPlacement="floating" formControlName="nombre"></ion-input>
      </ion-item>
      @if (formulario.controls.nombre.touched && formulario.controls.nombre.invalid) {
        <ion-note color="danger">El nombre es obligatorio (mínimo 2 letras)</ion-note>
      }
      <ion-item>
        <ion-input label="Email" labelPlacement="floating" type="email" formControlName="email"></ion-input>
      </ion-item>
      @if (formulario.controls.email.touched && formulario.controls.email.errors?.['email']) {
        <ion-note color="danger">Formato de email no válido</ion-note>
      }
    </ion-list>
    <ion-button type="submit" expand="block" [disabled]="formulario.invalid">Guardar</ion-button>
  </form>
</ion-content>
```

!!! info "Signal Forms"
    Angular está introduciendo los *Signal Forms*, formularios basados en signals. En 2026 siguen siendo **experimentales**, así que en el curso usamos formularios reactivos, que son los que encontrarás en las empresas.

## 5. Capacitor: acceso al hardware

### Cómo se usa un plugin

1. Instalar el plugin:

    ```bash
    npm install @capacitor/geolocation
    ```

2. Sincronizar el proyecto nativo:

    ```bash
    npx cap sync
    ```

3. Declarar los **permisos** en `android/app/src/main/AndroidManifest.xml` si el plugin lo indica en su documentación.
4. Usarlo desde un **servicio** (nunca directamente en la página).

### Plugins oficiales más usados

| Plugin | Paquete | Para qué |
|---|---|---|
| Geolocalización | `@capacitor/geolocation` | Posición GPS, seguimiento en tiempo real |
| Cámara | `@capacitor/camera` | Hacer fotos o elegirlas de la galería |
| Movimiento | `@capacitor/motion` | Acelerómetro y orientación |
| Vibración | `@capacitor/haptics` | Respuesta háptica |
| Preferencias | `@capacitor/preferences` | Guardar datos clave-valor (UD4) |
| Red | `@capacitor/network` | Saber si hay conexión |
| App | `@capacitor/app` | Ciclo de vida, botón atrás de Android |
| Notificaciones locales | `@capacitor/local-notifications` | Avisos programados |
| Compartir | `@capacitor/share` | Menú nativo de compartir |

Para sensores que no cubren los plugins oficiales (luz ambiente, humedad, linterna) hay plugins de la comunidad: busca en [Capacitor Community](https://github.com/capacitor-community) y [Capawesome](https://capawesome.io) y comprueba que sean compatibles con tu versión de Capacitor.

### GPS: servicio con seguimiento en tiempo real

```ts title="services/gps.service.ts"
import { Injectable, signal } from '@angular/core';
import { Geolocation, Position } from '@capacitor/geolocation';

@Injectable({ providedIn: 'root' })
export class GpsService {
  readonly posicion = signal<Position | null>(null);
  readonly error = signal<string | null>(null);
  private watchId: string | null = null;

  async iniciar() {
    const permisos = await Geolocation.requestPermissions();
    if (permisos.location !== 'granted') {
      this.error.set('Permiso de ubicación denegado');
      return;
    }
    this.watchId = await Geolocation.watchPosition(
      { enableHighAccuracy: true },
      (pos, err) => {
        if (err) { this.error.set(err.message); return; }
        this.posicion.set(pos);   // actualizar un signal refresca la vista
      },
    );
  }

  async detener() {
    if (this.watchId) {
      await Geolocation.clearWatch({ id: this.watchId });
      this.watchId = null;
    }
  }
}
```

```xml title="AndroidManifest.xml (dentro de <manifest>)"
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-feature android:name="android.hardware.location.gps" />
```

!!! warning "Actualiza siempre la vista con signals"
    Los plugins avisan desde fuera de Angular. Si guardas el resultado en una propiedad normal, la pantalla puede no refrescarse. **Guárdalo en un signal**, como en el ejemplo.

### Cámara

```ts
import { Camera, CameraResultType, CameraSource } from '@capacitor/camera';

async hacerFoto() {
  const foto = await Camera.getPhoto({
    quality: 80,
    resultType: CameraResultType.Uri,
    source: CameraSource.Camera,
  });
  this.fotoUrl.set(foto.webPath ?? null);
}
```

```html
@if (fotoUrl(); as url) {
  <img [src]="url" alt="Foto tomada">
}
```

### Acelerómetro

```ts
import { Motion } from '@capacitor/motion';
import { PluginListenerHandle } from '@capacitor/core';

private listener?: PluginListenerHandle;
aceleracion = signal({ x: 0, y: 0, z: 0 });

async escuchar() {
  this.listener = await Motion.addListener('accel', evento => {
    const { x, y, z } = evento.accelerationIncludingGravity;
    this.aceleracion.set({ x, y, z });
  });
}

parar() {
  this.listener?.remove();
}
```

### Vibración

```ts
import { Haptics, ImpactStyle } from '@capacitor/haptics';

await Haptics.impact({ style: ImpactStyle.Medium });
```

## 6. Ciclo de vida

Hay **tres** ciclos de vida distintos y conviene no confundirlos.

### Del componente (Angular)

| Momento | Cómo | Uso típico |
|---|---|---|
| Se crea | `constructor` / `ngOnInit()` | Cargar datos iniciales |
| Se destruye | `ngOnDestroy()` o `inject(DestroyRef).onDestroy(...)` | Parar listeners, GPS, temporizadores |

### De la página (Ionic)

Ionic **mantiene en memoria** las páginas por las que navegas (para que el botón atrás sea instantáneo), así que `ngOnInit` no se repite al volver. Para eso están:

| Hook | Cuándo |
|---|---|
| `ionViewWillEnter()` | Justo antes de mostrarse, **cada vez** que entras |
| `ionViewDidEnter()` | Cuando ya se ve |
| `ionViewWillLeave()` | Antes de salir: buen sitio para pausar el GPS o la cámara |
| `ionViewDidLeave()` | Cuando ya no se ve |

### De la app (Capacitor)

```ts
import { App } from '@capacitor/app';

App.addListener('appStateChange', ({ isActive }) => {
  if (isActive) {
    this.gps.iniciar();   // la app vuelve al primer plano
  } else {
    this.gps.detener();   // la app pasa a segundo plano: ahorra batería
  }
});
```

!!! example "Regla práctica"
    Todo lo que consuma batería (GPS, sensores, cámara) **se para** al salir de la página o al pasar la app a segundo plano, y **se reanuda** al volver.

## 7. Depurar en el móvil

1. Instala la app desde Android Studio con el móvil conectado.
2. En Chrome abre `chrome://inspect/#devices`.
3. Pulsa *inspect* en tu app: tienes consola, red y elementos igual que en la web.

Para desarrollar más rápido, recarga en caliente en el móvil:

```bash
ionic cap run android -l --external
```

## Para saber más

- [Angular: componentes e inputs](https://angular.dev/guide/components/inputs) · [outputs](https://angular.dev/guide/components/outputs)
- [Angular: formularios reactivos](https://angular.dev/guide/forms/reactive-forms)
- [Ionic: ciclo de vida](https://ionicframework.com/docs/angular/lifecycle)
- [Capacitor: plugins oficiales](https://capacitorjs.com/docs/apis)
