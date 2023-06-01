# from django.shortcuts import render
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Tool, Topic, Message, Project
# from .forms import ToolForm

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User with the credentials does not exist')
    context = { 'page': page }
    return render(request, 'base/views/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

# def registerUser(request):
#     form = UserCreationForm()

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Ann error occured during registration')
#     context = { 'form': form }
#     return render(request, 'base/views/login_register.html', context)

def home(request):
    context = {}
    return render(request, 'base/views/home.html', context)

def tools(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    skills = Tool.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    ).reverse()
    topics = Topic.objects.all()
    skill_count = skills.count()
    skill_messages = Message.objects.filter(Q(tool__topic__name__icontains=q))
    context = { 
        'skills': skills, 
        'topics': topics, 
        'skill_count': skill_count,
        'skill_messages': skill_messages
    }
    return render(request, 'base/views/tools.html', context)

def projects(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    projects = Project.objects.filter(
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    skill_count = projects.count()
    skill_messages = Message.objects.filter(Q(tool__topic__name__icontains=q))

    context = { 
        'skills': projects, 
        'topics': topics, 
        'skill_count': skill_count,
        'skill_messages': skill_messages
    }
    return render(request, 'base/views/projects.html', context)

# def tool(request, pk):
#     skill = Tool.objects.get(id=pk)
#     tool_messages = skill.message_set.all().order_by('-created')
#     participants = skill.participants.all()
#     if request.method == 'POST':
#         message = Message.objects.create(
#             user = request.user,
#             skill = skill,
#             body = request.POST.get('body')
#         )
#         skill.participants.add(request.user)
#         return redirect('skill', pk=skill.id)
#     context = { 'skill': skill, 'skill_messages': tool_messages, 'participants': participants }
#     return render(request, 'base/views/skill.html', context)

# def userProfile(request, pk):
#     user = User.objects.get(id=pk)
#     skills = user.skill_set.all()
#     skill_messages = user.message_set.all()
#     topics = Topic.objects.all()
#     context = { 
#         'user': user, 
#         'skills': skills, 
#         'skill_messages': skill_messages,
#         'topics': topics
#     }
#     return render(request, 'base/views/profile.html', context)

# @login_required(login_url='login')
# def createTool(request):
#     form = ToolForm
#     if request.method == 'POST':
#         form = ToolForm(request.POST)
#         if form.is_valid():
#             skill = form.save(commit=False)
#             skill.host = request.user
#             skill.save()
#             return redirect('home')
#     context = { 'form': form }
#     return render(request, 'base/components/skill_form.html', context)

# @login_required(login_url='login')
# def updateTool(request, pk):
#     skill = Tool.objects.get(id=pk)
#     form = ToolForm(instance=skill)

#     if request.user != skill.host:
#         return HttpResponse('You are not allowed here!!')

#     if request.method == 'POST':
#         form = ToolForm(request.POST, instance=skill)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     context = { 'form': form }
#     return render(request, 'base/skill_form.html', context)

# @login_required(login_url='login')
# def deleteTool(request, pk):
#     skill = Tool.objects.get(id=pk)

#     if request.user != skill.host:
#         return HttpResponse('You are not allowed here!!')

#     if request.method == 'POST':
#         skill.delete()
#         return redirect('home')
#     return render(request, 'base/components/delete.html', { 'obj': skill })

# @login_required(login_url='login')
# def deleteMessage(request, pk):
#     message = Message.objects.get(id=pk)

#     if request.user != message.user:
#         return HttpResponse('You are not allowed here!!')

#     if request.method == 'POST':
#         message.delete()
#         return redirect('home')
#     return render(request, 'base/components/delete.html', { 'obj': message })
