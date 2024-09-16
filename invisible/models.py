from django.db import models
from django.contrib.auth.models import User

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_assigned = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Assignment(models.Model):
    giver = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='giver')
    receiver = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='receiver')

    def __str__(self):
        return f"{self.giver} -> {self.receiver}"
