# Cómo funciona el curso

## Una sesión a la semana

Tenemos clase **los lunes de 15:30 a 18:30** (3 horas). Cada sesión sigue más o menos este esquema:

| Tramo | Duración | Qué hacemos |
|---|---|---|
| Repaso y dudas | 15 min | Revisamos la actividad anterior y los problemas que hayan surgido |
| Explicación | 45–60 min | Teoría de la unidad con ejemplos en directo |
| Práctica guiada | 45 min | Todo el grupo hace el mismo ejemplo paso a paso |
| Actividad | 60 min | Empiezas la actividad evaluable de la semana; lo que no termines, en casa |

Como solo nos vemos un día a la semana, **la actividad de cada lunes se entrega antes del lunes siguiente** salvo que se indique otra cosa.

## Cómo se entrega

- **UD1 y UD2:** carpeta comprimida en Moodle con el código y las capturas que se pidan.
- **Desde la UD3:** repositorio en GitHub creado con tu cuenta del IES. En Moodle subes solo el enlace.
- **UD4 y UD5:** además del repositorio, un vídeo corto (1–5 min) mostrando la app funcionando.

!!! warning "Nombra bien los repositorios"
    Usa el formato `AH_UDx_Ay_NombreApellidos`, por ejemplo `AH_UD3_A2_LuciaGarciaPerez`. Nunca subas la carpeta `node_modules/`.

## El móvil es obligatorio desde la UD1

Las apps híbridas hay que probarlas en un dispositivo real: la cámara, el GPS o los sensores no funcionan igual en un emulador. Necesitas:

- un móvil Android con **opciones de desarrollador** y **depuración USB** activadas, y un cable que transmita datos;
- opcionalmente, [`scrcpy`](https://github.com/Genymobile/scrcpy) para ver la pantalla del móvil en el ordenador y hacer capturas.

Si no tienes móvil Android, avisa el primer día: hay dispositivos en el aula y puedes usar el emulador de Android Studio para lo que no dependa del hardware.

## Uso de IA

Puedes usar asistentes de IA (Copilot, Claude, ChatGPT, Gemini…) y en algunas actividades se pide expresamente. Tres reglas:

1. **Tienes que entender y poder explicar todo el código que entregas.** En la defensa y en la prueba práctica no hay IA.
2. Indica en el `README.md` qué partes has hecho con ayuda de IA y qué *prompts* principales usaste.
3. La IA no sustituye a probar en el móvil: el código generado a menudo olvida permisos, errores de red o el ciclo de vida.

## Relación con otros módulos

- **PMDM:** la API Spring Boot que despliegas en Render la consumes desde tu app híbrida en la UD4.
- **Proyecto (PFC):** el panel SCRUM de la UD4 recoge qué funcionalidades de este módulo usarás en tu proyecto.
- **Desarrollo de Interfaces:** usabilidad, accesibilidad y pruebas se refuerzan mutuamente.
