import requests
from bs4 import BeautifulSoup
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
# response = requests.get("https://www.google.com/?hl=ar", headers=headers)

# print(type(response))
# print(response.status_code)
# print(response.content)
# print(response.text)

# response1 = requests.get('https://api.github.com', headers=headers)
# print(response1.json())
# print(response1.headers)
# print(response1.headers['Content-type'])

# response2 = requests.get("https://www.amazon.eg/s", headers=headers, params={'k':'ساعة+يد'})
# print(response2.text)
url = 'https://www.amazon.eg/%D9%85%D8%B9%D8%AF%D9%86%D9%8A%D8%A9-%D9%83%D8%A7%D8%AC%D9%88%D8%A7%D9%84-%D8%A7%D9%86%D8%A7%D9%84%D9%88%D8%AC-%D9%85%D9%8A%D9%86%D9%8A-MF0188G-02%D8%8C/dp/B07NZVKGYF/ref=sr_1_5?crid=3SMDZCLLBVV1A&dib=eyJ2IjoiMSJ9.I9yKjossixX5cSzrQb-Zx1Z2o00VwuJl5P5uE212J44s8hgk6R9rQdZAZW5g5Bm6TXxN1h4gxY5ETI4ScePKT6ewwDveAU7IzQQVZeC01vYk7X10CLKg0Pmu8GG58iRzwXCQCJFK7p-6hHa8hyrrBXK4aaopYh73VHwLDl_nFldxsDmb0B618QBxyCBHnnewuTTOR8s-Xz-M7jALIHGelTADQM1hjQ5nF10GVBFg7cZaH1WW9KnL9RIbahAtTYydDnTTiy3o4zrPvhZ_-P12gZGACbusCfzd6eKbAUzWaLQ.2IZIK8KihIWBVQhwLSIVCxGCI0P0M4VhYSYgsSOmLfs&dib_tag=se&keywords=%D8%B3%D8%A7%D8%B9%D8%A9+%D9%8A%D8%AF&qid=1723372231&sprefix=%D8%B3%D8%A7%D8%B9%D8%A9+%D9%8A%D8%AF%2Caps%2C143&sr=8-5'
response = requests.get(url, headers=headers, params={'k':'ساعة+يد'})
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
# print(soup.prettify())
title = soup.find('span', id='productTitle')
print(title)
# print(title.string)
# print(title.string.strip())


whole_price = soup.find('span', class_='a-price')
# print(whole_price.get_text().strip())

price = whole_price.find('span', class_='a-offscreen')
# print(price.get_text().strip())

image = soup.find('div', id='imgTagWrapperId')
# price(image)
price(image)
# price(image['src'])
