# pokusy se scrapingem
import requests
import json

try:
    content = requests.get("http://example.com")
except Exception:
    print("chyba!")
finally:
    print("status code:", content.status_code)
    print(content.text)
