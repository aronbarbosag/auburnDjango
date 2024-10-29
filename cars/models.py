from django.db import models

# Create your models here.


class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Car(models.Model):
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name='modelo_carro')
    modelo = models.CharField(max_length=100)
    OPCOES_CAMBIO = (
        ('Automático', 'Automático'),
        ('Manual', 'Manual'),
    )
    cambio = models.CharField(max_length=100, choices=OPCOES_CAMBIO)
    OPCOES_COMBUSTÍVEL = (
        ('Flex', 'Flex'),
        ('Gasolina', 'Gasolina'),
        ('Gasolina e Gás', 'Gasolina e Gás'),
        ('Flex e Gás', 'Flex e Gás'),
        ('Elétrico', 'Elétrico'),
        ('Híbrido', 'Híbrido'),
    )
    combustivel = models.CharField(max_length=100, choices=OPCOES_COMBUSTÍVEL)
    quilometragem = models.IntegerField()
    preco = models.FloatField()
    ano_fabrica = models.IntegerField()
    ano_lancamento = models.IntegerField()
    foto_carro = models.ImageField(upload_to='cars/')
    motor = models.FloatField(default=1.0, max_length=2)

    def __str__(self):
        return self.modelo
