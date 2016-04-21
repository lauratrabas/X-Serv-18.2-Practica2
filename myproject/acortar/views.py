from django.shortcuts import render
from django.http import HttpResponse
from models import Url
from django.template import Context
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def acortarUrl(url):
    if("https://" in url) or ("http://" in url):
        acortar = url.split("http://")[1]
        guardar = "http://" + acortar
    return guardar

@csrf_exempt
def pagina(request):
    if request.method == "GET":
        template = get_template("pagina.html")
        lista_url = Url.objects.all()
        for url in lista_url:
            lista_url = "<li><a href=/" + str(url.id) + ">" + url.original_url + "</a>"
    elif request.method == "POST" or request.method == 'PUT':
        url = request.POST.get('url')
        url = acortarUrl(url)
        try:
            url_encontrada = Url.objects.get(original_url = url)
        except Url.DoesNotExist:
            urls=Url(original_url = url)
            urls.save()
            url_encontrada = Url.objects.get(original_url = url)
        return HttpResponse(str(url_encontrada.id))
    lista_url = Url.objects.all()
    respuesta = "<ol>"
    for elemento in lista_url:
        respuesta += '<li><a href ="'+ str(elemento.original_url) + '">'
        respuesta += str(elemento.original_url) + '</a>' + " = " + '<a href="'+ str(elemento.id) +'">' +  str(elemento.id) + '</a>'
    respuesta += "</ol>"
    template = get_template("pagina.html")
    cont = {'contenido': respuesta,}
    return HttpResponse(template.render(Context(cont)))

def redirigirUrl(request, identificador):
    try:
        url = Url.object.get(id = identificador)
        respuesta = "<html><head><meta http-equiv='refresh' content='1;"
        respuesta += "url=" + url.original_url + "'></head>" + "<body></body></html>\r\n"
    except Url.DoesNotExist:
        respuesta = "No existe esa id"
    return HttpResponse(respuesta)

def notFound(request):
    return HttpResponse("Ha ocurrido un error")
