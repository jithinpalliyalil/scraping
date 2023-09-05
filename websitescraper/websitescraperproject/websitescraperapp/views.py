from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import links
def home(request):
    if request.method == "POST":
        link_new=request.POST.get('page', '')
        urls = requests.get(link_new)
        beautisoup = BeautifulSoup(urls.text, 'html.parser')

        for link in beautisoup.find_all('a'):
            li_address = link.get('href')
            li_name = link.string
            links.objects.create(address=li_address, stringname=li_name)
        return HttpResponseRedirect('/')
    else:
     data_values = links.objects.all()
    return render(request, 'home.html', {'data_values': data_values})