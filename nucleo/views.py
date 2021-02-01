from django.shortcuts import render, HttpResponse

# Create your views here.

html_base = '''
<h1>mi restaurante</h1>
<ul>
    <li><a href='/'>Portada</a></li>
    <li><a href= '/about-me/'>Acerca de</a></li>
    <li><a href= '/carta/'>Carta</a></li>
    <li><a href= '/blog/'>Blog</a></li>
    <li><a href= '/contacto/'>Contacto</a></li>
</ul>
'''
# EN EL SE DEFINEN LAS VISTAS DE LA APP

def home(request):
    return render(request, 'nucleo/home.html')

def about(request):
    return render(request, 'nucleo/about.html')

def carta(request):
    return render(request, 'nucleo/carta.html')

def blog(request):
    return render(request, 'nucleo/blog.html')

def contacto (request):
    return render(request, 'nucleo/contacto.html')
