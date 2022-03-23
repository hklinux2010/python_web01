import json
import re
import requests
from django.apps import AppConfig


class QqapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'QQapi'


def add(x, y):
    return x + y



