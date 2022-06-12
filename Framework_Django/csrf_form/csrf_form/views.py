from django.shortcuts import render
from django.http import HttpResponse

def score_func(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        score = int(request.POST.get('score', 0))
        print('받은 score 데이터', score)
        if score >= 70:
            msg = '합격'
        else:
            msg = '불합격'
        return HttpResponse(msg) # or redirect