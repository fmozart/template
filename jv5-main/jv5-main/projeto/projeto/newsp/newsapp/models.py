from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe

# Create your models here.
class noticia(models.Model):
    id = ShortUUIDField