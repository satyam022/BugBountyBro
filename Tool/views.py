import ipapi

from django.shortcuts import render


# Create your views here.

def IP_Finder(request):
    search = request.POST.get('search')

    data = ipapi.location(ip=search, output='json')

    context = {"data": data}
    return render(request, 'tool/ipfinder.html', context)



