from django.db import models
from django.conf import settings
from holding.models import Holding


class Transaction(models.Model):
    TIPO = (
        ("COMPRA","Compra"),
        ("VENDA","Venda")
    )

    holding = models.ForeignKey(Holding, on_delete=models.CASCADE, related_name='transactions')
    tipo = models.CharField(max_length=6, choices=TIPO)
    quantidade = models.DecimalField(max_digits=20, decimal_places=2)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return f"{self.tipo}: {self.holding.name_tikets}"