# UD2 · Actividades

| Actividad | Entrega | CE |
|---|---|---|
| [A2.1 Componentes Ionic](#a21) | Lun 26 oct | RA2 a |
| [A2.2 Primera app Ionic + Angular](#a22) | Lun 26 oct | RA2 a |
| [A2.3 Tarjeta de presentación con databinding](#a23) | Lun 9 nov | RA2 a |
| [A2.4 Cádiz Market](#a24) | Lun 9 nov | RA2 a |

---

## A2.1 · Componentes Ionic { #a21 }

**Ionic sin framework, desde CDN.**

Partiendo del ejemplo del [apartado 1 de la UD2](index.md#1-ionic-componentes-de-interfaz-movil), añade componentes de Ionic copiando y adaptando el código de la [documentación oficial](https://ionicframework.com/docs/components) (pestaña *JavaScript*).

### Requisitos

1. HTML, CSS y JS en **ficheros separados**.
2. Componentes mínimos:
    - `ion-card`
    - `ion-accordion-group` con al menos tres `ion-accordion`
    - `ion-action-sheet` que se abre con un botón
    - `ion-alert` que se abre con otro botón
    - al menos tres `ion-icon`
    - **dos componentes más a tu elección** (por ejemplo `ion-toast`, `ion-segment`, `ion-range`, `ion-datetime`)
3. Tema: tu ciudad, tu equipo o tu afición. El contenido tiene que ser tuyo, no el texto de ejemplo de la documentación.
4. Conviértela en app con Capacitor y pruébala en el móvil.

### Entrega (Moodle)

Carpeta comprimida con el código y **dos capturas**: web y app en el móvil. Para la captura del móvil puedes usar `scrcpy`.

### Rúbrica (10 puntos)

| Criterio | Puntos |
|---|---|
| Los seis componentes obligatorios funcionan | 5 |
| Dos componentes extra | 1,5 |
| Ficheros separados y contenido propio | 1,5 |
| App funcionando en el móvil | 2 |

---

## A2.2 · Primera app Ionic + Angular { #a22 }

**Crear un proyecto, entender su estructura y llevarlo al móvil.**

### Pasos

1. Crea el proyecto:

    ```bash
    ionic start HuertoApp_NombreApellido blank --type=angular
    ```

2. Levántalo con `ionic serve` y comprueba que se ve la página *Blank*.
3. En `home.page.ts` crea un signal con una lista de al menos **cinco cultivos** del huerto con `id`, `nombre`, `temporada` e `icono`.
4. En `home.page.html`:
    - En la cabecera pon **«Huerto de [tu nombre]»**, tomando el nombre de una propiedad del `.ts`.
    - Muestra los cultivos en una `ion-list` con `@for`, un `ion-icon` y la temporada en un `ion-badge`.
    - Añade una `ion-card` de bienvenida con una imagen de `src/assets/`.
5. Cambia el color principal de la app en `src/theme/variables.scss` o `global.scss`.
6. Llévala al móvil (`ionic build`, `npx cap add android`, `npx cap sync android`, `npx cap open android`).
7. En `capacitor.config.ts` cambia `appName` a **«Huerto [tu nombre]»** y vuelve a sincronizar.

### Preguntas (responde en un `RESPUESTAS.md` en la raíz del proyecto)

1. ¿Para qué sirven `main.ts`, `app.routes.ts` y `capacitor.config.ts`?
2. ¿Qué pasa si quitas `IonList` del array `imports` del componente? ¿Por qué?
3. ¿Qué diferencia hay entre `ionic serve` y `ionic build`?

### Entrega (Moodle)

Carpeta `src/` comprimida, `RESPUESTAS.md` y dos capturas (web y móvil).

### Rúbrica (10 puntos)

| Criterio | Puntos |
|---|---|
| Proyecto standalone creado y funcionando | 1,5 |
| Lista con `@for` y `track`, signal, iconos y badges | 3 |
| Cabecera con nombre por interpolación y tarjeta con imagen | 1,5 |
| Tema de color modificado | 1 |
| App en el móvil con el nombre cambiado | 1,5 |
| Respuestas correctas | 1,5 |

---

## A2.3 · Tarjeta de presentación con databinding { #a23 }

**Los cuatro tipos de databinding y signals.**

Crea el proyecto `Databinding_NombreAlumno` y construye una página «Mi tarjeta» con **todos los textos tomados del `.ts`** (ningún texto escrito directamente en el HTML, salvo etiquetas de formulario).

### Requisitos

1. **Interpolación:** nombre, ciclo, curso, ciudad, dos emojis y una frase sobre ti, desde propiedades o signals.
2. **Property binding:** la foto de perfil con `[src]` y `[alt]`, y el color de la tarjeta con `[color]`.
3. **Event binding:** un botón **«Me gusta»** que incrementa un contador (signal) y otro que lo reinicia.
4. **Two-way binding:** un `ion-input` para cambiar tu frase; la tarjeta se actualiza mientras escribes.
5. **Computed:** un texto que diga «Popular» si el contador supera 10 y «Empezando» si no, con `@if`.
6. Un `ion-toggle` que cambia entre tema claro y oscuro de la tarjeta.

!!! tip "Emojis"
    En VS Code puedes insertarlos con ++win+period++ en Windows o ++ctrl+cmd+space++ en macOS.

### Entrega (Moodle)

`home.page.html`, `home.page.ts` y una captura de la web en el servidor local.

### Rúbrica (10 puntos)

| Criterio | Puntos |
|---|---|
| Interpolación: todos los textos vienen del `.ts` | 2 |
| Property binding (imagen y color) | 1,5 |
| Event binding con signal (`set` / `update`) | 2 |
| Two-way binding con `ngModel` | 1,5 |
| `computed` + `@if` | 2 |
| Toggle de tema | 1 |

---

## A2.4 · Cádiz Market { #a24 }

**Signals, `@if`, `@for`, `@switch` y eventos en una app de inventario.**

Crea el proyecto `CadizMarket_NombreAlumno` y sustituye `home.page.ts` y `home.page.html` por el código de partida.

??? example "Código de partida: home.page.ts"

    ```ts
    import { Component, signal, computed } from '@angular/core';
    import { FormsModule } from '@angular/forms';
    import {
      IonHeader, IonToolbar, IonTitle, IonContent, IonSearchbar, IonList,
      IonItem, IonLabel, IonBadge, IonButton, IonSelect, IonSelectOption,
      IonChip, IonThumbnail,
    } from '@ionic/angular';

    type Tipo = 'fruta' | 'verdura' | 'pescado';

    interface Producto {
      id: number;
      nombre: string;
      tipo: Tipo;
      stock: number;
      imagen: string;
    }

    @Component({
      selector: 'app-home',
      templateUrl: 'home.page.html',
      styleUrls: ['home.page.scss'],
      imports: [FormsModule, IonHeader, IonToolbar, IonTitle, IonContent,
                IonSearchbar, IonList, IonItem, IonLabel, IonBadge, IonButton,
                IonSelect, IonSelectOption, IonChip, IonThumbnail],
    })
    export class HomePage {
      nombreApp = 'Mi mercado';
      filtro = signal('');
      tipoSeleccionado = signal<Tipo>('fruta');

      productos = signal<Producto[]>([
        { id: 1, nombre: 'Naranjas', tipo: 'fruta', stock: 20, imagen: 'https://picsum.photos/seed/naranja/80' },
        { id: 2, nombre: 'Tomates', tipo: 'verdura', stock: 3, imagen: 'https://picsum.photos/seed/tomate/80' },
        { id: 3, nombre: 'Urta', tipo: 'pescado', stock: 0, imagen: 'https://picsum.photos/seed/urta/80' },
      ]);

      filtrados = computed(() =>
        this.productos().filter(p =>
          p.nombre.toLowerCase().includes(this.filtro().toLowerCase()))
      );

      cambiarStock(id: number, cantidad: number) {
        this.productos.update(lista =>
          lista.map(p => p.id === id ? { ...p, stock: Math.max(0, p.stock + cantidad) } : p)
        );
      }

      anadirRapido() {
        const id = Date.now();
        this.productos.update(lista => [
          ...lista,
          { id, nombre: 'Producto nuevo', tipo: this.tipoSeleccionado(), stock: 1,
            imagen: `https://picsum.photos/seed/${id}/80` },
        ]);
      }
    }
    ```

??? example "Código de partida: home.page.html"

    ```html
    <ion-header>
      <ion-toolbar color="primary">
        <ion-title>{{ nombreApp }}</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content>
      <ion-searchbar [(ngModel)]="filtro" placeholder="Filtrar productos"></ion-searchbar>

      <ion-list>
        @for (p of filtrados(); track p.id) {
          <ion-item>
            <ion-thumbnail slot="start"><img [src]="p.imagen" [alt]="p.nombre"></ion-thumbnail>
            <ion-label>
              <h2>{{ p.nombre }}</h2>
              @switch (p.tipo) {
                @case ('fruta') { <ion-chip color="warning">Fruta</ion-chip> }
                @case ('verdura') { <ion-chip color="success">Verdura</ion-chip> }
                @case ('pescado') { <ion-chip color="tertiary">Pescado</ion-chip> }
              }
            </ion-label>
            @if (p.stock > 0) {
              <ion-badge slot="end" [color]="p.stock < 5 ? 'warning' : 'success'">{{ p.stock }}</ion-badge>
            } @else {
              <ion-badge slot="end" color="danger">Agotado</ion-badge>
            }
            <ion-button slot="end" size="small" (click)="cambiarStock(p.id, 1)">+1</ion-button>
            <ion-button slot="end" size="small" color="medium" (click)="cambiarStock(p.id, -1)">-1</ion-button>
          </ion-item>
        } @empty {
          <ion-item>No hay productos que coincidan</ion-item>
        }
      </ion-list>

      <ion-item>
        <ion-select label="Tipo" [(ngModel)]="tipoSeleccionado">
          <ion-select-option value="fruta">Fruta</ion-select-option>
          <ion-select-option value="verdura">Verdura</ion-select-option>
          <ion-select-option value="pescado">Pescado</ion-select-option>
        </ion-select>
      </ion-item>
      <ion-button expand="block" (click)="anadirRapido()">Añadir producto rápido</ion-button>
    </ion-content>
    ```

### Analiza (antes de modificar)

- Escribe en el filtro → la lista se actualiza (**two-way** + `computed`).
- Pulsa +1 / -1 → cambia el stock (**event binding** + `signal.update`).
- Observa el badge: cambia de color y de texto según el stock (**`@if`** + **property binding**).
- Cambia el tipo en el selector y añade un producto → el chip depende del tipo (**`@switch`**).

### Modificaciones que se piden

1. Los botones pasan a **+5 y -5** y el stock cambia en 5 unidades.
2. Cada cambio de stock escribe en la consola (DevTools) `console.log('TuNombre', 'Stock de X: N')`.
3. «Añadir producto rápido» también deja un mensaje en la consola.
4. El nombre de la app es **CÁDIZ MARKET** y el icono de la cabecera es el escudo del Cádiz C.F. (imagen en `src/assets/`).
5. Añade un **contador total** de unidades en stock en la cabecera con `computed`.
6. Añade un **formulario** para escribir el nombre del producto nuevo en lugar de «Producto nuevo».

### Entrega (Moodle)

`home.page.html`, `home.page.ts` y una captura con la consola de DevTools abierta mostrando los mensajes.

### Rúbrica (10 puntos)

| Criterio | Puntos |
|---|---|
| +5 / -5 funcionando sin stock negativo | 2 |
| Mensajes en consola (cambio de stock y alta) | 1,5 |
| Nombre CÁDIZ MARKET y escudo | 1 |
| Contador total con `computed` | 2 |
| Formulario para el nombre del producto | 2 |
| Explicación en comentarios de qué tipo de binding hay en cada parte | 1,5 |
