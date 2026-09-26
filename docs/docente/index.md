# Guía docente

Esta sección es para el profesorado. Puedes ocultarla antes de publicar el sitio al alumnado quitando el bloque `Docente` del `nav` en `mkdocs.yml`.

## El curso en una página

- **Qué:** módulo de libre configuración de 2º DAM vinculado a PMDM. 3 RA, 5 UD, 15 lunes de 3 h (45 h) entre el 28 sep y el 15 feb.
- **Stack:** TypeScript + Angular moderno (standalone, signals, `@if/@for`) + Ionic 9 + Capacitor 8 + Firebase + Vitest + Cypress.
- **Metodología:** cada lunes, explicación (≈ 1 h) + práctica guiada (≈ 45 min) + actividad evaluable que se termina en casa.
- **Evaluación:** RA1 20 % · RA2 40 % · RA3 40 %. Hay que aprobar cada RA. 1ª parcial en diciembre (RA1 + RA2); RA3 con el proyecto final y la validación en la FFEOE.

## Cómo está construido el material

Parte de las **14 actividades del curso 2025-26** y de los cinco temas en PDF. Se ha:

1. reordenado en las **5 UD** de la programación;
2. actualizado a la sintaxis y herramientas de Angular en 2026 ([qué cambia](cambios-2026.md));
3. completado con **tres actividades nuevas** para cubrir criterios que no tenían evidencia: A1.3 (RA1 b, c, d), A4.2 (RA2 c, d) y el empaquetado y documentación de A5.2 (RA3 d, e);
4. dotado de rúbricas con puntos ligadas a los CE.

## Qué preparar antes de cada unidad

| Antes de | Prepara |
|---|---|
| **28 sep** | Cuestionario de evaluación inicial en Moodle. Comprobar que los PC del aula tienen Node LTS, Android Studio y el Ionic CLI. 3–4 móviles Android de préstamo con depuración USB |
| **19 oct** | ✔ Comprobado el 25 sep: `ionic start` genera Angular 22.1.7 + Ionic 9 + Capacitor 8.5.2 + Vitest 4. Que el alumnado use Node 24 e Ionic CLI 7.2 |
| **9 nov** | Plantilla de repositorio en GitHub Classroom (opcional) con la convención de nombres |
| **23 nov** | Comprobar qué móviles del aula tienen sensor de luz (para A3.4) |
| **30 nov** | Confirmar con el profesor de PMDM que la API de Render estará desplegada |
| **14 dic** | Proyecto Firebase de ejemplo y reglas; comprobar que la red del centro permite Firebase |
| **21 dic** | [Prueba de diciembre](prueba-diciembre.md) y post-its para el panel SCRUM |
| **11 ene** | Montar el proyecto **RedSocialMalasPracticas** con los ficheros de A5.1 y subirlo a Moodle |
| **1 feb** | Enviar a los tutores laborales la [guía FFEOE](ffeoe.md) |

## Decisiones y pendientes

- [x] El **7 de diciembre** es festivo.
- [x] Reparto del RA3: 70 % en clase (A5.1 + A5.2) y 30 % actividad de validación en la FFEOE ([guía FFEOE](ffeoe.md)).
- [x] Versiones del curso: **Node 24 · Ionic CLI 7.2 · Angular 22.1 · Ionic 9 · Capacitor 8.5 · Vitest 4**.
- [ ] Revisar el número de sesiones: la programación suma 60 y el calendario real da 45 horas.
- [ ] Unificar el nombre de las unidades en la programación si se cambia algo.
