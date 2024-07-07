# inventario/views.py

from django.shortcuts import render, redirect
from .forms import InventarioForm

def ingresar_inventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventario_success')
    else:
        form = InventarioForm()
    return render(request, 'ingresar_inventario.html', {'form': form})

def inventario_success(request):
    return render(request, 'inventario_success.html')
