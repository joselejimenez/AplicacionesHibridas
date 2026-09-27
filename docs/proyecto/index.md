# Proyecto final

!!! abstract "Ficha"
    - **En parejas** · Del **21 de diciembre** al **14 de febrero** · Defensa el **15 de febrero**
    - **RA3 completo** (40 % del RA3) y repaso de todo el RA2
    - Se trabaja en casa y en la última hora de las sesiones 11 a 14

Una app multiplataforma **de verdad**, pensada por vosotros, que junte todo lo aprendido: pantallas, hardware, datos locales y en la nube, pruebas, rendimiento y publicación.

## Requisitos mínimos

| # | Requisito | Tema | CE |
|---|---|---|---|
| 0 | **Documento de diseño** al arrancar: capas, estructura de carpetas y bocetos mobile-first (móvil y escritorio) | T2 | RA1 d, e |
| 1 | Al menos **3 pantallas** con navegación y un **formulario validado**, adaptables a móvil y escritorio | T3 | RA2 a, e |
| 2 | **Estado compartido** con `provider` (u otra solución justificada) | T3 | RA2 c |
| 3 | Al menos **una funcionalidad nativa** (GPS, cámara, sensores o notificaciones) con gestión de permisos | T4 | RA2 b, c |
| 4 | **Persistencia local** (`shared_preferences` o SQLite) | T5 | RA2 d |
| 5 | **Datos remotos**: una API REST o Firebase, con errores de red controlados | T5 | RA2 d |
| 6 | **Análisis de rendimiento** con DevTools documentado (antes y después de al menos una mejora) | T6 | RA3 a |
| 7 | **Tests**: mínimo 10 unitarios, 3 de widget y 1 de integración | T6 | RA3 b |
| 8 | **Gestión centralizada de errores** y registro | T6 | RA3 c |
| 9 | **Android firmado** y **una segunda plataforma publicada** (web o escritorio) | T7 | RA3 d |
| 10 | **README** completo, CHANGELOG, CI en GitHub Actions y documentación del código | T7 | RA3 e |

## Ideas (o proponed la vuestra)

| Idea | Nativo | Remoto |
|---|---|---|
| **Ruta del Carnaval:** agrupaciones del COAC, horarios, ubicación de los tablaos callejeros y «¿dónde está la chirigota?» | GPS | Firestore |
| **Mareas y playas de Cádiz:** estado de las playas, bandera, previsión y avisos | GPS, notificaciones | API de tiempo |
| **Incidencias del barrio:** foto + ubicación de un desperfecto y seguimiento | Cámara, GPS | Firestore |
| **Pádel del instituto:** reservas de pista entre alumnos | Notificaciones | Firestore + Auth |
| **Mi gimnasio:** rutinas, contador de repeticiones con el acelerómetro | Sensores | API propia (Spring Boot de PMDM) |
| **Recetario gaditano:** recetas con foto, lista de la compra y modo cocina | Cámara | API propia |
| **Continuación del proyecto intermodular** | Según el caso | Según el caso |

!!! tip "Si ya tenéis un proyecto en otro módulo"
    Podéis hacer la **app cliente** del backend que estéis desarrollando en otro módulo (por ejemplo, la API Spring Boot de PMDM o el proyecto intermodular). Hablad con los profesores implicados.

## Hitos

| Fecha | Hito | Qué se entrega | Se revisa en clase |
|---|---|---|---|
| **21 dic** | Arranque | Equipo, idea, 10 historias de usuario, panel en **GitHub Projects** y documento de diseño (requisito 0) | Sí, al final de la 1ª parcial |
| **11 ene** | Prototipo | Pantallas navegables con datos de prueba | Sí, 20 min |
| **25 ene** | Funcional | Funcionalidades completas, tests y análisis de rendimiento | Sí, 20 min |
| **1 feb** | Producción | Builds firmados, web publicada, CI | Sí, 20 min |
| **14 feb** | Entrega final | Repositorio, release `v1.0.0`, README, memoria breve | — |
| **15 feb** | Defensa | Presentación y preguntas | — |

!!! warning "El panel SCRUM cuenta"
    El panel de GitHub Projects debe reflejar el trabajo real: tareas asignadas a cada miembro, movidas de columna y enlazadas a *commits* o *issues*. Si un miembro no tiene *commits*, no tiene nota de proyecto.

## Defensa (15 de febrero)

- **10 minutos** por pareja: demostración en **dos plataformas** en directo (una de ellas un móvil real), arquitectura y decisiones técnicas, lo que mejorarías.
- **5 minutos** de preguntas **individuales** sobre el código. Cada miembro debe poder explicar cualquier parte.

## Rúbrica

| Criterio | CE | Peso | Excelente | Adecuado | Insuficiente |
|---|---|---|---|---|---|
| Diseño y funcionalidad (requisitos 0-5) | RA1 d, e · RA2 | 20 % | Todos los requisitos, integrados con sentido | Todos pero alguno forzado o incompleto | Faltan requisitos |
| Rendimiento | RA3 a | 10 % | Análisis con medidas y mejora demostrada | Análisis sin medidas antes/después | Sin análisis |
| Pruebas | RA3 b | 15 % | Supera los mínimos, casos límite, CI en verde | Cumple los mínimos | Por debajo de los mínimos |
| Errores y registro | RA3 c | 10 % | Centralizados, mensajes útiles al usuario | Parcial | Sin gestión |
| Producción multiplataforma | RA3 d | 15 % | Android firmado + otra plataforma publicada | Solo Android firmado | Sin builds de producción |
| Documentación y distribución | RA3 e | 10 % | README, CHANGELOG, docs de código, release | Incompletos | Sin documentación |
| Trabajo en equipo (panel y *commits*) | — | 5 % | Reparto equilibrado y visible | Desequilibrado | Sin evidencias |
| Defensa | — | 15 % | Explica con soltura cualquier parte del código | Explica su parte | No sabe explicar su código |

---

## Actividad de validación en la FFEOE { #actividad-ffeoe }

!!! abstract "Ficha"
    - **Individual** · 30 % del RA3 · Del **16 de febrero al 14 de mayo**
    - Pensada para hacerse en **cualquier empresa**, trabaje o no con Flutter

1. **Análisis del stack de la empresa** (1-2 páginas). Con el vocabulario del Tema 2: ¿qué tecnología usan para móvil o web?, ¿nativa, híbrida, multiplataforma?, ¿por qué crees que la eligieron?, ¿qué ventajas e inconvenientes le ves?, ¿cómo prueban y despliegan?
2. **Mantenimiento de tu proyecto final.** Publica una **versión 1.1.0** con: una mejora funcional, sus tests, `flutter pub upgrade` de las dependencias (resolviendo lo que se rompa), CHANGELOG actualizado y nueva release.
3. **Videollamada de 15 minutos** con el profesor antes del 14 de mayo: presentas el análisis y demuestras la versión 1.1.0.

| Criterio | Peso |
|---|---|
| Análisis del stack con criterio técnico | 35 % |
| Versión 1.1.0: mejora, tests y dependencias actualizadas | 45 % |
| Videollamada | 20 % |
