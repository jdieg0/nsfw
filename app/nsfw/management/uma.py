from app.nsfw.models import Report
import requests
from django.core.management.base import BaseCommand
import datetime
from urllib.parse import urlencode
from app.nsfw.management.utils import POLLUTANTS, SCOPES, UBA_BASE_URL

class UmaCommand(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('date', nargs='+', type=str, help='13.12.2015')

    def handle(self, *args, **options):
        for date in options['date']:
            date = datetime.datetime.strptime(date, "%d.%m.%Y").strftime("%Y-%m-%d")
            query = {
                "component" : POLLUTANTS[self.pollutant],
                "scope"     : SCOPES[self.data_type],
                "date_from" : date,
                "time_from" : 1,
                "date_to"   : date,
                "time_to"   : 24,
            }
            query_string = urlencode(query)
            url = UBA_BASE_URL + query_string
            print('url', url)
            req = requests.get(url)
            content = req.content.decode('iso-8859-1')
            if content:
                res, created = Report.objects.get_or_create(
                    data=content,
                    country='de',
                    source='uba',
                    kind=self.pollutant,
                    date=date)
                if created:
                    self.stdout.write(self.style.SUCCESS('%s' % res))
            else:
                raise Exception('%s: no data available yet on %s. %s' % (self.pollutant, date, url))
