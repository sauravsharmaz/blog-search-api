from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default=None, blank=True, null=True)
    body = models.CharField(max_length=1000, default=None, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title