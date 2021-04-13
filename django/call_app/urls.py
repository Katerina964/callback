from django.urls import path

from . import views

app_name = 'call_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('deal_result', views.deal_result, name='deal_result'),
    path('webhook_input', views.webhook_input, name='webhook_input'),
    path('calls', views.calls, name='calls'),
]
