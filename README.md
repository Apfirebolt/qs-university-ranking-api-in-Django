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

API keys are now added for unauthenticated users to access the API through API key generation. The url for api key generation is 'api/create-api-key' and expects name key in request body. It generates the following response.
```
{
    "name": "Gareth",
    "key": "BjGca2Rg.y3sScExPYRzdVRraXQigvfNNEUe9mgxV"
}
```

Subsequently you can use this key to access the university data through the inclusion of 'Api-Key' Authorization in the request header.

```
{
    'Authorization': 'Api-Key xBybKmJ8.Z1W2CTLrM0767WF24k8R0DFfBhyxfjYU'
}
```

Below is the modified view of the University List API View which allows authenticated users as well as the users who have the API key to access the API data.

```
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey

...


class ListUniversityApiView(ListAPIView):
    serializer_class = UniversitySerializer
    permission_classes = [HasAPIKey | IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    throttle_classes = [UserRateThrottle]
    queryset = University.objects.all()
    search_fields = (
        '^name',
        '^country'
    )
    ordering_fields = (
        'country',
        'name',
        'rank',
        'ar_score',
        'ar_rank'
    )

class CreateApiKeyView(APIView):

    def post(self, request):
        """Generate API Key."""
        username = request.data.get('name')
        if username:
            api_key, key = APIKey.objects.create_key(name=username)
            return Response({'name':str(api_key), 'key': str(key)}, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

```



## Database

Postgres is used for the database configured in settings.py file insdie the Django app. Though it was not required, for the time being it still uses a Custom User model
since it is considered one of the best practices of starting out with Django.

## Docker deployment

Only build images without starting the services

```
docker-compose build
```

Run services in detached mode

```
docker-compose up -d
```

Start services without re-building the image

```
docker-compose up
```

To build images and start all the services

```
docker-compose up --build
```

After making changes to Nginx.conf file we can skip re-building the image

```
docker-compose down
docker-compose up -d
```

## Features

- Rate limit for authenticated users
- Basic Search Filtering
- Pagination
- API key generation using djangorestframework-api-key package

## Authors

* **Amit Prafulla (APFirebolt)** - [My Website](https://apgiiit.com)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



