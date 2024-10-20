from django.urls import path
from first_app.views import hello_view

urlpatterns = [
    path('hello/<str:name>/', hello_view),
]

