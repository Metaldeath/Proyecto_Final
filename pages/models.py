from django.db import models
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field

User = get_user_model()

class Page(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)
    contenido = CKEditor5Field('Contenido', config_name='default')
    imagen = models.ImageField(upload_to='pages/', blank=True, null=True)
    fecha = models.DateField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pages')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
