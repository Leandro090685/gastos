from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.db.models import Sum
from gastos.models import Gasto, Rubro
from . import forms
import gastos

def index(request):
    return render(request,"index.html")
    
    
def nuevo_gasto(request):
    if request.method == "POST":
        form= forms.FormularioGasto(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect (reverse("nuevo_gasto"))
    else:
        form = forms.FormularioGasto
    ctx = {"form":form}
    return render(request,"nuevo_gasto.html",ctx)

def nuevo_rubro(request):
    if request.method == "POST":
        form= forms.FormularioRubro(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect (reverse("nuevo_rubro"))
    else:
        form = forms.FormularioRubro
    todos = Rubro.objects.all()
    ctx = {"form":form,"todos":todos}
    return render(request,"nuevo_rubro.html",ctx)
    
def ver_gastos(request):
    gastos = Gasto.objects.all()
    total = Gasto.objects.aggregate(total_importe=Sum("importe"))
    ctx={"gastos": gastos,"total": total}
    return render(request,"ver_gastos.html",ctx)

def eliminar_gasto(request, id):
    gasto = Gasto.objects.get(id=id)
    gasto.delete()
    return redirect ("/gastos")

def eliminar_rubro(request, id):
    rubro = Rubro.objects.get(id=id)
    rubro.delete()
    return redirect ("/gastos")

    
    





    


    