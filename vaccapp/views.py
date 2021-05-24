from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import requests
# Create your views here.


class HomePage(TemplateView):
    def get(self, request):
        return render(request,'index.html')


class VacSlots(TemplateView):

    def post(self, request):
        date = request.POST['date']
        pincode = request.POST['pincode']
        pparams = {"pincode": pincode, "date": date}
        url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin/"
        response = requests.get(url, params=pparams, headers={"Accept-Language": "hi_IN"})
        if response.status_code == 200:
            response = response.json()
        else:
            print(f"Response Status {response}")
        print(response.text)
        return render(request, 'vacslots.html')




