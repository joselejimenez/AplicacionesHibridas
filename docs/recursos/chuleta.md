# Chuleta de Angular moderno

## Componente

```ts
import { Component, signal, computed, input, output, inject } from '@angular/core';
import { IonButton } from '@ionic/angular';

@Component({
  selector: 'app-ejemplo',
  templateUrl: 'ejemplo.component.html',
  imports: [IonButton],                    // todo lo que uses en la plantilla
})
export class EjemploComponent {
  titulo = input.required<string>();       // dato del padre
  pulsado = output<number>();              // aviso al padre
  private datos = inject(DatosService);    // servicio
  contador = signal(0);                    // estado
  doble = computed(() => this.contador() * 2);
}
```

## Signals

| Quiero | Código |
|---|---|
| Crear | `x = signal(valorInicial)` |
| Leer | `x()` |
| Cambiar | `x.set(nuevo)` |
| Cambiar con el anterior | `x.update(v => v + 1)` |
| Añadir a una lista | `lista.update(l => [...l, nuevo])` |
| Quitar de una lista | `lista.update(l => l.filter(e => e.id !== id))` |
| Modificar un elemento | `lista.update(l => l.map(e => e.id === id ? { ...e, ...cambios } : e))` |
| Derivado | `total = computed(() => ...)` |
| Efecto secundario | `effect(() => console.log(x()))` |
| Solo lectura (en servicios) | `readonly publico = this.privado.asReadonly()` |
| De Observable a signal | `datos = toSignal(obs$, { initialValue: [] })` |

## Plantilla

```html
{{ valor() }}                                  <!-- interpolación -->
<img [src]="url()">                            <!-- propiedad -->
<ion-button (click)="guardar()">               <!-- evento -->
<ion-input [(ngModel)]="nombre">               <!-- bidireccional (FormsModule) -->

@if (cond()) { ... } @else if (otra()) { ... } @else { ... }
@for (item of lista(); track item.id) { {{ $index }} } @empty { Vacío }
@switch (tipo()) { @case ('a') { ... } @default { ... } }
@let total = precio() * unidades();
@defer (on viewport) { <app-pesado /> } @placeholder { Cargando… }
```

## Rutas

```ts
{ path: 'detalle/:id', loadComponent: () => import('./detalle/detalle.page').then(m => m.DetallePage) }
```

```html
<ion-item [routerLink]="['/detalle', item.id]">
```

```ts
id = input.required<string>();   // con withComponentInputBinding()
inject(Router).navigate(['/home']);
```

## Servicio

```ts
@Injectable({ providedIn: 'root' })
export class DatosService {
  private http = inject(HttpClient);
  obtener() { return this.http.get<Modelo[]>(`${environment.apiUrl}/items`); }
}
```

## Ciclo de vida

| Hook | Cuándo |
|---|---|
| `ngOnInit` | Al crear el componente (una vez) |
| `ionViewWillEnter` | Cada vez que se va a mostrar la página |
| `ionViewWillLeave` | Cada vez que se va a salir de la página |
| `ngOnDestroy` / `DestroyRef` | Al destruirse |
| `App.addListener('appStateChange')` | La app pasa a primer o segundo plano |

## Comandos

| Quiero | Comando |
|---|---|
| Crear proyecto | `ionic start Nombre blank --type=angular` |
| Arrancar en navegador | `ionic serve` |
| Nueva página | `ionic generate page nombre` |
| Nuevo componente | `ionic generate component components/nombre` |
| Nuevo servicio | `ionic generate service services/nombre` |
| Compilar | `ionic build` |
| Añadir Android | `npx cap add android` |
| Copiar cambios al proyecto nativo | `npx cap sync android` |
| Abrir Android Studio | `npx cap open android` |
| Recarga en vivo en el móvil | `ionic cap run android -l --external` |
| Tests unitarios | `npx ng test` |
| Tests E2E | `npx cypress run` |
