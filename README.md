![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)


# QS Rankings of Universities - API

Just stumbled across a dataset on Kaggle which had QS rankings of universities all around the world. There are almost 1500 universities in the list. I thought of converting
this into an API using Django. That is the back-ground behind how this project started.

## Django Management Commands

Django comes with some command line instructions to create a super user for example. These scripts are executed with 'manage' prefixed over it and they look for a given 
directory structure to find the relevant commands to run. Below is the custom management script I created which populates the local database with the university data 
coming from the csv file.

```
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
        
```

You can run it just like you run your development server in Django. Just type 'python manage.py populate'

## Database

Postgres is used for the database configured in settings.py file insdie the Django app. Though it was not required, for the time being it still uses a Custom User model
since it is considered one of the best practices of starting out with Django.

## Future Updates/Tasks

- Apply rate limit and search filtering
- Docker deployment

## Authors

* **Amit Prafulla (APFirebolt)** - [My Website](https://apgiiit.com)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



