"""
Cloudflare Detection Tool
--------------------------

Autor: Eduardo Chasco  
Fecha: 2025-04-07  

Descripción:
Este script permite identificar si un sitio web está protegido por el CDN Cloudflare.  
Utiliza dos métodos comunes para este análisis:

1. 🔎 **Cabecera HTTP (Header)**  
   Busca menciones a Cloudflare dentro de los encabezados HTTP del sitio, como el campo `Report-To`.

2. 🌐 **Consulta WHOIS (Name Servers)**  
   Extrae los servidores de nombre del dominio usando `whois` y verifica si están asociados a Cloudflare.

Parámetros de entrada:
    -t o --target  : Dominio o URL del sitio a analizar  
    -m o --method  : Método de análisis a utilizar: `header` o `whois`

Requisitos:
    - Python 3.x
    - requests
    - whois
    - re (expresiones regulares)

Instalación:
    pip install whois

Ejemplos de uso:

    python cloudflare_detector.py -t dominio.com -m header  
    python cloudflare_detector.py -t dominio.com -m whois
"""
import argparse
import requests
import whois
import re
from urllib.parse import urlparse

#SOLICITUD DE PARAMETROS
parser = argparse.ArgumentParser(description="Analizador de sitios protegidos con Cloudflare")
parser.add_argument("-t", "--target", help="URL de la página web a analizar")
parser.add_argument("-m", "--method", help="Indica el método a utilizar EJEMPLOS: \
                    -m header = busca en la cabecera \
                    -m whois = busca con módulo whois")
parser = parser.parse_args()

#ANALIZA LA CABECERA DEL SITIO, BUSCANDO CLOUDFLARE EN "Report-To"
def buscarEnCabecera(target):
    # Asegurarse de que la URL tenga el esquema http:// o https://
    if not target.startswith("http://") and not target.startswith("https://"):
        target = "http://" + target  # Si no tiene esquema, agregar "http://"

    try:
        pagina = requests.get(url=target)  # Realiza la solicitud del dominio/sitio y lo almacena en pagina
        header = pagina.headers  # Almacena el contenido de header en header[]
    except requests.exceptions.ConnectionError:  # Si hay un error de conexión
        print(f"Error: No se pudo conectar con el sitio {target}. Asegúrate de que la URL esté correcta.")
        return  # Salir de la función si hay un error de conexión

    reportTo = ""
    while True:
        try:
            reportTo = header["Report-To"]  # Almaceno el contenido de "Report-To" en reportTo para analizarlo.
            patronCDN = re.compile(r'[cloudflareCLOUDFLARE]{10}\.[a-zA-Z]{2,3}')  # Regex para identificar un dominio Cloudflare
            cloudflare = patronCDN.findall(reportTo)  # Almacena las coincidencias en la lista reportTo[]
            print("Dominios Cloudflare encontrados en header:", cloudflare)
            if cloudflare:  # Si a lo menos existe un dominio Cloudflare en los ns, significa que está protegido por el CDN Cloudflare
                print("El sitio", target, "tiene protección de CDN Cloudflare")
            break
        except KeyError:
            print(f"El sitio {target} no tiene un campo 'Report-To' en su cabecera.")
            break
    return



#ANALIZA EL SITIO CON EL MODULO WHOIS, BUSCANDO NS DE CLOUDFLARE
def buscarEnWhois(target):
    dominio = urlparse(target).netloc or target  # Extrae solo el dominio
    respuesta = whois.whois(dominio)
    ns = str(respuesta["name_servers"])
    patronCDN = re.compile(r'[cloudflareCLOUDFLARE]{10}\.[a-zA-Z]{2,3}')
    cloudflare = patronCDN.findall(ns)
    if cloudflare:
        print("Dominios Cloudflare encontrados en Whois:", cloudflare)
        print("El sitio tiene protección de CDN Cloudflare")
    else:
        print("El sitio NO tiene protección de CDN Cloudflare")            


#LANZADOR
def main():
    if parser.target and parser.method=="header": #Si existe el dominio y se elije el metodo header, usa la funciona buscar en cabecera
        buscarEnCabecera(parser.target)

    elif parser.target and parser.method=="whois": #Si existe el dominio y se elije el metodo whois, usa la funciona buscar con whois
        buscarEnWhois(parser.target)

    else:
        print("Por favor ingrese una opción valida \n \
              EJEMPLOS:\n \
              -t dominio.com -m header = busca en la cabecera \n \
              -t dominio.com -m whois = busca con módulo whois")
    return 0
    

if __name__ == "__main__":
        main()