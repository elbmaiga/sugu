from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, kwargs={}, name="index"),
    path('category/<str:params>', views.search_category, kwargs={}, name="search_category"),
    path('search/', views.search, kwargs={}, name="search"),
    path('add/panner/<slug:article_slug>/<int:quantity>', views.add_panner, kwargs={}, name="add_panner"),
    path('<slug:article_slug>', views.detail, kwargs={}, name="detail"),
]