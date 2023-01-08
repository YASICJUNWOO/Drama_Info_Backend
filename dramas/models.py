from django.db import models


class Drama(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField(default="")
    genre = models.ManyToManyField(
        "genre.Genre",
        blank=True,
    )
