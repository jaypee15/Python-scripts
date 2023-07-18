import newspaper

def get_article_info(url):
  article = newspaper.Article(url)
  article.download()
  article.parse()

  return {
    "text": article.text,
    "published": article.publish_date,
    "image": article.top_image,
    "link": article.url,
  }

def main():
  urls = ["https://weetracker.com/2023/06/26/african-fintech-market-obstacles/", "https://african.business/2023/06/trade-investment/from-dotcom-bust-to-tech-wave-boom-african-tech-entrepreneur-hunts-second-fortune", "https://www.africanews.com/2023/06/29/sa-brics-summit-to-go-as-planned-despite-putin-arrest-warrant/"]

  article_info = []
  for url in urls:
    article_info.append(get_article_info(url))

  print(article_info + ' ')

if __name__ == "__main__":
  main()
