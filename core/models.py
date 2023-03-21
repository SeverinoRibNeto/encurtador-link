from django.db import models


class Links(models.Model):
    link_original = models.URLField()
    link_encurtado = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.link_encurtado
