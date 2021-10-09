from django.urls import path
from msg_manager.views import MessageView,hello_world

urlpatterns = [
    path('<username>/',MessageView.as_view())
]

