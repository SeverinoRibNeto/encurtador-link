from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FormLinks
from .models import Links


def home(request):
    form = FormLinks()
    status = request.GET.get('status')
    return render(request, 'home.html', {'form': form, 'status': status})


def encurtar_link(request):
    form = FormLinks(request.POST)
    link_encurtado = form.data['link_encurtado']
    links = Links.objects.filter(link_encurtado=link_encurtado)
    if (len(links) > 0):
        return redirect('/?status=1')  # Status 1 = Link já existe

    if (form.is_valid()):
        try:
            form.save()
            return HttpResponse(f"Seu link foi criado com sucesso! Para acessar,acesse: http://127.0.0.1:8000/{link_encurtado}")
        except Exception as e:
            return HttpResponse("Erro interno do sistema: "+e)


def redirecionador_de_link(request, link_recebido):
    link = Links.objects.filter(link_encurtado=link_recebido)
    if len(link) == 0:
        return redirect("/?status=2")  # Link digitado não existe
    link_original = link[0].link_original
    return redirect(link_original)
