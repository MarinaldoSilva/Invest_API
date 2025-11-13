from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)

    """RBAC"""
    JOB_ROLES = (
        ("JUNIOR", "Investidor Júnior"),
        ("SENIOR", "Investidor Senior"),
        ("ADMIN", "Administrador"),
    )

    """Mult-tenant"""
    HOST_LIST = (("ATIVOS", "Ativos Precatórios e investimentos"), ("IQBROKER", "IQ Investimentos S.A"))

    role = models.CharField(max_length=100, choices=JOB_ROLES, default="JUNIOR")

    host = models.CharField(max_length=100, choices=HOST_LIST, default="ATIVOS")

    def __str__(self):
        return f"{self.username} investidor {self.role}"
