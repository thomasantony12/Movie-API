from rest_framework import serializers
from API.models import Genre,Actor,Technician,Movie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=('name',)
        
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields=('first_name', 'last_name')

class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model=Technician
        fields=('first_name', 'last_name', 'role')

class MovieReadSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    technicians = TechnicianSerializer(many=True)
    
    class Meta:
        model=Movie
        fields=('name', 'release_year', 'genres', 'actors', 'technicians', 'average_rating')

class MovieWriteSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all()
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Actor.objects.all()
    )
    technicians = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Technician.objects.all()
    )

    class Meta:
        model = Movie
        fields = ('name', 'release_year', 'genres', 'actors', 'technicians', 'average_rating')

