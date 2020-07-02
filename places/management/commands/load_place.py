from io import BytesIO


from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Image

import requests


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='+', type=str)

    def handle(self, *args, **options):
        url = options['url'][0]
        response = requests.get(url)
        decoded_response = response.json()

        new_place, status = Place.objects.get_or_create(
            title=decoded_response['title'],
            description_short=decoded_response['description_short'],
            description_long=decoded_response['description_long'],
            lon=decoded_response['coordinates']['lng'],
            lat=decoded_response['coordinates']['lat'],
        )

        for num, image in enumerate(decoded_response['imgs'], start=1):
            new_image = Image(
                place=new_place,
                position=num
            )
            new_image.save()
            image_name = image.split('/')[-1]

            response = requests.get(image, verify=False)
            response.raise_for_status()

            i = BytesIO(response.content)

            new_image.image.save(image_name, i, save=True)
