from django.db import models
from ..authentication.models import User

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    entry_no = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    is_private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ["-created_at"]
    def __str__(self):
        return self.name
