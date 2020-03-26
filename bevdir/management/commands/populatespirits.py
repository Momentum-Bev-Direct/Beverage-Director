from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
  help = 'populates the Spirits database using beautifulsoup to scrape https://abc.nc.gov/Pricing/PriceList'

  def populate(self):
