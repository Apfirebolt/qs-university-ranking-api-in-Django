from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd
from api.models import University


class Command(BaseCommand):
    help = 'Clears already populated University data from the database'

    def handle(self, *args, **kwargs):
        
        df = pd.read_csv('data/2023_data.csv')

        result = df.head(10)

        universities = University.objects.all()
        
        for one_university in universities:
            try:
                print(f'Deleting university {one_university.name}')
                one_university.delete()
            except Exception as err:
                print('Could not delete ', err)
        
            
