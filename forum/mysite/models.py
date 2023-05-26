from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils import timezone

class Organisation(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование")
    mail = models.CharField(max_length=50, verbose_name="Почта")

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return '%s %s'%(self.name, self.mail)


class Types (models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование категории")
    organistaion = models.ForeignKey(Organisation, on_delete=models.CASCADE, verbose_name="Организация", null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return '%s'%(self.name)


"""class Role (models.Model):
    name = models.CharField(max_length=20, verbose_name="Наименование роли")

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'"""


class Person (AbstractUser):
    #role = models.ForeignKey( 'Role', on_delete=models.CASCADE)
    patron = models.CharField(max_length=20, verbose_name="Отчество", blank=True, null=True)
    number = models.IntegerField(verbose_name="Номер", null=True, blank=True)
    email = models.CharField(max_length=50, verbose_name="Почта", blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Request (models.Model):
    first_name = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name="Пользователь")
    theme = models.CharField(max_length=50, verbose_name="Тема запроса")
    type = models.ForeignKey('Types', on_delete=models.CASCADE, verbose_name="Категория запроса")
    datetime = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200, verbose_name="Текст запроса")
    adress = models.CharField(max_length=200, verbose_name="Адресс")
    img = models.ImageField(verbose_name="Фото", null=True, blank=True, upload_to='images/', default='default.jpg')
    on_del = models.BooleanField(verbose_name="Статус удаления пользователем", default=False)


    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-datetime']

    def __str__(self):
        return "Пользователь: {}, Описание: {}".format(self.first_name, self.text)
    
    @property
    def getStatus(self):
        return Status.objects.filter(request=self.pk)





class Status(models.Model):
    request = models.ForeignKey('Request', on_delete=models.CASCADE, verbose_name='Заявка',)
    category = models.ForeignKey('Category', verbose_name='Тип статуса', on_delete=models.CASCADE, default='0')
    datetime = models.DateTimeField(verbose_name='Время запроса', auto_now_add=True)
    text = models.CharField(max_length=200, verbose_name="Описание статуса", null=True)

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="Статус")

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name

