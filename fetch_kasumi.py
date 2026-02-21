import requests
from bs4 import BeautifulSoup

url = "https://www.kasumi.ed.jp/%e5%85%a5%e8%a9%a6%e6%83%85%e5%a0%b1/"
response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, 'html.parser')

entry_content = soup.find(class_='entry-content')
if entry_content:
    print("Found entry-content")
    print(str(entry_content)[:500])
else:
    print("Not found entry-content")
    main = soup.find('main')
    if main:
        print("Found main")
        print(str(main)[:500])
