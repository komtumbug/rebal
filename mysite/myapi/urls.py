from django.urls import include, path
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'rapper', views.RapperViewSet)
router.register(r"music", views.MusicViewSet)
router.register(r"car", views.CarViewSet)
router.register(r"crypto", views.CryptoViewSet)
router.register(r"games", views.GamesViewSet)
router.register(r"plant", views.PlantViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

