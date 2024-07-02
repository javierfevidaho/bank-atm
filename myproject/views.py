from django.shortcuts import render

def atm_view(request):
    return render(request, 'atm.html')
