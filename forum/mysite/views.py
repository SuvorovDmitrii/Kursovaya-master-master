import datetime

from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.views import View
from qsstats import QuerySetStats
from .models import *
from django.http import HttpResponse
from .forms import UserRegistrationForm, RequestCreate, EditProfileForm
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from .queryCheck import Check

# Create your views here.

#главная страница с отображением заявок
def index(request):
    reqs = Request.objects.all()
    model = Status.objects.all()
    com_ss = QuerySetStats(reqs, 'datetime') #запрос с помощью библиотеки
    p = Paginator(reqs, 3) #кол-во отображаемых заявок
    page_obj = p.page(1)
    return render(request, "index.html", context={'page_obj':page_obj, 'com_ss':com_ss})

#регистрация
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return render(request, 'registration/login.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/registration.html', {'user_form': user_form})

#создание заявки
def requestUser(request):
    if request.method == 'POST':
        request_form = RequestCreate(request.POST, request.FILES)
        # print(request.POST)
        if request_form.is_valid():
            new_request = request_form.save(commit=False)
            new_request.first_name_id = request.user.id
            new_request.save()
            Status.objects.create(
                request_id = new_request.id,
                category_id = 1,
            )
            txt = request_form.cleaned_data.get("text") #тута мы созздаем экземпляр данных формы а именно поля text
            res = Check(txt) #ну а тута мы создаем экземпляр класса с файла queryCheck
            check = res.txtCheck() #ну а тута мы вызываем функцию которая все подсчитыавет и сохранием результат
            print(check) #  ну а тута я вывожу результат в терминал
            # !!!Данные передаются в формате (Двор Водоснабжение Электричество Благоустройство Мусора Газоснабжение Человейники)

            return redirect('main')
    else:
        request_form = RequestCreate()
    return render(request, 'request_create.html', {'request_form': request_form})


#сортировка запросов в личном кабинете пользователя
class SectionView(View):

    def get(request):
        articles = Request.objects.filter().order_by('datetime')
        return render(request, 'my_orders.html', {'articles': articles})
    

    def remove(request, id):
        if request.POST:
            Request.objects.filter(pk=id, first_name=request.user).delete()
            return redirect('my_order')

#сортировка запросов в личном кабинете админа
class SectionViewAdmin(View):

    def get(self, request):
        #req = get_object_or_404(Request)
        sort = request.GET.getlist('sort')
        articles = Status.objects.all().order_by(*sort)
        print(request.GET.getlist('sort'))
        return render(
            request=request,
            template_name='registration/user_room_admin.html',
            context={
                'articles': articles
            }
        )

#таблица запросов админа
def show_orders(request):
    requests = Status.objects.all
    return render(request, 'my_orders.html', context={'requests':requests})

def getStatistic(req):
    model = Status.objects.all()
    com_ss = QuerySetStats(model, 'request')

    return render(req, 'statistic.html', context={'com_ss':com_ss})

def user_data(request):
    user_data = Person.objects.all()
    return render(request, 'my_orders.html', context={'user_data':user_data})



def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('my_order')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('my_order')
        else:
            return redirect('change_password')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'registration/change_password.html', args)

