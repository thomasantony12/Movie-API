from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from API.models import Actor,Movie
from API.serializers import MovieReadSerializer, MovieWriteSerializer
# Create your views here.


@csrf_exempt
def movieApi(req, id=0):
    '''
    This method is used to get a particular movie details or Add movie details or Update movie details

    Sample route: http://127.0.0.1:8000/movies/id
    Sample data: {
        "name": "squid game",
        "release_year": 2022,
        "genres": [1],
        "actors": [2],
        "technicians": [1],
        "average_rating": 4.0
    }
    '''
    if req.method=='GET':
        movie = Movie.objects.get(id=id)
        movie_serializer = MovieReadSerializer(movie)
        return JsonResponse(movie_serializer.data, safe=False)
    elif req.method=='POST':
        movie_data = JSONParser().parse(req)
        #print('hi',movie_data)

        if id:
            movie = Movie.objects.get(id=id)
            movies_serializer = MovieWriteSerializer(movie, data = movie_data)
            movies_serializer.is_valid()
            print(movies_serializer.errors)
            if movies_serializer.is_valid():
                movies_serializer.save()
                return JsonResponse("Movie updated successfully", safe=False)
            return JsonResponse("Failed to update movie", safe=False)
        else:
            movies_serializer = MovieWriteSerializer(data = movie_data)
            if movies_serializer.is_valid():
                movies_serializer.save()
                return JsonResponse("Movie Added successfully", safe=False)
            return JsonResponse("Failed to add movie", safe=False)
    
    else:
        return JsonResponse("Bad request")

@csrf_exempt
def movieFilterApi(req):
    '''
    This function is used to get all movies or filter through the movies.

    Sample route: http://127.0.0.1:8000/movieFilter/?actor_id=1&director_id=1&technician_id=1
    '''
    if req.method=='GET':
        actor_id = req.GET.get('actor_id', None)
        director_id = req.GET.get('director_id', None)
        technician_id = req.GET.get('technician_id', None)

        movies = Movie.objects.all()

        if actor_id:
            movies = movies.filter(actors__id=actor_id)
        if director_id:
            movies = movies.filter(director__id=director_id)
        if technician_id:
            movies = movies.filter(technicians__id=technician_id)

        movies_serializer = MovieReadSerializer(movies, many= True)
        return JsonResponse(movies_serializer.data, safe=False)
    
    else:
        return JsonResponse("Bad request")
    

@csrf_exempt
def deleteActorApi(req, actor_id):
    '''
    This function is used to check if the actor associated with any movies, if not delete the actor details

    Sample route: http://127.0.0.1:8000/actors/id
    '''
    if req.method=='POST':
        actor = Actor.objects.get(id=actor_id)
        if actor.movies.exists():
            return JsonResponse("Actor is associated", safe=False)
        actor.delete()
        return JsonResponse("Actor deleted", safe=False)
    