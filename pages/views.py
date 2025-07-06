import requests
from django.http import HttpResponse
from django.shortcuts import render


# def get_currency_data():
#     url ="https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
#     response = requests.get(url=url)
#     if response:
#         return response.json()
#     return None
#
#
# def currency_data_view(request):
#     res = get_currency_data()
#     if res is None:
#         return HttpResponse("Malumot topilmadi.")
#     data = {
#         "data" : res
#     }
#     return render(request=request, template_name="index.html", context=data)


def home_view(request):
    return render(request=request, template_name='index.html')

def about_view(request):
    return render(request=request, template_name='about.html')

def contact_view(request):
    return render(request=request, template_name='about.html')