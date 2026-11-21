# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Activity
from .forms import ActivityForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import models
def hello(request):
    query = request.GET.get('q', '')
    
    if query:
        activities = Activity.objects.filter(
            models.Q(title__icontains=query)#按标题过滤活动
        )
    else:
        activities = Activity.objects.all()
        
    context = {
        "title": "活动列表", 
        "activities": activities,
        "query": query,  
    }
    return render(request, template_name="hello_list.html", context=context)
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('hello') 
    # 如果 GET 请求，或者 POST 但验证失败，都渲染登录页
    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect('login') 

@login_required
def add(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hello') 
    else:
        form = ActivityForm()
    return render(request, "hello_forms.html", {"form": form}) 

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

@login_required
def delete_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    if request.method == "POST":
        activity.delete()
        return redirect('hello')
    return redirect('hello')

# 确保顶部有这行导入
# from django.shortcuts import render, redirect, get_object_or_404

@login_required
def edit_activity(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    
    if request.method == "POST":
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('hello')
    else:
        form = ActivityForm(instance=activity)
    return render(request, "hello_forms.html", {"form": form})