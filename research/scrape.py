from bs4 import BeautifulSoup


#site to scrape: https://abc.nc.gov/Pricing/PriceList

# Collections: <u> nested in <h5>
# Each Liquor Row: <div class='list-generic'
  # Subsequent Info Nested: <div class="border-right"

#SCRAPING
#Beautiful Soup
#Look up management commands.

soup = BeautifulSoup()

#Direct Access
# print(soup.body)
# print(soup.head)
# print(soup.title)

# FIND
  el = soup.find('div') # finds first element with that tag
  el = soup.find(id='nodeID')
  el = soup.find(class_='container') #need underscore since 'class' is a reserved word
  el = soup.find(attrs={"data-attribute": "value"}) #for data attribute
  # find_all() or findAll()
  el = soup.find_all('div') # returns a list of all of the items with that tag

#SELECT
  el = soup.select('#id OR .class')[0] #this is always returns a list.. so use index if you want something particular

#GET TEXT
  el = soup.find(class='container').get_text()
  #you can also use this in a loop to get the text of each item in an iterable

#NAVIGATION
  el = soup.body.contents #factors in linebreaks so ignore \n
  el = soup.body.contents[1].next_sibling() #won't ignore linebreaks
  el = soup.body.contents[1].find_next_sibling() #will ignore linebreaks
  .find_previous_sibling('can specify which tabs to target.. like <p> or <div>')
  .find_parent()
