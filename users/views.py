from django.shortcuts import render


def my_profile(request):
    return render(request=request, template_name="index.html")


def my_teacher(request):
    return render(request=request, template_name="teacher.html")