from django.core.management.base import BaseCommand
from app.nsfw.models import Station
import requests
import datetime
from urllib.parse import urlencode
from app.nsfw.management.utils import POLLUTANTS, SCOPES, UBA_BASE_URL

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--berlin', help='load only berlin data', action='store_const', const=True)

    def handle(self, *args, **kwargs):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        for station in Station.objects.filter(id__startswith='DE'):
            if kwargs['berlin'] and not station.id.startswith('DEBE'):
                continue
            print(station)

            # Assemble URLs for API GET requests
            query = {
                "component" : POLLUTANTS['PM10'],
                "scope"     : SCOPES['1TMW'],
                "station"   : station.id,
                "date_from" : today,
                "time_from" : 1,
                "date_to"   : today,
                "time_to"   : 24,
            }
            query_string = urlencode(query)
            url = UBA_BASE_URL + query_string
            pm10_r = requests.get(url)

            query = {
                "component" : POLLUTANTS['NO2'],
                "scope"     : SCOPES['1SMW_MAX'],
                "station"   : station.id,
                "date_from" : today,
                "time_from" : 1,
                "date_to"   : today,
                "time_to"   : 24,
            }
            query_string = urlencode(query)
            url = UBA_BASE_URL + query_string
            no2 = requests.get(url)

            assert no2.status_code is 200, 'error when downloading data for %s:\n%s' % (station, no2.__dict__)
            assert pm10_r.status_code is 200, 'error when downloading data for %s:\n%s' % (station, pm10_r.__dict__)
            pm10 = pm10_r.content.decode('iso-8859-1')
            no2 = no2.content.decode('iso-8859-1')
            if pm10:
                station.pm10_data = pm10
            if no2:
                station.no2_data = no2
            if pm10 or no2:
                station.save()
