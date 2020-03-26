import requests
from bs4 import BeautifulSoup

response = requests.get("https://abc.nc.gov/Pricing/PriceList")

soup = BeautifulSoup(response.text, 'html.parser')

#LOOK AT PYTHON STRING METHODS FOR MANIPULATIONS

spirits = soup.find_all(class_="list-generic")
spirits_list = []
for spirit in spirits:
  elements = spirit.find_all('div')
  spirit_obj = {}
  spirit_obj['nc_code'] = elements[0].get_text()
  spirit_obj['supplier'] = elements[1].get_text()
  spirit_obj['brandname'] = elements[2].get_text()
  spirit_obj['age'] = elements[3].get_text()
  spirit_obj['proof'] = elements[4].get_text()
  spirit_obj['size'] = elements[5].get_text().replace('L', '')
  spirit_obj['retail'] = elements[6].get_text().replace('$', '')
  spirit_obj['mxb'] = elements[7].get_text().replace('$', '')
  spirits_list.append(spirit_obj)
  # print(spirit_obj)

# for spirit in spirits_list:
#   print(spirit['brandname'])

print(soup)