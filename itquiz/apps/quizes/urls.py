from django.urls import path
from itquiz.apps.quizes import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
