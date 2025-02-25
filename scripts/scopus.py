import requests
import pandas as pd

# Configurar API de Scopus
api_key = 'TU_API_KEY'
url = 'http://api.elsevier.com/content/search/scopus'
query = 'alluvium AND Quito'
headers = {'Accept': 'application/json', 'X-ELS-APIKey': api_key}
params = {'query': query, 'count': 25}

# Hacer solicitud
response = requests.get(url, headers=headers, params=params)
data = response.json()

# Procesar resultados
articles = data['search-results']['entry']
articles_data = [{'title': article['dc:title'], 'date': article['prism:coverDate']} 
                 for article in articles]
df_scopus = pd.DataFrame(articles_data)
df_scopus.to_csv('scopus_articles.csv', index=False)