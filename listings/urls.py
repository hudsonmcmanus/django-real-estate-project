from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listings_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]
