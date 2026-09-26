# Qué cambia respecto a 2025-26

## En la organización

| 2025-26 | 2026-27 |
|---|---|
| Actividades por temas sueltos | Mismas actividades ordenadas en las 5 UD de la programación y ligadas a CE |
| Sin evidencia para RA1 b, c, d | Nueva **A1.3 Ficha de análisis y diseño** |
| Persistencia solo en la lista del PFC | Nueva **A4.2 Mis lugares** (Preferences + Firestore + ciclo de vida) |
| Proyecto final sin firma ni documentación | A5.2 exige **AAB/APK firmado** y **README técnico** (RA3 d, e) |
| RA3 evaluado en clase aunque la programación lo asigna a la FFEOE | Proyecto en clase + **actividad de validación** en la FFEOE |
| Actividades dependientes de ficheros de Moodle | Código de partida incluido en las páginas (A2.4, A5.1) |

## En la tecnología

| Antes | Ahora | Dónde |
|---|---|---|
| Ionic 8: `import { ... } from '@ionic/angular/standalone'` | **Ionic 9**: `import { ... } from '@ionic/angular'`; desaparece `ion-img` | Todo el curso |
| `*ngIf`, `*ngFor`, `[ngSwitch]` | `@if`, `@for (… ; track …)`, `@switch` | UD2 en adelante |
| Propiedades + Zone.js | **Signals**: `signal`, `computed`, `effect` (Angular sin Zone.js por defecto) | UD2 en adelante |
| Inyección en el constructor | `inject()` | UD3 |
| `@Input()` / `@Output()` | `input()` / `output()` / `model()` | UD3 |
| `ActivatedRoute` para parámetros | `withComponentInputBinding()` + `input()` | UD3 |
| Formularios template-driven | Formularios **reactivos** (Signal Forms como novedad, aún experimental) | UD3 |
| `HttpClientModule` | `provideHttpClient(withFetch())` + interceptores funcionales | UD4 |
| Estado con `BehaviorSubject` | *Store* con signals | UD5 |
| Karma + Jasmine | **Vitest 4** (la plantilla de Ionic 9 ya lo trae) | UD5 |
| `*ngFor` sin `track` | `track` obligatorio, `@defer`, KPIs con Lighthouse | UD5 |
| Ejecutar en móvil | Además **AAB/APK firmado**, iconos con `@capacitor/assets`, canales de distribución | UD5 |

## Detalles por actividad

| 2025-26 | 2026-27 | Cambios |
|---|---|---|
| Actividad 1 · Tema 1 | A1.1 | Título 2026-2027, mobile-first, `pointerdown` además de `mouseover` |
| Actividad 2 · Tema 1 | A1.2 | Botón extra con `fetch` a la API de chistes |
| — | **A1.3** | Nueva |
| Actividad 1 · Tema 2 | A2.1 | Dos componentes extra en lugar de uno |
| Actividad 2 · Tema 2 | A2.2 | Autocontenida (sin ficheros de Moodle) con signals y `@for` |
| Actividad 3 · Tema 2 | A2.3 | Autocontenida; cubre los cuatro tipos de binding y `computed` |
| Actividad 4 · Tema 2 | A2.4 | Código de partida modernizado; se añaden total con `computed` y formulario |
| Actividad 1 · Tema 3 | A3.1 | Autocontenida; añade detalle con parámetros |
| Actividad 2 · Tema 3 | A3.2 | Formulario reactivo; `input()`/`output()` |
| Actividad 3 · Tema 3 | A3.3 | Añade ciclo de vida e informe crítico de IA |
| Actividad 4 · Tema 3 | A3.4 | Opción B con acelerómetro si el móvil no tiene sensor de luz; linterna como extra |
| Actividad 1 · Tema 4 | A4.1 | Lista filtrada, `environment`, estados de carga y error |
| — | **A4.2** | Nueva |
| Actividad 2 · Tema 4 | A4.3 | Se añade F11 (calidad) y rúbrica |
| Actividad 1 · Tema 5 | A5.1 | Código de partida incluido; KPIs definidos |
| Actividad 2 · Tema 5 | A5.2 | Vitest en lugar de Karma; firma, README, gestión de errores y defensa |

## Versiones del curso

Comprobadas el 25 de septiembre de 2026 creando un proyecto con `ionic start … blank --type=angular`:

| Herramienta | Versión |
|---|---|
| Node.js | 24 LTS |
| Ionic CLI | 7.2 |
| Angular | 22.1 |
| Ionic Framework | 9 |
| Capacitor | 8.5 |
| Vitest | 4.0 |

Mantén estas versiones todo el curso para que nadie cambie de versión a mitad de trimestre.
