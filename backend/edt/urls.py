from django.urls import path

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('creneau', CreneauViewsSet)
router.register('filiere', FiliereViewsSet)
router.register('promo', PromotionViewsSet)
router.register('tdtp', GroupeTDTPViewsSet)
router.register('enseignant', EnseignantViewsSet)
router.register('salle', SalleViewsSet)
router.register('departement', DepartementViewsSet)
router.register('matiere', MatiereViewsSet)
router.register('user', UserViewsSet)



urlpatterns = router.urls
  