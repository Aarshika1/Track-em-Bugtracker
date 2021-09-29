from django.contrib import auth
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ProjectForm, RegisterForm
from .models import Project
from bugs_app.models import Bug
from .filters import ProjectFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'projects_app/home.html', context)


@login_required(login_url='login')
def project(request):
    project_list = Project.objects.all()
    Filter = ProjectFilter(request.GET, queryset = project_list)
    project_list = Filter.qs
    page = request.GET.get('page',1)

    paginator = Paginator(project_list,3)
    try:
        project_list = paginator.page(page)
    except PageNotAnInteger:
        project_list = paginator.page(1)
    except EmptyPage:
        project_list = paginator.page(paginator.num_pages)
    context = {
        'projects': project_list, 'Filter': Filter
    }
    return render(request, 'projects_app/project.html', context)

@login_required(login_url='login')
def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project')
    else:
        form = ProjectForm()    
    
    context = {
        'form': form
    }
    return render(request, 'projects_app/add_project.html',context)

@login_required(login_url='login')
def project_delete(request,project_id):
    project = Project.objects.filter(id = project_id)[0]
    project.delete()
    return redirect('project')

@login_required(login_url='login')
def update_project(request,project_id):
    project = Project.objects.get(id=project_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project')
    else:
        form = ProjectForm()  
    form = ProjectForm(instance=project)  
    context = {
        'form': form
    }
    return render(request, 'projects_app/add_project.html',context)

@login_required(login_url='login')
def view_project(request,project_id):
    project = Project.objects.get(id=project_id)
    if request.method == "GET":
        form = ProjectForm(request.GET, instance=project)
    else:
        form = ProjectForm()  
    form = ProjectForm(instance=project)  
    context = {
        'form': form
    }
    return render(request, 'projects_app/viewproject.html',context)

def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('project')
    else:
        form = RegisterForm()
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account successfully created: '+ user)
                return redirect('login')



        context ={
            'form': form
        }
        return render(request, 'projects_app/register.html',context)

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('project')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,'Username or Password is incorrect')

        context ={}
        return render(request, 'projects_app/login.html',context)

def Logout(request):
    logout(request)
    return redirect('login')