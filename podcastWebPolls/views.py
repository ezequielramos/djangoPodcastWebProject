from django.http import HttpResponse
from django.shortcuts import render
from podcastWebPolls.models import *
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json
import os

def webpage(request, webpage):
	return render(
		request,
		webpage + '.html'
	)

def rest(request, model, model_id):

	if request.method == 'POST':
		data = json.loads(request.body.decode('utf-8'))

		u = model(**data)
		u.save()

		return HttpResponse('{"success":true}', content_type="application/json")

	elif request.method == 'GET':

		if model_id:
			model_object = model.objects.get(pk=model_id)
			retorno = model_to_dict(model_object)
		else:
			retorno = []

			for model_object in model.objects.all():
				retorno.append(model_to_dict(model_object))

		return HttpResponse(json.dumps(retorno), content_type="application/json")

	elif request.method == 'DELETE':

		if not model_id:
			return HttpResponse('{"success":false, "message":"nao foi enviado id para o delete"}', content_type="application/json", status=400)
		else:

			model_object = model.objects.get(pk=model_id)
			model_object.delete()

			return HttpResponse('{"success":true}', content_type="application/json")

@csrf_exempt
def logout(request):
	request.session['user'] = 0
	return HttpResponse('{"success":true}', content_type="application/json")

@csrf_exempt
def login(request):

	if request.method == 'POST':
		usuarios = Usuario.objects.all()

		data = json.loads(request.body.decode('utf-8'))	

		try:
			usuario = usuarios.filter(login=data["login"],senha=data["senha"])[0].id

			request.session['user'] = usuario

			return HttpResponse('{"success":true, "id":' + str(usuario) + '}', content_type="application/json")
		except:
			return HttpResponse('{"success":false, "message":"Usuario nao valido ou senha incorreta."}', content_type="application/json", status=400)
	elif request.method == 'GET':
		return HttpResponse('{"success":true, "id":' + str(request.session.get('user',0)) + '}', content_type="application/json")

@csrf_exempt
def usuarios(request, userId=None):
	return rest(request,Usuario,userId)

@csrf_exempt
def categorias(request, categoryId=None):
	return rest(request,Categoria,categoryId)

@csrf_exempt
def favorito(request, favoritoId=None):

	if request.method == 'POST':
		data = json.loads(request.body.decode('utf-8'))

		u = Favorito(**data)
		u.save()

		return HttpResponse('{"success":true}', content_type="application/json")

	elif request.method == 'GET':

		if favoritoId:
			favoritos = Favorito.objects.all()
			favoritos = favoritos.filter(usuario_id=request.session.get('user',0), jingle_id=favoritoId)

			retorno = {"id":0}

			for favorito in favoritos:
				retorno = model_to_dict(favorito)

		else:
			retorno = []

			for model_object in Favorito.objects.all():
				retorno.append(model_to_dict(model_object))

		return HttpResponse(json.dumps(retorno), content_type="application/json")

	elif request.method == 'DELETE':

		if not favoritoId:
			return HttpResponse('{"success":false, "message":"nao foi enviado id para o delete"}', content_type="application/json", status=400)
		else:

			model_object = Favorito.objects.get(pk=favoritoId)
			model_object.delete()

			return HttpResponse('{"success":true}', content_type="application/json")

@csrf_exempt
def jingles(request, jingleId=None):
	#return rest(request,Jingle,jingleId)

	# Handle file upload
	if request.method == 'POST':

		parameters = {}

		for eachPost in request.POST:
			parameters[eachPost] = request.POST[eachPost]

		parameters['usuario_id'] = request.session.get('user',0)

		newdoc = Jingle(**parameters, docfile=request.FILES['docfile'])
		newdoc.save()

		# Redirect to the document list after POST
		return render(
			request,
			'index.html'
		)

	elif request.method == 'GET':

		if jingleId:
			model_object = Jingle.objects.get(pk=jingleId)
			retorno = {
				'id':model_object.id,
				'jnome':model_object.jnome,
				'url':model_object.docfile.url,
				'categoria_id':model_object.categoria_id,
				'categoria': model_object.categoria.nome,
				'usuario_id':model_object.usuario_id,
				'jautor':model_object.jautor,
				'texto':model_object.texto,
				'favoritos': len(Favorito.objects.filter(jingle_id=model_object.id))
			}
		else:
			retorno = []

			for model_object in Jingle.objects.all():
				#retorno.append(model_to_dict(model_object))
				retorno.append({
					'id':model_object.id,
					'jnome':model_object.jnome,
					'url':model_object.docfile.url,
					'categoria_id':model_object.categoria_id,
					'categoria': model_object.categoria.nome,
					'usuario_id':model_object.usuario_id,
					'jautor':model_object.jautor,
					'texto':model_object.texto,
					'favoritos': len(Favorito.objects.filter(jingle_id=model_object.id))
				})

		return HttpResponse(json.dumps(retorno), content_type="application/json")

	elif request.method == 'DELETE':

		if not jingleId:
			return HttpResponse('{"success":false}', content_type="application/json")
		else:

			model_object = Jingle.objects.get(pk=jingleId)

			if model_object.docfile:
				if os.path.isfile(model_object.docfile.path):
					try:
						os.remove(model_object.docfile.path)
					except PermissionError:
						return HttpResponse('{"success":false,"message":"arquivo em uso"}', content_type="application/json", status=500)

			model_object.delete()

			return HttpResponse('{"success":true}', content_type="application/json")