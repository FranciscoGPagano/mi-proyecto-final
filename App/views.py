from django.shortcuts import render
from App.models import Familiar
from App.forms import Buscar, FamiliarForm
from django.views import View

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

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "App/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'App/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})

    
class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'App/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})