from django.urls import path, include
from items.api.views import HomeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('items', HomeView, basename='items_home')

app_name = 'item'

urlpatterns = [
    path('', include(router.urls)),
]
