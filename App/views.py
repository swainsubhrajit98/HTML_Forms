from django.shortcuts import render

# Create your views here.
from App.models import *
from django.http import HttpResponse


def Insert_Topic(request):

    if request.method == 'POST':
        tn = request.POST['topic']
        # tn = request.POST.get('topic')
        T = Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('Topic is Inserted successfully!!!')
    return render(request, 'Insert_Topic.html')


def Insert_Webpage(request):
    topics = Topic.objects.all()
    d = {'topics': topics}
    if request.method == 'POST':
        to = request.POST['to']
        na = request.POST['na']
        ur = request.POST['ur']
        T = Topic.objects.get_or_create(topic_name=to)[0]
        T.save()
        W = Webpage.objects.get_or_create(topic_name=T, name=na, url=ur)[0]
        W.save()
        return HttpResponse('Webpage is Inserted Successfully!!!')
    return render(request, 'Insert_Webpage.html', d)


def Insert_Access(request):

    topics = Topic.objects.all()
    d = {'topics': topics}
    if request.method == 'POST':
        to = request.POST['to']
        na = request.POST['na']
        ur = request.POST['ur']
        da = request.POST['da']
        T = Topic.objects.get_or_create(topic_name=to)[0]
        T.save()
        W = Webpage.objects.get_or_create(topic_name=T, name=na, url=ur)[0]
        W.save()
        A = AccessRecords.objects.get_or_create(name=W, date=da)[0]
        A.save()
        return HttpResponse('AccessRecords is Inserted Successfully!!!')
    return render(request, 'Insert_Access.html', d)


def Display_Topic(request):
    LTO = Topic.objects.all()
    d = {'LTO': LTO}
    return render(request, 'Display_Topic.html', d)


def Display_Webpage(request):
    LWO = Webpage.objects.all()
    d = {'LWO': LWO}
    return render(request, 'Display_Webpage.html', d)


def Display_Access(request):
    LARO = AccessRecords.objects.all()
    d = {'LARO': LARO}
    return render(request, 'Display_Access.html', d)


def Select_Topic(request):
    topics = Topic.objects.all()
    d = {'topics': topics}

    if request.method == 'POST':
        tn = request.POST.getlist('topic')
        print(tn)
        webpages = Webpage.objects.none()
        for i in tn:
            webpages = webpages | Webpage.objects.filter(topic_name=i)
        data = {'webpages': webpages}
        return render(request, 'Display_Webpage.html', data)
    return render(request, 'Select_Topic.html', d)


def Checkbox(request):
    topics = Topic.objects.all()
    d = {'topics': topics}
    return render(request, 'Checkbox.html', d)
