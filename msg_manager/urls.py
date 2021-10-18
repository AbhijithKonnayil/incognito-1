from django.urls import path
from msg_manager.views import MessageSend, MessageView,hello_world

urlpatterns = [
    path('<username>/',MessageSend.as_view()),
    path('',MessageView.as_view())
]

