"""
Web Technology Analyzer
------------------------------

Autor: Eduardo Chasco
Fecha: 2025-04-07

Este script analiza las tecnologías utilizadas en un sitio web utilizando la librería Wappalyzer.

Requisitos:
    - python-Wappalyzer
    - setuptools

Instalación:
    pip install python-Wappalyzer setuptools

Uso:
    python app_wappalyzer.py -u https://ejemplo.com

"""

import argparse
from Wappalyzer import WebPage, Wappalyzer

def main():
    # Argument parser
    parser = argparse.ArgumentParser(description="Analiza tecnologías web con Wappalyzer")
    parser.add_argument("-u", "--url", required=True, help="URL del sitio web a analizar (incluye https://)")
    args = parser.parse_args()

    wap = Wappalyzer.latest()
    try:
        web = WebPage.new_from_url(args.url)
        tecs = wap.analyze(web)
        for t in tecs:
            print("🔍 Tecnología detectada:", t)
    except Exception as e:
        print("⚠️ Ocurrió un error:", e)

if __name__ == "__main__":
    main()