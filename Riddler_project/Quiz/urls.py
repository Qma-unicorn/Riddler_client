from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('tests/', views.QuizesView, name='quizes'),
    path('test/<int:quiz_id>', views.QuizView, name='quiz'),
    path('result/', views.ResultView, name='result'),

    path('api/tests', views.QuizesApi, name='apiT'),
]
