from django.db import models
from django.contrib.auth.models import User
class Message(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
