#import libraries
import urllib.request
from bs4 import BeautifulSoup

#specify the url
quote_page = 'https://www.nasdaq.com/symbol/fb/after-hours'

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(quote_page) 

# parse the html using beautiful soup and store in the variable 'soup'
soup = BeautifulSoup(page, 'html.parser') 

# Take out the <div> of name and get its value
name_box = soup.find('h1')

#define variable for where we'll store the name of our stock
name = name_box.text.strip() # strip() is used to remove starting and trailing
print(name)

# get the index price
price_box = soup.find('div', attrs={'class':'qwidget-dollar'})
# define variable for where we'll store the price of our stock
price = price_box.text
print(price)
