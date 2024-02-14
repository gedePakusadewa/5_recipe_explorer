from django.db import models
from django.contrib.auth.models import User

class FavoriteModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.CharField(max_length=10)
    title = models.CharField(max_length=200, default="")
    imageURL = models.URLField(default="")

    class Meta:
        def __str__(self) -> str:
            return self.title
