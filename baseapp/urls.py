
from django.urls.conf import path

from django.urls import path

from baseapp.views import BaseView



urlpatterns = [
    path('base', BaseView.as_view(), name='base'),
]

