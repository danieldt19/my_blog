from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

class HelloWorld(View):
    def get(self,request):
        data = {
            'name':'Daniel',
            'years': 28,
            'codes': {'Python','Django','React','Node'}
         }
        return render(request, 'hello_world.html',context = data)
