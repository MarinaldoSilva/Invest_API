from uuid import uuid4
from django.conf import settings
from django.db import models


class Portifolio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome_carteira = models.CharField(max_length=255, null=False, blank=False)
    dono = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name="portifolio")
    
    date_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.nome_carteira} created by {self.dono.username}"
    

