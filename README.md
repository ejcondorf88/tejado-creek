Análisis de Percepción Ciudadana sobre Aluviones en El Tejado y La Gasca
========================================================================

![Banner](https://via.placeholder.com/800x200.png?text=Aluviones+El+Tejado+y+La+Gasca)\
*Análisis multidimensional de datos sociales y científicos sobre aluviones en Quito, Ecuador.*
https://app.powerbi.com/reportEmbed?reportId=26b09999-35fa-46d2-809f-cd53e19ef5c4&autoAuth=true&ctid=8ca52e2b-1d20-4274-9a13-bd76eccb81d1

Descripción
-----------

Este proyecto utiliza técnicas de **webscraping** y **APIs** para extraer datos de redes sociales (TikTok, Twitter, Instagram, Facebook) y bases de datos científicas (Scopus, Web of Science) con el objetivo de analizar la percepción ciudadana y el contexto técnico de los aluviones en las zonas de El Tejado y La Gasca, Quito, Ecuador. El análisis combina opiniones públicas con evidencia científica para generar insights útiles en la gestión de riesgos y la planificación urbana.

* * * * *

Características
---------------

-   Extracción de comentarios y metadatos de múltiples plataformas sociales.

-   Recopilación de artículos científicos relevantes.

-   Integración y procesamiento de datos con Python.

-   Visualización interactiva de resultados (en desarrollo con Dash).

-   Cumplimiento ético y legal en la manipulación de datos.

* * * * *

Requisitos
----------

### Dependencias de Python

Instala las bibliotecas necesarias con:

bash

AjusteCopiar

`pip install puppeteer-python selenium scrapy tweepy requests pandas beautifulsoup4 dash openpyxl nltk`

-   puppeteer-python: Scraping dinámico en TikTok.

-   selenium: Manejo de contenido dinámico (Instagram, Twitter).

-   scrapy: Extracción estructurada en Facebook.

-   tweepy: Acceso a la API de Twitter.

-   requests: Solicitudes HTTP a APIs.

-   pandas: Procesamiento de datos.

-   beautifulsoup4: Parsing HTML.

-   dash: Visualización de dashboards.

-   openpyxl: Exportación a Excel.

-   nltk: Procesamiento de lenguaje natural.

### Otros Requisitos

1.  **WebDriver**: Descarga [ChromeDriver](https://chromedriver.chromium.org/downloads) o el correspondiente a tu navegador para Selenium.

3.  **Credenciales**:

    -   Twitter API: Regístrate en [Twitter Developer Portal](https://developer.twitter.com/).

    -   Scopus API: Obtén una clave en [Elsevier Developer Portal](https://dev.elsevier.com/).

5.  **Node.js**: Necesario para puppeteer-python (instala con npm install puppeteer).

7.  **Ambiente**: Python 3.8+ recomendado.

* * * * *

Fuentes de Datos
----------------

| Fuente | Tipo de Datos | Método de Extracción |
| --- | --- | --- |
| **TikTok** | Comentarios, likes | Puppeteer |
| **Twitter** | Tweets, likes, fechas | Tweepy (API) |
| **Instagram** | Comentarios, publicaciones | Selenium |
| **Facebook** | Comentarios en grupos | Scrapy |
| **Scopus** | Artículos científicos | API (Elsevier) |
| **Web of Science** | Artículos científicos | Manual (exportación CSV) |

* * * * *

Instalación y Uso
-----------------

1.  **Clona el repositorio**:

    bash

    AjusteCopiar

    `git clone https://github.com/tu-usuario/aluviones-analysis.git cd aluviones-analysis`

3.  **Instala las dependencias**:

    bash

    AjusteCopiar

    `pip install -r requirements.txt`

5.  **Configura las credenciales**:

    -   Crea un archivo .env con tus claves:

        text

        AjusteCopiar

        `TWITTER_CONSUMER_KEY=tu_consumer_key TWITTER_CONSUMER_SECRET=tu_consumer_secret\
        TWITTER_ACCESS_TOKEN=tu_access_token\
        TWITTER_ACCESS_TOKEN_SECRET=tu_access_token_secret\
        SCOPUS_API_KEY=tu_api_key`

7.  **Ejecuta los scripts**:

    -   Extrae datos de cada fuente ejecutando los scripts correspondientes:

        bash

        AjusteCopiar

        `python extract_tiktok.py python extract_twitter.py\
        python extract_instagram.py\
        python extract_facebook.py\
        python extract_scopus.py`

    -   Combina los datos:

        bash

        AjusteCopiar

        `python integrate_data.py`

9.  **Resultados**:

    -   Los datos extraídos se guardan en archivos CSV en la carpeta data/.

* * * * *

Estructura del Proyecto
-----------------------

text

AjusteCopiar

`aluviones-analysis/ │\
├── data/ # Archivos CSV generados\
├── scripts/ # Scripts de extracción\
│ ├── extract_tiktok.py\
│ ├── extract_twitter.py\
│ ├── extract_instagram.py\
│ ├── extract_facebook.py\
│ ├── extract_scopus.py\
│ └── integrate_data.py\
├── requirements.txt # Dependencias\
├── .env # Credenciales (no subir a Git)\
└── README.md # Este archivo`

* * * * *

Ejemplo de Código
-----------------

### Extracción de Twitter

python

AjusteCopiar

`import tweepy import pandas as pd # Configurar API auth = tweepy.OAuthHandler('TU_CONSUMER_KEY', 'TU_CONSUMER_SECRET') auth.set_access_token('TU_ACCESS_TOKEN', 'TU_ACCESS_TOKEN_SECRET') api = tweepy.API(auth)\
# Buscar tweets tweets = api.search_tweets(q='aluviones el tejado la gasca', lang='es', count=100) data = [{'text': t.text, 'likes': t.favorite_count, 'date': t.created_at} for t in tweets] # Guardar df = pd.DataFrame(data) df.to_csv('data/twitter_data.csv', index=False)`

Consulta los scripts completos en la carpeta scripts/ para cada fuente.

* * * * *

Consideraciones Éticas y Legales
--------------------------------

-   **Privacidad**: Anonimiza datos sensibles (e.g., nombres de usuarios) antes de procesarlos.

-   **Cumplimiento**: Respeta las políticas de uso de cada plataforma y la [Ley Orgánica de Protección de Datos Personales](https://www.telecomunicaciones.gob.ec/ley-organica-de-proteccion-de-datos-personales/) de Ecuador.

-   **Límites**: Usa tiempos de espera o proxies para evitar bloqueos por scraping.

* * * * *

Contribuciones
--------------

¡Las contribuciones son bienvenidas! Para colaborar:

1.  Haz un fork del repositorio.

3.  Crea una rama (git checkout -b feature/nueva-funcionalidad).

5.  Envía un pull request con tus cambios.

* * * * *
o en un archivo con extensión .md (por ejemplo, README.md) y asegúrate de mantener los espacios y saltos de línea para que el formato Markdown se rend
