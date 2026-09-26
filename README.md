# Desarrollo de Aplicaciones Híbridas · 2º DAM · 2026-2027

Sitio del módulo hecho con MkDocs + Material.

## Verlo en tu ordenador

Ejecuta los comandos de uno en uno, dentro de esta carpeta.

Crear el entorno virtual (solo la primera vez):

    python3 -m venv .venv

Activarlo (cada vez que abras la terminal):

    source .venv/bin/activate

Instalar MkDocs Material (solo la primera vez):

    python3 -m pip install -r requirements.txt

Arrancar el servidor y abrir http://127.0.0.1:8000:

    mkdocs serve

## Generar la web estática

    mkdocs build

Se crea la carpeta `site/`, que puedes subir a GitHub Pages, Moodle o cualquier hosting.

## Ocultar la guía docente al alumnado

En `mkdocs.yml`, borra el bloque `- Docente:` del apartado `nav` antes de ejecutar `mkdocs build`.

## Materiales docentes

La carpeta `materiales-docente/` no forma parte del sitio web. Contiene los materiales de clase que no debe ver el alumnado (cuestionarios, soluciones, demos). El guion de cada sesión está en el sitio, en *Docente*.
