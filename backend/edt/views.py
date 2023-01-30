from django.shortcuts import render
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *
# Create your views here.

class CreneauViewsSet(ModelViewSet):
    queryset = Creneau.objects.all()
    serializer_class = CreneauSerializer

class FiliereViewsSet(ModelViewSet):
    queryset = Filiere.objects.all()
    serializer_class = FiliereSerializer

class PromotionViewsSet(ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class GroupeTDTPViewsSet(ModelViewSet):
    queryset = GroupeTDTP.objects.all()
    serializer_class = GroupeTDTPSerializer

class EnseignantViewsSet(ModelViewSet):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer

class SalleViewsSet(ModelViewSet):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer

class DepartementViewsSet(ModelViewSet):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer

class MatiereViewsSet(ModelViewSet):
    queryset = Matiere.objects.all()
    serializer_class = MatiereSerializer

class UserViewsSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

