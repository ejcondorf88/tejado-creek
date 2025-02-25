from puppeteer import Puppeteer
import pandas as pd

# Configurar Puppeteer
browser = Puppeteer(executable_path='path/to/chromedriver')
page = browser.new_page()

# Navegar a TikTok con una búsqueda específica
page.goto('https://www.tiktok.com/search?q=aluviones+quito')
page.wait_for_selector('div.video-feed-item')

# Extraer comentarios
videos = page.query_selector_all('div.video-feed-item')
data = []
for video in videos[:5]:  # Limitar a 5 videos
    video.click()
    page.wait_for_selector('div.comment-item')
    comments = page.query_selector_all('div.comment-item')
    for comment in comments:
        text = comment.query_selector('p').text_content()
        likes = comment.query_selector('span.like-count').text_content()
        data.append({'comment': text, 'likes': likes})

# Guardar en CSV
df_tiktok = pd.DataFrame(data)
df_tiktok.to_csv('tiktok_comments.csv', index=False)
browser.close()