


from django.http import HttpResponse

def fbv_view(request):
    if request.method =='GET':
        return HttpResponse('FBV View - GET 입니다')
    
    elif request.method =='POST':
        return HttpResponse('FBV View - POST 입니다')

from django.views import View
class cbv_view(View):
    def get(self ,request):
        return HttpResponse('CBV View - GET 입니다')
    def post(self, request):
        return HttpResponse('CBV View - POST 입니다')