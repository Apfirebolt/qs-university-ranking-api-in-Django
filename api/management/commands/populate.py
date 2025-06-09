from django.core.management.base import BaseCommand
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
                                        ar_score=row['ar score'], ar_rank=row['ar rank'], location=row['location code'],
                                        fsr_score=row['fsr score'], fsr_rank=row['fsr rank'], cpf_score=row['cpf score'],
                                        cpf_rank=row['cpf rank'], ifr_score=row['ifr score'], ifr_rank=row['ifr rank'],
                                        isr_score=row['isr score'], isr_rank=row['isr rank'], irn_score=row['irn score'],
                                        irn_rank=row['irn rank'], ger_score=row['ger score'], ger_rank=row['ger rank'],
                                        score_scaled=row['score scaled'] )
                current_university.save()
                print('Data saved for ', row['institution'])
            except Exception as err:
                print('Could not save data for this university ', err)
        
            
