from django.apps import AppConfig


class MysiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mysite'

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forum'
    verbose_name = 'Пользователи'
    label = 'Пользователи'
