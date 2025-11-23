from django.urls import path
from .views import Data_API

urlpatterns = [
    path('task/', Data_API.as_view()),
    path('task/<int:task_id>/', Data_API.as_view()),
]