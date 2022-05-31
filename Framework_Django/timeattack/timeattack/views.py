from django.shortcuts import render, redirect
from .models import UserModel
import hashlib

def sign_up_view(request):
    if request.method == 'GET':
        print('===여기1')

        return render(request, 'index.html')
    elif request.method=='POST':
        print('===여기2')
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        
        hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()

        exist_user = UserModel.objects.filter(email=email) # 유저 존재하는지 체크
        if exist_user:
            return render(request, 'index.html')  # 사용자가 존재하기 때문에 회원가입 페이지를 다시 띄움
        else:
            try:
                new_user = UserModel()
                new_user.email = email
                new_user.password = hashed_pw
                new_user.save()
                print('성공!')
                return redirect('/')
            except:
                return render(request, 'index.html', context ={'status':'400', 'reason' : "email 형식이 아니거나 비밀번호가 맞지 않습니다."})
