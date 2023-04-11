from django.shortcuts import render,redirect
from .models import BlogModel
from .forms import BlogForm
# Create your views here.


def home(request):

    blog = BlogModel.objects.all()

    context = {"blog":blog}
    return render(request, 'home.html', context)



def DashBoard(request):


    blog = BlogModel.objects.all()

    context = {"blog":blog}

    return render(request, 'dashboard.html' , context)



def addblog(request):
    forms = BlogForm()
    if request.method == 'POST':
        forms = BlogForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard')
    context = {'forms':forms} 
    return render(request, 'addblog.html' , context)




def deleteblog(request , id):
    blog = BlogModel.objects.get(id =id ) #right side id itsa optional id u can change id = pk, name. anything

    blog.delete()
    return redirect('dashboard')


def updateblog(request, id):
    blog = BlogModel.objects.get(id =id ) #right side id itsa optional id u can change id = pk, name. anything

    context = {"blog":blog}
    return render(request, 'update.html' , context)

