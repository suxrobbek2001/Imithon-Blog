from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from blogapp.models import Maqola


def LoginView(request):
    if request.method == 'POST':
        users = authenticate(username=request.POST['login'], password=request.POST['parol'])
        if users is None:
            return redirect('login')
        else:
            login(request, users)
            return redirect('blog')
    return render(request, 'login.html')


def RoyhatView(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['login'],
            password=request.POST['parol']
        )

        login(request, user)
        return redirect('login')
    return render(request, "royhatdan otish.html")

def BlogView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Maqola.objects.create(
                sarlavha=request.POST.get('sarlavha'),
                sana=request.POST.get('data'),
                mavzu=request.POST.get('mavzu'),
                matn=request.POST.get('matn'),
                muallif=request.POST.get('muallif'),
                user=request.user
            )
            return redirect('blog')
        else:
            return redirect('login')

def All_BlogView(request):
    if request.user.is_authenticated:
        #maq = Maqola.objects.filter(user=request.user)
        m = Maqola.objects.all()
        return render(request, 'blog.html', {"maq": m})
    else:
        return redirect('login')


def MaqolaView(request, son):
    if request.user.is_authenticated:
        m = Maqola.objects.get(id=son)
        return render(request, "maqola.html", {"maq": m})


def LoGout(request):
    logout(request)
    return render(request, "login.html")
