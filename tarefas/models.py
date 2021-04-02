from django.db import models

class Tarefa(models.Model):
    descricao = models.CharField(max_length=64)
    data_criacao = models.DateField(auto_now_add=True)
    realizado = models.BooleanField(default=False)
    data_hora_realizado = models.DateTimeField(null=True, blank=True)

