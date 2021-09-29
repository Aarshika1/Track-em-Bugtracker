from django.shortcuts import render, redirect, reverse
from .models import Bug
from projects_app.models import Project
from .forms import AddBugForm
from .filters import BugFilter
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def list_bugs(request,id):
    query_bugs = Bug.objects.filter(project_id=id)
    project = Project.objects.filter(id = id)[0]
    Filter = BugFilter(request.GET, queryset = query_bugs)
    query_bugs = Filter.qs

    context = {
        'bugs_list': query_bugs,
        'project': project,
        'Filter': Filter
    }
    return render(request, 'bugs_app/bugs.html', context)

@login_required(login_url='login')
def bug_add(request,project_id):
    if request.method == "POST":
        form = AddBugForm(request.POST)
        if form.is_valid():
            project = Project.objects.filter(id=project_id)[0]

            bug = form.save(commit = False)
            bug.project_id = project
            bug.save()
            a = reverse('bug_list', args=[project_id])
            
            return redirect(a)
            
    else:
        form = AddBugForm()
        
    context = {
        'form': form
    }

    return render(request,'bugs_app/addbugs.html', context)

@login_required(login_url='login')
def bug_delete(request,project_id,bug_id):
    project = Project.objects.filter(id = project_id)[0]
    bug = Bug.objects.filter(project_id = project,id = bug_id)[0]
    bug.delete()
    return redirect(reverse('bug_list', args=[project_id]))

@login_required(login_url='login')
def bug_update(request,project_id, bug_id):
    project = Project.objects.get(id=project_id)
    bug = Bug.objects.get(project_id=project,id=bug_id)
    if request.method == "POST":
        form = AddBugForm(request.POST, instance=bug)
        if form.is_valid():
            project = Project.objects.filter(id=project_id)[0]

            bug = form.save(commit = False)
            bug.project_id = project
            bug.save()
            a = reverse('bug_list', args=[project_id])
            
            return redirect(a)
            
    else:
        form = AddBugForm()
    form = AddBugForm(instance=bug)
    context = {
        'form': form
    }
    return render(request,'bugs_app/addbugs.html', context)

@login_required(login_url='login')
def bug_view(request,project_id, bug_id):
    project = Project.objects.get(id=project_id)
    bug = Bug.objects.get(project_id=project,id=bug_id)
    if request.method == "GET":
        form = AddBugForm(request.GET, instance=bug)
       
    else:
        form = AddBugForm()
    form = AddBugForm(instance=bug)
    context = {
        'form': form
    }
    return render(request,'bugs_app/viewbugs.html', context)

@login_required(login_url='login')
def profile(request):
    bugs = Bug.objects.filter(assigned_user = request.user)
    context ={
        'bugs' : bugs
    }
    return render(request, 'bugs_app/profile.html', context)