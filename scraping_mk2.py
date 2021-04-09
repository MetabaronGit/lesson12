# pokusy se scrapingem
import requests
import bs4

# odfiltrování prázdných řádků
def clear_content(content: list):
    for item in content:
        if item == "\n":
            content.remove(item)

try:
    content = requests.get("http://example.com")
    print("status code:", content.status_code)
    soup = bs4.BeautifulSoup(content.text, "html.parser")
    # print(soup)
except Exception:
    print("chyba!")

text = soup.body.div.contents
print(len(text))
clear_content(text)
print(len(text))
