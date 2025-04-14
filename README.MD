# 🛡️ CyberTools: Herramientas de Ciberseguridad con Python

Bienvenido a **CyberTools**, una colección ligera y poderosa de herramientas creadas con Python para análisis y reconocimiento en entornos de ciberseguridad. Ideal para pentesters, analistas y curiosos digitales 🧠💻.

---

## 🚀 Herramientas incluidas

### 🔍 CDN Detector (Cloudflare)
 **¿El sitio está protegido por Cloudflare?**  
Esta herramienta analiza si un recurso está detrás de un CDN como Cloudflare, útil para saber si estás frente a una IP real o una red de protección.

```
python cloudflare_detector.py -t example.com -m header
python cloudflare_detector.py -t example.com -m whois
```


### 🧠 Web Technology Analyzer
**Descubre qué tecnologías utiliza un sitio web**
Basado en la librería python-Wappalyzer, esta herramienta identifica las tecnologías utilizadas por un sitio web, incluyendo frameworks, CMS, servidores, librerías JS y más.

Ideal para reconocimiento pasivo y análisis de superficie de ataque.
Permite ingresar la URL desde la línea de comandos.
```
python web_technology_analyzer.py -u example.com
```


### 🧭 DNS Query Tool
**Realiza consultas DNS y búsqueda de subdominios utilizando un diccionario**

Basado en la librería dnspython, esta herramienta permite realizar consultas a registros DNS de un dominio y realizar ataques de fuerza bruta para descubrir subdominios a partir de un diccionario.

Ideal para pruebas de penetración, análisis de superficie de ataque y reconocimiento de infraestructura web.

Permite consultar diferentes tipos de registros DNS (A, MX, entre otros) o buscar subdominios utilizando un archivo de diccionario.

```
python dns_query_tool.py -t example.com -q mx
python dns_query_tool.py -t example.com -b subdomains.txt

```
