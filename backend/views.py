from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import FileUploadForm,LoginForm
from .models import FileUpload
from django.core.files.storage import default_storage
# Create your views here.

def home(request):
    allfiles = FileUpload.objects.all()

    return render(request,'home.html',{'files':allfiles})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def Login(request):
   
    if request.method == "GET":
        form = LoginForm()
        return render(request,'login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        # if not User.objects.filter(username=username).exists():
        #     return redirect('register')
        user = authenticate(username=username, password=password)

        if user is None:
            return redirect('register')
        else:
            login(request, user)
            return redirect('upload_file')
    return render(request, 'login.html',{'form':form})


def Logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def upload(request):
    if request.method == 'POST':
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                files = request.FILES.getlist('file')

                for file in files:
                    if file.size > 20000000 :
                      return HttpResponse('filesize must be less than 20MB')
                    FileUpload.objects.create(file=file, user=request.user)

                return redirect('home')
    else:
        form = FileUploadForm()
    return render(request, 'fileupload.html', {'form': form ,'User':User})


@login_required(login_url="login")
def f_delete(request,id):
    obj = FileUpload.objects.get(id = id)
    allfiles = FileUpload.objects.all()

    temp=str(request.user.username) 
    temp1=str(obj.user)
    print(temp,temp1)
    if temp == temp1:
        media_path = obj.file.path
        obj.delete()
        if default_storage.exists(media_path):
            default_storage.delete(media_path)
    else:
        return render(request,'home.html',{'files':allfiles,'message':'You have no right to remove this file'})
    # f = FileUpload.objects.get(id=id)
    # f.delete()
    return redirect('home')
