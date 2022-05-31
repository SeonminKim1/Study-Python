from django.shortcuts import render

# Create your views here.
def app_render_view(request):
    return render(request, 'app_base.html')


# Create your views here.
def app_render_view2(request):
    return render(request, 'app_base2.html')