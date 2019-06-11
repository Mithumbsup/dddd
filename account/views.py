from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import views 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == "POST": # POST 방식이라면
        userform = CreateUserForm(request.POST) # 웹페이지에서 폼에 값을 받아
        print(userform.is_valid())
        if userform.is_valid():# 폼의 내용이 양식에 맞는 지 확인후에, 오류메세지보내기
            userform.save() # userform을 데이터베이스에 저장!
            return redirect('home') # 처음페이지로 보내주기!
    elif request.method =='GET': # 만약 폼 내용이 맞지않는다면, 
        userform = CreateUserForm() 

    return render(request, 'registration/signup.html',{"userform":userform})


# def login(request):
#     print(11111111)
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=username, password=password)
#         print(22222)
#         if user is not None:
#             print(3333)
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'registration/login.html', {'error':'username or password is incorrect'})
#     else:
#         return render(request, 'registration/login.html')


# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         return redirect('home')
#     return render(request, 'registration/login.html')










