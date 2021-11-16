
from django.urls.conf import path

from django.urls import path

from baseapp.views import BaseView



urlpatterns = [
    path('', BaseView.as_view(), name='base'),
]

