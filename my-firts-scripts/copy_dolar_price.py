#Get dollar price from BNA www.bna.com.ar
import requests, bs4, pyperclip,locale

res = requests.get('https://www.bna.com.ar/Personas')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
prices = soup.select('#billetes > table > tbody > tr:nth-child(1) > td')
#print(prices.get_text())
dollarValues = ''
for price in prices:
    if(price.text.isdecimal()):
        print(locale.str(locale.atof(price.text)))
        dollarValues = dollarValues + '\n' + locale.str(locale.atof(price.text.replace(',','.')))
    else:
        dollarValues = dollarValues + '\n' + price.text
        print(price.text)
print(dollarValues)
#formatted = dollarValues.replace(',','.')        
pyperclip.copy(dollarValues)
