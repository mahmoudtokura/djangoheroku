from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients':clients})

@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'form.html', {'form':form})
    form = ClientForm()
    return render(request, 'form.html', {'form':form})

@login_required
def update_client(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('list_clients')
        else:
            return render(request, 'form.html', {'form':form})
    
    form = ClientForm(instance=client)
    return render(request, 'form.html', {'form':form})

@login_required
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('list_clients')
    
    return render(request, 'confirm.html', {'client':client})