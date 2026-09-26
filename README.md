# Aplicaciones Híbridas · 2º DAM

Material del módulo propio de centro **Aplicaciones Híbridas** (2º DAM, IES Rafael Alberti, Cádiz), con **Flutter + Dart**.

Web publicada: <https://joselejimenez.github.io/AplicacionesHibridas/>

## Contenido

- `docs/modulo/` — RA, decisión tecnológica, coordinación con PMDM y DI, planificación
- `docs/t0/` — T0 · Programación en Dart
- `docs/t1/` — T1 · Arquitectura de apps multiplataforma (cierra RA1)

## Ver la web en local (macOS)

Ejecuta cada comando por separado, en la carpeta del repositorio.

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
python3 -m pip install -r requirements.txt
```

```bash
mkdocs serve
```

Abre <http://127.0.0.1:8000>.

## Publicación

Cada `push` a `main` lanza el workflow `.github/workflows/deploy.yml`, que compila la web y la publica en la rama `gh-pages`.

La primera vez, en GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `gh-pages` / `(root)`**.
