from django.urls import path
from itquiz.apps.quizes import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<slug>/', views.CategoryView.as_view(), name='category'),
    path('category/<category_slug>/<slug>/', views.QuizView.as_view(), name='quiz'),
    path('about/', views.about, name='about'),
]
