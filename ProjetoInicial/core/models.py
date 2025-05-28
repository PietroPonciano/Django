from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length= 100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Quantidade no estoque')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length = 100)
    email = models.EmailField('email', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome} '
