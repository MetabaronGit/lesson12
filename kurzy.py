# colab
# https://colab.research.google.com/drive/1ksMAK0wmSacOZnZXTBAhZZwM_QiRdAfE?usp=sharing#scrollTo=lYlvlcLfgjwp

# import pandas as pd
#
# pd.read_html("http://heroes3.cz/hraci/")[2].to_csv("hraci_II.csv")

# RSS
# import feedparser
# dir(feedparser)
# rss_url = "https://news.google.com/news/rss/?hl=cs&amp;ned=cs&amp;gl=CSdef"
# feeds = feedparser.parse(rss_url)
# def my_info_from_feed(feeds):
#   for feed in feeds["entries"]:
#     # print(feed["img"])
#     print(feed["title"])
#     print(feed["summary"])
#     print(feed["link"])
#     print(100*"-")
# my_info_from_feed(feeds)


url = "https://www.kurzy.cz/ethereum/"
def get_price(url):
  data = requests.get(url)
  html = data.text
  soup = BeautifulSoup(html)
  price = soup.find("span", id = "last_usd").text
  print(price)

get_price(url)