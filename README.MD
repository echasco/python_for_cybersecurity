# 🛡️ CyberTools: Herramientas de Ciberseguridad con Python

Bienvenido a **CyberTools**, una colección ligera y poderosa de herramientas creadas con Python para análisis y reconocimiento en entornos de ciberseguridad. Ideal para pentesters, analistas y curiosos digitales 🧠💻.

---

## 🚀 Herramientas incluidas

### 🔍 CDN Detector (Cloudflare)
 **¿Un archivo o sitio está protegido por Cloudflare?**  
Esta herramienta analiza si un recurso está detrás de un CDN como Cloudflare, útil para saber si estás frente a una IP real o una red de protección.

```
python cdn_detector.py -u https://example.com
```


### 🧠 Web Technology Analyzer
**Descubre qué tecnologías utiliza un sitio web**
Basado en la librería python-Wappalyzer, esta herramienta identifica las tecnologías utilizadas por un sitio web, incluyendo frameworks, CMS, servidores, librerías JS y más.

Ideal para reconocimiento pasivo y análisis de superficie de ataque.
Permite ingresar la URL desde la línea de comandos.
```
python app_wappalyzer.py -u https://example.com
```