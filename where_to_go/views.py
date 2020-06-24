from django.shortcuts import render
from places.models import Place


def index(request):
    places = Place.objects.all()

    feature_collection = make_feature_collection(places)

    data = {'feature_collection': feature_collection}

    return render(request, '../templates/index.html', context=data)


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
