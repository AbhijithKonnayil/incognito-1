from django.urls import path
from msg_manager.views import hello_world

urlpatterns = [
    path('',hello_world)
]

