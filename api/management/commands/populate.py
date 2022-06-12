from django.core.management.base import BaseCommand
from django.utils import timezone
import pandas as pd
from api.models import University


class Command(BaseCommand):
    help = 'Populates University Database from csv file'

    def handle(self, *args, **kwargs):
        
        df = pd.read_csv('data/2023_data.csv')

        result = df.head(10)

        for index, row in df.iterrows():
            try:
                current_university = University(name=row['institution'], country=row['location'], rank=row['Rank'], 
                                        ar_score=row['ar score'], ar_rank=row['ar rank'], location=row['location code'])
                current_university.save()
                print('Data saved for ', row['institution'])
            except Exception as err:
                print('Could not save data for this university ', err)
        
            
