from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 新建一张注册表单
        form = UserCreationForm()
    else:
        # 处理填写好了的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录,在重定向到主页
            authenticate_user = authenticate(username=new_user.username,
                                             password=request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)