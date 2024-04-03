from django.urls import path
from main import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),  # new
    path('index2', views.Index2.as_view(),
         name='index2'),  # old (to be removed)
]
