from django.shortcuts import render
# from django.http import HttpResponse

from .forms import RegisterForm
# Create your views here.

def index(request):
    print(request.GET)
    return render(request,"home.html")
def post_request(request):
    print(request.POST)
    form = RegisterForm()
    return render(request, "register.html", {'form': form})
def my_form(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = RegisterForm()
  return render(request, 'register.html', {'form': form})