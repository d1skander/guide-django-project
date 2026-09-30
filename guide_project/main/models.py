from django.db import models


import uuid


class SightModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default="Название отсутствует.")
    description = models.TextField(default="Описание отсутсвует.")
    image = models.ImageField(upload_to="image/sight", default="image/default.png")