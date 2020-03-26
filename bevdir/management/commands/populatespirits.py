from django.core.management.base import BaseCommand, CommandError
import requests
from bs4 import BeautifulSoup
from bevdir.models import Spirit

class Command(BaseCommand):
  help = 'populates the Spirits database using beautifulsoup to scrape https://abc.nc.gov/Pricing/PriceList'

  def handle(self, *args, **kwargs):
    response = requests.get("https://abc.nc.gov/Pricing/PriceList")
    soup = BeautifulSoup(response.text, 'html.parser')
    spirits = soup.find_all(class_="list-generic")
    for spirit in spirits:
        elements = spirit.find_all('div')
        try:
            this_spirit = Spirit.objects.get(brandname=elements[2].get_text())
            this_spirit.mxb = float(elements[7].get_text().replace('$', '').replace(',',''))
            this_spirit.save()
            print(this_spirit.brandname)
        except Spirit.DoesNotExist:
            new_spirit = Spirit.objects.create(
                nc_code = elements[0].get_text(),
                supplier = elements[1].get_text(),
                brandname = elements[2].get_text(),
                proof = elements[4].get_text(),
                size = float(elements[5].get_text().replace('M', '').replace('L', '').replace(',','')),
                mxb = float(elements[7].get_text().replace('$', '').replace(',',''))
            )
            new_spirit.save()
            print(new_spirit.brandname)