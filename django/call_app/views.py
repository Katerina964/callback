from django.shortcuts import render
from django.utils import timezone,dateformat
from django.core.paginator import Paginator
from .models import Crmaccount, Call, Customer
from .forms import CrmaccountForm
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
import json
import requests


AUTHORIZATION_TOKEN = 'Bearer NDFjNjE3ODJkYjg0MDhjNTMzMDlkNDg3ZjRlOGE5NTU2ODk0MmI3ZGRmYTAxYjU4MTgxMzkyMjZkOGJlNmFjOA'


def index(request):

    crmaccount_list = Crmaccount.objects.all()
    form = CrmaccountForm()

    # url = "https://webhook.site/988dd30f-da87-4136-b930-8e51c1de9adc"
    # response = requests.post(url, json={'msg': 'Hello world'})
    # response.json()
    return render(request, 'call_app/index.html', {'crmaccount_list': crmaccount_list, "form":form})
    # return HttpResponse("Index page")


@csrf_exempt
def deal_result(request):
    if request.method == 'GET':
        return HttpResponse("deal result page")
    elif request.method == 'POST':
        payload = json.loads(request.body)

        deal_id = payload['data']['deal']['Id']
        result = payload['data']['deal']['result']

        url = f"https://mp72700630.megaplan.ru/api/v3/deal/{deal_id}/"
        headers = {
          'Authorization': AUTHORIZATION_TOKEN
        }
        data = {"Category1000060CustomFieldRezultatZvonka": result }
        response = requests.post(url, headers=headers, json=data)
        return JsonResponse(response.json())


@csrf_exempt
def webhook_input(request):
    if request.method == "GET":
        return HttpResponse("webhook page")
    elif request.method == "POST":
        webhook =json.loads(request.body)
        deal_id = webhook['data']['deal']['Id']
    # def cart(deal_id):
        # url = f"https://mp72700630.megaplan.ru/api/v3/deal/{deal_id}/"
        # headers = {
        #   'Authorization': AUTHORIZATION_TOKEN
        # }
        # response = requests.get(url, headers=headers)
        # deal_data = response.json()
    with open('/django/call_app/megaplan/cart.json', 'rt') as f:
         data=json.load(f)
         tipe_of_deal = data['class']
         employee = data["data"]["deal"]["Category1000060CustomFieldVneshtatniySpetsialist"][0]["Name"]
         employee_number = data['data']["deal"]["Name"]
         customer_number  = data["data"]["deal"]["Manager"]['phone']
         customer_surname = data['data']["deal"]["Contractor"]["Id"]

    customer = Customer(surname=customer_surname)
    customer.save()

    call = Call.objects.create(deal_id_megaplan=deal_id,
         tipe_of_deal=tipe_of_deal, employee=employee,
         customer=customer,
         employee_number=employee_number,
         customer_number=customer_number)
    data_ats =" id_звонка  "  + str(call.id)+"\nсотрудник  " + str(employee_number) + "\nклиент  " + str(customer_number ) + '\n'

    with open(f'/django/call_app/ats/{call.id}.txt', 'w') as f:
        f.write( data_ats)
    return JsonResponse({'deal_id': deal_id} )


def calls(request):
    call_list = Call.objects.all()
    return render(request, 'call_app/calls.html', {'call_list': call_list})
