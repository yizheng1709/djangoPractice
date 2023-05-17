from django.shortcuts import render

def home(request):
    context = {'name': 'Customer'}
    return render(request, 'hello/home.html', context)

def pets(request):
    context = {'pets': 'No pets atm, sadge'}
    return render(request, 'hello/pets.html', context)
