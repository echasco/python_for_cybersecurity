"""
DNS Query and Subdomain Finder
-------------------------------

Autor: Eduardo Chasco
Fecha: 2025-04-07  

Descripción:
Este script permite realizar consultas DNS para un dominio específico o llevar a cabo un ataque de fuerza bruta para descubrir subdominios.  
Utiliza la librería `dnspython` para realizar consultas de diferentes tipos de registros DNS, como A, MX, entre otros. Además, permite realizar un escaneo de subdominios utilizando un diccionario de palabras.

Métodos disponibles:
1. 🔎 **Consulta DNS**  
   Realiza consultas a los registros DNS de un dominio para obtener información como registros A, MX, entre otros.

2. 🌐 **Fuerza bruta de subdominios**  
   Realiza un escaneo de subdominios a partir de un archivo de diccionario con posibles subdominios.

Parámetros de entrada:
    -t o --target  : Dominio o URL a consultar  
    -q o --query   : Tipo de consulta DNS (ej: A, MX, etc.)  
    -b o --brute   : Ruta al archivo de diccionario de subdominios

Requisitos:
    - Python 3.x
    - dnspython (pip install dnspython)
    - tqdm (pip install tqdm)

Instalación:
    pip install dnspython tqdm

Ejemplos de uso:

    python dns_query_tool.py -t example.com -q A  
    python dns_query_tool.py -t example.com -b subdominios.txt
"""
import dns.resolver
import argparse
from dns.resolver import NoAnswer
from urllib.parse import urlparse
from tqdm import tqdm  # Importamos tqdm para la barra de progreso

# Parsing input arguments
parser = argparse.ArgumentParser(description="Programa para realizar consultas DNS y búsqueda de subdominios a través de un diccionario.")
parser.add_argument("-t", "--target", help="Dominio o URL a consultar")
parser.add_argument("-q", "--query", help="Tipo de consulta DNS (ej: A, MX, etc.)")
parser.add_argument("-b", "--brute", help="Ruta al archivo de diccionario de subdominios")
parser = parser.parse_args()

# Brute-force subdomain search using a wordlist
def brute(target, brute_file):
    """Realiza un ataque de fuerza bruta para descubrir subdominios utilizando un archivo de diccionario."""
    try:
        with open(brute_file, "r") as archivo:
            subdominios = archivo.read().splitlines()
    except FileNotFoundError:
        print(f"Error: El archivo {brute_file} no se encontró.")
        return

    listaSubdominiosEncontrados = []

    # Inicializamos la barra de progreso
    with tqdm(total=len(subdominios), desc="Escaneando subdominios: 0 encontrados", unit="subdominio") as pbar:
        # Iteramos sobre los subdominios y actualizamos la barra de progreso
        for sub in subdominios:
            subdominio_completo = f"{sub}.{target}"
            try:
                # Realiza la consulta DNS de tipo A para cada subdominio
                respuesta = dns.resolver.resolve(subdominio_completo, "A")
                for ip in respuesta:
                    listaSubdominiosEncontrados.append(f"{subdominio_completo} - {ip}")
            except (NoAnswer, dns.resolver.NXDOMAIN):
                pass  # Ignora si no se encuentra respuesta o el subdominio no existe

            # Actualiza la barra de progreso y la descripción con los subdominios encontrados
            pbar.set_description(f"Escaneando subdominios: {len(listaSubdominiosEncontrados)} encontrados")
            pbar.update(1)  # Avanza la barra de progreso en 1 unidad por cada subdominio procesado

    # Al finalizar, imprime todos los subdominios encontrados
    print("\nBúsqueda finalizada.\n")

    if listaSubdominiosEncontrados:
        print("Subdominios encontrados:")
        for sub in listaSubdominiosEncontrados:
            print(sub)
    else:
        print("No se encontraron subdominios.")

def main():
    """Función principal para gestionar las consultas y las opciones de fuerza bruta."""
    if parser.target:
        # Elimina el esquema (https:// o http://) del target si existe
        target = urlparse(parser.target).netloc if parser.target.startswith("http") else parser.target
        if parser.query and not parser.brute:
            try:
                respuesta = dns.resolver.resolve(target, parser.query)
                for cosa in respuesta:
                    print(cosa)
            except NoAnswer:
                print(f"No encontré resultados para la consulta {parser.query} en el dominio {target}")
            except dns.resolver.NXDOMAIN:
                print(f"No se pudo encontrar el dominio {target}")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
        elif parser.brute:
            target_split = target.split(".")
            # Usamos el dominio completo como base para la consulta de subdominios
            nuevaURL = ".".join(target_split[-2:])  # Solo mantiene el dominio principal y el TLD (por ejemplo, dvp.cl)
            brute(nuevaURL, parser.brute)
        else:
            print("Los parámetros ingresados no son válidos. Asegúrese de proporcionar los argumentos correctos.")

if __name__ == "__main__":
    main()