import json

from django.shortcuts import render, get_object_or_404
from places.models import Place, Image
from django.http import HttpResponse, JsonResponse


def index(request):
    places = Place.objects.all()

    feature_collection = make_feature_collection(places)

    data = {'feature_collection': feature_collection}

    return render(request, '../templates/index.html', context=data)


def place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return make_place_json(place)


def make_feature_collection(places):
    result = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": "zagluwe4ka"
            }
        }

        result["features"].append(feature)

    return result


def make_place_json(place):

    result = {
        "title": place.title,
        "imgs": get_place_images(place),
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lon
        }
    }

    print(get_place_images(place))

    return JsonResponse(result, safe=False, json_dumps_params={'indent': 4, 'ensure_ascii': False})


def get_place_images(place):
    return [image.image.url for image in Image.objects.filter(place=place.id)]