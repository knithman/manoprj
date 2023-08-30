from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage-url'),
    path('kompiuteriai/', views.kompiuteriai, name='kompiuteriai-visi-url'),
    path('kompiuteriai/<int:kompiuteris_id>/', views.kompiuteris, name='kompiuteris-vienas-url'),
    path('nesiojami/', views.KompiuterisListView.as_view(), name='nesiojami-visi-url'),
    path('nesiojami/<int:pk>/', views.KompiuterisDetailView.as_view(), name='nesiojami-vienas-url'),
    path('paieska/', views.search_stacionarus, name='paieska-url'),
    path('paieska/stacionarus/', views.search_stacionarus, name='paieska-stacionarus-url'),
]
