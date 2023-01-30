from xml.dom import ValidationErr
from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
# Create your models here.
from django.db import models

class Departement(models.Model):
    nom = models.CharField(max_length=255)  
   
    
 

class Filiere(models.Model):
    nom = models.CharField(max_length=255)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    

class Promotion(models.Model):
    nom = models.CharField(max_length=255)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    
class GroupeTDTP(models.Model):
    nom = models.CharField(max_length=255)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

class Enseignant(models.Model):
    nom = models.CharField(max_length=255)
   

class Salle(models.Model):
    nom = models.CharField(max_length=255)

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=256)


class Matiere(models.Model):
    nom = models.CharField(max_length=255)
    

class Creneau(models.Model):
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    promo = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere,max_length=255,on_delete=models.CASCADE)
    type_creneau = models.CharField(max_length=255, choices=[("Cours", "Cours"), ("TD", "TD"), ("TP", "TP")])
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    dateString = models.CharField(max_length=255,null=True)
    debut = models.CharField(max_length=255,null=True)
    fin = models.CharField(max_length=255,null=True)
    dif = models.IntegerField(null=True)

    # def clean(self):
    #     overlapped_creneaux = Creneau.objects.filter(
    #         enseignant=self.enseignant,
    #         date=self.date,
    #         heure_debut__lte=self.heure_fin,
    #         heure_fin__gte=self.heure_debut
    #     )
    #     if self.pk:
    #         overlapped_creneaux = overlapped_creneaux.exclude(pk=self.pk)
    #     if overlapped_creneaux.exists():
    #         raise ValidationErr("This teacher is already assigned to another creneau at this time.")

    
    def __str__(self):
        return  Creneau


