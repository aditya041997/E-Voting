

from django.db import models
from django.urls import reverse

class VoteFor(models.Model):
    name = models.CharField(max_length=200, blank=True)
    party = models.CharField(max_length=200, blank=True)
    votedon = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    def __str__(self):
        return self.name
