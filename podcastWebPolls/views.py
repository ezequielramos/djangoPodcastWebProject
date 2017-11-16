from django.http import HttpResponse
from django.shortcuts import render
from podcastWebPolls.models import *
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
	return render(
		request,
		'index.html'
	)

@csrf_exempt
def usuarios(request):

	if request.method == 'POST':

		request.session['something'] = True

		data = json.loads(request.body)

		u = Usuario(**data)
		u.save()

		return HttpResponse('sucesso')

	elif request.method == 'GET':

		print("sessao")
		print(request.session.get('something',False))

		usuarios = []

		for usuario in Usuario.objects.all():
			usuarios.append(model_to_dict(usuario))

		return HttpResponse(json.dumps(usuarios), content_type="application/json")