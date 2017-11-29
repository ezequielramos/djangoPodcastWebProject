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
def usuarios(request, userId=None):

	request.session['something'] = True

	print("sessao")
	print(request.session.get('something',False))

	return rest(request,Usuario,userId)

@csrf_exempt
def categorias(request, categoryId=None):
	return rest(request,Categoria,categoryId)

@csrf_exempt
def jingles(request, jingleId=None):
	#return rest(request,Jingle,jingleId)

	# Handle file upload
	if request.method == 'POST':

		parameters = {}

		for naosei in request.POST:
			parameters[naosei] = request.POST[naosei]

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
				'usuario_id':model_object.usuario_id,
				'jautor':model_object.jautor,
				'texto':model_object.texto
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
					'usuario_id':model_object.usuario_id,
					'jautor':model_object.jautor,
					'texto':model_object.texto
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