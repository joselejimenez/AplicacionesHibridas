"""
Oculta temas de la web publicada sin tocar las páginas.

Uso en mkdocs.yml:

    hooks:
      - hooks/ocultar.py

    extra:
      ocultos:
        - tema3                    # una carpeta entera
        - tema2/practica.md        # o una página suelta

Lo que está en la lista:
  - no se publica (no existe la página ni aparece en el buscador),
  - desaparece del menú,
  - los enlaces que apuntan a ello desde otras páginas se convierten
    en texto con «(próximamente)».

Para verlo todo en local sin publicar nada:

    MOSTRAR_TODO=1 mkdocs serve
"""

import logging
import os
import posixpath
import re

log = logging.getLogger("mkdocs.hooks.ocultar")

_ocultos: list[str] = []
_ENLACE = re.compile(r"(?<!!)\[((?:[^\[\]]|\[[^\[\]]*\])+)\]\(([^()\s]+)\)")
_AVISO = " *(próximamente)*"


def _esta_oculto(ruta: str) -> bool:
    ruta = ruta.lstrip("./")
    for o in _ocultos:
        o = o.strip("/")
        if ruta == o or ruta.startswith(o + "/"):
            return True
    return False


def _filtrar_nav(items):
    resultado = []
    for item in items:
        if isinstance(item, str):
            if not _esta_oculto(item):
                resultado.append(item)
        elif isinstance(item, dict):
            titulo, valor = next(iter(item.items()))
            if isinstance(valor, list):
                hijos = _filtrar_nav(valor)
                if hijos:
                    resultado.append({titulo: hijos})
            elif isinstance(valor, str) and "://" not in valor and _esta_oculto(valor):
                continue
            else:
                resultado.append(item)
    return resultado


def on_config(config, **kwargs):
    global _ocultos
    if os.environ.get("MOSTRAR_TODO"):
        _ocultos = []
        log.info("MOSTRAR_TODO activo: se publica todo")
        return config
    _ocultos = [str(o) for o in (config.get("extra") or {}).get("ocultos") or []]
    if _ocultos and config.get("nav"):
        config["nav"] = _filtrar_nav(config["nav"])
    if _ocultos:
        log.info("Ocultos: %s", ", ".join(_ocultos))
    return config


def on_files(files, config, **kwargs):
    if not _ocultos:
        return files
    for f in list(files):
        if f.src_uri.endswith(".md") and _esta_oculto(f.src_uri):
            files.remove(f)
    return files


def on_page_markdown(markdown, page, config, files, **kwargs):
    if not _ocultos:
        return markdown
    carpeta = posixpath.dirname(page.file.src_uri)

    def sustituir(m):
        texto, destino = m.group(1), m.group(2)
        if "://" in destino or destino.startswith(("#", "mailto:")):
            return m.group(0)
        ruta = destino.split("#", 1)[0]
        if not ruta.endswith(".md"):
            return m.group(0)
        destino_final = posixpath.normpath(posixpath.join(carpeta, ruta))
        if _esta_oculto(destino_final):
            return texto + _AVISO
        return m.group(0)

    return _ENLACE.sub(sustituir, markdown)
