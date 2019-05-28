from django.db import models
from ..diary.models import Diary

class Entry(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    body = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    views = models.IntegerField(verbose_name=" number of views", default=0)

    class Meta:
        ordering = ["-created_at"]
    def __str__(self):
        return self.title
