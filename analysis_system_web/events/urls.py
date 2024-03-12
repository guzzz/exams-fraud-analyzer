
from django.urls import path
from django.shortcuts import redirect

from .views import *

urlpatterns = [
    path('error/', ErrorTemplateView.as_view(), name='error'),
    path('register-event/', EventCreateView.as_view(), name='register-event'),
    path('processed-result/<int:pk>/', ProcessedTemplateView.as_view(), name='processed-page'),
    path('', lambda req: redirect('/register-event/')),
]
