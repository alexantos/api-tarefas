from django.db import models


class Tarefa(models.Model):
    descricao = models.CharField(max_length=64)
    data = models.DateField(auto_now_add=True)
    realizado = models.BooleanField(default=False)
    prioridade = models.CharField(max_length=16)
