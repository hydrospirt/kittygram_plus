from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from cats.views import CatViewSet, OwnerViewSet, CatLightViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register(r'mycats', CatLightViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]