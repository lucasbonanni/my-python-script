#Get dollar price from BNA www.bna.com.ar
import requests, bs4

res = requests.get('https://www.bna.com.ar/Personas')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
prices = soup.select('#billetes > table > tbody > tr:nth-child(1) > td')
print(prices)
