from django.shortcuts import render, redirect

# Create your views here.

def login_view(request):
    if request.method=='GET':
        return render(request, 'login.html')
    elif request.method=='POST':
        user_email = request.POST.get('user_email', '')
        password = request.POST.get('password', '')
        return redirect('/main')
