from django.shortcuts import render

def home(request):
    return render(request, 'index2.html')

def profile(request):
    return render(request, 'profile.html')

def products(request):
    return render(request, 'products.html')

def tables(request):
    return render(request, 'tables.html')

def reports(request):
    return render(request, 'reports.html')

def logout(request):
    # Lógica de logout
    return render(request, 'logout.html')
