@csrf_exempt
def webhook(request):
    if request.method == 'GET':
        return HttpResponse("webhook page")
    elif request.method == 'POST':
        payload = json.loads(request.body)
        deal_id = payload['data']['deal']['Id']
        url = f"https://mp72700630.megaplan.ru/api/v3/deal/{deal_id}/"
        headers = {
          'Authorization': AUTHORIZATION_TOKEN
        }
        response = requests.get(url, headers=headers)
        deal_data = response.json()
        print(json.dumps(deal_data))
        contractor_phone = deal_data['data']['contractorPhone']['value']
        roles = deal_data['data']['program']['roles']
        def role_filter(role):
            try:
                linkedField = role['linkedField']
                return linkedField is not None and linkedField['hrName'] == 'Внештатный специалист'
            except KeyError:
                return False
        freelancer_field = list(filter(role_filter, roles))[0]['linkedField']['name']
        freelancer_contacts = deal_data['data'][freelancer_field][0]['contactInfo']
        def contract_info_filter(info):
            return info['type'] == 'phone'
        freelancer_phone = list(filter(contract_info_filter, freelancer_contacts))[0]['value']

        return JsonResponse({'freelancer': freelancer_phone, 'contractor': contractor_phone, 'deal_id':deal_id}, safe=False)
