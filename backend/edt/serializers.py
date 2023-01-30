from rest_framework import serializers

from .models import *

class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = ('nom', 'departement','id')
        
class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ('nom', 'filiere','id')
        
class GroupeTDTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupeTDTP
        fields = ('nom', 'promotion')
        
class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignant
        fields = ('nom','id')
        
class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = ('nom','id')

class CreneauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creneau
        fields = ('date', 'heure_debut', 'heure_fin', 'promo', 'matiere', 'type_creneau', 'enseignant', 'salle', 'departement','dateString','debut','fin','dif','id')

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = ('nom','id')

class MatiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matiere
        fields = ('nom','id')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','id')
    

