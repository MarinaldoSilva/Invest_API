from django.db import models
from investing.models import Assets
from portifolio.models import Portifolio


class Holding(models.Model):
    portifolio = models.ForeignKey(Portifolio, on_delete=models.CASCADE, related_name="holding")
    name_tikets = models.ForeignKey(Assets, on_delete=models.CASCADE, related_name="nome_ativo") 
    quantidade_ativos = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    preco_medio = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        unique_together = ('portifolio', 'name_tikets')

    def __str__(self):
        return f"{self.quantidade_ativos} de {self.name_tikets.nome} da carteira {self.portifolio.nome_carteira}"