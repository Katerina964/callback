from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'call_app'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('deal_result', views.deal_result, name='deal_result'),
    path('webhook_input', views.webhook_input, name='webhook_input'),
    path('calls', views.calls, name='calls'),
]
