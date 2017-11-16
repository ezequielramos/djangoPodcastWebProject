from django.db import models

class Usuario(models.Model):
	login = models.CharField(max_length=20)
	nome = models.CharField(max_length=60)
	senha = models.CharField(max_length=32)
	email = models.CharField(max_length=60)

class Categoria(models.Model):
	nome = models.CharField(max_length=20)

class Jingle(models.Model):
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	jnome = models.CharField(max_length=60)
	jautor = models.CharField(max_length=60)
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	texto = models.CharField(max_length=500)

class Voto(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	jingle = models.ForeignKey(Jingle, on_delete=models.CASCADE)

class Favorito(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	jingle = models.ForeignKey(Jingle, on_delete=models.CASCADE)

class Mensagem(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	jingle = models.ForeignKey(Jingle, on_delete=models.CASCADE)
	comentario = models.CharField(max_length=500)