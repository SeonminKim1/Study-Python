from django.shortcuts import render
from django.http import JsonResponse

import json

def score_func(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        score = int(json.loads(request.body)['score'])
        print('받은 score 데이터', score)
        if score >= 70:
            msg = '합격'
        else:
            msg = '불합격'
        return JsonResponse({'msg': msg})