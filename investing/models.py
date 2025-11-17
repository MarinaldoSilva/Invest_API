from django.conf import settings
from django.db import models


class Assets(models.Model):
    TYPES_INVESTING = (
        ("ACAO", "Ação"),
        ("FLLS", "Fundos imobiliários"),
        ("COMMODITIES", "Commodities"),
        ("RENDA_FIXA", "Renda Fixa"),
    )

    """código da negociação, ex.: PETRA4/MAGL2"""
    tiket = models.CharField(max_length=10, unique=True)

    tipo = models.CharField(max_length=255, choices=TYPES_INVESTING, default="ACAO")

    nome = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.tiket} -> {self.tipo}"
