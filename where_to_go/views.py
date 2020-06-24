from django.shortcuts import render, get_object_or_404
from places.models import Place
from django.http import HttpResponse


def index(request):
    places = Place.objects.all()

    feature_collection = make_feature_collection(places)

    data = {'feature_collection': feature_collection}

    return render(request, '../templates/index.html', context=data)


def place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    response = HttpResponse(place.title)
    return response


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
