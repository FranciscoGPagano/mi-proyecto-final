from django.shortcuts import render

def index(request):
    return render(request, "App/saludar.html",
    {
        'nombre':'Francisco',
        'apellido':'Garcia Pagano'
        })

def index2(request, nombre, apellido):
    return render(request, "App/saludar.html",
    {
        'nombre': nombre,
        'apellido': apellido,
    })

def index3(request):
    return render(request, "App/saludar.html",
    {"notas": [1,2,3,4,5,6,7]}
    )

def imc(request, peso, altura):
    imc = 1
    return render(request, "App/imc.html", {"imc": imc})